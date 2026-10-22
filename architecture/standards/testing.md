# Testing standard

## Required coverage by concern

- Domain unit tests cover invariants without Spring or infrastructure.
- Application tests cover use-case orchestration, authorization decisions, transaction intent, and port interactions.
- Adapter tests cover mapping, validation, serialization, persistence queries, and failure translation.
- Contract tests protect versioned APIs and events. Integration tests use real compatible infrastructure when behavior depends on PostgreSQL, RLS, RabbitMQ, or transactions.
- Tenant-aware features require positive and negative tests with at least two tenants, missing/invalid context, cross-tenant identifiers, and ordinary non-bypass database roles.
- Messaging tests cover duplicates, retries, ordering assumptions, crash boundaries, dead-letter behavior, and idempotent effects.
- Security tests cover authentication and authorization denials without disclosing sensitive information.

## Test quality

- Tests are deterministic, isolated, readable, and assert observable behavior rather than implementation detail.
- Do not use production credentials or depend on shared mutable environments.
- A skipped or unexecuted test is not evidence of success. Report exactly what was and was not run.
- Under the root `AGENTS.md`, Codex may write required tests but must never execute tests, builds, containers, or services.

## Proposed choices requiring approval

Test libraries, container strategy, coverage thresholds, contract tooling, performance budgets, and CI quality gates.

