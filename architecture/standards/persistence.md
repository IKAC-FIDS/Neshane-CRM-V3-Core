# Persistence standard

<a id="v3-arch-od-013-014-registration"></a>
## P00-007 — Selected persistence architecture

Subject to traceable registration:

- Flyway versioned SQL migrations.
- Spring JDBC and explicit parameterized SQL.
- PostgreSQL JDBC driver.
- Privately controlled HikariCP pools.
- Explicit secured Tenant Unit of Work.
- Transaction-local validated Tenant Context.
- Applicable read/write RLS with non-owner runtime roles.
- Initial READ COMMITTED isolation.
- Optimistic locking for versioned aggregates.
- Atomic owned state, history and required Outbox operations.
- Verified connection cleanup and eviction of unsafe connections.
- Separate migration and runtime identities.
- No automatic ORM schema mutation.
- No raw pool or transaction handles in ordinary business operations.

The application defines the business transaction scope;
the secured Unit of Work owns its technical execution and connection lifecycle.

See [ADR-V3-017](../adr/017-postgresql-migration-strategy.md)
and [ADR-V3-018](../adr/018-java-persistence-tenant-integration.md)
for mandatory requirements and verification boundaries.


## Ownership

- Each service exclusively owns its database schema, credentials, migrations, repositories, and persistence mappings.
- Cross-service SQL, foreign keys, views, entity imports, shared repositories, and direct database access are forbidden.
- Other services obtain data through the owner's versioned API, events, or an explicitly owned projection.
- Persistence entities are adapter types and must not escape as API or domain DTOs.

## PostgreSQL and tenant isolation

- Use `snake_case` for tables, columns, indexes, constraints, and migration identifiers.
- Tenant-owned tables carry an explicit tenant key and tenant-scoped uniqueness/reference rules.
- Use PostgreSQL RLS as defense in depth with both read and write policies; ordinary runtime roles must not own tables or bypass RLS.
- Set validated tenant context transaction-locally on the same connection used for the operation. Missing context fails closed.
- Separate runtime, migration, and privileged identities.

## Transactions and migrations

- Keep transaction boundaries in the application use case; do not span transactions across services.
- Persist state changes and required integration events atomically through an outbox or an approved alternative.
- Migrations are forward-controlled, owned by one service, reviewed for clean install and upgrade, and include a safe rollback or forward-recovery plan.
- Never run migrations automatically from ordinary application startup in production.

## Proposed choices requiring approval

Schema naming, identifier strategy, retention, backup objectives and exact secured Tenant Context integration mechanism remain subject to applicable decisions. Migration tooling and Java persistence architecture are selected under ADR-V3-017 and ADR-V3-018, pending traceable registration.

