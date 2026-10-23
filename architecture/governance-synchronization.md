# Cross-repository governance synchronization

## Baseline

- Current reference: `NESHANE-V3-GOV-P00-000A`.
- Scope: the Root `AGENTS.md`, Root engineering standards, and this synchronization policy.
- This reference is a governance revision label, not an ADR. It does not approve choices explicitly marked proposed or unresolved.
- Current approved architecture revision: `NESHANE-V3-ARCH-P00-002`, formalized by ADR-V3-001 through ADR-V3-012 under R0-001.
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

## Missing, stale, or conflicting guidance

- A repository remains usable without the Root checkout because its local baseline records the required invariants.
- If Root is available and the local reference differs, stop architecture-sensitive work and report the mismatch.
- If a required decision is absent, mark it unresolved and request approval; do not invent a replacement.
- If local guidance conflicts with an approved Root ADR or standard, the Root decision wins, but Codex must report the conflict and update local guidance only under an authorized Task ID.
- Do not describe a nonexistent or proposed document as approved.

