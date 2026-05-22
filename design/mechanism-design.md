# Formula Zynerji — The Mechanism-Design Framework

The engine room. `philosophy.md` says **why** (meritocracy); this says **how** (the mechanisms) and **why each one is incentive-compatible**. Every rule in `regulations/` should trace back to a mechanism here.

> **The spine.** Mechanisms **M10 (forced on-chain disclosure)** and **M11 (the innovation incentive)** — see `design/blockchain-architecture.md` — are not just two more entries; the blockchain is the **spine** the rest hang on. Forced disclosure converts R&D from a private good into a club good, which collapses equilibrium spend and dissolves dynasties at the source. Because the field **self-balances by copying**, the artificial balancing machinery — **M2 (development auction/tokens) and M3 (success handicap) — has been removed (v0.5.0)**; the economy needs no currency. The one thing that *must* stay is **M12 (the minimum-spend floor)**, which forces continuous innovation and so prevents the only bad equilibrium (everyone copies, nobody innovates). See `regulations/financial.md` Art. 3.

---

## 1. The objective, formally

Let **M** = the true merit ordering of teams/drivers (unobservable). Let **S** = the season standings (observed). Meritocracy is:

> maximize the rank-correlation between **S** and **M**, subject to (a) the **safety invariant** — never traded — and (b) a **participation/entertainment floor** that keeps teams entering and fans watching.

Decompose the error:

```
S = M + Luck + Budget-bias + Gaming-bias
```

Each rule is an intervention on one of those error terms. A rule that doesn't measurably shrink one of them — or that shrinks one while inflating another — is rejected. This is the test the whole rulebook is held to.

---

## 2. Design razors (the rules for writing rules)

| # | Razor | Game-theory basis |
|---|-------|-------------------|
| **R1** | Design for the **equilibrium**, not the intent. Ask "what will a rational team actually do?" before "what do we want?" | Nash equilibrium |
| **R2** | **Embrace skill-variance; suppress luck-variance.** | Estimator variance decomposition |
| **R3** | **Equalize inputs, never outputs.** Cap money; never add weight/cut power to slow a fast car. | Why we reject BoP |
| **R4** | **Handicap future inputs, never current performance.** Dynasty prevention that doesn't invert merit. | Dynamic mechanism / handicapping |
| **R5** | Make **honesty and maximum effort a dominant strategy.** Anti-sandbag, anti-tank. | Incentive compatibility / strategy-proofness |
| **R6** | **Price externalities; don't prescribe around them.** | Pigouvian taxation > command-and-control |
| **R7** | **Assume Goodhart.** Every metric becomes a target and degrades. Prefer hard-to-game proxies + randomized audits. | Goodhart's law / measurement gaming |
| **R8** | **Use revealed history.** If teams gamed a similar rule before, they will again. | Revealed preference |
| **R9** | Mind the **principal–agent information gap.** Teams hold private info (true spend, true pace); design for monitoring, not trust. | Principal–agent / mechanism with private types |

The recurring failure of real F1 regulation is violating R1 and R6: prescribing the *intended* geometry (which teams then lawyer) instead of pricing the *outcome* we care about. The recurring success (cost cap, ATR, penalty points) is implicitly applying R3/R4/R5.

---

## 3. The mechanism catalog

Each entry: **Distortion targeted · Problem (history + theory) · Mechanism · Incentive analysis · Failure modes & guards · Parameters (TODO).** Mapped to a regulation file at the end.

### M1 — Money-neutral hard cap
- **Targets:** Budget-bias.
- **Problem:** Pre-2021 F1 was a Tullock contest — teams dissipated up to $400M/yr in rent-seeking R&D, and results tracked spend (history). F1's 2021 cap helped (McLaren's rise) but leaks via the luxury-tax temptation and exclusions.
- **Mechanism:** A single **hard, equal** budget cap. No luxury-tax overspend lane (a soft cap re-admits money as a performance lever — fatal for a *meritocracy* objective). Broad positive cost definition + explicit exclusions (R7).
- **Incentive analysis:** With money equalized, the marginal championship point is bought with *quality of decision*, not dollars — exactly the merit signal we want to amplify.
- **Failure modes & guards:** Hidden spend via related parties (→ M9); exclusions abused (→ keep the excluded list short and bright-line). 
- **Parameters:** cap value; inclusion/exclusion lists; indexation. *TODO.*

### M2 — Development-resource auction (tokens) — **REMOVED (v0.5.0)**
> **Status: not adopted.** Development is limited by **money alone** (the M1 cap); there is no token endowment, auction, or ATR sliding scale. With forced disclosure the field self-balances by copying, so a separate development-rationing currency is unnecessary (`financial.md` Art. 3). The "prioritization merit" it rewarded is still rewarded — through *results* (and the output is copied anyway), without a currency.

### M3 — Merit-weighted handicapping — **REMOVED (v0.5.0)**
> **Status: not adopted.** The dynasty problem is solved by the **self-balancing economy** (`financial.md` Art. 3.1): a leader's advantage is continuously *copied away*, so the field stays compressed and no one runs off — without ever handicapping a fast car. No success handicap exists.

### M4 — Dirty-air externality pricing
- **Targets:** the sport's central **negative externality**; enables merit-based overtaking; lets us delete DRS.
- **Problem:** Each team rationally maximizes its own downforce; collectively this fills the track with turbulent wake that prevents the following car from racing — a **tragedy of the commons**. Real F1 attacks it by *prescribing* wake-friendly geometry (2022 ground-effect rules) — command-and-control that teams immediately lawyer back toward outwash, and it bolts on DRS as a patch.
- **Mechanism:** In a standard test, **measure each car's wake / dirty-air footprint** at a reference following distance. **Price it as a design-stage downforce allowance** (no tokens — v0.5.0): a car that produces more downforce-destroying turbulence is permitted *less* downforce (a smaller reference-volume / downforce ceiling) at homologation; a clean-wake car may run *more*. So clean wake literally buys downforce. It is set at design/homologation (an **input**, never changed during the race) so it is not BoP (R3).
- **Incentive analysis:** Internalizes the externality (R6). Rewards the *harder* engineering of clean-wake downforce — a real merit dimension — and restores close following so on-track passes reflect merit, not a DRS button.
- **Failure modes & guards:** Test must be reproducible and hard to overfit (R7) — define the rig and the metric precisely; randomize test conditions. Keep the price **input-side** (design-stage allowance), never an in-race adjustment (R3).
- **Parameters:** wake metric + rig; following distance; the wake→downforce-allowance schedule. *TODO — `regulations/technical.md` Art. 3.*

### M5 — Luck-suppressing neutralization  — **REMOVED (v0.4.1)**
> **Status: not adopted.** A design decision was taken to use **conventional safety-car / VSC procedures** (`sporting.md` Art. 7) instead of engineered time-neutral neutralization. The series accepts ordinary safety-car variance as part of racing; merit is carried by inputs + the long calendar + the DMI, not output-side correction. The rationale below is retained for the record.
- **Targets:** Luck — the largest single injector in F1.
- **Problem:** A full safety car is a luck bomb: it gifts a near-free pit stop to whoever hasn't stopped, erases earned leads, and bunches the field. That's pure noise added to the estimator (R2). Reliability DNFs, by contrast, are *merit-relevant* (building a robust car is engineering merit) and stay.
- **Mechanism:** Default to **gap-preserving neutralization** (VSC-style delta) so positions and *earned time gaps* are conserved. When a physical intervention is unavoidable, apply a **time-credit / pit-stop-equivalence** system that normalizes the pit-time advantage a neutralization would otherwise gift, so a leader doesn't lose an earned lead to timing luck.
- **Incentive analysis:** Removes a large luck term without touching skill-variance. Wet weather, strategy, and tyre management — all skill — remain fully in play.
- **Failure modes & guards:** Over-engineering neutralization can confuse fans/teams — keep the rule legible. Edge cases (genuinely needing to bunch for safety) defer to the safety invariant.
- **Parameters:** time-credit formula; when physical SC overrides. *TODO — `regulations/sporting.md` Art. 7.*

### M6 — Championship-estimator design
- **Targets:** Luck, measurement bias.
- **Problem:** The points system *is* the estimator's weighting function. F1's choices add noise or gaming surface: the fastest-lap point (gamed, abolished 2025), sprint points (extra variance), a steep top-10 curve that ignores field strength.
- **Mechanism:** Tune the estimator for signal-to-noise:
  - **Points curve** chosen for discrimination across the field, not just the podium. **(Adopted — `sporting.md` Art. 5.1.)**
  - **No fastest-lap bonus, no sprint points** unless they survive the signal/noise test. **(Adopted.)**
  - ~~**Drop-results**~~ — **REMOVED (v0.4.1):** every round counts; variance is handled by the long 22-round sample instead of trimming worst results.
  - ~~**Field-strength weighting**~~ — **not used for points** (a no-op within a constant-field season); lives only in the DMI model (M7).
- **Incentive analysis:** A better estimator = standings closer to merit, by construction. Drop-results specifically protect a great season from one freak event (R2).
- **Failure modes & guards:** Drop-results can blunt incentive in dead-rubber rounds (mild); field-strength weighting adds complexity (keep it transparent or shelve).
- **Parameters:** points vector; N-of-K; whether to weight field strength. *TODO — `regulations/sporting.md` Art. 5.*

### M7 — Driver-merit disentanglement
- **Targets:** measurement — the hardest one: *was it the car or the driver?*
- **Problem:** The Drivers' title is badly confounded by machinery. The best driver in the 4th-best car cannot win it, so the championship mis-measures driver merit.
- **Mechanism:** Make the **teammate comparison** (same machinery, the cleanest controlled experiment in the sport) the *primary* driver-merit signal, and publish an **official driver-merit rating** built from a mixed-effects / Bayesian model that separates a car effect from a driver effect across all teammate pairings and conditions.
- **Incentive analysis:** Directly attacks the car/driver confound — the single biggest measurement bias in the Drivers' standings.
- **Failure modes & guards:** A rating is itself a mechanism and can be gamed (team orders, sandbagging a teammate). **Key design decision:** keep the rating **advisory** (a published classification / tie-breaker input) rather than **binding** (the actual title), to avoid corrupting team behaviour. → flagged as an open decision.
- **Parameters:** model spec; advisory vs binding; how/if it feeds the title. *TODO — `regulations/sporting.md` Art. 1 & 5.*

### M8 — Anti-gaming sporting rules
- **Targets:** Gaming, plus residual Luck (order effects).
- **Problem:** Qualifying track-evolution gives later runners a luck advantage; track limits invite lawyering; parc-fermé scope trades cost vs setup-merit.
- **Mechanism:** define **hard, sensor-measured** track limits (no judgement gaming, R7) **(adopted)**; set parc-fermé scope to reward *setup merit* while curbing overnight-rebuild spend **(adopted)**. ~~Qualifying order-effect (track-evolution) correction~~ — **REMOVED (v0.4.1):** standard knockout qualifying on raw times; reading track evolution is treated as qualifying craft.
- **Parameters:** quali format; track-limit sensing; parc-fermé scope. *TODO — `regulations/sporting.md` Art. 3, 4, 6.*

### M9 — Robust cost monitoring
- **Targets:** Gaming, principal–agent.
- **Problem:** The cap's biggest hole is **related-party transactions** and private spend info (R9). F1 patched related-party pricing mid-cycle; the audit lag was ~12 months (a full season of advantage).
- **Mechanism:** Related-party transfers priced at a declared market-consistent standard *from day one*; **randomized deep audits** (R7); **interim unaudited estimates** to shrink the lag; penalties scaled to **advantage gained**, with the primary sporting penalty being a **future-cap reduction** (it constrains the offender's next-season development, where it bites — there are no tokens to dock).
- **Parameters:** markup standard; audit cadence; penalty schedule. *TODO — `regulations/financial.md` Art. 4–5.* **(Note: largely subsumed by the on-chain cost/manpower ledger, M10 — monitoring becomes native and continuous.)**

### M10 — Forced on-chain disclosure (the spine)
- **Targets:** Budget-bias and dynasty — at the source.
- **Problem:** In F1, R&D yields a *private, excludable, durable* advantage (secret aero), so spend buys lasting results and dynasties ossify (the Tullock-contest core of M1, but worse because the advantage compounds).
- **Mechanism:** Every part that runs must have its full design record (CAD/FEA/CFD/materials) on an immutable, timestamped chain by the event Upload Deadline, visible to all rivals; **only on-chain parts are legal.** R&D output becomes a club good — disclosed and copyable after a short lead. See `design/blockchain-architecture.md`.
- **Incentive analysis:** Caps the value of any innovation at the head-start it buys → **equilibrium R&D spend collapses** (you won't pay millions to arm your rivals within a weekend). Shifts the contest from secrecy to *innovation cadence + integration speed* — purer merit. Makes scrutineering a hash check and cheating structurally near-impossible (R5, R7). Native, continuous cost/manpower monitoring (subsumes much of M9, R9).
- **Failure modes & guards:** Free-rider under-provision of innovation (→ M11 *head-start/recognition* + M12 *floor*, the keystone); off-chain secret pre-development (→ development limited by the budget cap M1; only on-chain parts may *run*, so secrecy buys nothing raceable); chain/storage outage (→ signed-snapshot fallback).
- **Parameters:** Upload Deadline timing; what counts as a "new part"; chain/access architecture. *TODO — `regulations/technical.md` Art. 9; `blockchain-architecture.md`.*

### M11 — Innovation incentive (head-start + recognition) — **reframed token-free (v0.5.0)**
- **Targets:** the innovation under-provision M10 would otherwise cause.
- **Problem:** If copying is instant and free (M10), a rational team might wait and copy rather than fund first-principles R&D — the public-goods free-rider problem.
- **Mechanism (no currency):** the reward for innovating is **(a) the transient on-track head-start** — you are fast *first*, and score championship points, before rivals can manufacture a copy — plus **(b) reputational recognition** via the published **Innovation Index** (the chain records who was first). There is **no token bounty and no championship bounty** for being copied. Provenance is declared on upload, arbitrated by similarity check + dispute panel.
- **Incentive analysis:** the head-start funds itself through results, and the championship's pull toward the best parts means an innovator's new part *is* the fastest part for a window. But the head-start alone may not *compel* innovation across the whole grid — so the **mandatory floor (M12) is the load-bearing innovation-forcing lever**, not M11. M11 is the carrot; M12 is the stick, and the stick does the heavy lifting in the token-free design.
- **Failure modes & guards:** under-declared provenance (similarity check + penalties); trivial-innovation farming on the Index (minimum-significance threshold).
- **Parameters:** Innovation Index significance threshold; similarity threshold. (No token schedule — removed.) *TODO — `regulations/financial.md` Art. 8.4; `regulations/sporting.md` Art. 8.*

### M12 — Minimum origination floor (mandatory contribution to the commons)
- **Targets:** the free-rider problem M10 creates — from the **stick** side (M11 is the carrot). The two together fully solve the disclosure dilemma.
- **Problem:** forced disclosure (M10) makes copying free, so a rational team **under-invests in origination and copies the pool.** A voluntary-contribution public-goods game **under-provides at Nash equilibrium** — if enough teams free-ride, the commons starves and innovation collapses. M11's reward helps but does not *compel* contribution.
- **Mechanism:** a **mandatory minimum development spend** (a floor), of which a **defined share must produce *original* on-chain designs** (declared original, passing the novelty threshold). With the cap as ceiling, the budget becomes a tight **band [floor, cap]**. You cannot purely copy: you must spend, and a portion of that spend must feed the commons with original work.
- **Incentive analysis:** converts the voluntary public-goods game into a **compulsory-contribution mechanism** — the public good is funded by *every* member, eliminating pure free-riders by construction. M10 forces sharing, **M12 forces contribution, M11 rewards leadership.** Bonus: a high floor narrows the spend band, which is also strong **input-equalization** (Budget-bias↓) — so M12 serves meritocracy twice.
- **Failure modes & guards:** a *pure dollar floor* is gamed by spending on copying/manufacturing rather than design (still free-riding on innovation) → the floor needs **origination teeth** (minimum N original, non-trivial uploads, verified by the novelty/similarity check); trivial-"original" farming → minimum-significance threshold; small-team burden → set the floor affordably (the cap is low, plus data-revenue redistribution).
- **Parameters:** floor level as % of cap (= band width); minimum origination N / original-spend fraction; novelty threshold; shortfall penalty. *TODO — `regulations/financial.md`.*

### M13 — Lapping elimination ("player-killer")
- **Category — different from M1–M12.** This is **not** a distortion-reducer; it is a deliberate **spectacle + merit-severity** feature (with one genuine merit side-benefit). Documented here for completeness and honest analysis. `sporting.md` Art. 6.7.
- **Rule:** no blue flags; a backmarker may fight, but if **lapped by P1** it is **black-flagged out**; **P1 earns +1 point**. (Only P1 can ever lap a car — by necessity: P1 reaches any backmarker first, so a lapped car behind P1 cannot exist for a lower car to take.)
- **Merit analysis:** merit-*consistent* — it eliminates the demonstrably uncompetitive and rewards the demonstrably superior, both through **racecraft** (the backmarker may defend; the lapper must earn the pass). And it **removes lapped-traffic interference** — a real luck source in conventional racing — because no lapped cars circulate (everyone running is on the lead lap). *That* part genuinely reduces Luck.
- **Costs (honest):** (a) **field attrition** — the grid thins through the race; (b) **dominance bounty** — the fastest car laps the most, mildly amplifying its lead (works against field-compression); (c) **safety** — backmarkers fighting large speed deltas (governed by the dangerous-driving rules + the safety invariant, unchanged).
- **Controls:** a **grace period** (arm the rule only once the race has settled — lap 3 / 10% distance) and an optional **per-race Lapping-Point cap**.
- **Net:** a signature severity/spectacle mechanic that is merit-consistent and even removes one luck source, at the cost of attrition and a mild dominance reward — a deliberate point on the meritocracy↔spectacle dial, knowingly chosen.
- **Parameters:** grace threshold; per-race point cap. (Killer is necessarily P1 — settled, not a parameter.) *TODO — `sporting.md` Art. 6.7.*

---

## 4. Which mechanism attacks which distortion

| Mechanism | Luck | Budget | Gaming | Dynasty |
|-----------|:----:|:------:|:------:|:-------:|
| M1 money-neutral cap | | ●● | ● | |
| ~~M2 dev-resource auction (tokens)~~ — removed | — | — | — | — |
| ~~M3 merit-weighted handicap~~ — removed (self-balance) | — | — | — | — |
| M4 dirty-air pricing (design-stage allowance) | | | ● | |
| ~~M5 luck-suppressing neutralization~~ — removed | — | | | |
| M6 estimator design (points curve; drop-results removed) | | | ● | |
| M7 driver disentanglement (DMI) | ● | | | |
| M8 anti-gaming sporting (track limits, parc fermé; quali-norm removed) | | | ●● | |
| M9 cost monitoring — *subsumed by M10* | | ● | ● | |
| **M10 forced on-chain disclosure (spine)** | | ●● | ●● | ●● |
| **M11 innovation incentive** (head-start + recognition; no tokens) | | ● | | ● |
| **M12 minimum-spend floor** (free-rider stick; the keystone) | | ●● | ● | ● |
| **M13 lapping elimination** (spectacle; removes lapped-traffic luck) | ● | | | |

(●● primary, ● secondary)

> The free-rider problem created by M10 is solved by **M11 (carrot: the head-start + recognition) + M12 (stick: the mandatory floor)** — and in the token-free design (v0.5.0) the **stick does the heavy lifting**. The field then **self-balances by copying** (`financial.md` Art. 3), which is why the old M2/M3 currency-and-handicap machinery could be deleted.

---

## 5. Tensions & open calibrations

- **Meritocracy vs entertainment.** Resolved in principle by R2, but needs an explicit *floor*: how much luck-variance do we deliberately leave in for the show? (A racing series with zero variance is a dyno test.) → set the floor.
- **Output-side luck — a design decision taken (v0.4.1).** The output-side luck-suppressors (M5 neutralization, drop-results, qualifying normalization) were **removed** in favour of conventional racing. The series therefore leans on **input-side** merit (M10/M11/M1/M12, the skill-primacy car) + the long calendar + the DMI, and *accepts* race-day variance. This is a deliberate point on the meritocracy↔tradition dial, not an oversight — the title now carries ordinary racing luck, while the DMI still gives a luck-robust read of driver merit.
- **Token-free economy (v0.5.0).** The whole development-token / auction (M2) and success-handicap (M3) apparatus was **removed**: the disclosure economy self-balances by copying. The remaining economic levers are just the **cap** and the **floor** (`financial.md` Art. 3). This is the biggest simplification in the project's history.
- **Driver rating (M7).** Advisory vs binding is a genuine fork — binding maximizes driver-merit accuracy but invites team-order gaming. *Recommend advisory first.*
- **Dirty-air price (M4).** Implemented as a **design-stage downforce allowance** (no tokens) — must stay input-side (set at homologation) to avoid becoming BoP.
- **M12 floor level (the keystone calibration).** The floor (≈70% of cap, first-pass) is now *the* lever that keeps innovation alive in a token-free copy economy. Too low → pure-copy stagnation; high → strong input-equalization + sustained innovation. Lean high. Plus the origination share (≈half of dev spend must be original).
- **Cap value.** ≈$75M first-pass (≈half F1, justified by shared-design R&D savings). The other genuinely-open headline number.

---

## 6. Map: mechanism → regulation

| Mechanism | Lives in |
|-----------|----------|
| **M10 forced disclosure, M11 innovation incentive (the spine)** | `design/blockchain-architecture.md`; `regulations/technical.md` Art. 9; `regulations/financial.md` Art. 3, 8.4 |
| M1 cap, M12 floor, M9 monitoring (the whole economy — token-free) | `regulations/financial.md` |
| M4 dirty-air pricing (design-stage allowance) | `regulations/technical.md` |
| M6, M7, M8, M13 | `regulations/sporting.md` |
| Safety invariant (constraint, not objective) | `regulations/safety.md` |
| ~~M2 tokens/auction, M3 handicap, M5 neutralization~~ | removed |
