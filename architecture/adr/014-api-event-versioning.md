# ADR-V3-014: REST and event contract versioning

- Status: ACCEPTED
- Authoring task: OD-008 formal closure
- Related decision/open decision: DEC-014 / OD-008
- Decision owner: API + Event Architecture
- Required approval authority: Technical Architecture Owner
- Approval disposition: APPROVED
- Approval provenance: Explicit CPO / Technical Architecture Owner direction in the OD-008 formal-closure task
- Effective date: Upon traceable commit of this approved decision package
- Architecture revision: `NESHANE-V3-ARCH-P00-004` upon traceable commit
- Supersedes: None
- Superseded by: None

## Context and scope

ADR-V3-008 requires contract-first compatible evolution but deliberately left exact REST and event versioning mechanics to OD-008. The accepted V3-011 and V3-012 engineering baselines now provide bounded executable evidence for public REST URI-major conventions, CloudEvents-compatible envelopes, immutable comparison baselines, deterministic schema resolution and conservative compatibility analysis. This decision makes the shared versioning and evolution rules architectural without claiming universal compatibility proof, CI execution, runtime enforcement or Production Readiness.

This ADR covers published REST and event contracts. The choice between REST, GraphQL BFF or a hybrid public API remains OD-007. If OD-007 later selects GraphQL or a hybrid boundary, GraphQL versioning requires a separate addendum; this ADR does not silently define it.

## Decision

### Contract ownership and lifecycle

- Each service owns its published HTTP and event contracts, version history, known-consumer inventory, compatibility evidence, deprecation and removal lifecycle.
- Changes follow the accepted Contract Change Protocol. A shared schema, SDK or transport type does not transfer business-fact ownership, authorization authority or implementation ownership.
- An accepted contract or compatibility baseline is immutable evidence. It must not be rewritten merely to make an incompatible candidate pass.

### REST contracts

- The default public REST convention is URI major versioning: `/api/v<major>/...`.
- Minor and patch revisions are recorded in contract metadata and traceable contract history; they do not create a new public URI when compatibility is preserved.
- Header-only and media-type versioning are not part of the initial baseline.
- HTTP compatibility remains directional. Request evolution must not invalidate requests accepted by a supported earlier contract. Response evolution must not make responses unacceptable to supported earlier consumers. Uncertain or unsupported constructs require manual review and cannot be presumed compatible.

### Event contracts

- Published events use CloudEvents 1.0-compatible envelopes.
- CloudEvents `specversion` identifies the envelope specification and is independent of the business event version.
- The event `type` contains its major business-contract version as `.v<major>`.
- `payloadversion` independently records the semantic payload version.
- Schema identity is immutable. Versioned schema artifacts and their manifest/history remain traceable; an existing schema artifact is not mutated to represent different semantics.
- Event compatibility is consumer-backward: every payload allowed by a candidate contract must remain acceptable to consumers of the supported baseline. Unsupported schema constructs require explicit manual review and fail closed in automated acceptance.

### Breaking change and retirement governance

A breaking HTTP or event change requires a new major version. Before publication or retirement, the owning service records:

1. supported old and new versions and their bounded coexistence;
2. known consumers and their migration state;
3. an accountable migration owner;
4. deprecation and removal criteria;
5. rollout, rollback or forward-recovery treatment; and
6. evidence that the removal criteria are satisfied before an existing contract is retired.

Unknown or unsupported contract, event or payload versions fail closed. No consumer is silently coerced to the latest version.

### Security boundaries

- A version downgrade must not weaken authentication, workload/producer validation, Tenant Context validation or domain-owned authorization.
- Tenant, producer, correlation or other envelope metadata is provenance or routing context only; it does not confer membership, entitlement or resource-access authority.
- Security-sensitive semantic changes require the applicable security review in addition to Level 2 compatibility approval.

## Alternatives and rationale

- **Header-only or media-type REST versioning for the initial baseline:** rejected because it reduces route-level visibility and does not match the accepted V3-011 engineering convention. It may be reconsidered only through a new Level 2 decision with migration consequences.
- **Silent in-place breaking changes or coordinated big-bang replacement:** rejected because they violate service independence, profile/version skew and ADR-V3-008.
- **One version field for envelope, event meaning and schema bytes:** rejected because protocol, business semantics and schema artifacts evolve under different authorities and cadences.
- **Mutable latest schema or compatibility baseline:** rejected because it destroys reproducible comparison, consumer evidence and recovery provenance.
- **GraphQL mechanics in this decision:** deferred to OD-007 because the public API strategy is still open.

The selected approach matches the accepted V3-011/V3-012 baselines, makes the version dimensions explicit and keeps breaking changes visible through major versions and governed coexistence.

## Consequences

- Services may need to serve or publish multiple major versions during coexistence.
- Consumer inventory, migration ownership and retirement evidence become release obligations.
- URI and event-type major versions are visible operationally, while minor/patch history remains contract metadata.
- Compatibility tooling remains conservative and incomplete by design; OD-020 still governs the final contract-testing and CI gate strategy.
- RabbitMQ topology, runtime delivery, retry, Outbox/Inbox and recovery mechanics remain outside this decision under ADR-V3-007 and future bounded implementation decisions. OD-019 applies where durable scheduling/workflow behavior is involved; OD-020 still governs contract-testing gates.

## Compatibility and consumer impact

V3-011 already implements the selected public URI-major convention and directional HTTP compatibility checks. V3-012 already implements the selected CloudEvents-compatible envelope, `.v<major>` event types, independent `payloadversion`, immutable schema identity, deterministic manifest resolution and consumer-backward compatibility checks. Their documented unsupported constructs continue to require manual review.

This decision does not retroactively certify unpublished examples as Business contracts or prove that any runtime producer, consumer, authentication, authorization or Tenant Context control exists.

## Migration and rollback/forward recovery

No migration is required for the accepted V3-011 and V3-012 engineering baselines because their recorded conventions already conform to this ADR. A future incompatible candidate is rejected before publication or introduced as a new major version with coexistence and consumer migration.

Before publication, rollback restores the last accepted immutable baseline together with the owning adapter change. After publication, Git rollback alone cannot undo emitted events or consumer adoption; the owner uses forward recovery, continued coexistence and reconciliation until recorded retirement criteria are met.

## Verification expectations

- Contract owners provide HTTP request/response or event consumer-backward compatibility evidence appropriate to the changed contract.
- Unknown versions, downgrade attempts, incompatible candidates and unsupported constructs have negative or manual-review evidence before release.
- Removal evidence identifies all approved consumers and demonstrates the recorded criteria for every affected deployment profile.
- Security-sensitive changes retain their Level 3 gates.
- Local engineering evidence, including V3-011/V3-012 tests, is not CI evidence, runtime security proof, independent Security Sign-off or Production Readiness.

## Traceability

Related records: OD-008; DEC-014; ADR-V3-002; ADR-V3-007; ADR-V3-008; the accepted [Contract Change Protocol](../contract-change-protocol.md); [API design standard](../standards/api-design.md); Backend V3-011 HTTP Contract Engineering Baseline; Backend V3-012 Event Contract Engineering Baseline; OD-007; OD-019; OD-020.

Affected repositories: Root architecture documentation. Backend governance-reference synchronization is required after this Root decision package is committed; V3-011 and V3-012 implementation content is unchanged. Frontend is unaffected until a public-client contract is selected under OD-007.
