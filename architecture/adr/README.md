# Neshane V3 Architecture Decision Records

This directory is the authoritative catalog for formal V3 ADRs. ADR IDs use `ADR-V3-NNN`; Task IDs use `V3-NNN` and never substitute for ADR IDs. Decision-register IDs use `DEC-NNN`, and open-decision IDs use `OD-NNN`.

## Status vocabulary

- **Accepted**: formally ratified by the recorded owner/review gate.
- **Proposed**: a concrete recommendation awaiting approval.
- **Open**: alternatives are still being evaluated; no decision authority.
- **Superseded**: replaced by a named later ADR; retained historically.
- **Deprecated**: retained for history but no longer recommended; no silent deletion.

An ADR status changes only through explicit approval. Project-owner approval for the twelve initial V3 ADRs is recorded by Task R0-001 on 2026-10-23.

## Catalog

V2 ADR-001 through ADR-011 remain historical V2 records and are not imported or renumbered as V3 ADRs.

| ADR ID | Title | Status | Replaces | Related decisions/tasks |
| --- | --- | --- | --- | --- |
| [ADR-V3-001](001-backend-architecture.md) | Java/Spring Boot independent microservices | Accepted | — | DEC-001; R0-001 |
| [ADR-V3-002](002-service-ownership.md) | Strict service and data ownership | Accepted | — | DEC-002; R0-001 |
| [ADR-V3-003](003-cell-based-hybrid-tenancy.md) | Cell-based hybrid multi-tenancy | Accepted | — | DEC-003; R0-001 |
| [ADR-V3-004](004-sovereign-authority.md) | Locally authoritative Sovereign control | Accepted | — | DEC-004; R0-001 |
| [ADR-V3-005](005-domain-owned-authorization.md) | Domain-owned authorization with shared policy governance | Accepted | — | DEC-005; R0-001 |
| [ADR-V3-006](006-plugin-extension-model.md) | Event-first plugins with controlled hooks | Accepted | — | DEC-006; R0-001 |
| [ADR-V3-007](007-data-messaging-baseline.md) | Service-owned persistence and reliable messaging | Accepted | — | DEC-007; R0-001 |
| [ADR-V3-008](008-contract-compatibility.md) | Contract-first controlled compatibility | Accepted | — | DEC-008; R0-001 |
| [ADR-V3-009](009-frontend-architecture.md) | Modular feature-oriented Frontend | Accepted | — | DEC-009; R0-001 |
| [ADR-V3-010](010-operational-profiles.md) | Verifiable profile-specific operations | Accepted | — | DEC-010; R0-001 |
| [ADR-V3-011](011-logical-boundaries-co-deployment.md) | Logical boundaries first with controlled co-deployment | Accepted | — | DEC-011; R0-001 |
| [ADR-V3-012](012-evidence-based-readiness.md) | Evidence-based readiness gates | Accepted | — | DEC-012; R0-001 |

These ADRs form approved architecture revision `NESHANE-V3-ARCH-P00-002`. New ADRs must state context, decision, alternatives, consequences, verification expectations, approval owner/date, related `DEC-*`/`OD-*`/Task IDs, and any superseded ADR. Historical records are never rewritten to disguise a conflict.

