# Formula Zynerji — Safety Regulations

**Version 0.2.0 (draft).** The **invariant**. Safety is the one part of Formula Zynerji that is *not* an objective and is *never* optimized against: it is a hard constraint on everything else (`design/mechanism-design.md` §1). Every limit here is an **outcome** the car and the event must meet; *how* it is met efficiently is engineering merit. **No clause in this document may be traded against merit, performance, cost, or tradition, and there is no waiver process.** Failure of any safety check is an immediate no-start or exclusion.

> **Basis & principle.** F1's safety architecture evolved by hard lessons: the post-Imola-1994 overhaul, wheel tethers after Henry Surtees (2009), the Virtual Safety Car after Bianchi (2014), and the halo (2018), which was mandated over aesthetic and commercial objection and saved at least four drivers within four years. The principle Formula Zynerji encodes: **the merit contest and rigid safety standards are orthogonal** — you can run a tightly tuned game-theoretic competition *while* mandating exact crash-test pass criteria that are never on the table. The formula that ignored safety as a hard constraint — Group B — was killed by safety failure at the height of its popularity. See `design/precedents-open-class.md`, Lesson 1.

---

## Article 1 — Principles

1.1 Safety limits are **outcome-based** ("the driver must survive an impact of defined energy with defined peak loads") so that teams may innovate in *how* they achieve them — not input-based ("you must use material X").

1.2 **No waivers.** Any failure of a test or check in this document means the car does not run. This is absolute and applies regardless of championship standing, commercial pressure, or schedule.

1.3 **Evidence ratchet.** Once an incident demonstrates a failure mode and a validated countermeasure exists, that countermeasure becomes mandatory at the next cycle and may not be relaxed thereafter. (The FIA pattern, made explicit.)

1.4 Safety figures below are **starting values ported from current FIA practice** and cited in `reference/f1-safety-regs.md`. They are floors, not ceilings.

---

## Article 2 — Survival Cell & Crash Structures

2.1 **Survival Cell.** A continuous closed structure enclosing the driver from below the knees to above the shoulders, intact after all tests in this Article. Geometry must accept the cockpit protection device (2.2) and provide a defined minimum occupant volume and head clearance.

2.2 **Cockpit protection device (halo-equivalent).** Mandatory for every car. Must withstand a static load of **≥ 125 kN** applied vertically for ≥ 5 s with no failure of the device or its mountings, and must not obstruct extraction. May not be removed, lightened below spec, or omitted for aerodynamic reasons. *(Ported from FIA 8869 / the F1 halo.)*

2.3 **Frontal impact structure.** Dynamic test at **≥ 15 m/s**; peak deceleration within defined limits; second impact on the already-deformed structure must also be survivable.

2.4 **Side intrusion.** Lateral structures and anti-intrusion panels (penetration-resistant layer between side structure and driver) tested to defined transverse loads.

2.5 **Rear impact structure.** Energy-absorbing structure behind the rear axle line tested to defined load before the cell is loaded.

2.6 **Roll structures (primary + secondary).** Combined-load test (vertical / lateral / longitudinal, e.g. **≈ 105 / 60 / 70 kN** simultaneously) with deflection ≤ 25 mm and any failure confined to the top region. *(Ported from F1; the 2026 cycle raised these — adopt the higher values.)*

2.7 **Wheel tethers.** Minimum **two tethers per wheel** of high-strength, cut-resistant material (Zylon-equivalent), proof-tested before each season. Detached wheels are the highest projectile hazard to other cars and marshals.

2.8 **Collapsible steering column** that cannot penetrate the helmet space in a frontal impact.

> All tests in this Article must be passed pre-season at a series-approved facility, witnessed by the Technical Delegate, before the car's first event (`technical.md` Art. 9.1).

---

## Article 3 — Energy-Storage Safety (powertrain-agnostic)

> Because the powertrain is open (`technical.md` Art. 5), energy *storage* safety must be written generically, not for one chemistry.

3.1 **Fuel cell.** Any liquid/gaseous fuel must be carried in a homologated bladder-type fuel cell (FT5-equivalent: defined puncture/tear resistance; defined service life). No production-car tanks.

3.2 **High-voltage electrical storage.** Any battery/capacitor system must meet a defined cell-containment, thermal-runaway-isolation, and post-impact-isolation standard, with an automatic high-voltage disconnect triggered on impact and a driver/marshal-visible HV status indicator.

3.3 **Hydrogen / pressurised storage.** Any pressurised storage must meet a defined burst-margin, crash-isolation, and venting standard.

3.4 **Common requirement.** Stored-energy systems must isolate automatically on an impact exceeding the Medical Warning threshold (Art. 5.3) and must be safe for marshals to approach within a defined time.
   > TODO: cite/define the specific standards for 3.2 and 3.3 (no single FIA number ports cleanly because F1 is not yet fully open on energy source).

---

## Article 4 — Driver Protection & Equipment

All items must carry a valid homologation to the stated (or equivalent current) standard, with expiry enforced at scrutineering. No exemptions.

| Item | Standard (or equivalent) | Note |
|------|--------------------------|------|
| Helmet | FIA 8860-2018 ABP | Ballistic protection variant |
| Frontal head restraint | HANS / FHR mandatory | Tethers certified |
| Fire-resistant clothing | FIA 8856-2018 | Suit, underwear, gloves, socks, shoes, balaclava |
| Harness | FIA 8853-2016, 6-point | HANS-compatible, ≤ 5-yr life |
| Seat | FIA 8862-2009 | Extractable as a unit with driver |
| Biometric monitoring | recommended | HR / SpO₂ to medical team |

---

## Article 5 — On-board Safety Systems

5.1 **Fire suppression.** Series-approved suppression system, sized to the energy load, driver-activated and auto-triggered above an impact threshold.

5.2 **Accident Data Recorder.** Minimum 3-axis high-g (≥ 250 g) + low-g accelerometers, speed, throttle, steering; data available to the series medical/safety official within minutes of an incident.

5.3 **Medical Warning Light.** Auto-triggers at **≥ 18 g**, upward-facing, visible to marshals from outside the car.

5.4 **High-speed cockpit camera** (≥ 200 fps) for post-incident injury reconstruction.

---

## Article 6 — Scrutineering for Safety

6.1 Before every event, every car: helmet/suit/harness/seat homologation tags and expiry, fire-suppression charge and routing, ADR function, cockpit-protection-device integrity, crash-structure integrity, wheel tethers, fuel-cell/HV-storage integrity and age, Medical Warning Light function.

6.2 **No-waiver policy.** Any failure = no start. There is no discretion.

---

## Article 7 — Circuit & Operational Safety

> **Basis & lesson:** Group B died because spectator separation was treated as an event-organiser problem, not a ruleset constraint. Formula Zynerji fixes the minimum at the *ruleset* level.

7.1 **Minimum circuit grade.** A series-recognised grade equivalent to **FIA Grade 2** minimum (Grade 1 recommended), independently audited.

7.2 **Run-off & barriers.** Defined minimum run-off at high-speed corners; energy-absorbing barriers (TecPro/SAFER-equivalent) at high-speed impact zones; tyre walls only at low-speed sections.

7.3 **Spectator separation.** A mandatory minimum spectator-to-track distance and barrier specification, defined here and **not** delegated to event organisers. *(The explicit Group B fix.)*
   > TODO: set the minimum distances/barrier classes by corner-speed band.

7.4 **Medical provision.** A medical car and a trauma-qualified physician present and deployed before any running begins; helicopter evacuation available during sessions; an extraction team trained specifically to this formula's cockpit geometry (halo + harness access).

7.5 **Neutralisation capability.** The series must be able to impose a controlled speed delta on all cars (Virtual-Safety-Car-equivalent, via the Standard Safety ECU) within **30 s** of an incident, plus a physical Safety Car and red-flag procedure (`sporting.md` Art. 7).

7.6 **Marshalling.** Flag and electronic marshalling-panel coverage at every post; marshals may not enter the racing surface without Race Control authorisation.

---

## Article 8 — The Safety Invariant (summary)

The minimum that holds regardless of any merit, cost, or performance consideration, in priority order:

1. Survival cell + full crash-test matrix (Art. 2) — passed pre-season, no waiver.
2. Cockpit protection device (Art. 2.2).
3. Homologated energy storage appropriate to the chosen source (Art. 3).
4. Dual wheel tethers (Art. 2.7).
5. Driver equipment to current standards (Art. 4).
6. ADR + Medical Warning Light + cockpit camera (Art. 5).
7. Fire suppression + collapsible steering column (Art. 5.1, 2.8).
8. Circuit grade + spectator separation + medical/extraction + neutralisation (Art. 7).
