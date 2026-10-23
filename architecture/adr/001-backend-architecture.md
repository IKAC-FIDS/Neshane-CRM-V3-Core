# ADR-V3-001: Java/Spring Boot independent microservices

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-001
- Decision approval: Explicit project-owner decision recorded in Task R0-001
- Documentation formalization: Codex under Task R0-001
- Independent reviewer sign-off: Not recorded
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Neshane needs business-service autonomy without a shared release train or infrastructure-coupled domain model.

## Decision

Use Java and Spring Boot independent microservices guided by DDD and Hexagonal Architecture. Domain logic remains independent of Spring and infrastructure. Each defined Business Service has its own build, test boundary, version, artifact, deployment and lifecycle; releasing one service must not require rebuilding another Business Service. Common engineering standards and narrow technical/contract libraries are permitted only when they preserve that independence.

## Alternatives

A shared application/monolith or a mandatory multi-service release unit was rejected because it couples ownership and deployment. Exact versions and build structure remain OD-002–OD-004.

## Consequences

Service autonomy increases contract, compatibility and operational work. Co-deployment may be used under ADR-V3-011 but cannot erase independent service boundaries.

## Verification expectations

Later evidence must demonstrate independent builds/tests/artifacts/releases and enforce dependency direction. This ADR records architecture only; no implementation evidence exists.

## Traceability

Related: V3-001 §4.1; R0-001 decision 1; DEC-001; OD-002–OD-004; ADR-V3-002; ADR-V3-011; ADR-V3-012.

