# ADR-V3-016: Consolidated Dedicated Managed reference architecture

- Status: ACCEPTED
- Document reconciliation state: LOCAL COMMIT CANDIDATE RETAINED — FORMAL EFFECTIVENESS PENDING
- Status qualification: ACCEPTED is the authorized intended Root lifecycle, not an effective repository transition.
- Root main adoption: NOT PERFORMED; ADR-V3-016 is absent from the pinned effective Root main baseline.
- Authoring task: V3-024 / R2 — Controlled Root Architecture Decision Document Authoring
- Related decision: DEC-016
- Related Open Decisions: OD-009, OD-010, OD-011, OD-012, OD-013, OD-014, OD-015, OD-019, OD-022, OD-023; all remain OPEN.
- Decision owner / required architecture approval authority: project Technical Architecture Owner under V3-006.
- Approved architecture disposition: CONDITIONALLY ACCEPTED — DESIGN_ONLY / REFERENCE_ONLY.
- Approval provenance: explicit Technical Architecture Owner approval in the project conversation of the corrected P01–P05 disposition, six directions, 47 conditions, lifecycle mapping and consolidated Root record; the current task authorizes retention for reconciliation and unstaged metadata corrections only.
- Decision date: NOT RECORDED; no drafting date is substituted.
- Effective date: NOT RECORDED; a separately authorized formal-registration decision and verification remain required.
- Actual original local candidate commit: `fd1e1703afc4fe730ae6e86f1ef72573106082f8`; parent `c3926e6a8c9847281d49987abdbafbbced562dbb`.
- COMMIT_EXECUTION_AUTHORIZATION_AT_TIME_OF_COMMIT: NOT GRANTED
- Subsequent commit retention: AUTHORIZED FOR RECONCILIATION ONLY by the Technical Architecture Owner's explicit direction in the project conversation; not retroactive execution authorization.
- FORMAL LEVEL 2 REGISTRATION: NOT YET CONFIRMED AS EFFECTIVE
- Metadata reconciliation: AUTHORIZED — UNSTAGED / UNCOMMITTED; these corrections are not part of the retained commit.
- Whitespace exception: STG-01 covers only original ADR blob `46a46d5a75b0e5349015b0fb36bc5825a6c09ecc`; renewed blob-scoped approval is required before staging or committing this reconciliation.
- Prepared architecture revision: NESHANE-V3-ARCH-P00-006 — LOCAL CANDIDATE; NOT EFFECTIVE.
- Current effective Root main architecture revision: NESHANE-V3-ARCH-P00-005.
- Governance reference: NESHANE-V3-GOV-P00-000A — unchanged.
- Supersedes: None; this bounded refinement does not rewrite or supersede an existing accepted Root ADR.
- Superseded by: None
- Independent Security Review: PENDING
- Overall V3-024 R2 Architecture Acceptance Gate: PENDING
- V3-024 implementation: BLOCKED — NOT AUTHORIZED

## Registration boundary and source control

This is one consolidated Root ADR with six independently traceable sub-decisions.
The proposed ACCEPTED lifecycle and conditional approval disposition are separate.
Neither the locally committed candidate nor these unstaged metadata corrections establish
effective registration, close the overall R2 gate, authorize implementation or accept
security risk. Existing Backend task-scoped ADR statuses remain unchanged until
separately authorized synchronization after effective Root registration.

The Technical Architecture Owner authorized retention of the existing local commit
for governance reconciliation and possible future authorized registration only.
Original commit execution was not separately authorized; retention is not retroactive
authorization or effective Level 2 registration. Root main and Backend remain unchanged.

| Source / artifact | Exact identity |
| --- | --- |
| Root source commit | `c3926e6a8c9847281d49987abdbafbbced562dbb` |
| Backend source commit | `938b9e7e3a0feaed4f3c09056f70365313dabb7e` |
| Approved external artifact | `E:\Neshane-V3-024-R2-approved-artifacts\V3-024-R2-approved-formal-architecture-disposition.md` |
| Approved artifact SHA-256 | `aa651e4e45355fb4bc80adf40cf6cd0fc125a702afb686891c28de4535bf0040` |
| Approved artifact byte / line count | 25,778 UTF-8 bytes / 351 LF-terminated lines |
| Canonical representation | UTF-8 without BOM; LF; exactly one final LF; internal text/whitespace unchanged |
| Artifact source | Exact English section D of the corrected prior Codex response, approved by the Technical Architecture Owner; not the earlier uncorrected draft or a reconstructed proposal |
| Actual signature, external approval ID or submission | NOT RECORDED; none is invented or required here as a substitute for project authority |
| Backend synchronization commit | NOT RECORDED; propagation NOT PERFORMED |

The artifact body below is embedded verbatim. Its DRAFT labels, reserved fields,
proposed mapping alternatives and NOT RECORDED statements remain historical source
text. They describe that approved source artifact, not a newly fabricated submission
or registration. The intended mapping has subsequently been explicitly selected:
CONDITIONALLY ACCEPTED disposition maps to ACCEPTED lifecycle for bounded design.
This wrapper records the original authoring and subsequent reconciliation context
without editing the artifact. The actual local commit is recorded above; a procedurally
authorized formal registration is not established by its existence.

## Context, decision and independently traceable sub-decisions

One synthetic Tenant is assigned to one Dedicated Managed Cell. Shared reference
infrastructure does not erase service/data ownership, Tenant Context, Domain
authorization, applicable PostgreSQL RLS, workload trust or control-plane authority
boundaries. Real customer data and production operation are excluded.

Each row below is a stable sub-decision of ADR-V3-016 / DEC-016, not a newly allocated
global ADR or DEC. Its anchor, source ADR, option and numbered condition range remain
independently identifiable for future change control.

| Sub-decision / stable anchor | Owner-selected option | Approved disposition | Scope | Conditions | Exact condition range and pinned source |
| --- | --- | --- | --- | --- | --- |
| <a id="db-001"></a>DB-001 — Database isolation | A — Database per Service/Cell | CONDITIONALLY ACCEPTED | DESIGN_ONLY / REFERENCE_ONLY | 7 | Embedded §2.1, conditions 1–7; [source ADR](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/ADR-V3-024-R2-DB-001.md) |
| <a id="rt-002"></a>RT-002 — Disposable runtime | A — Disposable Docker Compose | CONDITIONALLY ACCEPTED | DESIGN_ONLY / REFERENCE_ONLY | 6 | Embedded §2.2, conditions 1–6; [source ADR](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/ADR-V3-024-R2-RT-002.md) |
| <a id="oa-003"></a>OA-003 — Scoped Controller and Agent | B — Scoped Operations Agent + Operations Controller | CONDITIONALLY ACCEPTED | DESIGN_ONLY / REFERENCE_ONLY | 8 | Embedded §2.3, conditions 1–8; [source ADR](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/ADR-V3-024-R2-OA-003.md) |
| <a id="cl-004"></a>CL-004 — Credential lifecycle | B — Scoped Credentials + Controlled Rotation | CONDITIONALLY ACCEPTED | DESIGN_ONLY / REFERENCE_ONLY | 8 | Embedded §2.4, conditions 1–8; [source ADR](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/ADR-V3-024-R2-CL-004.md) |
| <a id="rtr-005"></a>RTR-005 — Placement and routing trust | B — Validated Placement + Fail-Closed Routing | CONDITIONALLY ACCEPTED | DESIGN_ONLY / REFERENCE_ONLY | 8 | Embedded §2.5, conditions 1–8; [source ADR](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/ADR-V3-024-R2-RTR-005.md) |
| <a id="of-006"></a>OF-006 — Outage and freshness | B — Bounded Valid Local State | CONDITIONALLY ACCEPTED | DESIGN_ONLY / REFERENCE_ONLY | 10 | Embedded §2.6, conditions 1–10; [source ADR](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/ADR-V3-024-R2-OF-006.md) |

Total: **47 binding architecture conditions**. Binding means normative design
requirements if the registration becomes effective, not implemented or verified
controls. The corrected DB-001 condition binds each owning service within each Cell;
shared cluster administration does not permit shared cross-service runtime access.

The full condition wording, residual risks and per-ADR dependencies are preserved
in the embedded artifact. Source-specific detailed obligations remain binding,
including OA-003 §§5.1/6.1/7/9/11, CL-004 §§8–12, DB-001 §7.1, RTR-005 §§4–11,
OF-006 §§3–15 and Design Proposal §6/N18 and §§12–14.

## Alternatives and rationale

The six owner-selected directions and the rejected/deferred alternatives are recorded
in each pinned Backend ADR's §2 and §3. This registration does not reopen those choices:
database/service/Cell rather than shared service databases; reference Compose rather
than a production orchestrator; scoped Controller/Agent rather than unrestricted
infrastructure execution; controlled scoped credentials rather than an assumed
production provider; validated placement rather than caller/static routing authority;
bounded valid-state consideration rather than unrestricted offline continuation.

The rationale is bounded reference reproducibility with explicit authority and
ownership boundaries, without selecting production mechanisms prematurely.
Original alternatives remain historical evidence at the pinned source revision.

## Consequences, compatibility and consumer impact

No executable API, Event, JSON Schema, manifest, database schema, runtime configuration
or service is changed or published by this document. Existing contracts and accepted
ADRs remain intact. Future implementation or contract changes must follow the
[Contract Change Protocol](../contract-change-protocol.md) and ADR-V3-014/015;
design acceptance supplies no Provider Conformance, CI or runtime evidence.

Shared PostgreSQL administration/failure domains, shared Docker host/daemon,
unverified workload identity, secret custody, durable execution, adapter privileges,
placement distribution, revocation exposure and production recovery remain residual
risks. Conditional design approval is not independent acceptance of those risks.

OD-009/010/011/012/013/014/015/019/022/023 remain OPEN under their authoritative
definitions in the [Open Decision Register](../open-decisions.md). OD-019 remains
Background scheduling; OD-023 remains SLO/RTO/RPO/capacity objectives and measurement.
No numeric TTL, clock/restart policy, production topology/product or outage permission
is selected by the proposed registration.

## Verification expectations, recovery and change control

V3-024 runtime/security verification remains NOT EXECUTED. Future authorized work
requires real positive controls, negative tests and effect observations for identity,
command authorization, replay/concurrency/crashes, restricted adapters, PostgreSQL
roles/read-write RLS/pools, credential revocation, destination trust, atomic generation
fencing and outage recovery. Deterministic fixtures and document checks are not
real persistence, workload authentication or Tenant data-isolation evidence.

Recovery must preserve authoritative generations, activation/revocation state,
credential scope and Domain-owned evidence. No blind replay, revoked-credential
restoration, automatic reconciliation winner, migration or executable DURABLE_DEFER
is authorized. Future schema recovery uses owned forward-fix/reviewed restoration,
not unsafe automatic downgrade. No rollback or runtime procedure is executed here.

For the current unstaged metadata reconciliation, corrections remain reviewable within the authorized
allowlist; do not erase unrelated user work. After effective registration, an
editorial correction must remain traceable; a material change to a sub-decision
requires the existing Root ADR revision/supersession process, identifying the exact
ADR-V3-016 sub-decision and affected condition numbers. Preserve the accepted history,
consumer impact, compatibility and recovery obligations; do not silently replace
one sub-decision through a mutable source link.

## Governance restrictions and propagation

- `GOVERNANCE METADATA RECONCILIATION: AUTHORIZED — UNSTAGED / UNCOMMITTED`
- `FORMAL DECISION REGISTRATION: NOT EFFECTIVE`
- `R2 ARCHITECTURE ACCEPTANCE: PENDING`
- `INDEPENDENT SECURITY REVIEW: PENDING`
- `V3-024 IMPLEMENTATION: BLOCKED — NOT AUTHORIZED`
- `V3-022 STAGE B2: NOT AUTHORIZED`
- `V3-017 FORMAL R1: PENDING`
- `V3-023 FORMAL B1: PENDING`
- `FINAL TENANT ISOLATION ACCEPTANCE: PENDING`
- `MERGE: NOT AUTHORIZED`
- `CONTRACT PUBLICATION: NOT AUTHORIZED`
- `PRODUCTION PROMOTION: NOT AUTHORIZED`

Separate authorization is required for staging/committing these metadata corrections,
confirming formal registration, Backend synchronization, merge/publication and any
implementation. Retention does not authorize those actions. Root and Backend commits
will be independently traceable; no cross-repository atomicity is claimed.
No Frontend synchronization is performed. Required later propagation is documented
in [Governance Synchronization](../governance-synchronization.md#v3-024-r2-proposed-registration-and-pending-propagation).

Applicable rules remain [Root task governance](../task-governance.md#level-2--architecture-decision),
[ADR lifecycle](README.md), ADR-V3-003/005/007/010/011/012 and ADR-V3-014/015.
No general governance rule is amended by this bounded authoring.

## Approved disposition artifact — verbatim

The markers delimit only the approved text. Extract bytes immediately after the
opening marker's LF and before the closing marker; the extracted text must have
exactly one final LF and the approved SHA-256. Do not include markers or this wrapper.

<!-- BEGIN APPROVED V3-024 R2 DISPOSITION -->
# V3-024 R2 — Draft Formal Architecture Disposition

**Document status:** DRAFT — FOR AUTHORITY REVIEW  
**Decision record status:** NOT RECORDED  
**Project:** Neshane V3 — Dedicated Managed  
**Review scope:** DESIGN_ONLY / REFERENCE_ONLY  
**Reviewed repository:** IKAC-FIDS/Neshane-CRM-V3-Back  
**Proposed reviewed repository revision:** `938b9e7e3a0feaed4f3c09056f70365313dabb7e`  
**Decision authority:** Project Technical Architecture Owner — project designation recorded under V3-006; explicit final disposition and attribution for this draft remain NOT RECORDED  
**Decision date:** NOT RECORDED  
**Independent Security Review:** PENDING  

The proposed repository revision identifies the source package. This corrected draft is supplied in the project conversation and is not contained in that commit. Any subsequent formal decision must identify both the source baseline and the exact corrected draft artifact or version actually approved.

## 1. Subject of the Decision

This document presents the proposed formal architecture disposition for the six task-scoped Architecture Decision Records associated with V3-024 R2.

The review concerns the Dedicated Managed reference architecture, consisting of one synthetic Tenant assigned to one Dedicated Cell, with explicit separation of service ownership, data boundaries, operational management, credentials, routing, and behavior during Control Plane outages.

According to the recorded advisory design re-review, findings F01 through F07 have been resolved at the design-documentation level. The re-review recommended readiness for formal architecture review.

Resolution of these findings does not constitute implementation of the proposed controls, verification of Tenant Isolation, independent security acceptance, or acceptance of residual security risk.

This draft does not issue a formal disposition. All proposed decisions remain subject to explicit final authority action and controlled registration.

Source references:

- [Design Proposal](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-design-proposal.md), §§1, 3, 12–18.
- [Design Re-review Report](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-design-re-review-report.md), §§2–10.
- [Architecture Decision Summary](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-architecture-decision-summary.md), §§3–11.
- [Formal Review Submission Package](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-formal-review-submission-package.md), §§A–J.

## 2. Proposed Architecture Dispositions

It is proposed that the following six ADRs be independently dispositioned as `CONDITIONALLY ACCEPTED`, strictly within Reference Architecture Design scope.

Conditional acceptance would signify approval of the bounded architectural direction and retention of its design requirements. It would not establish that implementation conditions have been satisfied or that residual security risks have been independently accepted.

No disposition below is an actual recorded decision.

| ADR | Owner-selected option | Proposed disposition | Conditions |
|---|---|---|---:|
| DB-001 | A — Database per Service/Cell | CONDITIONALLY ACCEPTED | 7 |
| RT-002 | A — Disposable Docker Compose | CONDITIONALLY ACCEPTED | 6 |
| OA-003 | B — Scoped Operations Agent + Operations Controller | CONDITIONALLY ACCEPTED | 8 |
| CL-004 | B — Scoped Credentials + Controlled Rotation | CONDITIONALLY ACCEPTED | 8 |
| RTR-005 | B — Validated Placement + Fail-Closed Routing | CONDITIONALLY ACCEPTED | 8 |
| OF-006 | B — Bounded Valid Local State | CONDITIONALLY ACCEPTED | 10 |

### 2.1. DB-001 — Database Isolation

**Option A — Database per Service/Cell**

**Proposed disposition:** CONDITIONALLY ACCEPTED

**Conditions:**

1. Maintain a separate database and separate runtime credentials for each owning service within each Cell. A shared PostgreSQL cluster does not permit shared cross-service databases or runtime privileges.
2. Preserve separation between Runtime and Migration roles and enforce least-privilege permissions.
3. Prohibit administrative access, privilege escalation, and RLS bypass by Runtime roles.
4. Require validated Tenant Context and applicable RLS controls for both read and write operations.
5. Preserve credential isolation and prohibit Operations Agent access to database secrets.
6. Require real PostgreSQL, role, RLS, Connection Pool, and cross-service/Cell unauthorized-access verification before Runtime Isolation acceptance.
7. Keep OD-012, OD-013, and OD-014 open until independently dispositioned. Do not select the production database topology at this stage.

**Residual risks:** Shared PostgreSQL cluster administration and failure domains, unverified runtime Tenant Isolation, and unresolved production Physical Isolation.

**Source requirements:** [DB-001](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/ADR-V3-024-R2-DB-001.md), §§3–7.1 and 8–9; [Consolidated Proposed Disposition](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §4.1. Condition 1 above clarifies the conjunctive service-within-Cell boundary; it does not broaden the selected option.

### 2.2. RT-002 — Runtime Topology

**Option A — Disposable Docker Compose**

**Proposed disposition:** CONDITIONALLY ACCEPTED

**Conditions:**

1. Restrict the Reference Environment to one synthetic Tenant and one Dedicated Cell.
2. Preserve separation of service Containers, Configuration, Runtime Identities, and network boundaries.
3. Prohibit Privileged Containers, unrestricted Docker Socket access, and unrestricted Host administration.
4. Enforce Controller and Agent authority restrictions in accordance with OA-003.
5. Preserve database and credential isolation in accordance with DB-001 and CL-004.
6. Require separately authorized verification of Network Isolation, Readiness, Service Lifecycle, Recovery, and cleanup limited to owned resources.

**Residual risks:** Shared Host and Docker Daemon, limited host-level isolation, unverified real Workload Identity, and unresolved OD-015.

A complete management-path reference smoke test requires both Controller and Agent. An Agent-only test using a Controller test double remains a component test and cannot independently satisfy the complete management-path criterion.

**Source requirements:** [RT-002](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/ADR-V3-024-R2-RT-002.md), §§3–11; [Design Proposal](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-design-proposal.md), §14; [Consolidated Proposed Disposition](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §4.2.

### 2.3. OA-003 — Operations Agent and Controller

**Option B — Scoped Operations Agent + Operations Controller**

**Proposed disposition:** CONDITIONALLY ACCEPTED

**Conditions:**

1. Maintain independent Controller and Agent identities and separate Authorization and Execution responsibilities.
2. Validate authorization at request admission and immediately before consequential execution.
3. Bind authorization to the exact Operation, Parameters, Target, Deployment/Cell, Resource Version, and immutable Digest.
4. Enforce Allowlisting scoped to operation type, resource, and configuration.
5. Prohibit arbitrary Shell execution, unrestricted Docker Socket access, broad Host administrative privileges, and access to database secrets or Tenant business data.
6. Enforce Replay, Concurrency, Conflict, and Crash Recovery safeguards.
7. Enforce Fail-Closed behavior for invalid, expired, revoked, superseded, or unverifiable authority.
8. Require separately authorized real verification of Identity, Trust, Execution, Adapter Isolation, and Recovery.

**Residual risks:** Unresolved Command Protocol, Workload Identity, Durable Replay, Adapter privilege boundaries, and production Orchestration.

OD-011, OD-012, OD-015, and OD-019 remain OPEN.

**Source requirements:** [OA-003](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/ADR-V3-024-R2-OA-003.md), §§4–11, especially §§5.1, 6.1, 7 and 9; [Consolidated Proposed Disposition](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §4.3.

### 2.4. CL-004 — Credential Lifecycle

**Option B — Scoped Credentials + Controlled Rotation**

**Proposed disposition:** CONDITIONALLY ACCEPTED

**Conditions:**

1. Maintain independent least-privilege credentials for each owning service, Cell, and database.
2. Preserve Runtime and Migration separation and prohibit administrative privilege escalation.
3. Prevent unauthorized storage or disclosure of Secret Material.
4. Distinguish routine Rotation from emergency revocation, and prevent new connections using old credentials before completing cleanup of existing sessions.
5. Define independent Emergency Revocation that does not wait for replacement credentials to become available.
6. Address active database sessions, Transactions, and Connection Pools.
7. Prohibit reporting success after failed or uncertain lifecycle phases, and prevent restoration of revoked credentials through Rollback or Backup.
8. Require separately authorized real database and Credential Lifecycle verification before Runtime acceptance.

**Residual risks:** Unresolved Secret Custody, Delivery, enforcement of Revocation, session termination, and secure recovery.

OD-009, OD-011, OD-012, OD-013, OD-014, and OD-015 remain OPEN.

**Source requirements:** [CL-004](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/ADR-V3-024-R2-CL-004.md), §§4–14, especially §§8.1–8.3 and 12; [Consolidated Proposed Disposition](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §4.4.

### 2.5. RTR-005 — Validated Placement and Fail-Closed Routing

**Option B — Validated Placement + Fail-Closed Routing**

**Proposed disposition:** CONDITIONALLY ACCEPTED

**Conditions:**

1. Derive Tenant Context from an approved authentication boundary.
2. Validate Authoritative Placement, Cell assignment, Deployment identity, Lifecycle State, and Generation.
3. Reject stale, expired, conflicting, or unauthorized Placement evidence.
4. Verify Cell Eligibility, Activation, Suspension, and Deployment Profile.
5. Authenticate the destination independently of network reachability.
6. Enforce Fail-Closed Routing with Zero Unauthorized Forwarding and no fallback to an unrelated Cell.
7. Preserve separation of Placement, Trust, Gateway, and Operations authorities.
8. Require separately authorized positive and negative verification of Routing, Trust, and Forwarding.

**Residual risks:** Unresolved real Tenant Identity, authoritative Placement distribution, Destination Trust, Freshness, Revocation, and production routing guarantees.

OD-009, OD-011, OD-012, OD-015, and OD-023 remain OPEN.

No general Offline Routing authorization is established.

**Source requirements:** [RTR-005](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/ADR-V3-024-R2-RTR-005.md), §§3–13; [Design Proposal](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-design-proposal.md), §6 and N18; [Consolidated Proposed Disposition](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §4.5.

### 2.6. OF-006 — Outage Behavior

**Option B — Bounded Valid Local State**

**Proposed disposition:** CONDITIONALLY ACCEPTED

**Conditions:**

1. Require validated Tenant Context.
2. Use only Placement Evidence previously validated by an authoritative source.
3. Preserve the authenticity and integrity of retained Local State.
4. Reject known superseded or conflicting Generations.
5. Enforce approved Freshness limits without automatically extending validity during outages.
6. Honor known Suspension and Revocation states.
7. Validate the target Cell and Deployment identities.
8. Maintain applicable Destination Trust requirements.
9. Consider continuation only for operations that were previously authorized.
10. Require a separately approved, operation-specific continuation Policy.

For condition 2, prior validation must establish the applicable Placement Authority, record provenance and semantic scope. A signature, issuer assertion or cache entry alone does not establish that authority.

**Residual risks:** Undefined numerical TTL, Clock/Restart Semantics, exposure window for unobserved Revocation, distribution mechanisms, operation-specific continuation policies, and production Recovery guarantees.

OD-023 and applicable dependencies OD-009, OD-011, OD-012, OD-015, and OD-019 remain OPEN.

This proposed disposition does not authorize actual Offline Continuation.

**Source requirements:** [OF-006](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/ADR-V3-024-R2-OF-006.md), §§3–16; [Consolidated Proposed Disposition](E:/Neshane-CRM-V3/Backend/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §4.6.

## 3. Cross-ADR Decision Conditions

The 47 conditions incorporate the detailed requirements of the six source ADRs and the consolidated proposed disposition at commit `938b9e7e3a0feaed4f3c09056f70365313dabb7e`. Their summaries do not replace or relax those requirements. No implementation or security-verification condition is recorded as satisfied by this design disposition.

If this disposition is formally approved, the following requirements must be preserved:

- All 47 conditions across the six ADRs shall be recorded as accepted architectural conditions. Their operational fulfillment remains subject to evidence.
- Tenant, Service, Cell, Domain, Registry, Lifecycle, Placement, Trust, Operations and Recovery authority boundaries shall remain unchanged.
- Selection of the Reference Architecture does not automatically authorize technology or topology decisions for Production.
- Any material modification to accepted conditions shall be subject to Change Control and renewed review by the competent authority.
- All unresolved Open Decisions shall remain OPEN until independently dispositioned.
- Synthetic or Design-Level evidence shall not substitute for real Security, Runtime, or Tenant Isolation verification.
- Subsequent implementation increments shall require an explicitly defined Scope, satisfied prerequisites, and separate authorization.

The following detailed source obligations are expressly retained:

- Independent Controller admission and Agent verification immediately before consequential execution, including expiry, revocation, supersession and applicable authority versions.
- Binding of commands and approvals to exact operations, parameters, target identities, deployment/Cell, expected resource versions and immutable configuration or artifact digests.
- Serialization, linearization or equivalent concurrency guarantees between validation and effect; conflict handling, immutable command-ID semantics, replay prevention and durable crash-recovery requirements. Uncertain outcomes do not authorize blind replay.
- Capability-restricted adapters, independently enforced resource/key allowlists and rejection before prohibited side effects. Non-secret configuration remains potentially security-sensitive.
- Separate routine credential rotation and emergency compromise revocation; emergency containment does not wait for replacement readiness.
- Existing database sessions, active transactions and connection pools, continuous reconnect attempts, partial failures and lifecycle-phase crashes. Failed or unknown phases are not successful revocation.
- Real PostgreSQL ownership, direct/inherited grants, role membership, SET ROLE escalation, PUBLIC/default privileges, ordinary non-bypass role controls, read/write RLS and pooled Tenant Context verification.
- Generation fencing and atomic or equivalently serialized mutation/effect boundaries, including an older validated mutation attempting to commit after an effective fence advances.
- Fail-closed routing, independently validated destination identity and zero unauthorized forwarding, without unrelated-Cell fallback.
- Approved outage freshness, no local expiry extension, known revocation/suspension precedence, generation anti-rollback and recovery reconciliation.

F01–F07 remain findings resolved at design level only. Their resolution does not record any runtime test, security verification or independently accepted residual risk.

Source references: OA-003 §§5.1, 6.1, 7, 9 and 11; CL-004 §§8–12; DB-001 §7.1; RTR-005 §§4–11; OF-006 §§3–15; Design Proposal §§6–9, 12–14.

## 4. Explicit Exclusions from Acceptance

If approved, this disposition shall **not** authorize:

- Implementation of Gateway, Controller, Agent, or Runtime components.
- Service Provisioning or Deployment.
- Database Migrations or modifications to database roles.
- Operational issuance, distribution, Rotation, or Revocation of credentials.
- Activation of Offline Routing or Offline Management.
- Contract Publication or activation of V3-022 Stage B2.
- Production database topology, orchestration, identity or secret-provider selection.
- Merge, Production Promotion, or final Tenant Isolation Acceptance.
- Independent Security Sign-off, security-critical exceptions or risk acceptance.
- Executable DURABLE_DEFER or automatic restoration.

Acceptance of the architectural design shall not constitute independent acceptance of residual Security, Availability, Data Isolation, or Operational Recovery risks.

## 5. Requirements Before the Implementation Stage

Before requesting implementation authorization, the following activities shall be completed as applicable to the proposed execution scope:

- Disposition the Open Decisions that materially affect the implementation scope.
- Identify the authorized implementation boundary, including permitted components and files.
- Assess the impact of V3-016, V3-017, V3-022, and V3-023 dependencies.
- Establish a real verification plan containing positive controls, negative tests, and observable effect evidence.
- Identify and satisfy applicable Independent Security Review requirements and authority boundaries.
- Obtain a separate, traceable implementation authorization.

OD-010 and OD-022 remain OPEN as broader session and migration dependencies. OD-023 retains its authoritative scope of SLO/RTO/RPO/capacity objectives and measurement; operation-specific freshness, clock and revocation-exposure policies require separate explicit dispositions.

The authoritative [Open Decision Register](E:/Neshane-CRM-V3/architecture/open-decisions.md), decision table, retains:

| ID | Authoritative subject | Current state |
|---|---|---|
| OD-009 | IdP integrations | OPEN |
| OD-010 | Session lifecycle/revocation | OPEN |
| OD-011 | Workload identity | OPEN |
| OD-012 | Secrets/keys | OPEN |
| OD-013 | PostgreSQL migrations | OPEN |
| OD-014 | Java/RLS integration | OPEN |
| OD-015 | Runtime orchestration | OPEN |
| OD-019 | Background scheduling | OPEN |
| OD-022 | Tenant migration automation | OPEN |
| OD-023 | SLO/RTO/RPO/capacity objectives and measurement | OPEN |

ADR-specific dependencies and broader project dependencies are distinct. Their inclusion here neither changes their scope nor resolves them.

The following dependency restrictions remain:

- [V3-016 engineering evidence](E:/Neshane-CRM-V3/Backend/ci/V3-016-engineering-evidence.md), status and Governance Phase A review: engineering acceptance does not establish final R1 or effective hosted governance enforcement.
- [V3-017 engineering evidence](E:/Neshane-CRM-V3/Backend/services/reference-peer-service/V3-017-engineering-evidence.md), R1 decision: Formal R1 acceptance remains PENDING. V3-024 reuse requires its own applicable dependency disposition.
- [V3-022 R2 acceptance](E:/Neshane-CRM-V3/Backend/contracts/routing/V3-022-R2-acceptance.md), §§3–6: limited design acceptance does not authorize real cryptography, durable activation, transactional fencing or Stage B2.
- [V3-023 B1 handoff](E:/Neshane-CRM-V3/Backend/deployment/shared/V3-023-B1-review-handoff.md), §2: Formal B1, final Tenant Isolation and Independent Security Sign-off remain PENDING. Shared reference evidence is not Dedicated Managed acceptance.

## 6. Decision and Governance Status

**Proposed ADR-level disposition:** CONDITIONALLY ACCEPTED — DESIGN ONLY

**Actual decision record:** NOT RECORDED — DRAFT

CONDITIONALLY ACCEPTED describes the proposed approval disposition, not a new ADR lifecycle state. Before formal registration, the authorized authority must explicitly determine its mapping to the existing Root ADR lifecycle and registration process. No local status edit alone makes these decisions effective. The overall V3-024 R2 gate remains PENDING unless separately and explicitly dispositioned; implementation and security gates remain unchanged.

The authoritative Root ADR lifecycle permits only:

`PROPOSED`, `ACCEPTED`, `REJECTED`, `DEPRECATED`, `SUPERSEDED`.

The source task-scoped ADRs remain `PROPOSED — R2 REVIEW PENDING`. This draft changes none of them.

For subsequent authority consideration, without selecting either alternative here:

- If the authority explicitly approves the bounded architecture now, it may explicitly authorize mapping the conditional disposition to lifecycle `ACCEPTED`, with the conditions, limitations, effective boundary and unmet implementation/security evidence recorded separately through the existing Root process.
- If unresolved conditions prevent architecture approval itself, the ADRs remain `PROPOSED`; an attributable conditional review position may be recorded without claiming effective architecture acceptance.

The authority must determine the applicable alternative, the controlled registration treatment of the six task-scoped records, and the relationship to the overall R2 gate. No new canonical ADR or DEC identifier is allocated by this draft.

Formal effectiveness requires the relevant Root ADR/catalog/decision-register and applicable baseline or Open Decision updates, validation and traceable Level 2 commit. Required Backend reference updates follow the controlled synchronization process separately; no cross-repository atomicity is implied.

Authoritative references:

- [Root ADR Catalog](E:/Neshane-CRM-V3/architecture/adr/README.md), Status vocabulary, Lifecycle and revision rules, Required ADR fields.
- [Root Task Governance](E:/Neshane-CRM-V3/architecture/task-governance.md), Level 2 designation/workflow and Level 3/4 boundaries.
- [Governance Synchronization](E:/Neshane-CRM-V3/architecture/governance-synchronization.md), Ownership and Propagation process.

Current gates remain:

```text
FORMAL DECISION: NOT RECORDED
R2 ARCHITECTURE ACCEPTANCE: PENDING
INDEPENDENT SECURITY REVIEW: PENDING
V3-024 IMPLEMENTATION: BLOCKED — NOT AUTHORIZED
V3-017 FORMAL R1: PENDING
V3-023 FORMAL B1: PENDING
V3-022 STAGE B2: NOT AUTHORIZED
FINAL TENANT ISOLATION ACCEPTANCE: PENDING
FORMAL DISPOSITION REQUEST: PREPARED — NOT SUBMITTED
FORMAL REVIEW SUBMISSION PACKAGE: PREPARED — NOT SUBMITTED
MERGE / CONTRACT PUBLICATION / PRODUCTION PROMOTION: NOT AUTHORIZED
```

Changing the overall R2 Architecture Acceptance gate requires verification of its applicable conditions and an explicit authority decision concerning that gate. No independent review or approval is claimed by this draft.

## 7. Decision Attribution and Registration — Reserved

The project Technical Architecture Owner designation is recorded in Root task-governance.md under V3-006. This draft does not itself evidence a final decision by that role holder. Formal registration requires an explicit disposition attributable to that role holder against the exact reviewed revision, followed by the required repository records and traceable Level 2 commit. No corporate credential or independent security approval is inferred.

The established project role, the requester's declared exercise of that role, the exact artifact reviewed, an explicit final decision, its attributable evidence and its effective repository registration are distinct matters. Independent Security Review remains a separate decision and evidence gate.

| Field | Status |
|---|---|
| Established project authority basis | Root task-governance.md / V3-006 project designation |
| Requester's exercise of that role | Declared in the project conversation; not itself a final disposition |
| Actual final decision attribution | NOT RECORDED |
| Decision date | NOT RECORDED |
| Proposed source repository revision | `938b9e7e3a0feaed4f3c09056f70365313dabb7e` |
| Exact corrected draft artifact/version approved | NOT RECORDED |
| Final per-ADR decisions and rationale | NOT RECORDED |
| Final conditions and responsible owners | NOT RECORDED |
| Conditional-disposition lifecycle mapping | PENDING EXPLICIT AUTHORITY DECISION |
| Overall R2 gate disposition | PENDING |
| Attributable final decision evidence | NOT RECORDED |
| Decision reference / signature, if applicable | NOT RECORDED |
| Independent security signoff | PENDING |
| Formal review submission evidence | NOT RECORDED |
| Effective registration / commit references | NOT RECORDED |
| Repository governance update | NOT PERFORMED |

This document is draft decision text. It shall not be treated as an authoritative Formal Decision Record until explicit final approval, valid project-level attribution and controlled registration have been completed.

No additional corporate credential or external signature is required by this draft beyond the applicable documented governance. No reviewer identity, decision date, signature, approval reference or registration evidence is fabricated.
<!-- END APPROVED V3-024 R2 DISPOSITION -->

## Additional pinned package references

These remote-form links identify immutable source revisions checked against the local
Backend repository. Remote reachability was not tested and is not approval evidence.
The embedded artifact's absolute workspace links remain verbatim historical source
text; they require the separate original Root/Backend workspace and are not assumed
to exist inside this isolated Worktree or a standalone clone.

- [Design Proposal](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-design-proposal.md), §§1, 3, 6–9, 12–18.
- [Decision Summary](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-architecture-decision-summary.md), §§3–11.
- [Consolidated Proposed Disposition](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-consolidated-proposed-disposition.md), §§4.1–4.6.
- [Design Re-review Report](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-design-re-review-report.md), §§4–10: F01–F07 resolved at design level only.
- [Formal Disposition Request](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-formal-disposition-request.md): prepared, not submitted.
- [Formal Review Submission Package](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-formal-review-submission-package.md): prepared, not submitted.
- [Independent Review Handoff](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/dedicated-managed/V3-024-R2-independent-review-handoff.md): no independent signoff.
- [V3-016 governance evidence](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/ci/V3-016-engineering-evidence.md): Phase A engineering accepted; R1/hosted governance enforcement pending.
- [V3-017 engineering/R1 record](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/services/reference-peer-service/V3-017-engineering-evidence.md): formal R1 pending.
- [V3-022 limited acceptance](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/contracts/routing/V3-022-R2-acceptance.md), §§3–6: Stage B2 not authorized.
- [V3-023 B1 handoff](https://github.com/IKAC-FIDS/Neshane-CRM-V3-Back/blob/938b9e7e3a0feaed4f3c09056f70365313dabb7e/deployment/shared/V3-023-B1-review-handoff.md): formal B1/final isolation/independent security pending.
