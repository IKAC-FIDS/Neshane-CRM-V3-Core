# ADR-V3-005: Domain-owned authorization with shared policy governance

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-005
- Decision approval: Explicit project-owner decision recorded in Task R0-001
- Documentation formalization: Codex under Task R0-001
- Independent reviewer sign-off: Not recorded
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Authentication, membership or central policy alone cannot safely decide resource-specific business actions.

## Decision

Shared Policy Governance defines common policy contracts and governance, while each resource-owning Business Service makes and enforces the final resource/action authorization decision. Authentication, tenant membership, entitlement and authorization remain distinct. User, Service, Operator and Plugin Installation identities remain distinct; service calls require authenticated audience-restricted identity. Sovereign policy authority is local. Missing or indeterminate authority fails closed where access cannot be safely established.

## Alternatives

Gateway-only, IdP-only or centralized universal authorization was rejected. Specific IdP, policy engine, session, workload identity and secrets tools remain OD-009–OD-012.

## Consequences

Services require consistent policy inputs plus domain-specific enforcement and audit. Trusted identity never implies permission.

## Verification expectations

Later evidence must include direct-service denials, tenant/resource matrices, workload audience checks, plugin grants and Sovereign-local policy behavior.

## Traceability

Related: V3-001 §4.4; R0-001 decision 5; DEC-005; OD-009–OD-012; ADR-V3-004; ADR-V3-006; ADR-V3-007; ADR-V3-009.

