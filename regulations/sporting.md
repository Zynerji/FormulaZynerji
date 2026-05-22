# Formula Zynerji — Sporting Regulations

**Version 0.4.2 (draft).** The competition, designed as a **measurement instrument for merit**. Implements **M6** (the points curve), **M7** (the Driver-Merit Index), parts of **M8** (sensor track limits, parc fermé, hash-scrutineering), the competition side of **M10/M11** (Innovation Index), and **M13** (the no-blue-flag lapping-elimination "player-killer" rule, Art. 6.7). Numbers are first-pass and tunable.

> **Design note (v0.4.1):** the **output-side luck-suppression** mechanisms — drop-results, qualifying track-evolution normalization, and time-neutral safety-car correction (parts of M5/M6/M8) — were **deliberately removed**. The series uses **conventional racing**: every round counts, raw knockout qualifying, standard safety-car procedures. The cost is that normal race-day variance (an unlucky DNF, a green-track run, a timely safety car) now counts fully. Meritocracy is therefore carried by the **inputs** (forced disclosure, money-neutral cap, skill-primacy car), the **long 22-round sample** (variance falls with round count), and the luck-robust **DMI** (Art. 5.4) — not by correcting outputs.

---

## Article 1 — The Championship

1.1 **Grid:** **11 Constructors × 2 cars = 22 entries** (first-pass). Both cars score for the Constructor.
   > TODO: ratify team/car counts; the points curve (Art. 5.1) is sized to a 22-car field.

1.2 **Calendar:** target **K = 22 rounds.** More rounds = a lower-variance estimator of merit (more samples), so a longer calendar is *meritocratically* preferable, bounded by cost and logistics.

1.3 **Three season classifications:**
   - **Constructors' Championship** — sum of both cars' points (Art. 5) over **all rounds** (no drop-results — every race counts).
   - **Drivers' Championship** — each driver's points over all rounds. *The* title.
   - **Driver-Merit Index (DMI)** — an *advisory* published rating (Art. 5.4) that ranks drivers **net of machinery**, with its own season award ("Driver-Merit Champion"). Reveals the best *driver* even if not in the best *car*.

1.4 **Tie-break:** most race wins, then most 2nds, 3rds, … Qualifying and fastest laps do not break ties (noisier merit signals). The DMI is the final tie-break if countback is exhausted.

---

## Article 2 — Eligibility & Entry

2.1 **Constructors** apply to the series and must design and build the primary structure of their own car (the locus of engineering merit; component classes in Art. 8). All design data is on-chain (M10).

2.2 **Drivers — Competition Licence.** Earned via a **feeder-series points ladder** (recognized junior categories award licence points by result) **plus** a minimum-distance test in a representative car, and a minimum age. This is a quality/safety filter *and* keeps the field a fair merit comparison (a weak entrant would bias both championships).
   > TODO: define the feeder-series points table and thresholds (the ladder depends on the series' junior ecosystem).

2.3 **New-entrant ramp:** a new Constructor receives maximum development allocation and no handicap for a defined ramp period (`financial.md` Art. 3.5), and a share of redistributed data revenue (`financial.md` Art. 8.2) so a well-run new team can establish itself.

---

## Article 3 — Event Format (M8)

3.1 **Standard event:** Practice → Qualifying → Race. Practice is limited (in-season running is rationed for cost; the development resource is the auction/token system, `financial.md` Art. 3).

3.2 **Qualifying — standard knockout.** Three knockout segments (Q1/Q2/Q3) set the grid on raw lap times (no track-evolution correction). Reading the track's evolution and timing your run to catch the best window is treated as **part of qualifying craft**, not luck to be engineered away — the conventional approach.

3.3 **Race:** minimum distance **~300 km** or a **2-hour** time cap, whichever first. In dry conditions, **≥ 1 pit stop and ≥ 2 different tyre compounds** are mandatory — forcing *strategic* variation (a skill dimension, R2), not a tyre lottery. Grid set by Art. 3.2.
   > TODO: confirm distance/time and the wet-race exception to the compound rule.

3.4 **No DRS.** Close following and overtaking come from **dirty-air externality pricing** (`technical.md` Art. 3, M4) — passes reflect merit, not a button.

3.5 **No sprint races, no fastest-lap point (default).** Both add variance and a gaming surface (M6); they are adopted only if a specific format demonstrably *raises* `corr(Standings, Merit)` — which extra-variance formats generally do not.

---

## Article 4 — Parc Fermé (M8)

4.1 Parc Fermé runs from the start of qualifying to the end of the race; only defined work is permitted within it. This includes the lock of all **set-and-run automated calibrations** (engine/VLEM/injection maps, `technical.md` Art. 8.4.2) — no in-race reprogramming.
   > Rationale: a broad parc fermé rewards *setup merit* (getting it right once) and curbs overnight-rebuild spend, keeping the comparison fair. Default broad; revisit only if it suppresses a legitimate merit dimension.

---

## Article 5 — The Championship Estimator (M6)

> The points system **is** the estimator's weighting function. Designed for signal-to-noise, not tradition or drama. Two goals: (a) score the **whole field** so mid-grid merit is measured (not rounded to zero), and (b) keep enough front-loading that **winning matters**.

### 5.1 Points curve — all classified finishers score

First-pass 22-position curve (strictly decreasing, convex at the front, non-zero tail):

| Pos | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|-----|---|---|---|---|---|---|---|---|---|----|----|
| Pts | **40** | 33 | 28 | 24 | 21 | 19 | 17 | 15 | 14 | 13 | 12 |

| Pos | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|-----|----|----|----|----|----|----|----|----|----|----|----|
| Pts | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | **1** |

Design notes: the front gaps shrink (7, 5, 4, 3, 2 …) — **convex**, so a win (40) is worth ~1.9× a 5th (21) and ~3× a 10th (13), but every position down to 22nd is **discriminated** (gap of 1), so the estimator extracts merit information from the *entire* field rather than discarding positions 11–22. Compared with F1's top-10-only curve, this is a markedly lower-bias estimator of mid-grid merit.
   > TODO: tune the curve (front steepness vs tail) once a target win-value is set.

> **All rounds count** — there are no drop-results (removed in v0.4.1). Variance is handled by the long 22-round sample rather than by trimming a competitor's worst results, so every race matters and an unlucky round counts like any other.

### 5.2 Field-strength weighting — deliberately NOT used (for points)

A win against a stronger field "should" count more — but **within a season the field is the same 22 cars every round**, so per-round field-strength weighting adds *no* information to the championship. It is therefore omitted (adding a no-op mechanism is a failure of discipline). Field/era strength *does* matter across contexts, where it is handled inside the Driver-Merit model (5.4), not the points.

### 5.3 No fastest-lap bonus, no sprint points

Each adds variance and a gaming surface without improving the merit estimate (the FL point was gamed and abolished in real F1 — revealed evidence, R8).

### 5.4 Driver-Merit Index (DMI) — separating the driver from the car (M7)

> The Drivers' points title is unavoidably confounded by machinery: the best driver in the 4th-best car cannot win it. The DMI is the series' answer — a published estimate of **driver skill net of car**.

5.4.1 **Model.** A **hierarchical Bayesian model** decomposes each car's per-round performance (race pace / pairwise finishing outcomes, with telemetry) as:

> `performance ≈ car_effect[constructor, season-phase] + driver_effect[driver] + track/condition_effects + noise`

5.4.2 **Identification.** **Teammates share `car_effect`** (identical machinery — the cleanest controlled experiment in the sport), so within-team gaps directly identify *differences* in `driver_effect`. The field is tied onto **one common scale** by the network of cross-links: drivers who change teams between seasons, and shared track/condition effects, connect everyone (a Bradley-Terry / Elo-style estimate on a connected comparison graph).

5.4.3 **Transparency.** All inputs — results, timing, telemetry, conditions — are **on-chain (M10)**, so the DMI is **reproducible**: anyone can recompute the official rating from public data. (A rare case where the blockchain underwrites a *driver* metric, not just a part.)

5.4.4 **Output & status.** The DMI is published each round as a rating with credible intervals, and a season **Driver-Merit Champion** is awarded. It is **advisory** — it does **not** decide the Drivers' Championship (that stays points-based, Art. 1.3), and it serves only as the final tie-break (Art. 1.4).
   - **Why advisory, not binding:** a binding rating would maximize driver-merit accuracy but is itself a gameable mechanism (team orders, sandbagging a teammate to flatter your own number). Keeping it advisory makes gaming it nearly pointless, while still publishing the truth about driver skill.
   > TODO: finalize the model family/priors and the published-uncertainty format.

### 5.5 Lapping points (the survival bounty, M13)

**+1 championship point** to the current **P1** each time it laps — and thereby eliminates — another car (the full rule is Art. 6.7; only P1 can lap, by necessity). A modest bounty (1 vs 40 for a win): flavour and a reward for leading through the field, not a title-decider. *(It does mildly reward dominance — capped if needed per Art. 6.7.5.)*

---

## Article 6 — Penalties, Stewarding & Track Limits (M8)

6.1 **Stewards' panel** includes an experienced-driver steward.

6.2 **Penalty ladder:** reprimand → 5 s → 10 s time penalty → drive-through → 10 s stop-go → grid penalty → disqualification → suspension.

6.3 **Licence penalty points:** **12 points in a rolling 12 months = an automatic one-event ban**; points expire after 12 months. A clean, low-discretion behavioural incentive (no per-incident negotiation over a ban).

6.4 **Track limits — hard-measured, not judged (M8/R7).** Defined by sensors (timing loops / transponders), not steward judgement — removing the lawyering/inconsistency gaming surface. Four wheels beyond the defined edge = a measured violation: in qualifying the lap is deleted; in the race a fixed warning-then-time-penalty escalation.

6.5 **Flags:** standard motorsport set (defined in `glossary.md`), supplemented by electronic marshalling panels — **except there are no blue flags** (replaced by the lapping rule, Art. 6.7).

6.6 **Technical legality by hash (M10).** A car is legal iff every fitted part matches an on-chain record uploaded by the Upload Deadline (`technical.md` Art. 9.4). Immutable timestamping makes secret/back-dated parts structurally impossible — most technical-cheating disputes simply cannot arise (R5, R7).

6.7 **No blue flags — lapping is elimination (the survival rule, "player-killer") (M13).** There are **no blue flags**; a backmarker is **never required to yield**.
   - **6.7.1 The fight.** A car about to be lapped **may defend and race** the car a full lap (or more) ahead — subject to the normal driving standards (6.2, penalty points) and the safety invariant; defence must be fair (no dangerous blocking despite the speed delta).
   - **6.7.2 Elimination.** If a car circulating on the racing line is **overtaken on-track by the race leader (P1), putting it a full lap down** — i.e. it is lapped — it is immediately shown the **black flag** and is **out of the race** (no result, no points). *Being lapped = elimination.*
   - **6.7.3 The bounty.** **The current P1 driver earns +1 championship Lapping Point** (driver and constructor) at the moment the black flag is shown (Art. 5.5).
   - **6.7.3a Only P1 can lap — by necessity, not by rule.** A car cannot be a lap down *behind* P1 for a lower car to lap, because **P1 would have lapped (and eliminated) it first**: P1 is the frontmost car and reaches any backmarker before anyone running 2nd or lower could. So the lapper is *always* the current leader — the elimination mechanic collapses the set of possible "killers" to exactly one.
   - **6.7.4 Emergent property.** Because anyone who would be lapped is removed, **every car still running is on the lead lap** — no lapped cars circulate. This also **removes lapped-traffic interference**, a genuine luck source in conventional racing (one leader catches traffic at a bad moment, another doesn't).
   - **6.7.5 Grace & caps (tunables).** The rule is **armed only after the race has settled** — no lapping-elimination before **lap 3 / 10% distance** (first-pass) — so a slow opening lap or an early off doesn't instantly kill. An optional **per-race cap on Lapping Points** bounds the dominance bounty.
   > Honest consequences: the field **thins** through the race (the player-killer intent — a thinning toward a climactic finish), and the bounty mildly **rewards dominance** (the fastest car laps the most). Both deliberate; the grace period + optional cap are the controls. Safety is unchanged — fair-defence and dangerous-driving rules + the safety invariant govern the speed-delta risk. See `design/mechanism-design.md` M13.

---

## Article 7 — Neutralization & Safety Car

> Conventional, standard-motorsport neutralization for safety. (The earlier engineered "time-neutral" correction was removed in v0.4.1; the series accepts ordinary safety-car variance as part of racing.)

7.1 **Virtual Safety Car (VSC).** For lesser incidents, an imposed speed delta via the Standard Safety ECU; deployable within 30 s (`safety.md` Art. 7.5). Standard procedure.

7.2 **Physical Safety Car.** Deployed when safety requires bunching or field control (recovery on the racing line, severe conditions). Cars form up behind it, no overtaking, lapped-car procedure and a standard restart. Conventional — no time-credit or gap-restoration.

7.3 **Red flag:** suspension and standard resumption procedure — the safety invariant overrides all else.

---

## Article 8 — Component Classification, Disclosure & Innovation Credit (M10/M11)

> Forced on-chain disclosure (M10) abolishes durable exclusive IP: there is no permanently "team-secret" part. The classification is about *who must originate* a design and *who gets credited*, not who may keep it secret.

8.1 Components classified as:
   - **(A) Self-originated** — must be designed by the entrant; uploaded on-chain; **visible and copyable by all** after the Upload Deadline. "Exclusive" lasts only as long as the manufacturing head-start.
   - **(B) Freely copyable** — any on-chain design any team may adopt, declaring provenance (8.3).
   - **(C) Standard supply** — single series supplier (tyres, wheels, safety-critical parts, the Standard Safety ECU and Standard Logger); common to all.

8.2 **No priced inter-competitor IP transfer** — disclosure is mandatory and copying is free (that is the whole economy). The F1 market for secrets is replaced by the originator-reward system (8.3).

8.3 **Provenance & Innovation Index (M11).** On upload, each part is declared *original* or *derived from on-chain element X* (`technical.md` Art. 9.2). First-originators earn Development Tokens per adopting team (`financial.md` Art. 3.4) and are recorded on a published **Innovation Index**. A similarity check + dispute panel resolves contested attribution (all designs are public).
   > TODO: whether the Innovation Index carries any championship credit (default: recognition only).

---

## Article 9 — Eligibility of Novel Technology

9.1 A genuinely novel technology outside the current technical rules may be submitted for evaluation; the series may admit it to the mainline rules at the next cycle on cited evidence.
   > Formula Zynerji is *prescriptive* (era-kitbash car), so this is an evaluation pathway, not the open-class "innovation class" of the superseded v0.1 concept.

---

## Article 10 — Rule-Change Process

10.1 **Cycle:** major revisions on a fixed multi-year cycle; minor clarifications annually; safety changes any time on cited evidence (the invariant). The rulebook itself is versioned on-chain (`design/blockchain-architecture.md` §2).

10.2 Any change to a **mechanism's calibration** (cap, tokens, handicap, points curve, drop-count, dirty-air price, DMI model) must be justified against the objective — *does it raise `corr(Standings, Merit)`?* — and logged with that justification in `CHANGELOG.md`.

10.3 Banning an existing legal technology requires a **supermajority of Constructors plus the governing body** — except safety changes, which the governing body may impose unilaterally on evidence (prevents competitive-threat bans dressed as safety).

---

## Article 11 — Economics & Prize Structure (closing the loop)

> Lesson 5 of `design/precedents-open-class.md`: a formula dies if its economics don't close (Can-Am). The competition must be financially survivable for a well-run small team.

11.1 **Prize fund** distributed across the championship such that a competently-run **mid-field team can break even** at mid-grid results — not only the front runners.

11.2 **Data-revenue redistribution** (`financial.md` Art. 8.2) is weighted toward smaller teams, an additional floor under the grid.

11.3 Combined with the money-neutral cap + minimum-spend floor (`financial.md` M1/M12) and the development handicap/auction (M2/M3), the intent is a grid where **results track merit, not budget, and the field stays full.**
   > TODO: set the prize-distribution curve and the qualifying/championship-position payout weighting.
