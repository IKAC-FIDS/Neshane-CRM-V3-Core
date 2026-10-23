# Neshane V3 architecture baseline

- Architecture version: `NESHANE-V3-ARCH-P00-002`
- Governance reference: `NESHANE-V3-GOV-P00-000A` (unchanged)
- Status: approved architecture revision; project-owner decision ratification recorded by R0-001; implementation and operational evidence remain pending
- Authority: ADR-V3-001 through ADR-V3-012 and future approved V3 ADRs
- Scope: intended target architecture; no implementation, security control, deployment, or readiness is implied

## Version history

| Revision | Status | Date | Record |
| --- | --- | --- | --- |
| `NESHANE-V3-ARCH-P00-001` | Superseded candidate | 2026-10-23 | V3-001 documented DEC-001–DEC-012 as pending R0 and OD-001–OD-023 as Open. |
| `NESHANE-V3-ARCH-P00-002` | Current approved architecture revision | 2026-10-23 | R0-001 recorded project-owner approval, formalized ADR-V3-001–ADR-V3-012 and refined the decisions without closing any Open Decision. |

Supersession preserves the historical status of P00-001; it does not imply that P00-001 already contained the R0 refinements.

## Goals and quality attributes

Neshane V3 is a multi-tenant CRM platform that supports independently evolving business capabilities, extensibility, and three production deployment profiles without changing core business semantics. Priority qualities are tenant and data isolation, explicit trust and authorization, service autonomy, contract compatibility, resiliency, auditability, operability, recoverability, supply-chain integrity, accessibility, and Persian/RTL usability.

Architecture readiness, implementation readiness, and production readiness are separate states. Documentation proves none of the runtime controls described here.

## Architectural principles

1. Business capability and data ownership define service boundaries; a logical capability does not automatically require its own initial deployment.
2. Java/Spring Boot microservices use Domain-Driven Design and Hexagonal Architecture. Domain logic is infrastructure-independent.
3. Each defined Business Service has an independent build/test boundary, version, artifact, deployment and lifecycle; releasing it must not require rebuilding another Business Service.
4. No cross-service implementation imports, private database access, shared business ownership, or shared ORM entities are allowed.
5. Authentication, membership, entitlement, authorization, and placement are distinct decisions. Shared Policy Governance does not replace the final authorization decision enforced by each resource-owning service; Sovereign policy authority is local.
6. Tenant identity is stable and independent of cell placement or physical deployment.
7. Public/internal APIs and events are contract-first and versioned. Breaking changes require a new version, coexistence, explicit deprecation and consumer migration planning; asynchronous delivery assumes duplicates and failures.
8. Plugins are external principals behind governed extension boundaries, never in-process extensions of Core or Business Services.
9. Sovereign deployments retain final local operational/security authority without synchronous Central dependency for critical operations; Central federation is locally approved and grants no implicit administration.
10. Frontend is modular and feature-oriented with logically isolated features and a shared Design System; independently deployed Micro-Frontends are not initially required.
11. Approved principles and unresolved implementation choices are kept separate. See [decision register](decision-register.md) and [open decisions](open-decisions.md).

## Technology baseline

| Area | Binding baseline | Unresolved detail |
| --- | --- | --- |
| Backend | Java, Spring Boot, independent microservices, DDD/Hexagonal Architecture and independent build/test/version/release boundaries | Exact versions, Gradle/Maven and project layout ([OD-002–OD-004](open-decisions.md)) |
| Relational data | PostgreSQL; service-owned persistence; RLS for shared tenant-aware tables | Migration tool and Java/RLS integration ([OD-013–OD-014](open-decisions.md)) |
| Messaging | RabbitMQ; transactional outbox and idempotent inbox where reliable events are required | Topology and detailed contract/version rules ([OD-008](open-decisions.md)) |
| Cache | Redis is permitted only when justified with tenant-safe keys, authorization, freshness, and safe failure behavior | Per-use-case adoption and numeric policies |
| Identity | Standards-based independent IdPs; OIDC/OAuth 2.0 where appropriate; Neshane-owned trust/principal mapping | Providers, sessions, workload identity and secrets tooling ([OD-009–OD-012](open-decisions.md)) |
| Frontend | Independent modular feature-oriented boundary with shared Design System; Persian/RTL and accessibility; no initial Micro-Frontend requirement | Framework, state and UI libraries ([OD-005–OD-006](open-decisions.md)) |
| Runtime | Three deployment profiles; reproducible signed/versioned artifacts | Orchestration and plugin isolation technologies ([OD-015–OD-016](open-decisions.md)) |

GraphQL BFF, object storage, search, scheduling, contract tools, and specific products are not selected by this baseline.

## Decision traceability

| Baseline concern | Decision record |
| --- | --- |
| Java/Spring Boot microservices and independent service releases | DEC-001; [ADR-V3-001](adr/001-backend-architecture.md) |
| Capability boundaries, service/data ownership and forbidden coupling | DEC-002; [ADR-V3-002](adr/002-service-ownership.md) |
| Cell-based hybrid tenancy and three production profiles | DEC-003; [ADR-V3-003](adr/003-cell-based-hybrid-tenancy.md) |
| Local Sovereign authority and controlled Central federation | DEC-004; [ADR-V3-004](adr/004-sovereign-authority.md) |
| Domain-owned authorization and shared policy governance | DEC-005; [ADR-V3-005](adr/005-domain-owned-authorization.md) |
| Event-first plugin model and controlled hooks | DEC-006; [ADR-V3-006](adr/006-plugin-extension-model.md) |
| PostgreSQL/RLS, RabbitMQ/outbox/inbox and justified Redis | DEC-007; [ADR-V3-007](adr/007-data-messaging-baseline.md) |
| Contract-first controlled compatibility | DEC-008; [ADR-V3-008](adr/008-contract-compatibility.md) |
| Modular feature-oriented Frontend and shared Design System | DEC-009; [ADR-V3-009](adr/009-frontend-architecture.md) |
| Verifiable profile-specific operations | DEC-010; [ADR-V3-010](adr/010-operational-profiles.md) |
| Logical boundaries with controlled co-deployment | DEC-011; [ADR-V3-011](adr/011-logical-boundaries-co-deployment.md) |
| Evidence-based architecture/implementation/production gates | DEC-012; [ADR-V3-012](adr/012-evidence-based-readiness.md) |

Full rationale, consequences, dependencies, provenance and R0 status are in the [decision register](decision-register.md).

## System boundaries

### Platform Core

Platform Core owns Identity Trust, Tenant Management, Organization and Membership, shared Authorization/Policy Governance, Entitlement, and related cross-cutting platform contracts. Identity authenticates and maps principals; tenant/membership establishes validated association; entitlement establishes consumption eligibility; each resource-owning Business Service makes and enforces final resource/action authorization.

Platform Core must not become a universal business-data owner, bypass service authorization, expose private databases, or infer permission from identity or membership alone. Logical responsibilities may initially be co-deployed only with explicit ownership and dependency boundaries.

### Business Services

Initial logical capabilities include Customer, Sales, Notification, Reporting, Workflow, and future independently owned business capabilities. Each owns its model, rules, persistence, contracts, authorization, migrations, and audit-relevant business decisions. Reporting uses authorized contracts, events, or owned projections rather than cross-service SQL.

Business Services must not import another service's implementation, query its private database, delegate final authorization to Frontend/Gateway/Control Plane, or share transactions across service boundaries.

### Plugin Platform

The Plugin Control Plane owns registry metadata, versions/compatibility, installation management, permission grants, and lifecycle governance. The Plugin Data Plane owns the Extension Gateway, event and hook dispatch, and installation-scoped access enforcement. The Execution Boundary hosts isolated third-party runtimes through customer-hosted, Neshane-hosted, or Sovereign-local models.

Plugin Package, Installation, and Runtime Instance are distinct. Each Installation is a tenant-bound principal with its own grants, configuration, and lifecycle. Plugins use language-independent versioned contracts and cannot access internal databases/classes. Event-driven integration is preferred; synchronous hooks require explicit timeout, failure, authorization, and idempotency semantics. Business Services retain final domain authority. Hosting/sandbox technology is open.

### Operational Platform

Operational responsibilities include deployment/cell management, configuration/secrets, observability, release management, backup/disaster recovery, supply-chain security, operational audit, and governed support access. It may operate infrastructure but must not silently acquire business-data or domain-authorization ownership. Privileged access is scoped, separated, auditable, and locally governed for Sovereign deployments.

## Cell-based hybrid multi-tenancy

Tenant identity remains stable while placement changes. Tenant routing and a monotonic Placement Generation prevent stale routing during provisioning, failover, or migration. Cell lifecycle, placement changes, compatibility, rollback/recovery, and tenant migration are explicit architectural responsibilities, not application hints.

| Profile | Required target behavior |
| --- | --- |
| Shared SaaS | Multiple tenants share managed cells; tenant-aware tables require validated Tenant Context, application authorization, PostgreSQL RLS, tenant-scoped constraints, and runtime roles that cannot bypass isolation. |
| Dedicated Managed | Dedicated placement operated through centrally managed capabilities while preserving service ownership, tenant authorization, and private database boundaries. |
| Dedicated Sovereign | Locally authoritative Control Plane and independently operating Data Plane; local trust, secrets, grants, audit, plugin lifecycle, and operations; no synchronous Central dependency for critical business/security operations. |

Dedicated profiles retain compatible business contracts and logical models. Offline-capable Sovereign does not mean fully Air-Gapped; that remains [OD-001](open-decisions.md). Outbound telemetry/metadata and federation are optional and controlled by local policy. Central administrative identity grants no automatic local administrative authority.

## Control Plane and Data Plane

The Control Plane governs placement, lifecycle, policy distribution, registrations, grants, compatibility, and operational intent. The Data Plane executes business APIs, events, hooks, and persistence under service/tenant authorization. Central management interfaces never expose service databases or replace domain authorization. In Sovereign, the local Control Plane has final security and operational authority; Central interaction exists only through locally approved federation and conveys no implicit administrative right.

Shared and Dedicated Managed profiles may use central control capabilities. Sovereign profiles require local authoritative control and data execution. Cross-domain federation must be explicitly enabled and policy constrained.

## Trust, identity, and authorization

- Independent standards-based IdPs authenticate users; Neshane owns accepted issuer/trust, principal mapping, audience, and lifecycle contracts.
- User, Service, Operator, and Plugin Installation identities are distinct. Workloads may belong to independent Trust Domains.
- Service calls require authenticated audience-restricted identities. A trusted identity, signed token, tenant membership, or broker delivery never by itself grants an operation.
- Authorization chain: authentication -> tenant membership -> entitlement -> owning-service resource/action authorization. Each step remains explicit.
- Plugin access additionally requires a valid Installation identity, tenant binding, and grants.
- Indeterminate security decisions fail closed when safe access cannot be established.
- Sovereign supports local trust roots and credential lifecycle. Specific IdP, policy engine, workload tooling, secrets product, and session model remain open.

## Data ownership and isolation

PostgreSQL is the primary relational store. Each service owns credentials, schema/logical database, migrations, mappings, repositories, and retention. Cross-service SQL, foreign keys, shared repositories, and private-database access are prohibited.

Shared tenant-aware data uses explicit tenant keys, tenant-scoped constraints/references, validated transaction-local Tenant Context, application authorization, and PostgreSQL RLS for reads and writes. Ordinary runtime identities cannot own protected tables or bypass RLS. Dedicated placement does not remove logical tenant/authorization contracts.

Schema evolution must preserve tenant isolation and compatibility. Cross-service needs use authorized APIs, versioned events, or owned projections with source and freshness provenance.

## API and messaging

Public and internal contracts are designed contract-first, versioned and owned. Backward-compatible evolution is preferred. Breaking changes require a new contract version, controlled coexistence, explicit deprecation, consumer inventory/migration planning and removal criteria. Exact REST/GraphQL BFF and versioning mechanics remain open. Gateways may compose or route but never own final authorization or access service databases.

RabbitMQ is the baseline asynchronous transport. State changes that require reliable domain-event publication use a transactional outbox; consumers persist inbox/idempotency state before acknowledging durable effects. Designs account for duplicates, reordering, bounded retries, dead-letter/re-drive, reconciliation, tenant provenance, producer identity, and minimized payloads. Exactly-once external effects are not assumed.

## Frontend integration

Frontend is independently versioned, modular and feature-oriented, with logically isolated feature modules and a shared Design System. Independent Micro-Frontend deployment is not required initially. Frontend has no dependency on Backend implementation details; API/session contracts are explicit, and transport DTOs are separated from domain/view models when meaning or lifecycle differs. Client permission checks are UX behavior only; Backend remains authoritative. Secrets never enter browser bundles. UI supports Persian, RTL, responsive behavior, accessibility, consistent states and safe recovery. Framework and libraries remain open.

## Operations and Sovereign constraints

Common operational contracts and acceptance requirements apply across profiles, with profile-specific implementations. Services require reproducible builds, versioned artifacts, signatures/integrity verification, structured logs, metrics, distributed tracing, safe configuration, external secrets, installation/recovery contracts, backup/restore, upgrade/rollback, and security-operation procedures. Release, upgrade, recovery, observability and security readiness require independent evidence for each profile. Values for SLO/RTO/RPO/capacity remain open.

Sovereign must locally perform critical administration, trust/credential lifecycle, audit, recovery, plugin governance, and business operations. Optional Central exchange must be locally permitted, minimized, authenticated, and resilient to disconnection.

## Scope by area

| Area | Architectural obligation | Minimal reference implementation in later tasks | Production capability before release | Intentionally deferred |
| --- | --- | --- | --- | --- |
| Foundation V3 | Build/dependency boundaries, safe configuration, trust/tenant contracts, observability and compatibility foundations | One thin end-to-end slice proving boundaries without product breadth | Enforced supply chain, recovery evidence, security/isolation and contract gates | Broad product functionality and speculative shared frameworks |
| Platform Core | Separate identity trust, tenant/membership, entitlement and policy governance | Test principals/tenant context and narrow contracts required by the first slice | Approved identity/session lifecycle, privileged administration, audit and isolation evidence | Specific vendor/tool choices and unnecessary registries |
| Business Services | Capability/data ownership and owner authorization | Small owned vertical slice, chosen by later Task ID | Complete domain, isolation, recovery, contracts and operational evidence per released service | Unrequested business capabilities and premature service splitting |
| Plugin Platform | External principal, gateway, grants, events/hooks and execution boundary | Contract/grant model and safe stub only after plugin decisions | Lifecycle, isolation, reconciliation, audit and supported hosting models | Sandbox/orchestration choice and marketplace breadth |
| Operational Platform | Cells, placement, releases, secrets, telemetry, recovery and audit | Minimal local development/reference operational contract | All-profile installation, upgrade, rollback, backup/restore, integrity and Sovereign-local operations | Production automation until authorized; full Air-Gap pending decision |
| Frontend | Independent boundary, explicit contracts, secure UX, RTL/accessibility and state separation | First approved-framework feature shell in a later task | Critical user flows, secure sessions, compatibility, accessibility and recovery evidence | Framework/library selection and unrequested screens |

## Risks and limitations

- Cell routing, Placement Generation, migration state machine, and Central/local authority protocols are architectural obligations but not yet designed in implementation detail.
- Sovereign autonomy increases release, trust, support, audit, and compatibility complexity.
- Plugin extensibility expands attack surface; runtime isolation technology and support boundaries are unresolved.
- Identity session/revocation, workload identity, secrets, API shape, and orchestration choices block affected production designs.
- Numeric reliability/security objectives are absent; production readiness cannot be assessed.
- Legacy V2 evidence is documentation-level for this task; see [legacy reference](legacy-v2-reference.md).
- No described safeguard is implemented or verified.

## Existing guidance reconciliation

No binding V3 governance rule contradicts this baseline. Two earlier Root standards contain explicit proposals rather than approvals: `architecture/standards/api-design.md` discusses versioned REST resources and proposes `/api/v1`, while `architecture/standards/repository-structure.md` proposes `ir.neshane.<service>` and leaves build layout open. They remain non-binding under OD-007/OD-008 and OD-004 respectively. After R0 and the relevant ADR, an authorized governance-alignment task must either adopt or revise those proposals and propagate the new reference. V2's GraphQL BFF, Compose, NestJS/TypeScript, Prisma and object-storage choices are historical conflicts/non-selections documented in [legacy-v2-reference.md](legacy-v2-reference.md); their V2 records are not modified.

## Open decisions

All unresolved choices are tracked in [open-decisions.md](open-decisions.md), OD-001 through OD-023. An existing naming convention, legacy decision, or example does not close an item. Material decisions require an approved V3 ADR and decision-register update.

## Explicit non-goals of V3-001

No Java or Frontend code, microservice, migration, authentication, plugin runtime, CI/CD, deployment automation, Docker/Kubernetes configuration, V2 data migration, production testing, publishing, or release work is included. This task does not select unresolved tools, create application/infrastructure files, or start V3-002.

## Architecture acceptance principles

R0-001 records project-owner ratification of DEC-001–DEC-012 and formalizes ADR-V3-001–ADR-V3-012 as this approved architecture revision. It does not supply reviewer identity/signature, implementation evidence, runtime security evidence or an unconditional R0 pass. Those pending items remain visible in the [R0 checklist](reviews/R0-checklist.md). Runtime and profile-readiness claims require later executable evidence.

