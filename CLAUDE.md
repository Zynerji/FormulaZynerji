# CLAUDE.md — Formula Zynerji

Working context for AI-assisted editing. Read this before touching the rules.

## What this project is

**Formula Zynerji** — a redesign of the Formula 1 rulebook as **mechanism design**. The deliverable is the Markdown in `regulations/`. It keeps F1's DNA (open-wheel single-seaters, a world championship, F1-derived cars) but re-derives the *rules* from one objective and one method.

- **Objective:** meritocracy — the genuinely best team and driver should win. The championship is a *measurement instrument* for merit.
- **Method:** game theory + revealed history. Design for the **equilibrium** behaviour, using how teams actually responded to past F1 rules as data.
- **Scope:** an era-kitbash F1-derived car + a 2-stroke diesel + **new game-theoretic mechanisms** (not an open formula; not a spec series; not BoP).
- **The spine:** a **blockchain** holding Rules/Designs/Data/Manpower. **Only on-chain parts are legal** (M10); innovators get a natural head-start + originator rewards (M11). This is the load-bearing concept — read `design/blockchain-architecture.md` before editing the car or financial rules.
- **The car:** 2026 wings/floor/tyres/safety · 2021 hydraulic interconnected suspension · 2013 gearbox + **driver-vectored diff** · 2008 dimensions/body, **3300 mm** wheelbase, **605 kg** min, ~80 kg fuel. **Engine:** 2.5 L I5 two-stroke diesel, screw (Lysholm) supercharged, JP-8, **electronically-controlled VLEM** (set-and-run), no traction hybrid, spec-base + open zones, **~1015 hp / ~1035 N·m** (BMEP 26, 7000 rpm). Aero disciplined by dirty-air pricing (M4); no DRS. **Art 8.4 principle: automate the engine, never the driving** (manual driver inputs permitted; auto engine-optimization permitted+locked; auto car-control aids banned).

> History note: this was briefly framed as "Open Formula" (an open/anything-goes box). That was wrong and is fully superseded. If you find stray "open formula / open-class / outcome-not-component / the Box" language in older files, treat it as legacy and reframe it toward meritocracy + mechanism design.

## The central model (do not drift from this)

```
Standings = True Merit + Luck + Budget-bias + Gaming-bias
```
Every rule must measurably shrink one of the three distortions without inflating another. The cures:
- **Luck** → suppress luck-variance, keep skill-variance (the variance razor).
- **Budget** → hard, money-neutral equal cap. **Equalize inputs, never outputs** (⇒ never BoP).
- **Gaming** → incentive-compatible mechanisms; assume Goodhart.

The nine design razors and the mechanism catalog (M1–M9) live in `design/mechanism-design.md`. **Every regulation should trace back to a mechanism there.**

## House style for the rules

- Numbered articles, FIA-style: `Article N — Title`, then `N.1`, `N.1.1`.
- Each substantive rule should name the **mechanism (Mx)** and **distortion** it serves — ideally in a one-line rationale note.
- Capitalised **Defined Terms** live in `glossary.md`.
- Mark unresolved decisions and calibrations with `> TODO:` blockquotes (greppable).
- Headline numbers (cap value, token endowment, points curve, handicap curve) are **placeholders for coherence**, not sacred — flag as tunable.
- Don't invent false precision. Cite real FIA figures from `reference/` where relevant; say so where we're choosing.

## Where things live

- `regulations/` — the ruleset (the product).
- `design/philosophy.md` — the thesis; `design/mechanism-design.md` — the framework + catalog (the novel core).
- `design/f1-historical-eras.md`, `design/precedents-open-class.md` — **behavioural evidence** (how teams respond to incentives).
- `reference/` — cited digests of the real FIA regs. Source material; read-mostly.
- `glossary.md`, `CHANGELOG.md` — keep current with every substantive edit.

## Conventions

- Not a git repo yet. Offer `git init`; don't assume.
- On a rule change: add a `CHANGELOG.md` entry and bump version per `README.md`.
- Safety (`safety.md`) is an **invariant constraint**, not something to optimize — never trade it for merit/cost.

## Open calibrations / decisions (see `design/mechanism-design.md` §5 and `> TODO:` markers)

- Cap value; token endowment; auction format (lean near-strategy-proof).
- Handicap curve strength (calibrate vs historical gap-decay; avoid merit inversion).
- Dirty-air wake metric + rig + price currency (must stay input-side, not BoP).
- Points vector + drop-results N-of-K + whether to field-strength-weight.
- Driver-merit rating: **advisory vs binding** (recommend advisory first).
- The deliberate luck-variance *floor* left in for entertainment.
