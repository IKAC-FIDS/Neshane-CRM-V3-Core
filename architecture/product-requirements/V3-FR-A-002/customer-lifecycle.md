# Customer lifecycle — V3-FR-A-002

## Current guards and bounded availability — v1.7.0

User-confirmed CM1-PD-086..095 refine the preserved state machines below, not a new schema or implementation. Archive/restoration and manual verification remain CONDITIONALLY INCLUDED; exact evidence/applicability/contracts missing -> affected path BLOCKED. Formal acceptance PENDING.

| Operation/transition | Additional current product guard |
| --- | --- |
| Customer ACTIVE -> INACTIVE | Authorization, mandatory deactivation reason/Audit; open dependencies allowed with existing new-activity restrictions; preserve related stored states |
| Customer ACTIVE/INACTIVE -> ARCHIVED | Mandatory reason/Audit; every applicable dependency cleared with evidence; unknown/unavailable blocks; closed activities/history alone not blockers |
| ARCHIVED -> INACTIVE | Authorized conditional restoration with mandatory reason/Audit; no related activation/reopening |
| INACTIVE -> ACTIVE | Validate mandatory fields/definite identifier conflicts/authorization/Audit; ordinary reason optional; VERIFIED not globally required unless workflow requires; no automatic Branch/Relationship activation |
| ARCHIVED -> ACTIVE | Prohibited; use restoration then separately validated reactivation |
| Branch ACTIVE -> INACTIVE | Mandatory reason/Audit; parent/Person/Relationship stored states and history preserved |
| Manual Relationship END | Mandatory reason/Audit; Person/target/Role identities not rewritten; correction END+new, no ENDED reopening |
| Natural Relationship expiry | No manually supplied END reason; no stored-status mutation/scheduling mechanism selected; mutations if any retain Audit |
| New Relationship assignment | Deny inactive Person/Company/Branch/effectively inactive parent and other invalid eligibility; existing history preserved, no retrospective grant |

Archive dependency categories (only applicable capabilities): open sales opportunities, active contracts, open orders, open support tickets, active projects, ongoing tenders, outstanding delivery commitments, open activities/follow-ups, active Branches, active Relationships. No integration with an unimplemented service is invented. Lack of clearance evidence blocks archive, never counts as no dependency.

Relationship intervals use **calendar-day [start,end)**, inclusive start/exclusive end, future start allowed, optional end; empty/backwards invalid. **Exact applicable day time reference remains OPEN**, along with calendar presentation/storage. This is not a selection of timezone, calendar system, locking or conflict-set mechanism. Controlled overlap/historical ENDED participation/fresh reasons/version/idempotency/Tenant safeguards unchanged.

Verification transitions: initial NOT_VERIFIED; valid evidence/authorized success -> VERIFIED; material identity change or expired/invalidated essential evidence -> REQUIRES_REVERIFICATION; proven fundamentally invalid verification -> NOT_VERIFIED; successful authorized reverification -> VERIFIED. Dispute/objection alone cannot restore VERIFIED. No universal fixed expiry; preserve verification/revocation/invalidation history and record-lifecycle independence. Manual revocation needs reason/Audit; essential evidence and three different-verifier cases PD-089/090 required. Trusted system integration remains deferred and real data/documents prohibited in initial synthetic development.

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

## F. Role Definition lifecycle (v1.3.0 user-confirmed product direction)

Exactly ACTIVE / INACTIVE; valid creation starts ACTIVE; authorized validated ACTIVE → INACTIVE and INACTIVE → ACTIVE. Physical deletion is unsupported even without Relationships. Full guards: `customer-role-catalog.md#rc-003--lifecycle` (CM1-PD-060/061). Role status changes never mutate existing Relationships or their intervals; INACTIVE Roles cannot receive new assignments (CM1-PD-062). This is independent of Relationship ACTIVE/ENDED and Customer/verification states; no IAM lifecycle or grant is implied.

## Current v1.8.0 refinement (overrides only corresponding historical OPEN product portions)

See `customer-v180-scope-and-document-catalog.md` and PDR.
- CM1-PD-100: Tenant can require a document at initial registration or identity verification, or leave optional; default no mandatory initial registration documents. Add mandatory type or change optional to mandatory for subsequent applicable operations; mandatory to optional removes obligation; deactivate prevents new uploads for that type while preserving existing documents; rename retains identity; no physical deletion of type. Configuration changes do not automatically invalidate prior verification. Actual policy/legal prerequisites remain applicable.
- CM1-PD-102: Show NOT_PROVIDED, PROVIDED, EXPIRED, SUPERSEDED, INVALIDATED. PROVIDED denotes upload, not authenticity. INVALIDATED by authorized user; replacement retains historical SUPERSEDED version. Show completed mandatory documents versus total applicable mandatory documents, separately from verification status. Exact computation for stage, expiry/invalidity, zero denominator and precedence remains OPEN where not expressly settled; no new verification shortcuts.
- CM1-PD-104: Tenant-configurable timezone; initial Iran timezone Asia/Tehran. Relationship business dates are calendar days in Tenant timezone, half-open [start,end), future starts/open ends permitted. Issue/expiry of documents are calendar dates; date-only facts do not shift with timezone. Events and Audit timestamps UTC; user-local presentation and Persian/Gregorian calendar configurable independently of language. Preserve past business dates when Tenant timezone changes, and event history unchanged. Exact timezone-change effective evaluation and storage mechanisms OPEN.

All 19 PDQs remain OPEN; no formal acceptance, executable contract or Gate change.
