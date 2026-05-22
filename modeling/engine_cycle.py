"""Formula Zynerji — first-principles derivation of the engine's headline numbers.

Derives BMEP (and hence power/torque) of the 2.5 L I5 two-stroke uniflow diesel from a
boost + energy balance, rather than asserting it: supercharger pressure ratio -> intercooled
charge density -> trapped air per cycle -> fuel burned at the smoke-limited air/fuel ratio ->
indicated work at the brake thermal efficiency -> BMEP. A positive-displacement (screw) blower
gives a roughly RPM-flat boost, so the torque curve is shaped by the uniflow trapping efficiency
falling at high rpm; power then peaks near the 7000 rpm ceiling.

  python modeling/engine_cycle.py  ->  modeling/engine_curve.{pdf,svg,png} + printed spec block

References / sanity anchors (orders of magnitude, not exact):
  * heavy-duty boosted diesels reach ~24-28 bar BMEP; this is a purpose-built racing unit.
  * best diesel BSFC ~190 g/kWh corresponds to ~44% brake thermal efficiency.
  * mean piston speed ~20 m/s is below current F1 (~25 m/s) -> 7000 rpm is mechanically sane.
"""
import sys, numpy as np
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
INK="#1b2430"; ACC="#b3122b"; BLUE="#1f6fb2"; MUT="#7a8694"; GREEN="#1e7d4f"

# ---------------- fixed design inputs ----------------
Vd      = 2.5e-3        # total swept volume, m^3
n_cyl   = 5
N_max   = 7000.0        # rev ceiling, rpm
Q_LHV   = 43.0e6        # JP-8/e-kerosene lower heating value, J/kg
AFR_st  = 14.7          # stoichiometric air/fuel for kerosene
lam     = 1.30          # excess-air ratio (lean, smoke-limited CI) -> trapped AFR = lam*AFR_st
eta_bt  = 0.44          # brake thermal efficiency (-> ~190 g/kWh BSFC)
eta_tr0 = 0.90          # peak uniflow trapping (delivery) efficiency
N_tpk   = 4200.0        # rpm of peak trapping
tr_fall = 0.012         # trapping fall-off coefficient per (krpm offset)^2
R, gam  = 287.0, 1.40   # air gas constant, ratio of specific heats
p0, T0  = 1.013e5, 298.0
eta_c   = 0.72          # supercharger isentropic efficiency (good high-helix screw)
eps_ic  = 0.82          # intercooler effectiveness (race water-to-air core)
T_cool  = 313.0         # coolant-side temperature for the intercooler, K
dp_loss = 0.96          # intake pressure-recovery factor after IC/plenum

AFR_tr = lam * AFR_st

def charge_density(PR):
    """Intercooled charge density (kg/m^3) for supercharger pressure ratio PR."""
    T2 = T0 * (1.0 + ((PR**((gam-1)/gam)) - 1.0)/eta_c)   # after compressor
    T3 = T2 - eps_ic*(T2 - T_cool)                        # after intercooler
    p3 = PR * p0 * dp_loss                                # manifold pressure
    return p3/(R*T3), T2, T3, p3

def bmep_from_density(rho, eta_tr):
    """BMEP (Pa) from trapped charge density and trapping efficiency."""
    m_air  = rho * Vd * eta_tr          # trapped air per cycle (whole engine)
    m_fuel = m_air / AFR_tr             # fuel per cycle at the lean limit
    W      = eta_bt * m_fuel * Q_LHV    # brake work per cycle
    return W/Vd, m_fuel

def trapping(N):
    return eta_tr0 - tr_fall*((N - N_tpk)/1000.0)**2

# ---- solve the boost ratio that yields 26 bar BMEP at the rev ceiling ----
target_bmep = 26.0e5
eta_tr_ceil = trapping(N_max)
# bisection on PR
lo, hi = 1.2, 4.5
for _ in range(80):
    mid = 0.5*(lo+hi)
    rho,_,_,_ = charge_density(mid)
    b,_ = bmep_from_density(rho, eta_tr_ceil)
    if b < target_bmep: lo = mid
    else: hi = mid
PR_op = 0.5*(lo+hi)
rho_op, T2, T3, p3 = charge_density(PR_op)

# ---------------- curves over the rev range ----------------
N = np.linspace(1500, N_max, 200)
eta_tr_N = trapping(N)
bmep_N   = np.array([bmep_from_density(rho_op, e)[0] for e in eta_tr_N])   # Pa
torque_N = bmep_N * Vd / (2*np.pi)                                          # N·m (2-stroke: 1 fire/rev)
power_N  = bmep_N * Vd * (N/60.0)                                           # W

i_pp = int(np.argmax(power_N)); i_pt = int(np.argmax(torque_N))
P_peak, N_Ppk = power_N[i_pp], N[i_pp]
T_peak, N_Tpk = torque_N[i_pt], N[i_pt]
P_ceil, T_ceil, bmep_ceil = power_N[-1], torque_N[-1], bmep_N[-1]

# ---------------- geometry & consumption sanity ----------------
Vcyl = Vd/n_cyl
bore = (4*Vcyl/np.pi)**(1/3.0)            # square engine (bore = stroke)
stroke = bore
piston_speed = 2*stroke*(N_max/60.0)      # mean piston speed at ceiling, m/s
m_fuel_cyc = bmep_from_density(rho_op, eta_tr_ceil)[1]
fuel_rate_ceil = m_fuel_cyc*(N_max/60.0)  # kg/s at ceiling (2-stroke: cycles/s = rev/s)
bsfc = fuel_rate_ceil/(P_ceil/1000.0)*3600.0*1000.0   # g/kWh
race_kg, race_min = 80.0, 90.0
avg_kW = race_kg/(race_min/60.0)/bsfc*1000.0          # avg power supported by 80 kg over 90 min

def fmt(): return f"""
FORMULA ZYNERJI — ENGINE CYCLE (first-principles)
  swept volume ............ {Vd*1e3:.2f} L ({n_cyl} cyl, {Vcyl*1e6:.0f} cc each)
  bore x stroke (square) .. {bore*1e3:.1f} x {stroke*1e3:.1f} mm
  mean piston speed @ ceil  {piston_speed:.1f} m/s   (F1 ~25; truck ~12)
  fuel / AFR .............. JP-8 LHV {Q_LHV/1e6:.0f} MJ/kg, lambda {lam:.2f} (trapped AFR {AFR_tr:.1f})
  brake thermal eff ....... {eta_bt*100:.0f} %   -> BSFC {bsfc:.0f} g/kWh
  required boost (screw) .. PR {PR_op:.2f}  ({(p3-p0)/1e5:.2f} bar gauge); manifold {p3/1e5:.2f} bar abs
    compressor-out temp ... {T2-273.15:.0f} C  -> intercooled to {T3-273.15:.0f} C
    charge density ........ {rho_op:.3f} kg/m^3  ({rho_op/(p0/(R*T0)):.2f}x ambient)
  PEAK TORQUE ............. {T_peak:.0f} N·m @ {N_Tpk:.0f} rpm   (BMEP {bmep_N[i_pt]/1e5:.1f} bar)
  PEAK POWER .............. {P_peak/1e3:.0f} kW ({P_peak/745.7:.0f} hp) @ {N_Ppk:.0f} rpm
  AT 7000 rpm CEILING ..... {P_ceil/1e3:.0f} kW ({P_ceil/745.7:.0f} hp), {T_ceil:.0f} N·m, BMEP {bmep_ceil/1e5:.1f} bar
  power-to-weight ......... {P_peak/1e3/605.0:.2f} kW/kg at 605 kg
  race fuel check ......... 80 kg over 90 min supports ~{avg_kW:.0f} kW avg ({avg_kW/(P_peak/1e3)*100:.0f}% of peak)
"""
print(fmt())

# ---------------- figure: performance map + boost derivation ----------------
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 4.4))

# left: torque & power vs rpm
axL.plot(N, torque_N, color=INK, lw=2.2, label="brake torque (N·m)")
axL.set_xlabel("engine speed (rpm)"); axL.set_ylabel("torque (N·m)", color=INK)
axL.tick_params(axis="y", labelcolor=INK)
axL.set_ylim(0, T_peak*1.18); axL.set_xlim(1500, N_max)
axL.axvline(N_max, color=MUT, ls=":", lw=1)
axL.annotate(f"{T_peak:.0f} N·m\n@ {N_Tpk:.0f}", (N_Tpk, T_peak), (N_Tpk-1200, T_peak*0.74),
             fontsize=8, color=INK, ha="center", arrowprops=dict(arrowstyle="-", color=MUT, lw=.7))
axP = axL.twinx()
axP.plot(N, power_N/1000.0, color=ACC, lw=2.2, label="brake power (kW)")
axP.set_ylabel("power (kW)", color=ACC); axP.tick_params(axis="y", labelcolor=ACC)
axP.set_ylim(0, P_peak/1000.0*1.18)
axP.annotate(f"{P_peak/1000:.0f} kW / {P_peak/745.7:.0f} hp\n@ {N_Ppk:.0f}", (N_Ppk, P_peak/1000),
             (N_Ppk-1700, P_peak/1000*0.66), fontsize=8, color=ACC, ha="center",
             arrowprops=dict(arrowstyle="-", color=ACC, lw=.7))
axL.set_title("Performance map (screw-blown, flat boost)", fontsize=10, color=INK, loc="left")
axL.text(0.02, -0.20, "2-stroke: one power stroke per revolution; torque shaped by uniflow trapping efficiency.",
         transform=axL.transAxes, fontsize=7.5, color=MUT)

# right: BMEP vs boost PR, operating point
PRs = np.linspace(1.2, 4.0, 120)
bmep_PR = np.array([bmep_from_density(charge_density(pr)[0], eta_tr_ceil)[0] for pr in PRs])/1e5
axR.plot(PRs, bmep_PR, color=BLUE, lw=2.2)
axR.axhline(26, color=ACC, ls="--", lw=1.2); axR.axvline(PR_op, color=ACC, ls="--", lw=1.2)
axR.plot([PR_op], [26], "o", color=ACC, ms=7)
axR.annotate(f"operating point\nPR {PR_op:.2f} -> 26 bar", (PR_op, 26), (PR_op+0.15, 14),
             fontsize=8, color=ACC, arrowprops=dict(arrowstyle="-|>", color=ACC, lw=.9))
axR.set_xlabel("supercharger pressure ratio"); axR.set_ylabel("BMEP at ceiling (bar)")
axR.set_xlim(1.2, 4.0); axR.set_ylim(0, bmep_PR.max()*1.05)
axR.set_title("Boost needed for 26 bar BMEP", fontsize=10, color=INK, loc="left")
axR.text(0.02, -0.20, f"intercooled (eff {eps_ic:.2f}), brake thermal eff {eta_bt*100:.0f}%, lambda {lam:.2f}.",
         transform=axR.transAxes, fontsize=7.5, color=MUT)

fig.suptitle("FORMULA ZYNERJI — 2.5 L I5 TWO-STROKE UNIFLOW DIESEL: cycle derivation",
             fontsize=12, fontweight="bold", color=INK, x=0.02, ha="left")
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
import os; OUT=os.path.dirname(os.path.abspath(__file__))
for e in ("pdf","svg"): fig.savefig(os.path.join(OUT,"engine_curve."+e), bbox_inches="tight")
fig.savefig(os.path.join(OUT,"engine_curve.png"), dpi=150, bbox_inches="tight"); plt.close(fig)
print("saved modeling/engine_curve.{pdf,svg,png}")
