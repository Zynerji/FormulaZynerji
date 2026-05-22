# Formula 1 Rulesets, Era by Era — Behavioural Evidence

> **Reframe note (v0.2).** This file was written for the superseded "Open Formula" concept; its "Open Formula take" annotations reflect that older framing. It is retained as **behavioural evidence** for Formula Zynerji: each era shows *how teams responded to a given incentive structure*, which is exactly the revealed-preference data our mechanism design (R8) depends on. Read the bans/loopholes/arms-races below as data on team behaviour, not as a freedom-vs-bans argument.

This document traces the major Formula 1 regulatory eras, what each made *free* vs *constrained*, the innovations that resulted, and *how* the FIA shut each one down — i.e. how the incentive structure shaped behaviour and how the regulator reacted.

The key pattern: **F1 was at its most open from 1966–1982, and almost every iconic innovation comes from that window; the FIA's response was always to ban the component.** For Formula Zynerji the lesson is *not* "keep the freedom" — it is that **prescriptive component bans get lawyered, while pricing/incentive mechanisms (our approach) shape behaviour more robustly** (R6/R7).

---

## The eras at a glance

| Era | Engine formula | Defining freedom | Iconic innovation | How it ended |
|-----|----------------|------------------|-------------------|--------------|
| 1947–1953 | 4.5L NA / 1.5L s/c | Pre-war diversity | Mercedes/Alfa GP cars | Formula 2 stopgap (1952–53) |
| 1954–1960 | 2.5L | Front- vs rear-engine open | Cooper rear-engine revolution | Engine formula change |
| 1961–1965 | 1.5L | "The return to grip" | Monocoque chassis (Lotus 25, 1962) | Engine formula change |
| **1966–1982** | **3.0L NA / 1.5L turbo** | **Aero, wheel count, ground effect, cooling — almost unregulated** | **Wings, ground effect, 6 wheels, fan car, turbos** | **Progressive component bans (see below)** |
| 1983–1988 | 1.5L turbo + 3.0L NA | Boost largely free | 1,000–1,400 hp turbos | Turbo ban (1989), boost/fuel limits |
| 1989–1994 | 3.5L NA | Electronics open | Active suspension, ABS, traction control, semi-auto box | Electronic-aid ban (1994, post-Senna) |
| 1995–2005 | 3.0L V10 | Aero detail still rich | Mass dampers, exotic aero | Tighter aero rules, V10 freeze |
| 2006–2013 | 2.4L V8 | Engine frozen 2007 | Double diffuser, F-duct, blown diffuser | Loophole-closing TDs |
| 2014–2021 | 1.6L V6 turbo-hybrid | Energy recovery strategy | MGU-H, complex ERS | Token freeze; cost cap arrives 2021 |
| 2022–2025 | 1.6L V6 turbo-hybrid | Ground effect *returns*, tightly prescribed | Floor-tunnel ground effect (re-regulated) | — |
| 2026– | 1.6L V6 hybrid (≈50% electric) | Active aero returns; sustainable fuel | X/Z-mode active aero, 350 kW MGU-K | — |

---

## 1. 1947–1965 — the formative eras

Early F1 inherited pre-war Grand Prix diversity. The lasting lesson for us is the **1952–53 Formula 2 stopgap**: when the top formula became unsustainable, the championship was run to a *cheaper* lower formula rather than cancelled. Open Formula echoes this with a defined, affordable entry spec so a small team can compete before it can afford to develop.

The other landmark is the **Lotus 25 monocoque (1962)** — the first stressed-skin chassis in F1, an innovation that emerged because chassis construction was essentially unregulated. It is the template for what an open formula should *want* to happen: a fundamental rethink, not a loophole.

> **Open Formula take:** chassis *construction* should be free (any architecture that passes the crash tests), exactly as it was when the monocoque was invented. We regulate the crash-test outcome, not the build method. → `regulations/technical.md` Art. 4, `regulations/safety.md` Art. 2.

---

## 2. 1966–1982 — the golden open era (our primary basis)

The "return to power" 3.0L formula of 1966 coincided with an almost total absence of aerodynamic, ground-effect, wheel-count, and cooling regulation. The constraints were essentially: engine displacement, a minimum weight, and rudimentary safety. **Everything else was open.** This is the closest F1 has ever come to being an open formula, and it is the era Open Formula is most directly modelled on.

What that freedom produced:

| Innovation | Car | Year | What it proved |
|------------|-----|------|----------------|
| Aerodynamic wings | Lotus 49B, Brabham, Ferrari | 1968 | Downforce as a design axis |
| Ground effect | **Lotus 78 / 79** | 1977–78 | Venturi underbody → 30–40% more cornering grip |
| Six wheels | **Tyrrell P34** | 1976 | Reduced frontal area / brake cooling; *won a GP* |
| "Fan car" | **Brabham BT46B** | 1978 | Active underbody suction; won its only race |
| Gas turbine | Lotus 56B | 1971 | Alternative powertrain (failed on throttle lag) |
| Forced induction | Renault RS01 | 1977 | The turbo era begins |

And how the FIA closed each one — the pattern Open Formula is designed to break:

| Year | Banned | Stated reason | The *real* problem | Outcome-based fix we'd have used |
|------|--------|---------------|--------------------|----------------------------------|
| 1978 | Fan cars | "unsportsmanlike" | Hard to scrutineer; downforce depends on a secondary system | Define a scrutineerable active-aero authority limit |
| 1981 | Sliding skirts | safety | Stiff suspension + min ride height = brittle | Limit downforce *sensitivity* to ride height |
| 1983 | Ground effect (flat floor) | safety | The performance *cliff*, not the downforce | "Downforce may not drop > X% across legal ride-height band" |
| 1983 | Six-wheelers | standardisation | None — a competitive/tidy-up ban | Nothing; let the tyre market decide (it already had) |

> **Open Formula take:** this era *is* the target state. Wheel count is free; aero concept is free; ground effect is **permitted** but governed by an *outcome* rule (a ride-height-stability limit + a plank/reference wear rule) that removes the 1982 performance-cliff danger without banning the physics. Active aero is permitted within a scrutineerable actuation-authority limit, rather than banned as the fan car was. → `regulations/technical.md` Art. 3.

---

## 3. 1983–1988 — the turbo arms race (the cost lesson)

With boost largely unregulated, turbo engines reached a reported ~1,400 hp in qualifying trim by the mid-1980s. The cars were fast, spectacular, dangerous, and *ruinously expensive* — only manufacturer-backed teams could compete. The FIA's response: progressive boost limits, a fuel-quantity cap, and finally a full **turbo ban for 1989**.

This is the **cost failure mode** in pure form, and the FIA's tool (limit the fuel, then ban the tech) is instructive. WEC later refined the good half of this idea into a *fuel-flow limit* that caps power without dictating engine architecture.

> **Open Formula take:** we adopt the *good* half (a source-agnostic **energy/power cap** as the single pinch-point) and reject the bad half (banning the architecture). A turbo, a V12, a battery, or a hydrogen fuel cell are all legal — they just have to live under the same energy and power ceilings. → `regulations/technical.md` Art. 5, `regulations/financial.md`.

---

## 4. 1989–1994 — the electronics era (the driver-aid lesson)

3.5L naturally-aspirated engines, but the real action was electronic: **active suspension, ABS, traction control, and semi-automatic gearboxes** (Williams FW14B/FW15C being the high-water mark). After Senna's and Ratzenberger's deaths at Imola 1994, the FIA banned electronic driver aids to put the car back in the driver's hands and cut cornering speeds.

> **Open Formula take:** this is a genuine philosophy choice, not just safety. We default to **banning driver aids that replace driver skill** (traction control, ABS, active suspension) to keep the formula a *driving* contest — but we make this an explicit, debatable rule rather than an accident of history, and we route any future reintroduction through the innovation-class pathway. → `regulations/technical.md` Art. 6, `regulations/sporting.md` (innovation class).

---

## 5. 1995–2013 — the loophole era (the prescription lesson)

As the rulebook thickened, competition shifted from *reinventing the car* to *finding the gap in the wording*: the Renault mass damper (2005), the Brawn/Toyota/Williams **double diffuser** (2009), the McLaren **F-duct** (2010), the **blown diffuser** (2010–11). Each was a clever reading of prescriptive geometry, and each was closed by a Technical Directive or rule tweak.

> **Open Formula take:** this era is the *anti-pattern*. The more you prescribe geometry, the more the sport becomes about lawyers and CFD interpreters rather than engineers. Our outcome-based box is the deliberate opposite — there is far less *wording* to exploit because we specify what the car may *do*, not what shape it may be. → `philosophy.md`, "Why outcome-based".

---

## 6. 2014–2026 — the hybrid + cost-cap + safety era (the machinery we borrow)

The modern era contributes the parts of F1 that Open Formula actually keeps:

- **Energy thinking (2014).** ERS, energy-deployment-per-lap limits, and (in 2026) a shift from a mass-based fuel-flow limit to an *energy*-based one (MJ/h). This is conceptually exactly our energy pinch-point — we simply make it source-agnostic.
- **The budget cap (2021→).** ~$135–145M operating cap (restructured to ~$215M for 2026), with defined inclusions/exclusions, an audit, an adjudication panel, and real penalties (Red Bull 2021). Our `financial.md` is modelled directly on this.
- **The ATR sliding scale (2021→).** Wind-tunnel/CFD allowance scaled 70%–115% by championship position, reset twice a year. This is our primary anti-dominance lever.
- **The safety floor (halo 2018, escalating crash loads, FIA equipment standards).** Adopted wholesale and made non-negotiable in `safety.md`.
- **2026's active aero (X/Z-mode).** Proof that movable aero can be governed safely via a standard ECU and a defined actuation authority — the template for permitting (not banning) the kind of device the 1978 fan car represented.

> **Open Formula take:** the *machinery* of modern F1 — energy caps, cost cap, ATR, crash tests, halo, standard safety-critical ECU — is exactly the armour that lets us safely re-open the technical freedom of the 1970s. We are, in one line: **1970s F1 freedom inside 2020s F1 safety and cost armour.**

---

## What we take from each era (summary)

| From this era | We take | Into |
|---------------|---------|------|
| 1962 monocoque | Free chassis construction, regulated by crash-test outcome | technical Art. 4 / safety Art. 2 |
| 1966–1982 open era | Free aero concept, free wheel count, permitted ground effect & active aero via outcome limits | technical Art. 3 |
| 1983–88 turbos | A single source-agnostic energy + power pinch-point (the good half of the fuel cap) | technical Art. 5 |
| 1994 aid ban | An explicit, debatable ban on skill-replacing driver aids | technical Art. 6 |
| 1995–2013 loopholes | The lesson *not* to prescribe geometry | philosophy |
| 2014–2026 modern | Energy caps, cost cap, ATR, crash tests, halo, safety ECU | financial + safety + technical |
