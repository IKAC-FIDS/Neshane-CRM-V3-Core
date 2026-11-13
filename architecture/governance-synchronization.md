# Cross-repository governance synchronization

V3-024 temporal qualification: the P00-006 non-effective and Events 2–4 PENDING statements below
are preserved pre-E4 snapshots. For the completed boundary and current design/reference effectivity,
see the [E5 administrative record](#v3-024-r2-administrative-effectiveness-record).

## Baseline

- Current reference: `NESHANE-V3-GOV-P00-000A`.
- Scope: the Root `AGENTS.md`, Root engineering standards, and this synchronization policy.
- This reference is a governance revision label, not an ADR. It does not approve choices explicitly marked proposed or unresolved.
- Current approved architecture revision: `NESHANE-V3-ARCH-P00-005` upon traceable commit of the OD-020 decision package; ADR-V3-001 through ADR-V3-012 were formalized under R0-001, ADR-V3-013 records the Backend foundation toolchain selection, ADR-V3-014 records REST/event versioning and ADR-V3-015 records risk-based Contract Testing governance.
- Architecture revisions do not silently rename this governance reference. A V3 ADR is authoritative after explicit approval and storage in the Root architecture area.

## Ownership

- Root owns cross-repository principles, ADRs, shared standards, and architecture review policy.
- Backend owns Java/Spring Boot implementation guidance and repository-local skills.
- Frontend owns framework-neutral frontend implementation guidance and repository-local skills.
- Backend and Frontend remain independent Git repositories. Do not use submodules, nested-repository tracking, or synchronization automation for this policy.

## Propagation process

1. Approve the architecture change in Root and update the affected Root standard or ADR.
2. Assign a new architecture revision for an architecture change. Change the governance baseline reference only when governance rules themselves change and the authorizing task requires a new governance revision.
3. Review impact on Backend and Frontend separately.
4. Update only affected local instructions, standards, and skills; record the applicable governance and architecture references in each repository's `architecture/governance-baseline.md`.
5. Review local differences for consistency before implementation resumes. Propagation is complete only when each affected repository records the same current reference.

## Completed local propagation under R0-003

R0-003 propagated architecture revision `NESHANE-V3-ARCH-P00-002` and governance reference `NESHANE-V3-GOV-P00-000A` to the affected repository-local instructions, standards, skills, and governance baselines without changing approved ADRs:

- Backend synchronization: commit `6a7afc5`; independent build/test/version/release boundaries, domain-owned authorization with shared policy governance, contract coexistence/deprecation, controlled co-deployment, and profile-specific readiness evidence were reconciled.
- Frontend synchronization: commit `f3d138f`; modular feature-oriented architecture, shared Design System ownership, no initial Micro-Frontend requirement, controlled contract compatibility, and evidence-based readiness terminology were reconciled.

Both local governance baselines now record the current architecture and governance references. This completion records documentary propagation only; it does not establish implementation or production readiness, or independent R0 reviewer approval. Future architecture or governance revisions continue to follow the propagation process above.

## V3-005 propagation state

Architecture revision `NESHANE-V3-ARCH-P00-003` changes the Backend foundation baseline only. Backend commit `8f1cfaca40c0471a03418831aacfbe2689417cad` records the synchronized local governance reference, ADR-V3-013 engineering guidance, complete Gradle foundation and bounded R0 acceptance. Traceable Backend propagation is complete. Frontend is unaffected by the toolchain decision.

The V3-005 CPO/Technical Architecture Owner direction also replaces the project blanket build/test prohibition with controlled, Task-scoped local execution. Root commit `c65c97d746c804e0569ff50701d1f4eaedae7312` and Backend commit `8f1cfaca40c0471a03418831aacfbe2689417cad` record the shared and local policies. Offline build, formatting, module-boundary, dependency-report and reproducibility evidence is recorded in the Backend baseline; Gradle test tasks were `NO-SOURCE`, so no Unit Test coverage or passing Unit Test suite is claimed.

`V3-005` is `CLOSED — ENGINEERING FOUNDATION R0 BASELINE`. Closure establishes the engineering foundation only; it does not establish Spring Boot application/runtime verification, Security Sign-off, CI evidence, deployment-profile assurance, publishing, release authorization or Production Readiness.

## V3-010 development-first propagation state

The CPO/Technical Architecture Owner authorizes a prospective development-first policy for ordinary Tasks. Root, Backend and Frontend may implement, resolve pinned dependencies from approved official registries, build, test, debug, and use isolated Task-owned local services/containers without repeated per-command approvals. The explicit Task ID and affected component boundaries remain mandatory.

This propagation removes project-owned blanket execution prohibitions from repository instructions, testing standards and mandatory skills. It does not alter an ADR, security invariant, production gate or architecture revision. Governance reference `NESHANE-V3-GOV-P00-000A` remains unchanged because V3-010 did not authorize a new label.

The synchronized guardrails prohibit production/customer data and credentials, untrusted registries, disabled integrity checks, privileged/host-network containers, sensitive host or Docker-socket mounts, unrelated resource deletion, publishing, push, remote mutation and deployment without their required authorization. Security-critical decisions, risk acceptance, executable `DURABLE_DEFER`, production migrations and releases retain their existing approval gates.

## OD-008 propagation state

Architecture revision `NESHANE-V3-ARCH-P00-004` closes OD-008 through DEC-014/ADR-V3-014 upon a traceable Root commit. The accepted Backend V3-011 and V3-012 engineering baselines already implement conforming bounded conventions for public REST URI-major versioning, CloudEvents 1.0-compatible envelopes, independent event/payload/schema versions, immutable baselines and fail-closed compatibility analysis. This governance-only task does not modify those implementations.

Backend synchronization commit `03987f4cf7ffab377742e5f8799bccd16f5851eb` records architecture reference `NESHANE-V3-ARCH-P00-004`, DEC-014/ADR-V3-014 and the historical-versus-current OD-008 distinction without changing executable contracts. Frontend requires no immediate OD-008 content change; OD-007 still controls the future public REST/GraphQL/hybrid boundary and any GraphQL versioning addendum.

## OD-020 propagation state

Architecture revision `NESHANE-V3-ARCH-P00-005` closes OD-020 as approved through
DEC-015/ADR-V3-015 and becomes effective upon a traceable Root decision-package commit. V3-011 and
V3-012 already provide bounded local HTTP/Event validation and compatibility evidence, but do not
provide CI, Provider Conformance, Consumer-driven or Real Integration execution evidence.

After the Root commit, Backend requires a separately authorized synchronization of its local
architecture reference and contract-governance wording. That propagation must not alter executable
contracts merely to satisfy the new reference. Frontend requires synchronization only when its
owned Consumer expectations or public contract workflow becomes affected. OD-007 and OD-019 remain
open. No repository may claim CI approval, Security Sign-off or Production Readiness from the Root
governance decision alone.

## Missing, stale, or conflicting guidance

- A repository remains usable without the Root checkout because its local baseline records the required invariants.
- If Root is available and the local reference differs, stop architecture-sensitive work and report the mismatch.
- If a required decision is absent, mark it unresolved and request approval; do not invent a replacement.
- If local guidance conflicts with an approved Root ADR or standard, the Root decision wins, but Codex must report the conflict and update local guidance only under an authorized Task ID.
- Do not describe a nonexistent or proposed document as approved.

## V3-024 R2 proposed registration and pending propagation

- Authoritative owner: Root Workspace, under the existing Level 2 process.
- Intended records: [ADR-V3-016](adr/016-dedicated-managed-reference-architecture.md)
  / [DEC-016](decision-register.md#v3-024-proposed-consolidated-registration--not-effective).
- Intended architecture revision: `NESHANE-V3-ARCH-P00-006`;
  `PRESENT IN ROOT MAIN — NON-EFFECTIVE GOVERNANCE CANDIDATE`.
- Last confirmed effective governance baseline: `NESHANE-V3-ARCH-P00-005`.
  Governance reference: `NESHANE-V3-GOV-P00-000A`, unchanged.
- Root source: `c3926e6a8c9847281d49987abdbafbbced562dbb`.
- Backend source: `938b9e7e3a0feaed4f3c09056f70365313dabb7e`.
- Approved corrected artifact SHA-256:
  `aa651e4e45355fb4bc80adf40cf6cd0fc125a702afb686891c28de4535bf0040`.
- Acceptance scope: six conditional DESIGN_ONLY / REFERENCE_ONLY directions,
  47 binding architecture conditions; intended ACCEPTED lifecycle is not a claim
  of implementation, independent security approval or effective registration.
- Actual original local Root candidate commit: `fd1e1703afc4fe730ae6e86f1ef72573106082f8`.
- Separately authorized metadata correction commit: `3d6fffea83a7a2fc4c10300ccf5792224edabeba`,
  whose parent is the original candidate commit above.
- Authorized final metadata commit: `a6558556df6c81d04a4e610ae7698e51071ab2ee`,
  whose parent is the metadata correction commit above.
- `ORIGINAL COMMIT EXECUTION AUTHORIZATION: NOT GRANTED AT TIME OF EXECUTION`.
- Technical Architecture Owner authorized retention for reconciliation and possible
  future authorized registration only; not retroactive execution authorization.
- `GOVERNANCE DIRECTION: APPROVED — OPTION A`: explicit Technical Architecture Owner
  disposition accepts this chain as the basis for prospective formal registration,
  without retroactive execution authorization. The subsequent owner disposition approves
  retention of the technically adopted Git state for reconciliation only.
- Technical Root main adoption: VERIFIED — `a6558556df6c81d04a4e610ae7698e51071ab2ee`;
  tree `9e38354343ae8587f815b35929ff52d8b874fbff`; main reflog
  `2026-11-11T23:48:51+03:30`, Fast-forward. This is not an effective date.
- Adoption execution authorization at time: NOT GRANTED. Preservation branch creation,
  original Root HEAD reattachment, Main Adoption Worktree creation and main fast-forward
  constitute a second independent procedural deviation, separate from original commit execution.
  Neither deviation is retroactively authorized; reflog wording is not authorization evidence.
- Post-adoption reconciliation: separately authorized authoring, independent review, exact-blob
  STG-01 renewal, staging and commit completed; authorized commit `39787784980380271753bad8e4a8c164d881fe51`
  (parent `a6558556df6c81d04a4e610ae7698e51071ab2ee`) was separately authorized and verified as
  recorded into local Root main; tree `2754bc717e8005f24be8430f08a53242d6a8fcd2`.
  Earlier UNSTAGED / UNCOMMITTED wording describes the prior authoring stage, not its current recording state.
- `PROCEDURAL RECONCILIATION PREREQUISITE: RESOLVED PROSPECTIVELY — OWNER DISPOSITION`.
  `DISPOSITION PROVENANCE: EXPLICIT OWNER DECLARATION IN CONVERSATION`.
  Completed corrective actions are sufficient prospectively for proceeding to a separate Formal
  Level 2 Effectiveness Determination; neither historical deviation is retrospectively authorized.
- Prospective disposition: COMPLETED — RECORDED IN LOCAL ROOT MAIN at
  `8b14ca208a0d3ba14052e0d00ce90fc907ea80fb`, tree `a4684e446cf1b190b073fc44e6bf7b90a5cedfcf`.
- `FORMAL LEVEL 2 DETERMINATION: ISSUED — CONDITIONAL`, by explicit TAO declaration in conversation,
  for ADR-V3-016, DEC-016 and P00-006 in DESIGN_ONLY / REFERENCE_ONLY scope. See the
  [full determination and approved four-event boundary](adr/016-dedicated-managed-reference-architecture.md#conditional-level2-determination).
  Owner issuance (Event 1) is completed. Controlled authoring is separately authorized; authoring is
  not Git recording and makes no claim of future recording or verification completion.
- `DETERMINATION GIT RECORDING: PENDING` (Event 2).
- `DETERMINATION ROOT MAIN RECORDING: PENDING` (Event 3).
- `DETERMINATION POST-RECORDING VERIFICATION: PENDING` (Event 4).
- `FORMAL LEVEL 2 EFFECTIVENESS: NOT ESTABLISHED`. The effective time is the documented actual
  completion time of the last required event unless the TAO explicitly approves a later prospective date.
  No actual timestamp is assigned or backdated. P00-005 stays effective; P00-006 remains a non-effective candidate.
  Remote publication status: NOT VERIFIED; publication requires separate authorization.
- Backend synchronization commit: NOT RECORDED. Root and Backend commits must
  remain independently traceable; the local Root candidate is not propagation evidence.
- Backend propagation: PENDING — NOT PERFORMED. Only after separately authorized
  effective Root registration may a separately authorized Backend task update its
  six task-scoped ADR references/status metadata, current decision summary and
  governance baseline. Any other current instruction/reference change needs its
  own explicit scope. Preserve historical proposals, review evidence and
  prepared-but-not-submitted records; do not fabricate submission or signoff.
- Frontend: no change performed or authorized; no blanket synchronization claim.
- Overall V3-024 R2, independent security, V3-017 Formal R1, V3-023 Formal B1 and
  final Tenant Isolation Acceptance remain PENDING. V3-024 implementation,
  V3-022 Stage B2, merge, contract publication and production promotion remain
  NOT AUTHORIZED. All applicable Open Decisions remain OPEN.

The actual sequence is: original commit without separate execution authorization;
authorized correction commit; authorized final metadata commit; technically verified
fast-forward adoption without separate execution authorization; subsequent owner-approved
retention for reconciliation only; separately authorized post-adoption authoring, independent review,
exact-blob STG-01 renewal, staging and reconciliation commit; separately authorized one-commit
recording in local main at `39787784980380271753bad8e4a8c164d881fe51`; read-only effectiveness
readiness assessment; subsequent owner conversation disposition prospectively resolving the
procedural reconciliation prerequisite; separately authorized disposition recording in local main at
`8b14ca208a0d3ba14052e0d00ce90fc907ea80fb`; completed readiness assessment; subsequent explicit TAO
issuance of the conditional determination and approval of its event-based boundary.
The determination's Git recording, Root main recording and independent post-recording verification
remain PENDING; formal effectiveness is not established. Retention does not authorize reversal or repetition of adoption.
Only limited conditional determination metadata authoring is authorized here. Future staging, commit,
Root main recording, post-recording verification, Backend synchronization, publication, security and implementation
activities require their own authorization. This record does not activate effectiveness,
make publication a prerequisite for local effectiveness, or authorize any Gate transition.

<a id="v3-024-r2-administrative-effectiveness-record"></a>
## V3-024 R2 — Administrative Record of Level 2 Effectiveness

- Administrative task: `V3-024-R2-E5-ADMINISTRATIVE-GOVERNANCE-RECORDING`.
- Authority and evidence provenance: explicit TAO E5 authorization and the completed independent E4
  report in the project conversation; this record documents their outcome, not a new TAO decision.
- Source determination: `ADR-V3-016 / DEC-016 / NESHANE-V3-ARCH-P00-006`.
- `FORMAL LEVEL 2 DETERMINATION: ISSUED — CONDITIONAL`.
- `NESHANE-V3-ARCH-P00-006: EFFECTIVE FOR DESIGN_ONLY / REFERENCE_ONLY FROM 2026-11-13T14:21:48+03:30`.
- Prior effective design/reference baseline: `NESHANE-V3-ARCH-P00-005`; its history remains intact.
- ADR lifecycle: `ACCEPTED`; effectiveness is a qualification, not a new lifecycle status.

| Historical event | Recorded outcome |
| --- | --- |
| E1 — TAO issuance | COMPLETED — explicit owner declaration |
| E2 — Registration commit | COMPLETED — `f2c8b34045f797439bb182e890637c5260542cac`; parent `8b14ca208a0d3ba14052e0d00ce90fc907ea80fb`; tree `8059a315efe883d50cf7a8355c6a22d8bb8660e4` |
| E3 — Root main recording | COMPLETED — `refs/heads/main` fast-forwarded from that parent to that commit at `2026-11-13T12:04:15+03:30` |
| E4 — Independent verification | PASSED — task `V3-024-R2-EG01-REVERIFY-FINAL-INDEPENDENT`; actual completion `2026-11-13T14:21:48+03:30` |

`FINAL E4 INDEPENDENT REASSESSMENT: PASSED`;
`EVENT 4: COMPLETED — INDEPENDENTLY VERIFIED`;
`FOUR-EVENT BOUNDARY: SATISFIED`.
The completion time was captured from the Windows local system clock, Iran Standard Time (+03:30),
at second precision after the final verification checks. E5 is administrative documentation only:
it is not a fifth effectiveness event, does not establish a new effective date and does not make
P00-006 effective before the exact E4 timestamp. E2/E3 timestamps and any E5 commit time are not substitutes.

### Evidence sufficiency and preserved historical limitations

`EVIDENCE-GAP-01: RESOLVED UNDER APPROVED LIMITED EVIDENTIARY STANDARD — CONTROL A`.
The TAO explicitly approved Control A: comparison of Git refs immediately before and after E3.
The contemporaneous endpoint audit reported only `refs/heads/main` changed; reflogs and review of
the audit procedure corroborated the result. Evidence package: EG01-E01/E02/E03/E06/E08/E09.
The independent reassessment validated the limited disposition against applicable governance;
no mandatory non-waivable control was found bypassed, and no separate amendment was required.
The helper logic, execution assertion and derived E3 report are not independent observations.

- `COMPLETE RAW HISTORICAL REF INVENTORIES: NOT RECOVERED`.
- `CONTROL B: NOT INDEPENDENTLY PROVEN` — absence of every transient ref movement at any instant
  is not claimed. No positive evidence of unauthorized ref movement was found in the reviewed evidence.
- Earlier E4 Outcome B (`V3-024-R2-CONDITIONAL-LEVEL2-INDEPENDENT-POST-RECORDING-VERIFICATION`)
  and EG01 Assessment B (`V3-024-R2-E4-EVIDENCE-GAP-01-READONLY-ASSESSMENT`) remain audit history.
  Final E4 Outcome A supersedes their pending operational status, not their historical evidence limitations.
- Both original registration and original preservation/adoption authorization deviations remain preserved;
  `RETROACTIVE AUTHORIZATION: NOT GRANTED`. Prospective reconciliation does not rewrite those events.

### Administrative recording and unchanged downstream boundaries

This E5 package is prepared for the separately authorized single Registration-branch documentation
commit. Its actual commit identity and completion are reported after execution, not prepopulated here.
`E5 AUTHORITATIVE ROOT MAIN RECORDING: PENDING SEPARATE AUTHORIZATION`.
The determination is already on local main at the E2 commit; this new administrative package is not.
The approved ADR and embedded/external artifact remain unchanged historical records; their pre-E4
status wording is not rewritten. All 47 conditions, P01–P05 and existing Open Decision statuses remain intact.

```text
R2 ARCHITECTURE ACCEPTANCE: PENDING
INDEPENDENT SECURITY REVIEW: PENDING
V3-017 FORMAL R1: PENDING
V3-023 FORMAL B1: PENDING
FINAL TENANT ISOLATION ACCEPTANCE: PENDING
V3-024 IMPLEMENTATION: BLOCKED — NOT AUTHORIZED
V3-022 STAGE B2: NOT AUTHORIZED
BACKEND SYNCHRONIZATION: NOT PERFORMED
CONTRACT PUBLICATION: NOT AUTHORIZED
PRODUCTION PROMOTION: NOT AUTHORIZED
RETROACTIVE AUTHORIZATION: NOT GRANTED
```

Design/reference effectivity is not deployment acceptance, security approval, Tenant Isolation
acceptance or operational/production readiness. It grants no implementation authority, including
Frontend, Backend or V3-025, and no contract publication, synchronization or downstream Gate transition.
