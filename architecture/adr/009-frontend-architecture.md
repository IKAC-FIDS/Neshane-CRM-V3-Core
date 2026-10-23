# ADR-V3-009: Modular feature-oriented Frontend

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-009
- Decision approval: Explicit project-owner decision recorded in Task R0-001
- Documentation formalization: Codex under Task R0-001
- Independent reviewer sign-off: Not recorded
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Frontend requires modular product evolution and a coherent accessible UI without premature distributed deployment complexity.

## Decision

Use a modular, feature-oriented Frontend with logically isolated feature modules and a shared Design System. Features do not depend on Backend implementation details and consume explicit versioned contracts. Frontend permission checks are UX controls; resource-owning services authorize. Persian, RTL, responsive behavior and accessibility are mandatory. Independent Micro-Frontend deployment is not initially required.

## Alternatives

A layer-only unmodularized application and mandatory Micro-Frontend deployment were rejected. Framework, rendering, state and UI libraries remain OD-005–OD-007.

## Consequences

Feature public surfaces and Design System ownership must remain explicit. A future move to independently deployed Micro-Frontends requires a new ADR.

## Verification expectations

Later evidence must cover dependency boundaries, contract mapping, permission denial, accessibility, RTL and critical user states.

## Traceability

Related: V3-001 §4.7; R0-001 decision 9; DEC-009; OD-005–OD-007, OD-010; ADR-V3-005; ADR-V3-008; ADR-V3-012.

