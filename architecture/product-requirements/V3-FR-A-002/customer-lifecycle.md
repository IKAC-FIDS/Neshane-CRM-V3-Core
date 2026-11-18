# Customer lifecycle — V3-FR-A-002

## A. Formal source baseline

The authoritative source baseline (V3-003 decision record, support-matrix, V3-002B ownership) did **not** previously approve a detailed Customer lifecycle state machine. The earlier "no approved state machine / all transitions OPEN" statement is retained as historical source status only, not as a contradiction of the user-confirmed target lifecycle below.

## B. User-confirmed target product lifecycle — Company and Person

States: **ACTIVE** / **INACTIVE** / **ARCHIVED**. Record lifecycle is separate from commercial status and identity verification. No independent authoritative PENDING_SUBMISSION lifecycle state is introduced (Pending Submission remains PERMITTED NOT REQUIRED and non-authoritative).

| Transition | Guard condition |
| --- | --- |
| CREATE → ACTIVE | After successful authorized create and validation |
| ACTIVE → INACTIVE | Allowed; ongoing activities preserved |
| INACTIVE → ACTIVE | Revalidation required |
| ACTIVE → ARCHIVED | All applicable open dependencies resolved |
| INACTIVE → ARCHIVED | All applicable open dependencies resolved |
| ARCHIVED → INACTIVE | Authorized recovery; no auto-reopen of activities/relationships |
| ARCHIVED → ACTIVE | **Prohibited** |

Rules: deactivation allowed with open activities; existing activities preserved; new activities restricted by owning-module policy; archive requires resolution of all applicable open dependencies (unknown dependency status is NOT treated as cleared); archive does not delete data/relationships/Audit; restoration does not auto-reopen closed activities/relationships.

## C. Branch lifecycle

States: **ACTIVE** / **INACTIVE** (no independent ARCHIVED). Effective availability = Branch status + parent Company lifecycle + applicable policy.

- Company deactivation does not mutate stored Branch statuses; Company restoration does not auto-activate inactive Branches.
- Parent Company ID remains immutable (CM1-PD-044); direct reparenting prohibited; transfer via new Branch (CM1-PD-045).
- Company archiving requires resolution of applicable open dependencies across Company and Branches (CM1-PD-046).

## D. Relationship lifecycle

States: **ACTIVE** / **ENDED**. ENDED is not reopened; a later recurrence is a separate Relationship. Independent temporal validity `[startDate, endDate)` (half-open; null end = open-ended; empty/backwards invalid). Overlap governed by the controlled-exception policy (CM1-PD-033..041).

## E. Verification lifecycle

States: **NOT_VERIFIED** / **VERIFIED** / **REQUIRES_REVERIFICATION**, independent of Customer record lifecycle.

- initial → NOT_VERIFIED; trusted system/manual evidence → VERIFIED; necessary-evidence expiry or material identity change → REQUIRES_REVERIFICATION; fresh success → VERIFIED; fundamental invalidity → NOT_VERIFIED. No universal TTL.

No unapproved API, database, or IAM implementation choice is presented as an accepted requirement.
