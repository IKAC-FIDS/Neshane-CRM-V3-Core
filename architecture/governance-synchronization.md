# Cross-repository governance synchronization

## Baseline

- Current reference: `NESHANE-V3-GOV-P00-000A`.
- Scope: the Root `AGENTS.md`, Root engineering standards, and this synchronization policy.
- This reference is a governance revision label, not an ADR. It does not approve choices explicitly marked proposed or unresolved.
- Current approved architecture revision: `NESHANE-V3-ARCH-P00-005` upon traceable commit of the OD-020 decision package; ADR-V3-001 through ADR-V3-012 were formalized under R0-001, ADR-V3-013 records the Backend foundation toolchain selection, ADR-V3-014 records REST/event versioning and ADR-V3-015 records risk-based Contract Testing governance.
- Architecture revisions do not silently rename this governance reference. A V3 ADR is authoritative after explicit approval and storage in the Root architecture area.

## Ownership

- Root owns cross-repository principles, ADRs, shared standards, and architecture review policy.
- Backend owns Java/Spring Boot implementation guidance and repository-local skills.
- Frontend owns framework-neutral frontend implementation guidance and repository-local skills.
- Backend and Frontend remain independent Git repositories. Do not use submodules, nested-repository tracking, or synchronization automation for this policy.

## Propagation process

1. Approve the architecture change in Root and update the affected Root standard or ADR.
2. Assign a new architecture revision for an architecture change. Change the governance baseline reference only when governance rules themselves change and the authorizing task requires a new governance revision.
3. Review impact on Backend and Frontend separately.
4. Update only affected local instructions, standards, and skills; record the applicable governance and architecture references in each repository's `architecture/governance-baseline.md`.
5. Review local differences for consistency before implementation resumes. Propagation is complete only when each affected repository records the same current reference.

## Completed local propagation under R0-003

R0-003 propagated architecture revision `NESHANE-V3-ARCH-P00-002` and governance reference `NESHANE-V3-GOV-P00-000A` to the affected repository-local instructions, standards, skills, and governance baselines without changing approved ADRs:

- Backend synchronization: commit `6a7afc5`; independent build/test/version/release boundaries, domain-owned authorization with shared policy governance, contract coexistence/deprecation, controlled co-deployment, and profile-specific readiness evidence were reconciled.
- Frontend synchronization: commit `f3d138f`; modular feature-oriented architecture, shared Design System ownership, no initial Micro-Frontend requirement, controlled contract compatibility, and evidence-based readiness terminology were reconciled.

Both local governance baselines now record the current architecture and governance references. This completion records documentary propagation only; it does not establish implementation or production readiness, or independent R0 reviewer approval. Future architecture or governance revisions continue to follow the propagation process above.

## V3-005 propagation state

Architecture revision `NESHANE-V3-ARCH-P00-003` changes the Backend foundation baseline only. Backend commit `8f1cfaca40c0471a03418831aacfbe2689417cad` records the synchronized local governance reference, ADR-V3-013 engineering guidance, complete Gradle foundation and bounded R0 acceptance. Traceable Backend propagation is complete. Frontend is unaffected by the toolchain decision.

The V3-005 CPO/Technical Architecture Owner direction also replaces the project blanket build/test prohibition with controlled, Task-scoped local execution. Root commit `c65c97d746c804e0569ff50701d1f4eaedae7312` and Backend commit `8f1cfaca40c0471a03418831aacfbe2689417cad` record the shared and local policies. Offline build, formatting, module-boundary, dependency-report and reproducibility evidence is recorded in the Backend baseline; Gradle test tasks were `NO-SOURCE`, so no Unit Test coverage or passing Unit Test suite is claimed.

`V3-005` is `CLOSED — ENGINEERING FOUNDATION R0 BASELINE`. Closure establishes the engineering foundation only; it does not establish Spring Boot application/runtime verification, Security Sign-off, CI evidence, deployment-profile assurance, publishing, release authorization or Production Readiness.

## V3-010 development-first propagation state

The CPO/Technical Architecture Owner authorizes a prospective development-first policy for ordinary Tasks. Root, Backend and Frontend may implement, resolve pinned dependencies from approved official registries, build, test, debug, and use isolated Task-owned local services/containers without repeated per-command approvals. The explicit Task ID and affected component boundaries remain mandatory.

This propagation removes project-owned blanket execution prohibitions from repository instructions, testing standards and mandatory skills. It does not alter an ADR, security invariant, production gate or architecture revision. Governance reference `NESHANE-V3-GOV-P00-000A` remains unchanged because V3-010 did not authorize a new label.

The synchronized guardrails prohibit production/customer data and credentials, untrusted registries, disabled integrity checks, privileged/host-network containers, sensitive host or Docker-socket mounts, unrelated resource deletion, publishing, push, remote mutation and deployment without their required authorization. Security-critical decisions, risk acceptance, executable `DURABLE_DEFER`, production migrations and releases retain their existing approval gates.

## OD-008 propagation state

Architecture revision `NESHANE-V3-ARCH-P00-004` closes OD-008 through DEC-014/ADR-V3-014 upon a traceable Root commit. The accepted Backend V3-011 and V3-012 engineering baselines already implement conforming bounded conventions for public REST URI-major versioning, CloudEvents 1.0-compatible envelopes, independent event/payload/schema versions, immutable baselines and fail-closed compatibility analysis. This governance-only task does not modify those implementations.

Backend synchronization commit `03987f4cf7ffab377742e5f8799bccd16f5851eb` records architecture reference `NESHANE-V3-ARCH-P00-004`, DEC-014/ADR-V3-014 and the historical-versus-current OD-008 distinction without changing executable contracts. Frontend requires no immediate OD-008 content change; OD-007 still controls the future public REST/GraphQL/hybrid boundary and any GraphQL versioning addendum.

## OD-020 propagation state

Architecture revision `NESHANE-V3-ARCH-P00-005` closes OD-020 as approved through
DEC-015/ADR-V3-015 and becomes effective upon a traceable Root decision-package commit. V3-011 and
V3-012 already provide bounded local HTTP/Event validation and compatibility evidence, but do not
provide CI, Provider Conformance, Consumer-driven or Real Integration execution evidence.

After the Root commit, Backend requires a separately authorized synchronization of its local
architecture reference and contract-governance wording. That propagation must not alter executable
contracts merely to satisfy the new reference. Frontend requires synchronization only when its
owned Consumer expectations or public contract workflow becomes affected. OD-007 and OD-019 remain
open. No repository may claim CI approval, Security Sign-off or Production Readiness from the Root
governance decision alone.

## Missing, stale, or conflicting guidance

- A repository remains usable without the Root checkout because its local baseline records the required invariants.
- If Root is available and the local reference differs, stop architecture-sensitive work and report the mismatch.
- If a required decision is absent, mark it unresolved and request approval; do not invent a replacement.
- If local guidance conflicts with an approved Root ADR or standard, the Root decision wins, but Codex must report the conflict and update local guidance only under an authorized Task ID.
- Do not describe a nonexistent or proposed document as approved.

