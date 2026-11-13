# Neshane V3 decision register

E5 administrative qualification (`V3-024-R2-E5-ADMINISTRATIVE-GOVERNANCE-RECORDING`):
DEC-016 / ADR-V3-016 / P00-006 are effective in `DESIGN_ONLY / REFERENCE_ONLY` scope from
`2026-11-13T14:21:48+03:30`, following final independent E4 Outcome A and satisfaction of E1–E4.
See the [administrative effectiveness record](governance-synchronization.md#v3-024-r2-administrative-effectiveness-record)
for Control A sufficiency, unrecovered raw inventories, unproven Control B and unchanged restrictions.
Earlier non-effective/PENDING wording below is retained pre-E4 history. The ADR lifecycle remains
`ACCEPTED`; P00-005 history is preserved. E5 is not a new effectiveness decision or implementation authorization.

Architecture version: `NESHANE-V3-ARCH-P00-005` upon traceable commit of the OD-020 decision package. DEC-001 through DEC-012 were accepted through project-owner approval recorded in Task R0-001 on 2026-10-23; DEC-013 was accepted by the Technical Architecture Owner under the V3-006 Level 2 protocol on 2026-10-30; DEC-014 was explicitly approved by the CPO/Technical Architecture Owner through the OD-008 formal-closure task; DEC-015 is accepted by the Technical Architecture Owner and scoped interim Quality Authority through the OD-020 finalization task. Acceptance is architectural authority, not evidence of implementation or production readiness.

Approval provenance: the project owner supplied the explicit R0 decisions recorded in R0-001; Codex converted them into DEC/ADR documentation under R0-001. The Technical Architecture Owner/CPO explicitly supplied the V3-005 OD-002 through OD-004 selections recorded as DEC-013/ADR-V3-013, the OD-008 API/event versioning selection recorded as DEC-014/ADR-V3-014 and the complete OD-020 disposition recorded as DEC-015/ADR-V3-015. DEC-015 includes a separate scoped interim Quality Authority review with the same role holder and disclosed dual capacity. No independent Security, organizational Quality, Operations or Developer Experience approval is claimed.

V3-024 proposed registration: DEC-016 is technically present in Root main through
the chain `fd1e1703afc4fe730ae6e86f1ef72573106082f8`, separately authorized metadata
correction `3d6fffea83a7a2fc4c10300ccf5792224edabeba` and authorized final metadata
commit `a6558556df6c81d04a4e610ae7698e51071ab2ee`; formal effectiveness is NOT ESTABLISHED.
The original commit execution lacked separate authorization. The main adoption operations
also lacked separate authorization at execution: a second, independent procedural deviation.
Main's reflog records `2026-11-11T23:48:51+03:30`, Fast-forward to `a6558556df6c81d04a4e610ae7698e51071ab2ee`.
The Technical Architecture Owner approved the corrected P01–P05 artifact, six reference
directions, 47 conditions and intended ACCEPTED lifecycle mapping.
`GOVERNANCE DIRECTION: APPROVED — OPTION A`; subsequent owner-approved retention of
the adopted Git state is for reconciliation only, not retroactive authorization.
P00-005 remains the last confirmed effective governance baseline; P00-006 is a
non-effective candidate technically present in main. Separately authorized post-adoption
authoring, independent review, exact-blob STG-01 renewal, staging and reconciliation commit
were completed and separately recorded into local Root main at `39787784980380271753bad8e4a8c164d881fe51`.
Earlier unstaged/uncommitted wording describes that historical authoring stage.
The Technical Architecture Owner's subsequent explicit conversation disposition resolves the
procedural reconciliation prerequisite prospectively; neither historical deviation is retrospectively authorized.
The prospective disposition is recorded in local Root main at
`8b14ca208a0d3ba14052e0d00ce90fc907ea80fb`, tree `a4684e446cf1b190b073fc44e6bf7b90a5cedfcf`.
`FORMAL LEVEL 2 DETERMINATION: ISSUED — CONDITIONAL` covers ADR-V3-016, DEC-016 and P00-006
in DESIGN_ONLY / REFERENCE_ONLY scope; its authority is the explicit TAO declaration in conversation.
The [issued determination and owner-approved four-event boundary](adr/016-dedicated-managed-reference-architecture.md#conditional-level2-determination)
complete only owner issuance (Event 1). Determination Git recording, local Root main recording and
independent post-recording verification (Events 2–4) remain PENDING; formal Level 2 effectiveness
is NOT ESTABLISHED. The effective time is actual documented completion of the last required event,
unless the TAO explicitly approves a later prospective date. No actual timestamp, signature,
submission, independent security approval or authorization for future Git operations is implied.

| ID | Title | Decision | Rationale | Consequences | Dependencies | Related ADRs | Approval provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-001 | Backend architecture | Java/Spring Boot independent microservices with DDD/Hexagonal structure and independent build, test, version, artifact and deployment; one service release cannot require rebuilding other Business Services. | Preserve business autonomy and replaceable infrastructure. | More contract/operational boundaries; foundation versions/build are refined by DEC-013 without changing service independence. | DEC-013 | [ADR-V3-001](adr/001-backend-architecture.md) | V3-001 §4.1 refined and owner-approved by R0-001 decision 1, 2026-10-23 |
| DEC-002 | Capability and data ownership | Strict service ownership of domain, persistence and migrations; contract integration; no cross-service SQL, shared ORM entities or implementation dependencies. | Prevent distributed-monolith and shared-schema coupling. | Consistency uses versioned APIs/events/projections. | DEC-007, DEC-014; OD-007 | [ADR-V3-002](adr/002-service-ownership.md) | V3-001 §4.1/§4.6 refined and owner-approved by R0-001 decision 2, 2026-10-23 |
| DEC-003 | Cell-based hybrid tenancy | Shared SaaS, Dedicated Managed and Dedicated Sovereign are required for first production release; tenant identity is placement-independent. | Meet shared, dedicated and sovereignty needs with compatible semantics. | Routing, Placement Generation, lifecycle/migration become explicit responsibilities. | OD-001, OD-022–OD-023 | [ADR-V3-003](adr/003-cell-based-hybrid-tenancy.md) | V3-001 §4.2 owner-approved by R0-001 decision 3, 2026-10-23 |
| DEC-004 | Sovereign authority | Locally authoritative Control Plane has final security/operational authority; Central uses locally approved federation and has no implicit administrative rights. | Preserve local authority and disconnected operation. | Local trust, secrets, policy, grants, audit, operations and plugin governance; Air-Gap remains open. | DEC-003; OD-001, OD-011–OD-012, OD-015, OD-023 | [ADR-V3-004](adr/004-sovereign-authority.md) | V3-001 §4.3 refined and owner-approved by R0-001 decision 4, 2026-10-23 |
| DEC-005 | Domain-owned authorization | Shared Policy Governance with final resource/action authorization in each resource-owning service; Sovereign policy authority is local. | Avoid confused-deputy and identity-equals-permission failures. | Consistent policy inputs plus domain enforcement; identity/tool choices remain open. | OD-009–OD-012 | [ADR-V3-005](adr/005-domain-owned-authorization.md) | V3-001 §4.4 refined and owner-approved by R0-001 decision 5, 2026-10-23 |
| DEC-006 | Plugin extension model | External plugins use Installation-specific identity/grants/tenant binding through Extension Gateway; event-first plus controlled synchronous hooks. | Enable extension without surrendering domain/data ownership. | Lifecycle, isolation, compatibility, audit, timeout/failure semantics are required. | DEC-014; OD-016, OD-021 | [ADR-V3-006](adr/006-plugin-extension-model.md) | V3-001 §4.5 refined and owner-approved by R0-001 decision 6, 2026-10-23 |
| DEC-007 | Data and messaging baseline | Service-owned PostgreSQL with logical/physical isolation, independent roles/migrations, RLS on shared tenant-aware tables; RabbitMQ/outbox/inbox and justified Redis. | Tenant defense-in-depth and reliable integration. | Non-bypass roles, idempotency, recovery and compatible schema evolution. | DEC-014–DEC-015; OD-013–OD-014 | [ADR-V3-007](adr/007-data-messaging-baseline.md) | V3-001 §4.6 refined and owner-approved by R0-001 decision 7, 2026-10-23 |
| DEC-008 | Contract compatibility | Contract-first evolution with backward compatibility; breaking changes require new version, coexistence, deprecation and consumer migration plan. | Enable independent evolution and profile/version skew. | Producers may support multiple versions; DEC-014 governs REST/Event versioning and DEC-015 governs Contract Testing; public API selection remains OD-007 and specific tooling remains implementation-specific. | DEC-014–DEC-015; OD-007 | [ADR-V3-008](adr/008-contract-compatibility.md) | V3-001 §4.6 refined and owner-approved by R0-001 decision 8, 2026-10-23 |
| DEC-009 | Frontend architecture | Modular feature-oriented Frontend with logically isolated features and shared Design System; Micro-Frontend deployment not initially required. | Preserve UI modularity and consistency without premature deployment complexity. | Framework/state/UI/session choices remain open; Backend authorization remains final. | OD-005–OD-007, OD-010 | [ADR-V3-009](adr/009-frontend-architecture.md) | V3-001 §4.7 refined and owner-approved by R0-001 decision 9, 2026-10-23 |
| DEC-010 | Operational profiles | Common operational contracts/acceptance with profile-specific implementation and independent evidence for release, upgrade, recovery, observability and security. | Make all supported profiles operable and auditable. | Evidence multiplies by profile; numeric objectives/tooling remain open. | OD-001, OD-012, OD-015, OD-023 | [ADR-V3-010](adr/010-operational-profiles.md) | V3-001 §4.8 refined and owner-approved by R0-001 decision 10, 2026-10-23 |
| DEC-011 | Logical boundaries and co-deployment | Logical boundaries first; controlled co-deployment may not erase ownership/dependency boundaries; defined microservices retain independent build/version/deployment. | Balance clear ownership with incremental operations. | Boundary enforcement and extraction readiness required under co-deployment. | DEC-001–DEC-002 | [ADR-V3-011](adr/011-logical-boundaries-co-deployment.md) | V3-001 §5 refined and owner-approved by R0-001 decision 11, 2026-10-23 |
| DEC-012 | Evidence-based readiness | Architecture, Implementation and Production Readiness are separate evidence gates; each operational profile needs independent evidence; Codex does not execute builds/tests/deployments. | Prevent unsupported assurance claims. | Completion/release claims must name gate, profile, evidence and omissions. | DEC-015; OD-023 | [ADR-V3-012](adr/012-evidence-based-readiness.md) | V3-001 §4.8/§9 refined and owner-approved by R0-001 decision 12, 2026-10-23 |
| DEC-013 | Backend foundation toolchain | Java 21 LTS; Spring Boot 4.1.2; Gradle multi-project with Groovy DSL and Gradle Wrapper. Service build/artifact/release independence remains mandatory; exact Wrapper distribution evidence is deferred to V3-005 implementation. | Establish one reproducible engineering baseline while preserving independently owned Business Services. | Requires authoritative artifact/version verification, pinned Wrapper distribution/checksum and Backend governance-reference synchronization before implementation evidence. | DEC-001, DEC-002, DEC-011, DEC-012 | [ADR-V3-013](adr/013-backend-foundation-toolchain.md) | Explicit Technical Architecture Owner/CPO Level 2 decision under V3-005, 2026-10-30; no separate DX review claimed |
| DEC-014 | REST and event contract versioning | Public REST uses `/api/v<major>/...`; minor/patch history remains contract metadata. Events use CloudEvents 1.0-compatible envelopes with independent `specversion`, `.v<major>` event type, semantic `payloadversion` and immutable schema identity. Breaking changes require a new major, coexistence, consumer inventory/migration ownership and removal evidence. | Make independently owned contracts evolvable and operationally visible without conflating protocol, business semantics and schema artifacts. | Services may support multiple majors; unknown versions fail closed; security-sensitive changes retain security review; GraphQL versioning remains OD-007 and Contract Testing gates are governed by DEC-015. | DEC-002, DEC-007, DEC-008, DEC-015; OD-007, OD-019 | [ADR-V3-014](adr/014-api-event-versioning.md) | Explicit CPO/Technical Architecture Owner Level 2 decision through OD-008 formal closure; effective upon traceable commit |
| DEC-015 | Risk-based contract testing strategy | Risk-based Consumer-driven Testing; Provider Conformance before Merge/Release; risk-based Real Integration Testing; Service Owner baseline ownership with Audit Trail; limited time-bound exceptions; layered schema/compatibility/negative gates, Manual Review and non-waivable Security boundaries. | Combine structural and behavioral evidence while keeping test cost proportional to risk and preserving independent service delivery. | Applicable CI/Merge/Release gates are blocking; Quality owns risk/evidence policy under the scoped designation; architecture acceptance does not prove CI/runtime execution, Security Sign-off or Production Readiness. | DEC-008, DEC-012, DEC-014; OD-007, OD-019 | [ADR-V3-015](adr/015-contract-testing-strategy.md) | Explicit consolidated CPO/Technical Architecture Owner approval plus separate scoped interim Quality Authority review against pinned ADR SHA-256; effective upon traceable Level 2 commit |

R0-001 ratified DEC-001 through DEC-012 and formalized them as ADR-V3-001 through ADR-V3-012. V3-005 resolves OD-002 through OD-004 through DEC-013/ADR-V3-013. The OD-008 formal-closure task resolves API/event versioning through DEC-014/ADR-V3-014. The OD-020 finalization task resolves contract-testing governance through DEC-015/ADR-V3-015, effective upon its traceable Level 2 commit. Any material change requires a traceable superseding/deprecating ADR rather than silent edits. OD-001, OD-005 through OD-007, OD-009 through OD-019 and OD-021 through OD-023 remain Open.

<a id="v3-024-final-g-r2-closure"></a>
## V3-024 — Formal limited G-R2 closure, 2026-11-13

Under `V3-024-G-R2-FINAL-ACCEPTANCE-AND-CLOSURE`, the TAO explicitly decides
`V3-024 / G-R2: ACCEPTED — LIMITED DESIGN_ONLY / REFERENCE_ONLY`,
`F-R2-01: CLOSED — PROCEDURALLY SATISFIED` on independent Assessment A, and
`V3-024 ARCHITECTURE DESIGN STAGE: CLOSED`. See the
[full dated decision, evidence, restrictions and recording boundary](governance-synchronization.md#v3-024-final-g-r2-closure).
Repository closure requires this task's verified Registration commit, authoritative
Main recording and postflight; owner issuance alone is not completed recording.
Existing `ADR-V3-016 / DEC-016 / P00-006`, the historical effectiveness timestamp,
all 47 conditions and the 41/1/5 review classifications remain unchanged.
F-R2-02 through F-R2-06, all Open Decisions, independent Security/Tenant Isolation,
Backend propagation and implementation/production restrictions remain in force.
This new Gate/finding disposition neither replaces the ADR nor rewrites the history below.

<a id="v3-024-r2-applicability-registration"></a>
## V3-024 R2 applicability registration — separate from Gate acceptance

The TAO approved **V3-024 R2 — Architecture Acceptance Applicability & Exit Boundary**
in the current project conversation. Task `V3-024-G-R2-APPLICABILITY-FORMAL-REGISTRATION`
records that limited decision under existing `ADR-V3-016 / DEC-016 / P00-006`, not a
new global decision or substantive ADR amendment. See the
[full decision, rationale, condition allocation, contract impact and recording boundary](governance-synchronization.md#v3-024-r2-applicability-exit-boundary).
All 47 conditions, existing Open Decisions and later mandatory verification remain binding.
`F-R2-01: TAO APPLICABILITY CONTENT APPROVED — FORMAL REGISTRATION IN PROGRESS` is the
pre-commit record; Registration verification and authoritative Main recording are distinct.
Main recording is `NOT AUTHORIZED — PENDING`; `V3-024 / G-R2: PENDING`.
No implementation, synchronization, Security/isolation acceptance or publication is authorized.
The historical records below and P00-006 effectivity at `2026-11-13T14:21:48+03:30` are unchanged.

## V3-024 proposed consolidated registration — not effective

The following single entry is part of the technically adopted, non-effective governance candidate,
not a completed formal registration. Existing DEC-001 through DEC-015 are unchanged.

| ID | Title | Decision | Rationale | Consequences | Dependencies | Related ADRs | Approval provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DEC-016 | Dedicated Managed disposable reference architecture | CONDITIONALLY ACCEPTED — DESIGN_ONLY / REFERENCE_ONLY; intended ADR lifecycle ACCEPTED; TECHNICALLY PRESENT IN ROOT MAIN — FORMAL LEVEL 2 EFFECTIVENESS NOT ESTABLISHED. DB-001 A database/service/Cell (7); RT-002 A disposable Compose (6); OA-003 B scoped Controller/Agent (8); CL-004 B scoped credentials/rotation (8); RTR-005 B validated placement/fail-closed routing (8); OF-006 B bounded valid local state (10). All 47 conditions and detailed source obligations remain binding architectural requirements, not verified controls. | Reproducible reference design with explicit service, Cell, Tenant and authority boundaries without production-mechanism selection. | Shared host/cluster administration, real identity/trust, credential custody/revocation, durable execution, adapter privilege, freshness and recovery remain unresolved. Overall R2 and independent security PENDING; implementation, B2, merge, publication and production promotion NOT AUTHORIZED. Proposed P00-006 is not effective or propagated. | OD-009/010/011/012/013/014/015/019/022/023 remain OPEN; V3-016 governance, V3-017 Formal R1 and V3-023 Formal B1 remain pending; V3-022 B2 not authorized. | [ADR-V3-016](adr/016-dedicated-managed-reference-architecture.md), V3-024; sub-decisions [DB-001](adr/016-dedicated-managed-reference-architecture.md#db-001), [RT-002](adr/016-dedicated-managed-reference-architecture.md#rt-002), [OA-003](adr/016-dedicated-managed-reference-architecture.md#oa-003), [CL-004](adr/016-dedicated-managed-reference-architecture.md#cl-004), [RTR-005](adr/016-dedicated-managed-reference-architecture.md#rtr-005), [OF-006](adr/016-dedicated-managed-reference-architecture.md#of-006). | Explicit Technical Architecture Owner approval of corrected artifact SHA-256 `aa651e4e45355fb4bc80adf40cf6cd0fc125a702afb686891c28de4535bf0040` and controlled six-file authoring in the project conversation; Backend source `938b9e7e3a0feaed4f3c09056f70365313dabb7e`; Root source `c3926e6a8c9847281d49987abdbafbbced562dbb`. Actual original local candidate commit `fd1e1703afc4fe730ae6e86f1ef72573106082f8`; original execution authorization NOT GRANTED; subsequent retention authorized for reconciliation only, not retroactive authorization. Separately authorized correction `3d6fffea83a7a2fc4c10300ccf5792224edabeba` and authorized final metadata commit `a6558556df6c81d04a4e610ae7698e51071ab2ee` follow it. Option A approves the prospective registration basis. Main's reflog records Fast-forward to `a6558556df6c81d04a4e610ae7698e51071ab2ee` at `2026-11-11T23:48:51+03:30`; adoption execution authorization at time NOT GRANTED, a separate procedural deviation. Subsequent owner retention is for reconciliation only; neither deviation is retroactively authorized. Separately authorized post-adoption authoring, independent review, exact-blob STG-01 renewal, staging and reconciliation commit were completed and separately recorded in local Root main at `39787784980380271753bad8e4a8c164d881fe51`. The subsequent explicit Technical Architecture Owner declaration in conversation resolves the procedural reconciliation prerequisite prospectively, not retrospectively. Its disposition is recorded in local Root main at `8b14ca208a0d3ba14052e0d00ce90fc907ea80fb`. FORMAL LEVEL 2 DETERMINATION: ISSUED — CONDITIONAL by explicit TAO declaration in conversation for ADR-V3-016, DEC-016 and P00-006; see the ADR's conditional determination section. Only Event 1 is completed; determination Git recording, Root main recording and independent post-recording verification remain PENDING. DEC-016 effectiveness is NOT ESTABLISHED pending the approved four-event boundary. |

