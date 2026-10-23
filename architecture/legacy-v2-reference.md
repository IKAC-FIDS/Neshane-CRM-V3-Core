# Legacy V2 reference findings

## Scope and provenance

V2 was available read-only at `E:\Neshane-CRM-V2`. V3-001 directly inspected only these documents:

- `docs/architecture/architecture-baseline.md` — V2 target baseline, status dated 2026-10-19.
- `docs/architecture/legacy-review.md` — a prior report of a focused source inspection at legacy commit `9b918ba8972812c129c8b073e1ac4991023ccbbb`.
- `docs/architecture/principal-architecture-review.md` — V2 documentation review dated 2026-10-20.
- `docs/adr/index.md`, `001-bounded-contexts.md`, `004-database-ownership.md`, `005-tenant-rls.md`, `006-rabbitmq-outbox.md`, `010-ai-approval.md`, and `011-multi-application-platform.md`.

No V2 application source, test, migration, container, provider, or runtime was inspected or executed during V3-001. Statements in V2's `legacy-review.md` about its earlier 106-file source review are secondary documented evidence here; V3-001 did not independently reproduce that source inspection.

## Concepts that may be reused

These V2 documents support concepts consistent with, or useful to refine, approved V3 direction:

- business capability and service-owned data boundaries; no cross-service SQL/ORM coupling;
- validated transaction-local Tenant Context, application authorization, PostgreSQL RLS, tenant-scoped constraints, and non-bypass runtime roles;
- RabbitMQ at-least-once handling, transactional outbox, durable idempotency/inbox, bounded retry, DLQ and reconciliation;
- separation of identity, membership, admission/entitlement and final domain authorization;
- authorization-neutral gateways/BFFs and audience/client distinction;
- scoped cache keys/freshness and fail-safe authorization behavior;
- persistent single-use authorization for AI-initiated mutations rather than process-local nonces;
- provider adapter boundaries, provenance-bearing drafts, notification deduplication/recovery, and domain-owned audit.

Only concepts independently approved in V3-001 are binding. Other items above remain candidates for V3-002 or future ADRs.

## V2 choices not carried into the V3 baseline

V2 history remains unchanged, but the following V2 choices conflict with or are not approved for V3:

- NestJS/TypeScript, pnpm/Turborepo and Prisma are replaced by the approved Java/Spring Boot direction; exact Java build/persistence tooling remains open.
- GraphQL BFF as the principal API is not inherited; public API/BFF strategy is OD-007.
- Docker Compose as the initial deployment target is not inherited; orchestration is OD-015 and must cover three profiles.
- MinIO/S3-compatible storage is not selected; object storage is OD-017.
- V2's shared-SaaS-centered deployment assumptions are insufficient for mandatory Dedicated Managed and Dedicated Sovereign profiles.
- V2 ADR identifiers/statuses remain V2 provenance and are not V3 ADRs.

These are explicit V3 divergences, not edits or invalidations of the historical V2 records.

## Reported V2 risks requiring V3-002 verification

The inspected V2 legacy report describes a broad shared model/process, direct module coupling, process-local permission cache, in-memory AI nonce state, migrations at application startup, default credentials/exposed ports/floating images, and unverified RLS/provider/test behavior. These are reported findings, not independently verified V3-001 source observations.

V3-002 should perform a bounded inventory against the actual available V2 artifacts and verify, with exact file provenance:

- business capabilities, aggregates, state transitions and contract/schema shapes worth preserving;
- tenant keys, constraints, RLS policies, runtime/migration roles and pooled-connection behavior;
- identity/session rotation, revocation, provider federation and permission-cache semantics;
- notification retry/deduplication, outbox/inbox and external-provider ambiguity handling;
- customer request, audit, quota/entitlement, Linka, AI/tool and file behaviors;
- deployment/security defects and test scenarios without copying V2 implementation choices.

## Unverified statements

Production topology, live provider contracts, credentials, data volumes, actual security posture, complete RLS coverage, test pass status, migration correctness, runtime resilience, user-facing behavior, and business-rule completeness remain unverified. V2 is neither a production-readiness certificate nor the implementation foundation for V3.

