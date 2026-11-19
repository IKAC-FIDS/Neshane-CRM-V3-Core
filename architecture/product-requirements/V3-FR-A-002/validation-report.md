# Requirements-engineering validation report — V3-FR-A-002

## Current supplement — v1.6.0 catalog governance, history and Audit

**PREPARED FOR USER REVIEW; USER-CONFIRMED PRODUCT DIRECTION; formal acceptance PENDING.** Earlier reports are historical, not renewed execution evidence. No executable architecture, IAM, Audit integration, runtime or production approval is granted.

### A. Repository baseline and scope

- Root `E:/Neshane-CRM-V3-V3-024-main-adoption`; branch `codex/v3-fr-a-002`; original/full HEAD `895efd76595ca36a9ee5c8028a67c8854d5d318e`, matching requested prefix `895efd7`. Initial worktree/index clean; baseline v1.5.0, 72 decisions, 5 canonical +128 detailed criteria, 19 OPEN IDs verified from actual files.
- Task V3-FR-A-002 / PDQ-002-08. Exact user decisions CM1-PD-073..077, source, scope, baseline and actual UTC recording time in PDR JSON catalogGovernanceAuthority/decisions; issuance time not supplied. Prior authority records/provenance preserved.
- Only Markdown/JSON documentation in the requested package modified. No Backend/Frontend/product code/schema/migration/API/IAM grant/application test/build/runtime work. No add/commit/push/merge/rebase/reset/clean, branch change, next roadmap task or acceptance decision.

### B. Product reconciliation and scoped review

- CM1-PD-073: reason OPTIONAL for Hide/Unhide, Audit MANDATORY, own-Tenant authorized catalog managers only; actor/Tenant/Role/old-new selectability/time/optional reason preserved; no Relationship/history/other-Tenant or global inactive/scope/authority bypass.
- CM1-PD-074: authorized System metadata under controlled release versus own-custom Tenant metadata; labels/translations/descriptions preserve identity/semantics and old/new values. Ordinary reason OPTIONAL, Audit MANDATORY. No unique-label identity, mandatory language/localization storage or Relationship mutation; materially different Role needs new Role/new code under existing reservation rules.
- CM1-PD-075: authorized current Relationship title is current valid title; event/Audit title remains event-time title without rewrite. Hidden/INACTIVE Roles stay visible in existing authorized references/history. Temporal/version/snapshot/reference/API representation remains OPEN; initial vocabulary v1.0 evidence is not rewritten by future display releases.
- CM1-PD-076: three independent logical System-governance/Tenant-manager/Customer-operator responsibilities, not executable IAM roles or appointments. Backend authorization mandatory; neither management nor assignment implies the other. No identity/code/deletion override, business-role IAM/admin/legal grant or new three-person SoD rule; prior scope/overlap safeguards retained.
- CM1-PD-077: explicit mandatory catalog-operation and unauthorized-modification Audit with logical information, old/new applicable values, isolated immutable history and no successful state-change report without durable guarantee. Ordinary reasons optional; incompatible-scope reason and publication reason including release reference mandatory. Optional ordinary metadata reason cannot waive publication reason.
- Catalog-specific unauthorized-attempt Audit now has an explicit product basis; no blanket event rule for ordinary reads, unrelated warnings or all validation failures. Existing source/security monitoring and coordinated durable obligations remain unchanged; ACK/outbox is not authoritative ingestion and no new transaction/defer protocol is selected. Protected old/new Audit values are not unredacted public logs or cross-Tenant disclosures.
- Removed stale active blanket policy-OPEN wording from requirements/operation/assessment notes by distinguishing source-baseline inventory, confirmed product direction, technical OPEN contracts and formal acceptance PENDING. Five canonical definitions and previous business decisions remain unchanged; general historical failure dispositions explicitly identified as historical, not policy overrides.
- Scoped review found no unresolved contradiction in the five new policies. Exhaustive re-review of older product ambiguities, source execution/recovery claims, independent specialist assessment and actual authorization/Audit durability: NOT VERIFIED. This is not Security Sign-off.

### C. Inventory and coverage

- **77 unique decisions**; prior 72 parsed objects and raw UTF-8 object substrings unchanged against reviewed Git baseline. Exact 12-role initial vocabulary unchanged in JSON/Markdown, including Persian ZWNJ and scopes. Role lifecycle, applicability, ordinary controlled overlap, code/default/uniqueness/reservation policy sections retained verbatim; Customer lifecycle/verification/deployment files unchanged.
- All 31 field IDs retained. Only FLD-002-15 Audit-correlation and REL-002-06 title descriptions/constraints clarified; logical Audit information is not an approved schema/new physical field list. Role registry uniqueness is not Relationship row uniqueness.
- Actual criteria: baseline 5+128=133; current **5 canonical +153 detailed =158 unique IDs**. Added **CM1-ROL-46..70 (25)** only; all previous definition lines preserved. New criteria PROPOSED / NOT TESTED with implementation-dependent execution BLOCKED. No literal duplicate new scenario under another ID; scoped review checks their new governance/history/Audit distinctions from earlier generic scenarios.
- Matrix **FULL=3, PARTIAL=67, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2**; complete 77-entry machine/human inventories. Five new decisions PARTIAL with direct rules/logical operations/scenarios/fields-or-explicit-gaps/OPEN references and technical residuals; no earlier class promoted.
- All 19 OPEN IDs retained; PDQ-002-08 OPEN / PARTIALLY ANSWERED. Hide/Unhide reason, metadata governance, current/event-time display, logical authorities and Audit product coverage/reasons/information are answered, not closed executable contracts. Current register/RC-OPEN/RC-PROPOSED/Traceability updated; earlier version dispositions explicitly historical.
- Still OPEN: exact catalog/configuration/default materialization; IAM/operations/permissions/grants/actor mappings/technical enforcement; temporal/version/snapshot/localization/reference/API; Audit schema/event names/transactions/storage/retention/recovery/access/failure protocols; namespace/concurrent uniqueness/reservation/scope/assignment mechanisms; Unicode/encoding/further grammar; cross-Tenant collision detection/privacy/authority; publication/release/rollback/authorized resolution and semantic-change assessment procedure.

### D. Commands, validation results and failures

```powershell
git --no-optional-locks status --short --branch --untracked-files=all
git --no-optional-locks rev-parse HEAD
git --no-optional-locks diff --cached --stat
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-160-validate.py
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-160-validate.py --manifest
git --no-optional-locks diff --check
git --no-optional-locks diff --stat
git --no-optional-locks status --short --untracked-files=all
```

- Initial documentation run: **42/43 PASS, 1 FAIL** in the new section-preservation checker. Its heading regex used a greedy dot under DOTALL, incorrectly including subsequent sections. Corrected the heading match to stop at newline; same 13 old sections still compared, no expected set/control removed. Rerun **43/43 PASS**. This was validator parsing, not a software test or accepted policy change.
- One combined patch was rejected by context verification because an expected sentence had an actual `Examples and guard detail` prefix; no files changed by that rejected patch. Re-read actual context and applied narrower patches. No user work reset/deleted and no check suppressed.
- JSON syntax, decision/raw preservation, vocabulary, field/criterion/OPEN uniqueness, literal scenario duplication, matrix/ledger completeness, introduced IDs/file/anchor links, current versions/counts, known stale reason-OPEN wording, Tenant/history/Audit policy boundaries, documentation-only scope and whitespace checked. Source inventory/evidence/historical SHA/authority/governance data preserved, not recast as current execution proof.
- Final manifest-mode run: **45/45 PASS**, including complete inventory/self-exclusion and all exact current file-byte SHA-256 values. The report hash is regenerated after this recording and the check repeated. This validates consistency, not independent authenticity of the manifest. Historical source SHA values are not recalculated. git diff --check PASS; only LF-to-CRLF working-copy warnings, no whitespace errors.
- Checker is task-local outside Git, not application code or a durable runtime test suite. Build/application/integration/runtime tests NOT EXECUTED; all proposed software scenarios stay BLOCKED. No dependency/network, service or Docker activity; no external specialist/runtime evidence claimed.
- Manual review required: exact five PDR decisions, RC-017..021 reason/Audit matrix, logical authority separation, current/event-time title distinction, future display release versus immutable vocabulary/history, failure scenarios, remaining contracts and CM1-ROL-46..70. Next action is user review only; later Git, formal acceptance and executable contract work require separate explicit authorization.

### E. Governance unchanged

G-RUNTIME: BLOCKED; FE-BE: PENDING; AUTH/IAM: PENDING; Offline: PROHIBITED; Local-Infra: ACCEPTED — DEVELOPMENT-ONLY; Production: NOT AUTHORIZED; Formal acceptance: PENDING. Pending Submission PERMITTED NOT REQUIRED and non-authoritative. Existing coordinated durable Audit obligations retained.

## Historical v1.5.0 supplement (not renewed v1.6.0 evidence)

### v1.5.0 defaults and canonical code policies

**PROPOSED DOCUMENTATION PACKAGE; formal acceptance PENDING.** Earlier sections are historical evidence only; their previous inventory/OPEN statements are not current where superseded by this supplement. No executable design or Gate disposition is granted.

### Baseline, scope and authority

- Task V3-FR-A-002 / Customer Master v1.5.0 / Relationship Role Catalog / PDQ-002-08. Root `E:/Neshane-CRM-V3-V3-024-main-adoption`; expected and actual branch `codex/v3-fr-a-002`, original HEAD `92d02d2c45103d5223e5d9ffd7a6bafc556e3443`. Initial worktree/index clean. No branch/index mutation, stage, commit or push.
- New IDs CM1-PD-068..072 and CM1-ROL-30..45 were verified unoccupied before authoring. User task decisions are USER-CONFIRMED PRODUCT DIRECTION; exact words, scope, baseline and actual UTC recording timestamp are in PDR JSON defaultCodePolicyAuthority/decisions. Issuance time not supplied; historical authority/provenance retained.
- Documentation only, confined to the requested package. No executable schema/API/IAM/DB/persistence/migration/Audit integration/runtime/offline/release implementation or approval. No application code/test, Backend/Frontend or unrelated source/roadmap change.

### Current inventory and traceability

- **72 unique decisions CM1-PD-001..072.** All 67 prior JSON decision objects and their original UTF-8 object substrings remain identical to the reviewed Git baseline. New CM1-PD-068..072 represented in Markdown/JSON with RC-012..016 and scenario/operation/field-or-explicit-gap/OPEN mappings.
- Exact original 12-entry System vocabulary unchanged in JSON and Markdown, including Persian titles/ZWNJ/scopes. All 31 field IDs retained; only REL-002-05 registry/reference policy clarified. Registry code uniqueness is not uniqueness of roleCode across Relationship rows. No new approved field/schema or roleId-based overlap key.
- Actual baseline acceptance definitions: 5 canonical +112 detailed =117; current 5 +128 =**133 unique IDs**. Added exactly CM1-ROL-30..45 (16), all PROPOSED / NOT TESTED, software execution BLOCKED pending relevant design. All earlier definition lines, including canonical five and CM1-ROL-01..29, unchanged.
- Coverage: **FULL=3, PARTIAL=62, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2**. All five new decisions PARTIAL with direct proposed scenarios and explicit residual contracts; no older coverage class promoted. Product answers are not blocked merely because implementation design remains OPEN.
- **19 OPEN question IDs preserved**; PDQ-002-08 stays OPEN / PARTIALLY ANSWERED. Current RC-OPEN/RC-PROPOSED, register and Traceability mark default policy, scoped uniqueness/permanent reservation, future collision blocking and trim-uppercase/ASCII/3..64 normalization ANSWERED at product level. Earlier versions' OPEN language is explicitly historical.
- Still OPEN: exact catalog/configuration schema/persistence/default materialization; namespace/concurrent uniqueness/reservation enforcement; cross-Tenant conflict detection authorization/privacy; publication/version/rollback and authorized resolution workflow; Unicode trim/uppercase/input encoding/additional proposed grammar; operation IDs/IAM/actor mappings; Role Audit/failure/recovery; ordinary hide/unhide mandatory reason; history/reference/temporal/API and scope-change/assignment consistency.

### Scoped review and limitations

- Confirmed policies preserve prior Tenant settings and existing Relationships through defaulting/releases, global INACTIVE override, identity-preserving reactivation and scoped permanent reservation. Same custom code is allowed across independent Tenants. Conflict blocks only the proposed conflicting System Role; no automatic Role/Relationship mutation or central private-data inspection right.
- Trim-uppercase/allowed ASCII output/3..64 length is confirmed without an extra first-letter or underscore-placement rule. The validator's isolated ASCII documentary fixtures illustrate examples and boundaries only; they are not a production Unicode normalizer or application tests. Further lexical/Unicode behavior remains PROPOSED / OPEN.
- Controlled overlap, no additional supervisor approval for ordinary authorized overlap, separate management/reason requirements for incompatible scope changes, validated Tenant Context/fail-closed Customer Domain authorization, no physical deletion and no IAM/legal authority grant preserved. Ordinary hide/unhide reason policy is still OPEN, not inherited from scope changes.
- Source inventory, original evidence/revisions/SHA values, historical authority, governance fields and adjacent lifecycle/verification/failure/deployment files preserved. Scoped review found no remaining contradiction in the five new policies; exhaustive re-review of earlier product policies, historical recovery claims and independent specialist assessment is NOT VERIFIED.
- Authoring correction: an extra closing brace introduced while appending decisions was spotted in a read and corrected before the first validator run; original decision objects then passed semantic and raw-byte preservation checks. No failing control disabled or expected count reduced.

### Actual validation commands and results

```powershell
git --no-optional-locks status --short --branch --untracked-files=all
git --no-optional-locks rev-parse HEAD
git --no-optional-locks diff --cached --stat
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-150-validate.py
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-150-validate.py --manifest
git --no-optional-locks diff --check
git --no-optional-locks diff --stat
git --no-optional-locks status --short --untracked-files=all
```

- Structural/documentation run: **39/39 PASS**; final manifest-mode run: **41/41 PASS**, including complete inventory/self-exclusion and exact-byte SHA-256 consistency. JSON syntax, raw/semantic decision preservation, vocabulary, criteria/field/OPEN IDs, all five new mappings, cross-file paths/anchors, current versions/counts, historic/current OPEN distinctions, scope, unchanged governance and whitespace checked. No validation failures remained. Report hash is regenerated after this update and the final control repeated.
- Manifest uses the existing exact-byte SHA-256 convention and excludes itself. Full inventory/hash consistency PASS; this does not independently authenticate the manifest. Historical source SHA values are not recalculated. git diff --check PASS with only LF-to-CRLF working-copy warnings, no whitespace errors.
- The checker is task-local outside Git, not application code or a durable runtime test suite. It uses read-only git show/diff for baseline comparisons; introduced reference checks and fixture assertions are documentary evidence only.
- Build/application/integration/runtime tests **NOT EXECUTED** (documentation-only); no dependencies/network activity, services or Docker resources used. All new software scenarios remain unexecuted and contract-blocked. No skipped check is labelled software PASS.
- Manual review needed: exact new PDR decisions and RC-012..016, namespace scope versus repeated Relationship refs, only-conflicting-Role publication gate/privacy, normalization examples, remaining contracts and CM1-ROL-30..45 dependencies. Next authorized action is user review; formal acceptance, executable contract decisions and Git operations require separate authorization.

### Governance — unchanged

G-RUNTIME: BLOCKED; FE-BE: PENDING; AUTH/IAM: PENDING; Offline: PROHIBITED; Local-Infra: ACCEPTED — DEVELOPMENT-ONLY; Production: NOT AUTHORIZED; Formal acceptance: PENDING. Pending Submission remains PERMITTED NOT REQUIRED and non-authoritative; coordinated durable Audit obligations preserved.

## Historical v1.4.0 supplement (not renewed v1.5.0 evidence)

### v1.4.0 vocabulary and Tenant selectability

**PROPOSED DOCUMENTATION PACKAGE; formal requirements acceptance PENDING.** This supplement supersedes only current inventory/residual statements of earlier reports, not historical decision semantics or source provenance. Historical reports below are not renewed execution evidence.

### Baseline and authority

- Task: V3-FR-A-002, Customer Master v1.4.0. Root `E:/Neshane-CRM-V3-V3-024-main-adoption`; origin `https://github.com/IKAC-FIDS/Neshane-CRM-V3-Core.git`; branch `codex/v3-fr-a-002`; HEAD `41a0620ba8216cc86afcccfccbb849ee5e33782e`. Verified against the requested values before editing; initial worktree and index clean.
- Authority: user task sections CM1-PD-066/067 are USER-CONFIRMED PRODUCT DIRECTION; proposed supplementary governance rules are not confirmed decisions. Exact wording/data, reviewed baseline, actual UTC recording time and unknown owner issuance time are recorded in PDR JSON vocabularySelectabilityAuthority/decisions. Historical authority records retained.
- Documentation only: no executable code, schemas, migrations, application tests, IAM configuration, Backend/Frontend, deployment or unrelated roadmap edit; no implementation/architecture/runtime authorization inferred. No stage, commit, push or other branch mutation.

### Changes and coverage

- CM1-PD-066 records initial System Role Vocabulary v1.0: exactly 12 codes/Persian titles/scopes in PDR JSON catalogEntries and RC-009. Data is documentation, not a DB seed/schema/migration; no fixed roleId/English title assumed. No exclusive PRIMARY_CONTACT, implicit IAM or verified legal authority.
- CM1-PD-067 / RC-010/011 adds Tenant-local assignment restriction and effective eligibility, not global Role editing/deactivation. Customer Domain enforcement includes direct API attempts and invalid effective-state rejection during concurrent hide/finalization. Preserve global identity/status/scope, other Tenants, existing ACTIVE/ENDED Relationships and otherwise authorized history. Restore selectability cannot reactivate a global INACTIVE Role or reopen ENDED.
- 67 unique decisions; original CM1-PD-001..065 JSON object substrings byte-identical to the Git baseline and parsed objects unchanged. Existing overlap policy, management authority for incompatible scope changes, roleCode conceptual key, Branch and verification/lifecycle boundaries retained. No new physical deletion or mandatory hide/unhide reason rule.
- Coverage: FULL=3, PARTIAL=57, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2. Both new decisions have explicit criterion/field/operation/OPEN links and residual gaps. No earlier coverage class promoted. Values and product policy are answered; executable contracts are not approved.
- Actual criterion definitions: baseline 5 canonical + 99 detailed = 104; current 5 + 112 = 117, all unique. Only new IDs CM1-ROL-17..29 (13); five canonical definitions and all 99 earlier detailed definition lines unchanged, including CM1-ROL-01..16. New scenarios remain PROPOSED / NOT TESTED; executable cases explicitly BLOCKED pending relevant contracts.
- PDQ-002-08 remains OPEN / PARTIALLY ANSWERED; vocabulary v1.0 and Tenant-selectability product policy answered. All 19 OPEN IDs preserved. Remaining contracts: future catalog/publication, defaults for new Tenants/later roles, exact configuration/schema/reference/persistence, normalization/length/namespaces/custom collisions, operation/IAM/Audit names, ordinary hide/unhide reason policy, concurrency/dependency consistency, history/display, Audit failure/recovery, temporal/API compatibility. RC-PROPOSED does not choose any default/namespace/event/reason rule.
- Source inventory/evidence, historical SHA values, approved source invariants and governance fields preserved. Current manifest covers exact bytes of every other package file, excluding itself under the existing convention; consistency is not authentication of the manifest.
- Scoped manual review: new policy does not confer security/legal authority, Tenant override of global lifecycle/scope, exclusive primary contact or roleId-based overlap design. Ordinary authorized overlap still has no extra supervisor approval; incompatible scope changes retain their distinct management/reason requirements.

### Commands actually executed / validation boundary

```powershell
git --no-optional-locks status --short --branch --untracked-files=all
git --no-optional-locks rev-parse HEAD
git --no-optional-locks rev-parse --show-toplevel
git --no-optional-locks diff --cached --stat
git --no-optional-locks remote get-url origin
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-140-validate.py
python -X utf8 C:/Users/user/AppData/Local/Temp/opencode/a002-role-140-validate.py --manifest
git --no-optional-locks diff --check
git --no-optional-locks diff --stat
git --no-optional-locks status --short --untracked-files=all
```

The task-local validator is outside the repository; its read-only Git baseline comparisons check decisions, criterion definition lines, field IDs, source inventory, governance, scope and unchanged adjacent documentation. It independently compares the exact 12-entry table, including Persian ZWNJ, resolves introduced file/anchor references and computes counts from definition lines, not citations. Manifest mode verifies completeness/exclusion and all current SHA-256 values.

- Structural/documentation run: **34/34 PASS**; manifest-mode run: **36/36 PASS**, including complete inventory/self-exclusion and exact current SHA-256 checks. No software-test PASS is claimed. Manifest is regenerated after this report update and the final check repeated.
- First combined patch was rejected by context verification; no files were changed by that rejected patch. Re-read actual compact JSON mappings and applied smaller patches. No checks disabled or expected counts reduced.
- `git diff --check`: **PASS**, no whitespace errors; only LF-to-CRLF working-copy warnings. The validator also passes package-wide trailing-whitespace checks.
- Application/build/integration/runtime tests: **NOT EXECUTED** (documentation-only). No network/dependency resolution, service or Docker resources used. Exhaustive re-review of all earlier product policies, historical recovery claims, production readiness and independent specialist assessment: **NOT VERIFIED**.
- Manual review required: exact RC-009 vocabulary, RC-010/011 effective eligibility/history/authority, RC-PROPOSED residuals, PDR new decisions, CM1-ROL-17..29 blocked scenarios and coverage gaps. Next action is user review; contract disposition, formal acceptance and Git operations require separate authorization.

### Governance — unchanged

- G-RUNTIME: BLOCKED
- FE-BE: PENDING
- AUTH/IAM: PENDING
- Offline: PROHIBITED
- Local-Infra: ACCEPTED — DEVELOPMENT-ONLY
- Production: NOT AUTHORIZED
- Formal requirements acceptance: PENDING

Pending Submission remains PERMITTED NOT REQUIRED and non-authoritative. Existing coordinated durable Audit obligations are preserved; no executable API/IAM/DB/persistence/offline/deployment contract is approved.

## Historical v1.3.0 supplement (not renewed v1.4.0 evidence)

### v1.3.0 Role Catalog (proposed package; formal acceptance PENDING)

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
