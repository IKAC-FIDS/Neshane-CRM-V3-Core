# Neshane CRM V2 inventory and salvage assessment

## 1. Document control and scope

| Field | Value |
| --- | --- |
| Task | V3-002 — Legacy V2 Inventory and Salvage Assessment |
| Assessment date | 2026-10-23 |
| V3 architecture baseline | `NESHANE-V3-ARCH-P00-002` |
| V3 governance baseline | `NESHANE-V3-GOV-P00-000A` |
| V2 workspace | `E:\Neshane-CRM-V2` (strictly read-only) |
| V3 writable scope | This document under the Core `migration/` directory |
| Disposition authority | Original dispositions were Codex proposals; all 46 Final Dispositions are now owner-approved in `v2-owner-review.md` |
| Runtime evidence | None. No source, build, test, migration, container, database, service, CI, or validator was executed |
| Outcome | **Inventory Complete — Owner Disposition Review Complete** |
| V3-002A historical-source outcome | **Historical Source Verified — Inventory Reconciled**; owner dispositions are complete; see [historical evidence recovery](v2-historical-evidence.md) |

This inventory assesses the accessible V2 workspace and its related historical evidence. It does not migrate source, approve a V3 implementation, validate runtime behavior, or make V2 architecture authoritative. `RETAIN` means retain semantics, evidence, a contract idea, or a regression scenario where useful; it never authorizes copying source into V3.

## 2. Executive summary

The accessible V2 workspace is a small TypeScript/NestJS foundation fixture rather than a complete CRM product. Direct source contains one GraphQL BFF, one `tenant-organization` service, four shared packages, a four-table PostgreSQL/Prisma model, Redis cache behavior, RabbitMQ outbox/inbox behavior, Docker/Compose configuration, two CI workflows, two test files containing 17 test cases, governance tools, and architecture documentation.

The strongest salvage opportunities are behavioral rather than source-level: transaction-local tenant context, PostgreSQL RLS with ordinary roles, tenant/permission-scoped cache keys, atomic state-plus-outbox writes, publisher confirms, durable inbox/idempotency, bounded retry/DLQ behavior, failure-oriented integration scenarios, explicit boundary checks, and evidence-gate language. These align in principle with ADR-V3-002, ADR-V3-003, ADR-V3-005, ADR-V3-007, ADR-V3-008, and ADR-V3-012.

The implementation stack and several historical choices are not portable as V3 decisions: NestJS/TypeScript, pnpm/Turborepo, Prisma, GraphQL BFF as the principal API, and Docker Compose as the deployment answer are either replaced by V3 or remain open under OD-002–OD-008, OD-013–OD-015, and OD-020. The local signed-context mechanism is explicitly a non-production fixture and does not implement V3 identity, workload trust, membership, entitlement, or domain authorization.

V3-002A subsequently found the historical repository at `E:\nodejs\iam-crm-backend`, verified its Git origin and the exact commit object `9b918ba8972812c129c8b073e1ac4991023ccbbb`, and read that revision without checkout or repository mutation. All 106 indexed paths exist and all 106 ordinary SHA-256 content hashes match; zero entries mismatch or remain unverifiable. The pinned tree contains 838 files, so the index was a curated subset rather than a complete manifest.

Static source inspection now confirms implementations for Identity/session/SSO/passkey, Tenant/Organization/Membership, Notification, Linka, Customer Requests, Audit, Quota/Entitlement, AI/reporting, and additional CRM/Sales/Work/Content/Portal/Knowledge capabilities. These findings improve inventory confidence but do not approve source reuse, service boundaries, product scope, runtime security, or production readiness. The exact evidence and limitations are recorded in [Historical V2 source evidence recovery](v2-historical-evidence.md).

### Asset and disposition totals

| Inventory grouping | Asset groups |
| --- | ---: |
| Build/toolchain | 1 |
| Application, service, domain, API, and security fixtures | 5 |
| Shared packages and test support | 4 |
| Data, migration, infrastructure, cache, and messaging | 6 |
| Test suites | 2 |
| Deployment and CI | 3 |
| Governance, boundary tools, reports, and local skills | 4 |
| Architecture/engineering documentation and evidence records | 5 |
| Historical capability candidates and source groups | 16 |
| **Total** | **46** |

| Current disposition | Count |
| --- | ---: |
| RETAIN | 20 |
| REWRITE | 23 |
| RETIRE | 3 |
| NEEDS_REVIEW | 0 |
| **Total** | **46** |

## 3. Evidence collection method and limitations

### Pass A — discovery

- Enumerated the V2 root and first-party roots `apps`, `services`, `packages`, `infra`, `test`, `.github`, `docs`, `tools`, and `.agents` with bounded depth and explicit exclusions.
- Built a deduplicated file manifest for those roots while excluding dependency, generated, build, coverage, and cache directories.
- Searched archive extensions (`.zip`, `.tar`, `.gz`, `.tgz`) without extraction; no archive was found outside excluded dependency/build paths.
- Recorded metadata rather than contents for excluded generated/dependency trees.

### Pass B — analysis

- Read all local product source under `apps/*/src`, `services/*/src`, and `packages/*/src`.
- Read the Prisma schema and migration, PostgreSQL role initialization, root build/deployment manifests, both CI workflows, both test sources, representative governance implementations, the V2 baseline/ADR/engineering corpus, and the legacy evidence index.
- Verified the local historical Git repository identity and exact pinned commit, compared all 106 indexed SHA-256 values against exact-revision raw blob bytes, enumerated its 838-file tree, and inspected representative source/tests for each required and newly discovered capability.
- Compared observed behavior with V3 ADR-V3-001 through ADR-V3-012 and OD-001 through OD-023.
- Used exact file/line evidence where source was directly available. Claims that still depend on absent provider, production, runtime or business-authority evidence remain labeled Documentation-Reported, Probable or Unverified as appropriate.

### Evidence labels

- **Directly Observed:** content read from the local V2 file.
- **Documentation-Reported:** a local V2 report describes evidence from another source that is not present here.
- **Inferred:** a limited conclusion derived from multiple observed artifacts; not runtime proof.
- **Unverified:** required source or executable evidence is unavailable.

### Limitations

- No runtime behavior, build success, test result, migration behavior, RLS enforcement, broker behavior, cache behavior, or CI outcome was verified.
- No database, production configuration, secrets store, data volume, provider contract, traffic profile, backup, restore, deployment, or operational environment was available.
- The 106-file historical index is fully hash-verified, but it covers only 106 of 838 files in the pinned tree. The remaining 732 files were enumerated and grouped by repository/capability; they have no expected hashes in the V2 index.
- Minified one-line source reduces line granularity in a few files; the cited line still identifies the complete relevant implementation.
- No V2 frontend application, plugin runtime, plugin contract, Sovereign control plane, Dedicated Managed implementation, or Dedicated Sovereign implementation was found.

## 4. Inventory coverage and exclusions

### Accessible first-party file coverage

| Root | Files covered | Coverage note |
| --- | ---: | --- |
| Root configuration/manifests | 10 | `package.json`, workspace/lock/config files, Docker/Compose and ignore files |
| `apps/` | 8 | BFF package/config and all source files; generated `dist` excluded |
| `services/` | 16 | Tenant/Organization package, all source, Prisma schema and migration; generated client/`dist` excluded |
| `packages/` | 12 | Config, contracts, observability, and testing packages; generated `dist` excluded |
| `infra/` | 1 | PostgreSQL role initialization |
| `test/` | 2 | Unit and integration suites |
| `.github/` | 2 | Governance and foundation CI workflows |
| `docs/` | 31 | ADRs, architecture, engineering, and skill-audit evidence |
| `tools/` | 28 | Governance validator, boundary enforcement, reports, tests, and fixtures |
| `.agents/` | 16 | V2-specific local skills |
| **Total** | **126** | Accessible first-party files, excluding generated/dependency artifacts |

### Explicit exclusions

| Excluded path/category | Discovery result | Reason |
| --- | --- | --- |
| `node_modules/` | Present; not enumerated | Third-party dependency tree, not first-party migration inventory |
| `.turbo/` | 66 files / 65,087 bytes | Build cache |
| `apps/bff/dist/` | 6 files / 10,834 bytes | Generated build output; source inspected instead |
| `services/tenant-organization/dist/` | 11 files / 23,613 bytes | Generated build output |
| `services/tenant-organization/generated/` | 27 files / 25,014,483 bytes | Generated Prisma client |
| `packages/*/dist/` | 8 files / 5,466 bytes | Generated package output |
| `tools/governance/__pycache__/` | 1 file / 14,084 bytes | Binary interpreter cache |
| Archives | 0 found | No archive content required inspection |
| `.git/` | Not inventoried | Git metadata is not a migration asset and was not modified |

No first-party source root found in the accessible V2 workspace was silently omitted. The newly verified historical repository is separately bounded in sections 5 and 18.

## 5. V2 repositories, archives, and source roots

### Local workspace

| Root | Observed responsibility | Evidence status |
| --- | --- | --- |
| `apps/bff` | GraphQL composition fixture and health endpoints | Directly Observed |
| `services/tenant-organization` | Tenant-scoped persistence, cache, internal HTTP and messaging fixture | Directly Observed |
| `packages/config` | Typed environment validation and fixture HMAC context | Directly Observed |
| `packages/contracts` | DTO/event envelope types | Directly Observed |
| `packages/observability` | Structured logger redaction and trace-header propagation | Directly Observed |
| `packages/testing` | Stable two-tenant test identifiers | Directly Observed |
| `infra/postgres` | Local database role bootstrap | Directly Observed |
| `test` | Foundation unit/integration regression scenarios | Directly Observed, not executed |
| `.github`, `tools`, `.agents`, `docs` | CI, governance enforcement, instructions, architecture and historical evidence | Directly Observed as artifacts |

### Historical repository referenced by V2

- Repository: `IKAC-FIDS/iam-crm-backend`
- Pinned commit: `9b918ba8972812c129c8b073e1ac4991023ccbbb`
- Indexed paths: 106
- Verified local source: `E:\nodejs\iam-crm-backend`; origin `https://github.com/IKAC-FIDS/iam-crm-backend.git`.
- Provenance: exact commit object and tree verified locally; historical reads used exact-revision Git objects without changing the working tree.
- V3-002A verification result: 106 available indexed bodies, 106 SHA-256 matches, 0 mismatches, 0 missing paths and 0 unverifiable entries. The pinned tree contains 838 files, including 732 outside the historical index. See [the complete matrix](v2-historical-evidence.md#5-106-entry-coverage-and-hash-verification-matrix).
- Remaining evidence: no build/test/CI/runtime/provider/production result was produced or inferred. No network acquisition occurred.

### Archives

No ZIP or other supported archive was found in the bounded first-party discovery set. Nothing was extracted.

## 6. Complete asset inventory and proposed dispositions

Approval values below remain **Proposed** unless a row explicitly records an owner-approved V3-002B decision. No approval is inferred by this assessment.

| Asset ID | Category | Source Path | Responsibility | Dependencies | V3 Mapping | Disposition | Rationale | Evidence | Confidence | ADR / OD Impact | Follow-up | Approval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2-AST-001 | Build/toolchain | Root `package.json`, `pnpm-*`, `turbo.json`, TypeScript/Jest/ESLint configs | Monorepo build, dependency and check orchestration | Node, pnpm, Turbo, TypeScript, Jest | Independent V3 service build/test/artifact boundaries | REWRITE | Owner-approved under V3-002B-DEC-056: rewrite reproducible build, dependency locking, gates and independent service build/version/artifact semantics; direct V2 configuration port and historical stack mandates are prohibited. | `package.json:1-20`; `pnpm-workspace.yaml`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; build/runtime unverified | ADR-001, ADR-011, ADR-012; OD-002–OD-004, OD-020 | Select build tools, repository/CI/versioning/dependency/generated-code/artifact policies independently | Owner-approved — V3-002B-DEC-056 |
| V2-AST-002 | Application/API | `apps/bff` except `dist` | GraphQL tenant-probe query and dependency health composition | NestJS, Apollo, internal HTTP | Possible client composition boundary | RETAIN | Owner-approved under V3-002B-DEC-083 as read-only Historical API-composition/Discovery Evidence; GraphQL, Apollo, NestJS and the BFF pattern are not approved, and Query Composition remains Candidate Evidence only. | `apps/bff/src/module.ts:9-11`; resolver `:3-6`; `v2-owner-review.md` | Confirmed static evidence; owner final disposition recorded; runtime unverified | ADR-008, ADR-009, ADR-012; OD-007, OD-008 | Independently decide Public API strategy, Client/API boundary and Consumer Contracts; keep Dependency Health Aggregation in Operational Core and prohibit BFF business authority/direct database access | Owner-approved — V3-002B-DEC-083 |
| V2-AST-003 | API/security behavior | `apps/bff/src/transport/depth-limit.ts` | Bounds expanded GraphQL fields/depth | GraphQL AST | Generic resource-exhaustion/query-budget evidence if a composable-query technology is selected | RETAIN | Owner-approved under V3-002B-DEC-058 as read-only Historical Security/Performance Evidence; GraphQL AST code, thresholds and configuration are not inherited, and non-selection of GraphQL creates no implementation obligation. | `depth-limit.ts:3-25`; integration test `:198-202`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime protection unverified | ADR-008, ADR-012; OD-007, OD-020 | Independently design complexity/resource budgets, policy and acceptance criteria where applicable | Owner-approved — V3-002B-DEC-058 |
| V2-AST-004 | Security/integration fixture | BFF HTTP client plus `signed-context.guard.ts` | HMAC-signed service/tenant/actor test context | Shared secret, headers, clock | Identity Trust ownership approved under V3-002B-DEC-053; workload identity and validated Tenant Context design pending | REWRITE | Owner-approved under V3-002B-DEC-055: rewrite workload identity/context validation and negative cases; historical HMAC/shared-secret fixture and direct/one-to-one source port are prohibited. | client `:8-15`; guard `:2`; config `:16,22-29`; `v2-owner-review.md` | Confirmed static evidence; owner ownership/disposition recorded; runtime unverified | ADR-003, ADR-005; OD-009–OD-012 | Independently define workload identity protocol and re-prove security behavior | Owner-approved — V3-002B-DEC-055 |
| V2-AST-005 | Service/module | `services/tenant-organization` source shell | Internal endpoint, application service, persistence/cache/message adapters | NestJS, Prisma, Redis, RabbitMQ | Tenant Management logical/data ownership approved under V3-002B-DEC-054; deployment/design undecided | REWRITE | Owner-approved under V3-002B-DEC-055: rewrite Tenant/Organization/Membership under DEC-054; historical framework, adapters, layout and topology are not inherited. | `src/module.ts:1-2`; controller `:1-2`; `v2-owner-review.md` | Confirmed static evidence; owner ownership/disposition recorded; runtime unverified | ADR-001, ADR-002, ADR-005, ADR-011 | Define requirements, policy, contracts, persistence and topology independently | Owner-approved — V3-002B-DEC-055 |
| V2-AST-006 | Domain/test fixture | `TenantProbe` model/service/query | Synthetic tenant-scoped read/update used to exercise infrastructure | V2-AST-004/011–016 | No product capability; valid isolation/fail-closed scenarios may inform independent V3 tests | RETIRE | Owner-approved under V3-002B-DEC-059: do not recreate TenantProbe as a capability, domain model, API, persistence model or service; keep source and valid scenarios as read-only historical test evidence only. | schema `:11-20`; service `:2`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime behavior unverified | ADR-003, ADR-012 | Independently design acceptance/security tests without inheriting framework, contract, schema or topology | Owner-approved — V3-002B-DEC-059 |
| V2-AST-007 | Contract | `packages/contracts/src/index.ts` | Test principal, tenant-probe DTO and event envelope | TypeScript types | Explicit owned API/event contract semantics | RETAIN | Owner-approved under V3-002B-DEC-060 as read-only Historical Contract Evidence; historical types, DTOs and Event Shape are not V3 contracts, and Tenant Provenance cannot automatically establish trusted context. | `index.ts:1-4`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; contract/runtime behavior unverified | ADR-007, ADR-008, ADR-012; OD-008, OD-020 | Independently approve owner, versioning, context validation, authorization, error/delivery semantics and consumers | Owner-approved — V3-002B-DEC-060 |
| V2-AST-008 | Configuration/security | `packages/config` | Typed environment validation, test-runtime guard and HMAC helpers | Zod, Node crypto | Validated external configuration; Identity Trust ownership approved under V3-002B-DEC-053; tool/trust design pending | REWRITE | Owner-approved under V3-002B-DEC-055: rewrite fail-closed/startup/secret-trust configuration semantics; Zod, Node Crypto, HMAC helpers and historical security mechanisms are not selected. | `src/index.ts:4-17,19-30`; `v2-owner-review.md` | Confirmed static evidence; owner ownership/disposition recorded; runtime unverified | ADR-005, ADR-010; OD-009–OD-012 | Select configuration/security tooling and independently prove failure behavior | Owner-approved — V3-002B-DEC-055 |
| V2-AST-009 | Observability | `packages/observability` | Structured logging redaction and trace propagation | Pino, OpenTelemetry API | Candidate redaction and correlation/trace semantics for independent V3 observability design | RETAIN | Owner-approved under V3-002B-DEC-061 as read-only Historical Observability/Security Evidence; historical tools, fields, configuration and implementation are not inherited, and sensitive/cross-tenant disclosure is prohibited. | `src/index.ts:1-4`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime correctness/security/profile evidence unverified | ADR-010, ADR-012; OD-023 | Independently define classification, trace trust, tenant context, sampling, cardinality, retention, export/storage and three-profile evidence | Owner-approved — V3-002B-DEC-061 |
| V2-AST-010 | Test support | `packages/testing` | Stable two-tenant fixture identifiers | TypeScript | Cross-tenant negative-test fixture semantics | RETAIN | Owner-approved under V3-002B-DEC-062 as read-only Historical Test-support Evidence; scenarios may inform independent test design, but code, identifiers and structure are not inherited and two tenants do not prove isolation. | `src/index.ts:1`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; tests/runtime/security unverified | ADR-003, ADR-007, ADR-012 | Independently define framework, fixture API, provisioning, cleanup and environment using synthetic isolated data | Owner-approved — V3-002B-DEC-062 |
| V2-AST-011 | Data model | Prisma schema: four models | Tenant probe, outbox, inbox and processed-event persistence | Prisma/PostgreSQL | Service-owned persistence plus reliable messaging records | REWRITE | Owner-approved under V3-002B-DEC-063: rewrite only valid transactional Outbox, idempotent Inbox and processed-event behavior; TenantProbe and historical Prisma/table/index/naming/migration details are excluded. | `schema.prisma:11-53`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; implementation/runtime unverified | ADR-002, ADR-003, ADR-007, ADR-012; OD-013, OD-014 | Independently design physical schema, RLS, idempotency keys, retention, indexes, reconciliation, migration/cutover and tooling per owning Service | Owner-approved — V3-002B-DEC-063 |
| V2-AST-012 | Migration/RLS | Foundation migration | Creates four tables, FORCE RLS, read/write policies, ordinary grants | PostgreSQL roles/current setting | Shared SaaS tenant-isolation test specification | RETAIN | Owner-approved under V3-002B-DEC-064 as read-only Historical Tenant-isolation/RLS Evidence; historical SQL, policy names, settings, grants and table structures cannot be transferred or executed. | migration `:7-18`; integration test `:60-64,114-128`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime isolation/security unverified | ADR-003, ADR-007, ADR-012; OD-013, OD-014 | Independently design and prove per-Service RLS/context integration using real connections, non-bypass roles and invalid-context scenarios | Owner-approved — V3-002B-DEC-064 |
| V2-AST-013 | Infrastructure/security | `infra/postgres/init.sql` | Creates migration/runtime/dispatcher roles | PostgreSQL | Separated database identities | REWRITE | Owner-approved under V3-002B-DEC-065: rewrite per-Service Migration/Runtime and justified Dispatcher/Worker identity separation under least privilege; historical initialization, roles, credentials, ownership and grants are excluded. | `init.sql:1-7`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime security unverified | ADR-007, ADR-010, ADR-012; OD-012–OD-015 | Independently design secret management, role/grant matrix, bootstrap, rotation/revocation and privileged access per profile | Owner-approved — V3-002B-DEC-065 |
| V2-AST-014 | Cache | `cache.service.ts` | Tenant/permission/version-scoped cache-aside, invalidation generation, degraded miss | Redis | Optional justified tenant-safe cache | RETAIN | Owner-approved under V3-002B-DEC-084 as read-only Historical Cache/Security Evidence; Redis, Cache-aside and a general Cache capability are not approved, and candidate behaviors remain non-authoritative. | `cache.service.ts:1-3`; integration tests `:67-73,131-146,204-210`; `v2-owner-review.md` | Confirmed static evidence; owner final disposition recorded; runtime/security unverified | ADR-003, ADR-007, ADR-012 | Any future use requires an independently approved Use Case, Owner, Requirements, Freshness and Failure Policy with fail-closed revocation behavior | Owner-approved — V3-002B-DEC-084 |
| V2-AST-015 | Messaging | Outbox creation, publisher and dispatcher | Atomic outbox row, confirms, mandatory routing and publish marking | PostgreSQL, RabbitMQ | Service-owned event publication | REWRITE | Owner-approved under V3-002B-DEC-067: rewrite valid atomic Outbox, Publisher Confirm, Mandatory Routing and post-confirmation state behavior; direct source port is prohibited and confirm is not consumer success. | service `:2`; `rabbit.ts:25-53`; tests `:85-100,156-161,213-230`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime correctness unverified | ADR-007, ADR-008, ADR-012; OD-008, OD-019, OD-020 | Independently design leasing/concurrency, ordering, retry/DLQ/re-drive, reconciliation, idempotency, contract lifecycle and RabbitMQ topology | Owner-approved — V3-002B-DEC-067 |
| V2-AST-016 | Messaging | Consumer, inbox, retry and DLQ | Durable dedup, ACK-after-effect, bounded retry and redelivery | PostgreSQL, RabbitMQ | Idempotent V3 consumer pattern | REWRITE | Owner-approved under V3-002B-DEC-068: rewrite durable Inbox/deduplication, ACK-after-durable-effect, bounded retry and controlled DLQ semantics; direct source port is prohibited. | `rabbit.ts:56-100`; tests `:103-112,164-196,232-248`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; runtime correctness unverified | ADR-007, ADR-008, ADR-012; OD-008, OD-019, OD-020 | Independently design transaction/idempotency boundaries, retry/error policy, topology, retention, re-drive, reconciliation, ordering and versioning | Owner-approved — V3-002B-DEC-068 |
| V2-AST-017 | Test | `test/unit/config.spec.ts` | Production fixture rejection and signature forgery/expiry cases | Jest | Configuration/trust negative scenarios | RETAIN | Owner-approved under V3-002B-DEC-069 as read-only Historical Security Test Evidence; historical Jest code, fixtures, formats, algorithms and shared-secret mechanism are not inherited. | `config.spec.ts:4-16`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; tests/runtime security unverified | ADR-005, ADR-012; OD-009–OD-012 | Independently design protocol-specific negative tests for invalid context, applicable issuer/audience, expiry, replay and fail-closed configuration | Owner-approved — V3-002B-DEC-069 |
| V2-AST-018 | Test | `test/integration/foundation.integration.spec.ts` | 15 RLS/cache/BFF/messaging failure and recovery scenarios | Testcontainers, PostgreSQL, Redis, RabbitMQ, NestJS | V3 regression scenario catalog | RETAIN | Owner-approved under V3-002B-DEC-070 as a read-only Historical Regression Scenario Catalog; selective use requires approved scope/technology and Requirement/Risk mapping, while historical results provide no runtime/security evidence. | test `:60-248`; `v2-owner-review.md` | Confirmed static source; owner disposition recorded; runtime/security unverified | ADR-003, ADR-005, ADR-007, ADR-008, ADR-012; OD-020 | Independently select and design scenarios; BFF/Cache cases remain conditional; tooling/environment remain unapproved | Owner-approved — V3-002B-DEC-070 |
| V2-AST-019 | Deployment | `Dockerfile`, `docker-compose.yml` | Local build/runtime and PostgreSQL/Redis/RabbitMQ topology | Docker, Node, pnpm | Reference-only local topology concepts | REWRITE | Owner-approved under V3-002B-DEC-071: rewrite only independent Service build/version/artifact/deployment and three-profile verification requirements; historical image, build, Compose, port, volume and credential choices are excluded. | Dockerfile `:1-13`; Compose `:1-108`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; implementation/runtime/readiness unverified | ADR-001, ADR-010, ADR-011, ADR-012; OD-012, OD-015, OD-023 | Independently design orchestration, secrets, registry, network/storage, upgrade/recovery/observability and SLO/RTO/RPO per profile | Owner-approved — V3-002B-DEC-071 |
| V2-AST-020 | CI | `.github/workflows/governance.yml` | Read-only governance/boundary/test/build sequence | GitHub Actions, pnpm, Python | Evidence-gate sequencing and least-privilege CI intent | RETAIN | Owner-approved under V3-002B-DEC-072 as read-only Historical CI/Governance Evidence; workflow, tools, steps and ordering are not inherited and historical execution provides no V3 evidence. | workflow `:1-33`, especially `:13-22`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; pipeline/security unverified | ADR-012; OD-020 | Independently define gate scope/evidence/failure effects, provider, pinning, signing/attestation and branch protection | Owner-approved — V3-002B-DEC-072 |
| V2-AST-021 | CI | `.github/workflows/ci.yml` | Full foundation CI including Docker prerequisite | GitHub Actions, pnpm, Docker, Python | Independent V3 repository CI | REWRITE | Owner-approved under V3-002B-DEC-073: rewrite independent Repository/Service CI, owned gates and traceable artifacts; historical provider, toolchain, prerequisites, floating tags and workflow shape are excluded. | workflow `:1-24`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; pipeline/security/readiness unverified | ADR-001, ADR-010, ADR-012; OD-020 | Independently define provider, triggers/branches, runner isolation, cache, immutable pinning, signing/attestation, secrets and promotion | Owner-approved — V3-002B-DEC-073 |
| V2-AST-022 | Governance | `tools/governance/manifest.json`, validator and tests | Declared contexts/skills/gates and document integrity | Python, JSON | Historical input to V3 governance review | RETAIN | Owner-approved under V3-002B-DEC-085 as read-only Historical Governance Discovery/Provenance; historical Contexts, Skills, Gates, Statuses, Invariants, tools and rules create no V3 authority. | manifest `:1-133`; validator/tests; `v2-owner-review.md` | Confirmed static evidence; owner final disposition recorded; no Gate or Validation passed | ADR-002, ADR-011, ADR-012 | Independently approve each future invariant's authority, scope, failure semantics and approval; preserve current V3 Governance Controls | Owner-approved — V3-002B-DEC-085 |
| V2-AST-023 | Governance/test | Boundary policy/checker and adversarial fixtures | Detect cross-service imports, BFF DB access, dynamic imports and re-export bypass | Node, Dependency Cruiser | V3 boundary-policy regression requirements | RETAIN | Owner-approved under V3-002B-DEC-075 as read-only Historical Boundary-policy/Adversarial-test Evidence; historical checker/tooling is not inherited and static dependency analysis cannot prove database/runtime compliance. | `architecture-boundaries.json`; fixture paths under `tools/governance/fixtures`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; V3 enforcement/security unverified | ADR-001, ADR-002, ADR-011, ADR-012; OD-004, OD-020 | Independently design Java/multi-repository rules, generated-code handling, CI integration and failure policy | Owner-approved — V3-002B-DEC-075 |
| V2-AST-024 | Tooling | Bootstrap/deferred report scripts and typecheck bootstrap | Report missing implementation and make workspace checks addressable | Node/TypeScript | No durable product capability | RETIRE | Owner-approved under V3-002B-DEC-076: V2-stage-specific scripts are not transferred or rewritten; findings remain in inventory/review records and historical source is not physically deleted. | `tools/governance/report-*.cjs`; `typecheck-bootstrap.ts`; `v2-owner-review.md` | Confirmed static evidence; owner disposition recorded; no Gate passed | ADR-012 | Preserve findings only; do not infer product, governance, build or tooling authority | Owner-approved — V3-002B-DEC-076 |
| V2-AST-025 | Documentation | `docs/architecture/*` | V2 baseline, architecture reviews, governance boundary narrative and prior legacy review | V2 ADR corpus | Historical provenance and candidate concepts | RETAIN | Owner-approved under V3-002B-DEC-086 as read-only Historical Architecture/Governance Provenance and Secondary Evidence; retention does not approve content, historical status or readiness claims. | `architecture-baseline.md`; `legacy-review.md`; V3-002A record; `v2-owner-review.md` | Confirmed documents; owner final disposition recorded; historical readiness claims unverified | All ADRs; all relevant ODs | Independently reconcile concepts against V3 authority and record conflicts, gaps and obsolete claims; keep Open Decisions open | Owner-approved — V3-002B-DEC-086 |
| V2-AST-026 | Documentation | `docs/adr/*` | Eleven accepted V2 ADRs and one proposed identity/session ADR | V2 governance | Historical decision provenance | RETAIN | Owner-approved under V3-002B-DEC-087 as read-only Historical Decision Provenance; historical IDs, statuses and approvals do not transfer, and Final Asset Disposition does not complete Concept Reconciliation. | `docs/adr/index.md:1-21`; `v2-owner-review.md` | Confirmed documents; owner final disposition recorded; historical approvals are not V3 authority | ADR-001–ADR-012; OD-002–OD-020 | Independently classify each concept as Covered Evidence, Requires Independent Decision, Non-transferable or Insufficient Evidence without approval/scope change | Owner-approved — V3-002B-DEC-087 |
| V2-AST-027 | Documentation | `docs/engineering/*` | Patterns, quality gates and staged roadmap | V2 stack and V2 ADRs | Candidate acceptance scenarios and evidence vocabulary | RETAIN | Owner-approved under V3-002B-DEC-088 as read-only Historical Engineering/Quality Evidence; the V2 stack, assumptions, gates, roadmap, phase order, priorities and Passed Status do not transfer. | `quality-gates.md:1-60`; roadmap `:1-21`; `v2-owner-review.md` | Confirmed documents; owner final disposition recorded; historical gate/readiness results unverified | ADR-012; OD-020, OD-023 | Use patterns/scenarios only as inputs to independent V3 design; define any future Gate with its own scope, profile, owner, evidence and failure criteria | Owner-approved — V3-002B-DEC-088 |
| V2-AST-028 | Governance/skills | `.agents/skills/*` | Sixteen V2/NestJS-specific agent workflows | V2 AGENTS and stack | None as executable V3 governance | RETIRE | Owner-approved under V3-002B-DEC-080: historical Skills are not transferred, installed, executed or directly rewritten; sources remain read-only and create no V3 governance/tooling authority. | `.agents/skills/*/SKILL.md`; `AGENTS.md:11-34`; `v2-owner-review.md` | Confirmed documents; owner disposition recorded; no Skill executed | Governance baseline | Preserve only as historical evidence without cancelling or passing any V3 control/Gate | Owner-approved — V3-002B-DEC-080 |
| V2-AST-029 | Evidence | `docs/skill-audit/*` excluding legacy evidence | Skill inventory, coverage, dry runs, provenance and validation reports | V2 governance pack | Historical audit provenance | RETAIN | Owner-approved under V3-002B-DEC-081 as read-only Historical Audit Provenance; historical pass/coverage/validation status creates no V3 governance, runtime, security or readiness evidence. | `validation-report.md:1-25`; `coverage-matrix.md`; `v2-owner-review.md` | Confirmed documents; owner disposition recorded; no Validation executed | ADR-012 | Preserve provenance and conflicts only; future Validation requires independent scope/tool/inputs/expected and actual results/evidence | Owner-approved — V3-002B-DEC-081 |
| V2-AST-030 | Evidence | `docs/skill-audit/legacy-evidence.json` plus exact pinned Git tree | Paths and SHA-256 hashes for 106 historical files | Local Git object database | Bounded historical evidence index | RETAIN | Owner-approved under V3-002B-DEC-082 as a read-only Bounded Historical Evidence Index; the historical 106/106 result establishes indexed sample identity only, not inventory completeness, semantics, security, quality or readiness. | JSON metadata and [V3-002A matrix](v2-historical-evidence.md#5-106-entry-coverage-and-hash-verification-matrix); `v2-owner-review.md` | Historical record: 106/106 matches; no verification rerun for DEC-082 | ADR-012 | Preserve Commit/Tree provenance; never treat as a full manifest or authority; future use requires authorized semantic review | Owner-approved — V3-002B-DEC-082 |
| V2-AST-031 | Capability candidate | Pinned `src/auth/`, Identity/session/SSO/passkey source and tests | Credentials, sessions, refresh rotation, tenant switching, Passkeys, OIDC/SAML | NestJS, Prisma, JWT/WebAuthn/provider libraries | Identity Trust logical/data ownership approved under V3-002B-DEC-053; topology/protocol choices undecided | REWRITE | Owner-approved under V3-002B-DEC-055: rewrite valid Identity/session/tenant-switch/passkey/SSO behavior under DEC-053/054 and future requirements; no historical mechanism, provider, cache or topology is approved. | `auth.service.ts:69-209,333-423`; `refresh-token.service.ts:75-203`; `jwt.strategy.ts:41-70`; `passkeys.service.ts:11,28`; `tenant-scoped-sso.spec.ts:62-218`; `v2-owner-review.md` | Confirmed static source; owner ownership/disposition recorded; runtime unverified | ADR-004, ADR-005, ADR-012; OD-009–OD-012 | Define protocols/models/contracts/persistence independently and re-prove security behavior | Owner-approved — V3-002B-DEC-055 |
| V2-AST-032 | Capability candidate | Pinned `src/notification-core/` and notification tests | Templates, policies, schedules, delivery ledger, channels, retry/dedup/audit | Prisma, provider adapters, in-process scheduler/worker | Notification Core + In-App — FIRST_RELEASE; Email/SMS/Push — LATER_RELEASE under V3-002B-DEC-008; Notification logical/data ownership approved under V3-002B-DEC-009; topology undecided | REWRITE | Owner-approved under V3-002B-DEC-010 as a composite Asset Group: rewrite only within approved release scope; direct V2 source transfer prohibited. Producing domains retain business facts/authorization; Delivery Audit is internal to Notification. Provider credentials, contracts, scheduling, aggregate/persistence design and topology remain pending. | `notification-core.service.ts:24-56`; `notification-delivery-dispatcher.service.ts:20-37`; `notification-admin.service.ts:38-265`; `v2-owner-review.md` | Confirmed static source; runtime unverified; owner scope/ownership/disposition recorded | ADR-001–ADR-003, ADR-005, ADR-007, ADR-008, ADR-010–ADR-012 | Decide credentials, contracts, scheduling, aggregate/persistence design, providers and topology; re-prove behavior | Owner-approved — V3-002B-DEC-010 |
| V2-AST-033 | Capability candidate | Pinned company registry/Linka adapter and prior documentation | Normalize registration lookup into reviewed draft/provenance | External provider contract | Linka/External Registry — LATER_RELEASE under V3-002B-DEC-024; split ownership under V3-002B-DEC-025; disposition under V3-002B-DEC-026 | REWRITE | Rewrite valid behavior only after later-release requirements and Provider Contract/Retention/Security/Data Protection/Resilience approval. No direct source transfer, historical Provider adoption, implementation start or FIRST_RELEASE inclusion is authorized. | `src/companies/company-registry-lookup.service.ts`; `src/companies/companies.controller.ts:89-104`; `v2-owner-review.md` | Partial confirmed source; owner decisions recorded; provider/runtime unverified | ADR-001–ADR-003, ADR-005, ADR-008, ADR-010–ADR-012; OD-020 | Obtain approved provider requirements and resolve remaining design decisions before implementation | Owner-approved — V3-002B-DEC-026 |
| V2-AST-034 | Capability candidate | Pinned `src/crm-assistant/` and `src/reports/` | Permission-aware reads, deterministic reports, proposals and confirmed actions | CRM modules, model/provider configuration | Reporting decisions under V3-002B-DEC-027–029; AI decisions under V3-002B-DEC-030–032; final reconciliation under V3-002B-DEC-033 | REWRITE | Owner-approved composite disposition preserves Reporting FIRST_RELEASE and AI LATER_RELEASE as independent boundaries. No domain merge, shared database/service, direct source port, implementation start or AI inclusion in FIRST_RELEASE is authorized. | `crm-assistant-tools.service.ts`; `crm-assistant-actions.service.ts`; associated specs; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition decisions recorded; runtime unverified | ADR-001–ADR-005, ADR-008, ADR-010–ADR-012 | Preserve separate boundaries and resolve remaining report/model/provider/retention/approval/API/persistence/migration/topology questions | Owner-approved — V3-002B-DEC-033 |
| V2-AST-035 | Capability candidate | Pinned `src/customer-requests/`, `src/audit-log/`, `src/quota/`, `src/entitlements/` | Workflow/history, scoped audit/retention, quota reservation/reconciliation and entitlement evaluation | Shared Prisma schema and cross-module services | Customer Requests/Audit decisions approved under V3-002B-DEC-011–016; Entitlement under V3-002B-DEC-017–019; Quota under V3-002B-DEC-020–022; final reconciliation under V3-002B-DEC-023 | REWRITE | Owner-approved composite disposition reconciles four component rewrites. Composite grouping is historical traceability only; it authorizes no domain merge, shared database, single microservice or direct V2 source port. | `customer-requests.service.ts`; `customer-request-lifecycle.ts`; `audit-log.service.ts:51-169`; `quota.service.ts`; `entitlement.service.ts`; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition decisions recorded; runtime unverified | ADR-002, ADR-003, ADR-005, ADR-007, ADR-008, ADR-010–ADR-012 | Preserve component boundaries and resolve remaining policy/design/API/persistence/migration/topology questions separately | Owner-approved — V3-002B-DEC-023 |
| V2-AST-036 | Capability map | V2 baseline plus complete pinned historical tree | CRM/Sales/Work/Portal/File/Knowledge capability coverage map | 838-file monolithic repository | Historical capability and evidence traceability map only | RETAIN | Owner-approved under V3-002B-DEC-052 as a read-only map for discovery, coverage, evidence mapping and traceability. It grants no product/domain/service/topology authority; source port and folder-to-service inference are prohibited. | Exact tree enumeration; `src/` capability roots; `architecture-baseline.md:7-23`; `v2-owner-review.md` | Confirmed tree/capability presence; owner disposition recorded | ADR-002, ADR-006, ADR-009, ADR-011; OD-017–OD-019 | Maintain explicit asset-to-approved-capability traceability and flag incomplete/overlapping/contradictory evidence | Owner-approved — V3-002B-DEC-052 |
| V2-AST-037 | Historical business source | Pinned `src/companies/`, `people/`, contacts/socials/branches/industries/lookups | Customer/company/person master data and relationships | Shared Prisma schema, tenant context, audit | Customer Domain — logical/data ownership approved by V3-002B-DEC-002; Service Topology undecided | REWRITE | Owner-approved under V3-002B-DEC-003: preserve validated Customer/CRM business behavior through a new architecture-compliant V3 implementation; direct V2 source transfer is prohibited. FIRST_RELEASE scope is V3-002B-DEC-001. Aggregate/API/Migration/Topology remain separate. | `src/companies/companies.service.ts`; `src/people/people.service.ts`; related controllers/tests; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition recorded | ADR-001–ADR-003, ADR-005, ADR-008, ADR-011 | Define aggregate rules, identity rules and migration scope; topology remains separate | Owner-approved — V3-002B-DEC-003 |
| V2-AST-038 | Historical business source | Pinned `src/opportunities/`, `product-catalog/`, `lead-sources/`, `pain-points/`, `use-cases/` | Sales pipeline/opportunity and product/reference behavior | Customer data, shared Prisma schema | Sales Opportunity/Pipeline core — FIRST_RELEASE under V3-002B-DEC-004 and Sales Domain ownership under V3-002B-DEC-006; four auxiliary capabilities — LATER_RELEASE under V3-002B-DEC-005; Product Catalog ownership/topology undecided | REWRITE | Owner-approved under V3-002B-DEC-007 as a composite Asset Group: rewrite valid behaviors only in their approved release scope; direct V2 source transfer is prohibited. FIRST_RELEASE amount/currency must not require Product Catalog. Auxiliary ownership and Line Item/Pricing/Currency/Aggregate/API/Migration/Topology remain pending. | `src/opportunities/`; `src/product-catalog/`; `v2-owner-review.md` | Confirmed static source; owner scope/core-ownership/disposition recorded | ADR-001–ADR-003, ADR-005, ADR-008, ADR-011 | Decide Product Catalog ownership and detailed Sales design requirements separately | Owner-approved — V3-002B-DEC-007 |
| V2-AST-039 | Historical business source | Pinned `src/tasks/`, `meetings/`, `timesheets/`, `activities/`, `collaboration/`, `personal-todos/` | Work planning, activity, meeting and collaboration workflows | Users/teams/customer/sales, shared schema | Work Core scope/ownership approved under V3-002B-DEC-034–035; final scope-aware disposition under V3-002B-DEC-036 | REWRITE | Rewrite Task Core in FIRST_RELEASE; auxiliary capabilities only after separate requirements/ownership approval. Direct source port, domain merge, shared database and single-service inference are prohibited. | Corresponding pinned source roots and tests; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition recorded; runtime unverified | ADR-001–ADR-003, ADR-005, ADR-008, ADR-011–ADR-012 | Define Task design and separately decide auxiliary requirements/ownership before their implementation | Owner-approved — V3-002B-DEC-036 |
| V2-AST-040 | Historical business source | Pinned `src/attachments/`, `artifacts/`, `profile-media/` | File metadata, access, attachments and generated artifacts | Object storage/provider config, owning modules | File/Attachment Core — FIRST_RELEASE under V3-002B-DEC-037; split ownership under V3-002B-DEC-038; advanced capabilities — LATER_RELEASE; topology undecided | REWRITE | Owner-approved under V3-002B-DEC-039 as a composite Asset Group: rewrite only within approved release scope; direct source port, architectural merging and authorization by identifier/link/reference are prohibited. Advanced-capability ownership and detailed storage/security/lifecycle design remain pending. | `src/attachments/`; `src/artifacts/`; `test/tenant-scope-enforcement.spec.ts:146-168`; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition recorded; storage runtime unverified | ADR-003, ADR-005, ADR-008, ADR-010–012; OD-017 | Define lifecycle/access/retention, storage abstraction and security design; approve advanced-capability ownership before rewrite | Owner-approved — V3-002B-DEC-039 |
| V2-AST-041 | Historical business source | Pinned `src/technical-center/`, `universities/` | Technical knowledge and university/reference workflows | Shared search/data modules | Technical Knowledge — LATER_RELEASE under V3-002B-DEC-040; Technical Knowledge Domain ownership under V3-002B-DEC-041; topology undecided | REWRITE | Owner-approved under V3-002B-DEC-042 as a composite Asset Group: future rewrite is limited to approved LATER_RELEASE scope; direct source port, FIRST_RELEASE dependency and architectural merging are prohibited. File/resource ownership remains separate; Search Index is non-authoritative; links grant no authority. | `src/technical-center/`; `src/universities/`; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition recorded; runtime unverified | ADR-002, ADR-008; OD-018 | Define requirements and lifecycle/classification/search/access/retention design; OD-018 remains Open | Owner-approved — V3-002B-DEC-042 |
| V2-AST-042 | Historical boundary source | Pinned `src/customer-access/`, `customer-users/`, `portal-auth/`, `account-workspace/` | Customer portal access, users, authentication and workspace | Identity/membership/customer modules | Customer Portal — LATER_RELEASE under V3-002B-DEC-043; split Portal ownership under V3-002B-DEC-044; trust/topology undecided | REWRITE | Owner-approved under V3-002B-DEC-045 as a composite Asset Group: future rewrite is limited to approved LATER_RELEASE scope; direct source port, FIRST_RELEASE dependency and architectural merging are prohibited. Portal state grants no membership, entitlement or business-resource authority. | Corresponding pinned source roots; `v2-owner-review.md` | Confirmed static source; owner scope/ownership/disposition recorded; runtime unverified | ADR-004, ADR-005, ADR-008, ADR-009 | Define external principal, customer/tenant relationship, invitation/session trust, contracts and session design | Owner-approved — V3-002B-DEC-045 |
| V2-AST-043 | Historical data evolution | Pinned `prisma/schema.prisma`, 97 SQL migrations and database utilities | Shared historical schema and incremental data evolution | Prisma/PostgreSQL | Migration discovery input, never V3 schema authority | REWRITE | Owner-approved under V3-002B-DEC-046: read-only historical evidence only. V3 schemas/migrations must be independently designed per domain; direct execution, replay, import or port is prohibited; shared history grants no data authority. | `prisma/schema.prisma`; `prisma/migrations/*/migration.sql`; `v2-owner-review.md` | Confirmed static corpus; owner disposition recorded; execution unverified | ADR-001–ADR-003, ADR-007, ADR-011, ADR-012; OD-013, OD-014 | Independently approve each domain's migration mapping, validation, rollback/cutover and persistence design | Owner-approved — V3-002B-DEC-046 |
| V2-AST-044 | Historical test corpus | Pinned `test/` (126 files) plus colocated specs | Tenant/security/protocol/domain/notification regression scenarios | Jest/NestJS/Prisma and provider mocks | Candidate V3 acceptance/regression evidence | RETAIN | Owner-approved under V3-002B-DEC-047 as read-only Historical Test Evidence only. Scenarios require V3 ADR/scope/ownership/requirements review; direct or one-to-one test port, legacy framework adoption, V2 execution and historical-result validation are prohibited. | `test/tenant-scoped-sso.spec.ts`; `test/tenant-scope-enforcement.spec.ts`; tree count; `v2-owner-review.md` | Confirmed test source; owner disposition recorded; not executed | ADR-003, ADR-005, ADR-007, ADR-008, ADR-012 | Identify incomplete/contradictory evidence and independently design approved V3 acceptance/regression tests | Owner-approved — V3-002B-DEC-047 |
| V2-AST-045 | Historical contracts/docs | Pinned `openapi/`, `docs/`, controllers and DTOs | REST surface, DTOs and design/operational narratives | NestJS decorators, generated/spec tooling | Contract and documentation discovery evidence | RETAIN | Owner-approved under V3-002B-DEC-048 as read-only Historical Contract/Documentation Evidence only. No API shape, compatibility promise, direct source/specification port, code generation or publication as a V3 contract is approved. | `openapi/`; `src/**/dto/`; pinned `docs/`; `v2-owner-review.md` | Confirmed static artifacts; owner disposition recorded | ADR-008, ADR-012; OD-007, OD-008, OD-020 | Identify incomplete/conflicting evidence and establish independently approved V3 contracts and consumer baselines | Owner-approved — V3-002B-DEC-048 |
| V2-AST-046 | Historical platform/admin source | Pinned `src/admin/`, `reports/`, `dashboard/`, `operations/`, `health/`, `import/`, `email/` | Administration, reporting, dashboard, import/email and operational endpoints | Broad shared-domain reads and shared schema | Reporting decisions under V3-002B-DEC-027–029; Operational scope/core ownership under DEC-049–050; deferred capability ownership/topology unresolved | REWRITE | Owner-approved under V3-002B-DEC-051 as a composite Asset Group: rewrite Reporting and Operational Core in FIRST_RELEASE; deferred capabilities only after separate requirements/ownership/authorization. Direct source port, universal Admin authority and architectural merging are prohibited. | Corresponding pinned source roots; `v2-owner-review.md` | Confirmed static source; owner scope/core-ownership/disposition recorded; runtime unverified | ADR-001–ADR-003, ADR-005, ADR-008, ADR-010–ADR-012 | Define deferred ownerships and detailed role/action/contract/observability/persistence/topology design | Owner-approved — V3-002B-DEC-051 |

## 7. Business capabilities and bounded-context candidates

| Capability | Evidence | Observed or reported workflows/entities | Candidate V3 mapping | Key invariant/gap | Status |
| --- | --- | --- | --- | --- | --- |
| Tenant foundation probe | Direct source | Read/update `TenantProbe`; emits changed event | Test-only thin slice, not a product context | Synthetic entity; retire after preserving tests | Confirmed fixture |
| Tenant & Organization | Direct fixture plus pinned historical source/tests and V3-002B owner decision | Membership resolution, RBAC and tenant-context propagation | Tenant Management owns Tenant/Organization/Lifecycle/Membership/Principal association/role assignment; Identity, Entitlement and resource authorization remain separate | Historical layout approves no topology; role/policy, invitation, lifecycle, placement and persistence designs remain open | Confirmed static source; logical/data ownership approved under V3-002B-DEC-054 |
| Identity | Pinned historical source/tests plus V3-002B owner decision | Login/lockout, sessions, refresh rotation, tenant switch, Passkeys, OIDC/SAML | Identity Trust owns principal/credential/authentication/session/revocation state; Tenant, Entitlement, Portal and resource authorization remain separate | Trust/provider/token/session/tenant-switch/Passkey choices open; authentication grants no membership, entitlement or business authorization | Confirmed static source; logical/data ownership approved under V3-002B-DEC-053 |
| Notification | Pinned historical source/tests plus V3-002B owner decisions | Template/rule/policy/schedule, multi-channel delivery, dedup/retry/audit | Notification Domain owns Notification data/resources; Core + In-App is FIRST_RELEASE; Email/SMS/Push are LATER_RELEASE; topology undecided | Provider credentials/contracts, runtime guarantees, scheduling, physical design and disposition unresolved | Confirmed static source; owner scope/ownership approved |
| CRM/Customer | Pinned historical source/tests plus V3-002B owner decisions | Company/person/contact/social/branch/reference relationships and Linka draft | Customer Domain; FIRST_RELEASE scope and logical/data ownership approved, topology undecided | Aggregate rules, migration authority and legacy disposition require separate decisions | Confirmed static source; owner scope/ownership approved |
| External Integration/Linka | Pinned adapter source plus V3-002B owner decisions; provider unavailable | Provider lookup, normalized draft and provenance | LATER_RELEASE; Linka owns pre-acceptance provider/candidate data and Customer owns acceptance/master data | Provider contract, retention, security, resilience and detailed design remain unverified; no direct Customer database access | Product scope/ownership approved; provider/runtime unverified |
| Sales | Pinned historical source plus V3-002B owner decisions | Opportunity/Pipeline core plus Product Catalog, Lead Source, Pain Point and Use Case candidates | Sales Domain owns Opportunity/Pipeline core; core is FIRST_RELEASE; four auxiliary capabilities are LATER_RELEASE; topology undecided | Product Catalog ownership, Line Item/Pricing/Currency rules and disposition require separate decisions | Confirmed static source; owner scope/core ownership approved |
| Work & Collaboration | Pinned historical source plus V3-002B owner decisions | Tasks, meetings, timesheets, activities, todos and collaboration | Work Domain owns FIRST_RELEASE Task; asset is REWRITE; auxiliary capabilities are separately gated LATER_RELEASE | Assignment/links grant no authority; related domains retain facts; no source port or architectural merge | Confirmed static source; Work Core scope/ownership/disposition approved |
| Customer Portal/Requests | Pinned historical source plus V3-002B owner decisions | Internal request core plus Portal access/auth, external users, workspace, submission/sharing and extended workflow/history | Customer Request Domain owns minimal FIRST_RELEASE Request core; Portal Domain owns Portal-specific state; Customer Portal and extended features are LATER_RELEASE; V2-AST-042 is REWRITE | Identity/Tenant/Customer/resource authorities stay separate; Portal cannot authorize domain resources or become a FIRST_RELEASE dependency; external-principal and trust models remain unresolved | Confirmed static source; Request and Portal scope/ownership/disposition decisions approved |
| Content & File | Pinned historical source/tests plus V3-002B owner decisions | File metadata, controlled upload/download, base lifecycle and contract-based attachments; advanced file capabilities deferred | File Domain owns file state; each resource owner owns attachment semantics/relations; Core is FIRST_RELEASE, advanced capabilities are LATER_RELEASE and V2-AST-040 is REWRITE | Dual authorization, multiple-link safety and lifecycle separation required; Storage OD-017, scanning, access and retention design open; no mandatory external provider in any production profile | Confirmed static source; product scope/ownership/disposition approved under V3-002B-DEC-037–039 |
| Technical Knowledge | Pinned historical source plus V3-002B owner decisions | Technical Documents/Articles, Basic Classification, contract links and University Reference Data | Technical Knowledge Domain ownership; LATER_RELEASE; V2-AST-041 is REWRITE; FIRST_RELEASE and File Core remain independent | Resource/File ownership retained; links grant no authority; Search Index is non-authoritative; detailed design needs approval; OD-018 remains Open | Confirmed source presence; product scope/ownership/disposition approved under V3-002B-DEC-040–042 |
| Reporting | Pinned historical source plus V3-002B owner decisions | Deterministic reports and base filtering | Reporting owns report metadata/execution/artifacts/authorized projections; Core is FIRST_RELEASE, advanced reporting is LATER_RELEASE and historical Reporting components are REWRITE | Producers retain facts/disclosure contracts; each Report Set needs approval; no direct source port, authorization bypass or cross-service database access | Confirmed static source; scope/ownership/component dispositions approved |
| AI | Pinned historical source/tests plus V3-002B owner decisions | Permission-aware tools, proposals/actions and candidate generated insights | LATER_RELEASE with staged entry; AI owns interaction/proposal/replay state; historical AI component is REWRITE | Approval Reference is not authority; no direct source port/database access/autonomous writes; target domains retain facts/writes; detailed design unresolved | Confirmed static source; scope/ownership/component disposition approved, runtime unverified |
| Platform Operations | Pinned historical source plus V3-002B owner decisions | Audit, entitlement/quota, admin/report/import/email/health | Audit, Entitlement and Quota remain separate; Operational Platform owns Operational Core state; V2-AST-046 is scope-aware REWRITE; advanced Administration/Operations are LATER_RELEASE with deferred ownerships | No Business Fact/universal Authorization ownership; privileged actions require destination authorization/Audit; Dedicated Sovereign authority local; no direct source port/database access | Confirmed static source; scope/core-ownership/disposition approved, detailed design open |
| BFF/API composition | Direct fixture plus V2 ADR | One GraphQL query composed over internal HTTP | Client/API boundary only if OD-007 approves | No direct DB; final authorization still required in owner | Confirmed fixture, V3 decision open |

These are logical capability candidates only. This assessment does not approve bounded contexts, microservice count, co-deployment topology, or aggregate ownership.

## 8. Data models, migrations, and tenant isolation

### Directly observed model

- `TenantProbe`: globally keyed UUID, explicit `tenant_id`, value, cache version, timestamps; only a tenant index is present (`schema.prisma:11-20`).
- `Outbox`: tenant, event type/payload/correlation, attempt/publication timing (`schema.prisma:23-35`).
- `Inbox`: composite consumer/event identity plus tenant and processed time (`schema.prisma:38-45`).
- `ProcessedEvent`: event identity, tenant, type and processed time (`schema.prisma:48-54`).
- No foreign keys, seed files, business aggregates, cross-service schemas, or data migration scripts were found.

### Isolation controls observed statically

- RLS is enabled and forced on all four tables; tenant policies use transaction-local `current_setting('app.tenant_id', true)` with both `USING` and `WITH CHECK` (`migration.sql:7-16`).
- Runtime and dispatcher roles are distinct from the migration role (`infra/postgres/init.sql:1-7`).
- `PrismaService.withTenant` rejects missing context and sets `app.tenant_id` within the same transaction/connection (`prisma.service.ts:1-2`).
- The integration source includes two-tenant, missing/invalid context, rollback, single-connection reuse, and role-flag checks (`foundation.integration.spec.ts:60-64,114-128`). These tests were not run.

### Gaps and incompatibilities

- `TenantProbe.id` is globally unique rather than tenant-compound; this may be valid for globally generated IDs but is not evidence of general tenant-scoped uniqueness design.
- Dispatcher policies allow cross-tenant `SELECT`/`UPDATE` on all outbox rows (`migration.sql:11-12`). A V3 dispatcher may need such access, but identity, least privilege, audit, partitioning, and compromise impact require explicit design.
- The migration has no observed rollback/forward-recovery companion, upgrade path, data backfill, retention cleanup, or schema-compatibility evidence.
- Prisma and its migration mechanism are not V3 selections; OD-013 and OD-014 remain open.
- No production schema/data was available, so data volume, referential integrity, duplicate identity, retention, sensitive-data classification, and migration complexity are unverified.

## 9. Authentication, authorization, and security

### Directly observed

- Local/test requests use a shared HMAC secret over service, tenant, actor, permission version, timestamp, nonce and correlation context (`packages/config/src/index.ts:19-24`).
- The guard requires service name `bff`, non-empty tenant/actor and a valid signature, and explicitly rejects production or disabled-fixture execution (`signed-context.guard.ts:2`).
- The BFF ignores caller-supplied tenant headers and constructs its test tenant/actor from environment settings (`tenant-http.client.ts:8-13`; integration test `:149-154`).
- In the verified historical source, JWT audience/expiry checks, active-membership re-resolution, sessions, refresh-token hashing/rotation/revocation, tenant switching, OIDC, SAML, Passkeys, permissions, quota and entitlements are present (`src/auth/jwt.strategy.ts:41-70`; `auth.service.ts:69-209,333-423`; `refresh-token.service.ts:75-203`). This is static evidence only; issuer/algorithm pinning is not visible in the inspected JWT strategy and Passkey challenges use process-local state.
- The tenant-probe service relies on signed context plus RLS. It does not implement a business resource/action authorization rule (`tenant-probe.service.ts:2`). This is acceptable only as a fixture and must not be copied as production authorization.

### Secret handling observation

`docker-compose.yml` and `infra/postgres/init.sql` contain explicit local-development passwords and a local fixture HMAC secret (`docker-compose.yml:7,29,40,49-50,68,88-89,101-102`; `init.sql:1,4-5`). They were not treated as live credentials and are not reproduced in this inventory. Their presence is direct evidence that the deployment files are development fixtures and must be rewritten rather than reused for any V3 profile.

### Historical-source security evidence

The 106 indexed bodies and broader pinned tree confirm the authentication, session, SSO and tenant-scope implementations previously known only through documentation. Source tests cover tenant-scoped provider non-enumeration, unsafe OIDC URL denial, nonce/PKCE/provider binding and cross-tenant request denial (`test/tenant-scoped-sso.spec.ts:62-218`; `test/tenant-scope-enforcement.spec.ts:25-229`). They were not executed, and static inspection does not prove cryptographic configuration, provider interoperability, runtime isolation or exploitability.

## 10. APIs, events, and external integrations

### APIs

- GraphQL: one `tenantProbe(id)` query with an auto-generated schema and field/depth budget (`tenant-probe.resolver.ts:3-6`; `module.ts:9-11`). No checked-in GraphQL schema or released compatibility baseline was found.
- Internal HTTP: `GET /internal/tenant-probes/:id`, guarded by signed fixture context (`tenant-probe.controller.ts:1-2`). No OpenAPI document was found.
- Health: liveness/readiness endpoints in BFF and service. The service readiness checks PostgreSQL and reports Redis as `up` or `degraded` (`health.controller.ts`).
- The verified historical repository contains a broad REST/controller/DTO surface and an `openapi/` artifact. It is contract-discovery evidence only; no released V3 baseline, compatibility result, provider contract or frontend contract is established.

### Events and jobs

- One event name is defined: `foundation.tenant-probe.changed.v1` (`packages/contracts/src/index.ts:3-4`).
- Producer creates the outbox row in the tenant transaction; dispatcher uses publisher confirms and mandatory routing; consumer validates a limited envelope, uses an advisory lock and inbox, ACKs after durable handling, retries three local fixture delays, then sends to a DLQ (`rabbit.ts:25-100`).
- The dispatcher is a continuous one-second polling loop (`dispatcher-main.ts:5-18`), not evidence of an approved scheduler design.
- The historical source contains notification event/idempotency/delivery processing, but no finding in this task closes V3 event-versioning, broker, scheduling, re-drive, retention or provider decisions.

GraphQL/REST strategy, version mechanics, event tooling and scheduling remain OD-007, OD-008, OD-019 and OD-020. The V2 choices do not close them.

## 11. CI/CD, tests, fixtures, and operational assets

### CI and build

- `governance.yml` uses read-only contents permission, a commit-pinned checkout action, disabled persisted credentials, locked install, governance/boundary checks, tests, build and integration-stage commands. This is observed configuration, not an observed successful run.
- `ci.yml` invokes Docker, locked install, Prisma generation and the root `ci` script, but uses tag-based action references and shares the V2 workspace pipeline.
- Root scripts chain governance, boundary fixtures, lint, typecheck, build, unit and integration commands (`package.json:9-20`). None was executed here.

### Test source

- 2 unit cases: production fixture rejection; signature forgery/expiry rejection.
- 15 integration cases: RLS read/write isolation; cache stale-fill protection; BFF signed-context path; outbox confirm/idempotency; poison retry/DLQ; missing/invalid tenant context and pooled reuse; cache tenant/permission/expiry/reorder isolation; unsigned/forged tenant denial; unroutable publication; lost ACK; consumer crash; GraphQL budget; Redis outage; crash after confirm; persistent delivery across broker restart.
- The pinned historical repository adds 126 files under `test/` plus colocated specs. Representative tests cover tenant-scoped SSO, refresh reuse, JWT tenant context, domain authorization, cross-tenant CRUD/storage denial, notifications and business workflows.
- These are valuable regression scenarios but remain unexecuted source, not evidence that V2 or V3 controls work.

### Operational gaps

- Compose supplies local PostgreSQL, Redis, RabbitMQ, migrate, tenant, BFF, dispatcher and consumer containers. It is not a Shared SaaS, Dedicated Managed, or Dedicated Sovereign implementation.
- No backup/restore procedure, disaster recovery evidence, rollback runbook, artifact signing/SBOM, production secrets flow, SLO/RTO/RPO, capacity evidence, Sovereign-local authority, upgrade skew, or support-access model was found.

## 12. Retain / Rewrite / Retire / Needs Review analysis

### RETAIN — 20

Retain semantics and evidence from query bounding, owned/versioned envelope concepts, structured redaction/correlation, two-tenant fixtures, RLS/non-bypass scenarios, regression cases, governance CI intent, boundary adversarial cases, skill-audit provenance, the verified historical index and capability map, historical test corpus and contract/document corpus. The historical API-composition, Cache/security, Governance, Architecture, ADR and Engineering/Quality assets are also retained strictly as read-only evidence under DEC-083 through DEC-088. No source-copy, technology, authority, approval, Passed Gate or readiness claim is implied.

### REWRITE — 23

Rewrite the original implementation groups plus verified historical Identity, Notification, CRM master data, Sales, Work/Collaboration, Content/File, Portal and Administration/Reporting semantics in the approved V3 stack and explicit owner boundaries. V2-AST-034 and V2-AST-035 are owner-approved as traceability-only composites whose logical boundaries remain separate; V2-AST-033 is owner-approved only for its conditional LATER_RELEASE scope.

### RETIRE — 3

Retire the synthetic TenantProbe as a product asset, V2 bootstrap/deferred reporting glue, and V2-specific agent skills. Their useful evidence is captured here.

### NEEDS_REVIEW — 0

All 46 Asset Groups now have owner-approved Final Dispositions. Concept Reconciliation, Open Decisions, independent architecture review, detailed design and implementation/readiness evidence remain separate and Pending; their pending status does not leave any Asset disposition unresolved.

## 13. Security and architecture findings

| Finding ID | Category / priority | Finding and exact evidence | V3 impact | ADR / OD | Proposed action | Confidence | Owner approval required |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V2-FND-001 | Security / High migration priority | Local Compose/init files embed development database, broker and HMAC credentials (`docker-compose.yml:7,29,40,49-50,68,88-89,101-102`; `init.sql:1,4-5`). No claim is made that they are live secrets. | Copying deployment/configuration would violate V3 secret handling and profile readiness | ADR-004, ADR-010, ADR-012; OD-012, OD-015 | Do not reuse values/files; design external secrets and rotation per profile | Confirmed | Yes, for later secrets design |
| V2-FND-002 | Authorization / High migration priority | Tenant probe checks fixture signature/context but no domain resource/action policy (`signed-context.guard.ts:2`; `tenant-probe.service.ts:2`). | Signed context/RLS alone cannot satisfy domain-owned authorization | ADR-005 | Preserve denial scenarios; implement owner authorization in V3 | Confirmed | Yes, policy semantics |
| V2-FND-003 | Identity / High migration priority | HMAC test principal is explicitly disabled for production (`packages/config/src/index.ts:16,27-30`; client `:8`). | Cannot be treated as user or workload identity solution | ADR-004, ADR-005; OD-009–OD-012 | Replace after identity/workload decisions; no silent selection | Confirmed | Yes |
| V2-FND-004 | Data isolation / Medium | FORCE RLS and transaction-local context are strong candidates, but the dispatcher has all-tenant outbox read/update policies (`migration.sql:7-18`). | Privileged cross-tenant path needs least privilege, audit and compromise analysis | ADR-003, ADR-005, ADR-007 | Retain RLS tests; redesign privileged dispatcher authority | Confirmed | Yes |
| V2-FND-005 | Messaging / Medium | Outbox selection has no observed claim/lease across concurrent dispatchers (`rabbit.ts:43-47`); duplicate publication is therefore possible and must remain safe. | V3 must explicitly support at-least-once, idempotency, reconciliation and concurrency | ADR-007, ADR-008; OD-008, OD-019 | Preserve duplicate/crash tests; design dispatcher concurrency/re-drive | Probable static conclusion | Yes for topology |
| V2-FND-006 | Architecture / High migration priority | V2 uses NestJS/TypeScript/Prisma/pnpm/Turbo and GraphQL BFF (`package.json`; `apps/bff/src/module.ts:9-11`). | Backend stack conflicts with ADR-001; BFF strategy remains open | ADR-001, ADR-008; OD-002–OD-008, OD-013, OD-014 | Rewrite; retain only approved semantics | Confirmed | Yes for open decisions |
| V2-FND-007 | Service autonomy / Medium | One root build/image copies and builds the whole workspace (`Dockerfile:5-13`; `package.json:17-20`). | Does not demonstrate independent V3 service build/version/artifact/release | ADR-001, ADR-011 | Establish independent boundaries in later V3 foundation work | Confirmed | No new decision beyond open build layout |
| V2-FND-008 | Evidence / High | 17 test cases exist, but no tests/builds/CI were run in this task. V2 reports do not establish runtime results. | Cannot claim isolation, security, reliability or readiness | ADR-012 | Treat as future test specifications only | Confirmed | No |
| V2-FND-009 | Evidence coverage / Medium | Exact historical commit is locally verified; 106/106 indexed raw-content SHA-256 values match. The pinned tree has 838 files, so 732 files were outside the curated index and are grouped rather than individually index-hashed ([V3-002A matrix](v2-historical-evidence.md#5-106-entry-coverage-and-hash-verification-matrix)). | Removes the historical-source blocker but does not create runtime or approval evidence | ADR-012 | Preserve exact provenance; treat the index as a verified subset, not a complete manifest | Confirmed | No |
| V2-FND-011 | Identity / High migration priority | JWT strategy visibly checks expiry/audience and active membership but does not visibly pin issuer or an algorithm allowlist (`src/auth/jwt.strategy.ts:41-70`); Passkey challenges use process-local cache (`src/auth/passkeys/passkeys.service.ts:11,28`). | Historical controls must not be copied as V3 production trust | ADR-004, ADR-005, ADR-012; OD-009–OD-012 | Specify issuer/algorithm/key rotation and durable distributed challenge lifecycle before implementation | Probable static finding | Yes |
| V2-FND-012 | Architecture / High migration priority | Historical backend centralizes 542 source files and a shared Prisma schema/migration history in one NestJS repository. | Directory modules do not establish independent V3 service/data ownership | ADR-001, ADR-002, ADR-011; OD-002–OD-006, OD-013, OD-014 | Use business invariants as input; redesign build, runtime and persistence ownership | Confirmed static structure | Yes |
| V2-FND-010 | Operations / High | No production profiles, backup/restore, Sovereign authority, plugin platform or Frontend implementation found. | V2 cannot evidence V3 operational/profile/plugin/frontend readiness | ADR-004, ADR-006, ADR-009, ADR-010, ADR-012; OD-001, OD-015–OD-023 | Address only in later authorized architecture/implementation tasks | Confirmed absence in accessible roots | Yes where ODs apply |

These are migration/architecture findings, not penetration-test results. No exploitability claim is made from static absence alone.

## 14. V3 architectural compatibility assessment

| V3 principle | V2 evidence | Compatibility assessment |
| --- | --- | --- |
| Java/Spring Boot independent microservices | TypeScript/NestJS shared workspace/image | Incompatible implementation; REWRITE. Service autonomy intent is reusable. |
| Strict service/data ownership | One fixture service plus a historical modular monolith with shared Prisma schema | Historical capability modules are confirmed, but implementation is incompatible with independent V3 ownership and must be decomposed by approved boundaries. |
| Cell-based hybrid tenancy | Tenant discriminator/RLS fixture plus historical tenant-context and organization-scoped queries/tests | Useful Shared SaaS requirements; no cell placement, generation, migration or dedicated-profile implementation. |
| Sovereign authority | No local Sovereign control/trust/operations implementation | Not evidenced. |
| Domain-owned authorization | Fixture signed context/RLS plus historical controller permission and domain-service checks | Candidate semantics exist; shared framework rules do not prove complete owner authorization and require V3 redesign/reverification. |
| Plugin extension model | No plugin package/installation/gateway/runtime observed | Not evidenced; do not infer from V2 skills/extensions. |
| Service-owned persistence and messaging | RLS, outbox/inbox, RabbitMQ fixture | Strong semantic alignment; implementation must be rewritten and reverified. |
| Contract compatibility | Version field/event name plus historical controllers/DTOs/OpenAPI | Discovery evidence only; released baseline, coexistence, deprecation and consumer migration are not evidenced. |
| Modular Frontend | No frontend source found | Not evidenced. |
| Operational profiles | Local Compose only | Incompatible as production evidence; no profile-specific proof. |
| Controlled co-deployment | Shared workspace/image without independent artifact proof | Does not establish ADR-011 requirements. |
| Evidence-based readiness | Rich test/gate documentation, no executed evidence here | Good vocabulary/scenario source; no readiness claim. |

No V3 ADR conflict is resolved by this assessment. All OD-001 through OD-023 remain Open.

## 15. Proposed migration sequencing and dependencies

This is a proposed knowledge sequence, not authorization to implement:

1. **Owner disposition review:** approve, reject or revise each of the 46 Asset IDs and select V3 product scope.
2. **Recover remaining knowledge:** obtain authoritative business rules, sanitized provider contracts, production-neutral schemas/data dictionaries and operational runbooks; do not treat historical implementation as product authority.
3. **Preserve specifications:** convert approved RETAIN items into V3-owned behavioral requirements and test scenarios, without copying V2 implementation.
4. **Close blocking decisions only when needed:** OD-002–OD-004 before Backend initialization; OD-007/OD-008/OD-020 before public contracts; OD-009–OD-014 before production identity/tenant persistence; OD-015/OD-023 before deployment/readiness claims.
5. **Design the first V3 thin slice:** use approved logical ownership and independent build/data boundaries; do not assume `tenant-organization` or BFF must be separate deployables solely because V2 used those directories.
6. **Plan data migration separately:** actual production schema, record counts, identifiers, tenant mapping, retention/legal constraints and reconciliation evidence are prerequisites. None is available here.
7. **Execute verification later:** port selected negative/failure cases and produce real build/test/CI/contract evidence only under a task that permits execution.

## 16. Open questions and approval requirements

1. Which of the 46 proposed dispositions does the owner approve, reject or revise?
2. What detailed requirements, ownership and trust model govern the approved LATER_RELEASE Customer Portal scope?
3. Which business rules, contracts, and user-visible workflows are authoritative outside source code?
4. Is any production-neutral database schema/data dictionary available, and what tenant/record volumes, retention and legal constraints apply?
5. Which historical business rules and user-visible behaviors are authoritative beyond the inspected source?
6. What are the intended scope and aggregate owners for entitlement evaluation and quota, and who owns shared external-provider data?
7. Are provider contracts and sanitized fixtures available for Linka, notification channels, OIDC/SAML and other integrations?
8. Are there separate V2 Frontend, plugin, infrastructure, or operational repositories requiring a separately authorized inventory?
9. Blocking V3 choices remain in OD-001 through OD-023; this task closes none of them.

## 17. Future verification requirements

- Reproduce all retained tenant/RLS tests with at least two tenants, missing/invalid context, ordinary non-owner/non-BYPASSRLS roles, pooled connection reuse, reads, writes and constraints.
- Verify resource-owner authorization independently of gateway, identity, membership and RLS.
- Define and test user/workload identity, issuer/audience/client boundaries, revocation, secrets and Sovereign-local trust after decisions are approved.
- Verify API/event compatibility with released baselines, coexistence, deprecation and consumer migration evidence.
- Exercise outbox/inbox duplicates, reorder, crash boundaries, unroutable delivery, retry/DLQ, re-drive, retention and reconciliation.
- Verify cache authorization before hit, tenant/permission/version scoping, stale fill, invalidation races, outage and bounded freshness.
- Obtain actual migration clean-install/upgrade/rollback-or-forward-recovery and data reconciliation evidence.
- Produce independent build/artifact/release evidence per service and operational evidence per Shared SaaS, Dedicated Managed and Dedicated Sovereign profile.
- Verify backup/restore, upgrade/rollback, artifact integrity, observability, privileged audit and local Sovereign authority.
- Review any future legacy source for secrets safely; record locations/categories only and rotate through an authorized security process.

The roadmap phrase `Clean build + automated negative tests + CI logs + contract diff` is a future expectation only. None was performed for V3-002.

## 18. Evidence index and source references

### Direct local source

- Workspace/build: `E:\Neshane-CRM-V2\package.json`, `pnpm-workspace.yaml`, `turbo.json`, `tsconfig.base.json`, Jest/ESLint configs.
- BFF: `apps/bff/src/`.
- Tenant service: `services/tenant-organization/src/`.
- Data: `services/tenant-organization/prisma/schema.prisma` and `prisma/migrations/202610220001_foundation/migration.sql`.
- Packages: `packages/config/src`, `packages/contracts/src`, `packages/observability/src`, `packages/testing/src`.
- Infrastructure: `infra/postgres/init.sql`, root `Dockerfile`, root `docker-compose.yml`.
- Tests: `test/unit/config.spec.ts`, `test/integration/foundation.integration.spec.ts`.
- CI/governance: `.github/workflows/`, `tools/governance/`, `.agents/skills/`.

### Direct local documentation

- V2 baseline and reviews: `docs/architecture/`.
- V2 decisions: `docs/adr/`.
- V2 patterns/gates/roadmap: `docs/engineering/`.
- Audit/provenance: `docs/skill-audit/`.

### Verified historical evidence

- `E:\nodejs\iam-crm-backend` is the verified local repository; exact-revision reads were taken from commit `9b918ba8972812c129c8b073e1ac4991023ccbbb` without checkout.
- `docs/skill-audit/legacy-evidence.json` records the repository, pinned commit and 106 path/hash entries; all 106 match SHA-256 over exact raw blob bytes.
- `migration/v2-historical-evidence.md` records provenance, the complete 106-entry comparison matrix, the 838-file tree summary and static capability findings.
- `docs/architecture/legacy-review.md` remains preserved secondary provenance; direct pinned source now supersedes it where findings overlap.

### V3 authority

- `architecture/baseline-v3.md`
- `architecture/decision-register.md`
- `architecture/open-decisions.md`
- `architecture/adr/README.md` and ADR-V3-001 through ADR-V3-012
- `architecture/legacy-v2-reference.md`
- `architecture/governance-synchronization.md`

## 19. Acceptance coverage matrix

| Requirement | Result | Evidence / limitation |
| --- | --- | --- |
| All accessible first-party V2 asset groups inventoried | Met | Original 126-file workspace plus 838-file pinned historical tree represented by 46 practical asset groups |
| Archive coverage and exclusions explicit | Met | No archives found; dependency/generated/cache exclusions listed with metadata |
| Every inventoried asset has disposition | Met | 46/46 have one proposed disposition and approval state |
| Major business capabilities/integrations mapped | Met for accessible backend source | Direct source used; provider/runtime/product-authority gaps remain explicit |
| Security/tenant risks use evidence or explicit uncertainty | Met | Exact pinned paths/lines; static, probable and unverified claims distinguished |
| V3 mappings do not override approved ADRs | Met | Mappings are candidates; ADR authority and co-deployment rules preserved |
| Open Decisions remain open | Met | OD-001–OD-023 unchanged |
| No V2/runtime source modified or executed | Met | Documentation-only inspection; final manual status check required |
| Future checks separated from performed checks | Met | No executable verification claimed; section 17 lists future evidence |
| Remaining owner approvals listed | Met | Sections 6 and 16 |
| Roadmap: every accessible asset has disposition; no blind source port | Met | Historical source and unindexed tree groups reconciled; no source copied |
| V3-002A historical-source recovery | Complete, pending owner review | Exact commit verified; 106 matches, 0 mismatches, 0 unverifiable; 732 additional tree paths grouped |

## 20. Inventory Review outcome and limitations

**Outcome: Inventory Complete — Owner Disposition Review Complete.**

**V3-002A outcome: Historical Source Verified — Inventory Reconciled.** The original inventory contained 46 Asset Groups with proposed totals of RETAIN 13, REWRITE 19, RETIRE 3 and NEEDS_REVIEW 11. Following the completed V3-002B Owner Disposition Review, the final owner-approved totals are RETAIN 20, REWRITE 23, RETIRE 3 and NEEDS_REVIEW 0.

The accessible V2 workspace and exact pinned historical backend tree have complete bounded asset-group coverage, every indexed historical file is hash-verified, and every inventory group has a proposed disposition. Completion means documentation-level inventory coverage only. Production data, authoritative provider contracts, operational profiles, runtime results, Frontend and plugin implementation remain unavailable or outside scope.

No migration, salvage implementation, V3 foundation work, runtime security verification or production-readiness claim has started. Owner review of Asset dispositions is complete; Concept Reconciliation, Open Decisions, independent architecture review and any implementation require separately authorized work.
