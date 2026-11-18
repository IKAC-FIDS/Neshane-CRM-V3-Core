# Proposed task register

All V3-FR-* IDs and definitions are **PROPOSED — NOT APPROVED**. Full fields, prerequisites, exclusions, acceptance, validation and authority requirements are in `proposed-task-register.json`; order is topological guidance, not dates or authorization. Phases may overlap.

## A — Product requirements/scope

- **V3-FR-A-001 — PROPOSED**: Confirm actors, ownership and product decision workflow | Core | prerequisites: separate scoped authorization
- **V3-FR-A-002 — PROPOSED**: Define requirements: Register and Maintain Customer Master | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-003 — PROPOSED**: Define requirements: Find and Review Customer | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-004 — PROPOSED**: Define requirements: Manage Opportunity Through the Sales Pipeline | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-005 — PROPOSED**: Define requirements: Register and Process a Customer Request | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-006 — PROPOSED**: Define requirements: Plan and Track a Work Task | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-007 — PROPOSED**: Define requirements: Establish Trusted Tenant Access | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-008 — PROPOSED**: Define requirements: Evaluate Feature Eligibility | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-009 — PROPOSED**: Define requirements: Enforce Quota-Controlled Operation | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-010 — PROPOSED**: Define requirements: Deliver Authorized In-App Notification | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-011 — PROPOSED**: Define requirements: Attach and Retrieve File for an Approved Resource | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-012 — PROPOSED**: Define requirements: Produce an Approved Deterministic Report | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-013 — PROPOSED**: Define requirements: Record Security, Administrative and Privileged Audit Evidence | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-014 — PROPOSED**: Define requirements: Review Authorized Audit Evidence | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-015 — PROPOSED**: Define requirements: Observe Platform and Service Health | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-016 — PROPOSED**: Define requirements: Execute an Authorized Privileged Operation | Core | prerequisites: V3-FR-A-001
- **V3-FR-A-017 — PROPOSED**: Define cross-capability approval matrices and bounded failure policies | Core | prerequisite: V3-FR-A-001; approved requirements for each selected integration as it enters review. Incremental dispositions; no all-capability completion prerequisite for the first slice.

## B — Architecture/technology decisions

- **V3-FR-B-001 — PROPOSED**: Decision preparation: OD-001 — Full Air-Gapped support: offline-capable only; import/export bridge; fully isolated release channel | Core | prerequisites: separate scoped authorization
- **V3-FR-B-005 — PROPOSED**: Decision preparation: OD-005 — Frontend framework/rendering: React/Angular/Vue/other; SPA/SSR variants | Core | prerequisites: separate scoped authorization
- **V3-FR-B-006 — PROPOSED**: Decision preparation: OD-006 — State/server-cache/UI libraries: library or framework-native approaches | Core | prerequisites: separate scoped authorization
- **V3-FR-B-007 — PROPOSED**: Decision preparation: OD-007 — Public API and GraphQL BFF: REST-first, GraphQL BFF, hybrid, or per-client boundary | Core | prerequisites: separate scoped authorization
- **V3-FR-B-009 — PROPOSED**: Decision preparation: OD-009 — IdP integrations: generic OIDC first versus named enterprise providers/federation | Core | prerequisites: separate scoped authorization
- **V3-FR-B-010 — PROPOSED**: Decision preparation: OD-010 — Session lifecycle/revocation: stateless short-lived, stateful sessions, refresh families, hybrid | Core | prerequisites: separate scoped authorization
- **V3-FR-B-011 — PROPOSED**: Decision preparation: OD-011 — Workload identity: platform-issued credentials, mTLS PKI, SPIFFE/SPIRE, hybrid | Core | prerequisites: separate scoped authorization
- **V3-FR-B-012 — PROPOSED**: Decision preparation: OD-012 — Secrets/keys: platform-native, Vault-class, cloud KMS/HSM, Sovereign-local mix | Core | prerequisites: separate scoped authorization
- **V3-FR-B-013 — PROPOSED**: Decision preparation: OD-013 — PostgreSQL migrations: Flyway, Liquibase, framework-native, other | Core | prerequisites: separate scoped authorization
- **V3-FR-B-014 — PROPOSED**: Decision preparation: OD-014 — Java/RLS integration: transaction interceptor, explicit unit-of-work, connection wrapper | Core | prerequisites: separate scoped authorization
- **V3-FR-B-015 — PROPOSED**: Decision preparation: OD-015 — Runtime orchestration: Compose-equivalent reference, Kubernetes, Nomad, other profile-specific runtime | Core | prerequisites: separate scoped authorization
- **V3-FR-B-016 — PROPOSED**: Decision preparation: OD-016 — Managed Plugin Runtime isolation: containers, microVMs, WASM, external workers, hybrid | Core | prerequisites: separate scoped authorization
- **V3-FR-B-017 — PROPOSED**: Decision preparation: OD-017 — Object storage: S3-compatible, cloud-specific, filesystem appliance, hybrid | Core | prerequisites: separate scoped authorization
- **V3-FR-B-018 — PROPOSED**: Decision preparation: OD-018 — Search/indexing: PostgreSQL search, external engine, hybrid projections | Core | prerequisites: separate scoped authorization
- **V3-FR-B-019 — PROPOSED**: Decision preparation: OD-019 — Background scheduling: in-service scheduler, DB-coordinated jobs, workflow engine, broker scheduling | Core | prerequisites: separate scoped authorization
- **V3-FR-B-021 — PROPOSED**: Decision preparation: OD-021 — Marketplace/Developer Portal: internal catalog, partner portal, public marketplace | Core | prerequisites: separate scoped authorization
- **V3-FR-B-022 — PROPOSED**: Decision preparation: OD-022 — Tenant migration automation: offline transfer, dual-run, event replication, cell-native workflow | Core | prerequisites: separate scoped authorization
- **V3-FR-B-023 — PROPOSED**: Decision preparation: OD-023 — SLO/RTO/RPO/capacity: per-profile/service objectives and measurement | Core | prerequisites: separate scoped authorization
- **V3-FR-B-024 — PROPOSED**: Review applicable design-governance synchronization and dependency acceptance | Core | prerequisites: separate scoped authorization

## C — AUTH/IAM foundation

- **V3-FR-C-001 — PROPOSED**: Design trusted access and Tenant Context contracts | Core | prerequisites: V3-FR-A-007
- **V3-FR-C-002 — PROPOSED**: Implement approved identity, membership and workload boundaries | Backend | prerequisites: V3-FR-C-001, V3-FR-D-001, V3-FR-B-009, V3-FR-B-010, V3-FR-B-011, V3-FR-B-012

## D — Runtime Tenant Isolation remediation

- **V3-FR-D-001 — PROPOSED**: Determine G-RUNTIME remediation scope and path applicability | Core | prerequisites: V3-FR-B-024
- **V3-FR-D-002 — PROPOSED**: Remediate and verify approved Runtime isolation control paths | Backend | prerequisites: V3-FR-D-001, V3-FR-C-002, V3-FR-B-013, V3-FR-B-014
- **V3-FR-D-003 — PROPOSED**: Submit Runtime reassessment for explicit scoped Gate decision | Core | prerequisites: V3-FR-D-002

## E — Platform capabilities

- **V3-FR-E-000 — PROPOSED**: Design approved producer/Audit event and ingestion contracts | Core | prerequisites: V3-FR-A-017, V3-FR-C-001
- **V3-FR-E-PF-002 — PROPOSED**: Implement approved capability: Evaluate Feature Eligibility | Backend | prerequisites: V3-FR-A-008, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-PF-003 — PROPOSED**: Implement approved capability: Enforce Quota-Controlled Operation | Backend | prerequisites: V3-FR-A-009, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-PF-004 — PROPOSED**: Implement approved capability: Deliver Authorized In-App Notification | Backend | prerequisites: V3-FR-A-010, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-PF-005 — PROPOSED**: Implement approved capability: Attach and Retrieve File for an Approved Resource | Backend | prerequisites: V3-FR-A-011, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-PF-006 — PROPOSED**: Implement approved capability: Produce an Approved Deterministic Report | Backend | prerequisites: V3-FR-A-012, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-SO-001 — PROPOSED**: Implement approved capability: Record Security, Administrative and Privileged Audit Evidence | Backend | prerequisites: V3-FR-A-013, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-SO-002 — PROPOSED**: Implement approved capability: Review Authorized Audit Evidence | Backend | prerequisites: V3-FR-A-014, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-SO-003 — PROPOSED**: Implement approved capability: Observe Platform and Service Health | Backend | prerequisites: V3-FR-A-015, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-E-SO-004 — PROPOSED**: Implement approved capability: Execute an Authorized Privileged Operation | Backend | prerequisites: V3-FR-A-016, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000

## F — Business capabilities

- **V3-FR-F-BJ-001 — PROPOSED**: Implement approved capability: Register and Maintain Customer Master | Backend | prerequisites: V3-FR-A-002, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-F-BJ-002 — PROPOSED**: Implement approved capability: Find and Review Customer | Backend | prerequisites: V3-FR-A-003, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000, V3-FR-F-BJ-001
- **V3-FR-F-BJ-003 — PROPOSED**: Implement approved capability: Manage Opportunity Through the Sales Pipeline | Backend | prerequisites: V3-FR-A-004, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000, V3-FR-F-BJ-001
- **V3-FR-F-BJ-004 — PROPOSED**: Implement approved capability: Register and Process a Customer Request | Backend | prerequisites: V3-FR-A-005, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000, V3-FR-F-BJ-001
- **V3-FR-F-BJ-005 — PROPOSED**: Implement approved capability: Plan and Track a Work Task | Backend | prerequisites: V3-FR-A-006, V3-FR-A-017, V3-FR-C-002, V3-FR-D-003, V3-FR-E-000
- **V3-FR-F-000 — PROPOSED**: Implement isolated Customer domain rules candidate | Backend | prerequisites: V3-FR-A-002

## G — Frontend

- **V3-FR-G-001 — PROPOSED**: Define feature UX, Design System and client boundary specifications | Core | prerequisites: V3-FR-A-001
- **V3-FR-G-002 — PROPOSED**: Implement approved Frontend foundation and feature slices | Frontend | prerequisites: V3-FR-G-001, V3-FR-B-005, V3-FR-B-006, V3-FR-B-007, V3-FR-C-001

## H — Cross-capability integration

- **V3-FR-H-001 — PROPOSED**: Validate first Customer end-to-end vertical slice | Backend + Frontend | prerequisites: V3-FR-G-002, V3-FR-F-BJ-001, V3-FR-F-BJ-002, V3-FR-E-SO-001, V3-FR-E-SO-003
- **V3-FR-H-002 — PROPOSED**: Validate remaining cross-capability journeys and contracts | Backend + Frontend | prerequisites: V3-FR-F-BJ-001, V3-FR-F-BJ-002, V3-FR-F-BJ-003, V3-FR-F-BJ-004, V3-FR-F-BJ-005, V3-FR-C-002, V3-FR-E-PF-002, V3-FR-E-PF-003, V3-FR-E-PF-004, V3-FR-E-PF-005, V3-FR-E-PF-006, V3-FR-E-SO-001, V3-FR-E-SO-002, V3-FR-E-SO-003, V3-FR-E-SO-004, V3-FR-G-002, V3-FR-H-001

## I — Security/acceptance

- **V3-FR-I-001 — PROPOSED**: Assess security and acceptance requirements across all profiles | Core | prerequisites: V3-FR-A-017, V3-FR-D-001
- **V3-FR-I-002 — PROPOSED**: Execute approved security/product acceptance and request dispositions | Backend + Frontend | prerequisites: V3-FR-H-002, V3-FR-I-001, V3-FR-D-003

## J — Release/production readiness

- **V3-FR-J-001 — PROPOSED**: Prepare release/readiness evidence: Shared SaaS | Core + Backend + Frontend | prerequisites: V3-FR-I-002, V3-FR-B-015, V3-FR-B-023, V3-FR-B-012
- **V3-FR-J-002 — PROPOSED**: Prepare release/readiness evidence: Dedicated Managed | Core + Backend + Frontend | prerequisites: V3-FR-I-002, V3-FR-B-015, V3-FR-B-023, V3-FR-B-012
- **V3-FR-J-003 — PROPOSED**: Prepare release/readiness evidence: Dedicated Sovereign | Core + Backend + Frontend | prerequisites: V3-FR-I-002, V3-FR-B-015, V3-FR-B-023, V3-FR-B-012
- **V3-FR-J-004 — PROPOSED**: Request final First Release readiness and release authorization | Core | prerequisites: V3-FR-J-001, V3-FR-J-002, V3-FR-J-003

## Existing identifiers (preserved, not new tasks)

- `G-RUNTIME.03`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `G-RUNTIME.04`: AUTHORITY_DECISION_RECORDED — BLOCKED
- `G-RUNTIME.05`: Scope assessment; FE-BE and AUTH/IAM decisions PENDING; no prior forward product roadmap located
- `GOV-V3-001`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `R0-001`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-001`: Approved initial architecture; not product implementation
- `V3-002`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-002B`: Owner dispositions/product scope/logical ownership complete; no source port authorization
- `V3-003`: CLOSED — ANALYTICAL SCOPE ONLY; DEC-001..014 bounded approvals; detailed security policies/candidates incomplete
- `V3-004`: CLOSED — FIRST_RELEASE support design baseline only
- `V3-005`: CLOSED — ENGINEERING FOUNDATION R0 baseline
- `V3-006`: CLOSED — ADR/contract change governance baseline
- `V3-007`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-008`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-009`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-010`: CLOSED — JAVA SERVICE SKELETON R1; not business service
- `V3-011`: CLOSED — HTTP CONTRACT ENGINEERING R1 only
- `V3-012`: CLOSED — EVENT CONTRACT ENGINEERING R1 only
- `V3-013`: CLOSED — OBSERVABILITY LIBRARY ENGINEERING R1 only
- `V3-014`: CLOSED — CONFIGURATION/SECRET CONTRACT ENGINEERING R1 only
- `V3-015`: CLOSED — ARCHITECTURE BOUNDARY ENGINEERING R1 only
- `V3-016`: IN PROGRESS — GOVERNANCE PHASE A ENGINEERING ACCEPTED; hosted enforcement and R1 PENDING
- `V3-017`: IMPLEMENTATION VALIDATED — R1 ACCEPTANCE PENDING; reuse separately scoped
- `V3-020`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-021`: IMPLEMENTED / DESIGN PROPOSED — R2 REVIEW PENDING in Backend source; no trusted Membership implementation acceptance
- `V3-022`: Stage B1 deterministic reference; later limited design awareness does not authorize Stage B2
- `V3-023`: Shared laboratory/reference evidence; formal B1/final isolation not inherited
- `V3-024`: G-R2, Security and Tenant LIMITED DESIGN/REFERENCE accepted per latest Core annotations; final Runtime G-RUNTIME BLOCKED
- `V3-025`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-LOCAL-INFRA-001`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-LOCAL-INFRA-003`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-LOCAL-INFRA-004`: REFERENCE LOCATED — completion not established by this review; inspect cited original task before reuse
- `V3-LOCAL-INFRA-005`: ACCEPTED — DEVELOPMENT-ONLY; not product Runtime/security acceptance
