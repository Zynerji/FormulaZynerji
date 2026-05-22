# Formula Zynerji — Blockchain Architecture

The **spine** of Formula Zynerji. Everything — rules, designs, data, manpower — lives on an immutable, timestamped ledger, and **only what is on the chain may run on the car.** This document explains the economic argument, what is on the chain, the legality model, the innovation incentive, and the open calibrations. It defines mechanisms **M10** (forced on-chain disclosure) and **M11** (originator rewards), now the primary instruments of the formula.

---

## 1. Why a blockchain — the economic argument

In Formula 1, R&D produces a **private, excludable** advantage: your aerodynamics are secret, so a breakthrough pays off for years. The result is a **Tullock contest** — teams dissipate hundreds of millions chasing durable secret advantages, and results track spend (Budget-bias) and ossify into dynasties.

Forcing every run part onto a public chain **converts R&D from a private good into a club good.** The moment you race an innovation you must disclose it (CAD, FEA, CFD), and rivals may copy it. This single change rewires the incentives:

- **The value of any one innovation is capped at the head-start it buys.** No team will spend millions for an advantage that, within a weekend or two, arms every competitor. **Equilibrium R&D spend collapses** — directly attacking Budget-bias at its source.
- **The contest shifts** from *"who hides the biggest secret"* to *"who innovates fastest and integrates best."* That is a purer **merit** contest — exactly the objective (`philosophy.md`).
- **Dynasties dissolve.** A dominant team's edge is continuously copied away; it must keep out-innovating, not coast on a moat.
- **Scrutineering becomes near-trivial and near-uncheatable** (§3): legality is a hash check against an immutable, timestamped record.

The cost of this is the **patent dilemma** (§4): if copying is instant and free, why innovate at all? That tension — and its resolution — is the heart of the design.

> The chain doesn't *enforce* meritocracy with a rule; it *creates the market conditions* under which merit, not money or secrecy, decides. This is mechanism design, not policing.

---

## 2. What is on the chain — four ledgers

| Ledger | Contents | Purpose |
|--------|----------|---------|
| **Rules** | The regulations themselves, versioned; governance votes; technical directives | Immutable, auditable rulebook; rule changes are on-chain transactions (maps to `CHANGELOG.md`) |
| **Designs** | Every team-designed part: CAD geometry, FEA, CFD, material spec, the wake-test result (`technical.md` Art. 3) | The forced-disclosure engine (M10) and the provenance record (M11) |
| **Data** | Homologation results, scrutineering hashes, energy/power logs, lap/telemetry data as defined | Legality verification + the saleable media product (§6) |
| **Manpower** | Personnel registered to teams, roles, hours; transfers | On-chain cost/labour accounting (`financial.md` M9) and a transparent personnel market |

---

## 3. The legality model — "only on-chain parts may run" (M10)

3.1 **The rule.** A part may be fitted to a car in any session only if its complete design record is on the **Designs** ledger and was uploaded before that event's **Upload Deadline**.

3.2 **Upload Deadline.** All parts to be run at an event must be on-chain by a deadline at the **start of the event** (before scrutineering / first practice). This is the disclosure moment — from here, every rival can see the design.

3.3 **Self-policing scrutineering.** Scrutineering reduces to verifying that each fitted part **matches an on-chain record** (geometry hash + material). Because the ledger is immutable and timestamped, a team cannot run a secret part, back-date an upload, or alter a design after the fact. Cheating moves from "hard to detect" to "structurally impossible" (R5, R7).

3.4 **Consequence for the head-start.** Because rivals can only *see* a design at the Upload Deadline but must still *manufacture* it, the innovator gets at minimum the current event as exclusive on-track use (rivals' earliest copy runs at the next event). That manufacturing lag **is** the "natural lead" head-start (§4).

---

## 4. The innovation incentive — resolving the patent dilemma

If disclosure were the whole story, innovation would **under-provide**: a rational team would wait and copy rather than fund first-principles R&D (the free-rider / public-goods problem). Formula Zynerji resolves this with a **carrot, a stick, and a head-start** — the two incentive levers below plus the **mandatory minimum origination floor (M12, §4.4)**. The embargo and originator-data-cut options were considered and rejected.

### 4.1 Natural lead (selected)
No formal exclusivity. Upload at the event start; rivals copy as fast as they can manufacture and integrate. **The head-start is your build and integration speed** — itself a merit (operational excellence). Keeps copying free and fast, which maximises field compression.

### 4.2 Originator rewards — M11 (selected)
The chain records **who uploaded a given innovation first.** When other teams subsequently adopt a design that derives from yours, the **originator earns an on-chain reward**. This pays innovators directly for the public good they create, curing the under-provision problem **without** slowing copying.

- **Reward currency:** primarily **Development Tokens** (`financial.md` M2) — so innovating buys you *more future R&D capacity*, the most merit-aligned reward; plus a published **Innovation Index** (recognition, and an optional small championship credit — open decision).
- **Attribution:** on upload, a team **declares provenance** — original, or derived from on-chain element X. A geometric-similarity check plus a dispute process (every design is public, so disputes are resolvable) assigns each innovation to its first appearance.
- **Reward scales** with the number of distinct teams that adopt the innovation — the more widely your idea propagates, the more it's worth.

> Net effect: copying is free and instant (field stays compressed), **and** being first is directly and measurably rewarded (innovation stays funded). This is the design's central balance — and the **strength of the originator reward is the main calibration knob**, the analogue of patent term.

### 4.3 Why not the embargo (rejected)
A formal exclusivity window would protect innovators but slow field compression and re-introduce a durable advantage — closer to the F1 status quo we're moving away from. Rejected in favour of the freer natural-lead + originator-reward combination.

### 4.4 Minimum origination floor — the stick (M12)
The carrot (§4.2) *rewards* contribution but does not *compel* it; a voluntary public-goods game still under-provides at equilibrium. So contribution is made **mandatory**: every team must spend a minimum each season (`financial.md` Art. 2.6), of which a defined share must produce **original on-chain designs** (Art. 2.7). A team cannot run a copy-only operation living off the pool — it is *required* to feed it.

This is the decisive lever for the free-rider problem: **M10 forces sharing, M12 forces contribution, M11 rewards leadership.** With the cap as ceiling, the floor also narrows the spend band, equalizing inputs (a meritocracy bonus). The dollar floor alone is insufficient — it needs the origination teeth (Art. 2.7), or teams meet it by spending on copying/manufacturing while still free-riding on design.

---

## 5. Manpower ledger

5.1 Personnel are registered on-chain to a team, with role and hours. This makes the **labour component of the cost cap natively auditable** (`financial.md` M9) and closes the "hide spend in people" hole.

5.2 Transfers are on-chain transactions, enabling a **transparent personnel market** and (optionally) a headcount limit as an additional input-equalizer.

---

## 6. The data-revenue stream

6.1 Chain data (designs, telemetry, manpower history) is a **product**. Access tiers:
   - **Series / scrutineers:** full access.
   - **Teams:** full access to all design ledgers (this *is* the forced disclosure).
   - **Public / media / journalists:** **paid** access — the revenue stream.

6.2 **Revenue routing.** Data-sale revenue flows to a series pool and is **redistributed toward smaller teams** (a further input-equalizer). *Note: per the head-start decision, revenue is **not** routed to originators* — originators are rewarded via M11 tokens instead (§4.2), keeping the two incentives separate.

---

## 7. Architecture notes (implementation)

7.1 **Chain type:** a **permissioned consortium chain** governed by the series, with teams and officials as nodes — not a public proof-of-work chain. The property we need is **immutable, timestamped provenance with controlled access**, not open mining.

7.2 **Storage:** large design files (CAD/FEA/CFD) are content-addressed off-chain (e.g. IPFS-style) with their **hashes** committed on-chain; the hash is what scrutineering checks and what makes tampering detectable.

7.3 **Access control:** cryptographic tiering enforces §6 (teams see everything; public pays). The "forced sharing" is a property of team-tier access, not of public exposure — designs are shared *among competitors* immediately and *to the public* as a paid/curated product.

7.4 **IP & legal:** entering the series grants the licence required for mandatory disclosure and copying among competitors (this must be airtight in the entry agreement; the CC BY-SA spirit of the project extends to on-chain design data within the competition).

---

## 8. Failure modes & guards

| Risk | Guard |
|------|-------|
| **Free-riding** (copy-only team lives off the pool, never originates) | **Mandatory minimum origination floor (M12, §4.4) + originator rewards (M11)** — contribution is compelled and contribution is paid |
| Under-declared provenance (copier claims "original") | All designs public → similarity check + dispute panel; penalties for false declaration |
| Originator-reward gaming (trivial "innovations" farmed for tokens) | Reward only on genuine adoption by *other* teams; minimum-significance threshold |
| Off-chain "secret" testing to pre-develop before forced upload | Physical test resource is rationed and logged (`financial.md` M2); only on-chain parts may *run*, so secrecy buys nothing raceable |
| Collusion to suppress data-sale value or fix the personnel market | Transparent ledgers + series oversight (R9) |
| Chain/storage outage on a race weekend | Defined fallback: signed local snapshot + post-hoc reconciliation; legality frozen at last good state |

---

## 9. Open calibrations

- **Originator-reward strength** (the patent-term analogue): tokens per adopter, the Innovation Index weighting, and whether it carries any championship credit (advisory vs scored).
- **Similarity threshold** for attribution/derivation.
- **Upload Deadline** precise timing and what counts as a "new part" requiring upload.
- **Data-revenue redistribution** formula (how strongly weighted to small teams).
- **Manpower** headcount limit (if any) and transfer-market rules.

---

## 10. Map to the rest of the rulebook

| Concept | Lives in |
|---------|----------|
| Only-on-chain-parts legality, Upload Deadline | `regulations/technical.md` Art. 9 + here |
| Originator rewards in Development Tokens | `regulations/financial.md` Art. 3 |
| On-chain cost & manpower ledger, data revenue | `regulations/financial.md` Art. 4, 8 |
| Provenance / Innovation Index / scrutineering-by-hash | `regulations/sporting.md` Art. 6, 8 |
| Mechanisms M10, M11 in the catalog | `design/mechanism-design.md` |
