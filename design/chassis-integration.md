# Formula Zynerji — Chassis Integration Study: 2026 Spec Parts on 2008 Dimensions

The era-kitbash car's principal engineering task: fit **2026 wings / floor / tyres / safety** onto **2008 chassis sizing**, with **2021 suspension**, a **2013 gearbox**, and the new **2-stroke diesel**. This document resolves the conflicts. It feeds `regulations/technical.md` Appendix T-A.

> Approximate historical figures are marked ≈; exact regulation transcription is flagged `> TODO`.

---

## 1. The principle: zone ownership

Most conflicts dissolve once you assign each part of the car to the era that governs it:

| Zone | Era owner | Note |
|------|-----------|------|
| Overall dimensions — width, height, length/overhang, wheelbase limit | **2008** | The "sizing" basis (≈1800 mm wide, ≤950 mm high) |
| Underbody — floor, venturi tunnels, diffuser, plank | **2026** | Ground effect; *replaces* the 2008 flat-bottom |
| Front wing, rear wing | **2026** | Active aero (X/Z-mode) |
| Tyres, wheels, rims | **2026** | 18″ rims |
| Upper bodywork — sidepods, engine cover, appendages, winglets | **2008** | The permissive "body rules" |
| Survival cell, crash structures, halo | **2026** | The safety invariant |
| Suspension | **2021** | Hydraulically interconnected |
| Gearbox | **2013** | 7-speed + longevity |
| Engine | **new** | 2.5 L I5 2-stroke diesel |

**Precedence rule** (resolves any overlap): **Safety (2026) > Dimensions (2008) > Aero parts (2026) > Bodywork freedom (2008).** Where a 2026 part will not fit a 2008 dimension, the **part is rescaled to the dimension** — never the dimension expanded — except where safety requires.

---

## 2. Dimensional reconciliation (the easy part)

The width gap is small: 2008 ≈ **1800 mm**, 2026 = **1900 mm**.

- **Lateral (Y) rescale factor = 1800 / 1900 ≈ 0.947**, applied to all 2026 aero reference volumes (front wing, floor width, rear wing, diffuser).
- **Vertical (Z): unchanged** — both eras cap height at ≈950 mm and both use a 10 mm plank, so the 2026 surfaces keep their native height.
- **Longitudinal (X): tied to the Reference Wheelbase** (§3).

This is a proportional narrowing, not a redesign — it preserves the 2026 aero philosophy (and therefore the dirty-air behaviour the wake price, M4, depends on).
> TODO: ratify *rescale* vs *trim-outermost-100 mm*. Rescale preserves aero balance; trim is simpler but alters behaviour. Recommend **rescale**.

---

## 3. Wheelbase & length — **DECIDED: 3300 mm**

**Reference Wheelbase = 3300 mm** (close to the 2026 ≤3400 mm dimensioning). The 2026 underbody is **X-compressed by only 3300/3400 ≈ 0.971** to fit — so the floor stays near-native lengthwise (§4, §9).

**Consequences (the derivation cascade):**
- **Longitudinal floor scale 0.971** combines with the **lateral scale 0.947** (§2) → floor planform ≈ **0.947 × 0.971 ≈ 0.919** of the 2026 footprint, i.e. **~8% less floor area → ~8% less ground-effect downforce** (notably more than the 3100 mm option's ~14% loss — the longer floor recovers downforce).
- A **3300 mm wheelbase is stable and planted** (close to the 2026 max), far less pitch-sensitive than a short car — well-suited to a ground-effect floor, which dislikes pitch.
- Combined with the **~1000 hp** torque-monster diesel (§7, and `technical.md` Art. 6) and **no traction control**, the emergent identity is a **planted but ferociously powerful car**: ~1.25 kW/kg (turbo-era-F1, above modern F1) with only ~8% less downforce than 2026. Stability tempers the savagery, but ~1035 N·m through the rear with no electronic safety net still makes it a **handful on power** — which is exactly what the **driver-vectored diff** (Art. 7.3) is there to manage. Still strongly driver-defined.
- **Overall length ≈ 4850 mm** = 3300 wheelbase + ≈900 front overhang + ≈650 rear overhang.
- **Bonus:** the longer wheelbase **eases the engine-packaging constraint** (§7) — more room for the long I5 + tunnels.

---

## 4. The underbody — 2026 ground effect onto a 2008 car (the hard one)

2008 ran a **flat/stepped floor + plank, with NO venturi tunnels** (ground effect was banned 1983–2021). 2026 is a **ground-effect venturi floor**. So:

- **The 2026 underbody fully replaces the 2008 flat-bottom rule.** "2008 body rules" therefore govern only the bodywork **above the reference plane** (§1). This must be stated explicitly in the regs so the two floor philosophies don't collide.
- **Packaging consequence (the real constraint):** venturi tunnels need vertical volume rising into the car ahead of the rear axle. The chassis must give that volume, which means the **engine and gearbox must package high/narrow enough to clear the tunnel exits and the diffuser.** This directly constrains the diesel installation (§7).
- **Reference plane / plank:** 2026 spec (10 mm nominal, titanium front skid, 2 mm max wear).

---

## 5. Wheels & tyres — 13″ → 18″ (forces a suspension adaptation)

- 2008 = **13″ rims**, ≈660 mm grooved tyres. 2026 = **18″ rims**, ≈705 mm front / ≈690 mm rear slicks.
- Adopting 2026 tyres on the 2008 chassis requires **18″ uprights and hubs, larger brakes** (18″ permits them), and revised wheel-end geometry.
- **Cross-era catch:** the **2021 suspension** basis was itself a **13″-wheel** design (18″ arrived in F1 in 2022). So the 2021 suspension geometry must be **adapted to 18″ wheels** — the unsprung mass, steering, and camber/toe envelopes all shift. This is the least obvious integration item and must be called out in the suspension article.
- **Coherence win:** the 2026 tyre diameter sets the ride-height datum, and we pair it with the 2026 floor — so tyre and floor are from the *same* era and internally consistent. Only their relationship to the *2008-sized chassis* needs work.

---

## 6. Survival cell & safety — 2026 within 2008 dimensions

- The **2026 survival cell, crash structures, and halo** (the safety invariant) are packaged within the 2008 envelope (≈1800 mm wide, ≤950 mm high).
- Feasibility: 2026 cells are comfortably **< 1800 mm** wide, so width is fine; the **halo adds height/structure** the 2008 car lacked, but within the 950 mm height limit. Safety wins all precedence (§1), so where the 2026 cell needs space, the 2008 bodywork yields.

---

## 7. Powertrain packaging — the diesel in a 2008 body around 2026 tunnels

- The **2.5 L inline-5 2-stroke diesel** is a **long** engine (five 500 cc cylinders in a row), and the **bigger screw (Lysholm) supercharger + larger intercoolers** needed for ~1000 hp add real bulk.
- It must fit the **2008 (permissive) sidepod/engine-cover volume** *while clearing the 2026 venturi tunnels and diffuser* (§4). The permissive 2008 bodywork helps (room for intercooler ducting); the 2026 tunnels hurt (they steal lower-rear volume).
- **Eased by the 3300 mm wheelbase:** a long I5 packaged around ground-effect tunnels is still tight, but the longer wheelbase gives meaningfully more room than the 3100 mm option. The engine is a longitudinal stressed member behind the driver, sharing the wheelbase budget with the fuel cell (~100 L, §9c) and the tunnel volume. Still worth checking early, but no longer the *binding* constraint.
- The **2013 gearbox** must mount to a structure that carries the **2026 rear-wing and rear-crash loads** and clears the diffuser.
> TODO: define the powertrain packaging envelope (engine height/length, blower + intercooler positions) against the tunnel/diffuser volume.

---

## 8. Cross-era interaction flags (the non-obvious ones)

1. **2021 suspension ⇄ 2026 18″ wheels** — geometry must be re-derived for the larger wheel (§5).
2. **2013 gearbox ⇄ 2026 rear loads + diffuser** — mounting and clearance (§7).
3. **2008 bodywork freedom ⇄ 2026 wake price (M4)** — 2008-style appendages are allowed but the dirty-air price disciplines them (`technical.md` Art. 3.3).
4. **2008 dimensions ⇄ 2026 safety cell** — safety wins; bodywork yields (§6).

---

## 9. Derived spec sheet (first pass, from wheelbase = 3300 mm)

### 9a. Dimensions

| Parameter | Derived value | How derived |
|-----------|---------------|-------------|
| Wheelbase | **3300 mm** | chosen (§3) |
| Max width (overall) | **1800 mm** | 2008 |
| Max height | **950 mm** | 2008/2026 (same) |
| Overall length | **≈4850 mm** | 3300 + ≈900 front OH + ≈650 rear OH |
| Front track (centre–centre) | **≈1520 mm** | 1800 − front tyre width ≈280 |
| Rear track (centre–centre) | **≈1425 mm** | 1800 − rear tyre width ≈375 |
| Front wing width | **≈1800 mm** | 2026 full-width, ×0.947 to track |
| Rear wing width | 2026 × 0.947 | lateral rescale (§2) |
| Floor / diffuser | 2026, **Y×0.947, X×0.971** | → planform ≈0.919 of 2026 → ~8% less DF (§3) |
| Plank | 10 mm + Ti front skid, 2 mm wear | 2026 |
| Wheels / tyres | **18″ rims; ≈705 mm F / ≈690 mm R; ≈280 F / ≈375 R wide** | 2026 (widths reduced from 305/405) |
| Survival cell + halo | 2026 spec, within the 1800×950 envelope | 2026 (safety wins) |

> Tyre widths and overhangs are ≈ first-pass; transcribe exact 2026 figures into Appendix T-A.

### 9b. Minimum mass — **set to 605 kg**

Adopted directly: **605 kg** was the 2008 F1 minimum (no hybrid, V8, 13″ wheels) — and 2008 is our chassis era. With no hybrid to carry, the car returns to that era's weight. Sanity check of the deltas vs the 2008 car:

| Δ vs the 2008 car | ~kg | Note |
|-------------------|-----|------|
| 2.5 L 2-stroke diesel + blower + intercoolers vs 2008 V8 | **+~25** | diesel is heavier than the V8, but only modestly — +1 L over a 1.5 L base is bigger bores/stroke, not a new architecture |
| 18″ wheels + brakes vs 13″ | **+~12** | bigger rims and discs |
| 2026 safety cell + halo vs 2008 | **+~20** | higher crash standards — the one weight you can't wish away |
| 18 years of composite/material progress | **−~30** | lighter monocoque, bodywork, ancillaries than 2008 |
| **Naive build estimate** | **≈632 kg** | |

> **Regulated minimum: 605 kg** — about **~25 kg below** the naive build, i.e. a modest, achievable **lightweighting target** (pure engineering merit). The halo and the diesel are the unavoidable adds; no hybrid + modern composites pay for them. Add ~80 kg fuel (§9c) → ~685 kg grid weight.

### 9c. Powertrain (first pass) — see `technical.md` Art. 6

Two-stroke power: **P[kW] = BMEP[bar] × V[L] × N[rpm] / 600** (the /600, vs /1200 for a 4-stroke, is the 2-stroke firing-every-rev factor).

| Quantity | Derived value | Inputs |
|----------|---------------|--------|
| Displacement | **2.5 L** (5 × 500 cc) | grown from 1.5 L |
| BMEP | **26 bar** | aggressive boosted-diesel target |
| Rev ceiling | **7000 rpm** | dropped from 7500 — bigger 500 cc cylinders rev lower; fires like a ~14,000 rpm 4-stroke |
| **Peak power cap** | **≈758 kW (~1015 hp)** | **26 bar × 2.5 L × 7000 / 600** |
| Peak torque | **≈1035 N·m** | P / ω at 7000 rpm — enormous diesel torque |
| Power-to-weight | **≈1.25 kW/kg** | 758 kW / 605 kg (**≈1.68 hp/kg — turbo-era-F1 territory; modern F1 ≈1.3**) |
| Race fuel allowance | **≈80 kg JP-8** | ≈288 kW avg × 5400 s ÷ ~0.45 eff ÷ 43 MJ/kg |
| Fuel tank | **≈100 L** | 80 kg ÷ 0.8 kg/L |
| Exhaust tuning | **electronically-controlled VLEM** | auto-optimal at any rpm; set-and-locked (§9d) |

> Power knob: at fixed 26 bar / 2.5 L, **P ≈ 0.1083 × N** kW — so 6900 rpm = 1000 hp exactly, 7000 ≈ 1015 hp, 7200 ≈ 1045 hp. Dial via rev ceiling (or BMEP).
> At **605 kg** the 1000 hp target makes this **savage**: ~1.25 kW/kg (1.68 hp/kg) is *well above* F1 and into 1980s turbo-era territory. With ~8% less downforce, no traction control, and ~1035 N·m of diesel torque, it is ferocious on power — but the 3300 mm wheelbase keeps it **planted rather than nervous**, and the driver-vectored diff (Art. 7.3) is the tool to manage the torque. Maximally skill-dependent on power delivery.
> Fuel: **≈80 kg / ~100 L** — only ~10 kg over F1's 70 kg despite ~40% more power, thanks to diesel efficiency (~45%). A reasonable load, not the packaging problem the earlier 95 kg estimate implied.

### 9d. Exhaust tuning — electronically-controlled variable-length manifold (VLEM)

A 2-stroke's power band is set by **exhaust pressure-wave tuning**: the reflected wave from the tuned-length exhaust returns a slug of fresh charge into the cylinder just before the exhaust closes. That tuning is sharply rpm-specific, so fixed-length 2-strokes are peaky. The **VLEM is electronically controlled to set the optimal length at *every* rpm in real time**, making the ~1000 hp usable across the whole range rather than at one peak.

Crucially, this is **automated *engine-output* optimization, not a driving aid** (`technical.md` Art. 8.4): it optimizes the powerplant — the driver still must deploy the resulting torque with no traction control. Its control map is **set and locked before the race** (set-and-run; no in-race changes, no driver input) and is on-chain (M10), so it is a pure engineering-merit zone, not a live tuning cheat or a skill substitute.

---

## 10. Open calibrations (remaining)

- Lateral rescale vs trim (§2).
- 2021-suspension geometry adapted to 18″ wheels (§5).
- Powertrain-vs-tunnel packaging envelope (§7).
- Confirm BMEP/efficiency assumptions in 9c against real 2-stroke-diesel data.
- Exact transcription of the 2008 dimensional set and 2026 reference volumes into Appendix T-A.
