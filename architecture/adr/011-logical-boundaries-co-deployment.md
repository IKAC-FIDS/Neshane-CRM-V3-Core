# ADR-V3-011: Logical boundaries first with controlled co-deployment

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-011
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

The target architecture has distinct responsibilities, but forcing every logical boundary into a separate initial runtime would add premature operational cost.

## Decision

Define logical ownership and dependency boundaries first. Controlled co-deployment is permitted when ownership, contracts, authorization, data boundaries and prohibited dependencies remain enforceable. Independently defined microservices retain independent build, version and deployment capability even when deployed together. Co-location never permits shared private data or implementation coupling.

## Alternatives

One deployable per logical capability from day one and a permanent shared-schema modular monolith were rejected.

## Consequences

Deployment topology may evolve independently of domain boundaries, but boundary enforcement and extraction readiness require explicit evidence.

## Verification expectations

Later evidence must show independent build/release boundaries, forbidden dependency enforcement and no ownership erosion under co-deployment.

## Traceability

Related: V3-001 §5; R0-001 decision 11; DEC-011; ADR-V3-001; ADR-V3-002; ADR-V3-012.

