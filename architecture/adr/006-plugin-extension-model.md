# ADR-V3-006: Event-first plugins with controlled hooks

- Status: Accepted
- Date: 2026-10-23
- Decision: DEC-006
- Decision approval: Explicit project-owner decision recorded in Task R0-001
- Documentation formalization: Codex under Task R0-001
- Independent reviewer sign-off: Not recorded
- Architecture revision: `NESHANE-V3-ARCH-P00-002`

## Context

Third-party extensibility must not place untrusted code or implicit authority inside Core or Business Service processes.

## Decision

Plugins execute outside main processes and access Neshane through the Extension Gateway. Event-driven extension is preferred; controlled synchronous hooks are supported with explicit timeout, failure, authorization and idempotency semantics. Plugin Package, Installation and Runtime Instance are distinct. Each Installation has its own identity, grants, tenant binding, configuration and lifecycle. Customer-hosted, Neshane-hosted and Sovereign-local execution are supported; Business Services retain final domain decisions.

## Alternatives

In-process plugins and direct database access were rejected. Managed runtime isolation and Marketplace/Developer Portal scope remain OD-016 and OD-021.

## Consequences

The platform must govern compatibility, delivery, retries, hooks, audit and per-installation isolation. Contracts remain language-independent.

## Verification expectations

Later evidence must cover cross-installation/tenant denial, grant changes, duplicate events, hook timeout/failure and local Sovereign operation.

## Traceability

Related: V3-001 §4.5; R0-001 decision 6; DEC-006; OD-008, OD-016, OD-021; ADR-V3-005; ADR-V3-008; ADR-V3-010.

