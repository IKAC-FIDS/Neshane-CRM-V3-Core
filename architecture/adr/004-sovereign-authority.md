# ADR-V3-004: Locally authoritative Sovereign control

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-004
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Dedicated Sovereign operation cannot depend on implicit Central authority or synchronous Central availability for critical security and business operations.

## Decision

Dedicated Sovereign has a locally authoritative Control Plane with final security and operational authority and an independently operating Data Plane. Local trust, secrets, policy, grants, audit, plugin lifecycle, recovery and credential lifecycle are supported. Neshane Central interacts only through locally approved, authenticated and policy-controlled federation/telemetry; Central identities have no implicit local administrative rights.

## Alternatives

Central-master authority and mandatory synchronous federation were rejected. Full Air-Gap remains OD-001; specific identity, secrets and orchestration tools remain open.

## Consequences

Local operations need independent release, trust, recovery and audit capabilities. Federation must tolerate disconnection and minimize shared metadata.

## Verification expectations

Later profile evidence must demonstrate local critical operations during Central loss and denial of unapproved Central administration.

## Traceability

Related: V3-001 §4.3; R0-001 decision 4; DEC-004; OD-001, OD-011, OD-012, OD-015, OD-023; ADR-V3-003; ADR-V3-005; ADR-V3-010.

