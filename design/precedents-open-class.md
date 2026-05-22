# Motorsport Precedents — Behavioural Evidence & Design Lessons

> **Reframe note (v0.2).** Retained from the superseded "Open Formula" concept and re-read as **behavioural evidence** for Formula Zynerji. The failure modes below (danger, runaway cost, dominance) map onto our distortions: *runaway cost* = Budget-bias, *dominance* = the dynasty problem (M3), *gaming/sandbagging* (BoP section) = Gaming-bias. The lessons about how teams behave under each rule regime are the revealed-preference inputs to our mechanism design (R8).

The history of open/unrestricted formulas, distilled into lessons about how teams behave under different incentive structures. The three failure modes any open formula must survive are **(A) danger, (B) runaway cost, (C) single-team dominance** — every precedent below failed on at least one. Compiled May 2026 with citations.

---

## Part I — Seven precedents (what was open, what killed it)

### 1. Group B Rally (1982–86)
**Open:** 200-unit homologation, no boost/displacement/aero/weight policing. **Constrained:** basic safety only; spectator access essentially none. **Produced:** AWD (Audi Quattro), anti-lag, twin-charging (Lancia S4), composite bodies; 250→600+ hp in four years. **Killed by DANGER:** spectator deaths (Portugal 1986) + Toivonen/Cresto fatal fire (Corsica 1986). FIA banned it within hours of the latter. **Root cause:** innovated powertrain but *not* safety infrastructure or crowd separation. → Lesson 1.

### 2. Can-Am (1966–74)
**Open:** Group 7 ≈ Formula Libre for sportscars — no limits on displacement, induction, aero, materials. **Produced:** the most adventurous tech in motorsport — high-downforce wings, the **Chaparral 2J fan car (1970)**, 1,000+ hp big-blocks, the 1,100–1,580 hp turbo **Porsche 917/30**. **Killed by DOMINANCE + COST:** the 917/30 was ~3 s/lap faster than anything; a desperate fuel-economy cap (1974) broke the formula's identity; sponsor (Johnson Wax) left. **Root cause:** no mechanism to stop a factory locking out the field economically. → Lessons 4, 5.

### 3. Formula Libre
**Open:** everything except basic safety/min weight. **Produced:** variety (pre-war GP cars vs post-war F2 at the same event), but **no focused innovation** — there's nothing to develop *toward*. **Lesson:** absolute freedom has no technological attractor; it produces anarchy/variety, not engineering progress. Innovation needs a *defined problem*. → Lesson 3 (the box must define a problem).

### 4. 1960s–70s F1 (our primary basis — see `f1-historical-eras.md`)
**Open:** aero config, wheel count, ground effect, cooling placement — almost unregulated. **Produced:** wings (1968), ground effect (Lotus 78/79), six wheels (Tyrrell P34, *won a GP*), the Brabham BT46B fan car (won its only race), turbos, a gas-turbine car. **Killed by COMPONENT BANS:** fan cars (1978, "unsportsmanlike"), skirts (1981), ground effect/flat-floor (1983, the performance *cliff*), six-wheelers (1983, tidy-up), turbos (1989). The fan car was withdrawn after *rivals protested* with no clear rule broken — a **competitive-threat ban dressed as safety**. → Lessons 3, 7, 8.

### 5. Formula SAE / Formula Student (1981–present) — the closest successful model
**Open:** suspension, aero, materials, transmission, drivetrain layout, cooling, body, fuel type. **Constrained:** 4-stroke ≤710 cc + a **20 mm intake restrictor** (caps power ~80–100 hp regardless of spend); mandatory safety structures (roll hoop, impact attenuator crash test, dual-circuit brakes, 5-pt harness, driver template); a **scored Cost Report**. **Multi-objective scoring** (Endurance 275, Design 150, Cost 100, Fuel Economy 100, Autocross 125, Skidpad/Accel 75 ea, Business 75) — *no single advantage wins the title.* **Why it works (45 yrs, growing):** absolute safety floor + one brilliant power equalizer + scored cost + multi-objective scoring + new classes added (hybrid 2007, electric 2010, driverless 2017) rather than retrofitting. → Lessons 1, 2, 4, 5, 7. **This is the most transferable blueprint.**

### 6. Unlimited Hydroplane / Bonneville
H1 Unlimited began truly unlimited, converged to a near-spec surplus-turbine class with a **fuel-flow cap** (4.3 gal/min) — "unlimited" is now historical. Bonneville is a **class matrix** (body × displacement × aspiration × fuel) and a *record* environment, not head-to-head racing, so dominance can't kill it. **Lesson:** truly unlimited classes either drift to de-facto spec, become non-competitive record-setting, or die. → Lesson 2 (a pinch-point is inevitable; design it deliberately).

### 7. Balance of Performance (GT3/GTE/WEC Hypercar)
**What it does:** post-homologation weight/power/aero/fuel-flow adjustments to equalize divergent cars. **Pros:** 11+ manufacturers in GT3; caps the arms race; close racing. **Cons:** **sandbagging** (deliberately underperform for favorable BoP — Porsche Le Mans 2016), **kills development incentive** (any gain gets BoP'd away), administratively fragile (WEC ran 3 BoP systems in 2025; LMH won 16 of 21 vs LMDh's 5 despite "equal" BoP), perceived unfairness. **Lesson:** BoP is a retrospective patch on divergent specs, not a design philosophy. **Open Formula rejects it.** → Lesson 4.

---

## Part II — Eight design lessons (referenced throughout the regs)

1. **Safety is a non-negotiable box, not a dial.** Group B died of safety, not competitiveness. Define a safety *envelope* (crash-test outcomes, fuel cell, egress, fire suppression, barriers, **and spectator separation at the ruleset level**) that can't be relaxed. Outcome-based, not material-based. → `regulations/safety.md`.

2. **One pinch-point > a thousand prescriptive rules.** FSAE's 20 mm restrictor / WEC's fuel-flow cap eliminate the power race in one sentence. Cap the most cost-correlated dimension (power-to-weight). Prefer a real-time-measurable power/energy cap over a fuel-consumption cap (which broke Can-Am). → `regulations/technical.md` Art. 5.

3. **Define the box by outcomes, not components.** Ground effect's danger was the performance *cliff*, not downforce — a ride-height-sensitivity rule would have kept the physics. The P34 died from tyre supply, not from "six wheels". Write performance envelopes; reserve component bans for inherently unscrutineerable hazards, labelled and time-limited. → `philosophy.md`; `technical.md` Art. 1.4, 3.2.

4. **Dominance needs a built-in correction — not BoP.** The 917/30 destroyed Can-Am with no rules violation. Use: max development/test allowance (sliding scale), multi-objective scoring, a cost cap, and (blunt, sunset-claused) success-ballast only if acute. **Not** post-hoc weight/power penalties. → `financial.md` Art. 3; `sporting.md` Art. 11.

5. **Prizes and economics must close the loop.** Can-Am died partly from sponsor/prize collapse; Group B's economics were already stressed. A well-run mid-field team must be able to break even. Front-load homologation cost; reward cost-efficiency (scored cost event). → `financial.md` Art. 6.

6. **Supplier independence is a first-order risk.** The P34 died because Goodyear wouldn't develop its bespoke tyre. Spec/approved tyres on equal terms; safety parts by *standard* not *supplier*; contractual equal-supply commitments. → `technical.md` Art. 8; `sporting.md` Art. 8.

7. **Class proliferation beats rule instability.** FSAE added hybrid/electric/driverless classes rather than retrofitting. Write the revision cycle into the founding doc; require a **supermajority to ban a legal technology** (stops competitive-threat bans); provide an **innovation-class pathway**. → `sporting.md` Art. 9, 10.

8. **The brilliant innovation usually dies from an adjacent constraint.** Fan car ("too complex to scrutineer"), P34 (tyre supply), ground effect (suspension brittleness), Can-Am (economics), Group B (crowd management). For every freedom, ask not "is it safe?" but "what *non-technical* constraint will kill it?" — supply chains, scrutineering complexity, venue compatibility, insurance. Define the scrutineering protocol for novel tech up front. → `technical.md` Art. 9; `sporting.md` Art. 9.

---

## Summary matrix

| Formula | Open | Constraint | Killed/limited by |
|---|---|---|---|
| Group B | powertrain, aero, materials | 200-unit homologation | **safety / crowd** |
| Can-Am | everything (Group 7) | two seats, closed wheels | **dominance + economics** |
| Formula Libre | everything | safety only | no design attractor |
| 1970s F1 | aero, configuration | displacement, weight | **competitive + safety bans** |
| Formula SAE | aero, chassis, drivetrain | 710 cc + 20 mm restrictor + safety + cost | *has not failed (45 yrs)* |
| H1 Unlimited | was all; now near-spec | turbine + fuel-flow cap | economic convergence |
| Bonneville | class matrix | displacement/aspiration class | n/a (record, not race) |
| GT BoP | homologated diversity | post-hoc BoP | sandbagging, instability |

**The transferable blueprint is Formula SAE:** a defined problem, an outcome-based envelope, a power ceiling via one equalizer, multi-objective scoring, scored cost, and an absolute non-negotiable safety floor — exactly the structure of the Open Formula Box.

## Sources
Wikipedia: Group B, Can-Am, Porsche 917, Formula Libre, Tyrrell P34, Brabham BT46, History of F1 regulations, Formula SAE, H1 Unlimited, Balance of Performance, Le Mans Hypercar, IndyCar. DirtFish (Rally Portugal 1986); Atelier Eau Rouge (Group B); Petrolicious & Goodwood (Can-Am/917/30); Motor Sport Magazine (Chaparral 2J); F1Chronicle & Formula1.com (ground effect, Lotus 79); Motorsport Strategy (P34 supplier lesson); Motorsport.com (banned BT46B); HotCars (Lotus 56); SAE International & IMechE (FSAE rules); APBA & H1Unlimited; Hagerty (Bonneville classes); Autosport & The-Race (BoP, WEC convergence).
