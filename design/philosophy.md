# Formula Zynerji — Design Philosophy

## What this is

**Formula Zynerji** is a redesign of the Formula 1 rulebook as an exercise in **mechanism design**. It keeps F1's DNA — open-wheel single-seaters, a combined Constructors' and Drivers' World Championship, recognizably F1-derived cars — but re-derives the *rules* from a single objective and a single method.

- **Objective — meritocracy.** The championship should be the most accurate possible *measurement of merit*: the genuinely best team and the genuinely best driver should win. Every rule is judged by one test — *does it make the finishing order track true competitive quality more closely, or less?*
- **Method — game theory + revealed history.** Teams are rational strategic actors who do whatever the rules *reward*, not whatever the rules *intend*. We design for the **equilibrium** behaviour, and we use seventy years of how teams actually responded to F1 rule changes as the data for predicting it.

The name says the goal: the rulebook **synthesizes** the two things teams pour in — **cost and effort** — into competitive *merit*, instead of letting them dissipate into **waste** (the aerodynamic arms race), **gaming** (loophole-lawyering, sandbagging), or **noise** (luck).

> This supersedes the v0.1 "open formula" framing. Formula Zynerji is **not** an open/anything-goes formula. Cars are prescriptively defined and F1-derived. What is novel is the *incentive structure*, not the freedom.

## The championship is a measurement instrument

Reframe the whole sport. A season is an **estimator** of an unobservable quantity — true competitive merit (car + team + driver quality). Like any estimator it has **bias** and **variance**. Meritocracy is the program of minimizing the distance between the estimate (the standings) and the truth (real merit).

Write the error as three terms. The entire rulebook is organized to shrink each one:

```
Standings  =  True Merit  +  Luck  +  Budget-bias  +  Gaming-bias
```

### Distortion 1 — Luck (variance)
Safety-car timing, weather, reliability lottery, first-lap chaos, qualifying track evolution, strategic coin-flips. These move results without moving merit.

**The variance razor (the single most important idea here):** *not all variance is bad.* Variance that rewards **skill** — a brilliant wet drive, a gutsy strategy call, superior tyre management — is **signal**. Variance that rewards **luck** — a safety car that gifts a free pit stop, being collected in someone else's crash — is **noise**. **Embrace skill-variance; suppress luck-variance.** This is also how we resolve the meritocracy-vs-entertainment tension: races can be wild, *as long as they are wild for merit-relevant reasons.*

### Distortion 2 — Budget (money buying results)
If the richest team wins *because* it is richest, the standings measure bank balances, not merit. The cure is **input equalization**: make every team's *resources* as equal as practical, so what differentiates them is the **quality of how they use those resources** — engineering and operational merit.

Note the precise target. We equalize **budget**, never **engineering freedom**. A spec series equalizes both and therefore measures nothing about engineering. Formula Zynerji equalizes the money and lets engineering merit speak.

### Distortion 3 — Gaming (rule-lawyering, sandbagging, exploiting wording)
A win from a clever reading of ambiguous text, or from deliberately underperforming to manipulate a handicap, is not a merit win. The cure is **incentive-compatible mechanisms**: rules whose *equilibrium* is the intended behaviour, robust to Goodhart's law, where honesty and maximum effort are a dominant strategy.

## Why not optimize for spectacle, like real F1?

Real F1 optimizes primarily for **commercial spectacle**, and reaches for merit-distorting patches when the show sags: DRS (manufactured passes), high-degradation tyres (a managed lottery), sprint races and the fastest-lap point (extra variance plus new gaming surfaces), and it tolerates the safety-car lottery because chaos sells. Formula Zynerji makes the opposite bet:

> A formula that rigorously rewards merit produces racing that is **also** compelling — because the drama comes from genuine competition, not contrived randomness.

So we replace **patches with cures**. The canonical example: real F1 added DRS to patch the fact that cars can't follow closely through dirty air. Formula Zynerji instead **prices the dirty-air externality** so cars *can* follow and overtake on merit — and then DRS is unnecessary.

## The system in three lines

1. **Equalize inputs** — a hard, money-neutral budget cap; a common safety floor; controlled supply of standard parts.
2. **Differentiate on merit** — leave engineering and driving genuinely free to matter, and *measure them cleanly*.
3. **Prevent dynasties without inverting merit** — handicap *future inputs* (development resource), **never** *current outputs*. No Balance of Performance, no ballast on a fast car. The best team still wins this season; the field gets a fair chance to **earn** its way back next season.

## The five new mechanisms (full treatment in `mechanism-design.md`)

1. **Development-resource auctions** — every team gets an equal endowment of development "tokens" and allocates scarce wind-tunnel / CFD / dyno resource through a near-strategy-proof market. Rewards *prioritization merit*, reveals valuations, and kills the "whoever runs the tunnel most, wins" dynamic.
2. **Dirty-air externality pricing** — measure each car's wake in a standard test and tax downforce that degrades the following car. A Pigouvian fix for the sport's central negative externality; the cure DRS only patches.
3. **Money-neutral cap with adaptive convergence** — an *equal, hard* cap (no luxury-tax money leak), with the *dynamic* element placed on development handicapping rather than base budget.
4. **Merit-weighted handicapping (inputs only)** — success buys you *less future development*, never a slower car. Calibrated to renew the field across seasons without inverting merit within one.
5. **Merit estimators in the sporting rules** — a points curve, drop-results, and field-strength weighting tuned for signal-to-noise; neutralization procedures that preserve *earned* gaps; and an official, teammate-referenced **driver-merit rating** to disentangle car from driver.

## Non-goals

- **Not** an open formula (corrected from v0.1). Cars are prescriptively defined, F1-derived.
- **Not** Balance of Performance. We never equalize *outputs*.
- **Not** spectacle-first. Spectacle is a welcome by-product of merit, not the objective.
- **Not** a spec series. Engineering merit must remain real and decisive.

## What survives from v0.1

The historical-F1 and open-class research is now **behavioural evidence**: every past ban, loophole, and arms race is a revealed-preference data point on how teams respond to incentives (`design/f1-historical-eras.md`, `design/precedents-open-class.md`, `reference/`). And **safety remains a non-negotiable invariant** — the one part of the car we never trade against or optimize for merit. It is a *constraint*, not an objective.
