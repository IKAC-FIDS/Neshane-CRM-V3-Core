# ADR-V3-008: Contract-first controlled compatibility

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-008
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Independent services, Frontend and plugins need stable evolution across deployment profiles and non-simultaneous upgrades.

## Decision

Public/internal APIs and events are owned, explicit and versioned. Contract design precedes implementation. Backward-compatible evolution is preferred. A breaking change requires a new contract version, a defined coexistence window, explicit deprecation, consumer inventory/migration planning and removal criteria. Shared and dedicated profiles preserve compatible business semantics.

## Alternatives

Coordinated big-bang replacement and silent in-place breaking changes were rejected. REST/GraphQL BFF strategy, exact versioning mechanics and tools remain OD-007, OD-008 and OD-020.

## Consequences

Producers may support multiple versions temporarily. Deprecation and consumer migration become release obligations.

## Verification expectations

Later evidence must include compatibility analysis, consumer status and profile-skew/coexistence scenarios before contract removal.

## Traceability

Related: V3-001 §4.6; R0-001 decision 8; DEC-008; OD-007, OD-008, OD-020; ADR-V3-001; ADR-V3-006; ADR-V3-009; ADR-V3-010.

