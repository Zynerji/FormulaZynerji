"""Formula Zynerji — the M4 dirty-air externality-pricing schedule, made concrete.

A car that chases maximum own-downforce tends to shed a dirtier wake, which destroys the
following car's downforce and so destroys overtaking. That loss is an externality: the cost
lands on racing, not on the team that caused it. M4 prices it. At the design stage each car's
CFD reports (a) its own peak downforce and (b) the downforce a standard follower retains in its
wake at a reference gap (wake cleanliness W). The legal downforce allowance is then scaled by W:
a clean wake keeps its full allowance, a dirty wake is docked. The privately-optimal design
therefore moves to a cleaner wake -- raceability bought without Balance-of-Performance and
without DRS.

  python modeling/aero_dirty_air.py  ->  modeling/aero_dirty_air.{pdf,svg,png} + printed numbers

Published anchors (orders of magnitude, FIA / Pat Symonds public figures):
  * 2017-21-generation cars: a follower lost ~35% downforce at ~20 m and ~47% at ~10 m.
  * 2022 ground-effect rules cut that to ~4% at 20 m and ~18% at 10 m.
The frontier W(x) and the allowance schedule g(W) below are an illustrative calibration; the
mechanism (and the direction of the equilibrium shift) is the point, not the exact constants.
"""
import sys, numpy as np
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
INK="#1b2430"; ACC="#b3122b"; BLUE="#1f6fb2"; MUT="#7a8694"; GREEN="#1e7d4f"; GOLD="#9a7d18"

GAP_REF = 10.0           # reference following gap for the wake metric, m
W_CLEAN = 0.85           # retention at/above which no allowance is docked

# --- design frontier: own-downforce up, wake cleanliness down (diminishing / convex) ---
x = np.linspace(1.0, 1.30, 301)              # design aggression (own downforce, normalised)
DF_own = 1.0 + 0.30*((x-1.0)/0.30)**0.7      # concave gain, +30% at the aggressive end
W      = 0.88 - 0.33*((x-1.0)/0.30)**1.5     # retention@10m: 0.88 (clean) -> 0.55 (dirty)

# --- M4 allowance schedule: keep full allowance if clean, docked if dirty (capped at 1) ---
def g_allow(w):  return np.clip(w/W_CLEAN, 0.0, 1.0)
DF_legal = DF_own * g_allow(W)               # downforce a team may actually run under M4

i_unpriced = int(np.argmax(DF_own))          # no M4: chase raw downforce -> dirtiest end
i_m4       = int(np.argmax(DF_legal))        # with M4: maximise legal downforce -> interior
W_unpriced, W_m4 = W[i_unpriced], W[i_m4]

print(f"""
FORMULA ZYNERJI — M4 DIRTY-AIR PRICING (illustrative calibration)
  reference gap ............ {GAP_REF:.0f} m ; full-allowance threshold W >= {W_CLEAN:.2f}
  UNPRICED optimum ......... design x={x[i_unpriced]:.2f}, own-DF {DF_own[i_unpriced]:.2f},
                             follower retention W={W_unpriced:.2f}  -> {(1-W_unpriced)*100:.0f}% loss (poor racing)
  M4-PRICED optimum ........ design x={x[i_m4]:.2f}, own-DF {DF_own[i_m4]:.2f},
                             legal-DF {DF_legal[i_m4]:.2f}, retention W={W_m4:.2f} -> {(1-W_m4)*100:.0f}% loss
  EFFECT ................... equilibrium follower retention {W_unpriced:.2f} -> {W_m4:.2f}
                             (+{(W_m4-W_unpriced)*100:.0f} pts), at {(1-DF_legal[i_m4]/DF_own[i_unpriced])*100:.0f}% less realised downforce
""")

# --- wake decay vs gap for the two resulting designs (illustrative shape, anchored at 10 m) ---
def retention(gap, W10, tau=18.0):
    return 1.0 - (1.0 - W10)*np.exp(-(gap - GAP_REF)/tau)
gaps = np.linspace(2, 40, 200)

fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.5, 4.4))

# Panel A: follower downforce vs gap
axA.plot(gaps, retention(gaps, W_unpriced)*100, color=ACC, lw=2.2,
         label=f"dirty wake (unpriced opt., W={W_unpriced:.2f})")
axA.plot(gaps, retention(gaps, W_m4)*100, color=GREEN, lw=2.2,
         label=f"clean wake (M4 opt., W={W_m4:.2f})")
axA.axvline(GAP_REF, color=MUT, ls=":", lw=1); axA.text(GAP_REF+0.4, 30, "metric gap\n10 m", fontsize=7.5, color=MUT)
# published anchors at 10 m
axA.plot([GAP_REF],[53], "o", color="#444", ms=6); axA.text(GAP_REF+0.6,53,"2017–21 (~47% loss)",fontsize=7,color="#444",va="center")
axA.plot([GAP_REF],[82], "s", color="#444", ms=6); axA.text(GAP_REF+0.6,82,"2022 (~18% loss)",fontsize=7,color="#444",va="center")
axA.set_xlabel("gap to car ahead (m)"); axA.set_ylabel("follower downforce retained (%)")
axA.set_xlim(2,40); axA.set_ylim(20,100); axA.legend(fontsize=7.5, loc="lower right", frameon=False)
axA.set_title("The externality: wake kills the follower's downforce", fontsize=10, color=INK, loc="left")

# Panel B: design tradeoff with/without M4
axB.plot(x, DF_own, color=BLUE, lw=2.2, label="own downforce (what a team chases)")
axB.plot(x, DF_legal, color=GREEN, lw=2.4, label="legal downforce under M4")
axB.plot([x[i_unpriced]],[DF_own[i_unpriced]],"o",color=ACC,ms=8)
axB.annotate(f"unpriced opt.\n(dirty, W={W_unpriced:.2f})", (x[i_unpriced],DF_own[i_unpriced]),
             (x[i_unpriced]-0.05, DF_own[i_unpriced]-0.16), fontsize=8, color=ACC, ha="center",
             arrowprops=dict(arrowstyle="-|>",color=ACC,lw=.9))
axB.plot([x[i_m4]],[DF_legal[i_m4]],"o",color=GREEN,ms=8)
axB.annotate(f"M4 opt.\n(clean, W={W_m4:.2f})", (x[i_m4],DF_legal[i_m4]),
             (x[i_m4]+0.085, DF_legal[i_m4]-0.16), fontsize=8, color=GREEN, ha="center",
             arrowprops=dict(arrowstyle="-|>",color=GREEN,lw=.9))
axW = axB.twinx()
axW.plot(x, W, color=GOLD, lw=1.4, ls="--")
axW.axhline(W_CLEAN, color=GOLD, ls=":", lw=0.9)
axW.text(1.297, W_CLEAN+0.006, "full-allowance threshold", fontsize=6.8, color=GOLD, ha="right", va="bottom")
axW.set_ylabel("wake cleanliness W, retention@10 m  (- - gold)", color=GOLD); axW.tick_params(axis="y", labelcolor=GOLD)
axW.set_ylim(0.45, 0.95)
axB.set_xlabel("design aggression  →  (own downforce)"); axB.set_ylabel("downforce (normalised)")
axB.set_xlim(1.0,1.30); axB.set_ylim(0.7, 1.35); axB.legend(fontsize=7.5, loc="lower left", frameon=False)
axB.set_title("M4 moves the privately-optimal design to a cleaner wake", fontsize=10, color=INK, loc="left")

fig.suptitle("FORMULA ZYNERJI — M4 DIRTY-AIR EXTERNALITY PRICING (clean wake → more downforce allowance)",
             fontsize=11.5, fontweight="bold", color=INK, x=0.02, ha="left")
fig.tight_layout(rect=[0,0.02,1,0.95])
import os; OUT=os.path.dirname(os.path.abspath(__file__))
for e in ("pdf","svg"): fig.savefig(os.path.join(OUT,"aero_dirty_air."+e), bbox_inches="tight")
fig.savefig(os.path.join(OUT,"aero_dirty_air.png"), dpi=150, bbox_inches="tight"); plt.close(fig)
print("saved modeling/aero_dirty_air.{pdf,svg,png}")
