# Requirements-engineering validation report — V3-FR-A-002

Status: **PREPARED — READY FOR TASK OWNER REVIEW; not accepted**. Recording timestamp `2026-11-18T18:40:28.795918+00:00`.

## Recovery investigation outcome (Phase 1)

No V3-FR-A-002 artifacts existed in any worktree, stash, Git history or filesystem search. The earlier completion report was not backed by physical files; this run regenerated from authoritative sources. Nothing restored/overwritten/deleted.

## Preflight / canonical scope

- Core `d0dcfe6a257792c7457ba49f3112f85bc79b0883` on `codex/v3-fr-a-002`, clean. Backend `abd76d821c98e1fe10fe2d6c2c1772b0df7641e7`, Frontend `faa563f8f5c3bda25c3e5f40c7a8688c1bc245e7` unchanged.
- Canonical V3-FR-A-002: sequence 2, Core, no prerequisites, deliverables operation catalog / fields / rules / states / actor-resource policy / failure+profile scenarios / decision questions. No conflict.

## Coverage (derived from sources, not reproduced counts)

- **5 approved master entities** (Company, Person, Contact, Branch, Relationship).
- **4 documented operations** (CUS-CREATE, CUS-VALIDATE, CUS-GET-FOR-UPDATE, CUS-UPDATE).
- **10 candidate actions** mapped, all PROPOSED.
- **16 candidate fields** all PROPOSED/OPEN.
- **14 OPEN decisions** (7 carried + 7 new).

## Distinctions preserved

APPROVED / PROPOSED / OPEN explicit everywhere. No invented approval/ownership/role/RBAC/IAM/API/schema/technology. FR-BJ-001 separated from FR-BJ-002.

## Integrity

- 35 roadmap artifacts byte-identical (35).
- 11 accepted V3-FR-A-001 artifacts byte-identical (11).
- Backend/Frontend unchanged; no Docker/build/runtime tests; no staging/commit/push.

## Commands

Read-only Git recovery investigation; filesystem search; authoring helper `v3-fr-a-002-documents.py`; physical verification below.

## Recommended disposition

**READY FOR OWNER REVIEW — REQUIREMENTS BASELINE PREPARED WITH EXPLICIT OPEN DECISIONS.** Not authority-issued ACCEPTED. STOP after physical artifact verification.

## Decision reconciliation (v1.2.0)

- Product decision record extended to **57 user-confirmed decisions** (CM1-PD-001..057), covering entity model, duplicates, minimum fields, lifecycle, CUS-UPDATE, identity verification, relationship model, overlap (controlled-exception, authoritative), branch reparenting, and audit boundaries.
- **Supersession:** the controlled-exception Relationship overlap policy (CM1-PD-041) supersedes any prior absolute-overlap prohibition. No active absolute-denial rule or CM1-REL-21..40 criteria existed in the working tree.
- Open questions: 14 existing + 5 new (PDQ-002-08..12); none closed.
- Field dictionary: 16 + 1 (FLD-002-17 verification state) + 14 (REL-002-01..14 relationship fields) = 31 candidate fields; all remain PROPOSED/OPEN (none approved as mandatory).
- Acceptance criteria: canonical AC-01..05 + CM1-FLD-06, CM1-DUP-01..03, CM1-LC-01..03, CM1-UPD-01..05, CM1-VER-17/18, CM1-BRN-01..05, CM1-REL-01..13, CM1-AUD-01..05 — all PROPOSED / NOT TESTED.

## v1.2.1 Coverage Reconciliation

- **Field dictionary:** FLD-002-11 corrected to Required / Immutable (Branch parent Company reference) per CM1-PD-044/045/047; earlier Optional/Mutable superseded; persistence/API schema still unapproved.
- **Lifecycle:** restated as formal-source-baseline vs user-confirmed target (Company/Person, Branch, Relationship, Verification) with explicit transition matrices; the historical "no state machine / all transitions OPEN" statement is preserved only as source-baseline status.
- **Business rules / operation catalog / requirements:** stale OPEN/PROPOSED statements reconciled into APPROVED SOURCE INVARIANT / USER-CONFIRMED / PROPOSED / OPEN distinctions.
- **Acceptance criteria:** canonical 5 + detailed 83 = 88 unique IDs (expanded with lifecycle/branch/CUS-UPDATE/duplicate/relationship/audit edge cases).
- **Decision coverage matrix:** 57 decisions mapped; FULL=3, PARTIAL=47, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2.
- **OPEN questions:** 19 total; 7 partial resolutions recorded; none closed.
- **Relationship overlap:** controlled-exception policy remains authoritative; absolute-overlap prohibition remains superseded.
