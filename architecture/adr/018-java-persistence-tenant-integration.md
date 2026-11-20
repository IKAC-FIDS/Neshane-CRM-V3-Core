# ADR-V3-018: Java Persistence and Tenant Transaction Integration

## Decision identity

- Decision: DEC-018
- Resolves: OD-014
- Task: V3-ARCH-OD-013-014
- Architecture revision: NESHANE-V3-ARCH-P00-007
- Status: Owner-approved; pending traceable registration
- Authority: Product Decision Owner / Technical Architecture Owner
- Reviewed Root baseline: 2df1f496b68b0e91a75591a56c5cb8ac4f3204e0
- Decision source: Explicit project conversation approval
- Recording timestamp: 2026-11-20T20:49:45.8881084+03:30
- Independent specialist sign-off: Not recorded

## Context

ADR-V3-007 requires service-owned PostgreSQL persistence,
validated Tenant Context and RLS for shared tenant-aware data.

Existing V3-024 database isolation evidence demonstrates
that uncontrolled pooled PostgreSQL session state may
leak between logical requests.

Raw Hikari SESSION-state leakage remains a recorded failure.

The bounded secured Unit of Work probe is relevant design
evidence, not proof of production runtime isolation.

## Alternatives

Persistence technology:

- Spring JDBC.
- Spring Data JPA / Hibernate.
- jOOQ.
- Unmanaged JDBC.

Tenant transaction integration:

- Implicit transaction interceptors alone.
- Explicit Tenant Unit of Work.
- General connection wrappers.

## Decision

Select the following architecture:

- Spring JDBC with explicit parameterized SQL.
- PostgreSQL JDBC driver.
- Privately controlled HikariCP connection pools.
- Explicit secured Tenant Unit of Work.
- PostgreSQL RLS for applicable tenant-aware tables.
- READ COMMITTED as the initial supported isolation scope.
- Optimistic locking for versioned aggregates.
- Flyway SQL migrations under ADR-V3-017.

Spring Data JPA, Hibernate and jOOQ are not selected as
the initial project persistence baseline.

Alternatives require an approved architecture change.

## Dependency boundaries

Domain remains independent of database and framework technology.

Application defines outbound port contracts.

Outbound persistence adapters implement those contracts
and own database-specific mapping and SQL.

Runtime composition owns framework wiring and configuration.

Persistence adapters shall not import other service implementations
or access databases owned by other services.

## Tenant and Cell isolation

Every applicable persistence operation shall require
validated Tenant Context and authorized Cell placement.

Context must originate from trusted authorization
and placement mechanisms, not arbitrary client selectors.

Untrusted Tenant labels, mutable session settings or
connection-local values alone shall not establish authority.

Mandatory safeguards include:

- Tenant-aware primary, unique and foreign-key constraints.
- Applicable read and write RLS.
- FORCE ROW LEVEL SECURITY where required.
- Ordinary non-owner runtime identities.
- No SUPERUSER or BYPASSRLS runtime privileges.
- No runtime access to migration or administrative roles.
- Explicit database and credential scope.
- Fail-closed behavior for absent or conflicting authority.
- No fallback to another service, Cell or administrator.

Dedicated deployment profiles retain compatible logical
tenant and authorization boundaries.

## Explicit Tenant Unit of Work

The secured Unit of Work owns the transaction and
the lifecycle of the underlying connection lease.

It shall:

1. Obtain an authorized service/Cell database connection.
2. Verify applicable database and principal scope.
3. Establish an explicit transaction.
4. Establish validated transaction-local Tenant Context.
5. Execute bounded repository operations.
6. Complete only through the owning transaction boundary.
7. Roll back incomplete or failed work.
8. Perform verified connection cleanup.
9. Return only a verified clean connection to the pool.
10. Discard or evict unsafe connections.

Repositories shall not bypass the Unit of Work.

Raw Connection, pool and transaction control handles
shall not escape into ordinary business operations.

## Pool hygiene and failure handling

HikariCP shall not be treated as a Tenant Context manager.

Connection hygiene must address arbitrary PostgreSQL
session state and not rely solely on ordinary JDBC resets.

The implementation must verify its cleanup mechanism
against actual PostgreSQL and pooled-connection behavior.

Transaction-local context is mandatory but is not sufficient
by itself to prove authenticated Tenant authority.

Cleanup failure, unknown connection state or failed validation
shall prevent unsafe connection reuse.

Unknown commit outcomes shall not trigger automatic
business-operation replay.

## Transactions and concurrency

Transactions remain within one owning service.

Aggregate updates shall enforce applicable record versions.

Stale versions and conflicting changes shall be rejected
without unauthorized partial effects.

Business changes, owned history and required Outbox records
shall use the applicable atomic transaction boundary.

Cross-service distributed database transactions are prohibited.

## Required runtime verification

Real PostgreSQL verification shall cover:

- Multiple synthetic Tenants.
- Positive and negative access controls.
- Cross-Tenant SELECT, INSERT, UPDATE and DELETE.
- Tenant-key mutation rejection.
- Cross-service and cross-Cell access rejection.
- Role escalation and unauthorized DDL.
- Pooled connection reuse after commit and rollback.
- SQL errors and application exceptions.
- Missing, malformed and spoofed Tenant Context.
- Session-state contamination and cleanup failures.
- Unsafe connection eviction.
- Stale authorization and placement rejection.
- Optimistic locking conflicts.
- Unknown commit outcomes and recovery.
- Applicable V3-024 DB01-DB14 obligations.

Tests must distinguish access denial from connectivity
failure and retain positive controls.

## Consequences

Explicit SQL and the secured transaction boundary improve
visibility of tenant-sensitive database behavior.

This introduces implementation responsibilities for mapping,
SQL correctness, transaction integration, pool hygiene and
negative security verification.

Spring JDBC and HikariCP selection does not approve any
specific unverified implementation.

## Acceptance boundary

This decision establishes an architecture direction only.

Existing V3-024 failures, residual risks and implementation
evidence obligations are preserved.

No production trust mechanism, credential strategy,
runtime Tenant Isolation Gate, security sign-off,
production readiness or deployment is accepted here.

## Related records

- [ADR-V3-005](005-domain-owned-authorization.md)
- [ADR-V3-007](007-data-messaging-baseline.md)
- [ADR-V3-016](016-dedicated-managed-reference-architecture.md)
- [ADR-V3-017](017-postgresql-migration-strategy.md)
- DEC-005
- DEC-007
- OD-012
- OD-013
- OD-014
