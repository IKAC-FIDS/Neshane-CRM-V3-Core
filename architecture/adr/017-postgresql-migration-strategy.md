# ADR-V3-017: PostgreSQL Migration Strategy

## Decision identity

- Decision: DEC-017
- Resolves: OD-013
- Task: V3-ARCH-OD-013-014
- Architecture revision: NESHANE-V3-ARCH-P00-007
- Status: Owner-approved; pending traceable registration
- Authority: Product Decision Owner / Technical Architecture Owner
- Reviewed Root baseline: 2df1f496b68b0e91a75591a56c5cb8ac4f3204e0
- Decision source: Explicit project conversation approval
- Recording timestamp: 2026-11-20T20:49:45.8881084+03:30
- Independent specialist sign-off: Not recorded

## Context

ADR-V3-007 establishes PostgreSQL and service-owned persistence
as the relational data baseline.

OD-013 requires selection of migration tooling, ownership,
execution and recovery conventions.

## Alternatives

- Flyway SQL-based migrations.
- Liquibase.
- Framework-native schema generation.
- Custom migration tooling.

## Decision

Flyway with versioned SQL migrations is selected as the
standard PostgreSQL migration mechanism for Neshane V3.

Each service owns its database migration artifacts,
schema evolution and compatibility obligations.

PostgreSQL-native SQL is permitted and preferred where
database-specific constraints, RLS or security enforcement
require explicit database behavior.

## Mandatory requirements

1. Migration and runtime identities shall be separate.
2. Runtime services shall not possess unrestricted DDL privileges.
3. Released versioned migrations shall remain immutable.
4. Corrections shall use new reviewed migrations.
5. ORM-generated automatic schema mutation is prohibited.
6. Migration execution shall be separate from ordinary runtime.
7. Migration history and checksums shall be validated.
8. Schema compatibility shall be checked before runtime acceptance.
9. Migration failures shall fail closed.
10. Cross-service database migrations are prohibited.
11. Credentials shall not be stored in migration artifacts.
12. Destructive migration operations require explicit authorization.
13. Flyway clean shall be prohibited for non-disposable environments.

## Ownership and deployment profiles

Migration ownership follows the owning service and its
authorized Cell/database placement.

Shared SaaS, Dedicated Managed and Sovereign deployments
shall preserve service-owned migration responsibility.

A migration shall not implicitly authorize cross-Cell or
cross-service database access.

## Compatibility and recovery

Schema evolution must preserve supported application versions,
tenant isolation and applicable security policies.

Expand/contract evolution is preferred for compatible releases.

Recovery shall use an approved combination of forward
corrections, backup/restore, application rollback and
reconciliation appropriate to the migration.

A successful migration alone does not prove recoverability.

## Verification obligations

- Empty database migration.
- Upgrade from supported schema baselines.
- Repeat execution and checksum validation.
- Migration failure and recovery behavior.
- Migration/runtime role separation.
- Unauthorized DDL rejection.
- Preservation of constraints and RLS.
- Compatibility with supported application releases.

Verification shall use isolated disposable databases.

## Consequences

Flyway becomes the selected migration mechanism after
traceable architecture registration and required propagation.

Exact dependency versions, licensing suitability and
implementation configuration require engineering verification.

## Acceptance boundary

This decision does not authorize production migration,
runtime deployment, security acceptance or risk waiver.

Existing V3-024 conditions and other unresolved decisions
remain applicable.

## Related records

- [ADR-V3-007](007-data-messaging-baseline.md)
- [ADR-V3-016](016-dedicated-managed-reference-architecture.md)
- [ADR-V3-018](018-java-persistence-tenant-integration.md)
- DEC-007
- OD-013
- OD-014
