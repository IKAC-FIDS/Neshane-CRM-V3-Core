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
| Disposition authority | All dispositions are Codex proposals; none is owner-approved unless explicitly recorded later |
| Runtime evidence | None. No source, build, test, migration, container, database, service, CI, or validator was executed |
| Outcome | **Inventory Complete — Pending Owner Review** |
| V3-002A historical-source outcome | **Historical Source Verified — Inventory Reconciled; Owner Review Pending**; see [historical evidence recovery](v2-historical-evidence.md) |

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

| Proposed disposition | Count |
| --- | ---: |
| RETAIN | 13 |
| REWRITE | 19 |
| RETIRE | 3 |
| NEEDS_REVIEW | 11 |
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

All Approval values below are **Proposed**. Owner approval must be recorded separately.

| Asset ID | Category | Source Path | Responsibility | Dependencies | V3 Mapping | Disposition | Rationale | Evidence | Confidence | ADR / OD Impact | Follow-up | Approval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2-AST-001 | Build/toolchain | Root `package.json`, `pnpm-*`, `turbo.json`, TypeScript/Jest/ESLint configs | Monorepo build, dependency and check orchestration | Node, pnpm, Turbo, TypeScript, Jest | Independent V3 service build/test/artifact boundaries | REWRITE | Preserve reproducibility/check sequencing, not the V2 stack or shared release shape | `package.json:1-20`; `pnpm-workspace.yaml` | Confirmed | ADR-001, ADR-011; OD-002–OD-004, OD-020 | Define V3 build layout only after ODs close | Proposed |
| V2-AST-002 | Application/API | `apps/bff` except `dist` | GraphQL tenant-probe query and dependency health composition | NestJS, Apollo, internal HTTP | Possible client composition boundary | NEEDS_REVIEW | BFF strategy is not inherited; no business UI/API breadth exists | `apps/bff/src/module.ts:9-11`; resolver `:3-6` | Confirmed | ADR-008, ADR-009; OD-007, OD-008 | Decide public API/BFF strategy before reuse | Proposed |
| V2-AST-003 | API/security behavior | `apps/bff/src/transport/depth-limit.ts` | Bounds expanded GraphQL fields/depth | GraphQL AST | Generic query-budget regression requirement if GraphQL is selected | RETAIN | Security/performance invariant is useful; implementation is GraphQL-specific | `depth-limit.ts:3-25`; integration test `:198-202` | Confirmed | ADR-008, ADR-012; OD-007, OD-020 | Translate to selected contract/API stack | Proposed |
| V2-AST-004 | Security/integration fixture | BFF HTTP client plus `signed-context.guard.ts` | HMAC-signed service/tenant/actor test context | Shared secret, headers, clock | Workload identity and validated Tenant Context | REWRITE | Explicitly disabled in production; no approved workload identity, membership or audience model | client `:8-15`; guard `:2`; config `:16,22-29` | Confirmed | ADR-003, ADR-005; OD-009–OD-012 | Preserve negative cases; design approved production trust | Proposed |
| V2-AST-005 | Service/module | `services/tenant-organization` source shell | Internal endpoint, application service, persistence/cache/message adapters | NestJS, Prisma, Redis, RabbitMQ | Platform Core tenant/organization responsibilities, subject to approved boundaries | REWRITE | Capability direction is relevant but framework/layering and fixture scope do not satisfy V3 | `src/module.ts:1-2`; controller `:1-2` | Confirmed | ADR-001, ADR-002, ADR-005, ADR-011 | Owner validates capability boundary; do not infer a deployable split | Proposed |
| V2-AST-006 | Domain/test fixture | `TenantProbe` model/service/query | Synthetic tenant-scoped read/update used to exercise infrastructure | V2-AST-004/011–016 | No product capability | RETIRE | It is a technical probe, not evidenced CRM behavior | schema `:11-20`; service `:2` | Confirmed | ADR-012 | Preserve only its regression scenarios | Proposed |
| V2-AST-007 | Contract | `packages/contracts/src/index.ts` | Test principal, tenant-probe DTO and event envelope | TypeScript types | Explicit owned API/event contract semantics | RETAIN | Envelope ownership/version/tenant/correlation semantics are useful; specific fixture DTO is not | `index.ts:1-4` | Confirmed | ADR-007, ADR-008; OD-008, OD-020 | Redesign language-neutral V3 contracts | Proposed |
| V2-AST-008 | Configuration/security | `packages/config` | Typed environment validation, test-runtime guard and HMAC helpers | Zod, Node crypto | Validated external configuration; future trust adapter | REWRITE | Fail-closed configuration semantics are useful; HMAC fixture is not production identity | `src/index.ts:4-17,19-30` | Confirmed | ADR-005, ADR-010; OD-009–OD-012 | Retain config failure cases; select no tool yet | Proposed |
| V2-AST-009 | Observability | `packages/observability` | Structured logging redaction and trace propagation | Pino, OpenTelemetry API | V3 observability contract | RETAIN | Redaction/correlation semantics align; implementation stack changes | `src/index.ts:1-4` | Confirmed | ADR-010, ADR-012; OD-023 | Define profile-specific evidence and cardinality later | Proposed |
| V2-AST-010 | Test support | `packages/testing` | Stable two-tenant fixture identifiers | TypeScript | Cross-tenant negative-test fixture semantics | RETAIN | Two-tenant testing is explicitly required by V3 | `src/index.ts:1` | Confirmed | ADR-003, ADR-007, ADR-012 | Recreate in chosen V3 test stack | Proposed |
| V2-AST-011 | Data model | Prisma schema: four models | Tenant probe, outbox, inbox and processed-event persistence | Prisma/PostgreSQL | Service-owned persistence plus reliable messaging records | REWRITE | Tables/purposes are useful, but Prisma is not V3 baseline and retention/index/schema rules need design | `schema.prisma:11-53` | Confirmed | ADR-002, ADR-003, ADR-007; OD-013, OD-014 | Define ownership, retention and migration approach | Proposed |
| V2-AST-012 | Migration/RLS | Foundation migration | Creates four tables, FORCE RLS, read/write policies, ordinary grants | PostgreSQL roles/current setting | Shared SaaS tenant-isolation test specification | RETAIN | Strong semantic evidence for RLS and non-bypass testing; SQL is not approved for direct copy | migration `:7-18`; integration test `:60-64,114-128` | Confirmed | ADR-003, ADR-007, ADR-012; OD-013, OD-014 | Re-prove with V3 ordinary roles and chosen integration mechanism | Proposed |
| V2-AST-013 | Infrastructure/security | `infra/postgres/init.sql` | Creates migration/runtime/dispatcher roles | PostgreSQL | Separated database identities | REWRITE | Role separation is valuable; hardcoded credentials/public-schema grants are local-only and unsuitable | `init.sql:1-7` | Confirmed | ADR-007, ADR-010; OD-012–OD-015 | Define secrets, ownership and least privilege per profile | Proposed |
| V2-AST-014 | Cache | `cache.service.ts` | Tenant/permission/version-scoped cache-aside, invalidation generation, degraded miss | Redis | Optional justified tenant-safe cache | NEEDS_REVIEW | Behavior is useful, but Redis adoption is per use case and the domain is only a probe | `cache.service.ts:1-3`; integration tests `:67-73,131-146,204-210` | Confirmed | ADR-003, ADR-007, ADR-012 | Owner/use-case approval; define freshness and security failure policy | Proposed |
| V2-AST-015 | Messaging | Outbox creation, publisher and dispatcher | Atomic outbox row, confirms, mandatory routing and publish marking | PostgreSQL, RabbitMQ | Service-owned event publication | REWRITE | Semantics align, but polling/concurrency/reconciliation/version policy need V3 design | service `:2`; `rabbit.ts:25-53`; tests `:85-100,156-161,213-230` | Confirmed | ADR-007, ADR-008, ADR-012; OD-008, OD-019, OD-020 | Design leasing/concurrency, re-drive and contract lifecycle | Proposed |
| V2-AST-016 | Messaging | Consumer, inbox, retry and DLQ | Durable dedup, ACK-after-effect, bounded retry and redelivery | PostgreSQL, RabbitMQ | Idempotent V3 consumer pattern | REWRITE | Failure semantics are valuable; topology/naming/retention are unresolved | `rabbit.ts:56-100`; tests `:103-112,164-196,232-248` | Confirmed | ADR-007, ADR-008; OD-008, OD-019, OD-020 | Preserve scenarios; approve topology/versioning later | Proposed |
| V2-AST-017 | Test | `test/unit/config.spec.ts` | Production fixture rejection and signature forgery/expiry cases | Jest | Configuration/trust negative scenarios | RETAIN | High-value failure cases; rewrite for approved identity/config stack | `config.spec.ts:4-16` | Confirmed | ADR-005, ADR-012 | Add membership/audience/replay cases later | Proposed |
| V2-AST-018 | Test | `test/integration/foundation.integration.spec.ts` | 15 RLS/cache/BFF/messaging failure and recovery scenarios | Testcontainers, PostgreSQL, Redis, RabbitMQ, NestJS | V3 regression scenario catalog | RETAIN | Strongest reusable artifact, but none of its results were executed in V3-002 | test `:60-248` | Confirmed as source; runtime unverified | ADR-003, ADR-005, ADR-007, ADR-008, ADR-012; OD-020 | Port scenarios selectively and execute only in later authorized tasks | Proposed |
| V2-AST-019 | Deployment | `Dockerfile`, `docker-compose.yml` | Local build/runtime and PostgreSQL/Redis/RabbitMQ topology | Docker, Node, pnpm | Reference-only local topology concepts | REWRITE | Single image/workspace and embedded local credentials do not meet V3 independent artifacts/profiles | Dockerfile `:1-13`; Compose `:1-108` | Confirmed | ADR-001, ADR-010, ADR-011; OD-012, OD-015, OD-023 | Define per-profile deployment only after decisions | Proposed |
| V2-AST-020 | CI | `.github/workflows/governance.yml` | Read-only governance/boundary/test/build sequence | GitHub Actions, pnpm, Python | Evidence-gate sequencing and least-privilege CI intent | RETAIN | Pinned checkout and `persist-credentials:false` are useful supply-chain practices | workflow `:1-33`, especially `:13-22` | Confirmed | ADR-012; OD-020 | Recreate for V3 repositories/toolchains | Proposed |
| V2-AST-021 | CI | `.github/workflows/ci.yml` | Full foundation CI including Docker prerequisite | GitHub Actions, pnpm, Docker, Python | Independent V3 repository CI | REWRITE | Stack-specific and uses floating action tags; not evidence that CI passed | workflow `:1-24` | Confirmed | ADR-001, ADR-010, ADR-012; OD-020 | Pin supply chain and split per independent repository | Proposed |
| V2-AST-022 | Governance | `tools/governance/manifest.json`, validator and tests | Declared contexts/skills/gates and document integrity | Python, JSON | Historical input to V3 governance review | NEEDS_REVIEW | Some invariants align; V2 contexts/statuses are not V3 authority | manifest `:1-133`; validator/tests | Confirmed | ADR-002, ADR-011, ADR-012 | Compare individual invariants, do not import decisions wholesale | Proposed |
| V2-AST-023 | Governance/test | Boundary policy/checker and adversarial fixtures | Detect cross-service imports, BFF DB access, dynamic imports and re-export bypass | Node, Dependency Cruiser | V3 boundary-policy regression requirements | RETAIN | The prohibited dependency scenarios directly align with service ownership | `architecture-boundaries.json`; fixture paths under `tools/governance/fixtures` | Confirmed | ADR-001, ADR-002, ADR-011, ADR-012 | Reimplement for Java/V3 build graph after OD-004 | Proposed |
| V2-AST-024 | Tooling | Bootstrap/deferred report scripts and typecheck bootstrap | Report missing implementation and make workspace checks addressable | Node/TypeScript | No durable product capability | RETIRE | V2-stage-specific reporting glue has no direct V3 migration value | `tools/governance/report-*.cjs`; `typecheck-bootstrap.ts` | Confirmed | ADR-012 | Preserve findings in this inventory only | Proposed |
| V2-AST-025 | Documentation | `docs/architecture/*` | V2 baseline, architecture reviews, governance boundary narrative and prior legacy review | V2 ADR corpus | Historical provenance and candidate concepts | NEEDS_REVIEW | Useful secondary evidence, never V3 authority; direct pinned source now verifies or refines overlapping claims | `architecture-baseline.md`; `legacy-review.md`; V3-002A record | Confirmed as documents | All ADRs; all relevant ODs | Owner reviews candidate concepts individually | Proposed |
| V2-AST-026 | Documentation | `docs/adr/*` | Eleven accepted V2 ADRs and one proposed identity/session ADR | V2 governance | Historical decision provenance | NEEDS_REVIEW | IDs/statuses do not transfer; choices conflict with or remain open in V3 | `docs/adr/index.md:1-21` | Confirmed as documents | ADR-001–ADR-012; OD-002–OD-020 | Map only through approved V3 decisions | Proposed |
| V2-AST-027 | Documentation | `docs/engineering/*` | Patterns, quality gates and staged roadmap | V2 stack and V2 ADRs | Candidate acceptance scenarios and evidence vocabulary | NEEDS_REVIEW | Gates contain valuable tests but also stack/product assumptions | `quality-gates.md:1-60`; roadmap `:1-21` | Confirmed as documents | ADR-012; OD-020, OD-023 | Extract scenarios per later authorized task | Proposed |
| V2-AST-028 | Governance/skills | `.agents/skills/*` | Sixteen V2/NestJS-specific agent workflows | V2 AGENTS and stack | None as executable V3 governance | RETIRE | V3 has synchronized local skills; importing V2 instructions would reintroduce obsolete authority | `.agents/skills/*/SKILL.md`; `AGENTS.md:11-34` | Confirmed | Governance baseline | Keep only as historical evidence | Proposed |
| V2-AST-029 | Evidence | `docs/skill-audit/*` excluding legacy evidence | Skill inventory, coverage, dry runs, provenance and validation reports | V2 governance pack | Historical audit provenance | RETAIN | Useful to explain what V2 claimed and did not prove; not runtime evidence | `validation-report.md:1-25`; `coverage-matrix.md` | Confirmed as documents | ADR-012 | Preserve provenance, not pass statuses | Proposed |
| V2-AST-030 | Evidence | `docs/skill-audit/legacy-evidence.json` plus exact pinned Git tree | Paths and SHA-256 hashes for 106 historical files | Local Git object database | Bounded, reproducible historical evidence index | RETAIN | Establishes exactly what the prior review sampled; all indexed bodies now content-verified | JSON metadata and [V3-002A matrix](v2-historical-evidence.md#5-106-entry-coverage-and-hash-verification-matrix) | Confirmed: 106/106 matches | ADR-012 | Preserve provenance; do not treat the subset as a full manifest | Proposed |
| V2-AST-031 | Capability candidate | Pinned `src/auth/`, Identity/session/SSO/passkey source and tests | Credentials, sessions, refresh rotation, tenant switching, Passkeys, OIDC/SAML | NestJS, Prisma, JWT/WebAuthn/provider libraries | Platform Core Identity Trust candidate | REWRITE | Semantics and negative tests are useful; stack, issuer/algorithm policy, process-local Passkey challenge state and open V3 trust choices prohibit direct reuse | `auth.service.ts:69-209,333-423`; `refresh-token.service.ts:75-203`; `jwt.strategy.ts:41-70`; `passkeys.service.ts:11,28`; `tenant-scoped-sso.spec.ts:62-218` | Confirmed static source; runtime unverified | ADR-004, ADR-005, ADR-012; OD-009–OD-012 | Owner requirements and later security/protocol verification | Proposed |
| V2-AST-032 | Capability candidate | Pinned `src/notification-core/` and notification tests | Templates, policies, schedules, delivery ledger, channels, retry/dedup/audit | Prisma, provider adapters, in-process scheduler/worker | Notification logical Business capability | REWRITE | Preserve state-machine/idempotency scenarios; redesign ownership, contracts, queueing/providers and operations for V3 | `notification-core.service.ts:24-56`; `notification-delivery-dispatcher.service.ts:20-37`; `notification-admin.service.ts:38-265` | Confirmed static source; runtime unverified | ADR-002, ADR-007, ADR-008, ADR-011, ADR-012 | Approve domain ownership and provider contracts; re-prove behavior | Proposed |
| V2-AST-033 | Capability candidate | Pinned company registry/Linka adapter and prior documentation | Normalize registration lookup into reviewed draft/provenance | External provider contract | External integration adapter owned by appropriate V3 capability | NEEDS_REVIEW | Source confirms the adapter shape, but live/sanitized provider contract, retention, resilience and ownership remain unavailable | `src/companies/company-registry-lookup.service.ts`; `src/companies/companies.controller.ts:89-104` | Partial confirmed source; provider unverified | ADR-002, ADR-008; OD-020 | Obtain sanitized contract and retention/ownership decision | Proposed |
| V2-AST-034 | Capability candidate | Pinned `src/crm-assistant/` and `src/reports/` | Permission-aware reads, deterministic reports, proposals and confirmed actions | CRM modules, model/provider configuration | Future AI capability behind owner contracts | NEEDS_REVIEW | Implementation exists, but V3 product scope, models/RAG, approval durability and replay policy are not approved | `crm-assistant-tools.service.ts`; `crm-assistant-actions.service.ts`; associated specs | Confirmed static source; product/runtime unverified | ADR-002, ADR-005, ADR-008, ADR-011, ADR-012 | Owner scope/approval model; later threat, replay and quality review | Proposed |
| V2-AST-035 | Capability candidate | Pinned `src/customer-requests/`, `src/audit-log/`, `src/quota/`, `src/entitlements/` | Workflow/history, scoped audit/retention, quota reservation/reconciliation and entitlement evaluation | Shared Prisma schema and cross-module services | Workflow/Operational Platform/owning-domain candidates | NEEDS_REVIEW | Implementations and invariants are visible, but this combined asset spans unresolved aggregate/policy owners | `customer-requests.service.ts`; `audit-log.service.ts:51-169`; `quota.service.ts`; `entitlement.service.ts` | Confirmed static source; ownership/runtime unverified | ADR-002, ADR-005, ADR-011, ADR-012 | Decide owners; avoid Platform Core business-data or final-domain authorization ownership | Proposed |
| V2-AST-036 | Capability map | V2 baseline plus complete pinned historical tree | CRM/Sales/Work/Portal/File/Knowledge capability coverage map | 838-file monolithic repository | Candidate capability map only | NEEDS_REVIEW | Tree confirms implementations behind the names, but service splits and V3 product scope cannot be inferred | Exact tree enumeration; `src/` capability roots; `architecture-baseline.md:7-23` | Confirmed tree/capability presence | ADR-002, ADR-006, ADR-009, ADR-011; OD-017–OD-019 | Owner scope and bounded-context workshop using specific assets below | Proposed |
| V2-AST-037 | Historical business source | Pinned `src/companies/`, `people/`, contacts/socials/branches/industries/lookups | Customer/company/person master data and relationships | Shared Prisma schema, tenant context, audit | Customer capability candidate | REWRITE | Business semantics are salvage candidates; shared NestJS/Prisma implementation and ownership need V3 redesign | `src/companies/companies.service.ts`; `src/people/people.service.ts`; related controllers/tests | Confirmed static source | ADR-001–ADR-003, ADR-005, ADR-008, ADR-011 | Approve aggregates, identity rules and migration scope | Proposed |
| V2-AST-038 | Historical business source | Pinned `src/opportunities/`, `product-catalog/`, `lead-sources/`, `pain-points/`, `use-cases/` | Sales pipeline/opportunity and product/reference behavior | Customer data, shared Prisma schema | Sales capability candidate | REWRITE | Preserve approved rules, not the monolithic implementation or implicit cross-module ownership | `src/opportunities/`; `src/product-catalog/` | Confirmed static source | ADR-001–ADR-003, ADR-005, ADR-008, ADR-011 | Product-owner rule and aggregate review | Proposed |
| V2-AST-039 | Historical business source | Pinned `src/tasks/`, `meetings/`, `timesheets/`, `activities/`, `collaboration/`, `personal-todos/` | Work planning, activity, meeting and collaboration workflows | Users/teams/customer/sales, shared schema | Workflow/collaboration candidate | REWRITE | Capability is real, but boundaries and cross-domain references require explicit V3 ownership/contracts | Corresponding pinned source roots and tests | Confirmed static source | ADR-001–ADR-003, ADR-005, ADR-008, ADR-011 | Decide whether one or multiple logical owners | Proposed |
| V2-AST-040 | Historical business source | Pinned `src/attachments/`, `artifacts/`, `profile-media/` | File metadata, access, attachments and generated artifacts | Object storage/provider config, owning modules | Content/File capability candidate | REWRITE | Denial-before-storage behavior is useful; storage OD and access/retention contracts remain open | `src/attachments/`; `src/artifacts/`; `test/tenant-scope-enforcement.spec.ts:146-168` | Confirmed static source; storage runtime unverified | ADR-003, ADR-005, ADR-008; OD-017 | Define owner/access/retention and storage abstraction | Proposed |
| V2-AST-041 | Historical business source | Pinned `src/technical-center/`, `universities/` | Technical knowledge and university/reference workflows | Shared search/data modules | Knowledge capability candidate | NEEDS_REVIEW | Source presence is confirmed, but V3 product scope, lifecycle and search/indexing requirements are not | `src/technical-center/`; `src/universities/` | Confirmed static source; scope unapproved | ADR-002, ADR-008; OD-018 | Owner scope and knowledge/search lifecycle decision | Proposed |
| V2-AST-042 | Historical boundary source | Pinned `src/customer-access/`, `customer-users/`, `portal-auth/`, `account-workspace/` | Customer portal access, users, authentication and workspace | Identity/membership/customer modules | Portal frontend/backend boundary candidate | REWRITE | Portal semantics may be retained; trust, API and frontend boundaries require V3 redesign | Corresponding pinned source roots | Confirmed static source | ADR-004, ADR-005, ADR-008, ADR-009 | Define portal principal, tenant and API contracts | Proposed |
| V2-AST-043 | Historical data evolution | Pinned `prisma/schema.prisma`, 97 SQL migrations and database utilities | Shared historical schema and incremental data evolution | Prisma/PostgreSQL | Migration discovery input, never V3 schema authority | REWRITE | Valuable model/history evidence; shared schema and Prisma mechanism do not satisfy independent V3 data ownership | `prisma/schema.prisma`; `prisma/migrations/*/migration.sql` | Confirmed static corpus; execution unverified | ADR-001–ADR-003, ADR-007, ADR-011, ADR-012; OD-013, OD-014 | Derive owner-specific migration/data plans after scope approval | Proposed |
| V2-AST-044 | Historical test corpus | Pinned `test/` (126 files) plus colocated specs | Tenant/security/protocol/domain/notification regression scenarios | Jest/NestJS/Prisma and provider mocks | Candidate V3 acceptance/regression specifications | RETAIN | Scenarios preserve behavior and failure knowledge; no test result or source-copy approval is implied | `test/tenant-scoped-sso.spec.ts`; `test/tenant-scope-enforcement.spec.ts`; tree count | Confirmed test source; not executed | ADR-003, ADR-005, ADR-007, ADR-008, ADR-012 | Select and rewrite approved scenarios in V3 stack | Proposed |
| V2-AST-045 | Historical contracts/docs | Pinned `openapi/`, `docs/`, controllers and DTOs | REST surface, DTOs and design/operational narratives | NestJS decorators, generated/spec tooling | Contract discovery and compatibility input | RETAIN | Preserves consumer vocabulary and candidate contracts; does not approve API shape or compatibility | `openapi/`; `src/**/dto/`; pinned `docs/` | Confirmed static artifacts | ADR-008, ADR-012; OD-007, OD-008, OD-020 | Establish released V3 baselines and consumer review separately | Proposed |
| V2-AST-046 | Historical platform/admin source | Pinned `src/admin/`, `reports/`, `dashboard/`, `operations/`, `health/`, `import/`, `email/` | Administration, reporting, dashboard, import/email and operational endpoints | Broad shared-domain reads and shared schema | Operational/admin capability candidates | REWRITE | Useful behaviors exist, but broad coupling and authority must be decomposed under V3 ownership | Corresponding pinned source roots | Confirmed static source; operational behavior unverified | ADR-001, ADR-002, ADR-005, ADR-008, ADR-010–ADR-012 | Approve read-model/data-access boundaries and operational evidence plan | Proposed |

## 7. Business capabilities and bounded-context candidates

| Capability | Evidence | Observed or reported workflows/entities | Candidate V3 mapping | Key invariant/gap | Status |
| --- | --- | --- | --- | --- | --- |
| Tenant foundation probe | Direct source | Read/update `TenantProbe`; emits changed event | Test-only thin slice, not a product context | Synthetic entity; retire after preserving tests | Confirmed fixture |
| Tenant & Organization | Direct fixture plus pinned historical source/tests | Membership resolution, RBAC and tenant-context propagation | Platform Core Tenant Management and Organization/Membership | Historical shared-module layout does not approve V3 service/data ownership | Confirmed static source |
| Identity | Pinned historical source/tests | Login/lockout, sessions, refresh rotation, tenant switch, Passkeys, OIDC/SAML | Platform Core Identity Trust | Trust/provider choices open; Passkey process-local challenge and JWT policy require redesign/review | Confirmed static source |
| Notification | Pinned historical source/tests | Template/rule/policy/schedule, multi-channel delivery, dedup/retry/audit | Notification logical Business capability | Provider contracts, runtime guarantees and service ownership unresolved | Confirmed static source |
| CRM/Customer | Pinned historical source/tests | Company/person/contact/social/branch/reference relationships and Linka draft | Customer capability candidate | Aggregate and migration authority require owner review | Confirmed static source |
| External Integration/Linka | Pinned adapter source; provider unavailable | Provider lookup, normalized draft and provenance | Adapter boundary owned by relevant V3 capability | Contract, retention and resilience remain unverified | Partially confirmed |
| Sales | Pinned historical source | Opportunity/pipeline/product and sales reference behavior | Sales logical capability candidate | Business rule authority and boundaries require owner review | Confirmed static source |
| Work & Collaboration | Pinned historical source | Tasks, meetings, timesheets, activities, todos and collaboration | Workflow/collaboration candidate | Cross-domain ownership and contracts unresolved | Confirmed static source |
| Customer Portal/Requests | Pinned historical source | Portal access/auth plus request workflow/history | Frontend boundary plus owning-domain workflow | Principal model and aggregate owner unresolved | Confirmed static source |
| Content & File | Pinned historical source/tests | Attachments, artifacts and profile media; denial before storage | Future owned capability | Storage OD-017, access and retention contracts open | Confirmed static source |
| Technical Knowledge | Pinned historical source | Technical-center and university/reference workflows | Future owned capability | Product scope and search/indexing OD-018 open | Confirmed source presence; scope open |
| AI | Pinned historical source/tests | Permission-aware tools, deterministic reports, proposals/actions | Future capability using owner APIs/contracts | Approval/replay, RAG, models and scope unresolved | Confirmed static source |
| Platform Operations | Pinned historical source | Audit, entitlement/quota, admin/report/import/email/health | Operational Platform plus narrow Platform Core policies | Must not become business-data owner or final domain authorizer | Confirmed static source; placement open |
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

### RETAIN — 13

Retain semantics and evidence from query bounding, owned/versioned envelope concepts, structured redaction/correlation, two-tenant fixtures, RLS/non-bypass scenarios, regression cases, governance CI intent, boundary adversarial cases, skill-audit provenance, the verified historical index, historical test corpus and contract/document corpus. No source-copy authorization is implied.

### REWRITE — 19

Rewrite the original ten implementation groups plus verified historical Identity, Notification, CRM master data, Sales, Work/Collaboration, Content/File, Portal and Administration/Reporting semantics in the approved V3 stack and explicit owner boundaries.

### RETIRE — 3

Retire the synthetic TenantProbe as a product asset, V2 bootstrap/deferred reporting glue, and V2-specific agent skills. Their useful evidence is captured here.

### NEEDS_REVIEW — 11

Owner/architecture review is required for the GraphQL BFF, Redis use case, governance manifest importability, V2 architecture/ADR/engineering documents, Linka/provider behavior, AI scope, the combined Customer Request/Audit/Quota/Entitlement ownership group, the broad capability map and Technical Knowledge scope. Open V3 decisions and product authority—not missing historical source—prevent final disposition.

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
2. Which verified V2 capability candidates are in V3 product scope: Notification, Linka/external integration, AI, Customer Requests, Audit, Quota/Entitlement, Content/File, Technical Knowledge, Work/Collaboration, Portal, CRM and Sales?
3. Which business rules, contracts, and user-visible workflows are authoritative outside source code?
4. Is any production-neutral database schema/data dictionary available, and what tenant/record volumes, retention and legal constraints apply?
5. Which historical business rules and user-visible behaviors are authoritative beyond the inspected source?
6. What is the intended aggregate owner for customer requests, entitlement evaluation, quota, audit read models and shared external-provider data?
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

**Outcome: Inventory Complete — Pending Owner Review.**

**V3-002A outcome: Historical Source Verified — Inventory Reconciled; Owner Review Pending.** The inventory now contains 46 asset groups with proposed totals: RETAIN 13, REWRITE 19, RETIRE 3 and NEEDS_REVIEW 11.

The accessible V2 workspace and exact pinned historical backend tree have complete bounded asset-group coverage, every indexed historical file is hash-verified, and every inventory group has a proposed disposition. Completion means documentation-level inventory coverage only. Production data, authoritative provider contracts, operational profiles, runtime results, Frontend and plugin implementation remain unavailable or outside scope.

No migration, salvage implementation, V3 foundation work, owner approval, runtime security verification, or production-readiness claim has started. The next permitted action is project-owner review of the proposed dispositions and remaining evidence gaps; any architecture decision or implementation requires a separately authorized task.
