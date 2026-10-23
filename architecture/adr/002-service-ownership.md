# ADR-V3-002: Strict service and data ownership

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-002
- Decision approval: Explicit project-owner decision recorded in Task R0-001
- Documentation formalization: Codex under Task R0-001
- Independent reviewer sign-off: Not recorded
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Independent services fail if domain models, migrations or private databases become shared implementation surfaces.

## Decision

Each service exclusively owns its domain model, persistence mappings, schema/logical database, credentials, repositories and migrations. Integration is through owned, versioned contracts. Cross-service SQL, private database access, shared ORM entities, cross-service foreign keys and implementation dependencies are prohibited. Shared libraries may contain limited technical primitives or versioned contract types, never shared business ownership.

## Alternatives

A shared schema/data layer and reusable business-domain library were rejected because they create hidden coupling and coordinated releases.

## Consequences

Cross-service consistency uses APIs, events or owned projections with provenance/freshness. Duplication of representations is acceptable when ownership remains clear.

## Verification expectations

Later evidence must inspect dependencies, database roles/migrations and integration contracts. No source or runtime enforcement is claimed now.

## Traceability

Related: V3-001 §4.1/§4.6; R0-001 decision 2; DEC-002; ADR-V3-001; ADR-V3-007; ADR-V3-008; ADR-V3-011.

