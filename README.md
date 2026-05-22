# Formula Zynerji

**A redesign of the Formula 1 rulebook as mechanism design — built on a blockchain that forces every team to share its designs, so that cost and effort are synthesized into *merit* and the genuinely best team and driver win.**

> Status: **v0.5.1 — draft** (car + competition complete; token-free self-balancing economy; cap & floor model-pinned) · License: [`LICENSE`](LICENSE) (CC BY-SA 4.0) · Maintainer: cknopp@gmail.com

---

## The one-paragraph pitch

Formula Zynerji re-derives the F1 rulebook from one objective — **meritocracy** — using **game theory** and seventy years of how teams actually behaved. Its spine is a **blockchain**: every part that runs on a car must have its full design (CAD, FEA, CFD) uploaded to an immutable ledger at the start of each race weekend, and **only on-chain parts are legal.** That single rule converts R&D from a private secret into a shared club good — no team will spend millions for an advantage that arms its rivals within a weekend — which collapses the spending war, dissolves dynasties, and turns scrutineering into a hash check. The innovator keeps a head-start (rivals still have to *build* the part) and is paid on-chain when others adopt their design. The car is a deliberate kitbash of historical F1 eras around a distinctive **2.5 L two-stroke diesel** (~1015 hp, ~605 kg).

## The spine: forced disclosure on a blockchain

| | |
|---|---|
| **What's on the chain** | Rules · Designs · Data · Manpower — immutable, timestamped |
| **The legality rule (M10)** | Only parts uploaded on-chain by the weekend's Upload Deadline may run |
| **Why teams accept sharing** | They have no choice — and the head-start (manufacturing lag) makes innovating still pay |
| **The innovator's incentive (M11)** | Natural lead (rivals must build your part) + reputational recognition (Innovation Index). **No tokens, no bounty** |
| **No free-riding (M12)** | A mandatory minimum spend + minimum original-design output — copy-only teams are impossible; the floor is the keystone that keeps innovation alive |
| **Self-balancing economy** | No tokens, no auction, no handicap — advantages are copied away (field compresses), the championship pulls everyone to the best parts, the floor forces innovation |
| **Self-policing** | Scrutineering = verifying each part matches its immutable on-chain hash; secret/back-dated parts are impossible |
| **Revenue** | Chain data sells to media/public; revenue redistributed toward smaller teams |

The economics: forced disclosure caps the value of any innovation at the head-start it buys, so equilibrium R&D spend collapses and the contest shifts from *"who hides the biggest secret"* to *"who innovates fastest and integrates best"* — a purer merit contest. Full treatment in [`design/blockchain-architecture.md`](design/blockchain-architecture.md).

## The core idea: the championship is a measurement instrument

A season is an **estimator** of unobservable true merit. Meritocracy = shrink the gap between standings and truth. Three things decouple them, and the whole rulebook neutralizes each:

```
Standings = True Merit + Luck + Budget-bias + Gaming-bias
```

| Distortion | Cure | Razor |
|------------|------|-------|
| **Luck** | suppress luck-variance, keep skill-variance | *Embrace variance that rewards skill; kill variance that rewards luck* |
| **Budget** | forced disclosure (M10) + money-neutral equal cap | *Equalize inputs, never outputs* (so, never Balance of Performance) |
| **Gaming** | incentive-compatible mechanisms; scrutineering-by-hash | *Design for the equilibrium, assume Goodhart* |

## The car — an era kitbash

| System | Era basis |
|--------|-----------|
| Front + rear wings, **floor**, tyres, wheels, safety | **2026** |
| Suspension (hydraulically interconnected) | **2021** |
| Gearbox (7-speed, longevity rule) | **2013** |
| Chassis sizing, dimensions, body rules | **2008** (1800 mm track) |
| **Engine** | **2.5 L inline-5 two-stroke diesel**, screw (Lysholm) supercharged, variable-length exhaust, on **JP-8**, ~1015 hp / ~1035 N·m, spec-base + open development zones |

Aero is disciplined not by ever-more-prescriptive geometry but by **dirty-air externality pricing** (M4): the dirtier your wake, the more it costs — so close racing and overtaking happen on merit, and there is **no DRS**. Details in [`regulations/technical.md`](regulations/technical.md).

## Repository layout

```
FormulaZynerji/
├── README.md · CLAUDE.md · CHANGELOG.md · LICENSE · glossary.md
├── regulations/               ← THE RULESET (the deliverable)
│   ├── technical.md           ←   the era-kitbash car + diesel + dirty-air pricing + on-chain legality
│   ├── sporting.md            ←   the competition as a merit estimator + scrutineering-by-hash
│   ├── safety.md              ←   the non-negotiable invariant (a constraint, not an objective)
│   └── financial.md           ←   money-neutral cap + minimum-spend floor + self-balancing economy (no tokens)
├── design/                    ← the "why"
│   ├── philosophy.md          ←   the meritocracy thesis
│   ├── mechanism-design.md    ←   the framework + mechanism catalog M1–M11 (the novel core)
│   ├── blockchain-architecture.md ← the spine: forced disclosure + originator rewards + the floor
│   ├── chassis-integration.md ←   fitting 2026 spec parts onto 2008 dimensions
│   ├── f1-historical-eras.md  ←   F1 rulesets era-by-era = behavioural evidence
│   └── precedents-open-class.md ← open-class history = more behavioural evidence
└── reference/                 ← cited digests of the real FIA regs (source material)
```

## How to read this

1. [`design/philosophy.md`](design/philosophy.md) — the thesis (meritocracy, the estimator, the three distortions).
2. [`design/blockchain-architecture.md`](design/blockchain-architecture.md) + [`design/mechanism-design.md`](design/mechanism-design.md) — **the novel core** (the spine + the full mechanism catalog M1–M11).
3. [`regulations/`](regulations/) — the rules (v0.3 drafts; numbers and calibrations flagged `> TODO:`).

## Design commitments (short version)

1. **Meritocracy is the objective.** Best team and best driver win; luck, money, and gaming engineered out.
2. **Forced on-chain disclosure is the spine.** Sharing is mandatory; only on-chain parts are legal; innovators get a head-start + originator rewards.
3. **Equalize inputs, differentiate on merit, never equalize outputs** — so, never Balance of Performance.
4. **Design for the equilibrium; assume Goodhart.**
5. **Price externalities; don't prescribe around them** (dirty air; no DRS).
6. **Safety is an invariant, not an objective.**

## Versioning

**MAJOR** = a change to the objective or the core mechanism set; **MINOR** = a new article/mechanism; **PATCH** = clarification. All changes logged in [`CHANGELOG.md`](CHANGELOG.md).
