# Formula Zynerji — The Mechanism-Design Framework

The engine room. `philosophy.md` says **why** (meritocracy); this says **how** (the mechanisms) and **why each one is incentive-compatible**. Every rule in `regulations/` should trace back to a mechanism here.

> **The spine.** Mechanisms **M10 (forced on-chain disclosure)** and **M11 (originator rewards)** — see `design/blockchain-architecture.md` — are not just two more entries; the blockchain is the **spine** the rest hang on. Forced disclosure converts R&D from a private good into a club good, which collapses equilibrium spend and dissolves dynasties at the source. As a result **M3 (merit-weighted handicapping) is downgraded to a backstop**: the blockchain already does most of the field-compressing that M3 was carrying, so M3 should be applied lightly, if at all, to avoid over-intervening.

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

### M2 — Development-resource auction
- **Targets:** Budget-bias, Gaming, dynasty.
- **Problem:** Even under a money cap, *development throughput* (wind-tunnel runs, CFD items, dyno hours, track/sim time) is the real currency of gains. F1 rations it with the **ATR sliding scale** (70–115% by standing) — effective but crude and exogenous.
- **Mechanism:** Give every team an **equal endowment of development tokens** per period. Teams spend tokens to *buy* units of each development resource through a periodic **market/auction**. Resource is genuinely scarce (fixed total tunnel/CFD capacity), so the auction *prices* it and forces teams to reveal where they believe their marginal gain is highest.
- **Incentive analysis:** Rewards **prioritization merit** — knowing *what* to develop and *when* is itself elite engineering judgement, and it's a merit dimension current F1 doesn't reward (everyone just maxes their allowance). Equal endowment keeps it money-neutral.
- **Failure modes & guards:** *Auction-gaming* (winning via bid strategy rather than engineering) — mitigate with a **near-strategy-proof format** (uniform-price sealed-bid, or a fixed-price menu with a hard token budget) so truthful valuation is ~optimal (R5). Collusion among teams to depress prices — randomize/seal and monitor.
- **Parameters:** token endowment; auction format (uniform-price vs menu); resources priced; period length. *TODO — and see the "advisory vs binding" style question for format.*

### M3 — Merit-weighted handicapping (inputs only)
- **Targets:** dynasty (the *across-season* failure mode) — without creating Gaming or output-distortion.
- **Problem:** A genuinely better team can win for a decade (Mercedes 2014–2020; the 917/30 ending Can-Am). Pure meritocracy *permits* this — but a permanent dynasty erodes the participation floor. The naive fix (BoP / success ballast) **inverts merit** (R3) and invites sandbagging (R5).
- **Mechanism:** Couple the handicap **only to future inputs**: a successful team's **token endowment (M2) and/or ATR multiplier shrinks**, scaled to its standing. It never receives a slower car. The within-season order is untouched; the *rate at which rivals can close the gap* increases.
- **Incentive analysis:** "Success buys you less *future development*, never a worse *current* car." The leader keeps every bit of merit it has earned this year; the field gets a fairer shot to **earn** its way back next year. Sandbagging is pointless because the handicap acts on development resource, not on a per-race performance break.
- **Failure modes & guards:** *Too weak* → dynasty persists; *too strong* → merit inversion (a worse team out-develops a better one purely on handicap). **Calibrate against the historical gap-decay data** (how fast did fields actually converge under ATR?) so the handicap restores *opportunity*, not *outcome*.
- **Parameters:** handicap curve (slope, floor, ceiling); reset cadence. *TODO.*

### M4 — Dirty-air externality pricing
- **Targets:** the sport's central **negative externality**; enables merit-based overtaking; lets us delete DRS.
- **Problem:** Each team rationally maximizes its own downforce; collectively this fills the track with turbulent wake that prevents the following car from racing — a **tragedy of the commons**. Real F1 attacks it by *prescribing* wake-friendly geometry (2022 ground-effect rules) — command-and-control that teams immediately lawyer back toward outwash, and it bolts on DRS as a patch.
- **Mechanism:** In a standard test, **measure each car's wake / dirty-air footprint** at a reference following distance. **Price it**: a car that produces more downforce-destroying turbulence pays a defined penalty — in development tokens (M2), in a small mass/aero-allowance adjustment at the *design* stage (an input, not a race output — careful framing), or in a homologation cost charge. The cleaner your wake, the cheaper your downforce.
- **Incentive analysis:** Internalizes the externality (R6). Rewards the *harder* engineering of clean-wake downforce — a real merit dimension — and restores close following so on-track passes reflect merit, not a DRS button.
- **Failure modes & guards:** Test must be reproducible and hard to overfit (R7) — define the rig and the metric precisely; randomize test conditions. Ensure the "price" is an **input-side** charge so it doesn't become BoP (R3).
- **Parameters:** wake metric + rig; following distance; price schedule and currency. *TODO — `regulations/technical.md` Art. 3.*

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
- **Mechanism:** Related-party transfers priced at a declared market-consistent standard *from day one*; **randomized deep audits** (R7); **interim unaudited estimates** to shrink the lag; penalties scaled to **advantage gained**, with the primary sporting penalty being a **development-token / ATR reduction** (it hurts a leader more than a fine).
- **Parameters:** markup standard; audit cadence; penalty schedule. *TODO — `regulations/financial.md` Art. 4–5.* **(Note: largely subsumed by the on-chain cost/manpower ledger, M10 — monitoring becomes native and continuous.)**

### M10 — Forced on-chain disclosure (the spine)
- **Targets:** Budget-bias and dynasty — at the source.
- **Problem:** In F1, R&D yields a *private, excludable, durable* advantage (secret aero), so spend buys lasting results and dynasties ossify (the Tullock-contest core of M1, but worse because the advantage compounds).
- **Mechanism:** Every part that runs must have its full design record (CAD/FEA/CFD/materials) on an immutable, timestamped chain by the event Upload Deadline, visible to all rivals; **only on-chain parts are legal.** R&D output becomes a club good — disclosed and copyable after a short lead. See `design/blockchain-architecture.md`.
- **Incentive analysis:** Caps the value of any innovation at the head-start it buys → **equilibrium R&D spend collapses** (you won't pay millions to arm your rivals within a weekend). Shifts the contest from secrecy to *innovation cadence + integration speed* — purer merit. Makes scrutineering a hash check and cheating structurally near-impossible (R5, R7). Native, continuous cost/manpower monitoring (subsumes much of M9, R9).
- **Failure modes & guards:** Free-rider under-provision of innovation (→ M11 *carrot* + M12 *floor*); off-chain secret pre-development (→ physical test resource rationed by M2; only on-chain parts may *run*, so secrecy buys nothing raceable); chain/storage outage (→ signed-snapshot fallback).
- **Parameters:** Upload Deadline timing; what counts as a "new part"; chain/access architecture. *TODO — `regulations/technical.md` Art. 9; `blockchain-architecture.md`.*

### M11 — Originator rewards (curing the patent dilemma)
- **Targets:** the innovation under-provision that M10 would otherwise cause; rewards **innovation merit** directly.
- **Problem:** If copying is instant and free (M10), a rational team waits and copies rather than funding first-principles R&D — the public-goods free-rider problem. Disclosure without a reward starves innovation.
- **Mechanism:** The chain records who uploaded each innovation **first**. When other teams adopt a derivative design, the **originator earns an on-chain reward** — primarily **Development Tokens** (M2: innovating buys more future R&D capacity, the most merit-aligned reward) plus a published **Innovation Index**. Reward scales with the number of distinct adopters. Provenance is declared on upload and arbitrated by similarity check + dispute panel (all designs are public, so disputes resolve).
- **Incentive analysis:** Pays innovators for the public good they create **without** slowing copying — so the field stays compressed *and* innovation stays funded. The reward strength is the **patent-term analogue**: the master knob balancing disclosure against incentive.
- **Failure modes & guards:** Under-declared provenance (similarity check + penalties); trivial-innovation farming (minimum-significance threshold; reward only on genuine cross-team adoption).
- **Parameters:** tokens per adopter; Innovation Index weighting; whether it carries any championship credit (advisory vs scored); similarity threshold. *TODO — `regulations/financial.md` Art. 3; `regulations/sporting.md` Art. 8.*

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
| M2 dev-resource auction | | ●● | ● | ● |
| M3 merit-weighted handicap (inputs) — *backstop* | | ● | | ● |
| M4 dirty-air pricing | | | ● | |
| ~~M5 luck-suppressing neutralization~~ — removed | — | | | |
| M6 estimator design (points curve; drop-results removed) | | | ● | |
| M7 driver disentanglement (DMI) | ● | | | |
| M8 anti-gaming sporting (track limits, parc fermé; quali-norm removed) | | | ●● | |
| M9 cost monitoring — *subsumed by M10* | | ● | ● | |
| **M10 forced on-chain disclosure (spine)** | | ●● | ●● | ●● |
| **M11 originator rewards** (free-rider carrot) | | ● | | ● |
| **M12 minimum origination floor** (free-rider stick) | | ●● | ● | |
| **M13 lapping elimination** (spectacle; removes lapped-traffic luck) | ● | | | |

(●● primary, ● secondary)

> The free-rider problem created by M10 is solved by the **M11 (carrot) + M12 (stick)** pair: M11 rewards contributing above the floor; M12 makes the floor mandatory. Neither alone is sufficient.

---

## 5. Tensions & open calibrations

- **Meritocracy vs entertainment.** Resolved in principle by R2, but needs an explicit *floor*: how much luck-variance do we deliberately leave in for the show? (A racing series with zero variance is a dyno test.) → set the floor.
- **Output-side luck — a design decision taken (v0.4.1).** The output-side luck-suppressors (M5 neutralization, drop-results, qualifying normalization) were **removed** in favour of conventional racing. The series therefore leans on **input-side** merit (M10/M11/M1/M12, the skill-primacy car) + the long calendar + the DMI, and *accepts* race-day variance. This is a deliberate point on the meritocracy↔tradition dial, not an oversight — the title now carries ordinary racing luck, while the DMI still gives a luck-robust read of driver merit.
- **Handicap strength (M3).** Too weak → dynasties; too strong → merit inversion. Must be calibrated against historical gap-decay, not guessed.
- **Auction-gaming (M2).** Choose a format where engineering judgement, not bid-strategy, decides. Lean strategy-proof.
- **Driver rating (M7).** Advisory vs binding is a genuine fork — binding maximizes driver-merit accuracy but invites team-order gaming. *Recommend advisory first.*
- **Dirty-air price currency (M4).** Token charge vs design-stage allowance — must stay input-side to avoid becoming BoP.
- **Originator-reward strength (M11) — the master knob.** The patent-term analogue: too weak and innovation under-provides (everyone copies); too strong and it re-creates a durable advantage. The single most important calibration in the formula.
- **M3 backstop level.** With M10 doing the field-compressing, how light can the handicap be — or can it be dropped entirely?
- **M12 floor level (band width).** How high is the minimum spend/origination floor? A high floor (narrow band) most strongly destroys free-riding *and* equalizes inputs, but leaves less room for "spend-efficiency" merit. Since the goal is to *destroy* free-riding, lean to a high floor.

---

## 6. Map: mechanism → regulation

| Mechanism | Lives in |
|-----------|----------|
| **M10 forced disclosure, M11 originator rewards (the spine)** | `design/blockchain-architecture.md`; `regulations/technical.md` Art. 9; `regulations/financial.md` Art. 3 |
| M1 cap, M3 handicap (backstop), M9 monitoring | `regulations/financial.md` |
| M2 auction (pays M11 rewards) | `regulations/financial.md` (+ technical for resource types) |
| M4 dirty-air pricing | `regulations/technical.md` |
| M5, M6, M7, M8 | `regulations/sporting.md` |
| Safety invariant (constraint, not objective) | `regulations/safety.md` |
