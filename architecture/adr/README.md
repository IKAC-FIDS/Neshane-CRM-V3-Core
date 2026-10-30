# Neshane V3 Architecture Decision Records

This directory is the authoritative catalog for formal V3 ADRs. ADR IDs use `ADR-V3-NNN`; Task IDs use `V3-NNN` and never substitute for ADR IDs. Decision-register IDs use `DEC-NNN`, and open-decision IDs use `OD-NNN`.

## Status vocabulary

- **`PROPOSED`**: a complete candidate decision awaiting the required approval. It has no architectural authority.
- **`ACCEPTED`**: explicitly approved by the recorded Level 2 authority and effective from the recorded effective date.
- **`REJECTED`**: considered and explicitly declined. The record and rationale remain historical evidence and have no architectural authority.
- **`DEPRECATED`**: previously accepted but no longer recommended for new use. Existing usage, compatibility, migration and removal obligations must be stated.
- **`SUPERSEDED`**: replaced by one or more named later ADRs. The old ADR remains immutable historical evidence and links to its replacements.

`OPEN` is an Open Decision state in `open-decisions.md`, not an ADR lifecycle state. An Open Decision becomes an ADR only after a concrete proposal is prepared and routed through Level 2 approval.

An ADR status changes only through explicit approval. Task R0-001 records the project owner's explicit decisions for the twelve initial V3 ADRs on 2026-10-23. Codex documented and formalized those decisions under R0-001; no independent reviewer identity, signature or separate approval evidence is recorded.

## Lifecycle and revision rules

The normal flow is `PROPOSED -> ACCEPTED`. An authorized decision may instead move `PROPOSED -> REJECTED`. An `ACCEPTED` ADR may later become `DEPRECATED` or `SUPERSEDED`, but never disappears or has its original decision rewritten.

- A material change to an accepted decision requires a new ADR. The new ADR names every replaced record; the old record changes only its status and supersession link.
- Editorial corrections that do not change meaning may update an ADR in place and must remain traceable in Git.
- The effective date is the date the authorized decision becomes applicable, not the drafting date. Do not invent a date.
- Rejected, deprecated and superseded ADRs remain in the catalog and decision history.
- A status change updates the ADR, this catalog, `decision-register.md`, affected `OD-*` entries, the architecture baseline where material, and affected repository baseline references.
- Compatibility, migration, rollback/forward-recovery and consumer impact are mandatory considerations when the decision affects an existing implementation or published contract.

## Required ADR fields

Every new ADR contains:

1. ADR ID and title.
2. Status using the canonical lifecycle vocabulary.
3. Authoring Task ID and related `DEC-*`/`OD-*` identifiers.
4. Decision owner and required approval authority.
5. Approval disposition, provenance and effective date; blank or `PENDING` while proposed.
6. Context and bounded scope.
7. Decision statement.
8. Viable alternatives and rationale.
9. Consequences and operational/security implications.
10. Compatibility and consumer impact.
11. Migration plus rollback or forward-recovery considerations.
12. Verification expectations and evidence gate.
13. Supersedes/superseded-by links where applicable.
14. Traceability to tasks, standards, contracts and affected repositories.

## ADR template

```markdown
# ADR-V3-NNN: <title>

- Status: PROPOSED
- Authoring task: <V3-NNN>
- Related decision/open decision: <DEC-NNN / OD-NNN>
- Decision owner: <role>
- Required approval authority: <role/gate>
- Approval disposition: PENDING
- Approval provenance: PENDING
- Effective date: PENDING
- Architecture revision: PENDING
- Supersedes: None
- Superseded by: None

## Context and scope
## Decision
## Alternatives and rationale
## Consequences
## Compatibility and consumer impact
## Migration and rollback/forward recovery
## Verification expectations
## Traceability
```

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
| [ADR-V3-013](013-backend-foundation-toolchain.md) | Backend foundation toolchain and build layout | Accepted | — | DEC-013; OD-002–OD-004; V3-005 |

ADR-V3-001 through ADR-V3-012 form approved architecture revision `NESHANE-V3-ARCH-P00-002`. ADR-V3-013 adds the accepted Backend foundation refinement in `NESHANE-V3-ARCH-P00-003`, effective when the V3-005 decision package is committed. Historical records are never rewritten to disguise a conflict. The lifecycle and template added by `V3-006` were accepted at R0 by the CPO/Technical Architecture Owner as governance revision `V3-006-R0-001`; they do not change the status or content of ADR-V3-001 through ADR-V3-012.

