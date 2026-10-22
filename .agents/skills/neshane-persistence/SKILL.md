---
name: neshane-persistence
description: Implement or review Neshane V3 PostgreSQL ownership, mappings, RLS, transaction boundaries, repositories, and migrations.
---

# Neshane persistence

Apply when a task changes database models, repositories, transactions, PostgreSQL RLS, or migrations.

Read the root `AGENTS.md` plus `architecture/standards/persistence.md`, `security.md`, and `service-architecture.md`. Confirm the owning service and schema. Keep persistence entities inside the outbound adapter, map them to domain types, and prohibit cross-service SQL or shared migrations. For tenant data, carry explicit tenant keys, tenant-scoped constraints, ordinary non-bypass runtime roles, RLS read/write policies, and transaction-local validated context. Keep transactions within one service; coordinate emitted facts through the messaging standard.

Deliver mappings/repository/migration code only when the Task ID requests it, relevant unexecuted isolation and migration tests, recovery/configuration notes, and open database decisions. Never execute migrations, builds, tests, databases, containers, or deployments.

