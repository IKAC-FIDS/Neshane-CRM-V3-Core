# Messaging standard

## Event contracts

- Publish facts owned by the producing service; do not publish commands disguised as events.
- Event contracts are stable, namespaced and versioned. Event type ends in `.v<major>`; the CloudEvents `specversion`, business-event major, semantic `payloadversion` and immutable schema identity are independent version dimensions under ADR-V3-014.
- Published events use CloudEvents 1.0-compatible envelopes. Every envelope carries event ID, type/version, occurred-at time, producer, correlation/causation identifiers, and validated tenant provenance when tenant-scoped.
- Minimize payloads and exclude secrets and unnecessary personal data.

## Delivery guarantees

- Use a transactional outbox for database-backed state changes that must emit events.
- Consumers use a durable inbox or equivalent idempotency record before acknowledging completed handling.
- Assume at-least-once delivery and possible reordering; never claim exactly-once effects.
- Acknowledge only after durable processing. Use bounded retries, backoff, dead-letter handling, and an explicit re-drive/reconciliation procedure.
- Preserve correlation and validated tenant/workload context without trusting arbitrary message headers.

## Ownership and evolution

- Consumers must not depend on producer implementation classes.
- Additive compatible changes are preferred. Breaking semantic or structural changes require a new major contract version, coexistence, consumer inventory, an accountable migration owner, deprecation/removal criteria and evidence before retirement.
- Unknown or unsupported event/payload versions fail closed. Tenant or producer metadata is provenance, not authentication, membership, entitlement or resource authorization.
- Event contract changes follow ADR-V3-015 layered blocking validation, Provider Conformance, risk-based Consumer-driven/Real Integration Testing, immutable Service Owner baselines, Manual Review and limited time-bound exception rules.
- Queue/exchange naming, retry budgets, ordering needs, retention, production schema-registry use, and specific compatibility/testing products require approval per integration.

