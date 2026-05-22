# Formula Zynerji — Technical Regulations

**Version 0.3.5 (draft).** Defines the *car*: a deliberate **kitbash of historical F1 eras** with a distinctive **2-stroke diesel** powertrain, every part of which is governed by the **on-chain legality rule** (`design/blockchain-architecture.md` M10) and disciplined by **dirty-air externality pricing** (M4). Safety is in `safety.md` (the invariant).

> **The car in one table — the era basis the design is built on:**
>
> | System | Era basis | Notes |
> |--------|-----------|-------|
> | Front + rear wings, **floor**, tyres, wheels, safety | **2026** | Modern ground-effect floor + wings + 18″ tyres + current crash standards |
> | Suspension | **2021** | Hydraulically-interconnected (front–rear) permitted |
> | Gearbox | **2013** | 7-speed, longevity rule, sequential |
> | Chassis sizing, dimensions, body rules | **2008** | Narrow (1800 mm) track, permissive centre-body aero |
> | Engine | **new** | 2.5 L I5 2-stroke screw-supercharged diesel, JP-8, ~1015 hp |

---

## Article 1 — General Principles

1.1 **On-chain legality (the meta-rule, M10).** A part may be fitted to a car only if its complete design record (CAD, FEA, CFD, materials) is on the Designs ledger by the event Upload Deadline (`blockchain-architecture.md` §3; Art. 9 below). **Off-chain parts are illegal.** This is the foundation of scrutineering and of the whole forced-disclosure economy.

1.2 **Prescriptive, era-based car.** The car is defined by porting specific historical F1 regulation sets (the table above). Within each ported set, the freedoms that set allowed are merit-bearing — and, because every design is disclosed on-chain, those freedoms no longer trigger a secret-spend arms race.

1.3 **Dangerous-construction clause.** A car presenting a danger may be excluded regardless of letter-compliance.

1.4 Each rule should name the mechanism/distortion it serves (`design/mechanism-design.md`).

---

## Article 2 — Definitions & Measurement

2.1 Defined Terms (Capitalised) are in `glossary.md`.

2.2 **Coordinate system & Reference Condition** as standard (origin at front-axle centre; driver aboard, no fuel, nominal tyre pressure, lowest legal ride height). Aero quantities incl. wake (Art. 3) are measured on the Standard Aero Rig (Appendix T-C).

---

## Article 3 — Aerodynamics: 2026 Surfaces + Dirty-Air Pricing (M4)

3.1 **Wings, floor, tyres — 2026 basis.** Front wing, rear wing, and the ground-effect **floor** are ported from the 2026 F1 Technical Regulations (reference volumes, deflection limits, plank), as is the 18″ tyre/wheel package.
   > The 2026 surfaces are dimensioned for a 1900 mm-wide car and must be **adapted to the 2008 1800 mm track** — a lateral rescale of **1800/1900 ≈ 0.947** (height unchanged). The full reconciliation, including the harder underbody and 13″→18″ items, is worked through in **`design/chassis-integration.md`**, which feeds Appendix T-A.

3.2 **Centre-body aero — 2008 basis.** Bodywork between the wings (sidepods, engine cover, appendages) follows the more permissive **2008** body rules (Art. 4). The discipline on this freedom is not prescriptive geometry but the wake price (3.3).

3.3 **Dirty-air externality pricing (M4).** Each homologated car's wake is measured on the Standard Aero Rig (the downforce loss it imposes on a reference following car). **The dirtier the wake, the more it costs** — charged on the *input* side (never as in-season weight/power; that would be BoP, R3). Default currency: a **Development-Token charge** (`financial.md` Art. 3).
   > TODO: define the wake metric + rig precisely and randomize test conditions (anti-overfit, R7); set the price schedule.

3.4 **No DRS.** Close following and overtaking come from low-wake cars racing on merit (3.3), not a drag-reduction button. Movable aero, if any, is limited to safety/efficiency via the safety ECU (Art. 8).

3.5 **Reference Plane (plank):** 2026 spec — nominal 10 mm, max 2 mm wear; the cheap, reliable proxy for legal ride height.

   > Rationale (M4): permits 2008-style centre-body inventiveness *without* the processional racing it caused, by pricing the externality instead of banning the geometry.

---

## Article 4 — Chassis, Dimensions & Body — 2008 Basis

4.1 **Dimensions ported from 2008:** maximum width **1800 mm**, the 2008 length/overhang and proportion rules, and 2008 cockpit-opening/templating *except* where superseded by the 2026 safety structures in `safety.md`.

4.1.1 **Zone ownership & precedence.** Where the ported eras overlap, the precedence is **Safety (2026) > Dimensions (2008) > Aero parts (2026) > Bodywork freedom (2008)**. A 2026 part that won't fit a 2008 dimension is **rescaled to the dimension**, never the reverse (except where safety requires). The full zone map and reconciliation are in **`design/chassis-integration.md`**.
   > TODO: transcribe the exact 2008 dimensional set into Appendix T-A; resolve overlaps with 2026 safety geometry (safety wins).

4.2.0 **Underbody precedence.** 2008 ran a *flat/stepped floor with no tunnels*; the **2026 ground-effect floor (Art. 3) fully replaces it.** "2008 body rules" therefore govern only bodywork **above the reference plane** — this prevents the two floor philosophies from colliding (`chassis-integration.md` §4).

4.2 **Body rules ported from 2008** (the more permissive appendage/winglet freedom), disciplined by the wake price (Art. 3.3) rather than by prescriptive 2026 bodywork volumes.

4.3 **Survival Cell & crash structures: 2026 safety basis** (`safety.md` Art. 2). The crash-test outcomes are the invariant; construction method is free provided it passes. Must accept the 2026 cockpit-protection device.

4.4 **Derived dimensional set (first pass, from wheelbase = 3300 mm).** Full derivation in `design/chassis-integration.md` §9.
   - Wheelbase **3300 mm** (chosen — near the 2026 max; 2026 floor X-compressed by only 3300/3400 ≈ 0.971).
   - Max width **1800 mm**; max height **950 mm**; overall length **≈4850 mm**.
   - Front track **≈1520 mm**, rear track **≈1425 mm**.
   - 2026 aero rescaled: lateral ×0.947, longitudinal ×0.971 → **floor planform ≈0.919 of 2026 → ~8% less ground-effect downforce** (a planted car that keeps most of the 2026 floor).
   > TODO: transcribe exact reference volumes into Appendix T-A; ratify tracks/overhangs.

4.5 **Minimum mass: 605 kg** (car + driver, no fuel) — the 2008 F1 minimum, adopted directly: 2008 is our chassis era and there is no hybrid to carry. A naive build with the 2.5 L diesel + 18″ wheels + 2026 safety cell estimates ~632 kg, so 605 kg is a modest **lightweighting target** (~25 kg, paid for by no hybrid + modern composites; `chassis-integration.md` §9b). Add ~80 kg fuel → ~685 kg grid weight. Distribution free; ballast density ≥ 7000 kg/m³, tool-removable only.

---

## Article 5 — Suspension, Brakes & Wheels

### Suspension — 2021 Basis (hydraulically interconnected)

5.1 **Suspension ported from the 2021 chassis rules,** with **hydraulically-interconnected (front–rear) suspension explicitly permitted.**
   > Honesty note: full hydraulic interconnection (FRIC-type) was *restricted* in that F1 era. Formula Zynerji **re-permits it deliberately** — it is exactly the kind of clever mechanical innovation that the forced-disclosure economy makes safe to allow: any advantage is disclosed on-chain and copied, so it rewards engineering merit without a secret-spend arms race. A clean illustration of the formula's philosophy.

5.2 Active (powered, closed-loop) suspension remains banned (driver-skill primacy, Art. 8). Interconnection here is **passive-hydraulic** (springs/inerters/interconnects), not actuated.
   > TODO: draw the precise line between permitted passive hydraulic interconnection and banned active suspension.

5.3 **Cross-era adaptation (critical).** The 2021 suspension basis was a **13″-wheel** design; this car runs **2026 18″ wheels** (Art. 3). The 2021 geometry must therefore be **re-derived for the larger wheel** (unsprung mass, steering, camber/toe envelopes all shift). This is the least obvious integration item — see `design/chassis-integration.md` §5.

### Brakes — newly specified (not era-ported)

> Braking is **pure car-control**, so it is **fully manual** — no ABS, no brake-by-wire, no electronic distribution (Art. 8.4.3). The driver's foot and hand do everything. This is deliberate: with ~1015 hp, ~685 kg and only ~8% less downforce than F1, threshold braking and bias management are major skill differentiators.

5.4 **Friction brakes only.** Carbon–carbon discs and pads (lighter and higher-temperature than carbon-ceramic), one disc per wheel, sized to the 18″ wheel. Up to **six-piston monobloc** calipers (one per wheel). No regenerative braking exists (no hybrid).
   > First-pass dimensions: front disc ≈325–330 mm, rear ≈275–280 mm dia, within the 18″ envelope. TODO: confirm.

5.5 **No ABS, no electronic brake distribution.** Lock-up management and threshold braking are driver skills (Art. 8.4.3).

5.6 **Brake bias is a live manual driver control (Art. 8.4.1).** Front/rear bias is set by a **cockpit-adjustable mechanical bias bar** the driver may trim through a lap or a corner. **No automated bias migration.**

5.7 **No brake-by-wire.** With no regen to blend, the brakes are **fully hydraulic** — the pedal directly modulates clamping force (maximally connected; skill primacy). This is a deliberate divergence from modern F1's rear BBW, which exists only for hybrid blending we don't have.

5.8 **Brake cooling** (ducts, drums, disc hole patterns) is an engineering-merit zone — designed by teams, disclosed on-chain (M10), bounded by the bodywork rules (Art. 4) and the wake price (Art. 3.3). The thermal load is high (heavy, fast, lower-downforce car), so cooling is a genuine development battleground.

### Wheels & Tyres — 2026 Basis, single supplier

5.9 **Wheels:** **18″ rims** (2026 spec), from a **single approved supplier**, common to all entrants. Rim dimensions and any wheel-body aero per the 2026 package (rescaled to track, Art. 3).

5.10 **Tyres — single approved supplier, equal terms.** One tyre supplier serves the whole grid on **identical contractual terms** (input-equalization, R3). This removes the first-order supplier-dependency risk that killed the Tyrrell P34 (`design/precedents-open-class.md`, Lesson 6), sets a known safety baseline, and keeps tyres from becoming a money/chemistry race. Tyres are **not** a development lever; tyre *management* is a driver/engineering skill. A defined dry-compound range plus intermediate and wet; allocation and the multi-compound race rule are sporting (`sporting.md` Art. 3.3).
   > TODO: confirm compound count and the supplier-selection process (tender).

5.11 **No tyre warmers.** Blankets are banned — cold-tyre management (out-laps, restarts, post-stop) is a deliberate driver skill, and it cuts cost. *(A skill-primacy choice; flag for review.)*

---

## Article 6 — Power Unit — the 2-Stroke Diesel

6.1 **Architecture (fixed):** **2.5 litre, inline-5, two-stroke, uniflow-scavenged, compression-ignition (Diesel)** (5 × 500 cc), fuelled by **synthetic e-kerosene (JP-8 class, Appendix T-B)**. Forced induction by a **mechanically-driven screw (Lysholm) supercharger** (positive-displacement; guaranteed scavenging every cycle). **No traction-ERS hybrid** — the powertrain is purely mechanical.

   6.1.1 **Uniflow scavenging.** Fresh charge enters through **intake ports at the bottom of the liner** (uncovered by the piston near BDC, fed by the supercharger) and burnt gas exits through **exhaust poppet valve(s) in the head** — air flows one way, bottom to top. This is the most efficient 2-stroke scavenging method (Detroit Diesel / EMD / Napier Deltic lineage) and is what makes the high BMEP and ~45% efficiency credible. It also *requires* the positive-displacement blower (a uniflow engine cannot self-scavenge). The cam-driven exhaust valves are the pulse source the VLEM (6.7) tunes; exhaust-valve and intake-port timing are development zones (6.6).

6.2 **Rev ceiling: 7000 rpm** (first pass) — diesel combustion is rate-limited and the 2.5 L's bigger 500 cc cylinders rev lower than the 1.5 L would; but because a 2-stroke fires every revolution, the firing cadence still equals a ~14,000 rpm four-stroke.
   > TODO: confirm 7000 against combustion and durability data for 500 cc cylinders.

6.3 **Charge cooling:** intercooling/aftercooling permitted and expected (the engine wants a cool, dense charge).

6.4 **Energy & Power caps (first pass):** peak power **≈758 kW (~1015 hp)**, peak torque **≈1035 N·m**, measured by a sealed Standard Logger. Derived as **BMEP 26 bar × 2.5 L × 7000 rpm / 600** (the 2-stroke power formula; `chassis-integration.md` §9c). At the 605 kg minimum this is **≈1.25 kW/kg (1.68 hp/kg) — turbo-era-F1 power-to-weight**, well above modern F1. Power knob: at 26 bar / 2.5 L, P ≈ 0.1083 × N kW (6900 rpm = 1000 hp).
   > TODO: confirm BMEP 26 assumption against real 2-stroke-diesel data; set the per-km energy cap from race distance.

6.5 **Fuel: synthetic e-kerosene, JP-8 class — a single common fuel (Appendix T-B).** Fully synthetic (carbon-neutral), identical for every entrant — fuel is an **equalized input, not a development lever** (input-equalization, R3). Density-optimized (~0.84 kg/L) for compactness, cetane floor ≥50 for clean compression ignition in the uniflow engine, ultra-low sulfur, minimal additive package. **Race allowance ≈80 kg (~95 L)** — from ≈288 kW avg ÷ ~0.45 efficiency ÷ ~43 MJ/kg; only ~10 kg over F1's 70 kg despite ~40% more power (the diesel advantage).
   > Note: a hydrocarbon's ~43 MJ/kg is fixed, so density buys a *smaller tank* (packaging), not more power. Confirm the allowance and the density/cetane target.

6.6 **Supply model — spec base + open development zones.** A common core unit is supplied; defined zones (e.g. combustion chamber, scavenge ports, supercharger, injection, **the variable-length exhaust, Art. 6.7**) are **open for development**, and that development is uploaded and shared on-chain like every other part (M10).
   > TODO: define the core unit and the exact development zones.

6.7 **Variable-length exhaust manifold (VLEM) — electronically controlled, the primary tuning element.** A 2-stroke's powerband is governed by **exhaust pressure-wave tuning** — the reflected wave returns fresh charge to the cylinder just before the exhaust closes, and that tuning is sharply rpm-specific. The **VLEM is electronically controlled to set the optimal length at every rpm in real time**, so the ~1000 hp is usable across the whole band rather than at a single peak.

   6.7.1 **It is automated *engine-output* optimization, not a driving aid (Art. 8.4).** It optimizes the powerplant; the driver still deploys the torque with no traction control. This is why an *automated* exhaust is permitted where automated *car-control* is not.

   6.7.2 **Set-and-run.** The VLEM control map is **calibrated and locked before the race** (under parc fermé, `sporting.md` Art. 4): **no in-race changes, no driver input.** During the race it runs autonomously on rpm. It is a marquee engine-development/merit zone (6.6), fully disclosed on-chain (M10).
   > A deliberate re-permit (F1 banned variable intake trumpets in 2006): forced disclosure removes the secret-spend objection — any gain is published and copyable.
   > TODO: bound the length range; confirm the locked-map / no-live-reprogramming enforcement.

6.8 **Fuel injection — high-pressure common-rail direct injection.** Electronically controlled, with rail pressure up to **~2500–3000 bar** and multiple injection events per cycle (pilot / main / post) for combustion, noise and emissions control. For the uniflow 2-stroke, **injection timing relative to the port/exhaust-valve events** is the primary combustion lever and a marquee development zone (6.6), disclosed on-chain (M10).
   - Injection control is **automated *engine-output* optimization** (Art. 8.4.2): the map is calibrated and **locked set-and-run** before the race; the driver does not manage injection.
   > TODO: confirm max rail pressure and injector type (piezo vs solenoid) as spec-base vs open-zone.

6.9 **Cooling.** The ~1000 hp diesel, its supercharger and the carbon brakes (Art. 5.8) reject a large heat load. Required circuits: **charge-air cooling** (intercooler/aftercooler — essential for the supercharged 2-stroke; a hot charge wrecks scavenging and power), **engine coolant radiators**, and **oil cooling**. Radiator/intercooler sizing and sidepod ducting are an engineering-merit zone (on-chain, M10), packaged in the 2008-permissive bodywork (Art. 4) and **traded against the wake price (Art. 3.3)** — cooling drag vs aero cleanliness is a genuine optimization. (Diesels run lower exhaust temperatures but reject substantial heat to coolant/oil, so the cooling job is large.)
   > TODO: any minimum-cooling or reliability provision; confirm charge-cooling approach (air-air vs air-water).

---

## Article 7 — Transmission — 2013 Gearbox Basis

7.1 **Gearbox ported from 2013:** **7 forward gears + reverse**, sequential, with the 2013-era **longevity rule** (a gearbox must last a defined number of consecutive events) and season-declared ratios.
   > TODO: confirm the exact 2013 figures (7 forward; ~5-event longevity; ratio-change rules) and transcribe.

7.2 Rear-wheel drive. Differential internals are a merit freedom within the 2013 framework (shared on-chain).

7.3 **Driver-vectored rear differential (permitted — a skill device).** The car runs a **torque-vectoring rear differential commanded in real time by the driver** via steering-wheel-mounted triggers, biasing drive torque across the rear axle (e.g. more torque to the outer wheel to rotate the car mid-corner, to the inner on exit). It is **manual**: the triggers are a continuous driver input, like throttle, brake, or brake-bias — mastering their timing and magnitude is "another test of skill," and so it *strengthens* the driver-merit signal (M7) rather than eroding it.
   > This extends the 2013 (driver-adjustable LSD) basis into live left/right vectoring — a deliberate re-permit of clever mechanical innovation, made safe to allow by forced disclosure (the hardware and control map are on-chain and copyable, M10), like the 2021 interconnected suspension (Art. 5) and the VLEM (Art. 6.7).

   **Actuation detail:**

   7.3.1 **Hardware (twin wet-clutch, GKN Twinster / Nissan-style).** There is **no central differential.** Drive reaches each rear wheel through its **own wet multi-plate clutch pack** on that side of the transaxle. The torque delivered to a wheel is set by **how hard that side's clutch is clamped** — clamp one side more than the other and torque biases to it. (This is the torque-vectoring layout Nissan uses on the Juke/X-Trail.)

   7.3.2 **Driver control — % lockup per side.** **Two digital-proportional steering-wheel triggers**, one per side. Each trigger commands the **percentage of clamp (lockup, 0–100%)** on its side's clutch. The driver modulates both continuously through the corner — clamping the outer side to rotate the car, balancing both to put power down. Managing two clutch triggers alongside throttle, brake and steering is a deep, deliberate skill axis (M7).

   7.3.3 **Baseline & authority.** Triggers neutral = both clutches at a **low common baseline clamp** (enough to transmit drive evenly — behaves like a mild LSD; it cannot be fully open or there is no drive). From there each trigger adds clamp to its side over the full range.
   > TODO: set the baseline clamp level.

   7.3.4 **Open-loop — the legality crux (Art. 8.4.1 vs 8.4.3).** The **trigger-position → clutch-clamp mapping is fixed, declared, and on-chain (M10)**, and the **Standard Safety ECU** actuates clamp pressure from trigger position with **no sensor feedback whatsoever** — no yaw, wheel-slip, steering-angle or speed input may modify the clamp. This is what *proves* it is a manual skill device, not banned automated vectoring: the control law is publicly verifiable and the ECU is spec, so a hidden closed loop is detectable and illegal.

   7.3.5 **Fail-safe:** on loss of signal or hydraulic pressure both clutches default to the **even baseline clamp** (predictable, mild-LSD-like drive) — never an asymmetric or one-side-locked state.

   7.3.6 **Gentle clamp-rate limiter (safety).** The actuator may change a clutch's clamp no faster than a **fixed maximum rate** — first-pass **full 0→100% travel no quicker than ~0.4 s** (≈250%/s) — so a driver retains full authority but **cannot apply an instantaneous lock-up step** that would spit the car off under ~1035 N·m. The limit is a **static, declared, on-chain value** in the trigger→clamp map (not a sensor-reactive loop), so it stays an open-loop manual device (Art. 8.4.1) and is verifiable.
   > TODO: confirm the rate (~0.4 s full travel) once the diff is modelled; it must damp snap-locks without dulling corner-by-corner modulation.

---

## Article 8 — Electronics & Driver Aids (driver-merit primacy)

8.1 **Skill-replacing aids banned:** traction control, ABS, launch control, active (powered) suspension, and any **closed-loop torque vectoring**. The driver must remain a measured variable (supports the Driver-Merit Rating, M7).

8.4 **The defining principle: automate the engine, never the driving.** Three categories:

   8.4.1 **Live manual driver inputs — PERMITTED (this is the skill).** Continuous hand/foot inputs the driver times and modulates throughout the race: throttle, brake, steering, brake bias, and the **driver-vectored differential** (Art. 7.3). Adding such controls is *encouraged* — each is another axis on which driver merit separates (supports M7).

   8.4.2 **Automated *engine-output* optimization — PERMITTED, but set-and-run.** Closed-loop systems that optimize the powerplant's own output without touching car control: the **VLEM** (Art. 6.7), fuel/ignition/boost maps. Permitted because they make power, not driving decisions — the driver still puts that power down unaided. Their calibrations are **locked before the race** (parc fermé, `sporting.md` Art. 4): no in-race changes, no driver input, all on-chain.

   8.4.3 **Automated *car-control* aids — BANNED.** Any closed loop that performs the driver's vehicle-control task from sensors: traction control, ABS, launch control, active (powered) suspension, **closed-loop torque vectoring**.

   **The test:** does the automation perform a *car-control* task (banned), merely *optimize the engine* (permitted, locked), or is it a *live driver input* (permitted, the skill)?

8.2 **Calibration & strategy software free**, provided it implements no banned aid and does not override the safety ECU. (All such software is on-chain, M10.)

8.3 **Standard Safety ECU** governs safety-critical functions only (cap-enforcement interlocks, neutralization speed-delta, pit limiter, any safety/efficiency active-aero). Teams may not modify it.

---

## Article 9 — Homologation, On-Chain Legality & Scrutineering

9.1 **Upload Deadline (M10).** Every part to be run at an event must have its full design record on the Designs ledger by the start of the event. Off-chain parts may not run. New parts = new uploads, visible to all rivals from that moment (the disclosure that drives the head-start economy).

9.2 **Provenance declaration (M11).** On upload, a team declares each part as *original* or *derived from on-chain element X*. Attribution feeds the originator rewards (`financial.md` Art. 3; `blockchain-architecture.md` §4.2).

9.3 **Pre-season homologation:** full 2026 crash-test matrix (`safety.md` Art. 2) — no pass, no race, no waiver — plus the Standard Aero Rig wake measurement (Art. 3.3).

9.4 **Scrutineering by hash.** A fitted part is legal iff it matches its on-chain record (geometry hash + material). Immutable timestamping makes back-dating and secret parts structurally impossible (R5, R7).

9.5 **Event checks:** mass, Reference Plane wear, Standard Logger seal and cap compliance, tyre compliance, full safety check (`safety.md` Art. 6), plus randomized deep inspection of ≥1 car against its on-chain record.

---

## Article 10 — Ancillary & Driver-Interface Systems

10.1 **Electrical system — low-voltage only.** No high-voltage/traction battery exists (no hybrid). A small low-voltage battery + an engine-driven generator powers the ECU, injection, sensors, pumps, the hydraulic actuation of the diff (Art. 7.3) and VLEM (Art. 6.7), telemetry and the Standard Logger. Starting may be by an on-board low-voltage starter or external starter.

10.2 **Steering.** Rack-and-pinion, front wheels only (no rear- or four-wheel steering). **Hydraulic power assist is permitted** — it reduces effort but makes no decisions, so it is not a driver aid (Art. 8.4 — assistance ≠ automation). Active/variable-ratio or electronically-modulated steering is banned.

10.3 **Driver interface (the cockpit is demanding by design).** The driver commands: three pedals (throttle, brake, clutch), sequential shift paddles (7-speed, Art. 7), the **two diff-vectoring triggers** (Art. 7.3), the **brake-bias adjuster** (Art. 5.6), and steering. With **no traction control, no ABS, manual diff vectoring and manual brake bias**, the workload is deliberately high — every manual control is another axis on which driver merit separates (supports M7). All control hardware and mappings are on-chain (M10).

10.4 **Mandatory rear rain light** and other operational signals per `safety.md` / `sporting.md`.

---

## Appendix T-A — Ported Reference Volumes & Dimensions
> Worked through in **`design/chassis-integration.md`** (zone map, the 0.947 lateral rescale, reference wheelbase, underbody replacement, 13″→18″). First-pass dimensional set in that document §9. Remaining: transcribe exact 2008 dimensions + 2026 reference volumes, ratify the reference wheelbase, and resolve safety-geometry overlaps here.

## Appendix T-B — Fuel Specification (Synthetic e-Kerosene, JP-8 class)

A **single common fuel**, mandated and identical for every entrant — fuel is not a development lever (input-equalization). Verified by fuel sampling against this spec + the Standard Logger.

**B.1 Base & sustainability.** A **fully-synthetic ("e-kerosene")** fuel to a **JP-8-class envelope** (MIL-DTL-83133 / NATO F-34 chemistry), produced by sustainable power-to-liquid / Fischer–Tropsch / HEFA routes. Carbon-neutral, and chemically a kerosene — so the engine, the compression-ignition behaviour, and the JP-8 identity are unchanged. Matches the spirit of F1 2026's 100%-sustainable-fuel move while staying distinctively kerosene-diesel.

**B.2 Density-optimized (for packaging, not power).** Composition skewed to the dense, **naphthene/cycloalkane-rich** end of the kerosene range, subject to the cetane floor (B.3):
- Density **~0.84 kg/L** (high end of kerosene).
- Volumetric energy **~35–36 MJ/L** (a few % over baseline JP-8 ≈34.5).
- Gravimetric energy **~43 MJ/kg** — a hydrocarbon constant; **cannot be meaningfully exceeded**.
- Benefit: the ~80 kg allowance fits in a **~95 L** tank (vs ~100 L) → eases packaging, centralizes mass. **Density does *not* raise peak power** (BMEP-limited) — it shrinks the tank.

**B.3 Cetane floor ≥ 50.** Higher than baseline JP-8 (~42–48) for consistent ignition in the uniflow 2-stroke; held by molecular selection + cetane improver. *The density↔cetane tension is this spec's main tuning frontier — dense cyclic molecules resist autoignition.*

**B.4 Ultra-low sulfur ≤ 15 ppm.** Clean combustion; enables any aftertreatment.

**B.5 Minimal additive package (race, not military-logistics):**
- **Lubricity improver — MANDATORY.** Kerosene has poor lubricity; the high-pressure injection system needs it. *A mechanical-protection additive, not a logistics one — it is not optional.*
- **Static dissipator — retained.** Refuelling safety (rapid flow → static); trace quantity.
- **Dropped:** fuel-system icing inhibitor (FSII / de-icer) and long-storage corrosion inhibitors — unnecessary for a fresh, warm, sea-level race fuel system. (Removes complexity/diluent; saves negligible volume — these are trace additives.)

**B.6 Flash point ≥ 38 °C** (kerosene) — a meaningful safety margin over gasoline.

> TODO: ratify the density/cetane target point; finalize additive concentrations; confirm the synthetic production-route certification and life-cycle carbon accounting.

## Appendix T-C — Standard Aero Rig, Wake Metric & Standard Logger
> TODO — load-bearing for Art. 3 (dirty-air pricing) and Art. 6 (energy/power caps); must be precise and hard to overfit.

## Appendix T-D — Engine Core Unit & Open Development Zones
> TODO — define the spec base and the open zones for Art. 6.6.
