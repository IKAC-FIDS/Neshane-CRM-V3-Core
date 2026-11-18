# Customer lifecycle — V3-FR-A-002

**No approved Customer state machine exists.** Candidate states only; all transitions OPEN.

## Candidate states (PROPOSED)

- ACTIVE (candidate)
- INACTIVE (candidate)
- ARCHIVED (candidate)
- PENDING_SUBMISSION (non-authoritative, permitted-not-required)

## Transition matrix

| From | To | Status |
| --- | --- | --- |
| (any) | (any) | OPEN — no approved transition |

## Governing boundaries

- Pending Submission never becomes a valid Customer Master or grants authority (DEC-005).
- Archive/deactivate and deletion have no approved policy; status change maps to CUS-UPDATE and remains PROPOSED.
- BC: only CUS-CREATE limited-interruption is BC-3 (CUS-BC-001); CUS-UPDATE/CUS-VALIDATE/CUS-GET-FOR-UPDATE remain NOT_ASSESSED. Evidence EVID-002-004, EVID-002-005, EVID-002-006, EVID-002-007.
- No retention/legal-hold/deletion policy approved; see PDQ-002-03 / PDQ-A001-050.

## Branch record states (user-confirmed)

- Branch states: **ACTIVE** / **INACTIVE**; no independently managed ARCHIVED state.
- Effective operational availability = Branch status + parent Company lifecycle + resource/action policy (CM1-PD-042).
- Company/Branch deactivation independence; archiving Company resolves Company+Branch dependencies; Branch history intact after Company archive; restoring Company does not auto-activate Branches (CM1-PD-043/046).

## Relationship lifecycle (user-confirmed, proposed for review)

- States: **ACTIVE** / **ENDED**. ENDED is not reopened; a later recurrence is a separate Relationship (CM1-PD-031).
- Half-open interval `[startDate, endDate)`; null end = open-ended; empty/backwards invalid (CM1-PD-032).
- Overlap: same Person+TargetType+TargetId+RoleCode overlapping intervals are allowed only via controlled exception (warning + authority + mandatory reason + Audit) (CM1-PD-033..041).

## Identity verification state machine (user-confirmed)

- States: **NOT_VERIFIED** / **VERIFIED** / **REQUIRES_REVERIFICATION** (independent of record lifecycle and commercial status).
- initial → NOT_VERIFIED; trusted system/manual evidence → VERIFIED; necessary-evidence expiry or material identity change → REQUIRES_REVERIFICATION; fresh success → VERIFIED; fundamental invalidity → NOT_VERIFIED. No universal TTL. (CM1-PD-019..028)
