# ADR-V3-012: Evidence-based readiness gates

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-012
- Approval: Project-owner approval recorded by Task R0-001
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Approved architecture is often mistaken for implemented or production-ready behavior, especially across multiple deployment profiles.

## Decision

Architecture Readiness, Implementation Readiness and Production Readiness are separate evidence-based gates. Operational readiness is assessed independently for each deployment profile. Documentation is not runtime evidence; unexecuted checks are not passed. Under current repository policy, Codex may write source/test documentation but must not execute builds, tests or deployments.

## Alternatives

A single completion status and inherited readiness across profiles were rejected.

## Consequences

Every completion/release claim identifies its gate, profile, evidence, omissions and assumptions. Approval of other ADRs grants no implementation or production claim.

## Verification expectations

Future gate definitions must name required artifacts, executable evidence, responsible owners and failure criteria without fabricating results.

## Traceability

Related: V3-001 §4.8/§9; R0-001 decision 12; DEC-012; OD-020, OD-023; ADR-V3-001; ADR-V3-003; ADR-V3-010; ADR-V3-011.

