# Formula Zynerji — Economic Modeling (pinning the cap & the floor)

The two keystone numbers — the **budget cap** (M1) and the **minimum-spend floor** (M12) — are pinned here from an explicit model rather than guessed. Reproduce with `python modeling/economy_model.py` (fixed seeds; outputs two plots in `modeling/`). Numbers are model-driven recommendations with stated assumptions, not ground truth.

---

## Part A — The cap: bottom-up cost build

**Method.** A triangular-distribution Monte-Carlo over the cost components of a *lean, shared-design* 2-car, 22-race program. The leanness is the point: F1's cost is inflated by secret *parallel* R&D (every team re-solving the same problems) and bloated logistics; forced disclosure (M10) lets you copy a solved problem instead, so design head-count is far lower. Driver and top-3 staff salaries are excluded from the cap. Five components are "running" (must-spend-to-exist; sharing barely cuts them); one is discretionary development.

**Results (per season, $M):**
- **Running-cost floor ≈ $56M** (personnel + manufacturing + powertrain + logistics + ops).
- **Competent-program total ≈ $67M** (P50; P10 $59M – P90 $75M).

**Cap recommendation: $75M.**
- ≈ **1.1× the competent program** and **1.35× the running floor** → a *bounded but real* development headroom of ~$19M. A tight cap (it genuinely constrains), which is what a meritocracy wants.
- Still **binds ~55%** of prospective entrants (those who would otherwise outspend it) → it compresses spend-driven advantage.
- It is also a **forcing function**: $75M is only feasible *with* the lean, sharing-enabled operating model — an F1-scale head-count cannot fit under it.
- *Tunable band: $70–80M.* Lower favours accessibility; higher loosens the constraint.

---

## Part B — The floor: an innovate-vs-copy game (the keystone)

**Method.** A repeated game: each season every team splits its development budget between **original innovation** (expensive, uncertain, *disclosed and copied next season*) and **execution/copying** (cheap — integrate the public pool). The private return to innovating is a one-season **head-start**; the public return (a faster-improving sport via the shared pool) is *not* captured by the innovator → classic public-goods under-provision. Teams myopically best-respond each season; the floor is a hard lower bound on original-R&D spend. We sweep the floor and measure vitality (how much the shared pace improves over 30 seasons), field compression, merit-correlation, and the innovation teams actually choose.

**Result 1 — the free-rider problem is real and large.** With **no floor**, teams self-select only **~13%** of their development budget on original R&D (the rest is copying/execution). The shared pool — i.e. the sport's progress — is starved. This empirically confirms the public-goods under-provision the whole design rests on, and is robust across the head-start sensitivity (7% → 20% as the private return rises). **Without the floor, innovation collapses; the floor is the keystone.**

**Result 2 — vitality rises monotonically with the floor; there is no internal knee.** Pace progress climbs steadily from ~9 (no floor) to ~21 (100% floor) with no plateau in range. **And merit-correlation (~0.97) and field-compression are essentially flat across the whole sweep** — copying keeps the field tight and meritocratic *regardless* of the floor. So the floor is a **pure vitality-vs-affordability lever**: more forced original-R&D → a more dynamic sport, at higher cost, with *no* downside to fairness or closeness.

**Floor recommendation:**
- **Minimum-spend floor = 80% of the cap (~$60M).** The cost model shows the *running floor is ~75% of the cap*, so a floor below that (e.g. the earlier 70% guess) **wouldn't bite** — every team already spends more just to exist. To force genuine *development* beyond bare running, the floor must sit just above running → **~80%.** This also yields a tight `[80%, 100%]` spend band → strong input-equalization.
- **Origination requirement ≈ half of the development spend must be original on-chain R&D.** Since vitality rewards a higher origination share with *no* fairness cost, this is a deliberately conservative floor (raisable) that preserves room for the copying/integration the accessibility case depends on. Per the model's mapping, ~half of development ≈ ~25–30% of the cap on declared-original work.

> **Honest caveat.** Because vitality is monotonic in the floor (no optimum), the floor number is a *judgment* balancing sport-vitality against accessibility and the value of allowing copying — not a sharp model optimum. The model's hard conclusions are the qualitative ones: (a) without a floor, innovation collapses to ~13%; (b) the floor must exceed the ~75%-of-cap running floor to bite; (c) the floor trades only against cost, never against merit or compression.

---

## Reproducibility & limitations

- `python modeling/economy_model.py` → prints this analysis and saves `cap_accessibility.png`, `floor_sweep.png`. Seeded; deterministic.
- The cost components are estimates for a lean formula; the game is stylized (myopic best-response, a one-season head-start, sqrt-diminishing innovation). Treat the **structure and qualitative findings** as the deliverable and the exact $/% as well-justified first-pass settings.
