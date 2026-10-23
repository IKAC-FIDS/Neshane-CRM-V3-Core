# ADR-V3-007: Service-owned persistence and reliable messaging

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-007
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Tenant isolation, service autonomy and recoverable integration require explicit persistence and delivery ownership.

## Decision

PostgreSQL is the primary relational store. Services use logical or physical persistence isolation with independent ownership, roles, credentials and migrations; cross-service SQL is prohibited. Shared tenant-aware tables use validated Tenant Context, owner authorization and PostgreSQL RLS with runtime identities unable to bypass tenant protection. RabbitMQ is the asynchronous baseline; reliable domain-event flows use transactional Outbox and idempotent Inbox patterns. Redis is allowed only for justified, tenant-safe use cases with defined freshness and failure behavior.

## Alternatives

Shared schemas, application filters alone and uncoordinated database/broker dual writes were rejected. Migration/RLS mechanisms remain OD-013–OD-014.

## Consequences

At-least-once delivery requires duplicates, retries, dead letters, re-drive and reconciliation. Schema changes preserve isolation and compatibility.

## Verification expectations

Later evidence must use ordinary database roles, multiple tenants, pooled connections and broker failure/duplicate scenarios.

## Traceability

Related: V3-001 §4.6; R0-001 decision 7; DEC-007; OD-008, OD-013, OD-014, OD-020; ADR-V3-002; ADR-V3-003; ADR-V3-008.

