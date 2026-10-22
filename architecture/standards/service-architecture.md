# Service architecture

## Responsibilities

- `domain`: aggregates, value objects, domain events, domain services, and required ports. It is framework-independent.
- `application`: use-case orchestration, commands, queries, application DTOs, transaction intent, and authorization coordination.
- `adapter/in`: REST or messaging entry points. It authenticates/validates boundary input and invokes one application use case.
- `adapter/out`: implementations for persistence, messaging, and integrations.
- `configuration`: Spring wiring and technical configuration only.

## Boundaries

- Each Business Service is independently buildable, deployable, and data-owning.
- Communication crosses service boundaries only through approved, versioned APIs or events.
- A service must enforce its own authorization and tenant rules; an upstream gateway is not sufficient authority.
- Avoid synchronous call chains. The owning service remains the source of truth; projections are read-only and explicitly stale.
- Do not share domain implementations, persistence entities, transactions, or database constraints across services.
- New service boundaries, ownership changes, or communication styles require an approved V3 ADR.

## Use-case flow

An inbound adapter constructs validated input, the application layer establishes the authorized use case and transaction boundary, the domain enforces invariants, and outbound ports perform owned external interactions. Map transport and persistence types at adapter boundaries.

