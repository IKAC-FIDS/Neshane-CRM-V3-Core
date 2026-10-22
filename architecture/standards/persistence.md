# Persistence standard

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

Migration tool, schema naming, identifier strategy, retention, backup objectives, and exact RLS session-setting mechanism.

