# Messaging standard

## Event contracts

- Publish facts owned by the producing service; do not publish commands disguised as events.
- Event contracts are namespaced and versioned. Proposed form: `<bounded-context>.<aggregate>.<event>.v<major>`; approve before the first contract.
- Every envelope carries event ID, type/version, occurred-at time, producer, correlation/causation identifiers, and validated tenant provenance when tenant-scoped.
- Minimize payloads and exclude secrets and unnecessary personal data.

## Delivery guarantees

- Use a transactional outbox for database-backed state changes that must emit events.
- Consumers use a durable inbox or equivalent idempotency record before acknowledging completed handling.
- Assume at-least-once delivery and possible reordering; never claim exactly-once effects.
- Acknowledge only after durable processing. Use bounded retries, backoff, dead-letter handling, and an explicit re-drive/reconciliation procedure.
- Preserve correlation and validated tenant/workload context without trusting arbitrary message headers.

## Ownership and evolution

- Consumers must not depend on producer implementation classes.
- Additive compatible changes are preferred. Breaking semantic or structural changes require a new major contract version and a migration plan.
- Queue/exchange naming, retry budgets, ordering needs, retention, schema format, and compatibility tooling require approval per integration.

