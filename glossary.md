# Formula Zynerji — Glossary of Defined Terms

Defined Terms are Capitalised throughout the regulations. The rules lean on these; change a definition and check every use.

## Core framework (see `design/mechanism-design.md`)

- **Meritocracy** — the project's objective: the standings should track true competitive merit as closely as possible.
- **The Estimator** — framing of a season as a measurement of unobservable true Merit; the standings are the estimate. `Standings = Merit + Luck + Budget-bias + Gaming-bias`.
- **The Three Distortions** — **Luck**, **Budget-bias**, **Gaming-bias**: the error terms the rulebook exists to shrink.
- **Variance Razor** — embrace variance that rewards skill; suppress variance that rewards luck.
- **Skill-variance / Luck-variance** — outcome variability driven by competitive quality (signal, kept) vs by chance (noise, suppressed).
- **Mechanism (M1–M12)** — an incentive-compatible rule designed for its *equilibrium* behaviour. Catalogued in `design/mechanism-design.md`.
- **Free-rider problem** — under forced disclosure, the temptation to copy the shared pool instead of originating; cured by the M11 *carrot* + M12 *floor* pair.
- **Design Razors (R1–R9)** — the rules for writing rules (e.g. *equalize inputs not outputs*; *price externalities*; *assume Goodhart*).
- **Input / Output (equalization)** — we equalize *inputs* (money, resource) and never *outputs* (no Balance of Performance).

## Blockchain — the spine (see `design/blockchain-architecture.md`)

- **The Chain / Ledger** — the permissioned, immutable, timestamped record holding four ledgers: Rules, Designs, Data, Manpower.
- **On-Chain Legality (M10)** — a part may run only if its full design record is on the Designs ledger by the Upload Deadline. Off-chain parts are illegal.
- **Upload Deadline** — the start-of-event moment by which all run parts must be uploaded; the disclosure moment from which rivals may copy.
- **Forced Disclosure** — the mandatory sharing of CAD/FEA/CFD for every run part; converts R&D from a private good to a club good. Mechanism M10.
- **Natural Lead** — the head-start an innovator gets purely from rivals' manufacturing/integration lag (no formal embargo).
- **Innovation Incentive (M11)** — the reward for innovating, **token-free (v0.5.0)**: the transient on-track head-start + reputational Innovation Index credit. No payment, no championship bounty.
- **Innovation Index** — the published record of originator credit.
- **Provenance Declaration** — the on-upload statement that a part is *original* or *derived from element X*; basis of attribution.
- **Scrutineering-by-Hash** — verifying a fitted part matches its on-chain record (geometry hash + material).
- **Data Revenue** — income from selling chain data to media/public (paid access tier); redistributed toward smaller teams.
- **Manpower Ledger** — on-chain registry of personnel/roles/hours; makes labour cost native-auditable; enables a transparent transfer market.

## The car & engine (see `regulations/technical.md`)

- **Era Kitbash** — the base car: 2026 wings/floor/tyres/safety · 2021 hydraulic interconnected suspension · 2013 gearbox · 2008 dimensions/body. Integration in `design/chassis-integration.md`.
- **Zone Ownership** — the map assigning each part of the car to the era that governs it; precedence Safety(2026) > Dimensions(2008) > Aero(2026) > Bodywork(2008).
- **Two-Stroke Diesel** — the spec engine: 2.5 L inline-5, two-stroke, **uniflow-scavenged**, compression-ignition; ~1015 hp / ~1035 N·m at 7000 rpm.
- **Uniflow Scavenging** — intake ports at the liner bottom (blower-fed) + exhaust poppet valves in the head; air flows one way (bottom→top), the most efficient 2-stroke method; requires the positive-displacement blower.
- **Synthetic e-Kerosene** — the fuel: a fully-synthetic (carbon-neutral) JP-8-class kerosene, single common spec, density-optimized (~0.84 kg/L), cetane ≥50, ULS, minimal additives (lubricity + static dissipator only). Appendix T-B.
- **VLEM (Variable-Length Exhaust Manifold)** — the engine's primary tuning element; **electronically controlled** to set the optimal exhaust length at every rpm, broadening the 2-stroke's powerband. *Automated engine-output optimization* (permitted), **set-and-run** (map locked pre-race, no driver input). Shared on-chain.
- **Driver-Vectored Differential** — a twin wet-clutch torque-vectoring rear axle (GKN Twinster / Nissan-Juke style: a clutch pack per side, no central diff). Two digital-proportional steering-wheel triggers set the **% lockup** of each side's clutch in real time — a *live manual* skill input (permitted). Legal because **open-loop**: the trigger→clamp map is fixed/on-chain and the Standard ECU adds no sensor feedback — distinct from banned *automated* (closed-loop) vectoring. Fail-safe to an even baseline clamp. Strengthens the driver-merit signal (M7).
- **Brakes** — carbon–carbon, 18″-sized, up to 6-piston; **no ABS / no brake-by-wire / no electronic distribution** (pure car-control, fully manual); brake bias is a live manual driver control (cockpit bias bar). No regen.
- **Fuel Injection** — high-pressure common-rail DI (~2500–3000 bar, multi-event); injection timing vs port/valve events is the primary combustion lever; automated engine-optimization, set-and-run, on-chain dev zone.
- **Single Tyre Supplier** — one approved tyre supplier serves the grid on equal terms (input-equalization; removes the supplier-dependency risk that killed the Tyrrell P34). Tyres aren't a dev lever; tyre management is the skill. No tyre warmers.
- **Driver Interface** — pedals (throttle/brake/clutch), shift paddles, the two diff triggers, brake-bias adjuster, steering. Deliberately high manual workload (no TC/ABS, manual diff + bias) as a driver-merit axis (M7).
- **"Automate the engine, never the driving"** — the defining electronics principle (`technical.md` Art. 8.4): live manual driver inputs permitted (the skill); automated *engine-output* optimization permitted but set-and-run/locked; automated *car-control* aids banned.
- **Set-and-Run** — automated calibrations (VLEM, fuel/ignition maps) are locked under parc fermé before the race; no in-race changes, no driver fiddling.
- **Screw (Lysholm) Supercharger** — the mechanical positive-displacement blower that scavenges the 2-stroke every cycle.
- **JP-8 (class)** — the kerosene chemistry the fuel is built to; here realized as carbon-neutral **Synthetic e-Kerosene** (see above; Appendix T-B), not fossil military JP-8.
- **Scavenging** — pushing exhaust out and fresh charge in during the 2-stroke's port window; requires the blower on every cycle.
- **Spec Base + Open Zones** — the engine supply model: common core unit, defined development zones, all shared on-chain.

## Financial / resource

- **Budget Cap** — the single, hard, **equal** per-season spending limit (no luxury-tax overspend lane). Mechanism M1.
- **Budget Band** — the bracket **[floor, cap]** within which every team must spend. Cap = M1 (ceiling); Floor = M12.
- **Minimum Development Spend (Floor)** — the mandatory minimum each team must spend on performance development; destroys free-riding. Mechanism M12.
- **Origination Floor / Teeth** — the requirement that a defined share of the floor produce *original* on-chain designs (≥ N novel uploads), so the spend feeds the commons rather than copying. Mechanism M12.
- **Relevant Costs / Exclusions** — what counts toward the cap / the short bright-line excluded list.
- **Self-Balancing Economy** — the field balances without artificial currency: disclosure makes advantages transient (copied away), the championship pulls everyone to the best on-chain parts, and the floor forces continuous innovation. Replaced tokens/auction/handicap (v0.5.0). `financial.md` Art. 3.
- **Development Token / Auction / Merit-Weighted Handicap (M2/M3)** — *removed v0.5.0.* The token currency, development auction, and success handicap are gone; development is limited by money (the cap) and the field self-balances by copying.
- **Reporting Group** — entrant + controlled subsidiaries + related parties; the scope of every limit.
- **Balance of Performance (BoP)** — post-hoc weight/power equalization of *outputs*. **Formula Zynerji does not use BoP**; the term names what we reject.

## Technical

- **Dirty-Air Footprint / Wake** — the aerodynamic disturbance a car imposes on a following car, measured on the Standard Aero Rig. Mechanism M4.
- **Externality Price** — the input-side charge proportional to a car's wake (the dirtier the wake, the more it costs). Mechanism M4.
- **Standard Aero Rig** — the reproducible test rig for downforce, ride-height stability, and wake.
- **Reference Plane** — the mandatory plank/skid (nominal 10 mm, max 2 mm wear); proxy for legal ride height.
- **Standard Logger** — the sealed energy/power meter enforcing the caps.
- **Standard Safety ECU** — series-supplied unit governing safety-critical functions only.
- **Survival Cell / Cockpit Protection Device** — the crash-tested driver structure / the mandatory halo-equivalent (≥ 125 kN).
- **Energy Cap / Power Cap** — the prescribed limits on energy per lap/km and instantaneous power.

## Sporting

- **Constructor** — entrant that builds its own primary car structure.
- **Competition Licence** — the driver eligibility credential (feeder-ladder + representative-car test).
- **Driver-Merit Index (DMI)** — the official **advisory** hierarchical-Bayesian rating separating car_effect from driver_effect (teammate-referenced, one scale via cross-team links, on-chain-reproducible). Has its own "Driver-Merit Champion" award but does **not** decide the points title (anti-gaming). Mechanism M7.
- **Points Curve** — the estimator's weighting function: all 22 finishers score, convex front (40→1), non-zero tail — measures the whole field. Mechanism M6.
- **All rounds count** — no drop-results (removed v0.4.1); variance handled by the long 22-round sample, not by trimming worst results.
- **Field-Strength Weighting** — *deliberately not used* for points (no-op within a constant-field season); lives only in the DMI model. Mechanism M6.
- **Qualifying** — standard knockout on raw times (no track-evolution normalization, removed v0.4.1); reading the track is qualifying craft.
- **Neutralization** — conventional VSC + safety car + red flag (the engineered "time-neutral" correction was removed v0.4.1); ordinary safety-car variance accepted.
- **Lapping Rule ("player-killer", M13)** — no blue flags; a backmarker may fight, but if **lapped by P1** it is **black-flagged out** (no result, no points); **P1 earns +1**. *Only P1 can ever lap* (necessity: P1 reaches any backmarker first). Everyone running stays on the lead lap → also removes lapped-traffic luck. `sporting.md` Art. 6.7.
- **Lapping Point** — the +1 championship bounty earned by P1 for lapping (eliminating) a car; modest (vs 40 for a win); grace-armed and optionally capped.
- **Parc Fermé** — the period (qualifying start → post-race) during which only defined work is permitted.
- **Listed / Transferable / Standard-supply** — the three component-classification tiers.

## Flags (`sporting.md` Art. 6.5)

| Flag | Meaning |
|------|---------|
| Green | Track clear |
| Single yellow | Hazard; slow, no overtaking in sector |
| Double yellow | Great danger; be prepared to stop |
| Red | Session suspended; return to pit lane |
| White | Slow vehicle on track |
| Chequered | Session/race end |
| Black (+ number) | Driver out — disqualified, **or lapped (Art. 6.7 lapping rule)** |
| Black & orange | Mechanical damage; pit |
| Black & white (halved) | Unsportsmanlike-conduct warning |
| Surface (yellow/red stripe) | Slippery surface |
