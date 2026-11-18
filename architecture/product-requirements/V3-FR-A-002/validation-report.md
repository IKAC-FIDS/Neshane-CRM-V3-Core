# Requirements-engineering validation report — V3-FR-A-002

## Current supplement — v1.3.0 Role Catalog (proposed package; formal acceptance PENDING)

The older sections below are historical reports, not renewed evidence for this task. In particular, this update does not revalidate recovery-investigation claims, historical Backend/Frontend HEADs, or earlier broad semantic-consistency claims. Current evidence is limited to the changes and checks listed here.

- Task: V3-FR-A-002 / Customer Master / Relationship / PDQ-002-08. Exact authority/source, baseline and actual UTC recording time: `customer-role-catalog.md#authority-and-scope` and PDR JSON `roleCatalogAuthority`.
- Root: `E:/Neshane-CRM-V3-V3-024-main-adoption`; branch `codex/v3-fr-a-002`; initial HEAD `5d9c2f491e24a5afdc8349fd067be982e1e64365`; initial working tree and index clean. No Git mutation authorized or executed.
- Added CM1-PD-058..065; total 65. Original 57 decision objects preserved without modification. Hybrid organizational catalog is not an IAM/RBAC grant. No exact vocabulary, namespace, executable schema, permission or API contract selected.
- New requirements/rules: `customer-role-catalog.md` RC-001..008/RC-OPEN; linked from requirements, rules, lifecycle, operation catalog, actor policy and field dictionaries. No field ID or approved source entity added.
- Coverage: FULL=3, PARTIAL=55, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2. All eight new decisions PARTIAL with explicit residual gaps; testable scenarios alone do not approve their executable contracts. Existing 57 coverage records retained.
- Acceptance inventory: previously 5 canonical + 83 detailed = 88; now 5 + 99 = 104 unique definition IDs. Added CM1-ROL-01..16 only; all PROPOSED / NOT TESTED. No original criterion definition removed or altered.
- OPEN inventory: 19 unchanged. PDQ-002-08 is OPEN / PARTIALLY ANSWERED with eight explicit residual contracts, dependent decisions/scenarios and related PDQ-002-10/12. No closure; affected executable design blocked pending disposition.
- Found and corrected: Traceability's current decision-register version was stale at 1.2.0; now 1.3.0. Historical source inventory, evidence, revisions and SHA values preserved. Source-baseline OPEN entries remain historical; the current partial-resolution ledger states the new answers.
- Manual scoped review: new policy preserves controlled-exception overlap and does not equate catalog management authority with CUS-CREATE or with ordinary overlap authorization. Role scope changes requiring management authority are not a new supervisor requirement for overlap. Exact Role reference/technical overlap key remains OPEN; no new absolute-overlap prohibition introduced.

### Actual validation commands and scope

Executed from the Root above:

```powershell
git --no-optional-locks rev-parse --show-toplevel
git --no-optional-locks status --short --branch --untracked-files=all
git --no-optional-locks rev-parse HEAD
git --no-optional-locks diff --cached --stat
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-130-validate.py
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-130-validate.py --manifest
git --no-optional-locks diff --check
git --no-optional-locks diff --stat
git --no-optional-locks status --short --untracked-files=all
```

The local checker is outside the package, not a durable software-test suite. It uses read-only `git show` against the reviewed HEAD for preservation comparisons. Its manifest mode checks exact current file bytes and full file inventory, excluding the manifest itself. The manifest cannot authenticate itself; an independently reviewed digest or future authorized Git recording is required for tamper evidence.

- Documentation/structural checks: PASS (27 checks before manifest regeneration; final manifest-mode result is recorded in the task response). JSON parsing, unique/preserved decisions/fields/criteria/OPEN IDs, references, matrix counts, current versions, baseline source invariants, scoped changes and whitespace checked.
- Validation tooling corrections: first text-inspection command failed under Windows cp1252; repeated with `python -X utf8`. Initial checker counted only table criteria and missed the five canonical bullet definitions (three count checks failed); corrected the parser to read actual canonical definitions, without weakening expected counts. Rerun: 27/27 PASS.
- Semantic review is scoped to the new Role decisions and their interactions; exhaustive re-review of all pre-existing product policy, historical evidence and independent specialist assessment: NOT VERIFIED.
- Software/build/runtime/integration tests: NOT EXECUTED (documentation-only task). No implementation, DB migration, IAM configuration, Backend/Frontend, deployment or unrelated roadmap edit. No network/dependency activity, Docker resource or service execution.
- Gates unchanged: G-RUNTIME BLOCKED; FE-BE/AUTH/IAM PENDING; Offline PROHIBITED; Local-Infra ACCEPTED — DEVELOPMENT-ONLY; Production NOT AUTHORIZED. Pending Submission PERMITTED NOT REQUIRED, non-authoritative; coordinated durable Audit obligations preserved.
- Manual review needed: PDR new exact decisions, RC-006 management/impact guards, RC-007 system/Tenant distinction, eight RC-OPEN residual contracts, CM1-ROL scenarios and coverage gaps. Next step requires separate user review/disposition; no formal acceptance or Git action inferred.

## Historical report (pre-v1.3.0; not revalidated by this update)

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
