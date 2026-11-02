# Neshane V3 contract change and compatibility protocol

## Document control

| Field | Value |
| --- | --- |
| Task | `V3-006 — ADR and Contract Change Protocol` |
| Task status | `CLOSED — ADR AND CONTRACT CHANGE GOVERNANCE BASELINE` |
| Status | `ACCEPTED — R0 GOVERNANCE BASELINE` |
| Accepted revision | `V3-006-R0-001` |
| Source baseline | Root parent commit `8a7434f1999b3d326e49e716997f68d7845f79ae` |
| Acceptance authority | CPO / Technical Architecture Owner, explicit bounded acceptance under `V3-006` |
| Scope | REST/OpenAPI, event/message, persistence migration, published SDK and integration contracts |
| Authority | Technical Architecture Owner under the Level 2 process; additional domain/security/operations authorities where explicitly required |
| Architecture basis | ADR-V3-002, ADR-V3-007, ADR-V3-008, ADR-V3-012, ADR-V3-014 and ADR-V3-015 |

This protocol governs contract change preparation and review. ADR-V3-014 selects the bounded REST/event versioning mechanics, and ADR-V3-015 selects the risk-based Contract Testing and evidence-gate strategy. This protocol still does not select the public REST/GraphQL strategy, schema registry, testing product, CI provider or migration product, and it does not close `OD-007`, `OD-013` or another Open Decision.

## Ownership and contract inventory

- Every contract has one accountable owning service or capability, a version, intended consumers and a bounded semantic purpose.
- Services retain exclusive ownership of domain truth, persistence, migrations and authorization. A shared contract never transfers business ownership or permits cross-service implementation/database access.
- Before changing a published contract, the owner records known consumers, deployment profiles, supported versions, data sensitivity and the latest safe removal milestone.
- Shared SDKs contain generated or narrow transport types only. They must not contain domain behavior, persistence entities or service implementation.

## Change classification

| Classification | Meaning | Required treatment |
| --- | --- | --- |
| Editorial | Documentation or metadata correction with no machine or semantic effect | Owner review and traceable change |
| Backward-compatible | Existing conforming consumers continue to operate without coordinated deployment | Compatibility evidence, consumer notification proportional to impact and ordinary release review |
| Conditionally compatible | Compatibility depends on a stated capability, ordering, default, profile or coexistence condition | Explicit condition, affected-consumer evidence and Level 2 review before publication |
| Breaking | Existing consumers, stored data, security semantics or operational behavior may fail or change meaning | New version or explicitly approved migration/coexistence plan, Level 2 approval and any applicable Level 3 review |

A change is breaking when it removes or renames required data, narrows accepted values, changes meaning/defaults, changes identity or authorization semantics, changes delivery/ordering/idempotency guarantees, requires simultaneous deployment, invalidates stored data, or removes a version still used by an approved consumer. Uncertainty is not classified as compatible; it requires evidence or escalation.

## Change workflow

1. Identify the owning service, contract, current version, proposed change, consumers and affected deployment profiles.
2. Classify the change and record semantic, security, privacy, tenant-isolation, availability and operational consequences.
3. For non-editorial changes, document alternatives, compatibility evidence, rollout order, coexistence, migration, rollback or forward recovery, observability and removal criteria.
4. Obtain owner review and the approvals required by the classification. Material architecture changes follow Level 2; security-critical changes retain Level 3 gates.
5. Update specifications, examples, generated artifacts and consumer documentation from the same approved source. Never treat generated code as the authority.
6. Validate references and compatibility evidence, then commit the decision/specification/registry changes as traceable Git history.
7. Remove an old version only after recorded consumer migration and removal criteria are satisfied.

## REST and OpenAPI

- Prefer additive optional fields, new resources or new operations whose absence does not alter existing behavior.
- Removing or renaming fields/operations, making optional input mandatory, changing validation/defaults, changing status/error semantics, changing authorization meaning or reusing a field for a different concept is breaking.
- A breaking public API change requires a new contract version unless an explicit Level 2 decision approves another compatibility and migration mechanism.
- Server implementation types and persistence entities are never public contract types.
- Public REST contracts use `/api/v<major>/...` by default under ADR-V3-014; minor/patch history remains contract metadata. Header-only and media-type versioning are outside the initial baseline. REST/GraphQL/hybrid public API selection and any GraphQL versioning addendum remain governed by `OD-007`.

## Events and messages

- Event contracts describe facts owned by the producer and preserve event identity, semantic version, producer provenance, tenant provenance where applicable and correlation/causation meaning.
- Additive fields are compatible only when consumers are required and shown to tolerate them and defaults do not change semantic truth.
- Changing event meaning, identity, partition/order expectations, required fields, tenant provenance, delivery semantics or enum interpretation is breaking.
- Breaking changes require a new major contract version, coexistence, producer/consumer migration ordering, replay/re-drive treatment and retirement criteria.
- A transport retry or re-drive cannot rewrite original semantic evidence. Under ADR-V3-014, events use CloudEvents 1.0-compatible envelopes, independent `specversion`, `.v<major>` event types, semantic `payloadversion` and immutable versioned schema identity.

## Persistence and data migration

- Database schemas and migrations are private contracts owned by one service; cross-service consumers are prohibited.
- Use expand/migrate/contract or an equivalent forward-compatible sequence when old and new application versions may coexist.
- Destructive, lossy, irreversible or long-locking changes require explicit data validation, backup/recovery treatment, deployment ordering and rollback or forward-recovery evidence.
- Migration rollback is not promised when unsafe. In that case the plan states forward recovery, restoration boundaries and data reconciliation.
- Migration tooling remains governed by `OD-013`; this protocol does not select it.

## SDK and external integration contracts

- A published SDK follows the underlying approved contract and has its own compatibility/version statement. SDK convenience APIs cannot create undocumented service semantics.
- External/provider changes require provenance, validation, failure behavior, data-protection and resilience assessment appropriate to the integration.
- Unsupported provider behavior or consumer assumptions are documented as limitations, not compatibility guarantees.

## Deprecation and supersession

Every deprecation records the replacement, affected consumers, coexistence expectations, migration owner, evidence required for removal and a decision milestone. Do not invent calendar deadlines when no authority has approved them.

Superseded specifications and schemas remain traceable and read-only. Removal requires evidence that approved consumers have migrated and that profile/version-skew obligations are satisfied.

## Review and evidence gates

- Contract owner: correctness, consumers, semantics and migration evidence.
- Technical Architecture Owner: Level 2 compatibility and architecture disposition.
- Security authority: changes to trust, identity, authorization, tenant isolation, sensitive data, cryptography or privileged operations when the applicable Level 3 gate requires it.
- Operations/profile owners: rollout, recovery and coexistence evidence where deployment profiles are affected.
- Quality authority: risk classification, critical-path inventory, compatibility/conformance evidence, mandatory re-execution criteria and limited Quality exceptions under ADR-V3-015. The scoped interim dual-role designation does not replace Security Authority or implementation evidence.

Documentation approval is not runtime compatibility evidence. Unexecuted tests, proposed tooling and future migration plans must not be reported as verified implementation or Production Readiness.

## V3-006 boundaries

`OD-002`, `OD-003` and `OD-004` were subsequently resolved under the Level 2 workflow by DEC-013/ADR-V3-013 in V3-005. That decision selects the Backend foundation architecture but does not itself verify downloaded tooling, Wrapper integrity, build execution or Production Readiness.

`OD-008` was subsequently closed under the Level 2 workflow by DEC-014/ADR-V3-014. That decision selects bounded REST/event versioning and evolution rules; it does not close OD-007, prove runtime enforcement or authorize contract release.

`OD-020` is closed as approved under DEC-015/ADR-V3-015 and becomes effective upon its traceable Level 2 commit. It selects the architecture testing strategy and blocking evidence obligations; it does not prove that CI, Provider, Consumer or Real Integration tests have executed and does not authorize Production Release.
