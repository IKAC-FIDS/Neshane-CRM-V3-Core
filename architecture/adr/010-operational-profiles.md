# ADR-V3-010: Verifiable profile-specific operations

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-010
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Shared, Managed and Sovereign profiles share outcomes but require different operational implementations and authority boundaries.

## Decision

Define common operational contracts and acceptance requirements with profile-specific implementations. Reproducible versioned artifacts, integrity verification, release/upgrade/rollback, backup/restore, observability, secrets, recovery, security operations and audit must be independently verifiable for every supported deployment profile. Sovereign operations remain locally authoritative.

## Alternatives

One unverified deployment recipe for all profiles and Central-only operations were rejected. Orchestration, secrets/key tooling and numeric SLO/RTO/RPO/capacity remain OD-012, OD-015 and OD-023.

## Consequences

Release evidence and support procedures multiply by profile where implementations differ. Architecture approval alone never establishes operational readiness.

## Verification expectations

Each profile requires its own install, upgrade, rollback, recovery, integrity, observability and authority evidence.

## Traceability

Related: V3-001 §4.8; R0-001 decision 10; DEC-010; OD-001, OD-012, OD-015, OD-023; ADR-V3-003; ADR-V3-004; ADR-V3-012.

