# Formula Zynerji — Blockchain Technical Specification

The implementable companion to [`blockchain-architecture.md`](blockchain-architecture.md). That document
makes the *economic* argument for the spine (forced disclosure → club good → merit); this one
specifies the *mechanics* precisely enough to build against: the record schemas, how a design becomes
a deterministic hash, how a physical part is shown to be legal, the race-weekend protocol, and the
external-access tiers that fund the sport. It defines no new mechanism — it concretizes **M10**
(forced on-chain disclosure), **M11** (innovation incentive), and the data-revenue product, and feeds
the numbers in [`regulations/financial.md`](../regulations/financial.md).

> Status: v0.1 spec draft. Concrete values (block cadence, tolerance bands, tier prices) are
> first-pass and flagged `> TODO:`; the schema and the hashing/conformance model are the load-bearing parts.

---

## 1. Chain model

A **permissioned consortium chain** governed by the series. Validating nodes are the series authority
and the registered teams; there is no public mining and no token (consistent with the token-free
economy, v0.5.0). The only properties required are **immutable, timestamped provenance** and
**cryptographically-tiered access** — not open consensus.

- **Consensus:** Byzantine-fault-tolerant voting among the series node + team nodes (e.g. a PBFT/Raft-class
  ordering service). A block is final when a supermajority of nodes co-sign it. The series node cannot
  rewrite history alone; a team node cannot suppress a rival's upload.
- **Block cadence:** event-driven plus a heartbeat. Uploads are ordered continuously; the
  **Upload Deadline** (Art. 3) is a wall-clock checkpoint, enforced by block timestamp, not by block height.
- **On-chain vs off-chain:** large binaries (CAD/FEA/CFD meshes, telemetry) are stored
  **content-addressed off-chain**; only their hashes, metadata, and access-control records live on-chain.
  *The hash on-chain is the source of truth; the off-chain blob is merely its body.*

> TODO: ordering-service implementation; node-admission and key-rotation policy; storage redundancy (≥3 geo-distributed replicas of every referenced blob).

---

## 2. Record schemas

Four record (transaction) types correspond to the four ledgers in `blockchain-architecture.md` §2.

### 2.1 `PartRecord` — the Designs ledger (the core object)

Every part that may run on a car is one `PartRecord`. Scrutineering and the Innovation Index both read it.

| Field | Type | Meaning / rule |
|---|---|---|
| `part_id` | uuid | Stable identity of this design revision |
| `team_id` | id | Uploading team |
| `class` | enum | Part class (e.g. `front_wing`, `floor`, `gearbox_internals`, `engine_ancillary`) — fixes which homologation/zone rules apply |
| `timestamp` | int (ns) | Block-assigned upload time; the disclosure moment and the provenance clock |
| `nominal_geometry` | hash + ref | SHA-256 of the **canonicalized** nominal solid (§3) + off-chain CAD blob ref |
| `tolerance_spec` | struct | Per-feature manufacturing tolerance band used for conformance (§4) |
| `material_spec` | struct + hash | Material(s), process, certified properties; hash of the full data sheet |
| `analyses` | list⟨hash+ref⟩ | FEA, CFD and (for aero parts) the **wake-test result** (`technical.md` Art. 3 / M4) — each a hashed dataset |
| `cost_entry` | ref | Link to the `Manpower/Cost` postings that produced this part (cap accounting, M1/M9) |
| `provenance` | enum + refs | `original`, or `derived_from:[part_id…]` — the declaration the Innovation Index audits (M11) |
| `homologation` | enum | `pending` / `passed` / `failed` from the on-chain checks for its `class` |
| `signature` | sig | Team key signature over the whole record |

### 2.2 Supporting records

| Record | Ledger | Key fields |
|---|---|---|
| `CostPosting` | Manpower/Cost | `team_id`, `category`, `amount`, `supplier`, `related_party?`, `manpower_hours`, `period` → feeds the cap (M1), floor (M12), related-party check (M9) |
| `DataCommit` | Data | `event_id`, `session`, `car_id`, `type` (telemetry/energy/scrutineering), `hash+ref`, `access_tier` |
| `RuleTxn` | Rules | `version`, `diff_hash`, `governance_vote`, `effective_event` — the regulations and Technical Directives as on-chain transactions (maps to `CHANGELOG.md`) |

---

## 3. Canonicalization & hashing (why a design hash is deterministic)

A naïve `sha256(cad_file)` is **not** stable — the same solid re-exported by a different CAD kernel,
or with reordered B-rep entities, yields different bytes. So a `PartRecord`'s `nominal_geometry` hash is
taken over a **canonical form**, not the raw file:

1. **Tessellate** the nominal solid to a fixed chordal tolerance (e.g. 50 µm), yielding a watertight mesh.
2. **Canonicalize** it: translate to the part datum frame, snap vertices to a fixed spatial grid, and
   sort vertices/faces by a deterministic key (lexicographic on quantized coordinates).
3. `nominal_geometry = sha256(canonical_mesh ‖ material_spec ‖ tolerance_spec)`.

Any kernel that reads the disclosed solid reproduces the same canonical mesh and therefore the same hash.
This is what makes a rival's *re-derivation* and a scrutineer's *check* land on identical bits.

> TODO: pin the tessellation tolerance and grid quantum per part `class` (small parts need a finer grid).

---

## 4. Scrutineering: design-hash ✚ physical-conformance (the precise model)

A common misconception is that scrutineering "hashes the part." It cannot: a manufactured part scanned
on a CMM differs from the nominal CAD by manufacturing tolerance and scan noise, so
`sha256(scan) ≠ nominal_geometry`. Legality is therefore a **two-clause** test:

> **A run part is legal iff (i) its design is on-chain and immutable, and (ii) the physical part conforms to that on-chain design within its declared tolerance.**

- **Clause (i) — provenance/immutability (pure hash):** the fitted part cites a `part_id`; the scrutineer
  recomputes the canonical hash of the referenced on-chain nominal solid and checks it equals the stored
  `nominal_geometry`, and that `timestamp < event.upload_deadline`. This proves the design was disclosed,
  not back-dated or altered. *This clause is cryptographic and uncheatable.*
- **Clause (ii) — conformance (metrology, not hashing):** the physical part is scanned (CMM/structured-light)
  and compared to the on-chain nominal mesh; every feature must lie inside `tolerance_spec`. This proves the
  thing on the car **is** the disclosed design, not a secret variant hidden behind a legal upload.

Cheating is reduced to "manufacture out of tolerance and hope metrology misses it" — a conventional,
detectable scrutineering problem — rather than "hide a secret part," which clause (i) makes impossible.

```
fitted part ─► read cited part_id ─► (i) recompute nominal hash == on-chain?  ──no──► ILLEGAL (no/altered record)
                                          │ yes & timestamp < deadline
                                          ▼
                              (ii) CMM scan within tolerance_spec?  ──no──► ILLEGAL (non-conforming)
                                          │ yes
                                          ▼
                                        LEGAL
```

---

## 5. Race-weekend protocol

| Phase | When | On-chain action | Legality state |
|---|---|---|---|
| **Development** | between events | `PartRecord`/`CostPosting` uploads allowed continuously | parts not yet runnable |
| **Upload Deadline** | event start, before scrutineering | ledger snapshot taken; later design uploads cannot run this event | **disclosure moment** — every rival can now read all event parts |
| **Scrutineering** | post-deadline | each fitted part runs the §4 two-clause check; `homologation` set | sets per-car legality |
| **Sessions** (practice/quali/race) | event | `DataCommit` of telemetry/energy logs per session | only parts that passed §4 may run |
| **Post-event** | after race | results, Innovation-Index adoption updates, provenance disputes resolved | provenance/credit finalized |

The manufacturing lag between the Upload Deadline (rivals can *see*) and the next event (rivals can *run* a
copy) **is** the head-start that rewards innovating (M11; `blockchain-architecture.md` §4.1).

> TODO: exact deadline offset; definition of a "new part" requiring a fresh `PartRecord` vs an in-tolerance batch.

---

## 6. External-access tiers (the data product)

Access is enforced by cryptographic tiering on the `Data` and `Designs` ledgers. Competitors see everything
for free (that *is* the forced-disclosure mechanism); everyone else pays, and that revenue funds the sport and
the prize money (`financial.md` Art. 8; `blockchain-architecture.md` §6).

| Tier | Audience | Scope | Pricing model |
|---|---|---|---|
| **Governance** | series, scrutineers | full read/write of legality data | n/a |
| **Competitor** | registered teams | full designs + data, real-time | free (mandatory disclosure) |
| **Public / fan** | anyone | highlights, basic telemetry, standings | free / nominal |
| **Media** | journalists, broadcasters | results, telemetry, Innovation Index, curated/narrative | subscription |
| **Deep-data (industry)** | non-competing aerospace/defence/automotive/energy (Boeing, Lockheed, OEMs) | full CAD/FEA/CFD, materials, durability, control datasets — **after** the competitive embargo window so it never aids a rival in-season | premium licence (the **largest** stream) |

- **Embargo:** deep-data is released to industry on a lag (e.g. end of season) so that selling data never
  hands a *competitor* an edge — competitors already have it free and live; outsiders get it delayed.
- **Routing:** external revenue → series pool → (a) operations/infra/safety, (b) prize money for the four
  championships, (c) small-team redistribution. Not routed to originators (their reward is head-start +
  recognition). Richer innovation → more valuable corpus → bigger prize fund (the collective-value loop).

> TODO: tier price points and the redistribution weighting (both interact with the cap/floor in `economic-modeling`).

---

## 7. Map to the rest of the rulebook

| This spec | Defined / used in |
|---|---|
| `PartRecord`, canonical hash, §4 two-clause scrutineering | `regulations/technical.md` Art. 9; `regulations/sporting.md` Art. 8 |
| Upload Deadline, weekend protocol | `regulations/technical.md` Art. 9; `blockchain-architecture.md` §3 |
| `CostPosting` (cap/floor/related-party) | `regulations/financial.md` Art. 2/4; M1/M9/M12 |
| Provenance / Innovation Index | `blockchain-architecture.md` §4; M11 |
| Access tiers & revenue routing | `regulations/financial.md` Art. 8; `blockchain-architecture.md` §6 |

The figure `drawings/blockchain_protocol.py` renders §4–§6 (weekend timeline, the `PartRecord` schema, and
the two-clause scrutineering check) for the whitepaper.
