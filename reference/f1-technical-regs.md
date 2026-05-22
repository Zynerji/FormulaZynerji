> **Reference digest — not part of the ruleset.** A synthesis of how the real FIA F1 *Technical* Regulations are structured and what their key levers are, gathered to inform Open Formula's `regulations/technical.md`. Compiled May 2026 with citations. Treat as read-mostly source material.

# FIA Formula 1 Technical Regulations: Reference Digest for Open Formula Design

## 1. DOCUMENT STRUCTURE

The FIA F1 regulations are published as a multi-section framework. The Technical Regulations are **Section C**.

### The Six Sections of the 2026 Regulatory Package

| Section | Subject |
|---|---|
| A | General Provisions |
| B | Sporting Regulations |
| **C** | **Technical Regulations** |
| D | Financial Regulations — Teams (cost cap) |
| E | Financial Regulations — Power Unit Manufacturers |
| F | Operational Regulations |

### Section C (Technical) — Article Skeleton (~260 pages)

| Article | Subject |
|---|---|
| C1 | General Principles — dangerous-construction clause, new-technology approval, competitor duty |
| C2 | Definitions — car definition, coordinate systems, reference volumes/surfaces, sprung/unsprung mass |
| C3 | Aerodynamic Components & Bodywork — longest article; every external surface by reference volume; floor, fences, diffuser, wings, active aero; plank & skid |
| C4 | Car Mass — minimum mass, ballast density, heat-hazard allowance |
| C5 | Car Construction — survival cell, roll/impact structures, headrest, halo, fuel-cell location |
| C6 | Suspension & Steering — geometry zones, active-suspension ban, wheel retention |
| C7 | Power Train — gearbox (≥8 fwd + reverse, sequential), differential, rear-drive mandate |
| C8 | Power Unit — references PU Technical Regs (1.6L V6, MGU-K, ES, CE, fuel-flow meter) |
| C9 | Electrical Systems — standard ECU, active-aero ECU control, telemetry |
| C10 | Fuel System — bladder spec, fuel-flow meter, samples, sustainable-fuel certification |
| C11 | Brakes — independent per axle, brake-by-wire rear allowed |
| C12 | Tyres & Wheels — single supplier (Pirelli), 18" rims, allocation |
| C13 | Safety Equipment — fire suppression, extraction, marshalling lights, harness, HANS |
| C14 | Ballast & Measurement |

Appendices: C3 drawings; C4 PU perimeter; C5 PU/fuel homologation 2026–2030; C6 components classification (Listed/Transferable/Standard); C7 approved future changes.

## 2. KEY NUMERIC LIMITS

### Mass
| Parameter | 2025 | 2026 |
|---|---|---|
| Min car mass (w/ driver, no fuel) | 800 kg | 768 kg |
| Driver + seat min | 82 kg | 82 kg |
| Race fuel load | 110 kg | 70 kg |
| Ballast density | 7,500 kg/m³ | 7,500 kg/m³ |

### Dimensions
| Parameter | 2022–2025 | 2026 |
|---|---|---|
| Max width | 2,000 mm | 1,900 mm |
| Max height | 950 mm | 950 mm |
| Max wheelbase | 3,600 mm | 3,400 mm |
| Tyre diameter (front/rear) | 720/720 mm | ~705/~690 mm |
| Rim diameter | 18" | 18" |

### Power Unit
| Parameter | 2014–2025 | 2026 |
|---|---|---|
| Architecture | 1.6L 90° V6 turbo | unchanged |
| Max RPM | 15,000 | 15,000 |
| ICE output | ~550 kW | ~400 kW |
| MGU-K | 120 kW | 350 kW |
| MGU-H | present | removed |
| Total system | ~700–750 kW | >745 kW (~1,000+ hp) |
| ICE/electric split | ~85/15 | ~50/50 |
| Fuel flow limit | 100 kg/h | 3,000 MJ/h (energy-based) |
| Fuel type | 10% bio | 100% advanced sustainable |

### Floor / Plank
Plank nominal 10 mm ±0.2; min 8 mm after racing (2 mm wear). 2026 adds mandatory titanium/steel front skid to prevent ride-height tricks.

### Crash loads (2026 increases)
Roll hoop full load 140→172 kN; fuel-tank side 50→110 kN; cockpit floor 30→75 kN; etc.

## 3. THE "BOX" PHILOSOPHY — PRESCRIBED vs FREE

- **Extremely prescribed (reference-volume geometry):** all external aero surfaces, floor, active-aero authority, survival-cell geometry, plank/skid, roll hoop, wheel size, ECU, fuel-flow meter.
- **Partially prescribed:** suspension (pickup zones regulated, tuning free; active banned), sidepod/bodywork outer boundary, brakes (independent per axle required; design free).
- **Relatively free:** engine internals above the bottom end, energy deployment strategy, gearbox ratios, cooling architecture, software/calibration.

## 4. HOMOLOGATION & SCRUTINEERING

Pre-season mandatory crash tests at FIA facilities (front/rear/side/roll/cockpit-floor/steering); no pass, no race. Gearbox cassette homologated per season. PU homologated with token-based in-cycle development (2026–2030). Components classified Listed / Transferable / Standard.

In-season: parc fermé from qualifying; weight, tyre pressures, fuel sample, plank thickness (micrometer), wing-flex deflection tests, ride-height checks. At least one car per event gets invasive inspection vs submitted CAD. Technical Directives interpret the regs in-season. Notable enforcement: Hamilton/Leclerc DSQ for plank wear (2023 US GP); Vettel DSQ for insufficient fuel sample (2021 Hungary).

## 5. EIGHT TECHNICAL LEVERS FOR AN OPEN-CLASS RULESET
1. **Total energy budget (MJ/lap or /km), not a mandated source** + a separate peak-power cap.
2. **Envelope box (L×W×H) + min wheelbase**, don't draw the shape.
3. **Min mass with driver + ballast-density floor.**
4. **Mandatory safety cell + defined crash-test program** (outcome, not method).
5. **Aero reference volume + ride-height-stability/plank rule** to kill the ground-effect cliff.
6. **Tyre control** (single supplier or defined envelope) — without it, instant tyre war.
7. **Standard ECU for safety-critical functions**; leave calibration/strategy open.
8. **Component classification + IP rules** with mandatory data submission.

## Sources
- FIA 2026 Technical Regs Section C (Issue 17, Apr 2026): https://www.fia.com/system/files/documents/fia_2026_f1_regulations_-_section_c_technical_-_iss_17_-_2026-04-28.pdf
- FIA 2026 hub: https://www.fia.com/F126
- FIA 2025 Technical Regs Issue 03: https://www.fia.com/sites/default/files/documents/fia_2025_formula_1_technical_regulations_-_issue_03_-_2025-04-07.pdf
- FIA 2026 PU Technical Regs Issue 7
- Formula1.com 2026 rules explainer; X/Z-mode aero explainer
- motorsport.tech 2026 deep dives; F1Chronicle (mass/fuel-flow/aero/gearbox); GPFans (dimensions); Motor Sport Magazine; PlanetF1; ScuderiaFans (floor/plank); The-Race (boost/overtake/active aero); FIA Insights (post-race legality); Wikipedia (F1 regulations); Sky Sports.
