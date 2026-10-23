# ADR-V3-003: Cell-based hybrid multi-tenancy

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-003
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Neshane must serve shared, managed-dedicated and sovereignty-sensitive customers without changing tenant identity or business semantics.

## Decision

The first supported production release must support Shared SaaS, Dedicated Managed and Dedicated Sovereign profiles. Tenant identity is stable and independent of cell, database and physical placement. Tenant routing, Placement Generation, cell lifecycle and migration are explicit architectural responsibilities. Shared cells enforce validated Tenant Context, service authorization and PostgreSQL RLS on tenant-aware tables; dedicated profiles retain compatible logical models/contracts.

## Alternatives

Shared-only or dedicated-only architecture was rejected. Fully Air-Gapped support is not implied and remains OD-001.

## Consequences

Placement, migration, compatibility, recovery and per-profile evidence add operational complexity. Tenant identifiers cannot encode topology.

## Verification expectations

Later evidence must cover isolation, stale routing/generation, placement migration and every supported profile independently.

## Traceability

Related: V3-001 §4.2; R0-001 decision 3; DEC-003; OD-001, OD-022, OD-023; ADR-V3-004; ADR-V3-007; ADR-V3-010; ADR-V3-012.

