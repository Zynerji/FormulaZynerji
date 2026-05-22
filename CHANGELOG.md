# Changelog — Formula Zynerji

All notable changes to the ruleset are recorded here. Versioning: **MAJOR** = change to the objective or core mechanism set; **MINOR** = new article/mechanism; **PATCH** = clarification/typo. Mechanism *calibration* changes should be justified against the objective (does it improve `corr(Standings, Merit)`?) and logged with that justification.

## [0.5.3] — 2026-05-22 — Whitepaper fleshed out (M1–M13 catalogue + dimension appendix)

`whitepaper/whitepaper.pdf` → **8 pages**. Added **Appendix A: the full M1–M13 mechanism catalogue** (ID · mechanism · role · status, with removed/subsumed entries documented) and **Appendix B: the dimension & specification set** (era basis; dimensions & mass; powertrain & economy tables). Recompiled.

## [0.5.2] — 2026-05-22 — Tiered data revenue + figures + LaTeX whitepaper

**Revenue (financial.md Art. 8, blockchain-architecture.md §6):** the shared R&D corpus is now a **product with tiered external access** — competitors free; **media/journalists** paid; **non-competing industry (aerospace/defence/OEM — Boeing, Lockheed)** pay a premium **deep-data tier** (the largest stream). Revenue funds **the sport + prize money (4 championships) + small-team redistribution**, closing the economic loop; a collective-value loop ties richer innovation to a bigger prize fund. Diagram updated (`drawings/blockchain_economy`).

**Figures (`drawings/`):** scripted, reproducible, vector (PDF/SVG/PNG):
- 2D (matplotlib): `car_ga` (3-view GA + dims), `engine_uniflow` (cylinder cross-section + gas path), `diff_schematic` (twin wet-clutch, open-loop), `blockchain_economy` (legality + self-balance + revenue).
- 3D (CadQuery): `car_3d` — parametric GA solid, **STEP exported (`car_3d.step`, committed)** + isometric/side render.

**Whitepaper (`whitepaper/`):** `whitepaper.tex` → compiled to **`whitepaper.pdf`** (7 pp, LaTeX/pdflatex) pulling the formula together with all figures and the model results.

## [0.5.1] — 2026-05-22 — Economic modeling: cap & floor pinned

Built an explicit model (`modeling/economy_model.py`, reproducible/seeded; write-up in `design/economic-modeling.md`) to pin the two keystone numbers instead of guessing.
- **Cap = $75M** (validated): bottom-up cost build puts a competent program at ~$67M, running floor ~$56M, so $75M is ~1.1x competent (tight), ~$19M dev headroom, still binds ~55% of would-be over-spenders.
- **Floor = 80% of cap (~$60M)** — *corrected up from 70%*: the model showed the running floor is ~75% of the cap, so a 70% floor wouldn't bite. The floor must sit just above running to force development.
- **Free-rider problem quantified:** with no floor, teams self-select only **~13%** original-R&D — empirically confirming M12 as the keystone.
- **Honest finding:** vitality rises *monotonically* with the floor at no cost to merit-correlation (~0.97) or field-compression — so the floor is a pure vitality-vs-affordability lever (no internal optimum); origination share kept at ~half (raisable) to preserve copying room.
- Synced cap/floor figures across financial.md, mechanism-design.md, CLAUDE.md. Plots: `modeling/cap_accessibility.png`, `modeling/floor_sweep.png`.

## [0.5.0] — 2026-05-22 — Token-free economy: financials added, self-balance (M2/M3 removed)

User decision: **no token system.** The forced-disclosure economy self-balances, so the development-token currency, development auction (M2), and success handicap (M3) are **all removed** — the biggest simplification in the project's history.

**Financials added (`financial.md` v0.5.0), concrete first-pass numbers:**
- **Cap ≈ $75 M/season** (≈half F1 — shared-design disclosure removes most duplicated R&D + widens the grid). Hard, equal, no luxury-tax lane.
- **Minimum-spend floor ≈ 70 % of cap (≈$52 M)**, of which **≥ half must be original on-chain work** — now the **keystone**: it forces continuous innovation, foreclosing the only bad equilibrium of a token-free copy economy (everyone copies, nobody innovates).
- CapEx ≈ $30 M/3 yr; standard exclusions; CPI+race indexation; penalties = fine + **future-cap reduction** (no token docking).
- **Article 3 "The Self-Balancing Economy"**: disclosure makes advantages transient (copied away → field compresses); the championship pulls everyone to the best on-chain parts; re-leading needs new innovation. Dynasties solved **without a handicap**. Development limited by **money alone** (no ATR/auction).

**Synced everywhere:** M2/M3 marked removed and M11 reframed token-free (reward = head-start + Innovation Index *recognition only*) in `mechanism-design.md`, `blockchain-architecture.md`, `philosophy.md`; **M4 dirty-air re-currencied to a design-stage downforce allowance** (`technical.md` Art. 3.3); sporting/glossary/README/CLAUDE scrubbed of token/auction/handicap. (Real-F1 "token" references in `reference/` and `f1-historical-eras.md` left intact.)

## [0.4.3] — 2026-05-22 — Renamed to Formula Zynerji + first git push

Project **renamed: Formula Synthesis → Formula Zynerji** (Zynerji org branding) throughout all docs and the repo folder. Initialized git and pushed to GitHub (Zynerji org). Lineage: *Open Formula* (v0.1, superseded) → *Formula Synthesis* (v0.2–0.4.2) → **Formula Zynerji** (v0.4.3).

## [0.4.2] — 2026-05-22 — Lapping = elimination ("player-killer"); blue flags abolished (M13)

New signature rule (`sporting.md` Art. 6.7, new mechanism **M13**):
- **No blue flags.** A backmarker is never required to yield — it may **fight** to stay on the lead lap (fair-defence + safety rules still apply).
- **Lapped = out.** A car overtaken by any car a full lap+ ahead is **black-flagged** (no result, no points).
- **Bounty:** the current **P1 earns +1 championship Lapping Point** (Art. 5.5). **Only P1 can ever lap** — a logical necessity of the elimination rule (P1 reaches any backmarker first; a lapped car behind P1 cannot exist for a lower car to take), not an arbitrary restriction.
- **Emergent property:** everyone still running is on the lead lap → **removes lapped-traffic interference** (a real luck source) — a genuine merit side-benefit.
- **Honest costs + controls:** field attrition (the intent) and a mild dominance bounty; controlled by a **grace period** (armed after lap 3 / 10% distance) and an optional per-race point cap. Safety governed by the dangerous-driving rules + invariant.
- Catalog: added **M13** (labelled a spectacle/merit-severity feature, not a distortion-reducer, with the lapped-traffic-luck benefit noted); distortion-map + glossary (blue flag removed, black flag updated) synced.

## [0.4.1] — 2026-05-22 — Removed output-side luck-suppression (conventional racing)

Design decision: the three **output-side** luck correctors are **removed** in favour of conventional racing. Meritocracy now rests on the inputs (forced disclosure, money-neutral cap, skill-primacy car), the long 22-round sample, and the luck-robust DMI — not on correcting outputs. The title now carries ordinary race-day variance (a deliberate point on the meritocracy↔tradition dial).
- **Drop-results — removed.** Every round counts (`sporting.md` Art. 1.3, 5).
- **Qualifying track-evolution normalization — removed.** Standard knockout on raw times; track-reading is qualifying craft (Art. 3.2).
- **Time-neutral neutralization — removed.** Conventional VSC + safety car + red flag, accepting normal safety-car variance (Art. 7, renamed "Neutralization & Safety Car").
- **Catalog synced:** M5 marked removed; M6 reduced to the points curve (+ no-FL/sprint); M8 reduced to track limits + parc fermé; distortion-map and §5 updated. Glossary updated.
- **Kept:** points curve (all 22 score), the DMI, sensor track limits, parc fermé, hash-scrutineering, Economics article.

## [0.4.0] — 2026-05-22 — Competition side built out (the meritocracy estimator)

`sporting.md` → **v0.4.0**, made concrete throughout (the meritocracy math now runs):
- **Structure:** grid 11×2 = 22; calendar **K = 22**; **three classifications** — Constructors', Drivers', and an **advisory Driver-Merit Index** with its own "Driver-Merit Champion" award.
- **Points curve (M6):** **all 22 finishers score**, convex front (**40 → 1**), non-zero tail — measures the *whole field* vs F1's top-10-only (a lower-bias estimator).
- **Drop-results (M6):** best **20 of 22** — modest, to cushion luck without erasing reliability merit (tension stated). Rejected "no-fault DNF" (too gameable).
- **Field-strength weighting dropped** for points — a no-op within a constant-field season (honest discipline); it lives only in the DMI model.
- **Driver-Merit Index (M7):** hierarchical Bayesian, **teammate-referenced** (shared car_effect), one-scale via cross-team links, **on-chain-reproducible**, **advisory** (doesn't decide the title → near-ungameable).
- **Qualifying (M8):** knockout **+ track-evolution normalization** (lap times corrected to a common track state — removes run-order luck).
- **Neutralization (M5):** **time-neutral SC** — record gaps at deployment, neutralize the pit windfall, restore gaps at restart; VSC gap-preserving default.
- **Track limits** sensor-measured; licence penalty points (12 / 12 mo = ban).
- **New Art. 11 Economics & Prize** — prize fund + data-revenue redistribution so a mid-field team can break even (Lesson 5: close the economic loop).

## [0.3.5] — 2026-05-22 — Remaining car systems (injection, wheels/tyres, cooling, ancillaries)

The car is now systems-complete. Added to `technical.md`:
- **Fuel injection (Art. 6.8):** high-pressure common-rail DI, ~2500–3000 bar, multi-event; injection timing vs port/valve events is the primary combustion lever; automated engine-optimization, set-and-run, on-chain dev zone.
- **Cooling (Art. 6.9):** charge-air (intercooler — essential for the supercharged 2-stroke), engine-coolant and oil circuits; sizing/ducting is a merit zone traded against the wake price (Art. 3.3).
- **Wheels & tyres (Art. 5.9–5.11, article renamed "Suspension, Brakes & Wheels"):** 18″ rims, **single approved tyre supplier on equal terms** (input-equalization; the Tyrrell-P34 supplier-risk lesson); tyres not a dev lever; **no tyre warmers** (cold-tyre management = skill, + cost).
- **Ancillary & driver-interface (new Art. 10):** low-voltage-only electrical (no HV/hybrid); rack-and-pinion with hydraulic power assist permitted (assistance ≠ automation), no rear/4-wheel steer; **driver-interface summary** — deliberately high manual workload (no TC/ABS, manual diff + bias) as a driver-merit axis (M7); mandatory rain light.

## [0.3.4] — 2026-05-22 — Fuel spec (synthetic e-kerosene) + uniflow engine

**Fuel (`technical.md` Art. 6.5 + Appendix T-B):** **synthetic e-kerosene, JP-8 class, single common fuel** (carbon-neutral; an equalized input, not a development lever). **Density-optimized ~0.84 kg/L** (naphthene-rich) for a smaller tank (~95 L) — honest note: gravimetric energy (~43 MJ/kg) is a hydrocarbon constant, so density buys *packaging*, not power. **Cetane floor ≥50**, **ULS ≤15 ppm**. **Minimal additives:** lubricity (mandatory — injection protection) + static dissipator (refuelling safety) retained; **de-icer (FSII) and storage corrosion inhibitors dropped** (military-logistics baggage, not needed for race use). Race allowance confirmed ≈80 kg.

**Engine architecture (`technical.md` Art. 6.1.1):** clarified as **uniflow-scavenged** — intake ports at the liner bottom (blower-fed), exhaust poppet valves in the head; most-efficient 2-stroke scavenging (Detroit Diesel / EMD / Deltic lineage), underpins the high BMEP & ~45% efficiency, and *requires* the positive-displacement blower. Cam-driven exhaust valves are the pulse the VLEM tunes.

## [0.3.3] — 2026-05-22 — Brakes + driver-vectored diff actuation

**Brakes (new, `technical.md` Art. 5.4–5.8 — grouped under "Suspension & Brakes"):** carbon–carbon discs/pads sized to the 18″ wheel, up to 6-piston monobloc calipers; **no ABS, no brake-by-wire, no electronic distribution** (braking is pure car-control → fully manual, Art. 8.4.3); **brake bias is a live manual driver control** via a cockpit bias bar (Art. 8.4.1); brake cooling is an on-chain merit zone. No regen (no hybrid). Friction brakes only, fully hydraulic pedal.

**Driver-vectored diff actuation (`technical.md` Art. 7.3.1–7.3.5):** **twin wet-clutch torque vectoring** (GKN Twinster / Nissan-Juke style — a clutch pack per side, no central diff). Two digital-proportional steering-wheel triggers set the **% lockup of each side's clutch**; neutral = even baseline clamp (mild LSD). **Legality crux:** the trigger→clamp map is fixed, declared, on-chain, and the Standard Safety ECU adds **no sensor feedback** — proving it's a manual skill device (Art. 8.4.1), not banned automated vectoring (8.4.3). Fail-safe defaults to even baseline clamp. **Gentle clamp-rate limiter** added (Art. 7.3.6): full travel no faster than ~0.4 s — a static on-chain value (not a sensor loop), prevents snap lock-ups while staying open-loop/legal.

## [0.3.2] — 2026-05-22 — Wheelbase 3300 mm, ~1000 hp engine, derived spec sheet

**Decisions:** Reference Wheelbase **3300 mm** (planted, near the 2026 max); engine grown to **2.5 L** at **26 bar BMEP** targeting **~1000 hp**; **minimum weight 605 kg** (the 2008 figure — no hybrid to carry); **electronically-controlled VLEM** (set-and-run); **driver-vectored rear differential**.

**Derived (first pass) into `chassis-integration.md` §9 + `technical.md` Art. 4/6/7/8:**
- 2026 floor X-compressed 3300/3400 ≈ 0.971 × 0.947 lateral → **floor ≈0.919 of 2026 → ~8% less downforce** (a planted car that keeps most of the 2026 floor).
- Dimensions: width 1800, height 950, **length ≈4850 mm**, **front track ≈1520 / rear ≈1425 mm**, front wing ≈1800 mm.
- **Minimum mass 605 kg** (2008 min; naive build ~632 kg → a ~25 kg lightweighting target, paid by no-hybrid + modern composites); +~80 kg fuel → ~685 kg grid.
- Powertrain: **2.5 L I5 2-stroke diesel, 7000 rpm, ≈758 kW (~1015 hp), ≈1035 N·m** (BMEP 26 × 2.5 L × 7000 / 600), **≈1.25 kW/kg (1.68 hp/kg) — turbo-era-F1 power-to-weight**.
- **Fuel ≈80 kg / ~100 L JP-8** (revised down from 95 — realistic ~45% diesel efficiency; only ~10 kg over F1 despite ~40% more power).
- **VLEM electronically controlled** (Art. 6.7) — optimal length at every rpm; **automated *engine* optimization, not a driving aid**; map set-and-locked pre-race.
- **Driver-vectored rear differential** (Art. 7.3) — steering-wheel triggers bias rear-axle torque live; permitted *because manual*; strengthens driver-merit (M7).
- **Art. 8.4 refined → "automate the engine, never the driving":** live manual driver inputs permitted; automated engine-output optimization permitted but set-and-run/locked; automated car-control aids banned.

All figures first-pass with derivation shown, flagged for ratification (BMEP/efficiency, ERS-removal & diesel-package mass, exact 2026 tyre widths/overhangs, diff & VLEM actuation bounds).

## [0.3.1] — 2026-05-22 — Minimum-spend floor (M12) + chassis integration study

**Added**
- **Mechanism M12 — minimum origination floor** in `design/mechanism-design.md`: the *stick* that completes the free-rider cure (M10 forces sharing, M12 forces contribution, M11 rewards leadership). Mandatory minimum development spend with **origination teeth** (a share must produce original on-chain designs), turning the cap into a **budget band [floor, cap]**. Updated the distortion-map, §5 calibrations, and M10's failure-mode line.
- `design/chassis-integration.md` — the 2026-spec-parts-onto-2008-dimensions study: zone-ownership map + precedence rule, the 1800/1900 ≈ 0.947 lateral rescale, reference-wheelbase decision, the 2026-ground-effect-floor-replaces-2008-flat-bottom resolution, the 13″→18″ change (and its forced adaptation of the 2021 suspension), powertrain-vs-tunnel packaging, and a first-pass dimensional set.

**Changed**
- `regulations/financial.md` → Article 2 is now **"The Budget Band: Cap + Floor"** with the minimum spend (2.6), origination teeth (2.7), and shortfall penalty (2.8).
- `regulations/technical.md` — Art. 3.1/4.1.1/4.2.0 add zone-ownership & precedence and point to the integration study; **fixed 2026 width to 1900 mm** (was mistakenly 2000); Art. 5.3 adds the critical 2021-suspension-to-18″-wheel adaptation; Appendix T-A references the study.
- `design/blockchain-architecture.md` — §4 free-rider resolution now "carrot + stick + head-start" with new §4.4 (the floor); §8 adds the free-riding row.
- `README.md`, `glossary.md` — add M12 / the floor / the budget band / zone ownership / the integration doc.

**Open calibrations** (new): floor level F (as % of cap → band width) + origination minimum N; reference wheelbase; lateral rescale vs trim; 2021-suspension geometry for 18″ wheels; powertrain-vs-tunnel packaging envelope.

## [0.3.0] — 2026-05-22 — The spine: blockchain, the diesel, and the era-kitbash car

Added the user's core concepts. The **blockchain becomes the spine** of the formula, and the car/engine are now concretely specified.

**Added**
- `design/blockchain-architecture.md` — forced on-chain disclosure (M10) + originator rewards (M11): the economic argument (R&D as a club good → collapsed spend → dissolved dynasties), the four ledgers (Rules/Designs/Data/Manpower), the "only on-chain parts are legal" model, the patent-dilemma resolution (natural lead + originator rewards; embargo rejected), data revenue, manpower ledger, architecture notes, failure modes, calibrations.
- `design/mechanism-design.md` — new mechanisms **M10** (forced disclosure, the spine) and **M11** (originator rewards); M3 handicapping downgraded to a *backstop* and M9 monitoring noted as subsumed by the on-chain ledger; updated distortion-map and regulation-map.

**Decisions captured** (via Q&A)
- Engine: **1.5 L inline-5 two-stroke diesel on JP-8, mechanical screw (Lysholm) supercharger, no traction hybrid**, diesel rev ceiling ~6–8k (tunable), **spec base + open development zones**.
- Head-start: **natural lead + originator rewards** (no embargo, no originator data-cut).
- Car: era kitbash — 2026 wings/floor/tyres/safety · 2021 hydraulic interconnected suspension · 2013 gearbox · 2008 dimensions/body.

**Changed**
- `regulations/technical.md` — rewritten to the concrete era-kitbash car + the 2-stroke diesel (Art. 6) + 2013 gearbox (Art. 7) + 2021 interconnected suspension (Art. 5) + 2008 dimensions/body (Art. 4) + 2026 aero with dirty-air pricing (Art. 3) + on-chain legality & scrutineering-by-hash (Art. 9). New appendices incl. the 2026-on-2008 integration task.
- `regulations/financial.md` — on-chain cost/manpower ledger (native M9); originator rewards paid in Development Tokens (Art. 3.4); handicap dialled to a backstop (Art. 3.3); data-revenue + manpower (Art. 8).
- `regulations/sporting.md` — component/IP article reframed for forced disclosure (no durable exclusive IP; Innovation Index); scrutineering-by-hash (Art. 6.6).
- `README.md`, `glossary.md` — feature the blockchain spine and the concrete car/engine.

**Open calibrations** (new): originator-reward strength (the master knob / patent-term analogue); the 2026-aero-on-2008-dimensions integration; engine rev ceiling, energy/power caps, JP-8 spec, core-unit vs open-zones split; whether M3 handicap is needed at all given M10; data-revenue redistribution formula; manpower headcount limit.

## [0.2.0] — 2026-05-22 — Reframe: Formula Zynerji (mechanism-design / meritocracy)

Project re-founded after the user clarified the concept. **This is not an open formula.** It is a redesign of the F1 rulebook as mechanism design, with **meritocracy** as the objective and **game theory + revealed history** as the method. Renamed Open Formula → **Formula Zynerji**.

**Added**
- `design/mechanism-design.md` — the framework: the estimator model (`Standings = Merit + Luck + Budget + Gaming`), nine design razors (R1–R9), and the mechanism catalog M1–M9 with incentive analysis (money-neutral cap, development auction, merit-weighted handicapping, dirty-air pricing, luck-suppressing neutralization, estimator design, driver-merit disentanglement, anti-gaming sporting rules, cost monitoring).

**Changed**
- `design/philosophy.md` — rewritten around meritocracy, the estimator framing, the three distortions, and the variance razor. The v0.1 "open box / outcome-not-component" thesis is superseded.
- `README.md`, `CLAUDE.md` — rewritten to the new framing.
- `regulations/financial.md` — money-neutral hard cap (no luxury-tax lane), development-token auction, merit-weighted handicapping (inputs only), randomized audits + related-party pricing.
- `regulations/sporting.md` — recast as the championship *estimator*: points curve + drop-results + field-strength weighting; gap-preserving neutralization + time-credit; **DRS removed**; hard-measured track limits; order-effect-corrected qualifying; official Driver-Merit Rating (advisory vs binding open).
- `regulations/technical.md` — F1-derived prescriptive car (no longer an open box); **dirty-air externality pricing (M4)** replaces prescriptive wake geometry and DRS; driver-skill primacy (aids banned).
- `regulations/safety.md` — reframed from "wall of the box" to the **invariant constraint** (never an objective, never optimized against).
- `glossary.md` — new mechanism-design terms.

**Retained as behavioural evidence**
- `design/f1-historical-eras.md`, `design/precedents-open-class.md`, `reference/*` — now read as revealed-preference data on how teams respond to incentives.

**Open calibrations** (see `design/mechanism-design.md` §5): cap value; token endowment; auction format; handicap-curve strength; dirty-air metric/rig/price currency; points vector + N-of-K; driver-rating advisory-vs-binding; the deliberate luck-variance floor.

## [0.1.0] — 2026-05-22 — Initial draft (superseded framing: "Open Formula")

Original open-class concept (define a Box, free inside). Established the four regulation pillars and gathered the F1 research now repurposed as behavioural evidence. Superseded by 0.2.0; the regulation *structure* and research survive, the *philosophy* was replaced.

## [0.1.0] — 2026-05-22 — Initial draft

Project founded. Established the open-class thesis (freedom of 1966–1982 F1 inside modern safety/cost armour) and the four-wall Box.

**Added**
- `design/philosophy.md` — central thesis, the three failure modes, the four-wall Box, outcome-over-component, anti-dominance-without-BoP.
- `design/f1-historical-eras.md` — F1 rulesets era-by-era as the design basis, with what we take from each era.
- `design/precedents-open-class.md` — lessons from Group B, Can-Am, Formula Libre, 1970s F1, Formula SAE, unlimited classes, and BoP.
- `regulations/technical.md` v0.1 — the Box and the free interior (aero, chassis, energy/power pinch-point, electronics, envelope, tyres, scrutineering).
- `regulations/safety.md` v0.1 — non-negotiable, outcome-based safety floor; crash matrix; powertrain-agnostic energy-storage safety; circuit/spectator/medical minimums.
- `regulations/sporting.md` v0.1 — championship, eligibility, format, points, penalties, neutralisation, component classification, Innovation Class, supermajority rule-change.
- `regulations/financial.md` v0.1 — budget cap, ATR sliding scale, audit, breaches/penalties, optional minimum-spend floor and scored cost event.
- `reference/` — digests of the real FIA Technical, Sporting, Financial, and Safety regulations, with citations.
- `glossary.md`, `README.md`, `CLAUDE.md`, `LICENSE`.

**Open decisions** (see `> TODO:` markers): headline numbers (energy/power caps, mass, envelope, cost cap); spec vs open tyres; per-lap vs per-km energy; whether to keep an explicit downforce ceiling; cars-per-team and grid size; the feeder-series licence ladder; single vs split chassis/powertrain cost caps; adoption of the optional minimum-spend floor and scored cost event.
