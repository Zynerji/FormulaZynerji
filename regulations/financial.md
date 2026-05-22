# Formula Zynerji — Financial Regulations

**Version 0.5.0 (draft).** The economic system that removes **Budget-bias** and lets the field **self-balance**. Implements **M1** (money-neutral cap), **M12** (minimum-spend floor + origination — now the keystone), and the financial side of **M10** (the on-chain cost/manpower ledger). **There is no token, auction, or success-handicap system** — the forced-disclosure economy self-balances without artificial currency (Art. 3). Numbers are first-pass and tunable.

> **Principle (R3):** equalize *inputs*, never *outputs*. We cap money; we **never** add weight or cut power to slow a fast car. With money equalized, the championship measures the *quality* of how resources are used — i.e. merit.

> **No tokens (v0.5.0).** Earlier drafts rationed development with Development Tokens, a development auction (M2), and a success handicap (M3). All removed. With forced disclosure, those were machinery to *force* a balance the disclosure economy produces on its own (Art. 3). Development is limited by **money alone** (the cap); the field is balanced by **copying** (everyone converges on the best on-chain parts) and kept innovating by the **floor**.

---

## Article 1 — Purpose & Scope

1.1 These regulations make every team's *spending power* as equal as practical, so finishing order reflects engineering and operational **merit**, not budget.

1.2 **Reporting Group:** the entrant plus all controlled subsidiaries and related parties — the scope of every limit here (closes the related-party hole; R9).

1.3 **On-chain ledger (M10).** All costs and personnel are recorded on the chain's cost and Manpower ledgers (`design/blockchain-architecture.md` §2, §5). Compliance is therefore largely *continuous and native* — a reconciliation, not a retrospective audit chase.

---

## Article 2 — The Budget Band: Cap + Floor (M1 + M12)

> Spend is bracketed **[floor, cap]**. The **cap** stops money buying results; the **floor** stops teams free-riding on the shared design pool *and* forces the continuous innovation that keeps the self-balancing economy (Art. 3) alive. A tight band also equalizes inputs.

2.1 **Cap — single, hard, equal: ≈ $75 M per season** (first-pass) for every entrant, published as a multi-year trajectory at launch.
   > Set well below F1 (~$135 M+) deliberately: forced disclosure removes most *duplicated* R&D (you copy a solved problem rather than re-solving it in secret), so a serious car can be fielded for less — which also widens the grid (accessibility). Tunable.

2.2 **No luxury-tax / soft-cap lane.** Overspend is a **breach** (Art. 5), not a payable option — a soft cap re-admits money as a performance lever, fatal to a meritocracy.

2.3 **Relevant Costs** = "costs related to competitive performance" (broad). **Exclusions** = a short, bright-line list: driver salaries; a small number of top-staff salaries; marketing; non-performance overhead. Keep it short — every exclusion is a gaming surface (R7).

2.4 **Capital expenditure:** a separate rolling allowance **≈ $30 M / 3 years** (first-pass) for facilities/tooling, kept distinct from the operating cap so a team can invest without a single-year cliff.

2.5 **Indexation:** cap adjusts by a published formula (CPI + a per-extra-event supplement) so calendar length doesn't silently move it.

2.6 **Minimum Development Spend — the floor (M12): ≥ 70 % of the cap (≈ $52 M)** must be spent on performance development each season. This destroys free-riding *and* is the keystone of the self-balancing economy: a team **cannot** run a copy-only operation living off the shared pool — it must keep developing. (Forced disclosure makes innovation a public good; a voluntary public-goods game under-provides, so contribution is **mandatory**.)

2.7 **Origination teeth (M12).** A pure dollar floor could be met by spending on *copying and manufacturing* while still free-riding on *design*. So **≥ half of the development spend (and ≥ [N] significant components per season) must be original on-chain work** — declared original under `technical.md` Art. 9.2 and passing the novelty/similarity check. The floor must *feed the commons*, not merely be burned.

2.8 **Shortfall penalty.** Failing the floor or origination minimum is a breach (Art. 5): the shortfall is paid into the data-revenue redistribution pool (Art. 8.2), plus a **future-cap reduction**; persistent free-riding escalates toward exclusion.

> TODO: ratify $75 M cap, the 70 % floor, the CapEx allowance, the origination minimum N, and the multi-year trajectory.

---

## Article 3 — The Self-Balancing Economy (no tokens, no auction, no handicap)

> The core economic claim: the forced-disclosure economy **balances the field by itself**, so no artificial currency or handicap is needed.

3.1 **The equilibrium.** Three forces interact:
   - **Disclosure compresses (M10).** Any advantage you build is uploaded on-chain and copied, so advantages are **transient** — the gap to the field shrinks on its own.
   - **The championship pulls everyone to the best parts.** You cannot win without the best parts, and the best parts are **freely on-chain**, so every team adopts them. Convergence is automatic — *"championship score for using the best parts possible"* drives universal adoption.
   - **Re-leading requires new innovation.** Because your edge is copied away, staying ahead means **innovating again** — constant pressure on whoever leads.

   The result is a **naturally compressed field** where the best team still wins, but narrowly, and differentiation is by *who innovates next* and *who executes/drives best*. Dynasties cannot run away because their advantage is continuously copied — **the dynasty problem is solved without a handicap (M3 deleted).**

3.2 **The one failure mode, and its fix.** A token-free copy economy has exactly one bad equilibrium: **pure-copy stagnation** — everyone copies, nobody innovates, the field freezes. The **minimum-spend floor + origination teeth (M12, Art. 2.6–2.7)** forecloses it by *forcing* every team to do original development. The floor is therefore the keystone that makes the self-balance stable; the innovation incentive is the **transient head-start** (you are fast first, and score points, before others copy) plus **recognition** (the Innovation Index, Art. 8.4) — **not** a paid bounty.

3.3 **Development resource is limited by money alone.** Wind-tunnel, CFD, dyno, simulator and track time are bought from the capped budget — there is **no separate allowance, ATR sliding scale, auction, or token pool.** Teams allocate their budget across development as they see fit; allocation skill is rewarded through *results* (and the output is copied anyway). This is simpler than F1's ATR and needs no currency.

3.4 **New-entrant ramp.** A new Constructor gets a defined grace on the floor and a share of redistributed data revenue (Art. 8.2) so it can establish itself; no handicap is applied to anyone (there is none).

---

## Article 4 — Reporting, Audit & Monitoring (native via M10)

> Mostly **continuous and on-chain** (Art. 1.3): costs and personnel post to the ledger as they occur, so the audit *reconciles* the chain rather than reconstructing private accounts.

4.1 **Filing.** Reconciliation of the on-chain ledger + any off-chain items by a fixed deadline (target ≤ 90 days after season end), with a signed independent certificate.

4.2 **Interim signal.** Quarterly unaudited estimates create an early-warning signal and shrink the audit lag.

4.3 **Related-party transactions (the main hole).** Any intra-group or inter-competitor transfer above a threshold must be priced to a declared **market-consistent standard** — designed in from day one (R7/R9).

4.4 **Randomized deep audits.** At least one entrant per cycle gets an invasive audit selected at random, plus risk-based selection (R7).

---

## Article 5 — Breaches & Penalties

5.1 **Tiers:** Procedural (reporting failure) · Minor overspend (< 5 %) · Material overspend (≥ 5 %) · Floor/origination shortfall (Art. 2.8).

5.2 **Penalty menu:** fine; **future-cap reduction** (the primary sporting lever — it constrains the offender's next-season development, where it bites); for material/repeat breaches, championship-points deduction or exclusion via an independent Adjudication Panel. Procedural/minor cases may settle by an Accepted Breach Agreement.
   > (No development-token penalty — there are no tokens. The cap reduction is the equivalent input-side sanction.)

---

## Article 6 — Powertrain Cost

6.1 Engine development (within the spec-base + open-zones architecture, `technical.md` Art. 6.6) is funded **inside the operating cap** — no separate token pool. Optionally, a **money sub-cap for propulsion** prevents a team starving aero to over-invest in the engine (or vice versa).
   > TODO: decide single cap vs a chassis/powertrain money sub-cap.

---

## Article 7 — Optional: Scored Efficiency Credit

7.1 *(Optional.)* A small championship credit for demonstrably cost-efficient engineering rewards spending *better*, not merely *up to the cap*. Largely redundant with the self-balancing economy (Art. 3), so likely unnecessary.
   > TODO: adopt or drop.

---

## Article 8 — Data Revenue, Recognition & Manpower Ledger (M10)

8.1 **Data revenue.** Chain data (designs, telemetry, manpower history) is sold to journalists/media/public via a paid access tier (`design/blockchain-architecture.md` §6). Teams have full access to all design ledgers regardless (that *is* the forced disclosure); the paid tier is the public/commercial product.

8.2 **Revenue redistribution.** Data-sale revenue flows to a series pool and is **redistributed toward smaller teams** — an additional input-equalizer and part of closing the economic loop (`sporting.md` Art. 11).
   > TODO: the redistribution formula (weighting to small teams).

8.3 **Manpower ledger.** Personnel are registered on-chain (team, role, hours), making labour cost natively auditable and closing the "hide spend in people" hole. Transfers are on-chain; an optional headcount limit is a further input-equalizer.
   > TODO: headcount limit (if any); transfer rules.

8.4 **Innovation Index (recognition, not currency).** The chain records who first uploaded each innovation (`technical.md` Art. 9.2); a published **Innovation Index** credits originators. This is **reputational recognition only** — the material reward for innovating is the transient on-track head-start (Art. 3.2), not a payment. (No tokens, no championship bounty, by design.)
