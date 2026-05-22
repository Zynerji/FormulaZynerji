# Formula Zynerji — Financial Regulations

**Version 0.3.1 (draft).** The machinery that removes **Budget-bias**, prevents **dynasties** without inverting merit, and **destroys the free-rider problem** from the stick side. Implements **M1** (money-neutral cap), **M12** (minimum origination floor — the budget becomes a *band*), **M2** (development-resource auction), **M3** (merit-weighted handicapping — now a *backstop*, see 3.3), **M11** (originator rewards, paid here in tokens), and the financial side of **M10** (the on-chain cost/manpower ledger, which makes monitoring native and subsumes most of **M9**).

> **Principle (R3):** equalize *inputs*, never *outputs*. We cap money and ration development; we **never** add weight or cut power to slow a fast car. With money equalized, the championship measures the *quality* of how resources are used — i.e. merit.

> **The blockchain changes the weighting.** Because forced disclosure (M10) already collapses the return on R&D spend and compresses the field, the cap and the handicap do *less* work than in F1, and cost monitoring becomes a property of the chain rather than an audit chase. The cap still matters (it bounds the *rate* of in-period spend), but the dynasty problem is mostly solved upstream by M10 — so the M3 handicap is dialled back to a backstop.

---

## Article 1 — Purpose & Scope

1.1 These regulations make every team's *resources* as equal as practical, so that finishing order reflects engineering and operational **merit**, not spending power.

1.2 **Reporting Group:** the entrant plus all controlled subsidiaries and related parties — the scope of every limit here (closes the related-party hole; M9, R9).

1.3 **On-chain ledger (M10).** All costs and all personnel are recorded on the Manpower and cost ledgers of the chain (`design/blockchain-architecture.md` §2, §5). Compliance is therefore largely *continuous and native*, not a retrospective audit — this is what subsumes most of M9.

---

## Article 2 — The Budget Band: Cap + Floor (M1 + M12)

> Spend is bracketed **[floor, cap]**. The **cap** (M1) stops money buying results; the **floor** (M12) stops teams free-riding on the shared design pool. A tight band does both *and* equalizes inputs.

2.1 **A single, hard, equal cap** of **[$C per season] *(placeholder)*** applies to every entrant. Published as a multi-year trajectory at launch.

2.2 **No luxury-tax / soft-cap overspend lane.** Unlike some leagues, overspend is *not* a payable option. A soft cap re-admits money as a performance lever, which is fatal to a meritocracy. Overspend is a breach (Art. 5), not a transaction.
   > Rationale (M1): the whole point is to delete the budget term from `Standings = Merit + Luck + Budget + Gaming`. A taxed overspend lane puts it back.

2.3 **Relevant Costs** (counted) are defined broadly as "costs related to competitive performance"; **Exclusions** are a short, bright-line list (driver salaries; a small number of top-staff salaries; marketing; non-performance overhead). Keep the exclusion list short — every exclusion is a gaming surface (R7).

2.4 **Capital expenditure** sits in a separate rolling multi-year allowance so a team can build tooling without a single-year cliff, kept distinct from the operating cap.

2.5 **Indexation** by a published formula (inflation + per-extra-event supplement) so calendar length doesn't silently move the cap.

2.6 **Minimum Development Spend — the floor (M12).** Every entrant must spend **at least [F per season] *(placeholder, e.g. ≈80% of the cap)*** on performance development. This destroys the free-rider problem that forced disclosure (M10) would otherwise create: a team cannot run a copy-only, shoestring operation and live off the shared design pool — it is *required* to invest. (Forced disclosure makes innovation a public good; a voluntary public-goods game under-provides, so contribution is made mandatory.)

2.7 **Origination teeth (M12).** A pure dollar floor could be met by spending on copying and manufacturing while still free-riding on *design*. So a defined share of the floor must produce **original on-chain designs** — each entrant must upload **≥ [N] original, non-trivial designs per season** (declared original under `technical.md` Art. 9.2 and passing the novelty/similarity check). The floor must *feed the commons*, not merely be burned.

2.8 **Shortfall penalty.** Failing the floor or the origination minimum is a breach (Art. 5): the shortfall is paid into the data-revenue redistribution pool (Art. 8.2) and a Development-Token reduction applies; persistent free-riding escalates toward exclusion.

> Rationale (M12): with the cap as ceiling and this floor, the spend **band** is narrow → strong input-equalization *and* compulsory contribution. The higher the floor, the more completely free-riding is destroyed (the user's intent) — at the cost of less "spend-efficiency" merit. Lean high.

> TODO: set $C, the multi-year trajectory, the inclusion/exclusion lists, the CapEx allowance, **the floor F (as % of cap), and the origination minimum N**.

---

## Article 3 — Development-Resource Allocation (M2 + M3)

> The real currency of performance gains is **development throughput** — wind-tunnel runs, CFD items, dyno hours, track and simulator time. Even under an equal money cap, whoever converts the most throughput tends to win. We ration throughput as a market, and handicap it by success.

### 3.1 Equal token endowment (M2)
Each entrant receives an **equal endowment of Development Tokens** per Development Period, before any handicap (Art. 3.3). Tokens are the only way to acquire development resource. Equal endowment keeps allocation money-neutral.

### 3.2 The development auction (M2)
3.2.1 The total available development resource each period (tunnel runs, CFD items, dyno hours, track/sim days) is **genuinely capped** (fixed series capacity) and **allocated by a periodic market**: teams spend tokens to acquire units of each resource.
3.2.2 The auction uses a **near-strategy-proof format** so that truthful valuation is approximately optimal and *engineering judgement*, not bid-strategy, decides outcomes.
   > TODO: choose the format — **uniform-price sealed-bid** (price = first rejected bid; weakly truthful) vs a **fixed-price menu** with a hard token budget (simplest, no bidding meta). See `design/mechanism-design.md` M2.
3.2.3 **Anti-collusion:** bids are sealed; allocations and clearing prices are published after the fact; coordinated bid suppression is a breach (Art. 5).

   > Rationale (M2): rewards **prioritization merit** — knowing *what* to develop and *when* — a real engineering skill that current F1 (everyone maxes their fixed allowance) does not reward. Reveals each team's marginal-gain beliefs through prices.

### 3.3 Merit-weighted handicapping — inputs only, *backstop* (M3)
3.3.1 An entrant's **token endowment (and/or its base resource multiplier) may shrink with championship success**, on a published curve indexed to standing. A successful team receives **less future development resource** — it **never** receives a slower car.
3.3.2 The handicap acts only on *future inputs*; the current season's order is untouched. Sandbagging earns nothing because it acts on development resource, not a per-race break (R5).
3.3.3 **Backstop posture.** Because forced disclosure (M10) already compresses the field by copying every advantage away, the handicap is a *light backstop*, not the primary lever. **Default: minimal or zero**, increased only if dynasties persist despite M10.
3.3.4 **Calibration mandate:** any non-zero curve must be set against historical gap-decay data so it restores *opportunity*, not *outcome*. A curve strong enough to let a worse team out-develop a better one is a defect (merit inversion, R3).

   > TODO: decide whether M3 is needed at all given M10; if so, set the curve (slope, floor, ceiling, reset cadence).

### 3.4 Originator rewards (M11)
3.4.1 The chain records who first uploaded each innovation (`technical.md` Art. 9.2). When other teams adopt a derivative design, the **originator earns Development Tokens**, scaled to the number of distinct adopting teams — so innovating buys *more future R&D capacity* (the most merit-aligned reward).
3.4.2 A published **Innovation Index** records originator credit; whether it carries any championship credit is an open decision (default: recognition only).
3.4.3 **The reward strength is the master calibration of the formula** — the patent-term analogue (`blockchain-architecture.md` §4.2). Too low → innovation under-provides; too high → re-creates durable advantage.
   > TODO: tokens-per-adopter schedule; Innovation Index weighting; similarity/derivation threshold; championship credit yes/no.

### 3.5 New-entrant ramp
A new entrant receives maximum endowment and no handicap for a defined ramp period.

---

## Article 4 — Reporting, Audit & Monitoring (M9, now native via M10)

> Most of this is **continuous and on-chain** (Art. 1.3): costs and personnel post to the ledger as they occur, so the audit largely *reconciles* the chain rather than reconstructing private accounts. The clauses below are the residual off-chain controls.

4.1 **Filing.** Reconciliation of the on-chain ledger plus any off-chain items by a fixed deadline (target ≤ 90 days after season end), with a signed independent certificate.

4.2 **Interim signal.** Quarterly *unaudited* estimates create an early-warning signal and shrink the audit lag (the ~12-month lag in real F1 meant a full season of advantage before any penalty; R9).

4.3 **Related-party transactions (the main hole).** Any intra-group or inter-competitor transfer above a threshold must be priced to a declared **market-consistent standard** (independent valuation, or a defined cost-plus). Designed in from day one — not patched mid-cycle (R7/R9).

4.4 **Randomized deep audits.** At least one entrant per cycle receives an invasive audit selected at random, in addition to risk-based selection (R7 — you cannot game what you cannot predict).

---

## Article 5 — Breaches & Penalties

5.1 **Tiers:** Procedural (reporting failure) · Minor overspend (< 5%) · Material overspend (≥ 5%) · Auction manipulation/collusion.

5.2 **Penalty principle:** scale to *advantage gained*, not just the overspend figure. The **primary sporting penalty is a reduction of future Development Tokens / resource allowance** — it removes development precisely when rivals are gaining, which hurts a leader far more than a fine (the lesson of real F1's 2021 case). Fines are secondary.

5.3 Material breaches and repeat manipulation may escalate to championship-points deduction or exclusion, via an independent Adjudication Panel. Procedural/minor cases may settle by an Accepted Breach Agreement.

---

## Article 6 — Powertrain Cost

6.1 Consider a **separate development-token pool (and sub-cap) for propulsion**, so a team cannot starve aero to over-invest in the power unit (or vice versa), and so the two can be handicapped on different schedules as the formula matures.
   > TODO: single pool vs split chassis/powertrain pools.

---

## Article 7 — Optional: Scored Efficiency Credit

7.1 *(Optional, supports meritocracy.)* Award a small, championship-relevant credit for demonstrably cost-efficient engineering, so that spending *better* — not merely *up to the cap* — is itself rewarded. Pairs with the estimator design in `sporting.md`.
   > TODO: decide whether to adopt, and how to score it without creating a new gaming surface (R7).

---

## Article 8 — Data Revenue & Manpower Ledger (M10)

8.1 **Data revenue.** Chain data (designs, telemetry, manpower history) is sold to journalists, media, and the public through a paid access tier (`design/blockchain-architecture.md` §6). Teams have full access to all design ledgers regardless (that is the forced disclosure); the paid tier is the public/commercial product.

8.2 **Revenue redistribution.** Data-sale revenue flows to a series pool and is **redistributed toward smaller teams**, an additional input-equalizer. Per the head-start decision, revenue is **not** routed to originators (they are rewarded via M11 tokens, Art. 3.4) — keeping the two incentives separate.
   > TODO: the redistribution formula (how strongly weighted to small teams).

8.3 **Manpower ledger.** Personnel are registered on-chain to a team with role and hours, making the labour component of the cap natively auditable (Art. 1.3) and closing the "hide spend in people" hole. Transfers are on-chain transactions, enabling a transparent personnel market and (optionally) a headcount limit as a further input-equalizer.
   > TODO: headcount limit (if any); personnel-transfer rules.
