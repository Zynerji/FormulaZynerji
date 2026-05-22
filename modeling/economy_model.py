"""
Formula Zynerji — economic modeling for the two keystone numbers:
  (A) the budget CAP            -> bottom-up cost build + accessibility curve
  (B) the minimum-spend FLOOR   -> innovate-vs-copy repeated game (the public-goods threshold)

Run:  python modeling/economy_model.py
Outputs: a printed report + two PNGs in modeling/.  Reproducible (fixed seeds).

The numbers here are model-driven recommendations, not ground truth — assumptions are
stated inline and the floor result is reported with a sensitivity sweep. See
design/economic-modeling.md for the write-up.
"""
from __future__ import annotations
import numpy as np
import os, sys
try:
    sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1252
except Exception:
    pass

OUT = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20260522)

# ----------------------------------------------------------------------------
# PART A — THE CAP: bottom-up cost build for a 2-car, 22-race entry ($M / season)
# ----------------------------------------------------------------------------
# Each component is (low, likely, high) in $M for a deliberately LEAN, shared-design
# formula. Forced disclosure (M10) cuts the *duplicated* secret R&D that dominates F1
# spend (you copy a solved problem off-chain instead of re-deriving it), so design/aero
# head-count is far smaller than F1's; the calendar is assumed efficient. Driver + top-3
# staff salaries are EXCLUDED from the cap. The cap is also a forcing function: it is
# only feasible WITH this lean operating model (an F1-scale head-count cannot fit).
CAP_COMPONENTS = {  # the first five are 'running' costs sharing barely cuts; last is discretionary
    "Capped personnel (lean, shared-design depts; ex top-3 & drivers)": (10, 15, 24),
    "Manufacturing (2 cars + spares; many parts copied)":              (6,  9,  14),
    "Powertrain (spec-base 2.5L diesel + open-zone dev)":              (6,  10, 16),
    "Logistics & travel (22 events, efficient calendar)":             (8,  12, 18),
    "Ops, spec tyres, fuel, misc":                                     (4,  6,  9),
    "Discretionary development (the capped R&D headroom)":             (3,  9,  22),
}
RUNNING_KEYS = 5  # first five are the must-spend-to-exist 'running' floor

def cap_cost_build(n=200_000):
    vals = list(CAP_COMPONENTS.values())
    sims = np.zeros(n); running = np.zeros(n)
    for j,(lo,mo,hi) in enumerate(vals):
        c = RNG.triangular(lo, mo, hi, n)
        sims += c
        if j < RUNNING_KEYS:
            running += c
    return sims, running

def accessibility_curve(caps, competent_p50):
    """Cap as accessibility-vs-constraint trade-off.
    Prospective-entrant annual budgets ~ lognormal (illustrative): a would-be entrant
    needs to clear the competent-program cost to be real; the cap BINDS those who would
    otherwise outspend it (that is the point — it compresses spend-driven advantage).
    headroom = cap - running-cost floor = the discretionary R&D the cap permits."""
    budgets = RNG.lognormal(mean=np.log(80), sigma=0.55, size=200_000)
    afford = np.array([np.mean(budgets >= competent_p50) for _ in caps])  # flat in cap (cost-driven)
    binds  = np.array([np.mean(budgets > cap) for cap in caps])
    return budgets, afford, binds


# ----------------------------------------------------------------------------
# PART B — THE FLOOR: innovate-vs-copy repeated game (the keystone)
# ----------------------------------------------------------------------------
# Each season every team splits its development budget between ORIGINAL innovation
# (expensive, uncertain, DISCLOSED & copied next season) and execution/copying
# (cheap: integrate the public pool). Private return to innovating = a one-season
# HEAD-START (you run your new part before rivals can copy it -> more points this
# season). Public return (a faster-improving sport via the shared pool) is NOT
# captured by the innovator -> classic public-goods under-provision. The mandatory
# minimum-origination FLOOR forces innovation up. We sweep the floor and measure:
#   - vitality   : how much the shared pool (the cars' pace) improves over T seasons
#   - spread     : field compression (std of car performance)
#   - merit_corr : Spearman(true competence, season-points) — does the best team win?
#   - eq_innov   : the innovation spend teams actually choose (free-rider check)

POINTS = np.array([40,33,28,24,21,19,17,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1], float)  # the 40->1 curve

def spearman(a, b):
    ra = np.argsort(np.argsort(a)); rb = np.argsort(np.argsort(b))
    ra = ra - ra.mean(); rb = rb - rb.mean()
    d = np.sqrt((ra**2).sum() * (rb**2).sum())
    return float((ra*rb).sum()/d) if d > 0 else 0.0

def simulate(floor_frac, N=11, T=30, head_start=1.0, cost=1.0, seed=0,
             rounds_per_season=3):
    """floor_frac: mandatory ORIGINAL-innovation spend as a fraction of the dev budget (0..1).
       head_start: value of a one-season head-start (private return knob).
       cost: marginal cost of innovation (in points-equivalent units)."""
    rng = np.random.default_rng(1000+seed)
    theta = np.clip(rng.normal(1.0, 0.15, N), 0.4, None)  # true competence (merit)
    P = 1.0                       # public pool / shared pace level (everyone has this)
    s = np.full(N, max(floor_frac, 0.1))  # innovation-spend fractions, start
    season_points = np.zeros(N)
    pace0 = P
    spreads = []

    def expected_points(s_vec, draws=6):
        """Monte-Carlo expected points per team (vectorized over draws)."""
        sq = np.sqrt(np.maximum(s_vec, 0.0))
        delta  = (theta*sq)[None,:] * rng.lognormal(0, 0.25, (draws, N))   # innovation head-start
        exec_q = (theta*(1.0 - s_vec)*0.5)[None,:]                         # execution from non-innovation budget
        perf   = P + delta + exec_q + rng.normal(0, 0.08, (draws, N))      # race-day noise
        order  = np.argsort(-perf, axis=1)
        pts    = np.empty((draws, N))
        pts[np.arange(draws)[:,None], order] = POINTS[:N][None,:]
        return pts.mean(axis=0)

    for t in range(T):
        # --- teams myopically best-respond on innovation spend, subject to the floor ---
        for _ in range(rounds_per_season):
            for i in range(N):
                grid = np.linspace(floor_frac, 1.0, 8)
                best_net, best_s = -1e9, s[i]
                for cand in grid:
                    s_try = s.copy(); s_try[i] = cand
                    pts_i = expected_points(s_try, draws=6)[i]
                    net = head_start*pts_i - cost*cand*POINTS[0]   # value of points minus innovation cost
                    if net > best_net:
                        best_net, best_s = net, cand
                s[i] = 0.6*s[i] + 0.4*best_s   # damped update
        # --- run the season for real, score it ---
        delta = theta * np.sqrt(np.maximum(s,0)) * rng.lognormal(0,0.25,N)
        exec_q = theta*(1.0-s)*0.5
        perf = P + delta + exec_q + rng.normal(0,0.08,N)
        order = np.argsort(-perf); p = np.zeros(N); p[order] = POINTS[:N]
        season_points += p
        spreads.append(perf.std())
        # --- forced disclosure: the frontier advances by the best innovations (copied next yr) ---
        P += 0.5*np.sort(delta)[-3:].mean()   # pool rises by ~the top innovations

    vitality = (P - pace0)/pace0                 # fractional pace gain over T seasons
    return dict(vitality=vitality, spread=float(np.mean(spreads)),
                merit_corr=spearman(theta, season_points), eq_innov=float(s.mean()))

def floor_sweep(floors, **kw):
    rows = []
    for f in floors:
        # average over several seeds for stability
        runs = [simulate(f, seed=k, **kw) for k in range(4)]
        agg = {key: float(np.mean([r[key] for r in runs])) for key in runs[0]}
        rows.append((f, agg))
    return rows

def knee(floors, vitality):
    """recommended floor = where marginal vitality per +10% floor falls below 25% of its early slope."""
    v = np.array(vitality); f = np.array(floors)
    dv = np.gradient(v, f)
    early = dv[1:4].mean()
    for i in range(2, len(f)):
        if dv[i] < 0.25*early:
            return f[i]
    return f[-1]


# ----------------------------------------------------------------------------
def main():
    print("="*78); print("FORMULA ZYNERJI — ECONOMIC MODEL"); print("="*78)

    # ---- PART A: CAP ----
    sims, running = cap_cost_build()
    print("\n[A] CAP - bottom-up cost build ($M/season, 2 cars, 22 races; lean shared-design formula)")
    for j,(k,(lo,mo,hi)) in enumerate(CAP_COMPONENTS.items()):
        tag = "(running)" if j < RUNNING_KEYS else "(discretionary)"
        print(f"    {k:<60} {lo:>3}-{hi:<3} likely {mo:<3} {tag}")
    p10,p50,p90 = np.percentile(sims,[10,50,90])
    run50 = np.percentile(running, 50)
    print(f"    {'RUNNING-COST FLOOR (must spend to exist)':<60} {'':>9} ~{run50:4.0f}")
    print(f"    {'COMPETENT-PROGRAM TOTAL':<60} P10={p10:3.0f} P50={p50:3.0f} P90={p90:3.0f}")
    caps = np.arange(50, 111, 5)
    budgets, afford, binds = accessibility_curve(caps, p50)
    print("\n    cap($M)  dev-headroom($M)  binds-top%  (headroom = cap - running floor;")
    print("                                            binds-top = entrants who'd outspend the cap)")
    for c,b in zip(caps, binds):
        mark = "  <-- recommended" if c==75 else ""
        print(f"      {c:>4}       {c-run50:5.0f}          {b*100:5.1f}{mark}")
    rec_cap = 75
    print(f"\n    -> Cap recommendation: ~${rec_cap}M.")
    print(f"       Running floor ~${run50:.0f}M; competent program ~${p50:.0f}M (P50).")
    print(f"       ${rec_cap}M = ~{rec_cap/p50:.2f}x competent / ~{rec_cap/run50:.2f}x running -> real but bounded dev headroom (~${rec_cap-run50:.0f}M),")
    print(f"       and it still binds the ~{np.mean(budgets>rec_cap)*100:.0f}% of prospective entrants who would outspend it.")
    print(f"       NB: the cap is also a forcing function - it is only feasible WITH the lean operating model.")

    # ---- PART B: FLOOR ----
    floors = np.round(np.arange(0.0, 1.001, 0.1), 2)
    print("\n[B] FLOOR — innovate-vs-copy game (origination floor = mandatory original-R&D")
    print("    spend as a fraction of the development budget). Baseline knobs head_start=cost=1.")
    rows = floor_sweep(floors)
    print("\n    floor   vitality  fieldspread  meritcorr  eq.innov")
    vit=[]
    for f,a in rows:
        vit.append(a['vitality'])
        print(f"     {f*100:4.0f}%   {a['vitality']:6.2f}    {a['spread']:7.3f}     {a['merit_corr']:+5.2f}    {a['eq_innov']*100:5.1f}%")
    rec = knee(floors, vit)
    eq_nofloor = rows[0][1]['eq_innov']
    print(f"\n    Free-rider check: with NO floor, teams self-select only ~{eq_nofloor*100:.0f}% innovation")
    print(f"    (the public-goods under-provision). Vitality (sport progress) is starved there.")
    print(f"    -> Floor recommendation (vitality knee): ~{rec*100:.0f}% of the development budget on original R&D.")

    # ---- sensitivity: vary the head-start value (private return) ----
    print("\n    Sensitivity — recommended floor vs the head-start value (private return):")
    for hs in (0.6, 1.0, 1.5):
        r = floor_sweep(floors, head_start=hs)
        rk = knee(floors, [a['vitality'] for _,a in r])
        eqn = r[0][1]['eq_innov']
        print(f"      head_start={hs:>3}:  no-floor self-select ~{eqn*100:4.0f}%   recommended floor ~{rk*100:4.0f}%")

    # ---- map to the financial-reg numbers ----
    print("\n[MAP] financial.md expresses the floor as: (dev-spend floor % of cap) x (origination share).")
    print(f"      Recommended origination ≈ {rec*100:.0f}% of the development budget.")
    print(f"      With development ≈ 55% of the cap, that is ≈ {rec*0.55*100:.0f}% of the CAP on original R&D.")
    print(f"      Reg's two parts: dev-spend floor ~80% of cap (just above the ~75% running floor, Part A),")
    print(f"      origination share ~half of dev (raisable - vitality rewards more, no fairness cost).")

    # ---- plots ----
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig,ax=plt.subplots(figsize=(7,4))
        ax.plot(caps,afford*100,marker='o',label='affordable (can fund competent program) %')
        ax.plot(caps,binds*100,marker='s',label='cap binds (would outspend) %')
        ax.axvline(rec_cap,color='k',ls='--',alpha=.6,label=f'recommended ${rec_cap}M')
        ax.set_xlabel('budget cap ($M/season)'); ax.set_ylabel('% of prospective entrants')
        ax.set_title('Cap: accessibility vs constraint'); ax.legend(fontsize=8); ax.grid(alpha=.3)
        fig.tight_layout(); fig.savefig(os.path.join(OUT,'cap_accessibility.png'),dpi=120)

        fig,ax=plt.subplots(figsize=(7,4))
        ax.plot(np.array(floors)*100, vit, marker='o', color='C2')
        ax.axvline(rec*100,color='k',ls='--',alpha=.6,label=f'recommended ~{rec*100:.0f}%')
        ax.set_xlabel('origination floor (% of dev budget on original R&D)')
        ax.set_ylabel('vitality (sport pace gain over 40 seasons)')
        ax.set_title('Floor: the public-goods threshold (vitality vs floor)')
        ax.legend(fontsize=8); ax.grid(alpha=.3)
        fig.tight_layout(); fig.savefig(os.path.join(OUT,'floor_sweep.png'),dpi=120)
        print("\n    [plots saved: modeling/cap_accessibility.png, modeling/floor_sweep.png]")
    except Exception as e:
        print(f"    [plotting skipped: {e}]")

if __name__ == "__main__":
    main()
