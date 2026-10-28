# V3-003 Contract Governance and Messaging/API Event Architecture Specialist Review Request

## Document Control

| Field | Recorded value |
| --- | --- |
| Task | `V3-003 — NFR and Threat Assumptions` |
| Document status | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWERS` |
| Coordinated review scopes | Contract Governance; Messaging/API Event Architecture |
| Contract Governance approval | `PENDING` |
| Messaging/API Event Architecture approval | `PENDING` |
| Security Architecture approval | `PENDING` |
| Independent Security Review | `NOT_SIGNED_OFF` |
| Implementation evidence | `NOT_VERIFIED` |
| Negative-test execution | `NOT_EXECUTED` |
| Executable DURABLE_DEFER | `NOT APPROVED` |

This document requests two independent specialist reviews. Coordination does not merge their identities, authority, decision rights, evidence requests or dispositions. It records no reviewer opinion, approval, identity, signature, review date, risk acceptance, runtime evidence or test result.

`CG-01` through `CG-05` are local working labels in this request. They are not official DEC, ADR, OD, SR, threat or test identifiers.

## A. Verified Baseline and Document Control

### A.1 Repository and revision identity

| Field | Verified value |
| --- | --- |
| Repository | `IKAC-FIDS/Neshane-CRM-V3-Core` |
| Branch | `main` |
| Preparation HEAD | `8a20559b4b9a71b90fb31342eb24d51de5c1763b` |
| HEAD subject | `docs(security): prepare tenant security specialist review request` |
| Local tracking state before creation | `main...origin/main [ahead 16]` |
| Worktree and index before creation | Clean |
| Target document in preparation HEAD | No |
| Remote publication claim | None; no fetch, stage, commit or push performed |

The HEAD change since the previously pinned analysis baseline is documentation-only: it records the Tenant Security Review Request. The exact bytes of the pinned design sources remain unchanged. This request is new working-tree content until separately committed; the preparation HEAD must not be represented as containing it.

### A.2 Exact review references

| Document | Git blob in preparation HEAD | SHA-256 | Recorded status |
| --- | --- | --- | --- |
| `architecture/reviews/V3-003-consolidated-security-design-review-manifest.md` | `3b0ff1657ff5b8a3218f81d8626242292bd5fb29` | `9592b9e9190d2182132d5eebefbd9fdcb7c802f7f8a8e305b8209db699b90c3e` | `PINNED_FOR_SPECIALIST_REVIEW` |
| `architecture/reviews/V3-003-customer-audit-technical-contract-draft.md` | `60cb1e3043a66e587c7b20428e2c68cdd361007a` | `56e71f3ee0537bfc70d0e3f02602175d0e0eb87510fbb7ab43125f37c4010412` | `DRAFT — CROSS-DOMAIN REVIEW REQUIRED` |
| `architecture/reviews/V3-003-identity-platform-security-review-request.md` | `28d51bce2c5c840b4913c9c81f3d9675ec0e570a` | `99f64d857ee22b3090bf9ad07fc270c903dab0c620190fba7ac3590c8631cc1e` | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |
| `architecture/reviews/V3-003-tenant-security-review-request.md` | `62370124a3304a84c56da4cf7daaaf2a756ab313` | `b2364c4d4469209e48e28e8a3f59d3f794337c194a79b18b4a7bece7976a0701` | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |

SEC-01 through SEC-05 remain `DRAFT — SECURITY REVIEW REQUIRED`. The V3-003 Decision Record preserves DEC-009 through DEC-014 as bounded Owner decisions while expressly withholding final contracts, protocols, security approval, implementation authorization and executable DURABLE_DEFER.

### A.3 Applicable baseline

- ADR-V3-002 preserves service and domain ownership.
- ADR-V3-004 preserves Sovereign-local final security and operational authority.
- ADR-V3-005 preserves resource-owning Domain authorization.
- ADR-V3-007 preserves service-owned data, transactional outbox/inbox principles and validated Tenant provenance.
- ADR-V3-008 requires explicit versioned contract compatibility.
- ADR-V3-010 requires profile-specific operational evidence.
- ADR-V3-012 separates documentation, implementation evidence and Production Readiness.
- `architecture/standards/api-design.md`, `messaging.md`, `security.md`, `persistence.md`, `service-architecture.md` and `error-handling.md` remain applicable.
- `OD-001` through `OD-023` remain Open; especially `OD-008`, `OD-011`, `OD-012`, `OD-019` and `OD-020` constrain this review.

Existing bounded decisions include six Customer principles, four Audit dispositions, five Messaging/Operations dispositions and the bounded SEC-01 through SEC-05 dispositions. None establishes either specialist approval requested here.

## B. Independent Specialist Authority Boundaries

### B.1 Contract Governance

Requested decisions are limited to:

- semantic field definitions and participation;
- contract identity, semantic equality and canonicalization rules;
- compatibility, evolution, coexistence, deprecation and transformation governance;
- confirmation and disposition vocabulary and semantic transitions;
- contract negotiation semantics;
- data-minimization and retention dependencies.

Contract Governance does not by itself approve producer identity, Tenant authority, cryptography, broker topology, runtime implementation, operational eligibility or Independent Security Review.

### B.2 Messaging/API Event Architecture

Requested decisions are limited to:

- logical envelope requirements and boundary validation;
- original producer provenance propagation;
- separation of semantic evidence from publication/retry/re-drive metadata;
- delivery and confirmation exchange patterns;
- version negotiation transport behavior and consumer compatibility constraints;
- failure-disposition transport semantics.

Messaging/API Event Architecture does not own Customer or Audit business facts, final resource authorization, final semantic vocabulary, Security sign-off, operational risk acceptance or executable DURABLE_DEFER.

### B.3 Shared decisions

Where both authorities participate, each must issue its own disposition. Contract Governance decides semantic meaning; Messaging/API Event Architecture decides transport/envelope behavior consistent with that meaning. Neither disposition implies the other.

## C. Semantic Contract Field Matrix

The complete `ObligationKey` is:

```text
ProducerAuthority + TenantScope + ObligationId
```

`MutationId` remains traceability evidence and is not Audit ingestion identity. Customer owns producer-side business and recovery evidence; Audit owns authoritative ingestion, confirmation and Audit dispositions.

| Field | Candidate class | Semantic owner | Equality participation | Transfer/minimization boundary | Unresolved specialist question |
| --- | --- | --- | --- | --- | --- |
| `ProducerAuthority` | Identity-defining | Customer authority; Audit validates | Immutable; part of full key | Never inferred from mutable header | Provenance representation and binding |
| `TenantScope` | Identity-defining | Customer establishes; Audit independently validates | Immutable; part of full key | Selector alone is not authority; no cross-Tenant fallback | Authoritative evidence and profile binding |
| `ObligationId` | Identity-defining | Customer | Immutable; part of full key | Identifier technology unselected | Format, uniqueness and retention |
| `ContractType` | Required immutable semantic evidence | Contract Governance | Yes | Not authorization proof | Namespace and negotiation |
| `ContractVersion` | Required immutable semantic evidence | Contract Governance | Yes | Unauthorized downgrade prohibited | Compatibility and support matrix |
| `SemanticContentVersion` | Semantic comparison-version evidence | Contract Governance | Selects comparison rules | Security review required | Representation and binding |
| `OperationType` | Required immutable semantic evidence | Customer | Yes | Versioned approved vocabulary only | Enum evolution |
| `Outcome` | Required immutable semantic evidence | Customer | Yes | Must not generalize unapproved failures | Vocabulary and future evolution |
| `MutationId` | Required traceability evidence; not identity | Customer | Candidate immutable evidence; not full key | Must not expose private persistence details | Exact equality participation |
| `ActorRef` | Minimal accountability evidence | Customer / Identity provenance | Candidate semantic evidence | No credentials, tokens or excess identity attributes | Stable safe-reference rules |
| `SafeCustomerRef` | Minimal domain reference | Customer | Candidate semantic evidence | No full Customer record or unnecessary sensitive identifier | Representation and classification |
| `OccurredAt` | Candidate required evidence | Customer | **UNRESOLVED** | Clock and skew policy pending | Identity/equality participation and precision |
| `CorrelationRef` | Candidate traceability evidence | Customer | **UNRESOLVED** | Sanitized; no request content | Semantic versus diagnostic participation |
| `ChangeCategoryRef` | Conditional semantic evidence for CUS-UPDATE | Customer vocabulary; Audit validates | Conditional; rules pending | Old/new sensitive values excluded | Taxonomy and inclusion rules |
| `CausationRef` | Conditional semantic evidence | Customer | Conditional; rules pending | No raw token, credential or secret | Approved causal uses and equality participation |
| `TransportAttemptId` | Non-semantic transport metadata | Messaging/Operations | No | Operational evidence only | Identity and retention |
| Broker delivery ID, attempt number, route, ACK/NACK, retry/backoff and DLQ observations | Non-semantic transport metadata | Messaging/Operations | No | Must not become business or Audit truth | Diagnostic retention and disclosure |

Customer-owned evidence not transferred by default includes `CommandIdentityRef`, Customer commit evidence, pending/recovery state, producer evidence references and transport-attempt history. Credentials, tokens, complete Customer snapshots, unnecessary Customer data, sensitive old/new values and raw private-database locators are prohibited ordinary Audit-event content.

Contract Governance must decide semantic classes and participation. Messaging/API Event Architecture must separately decide where approved fields appear and how their boundaries are preserved in an envelope.

## D. Canonicalization Alternatives Matrix

Required logical properties are typed, deterministic, version-bound semantic comparison independent of incidental serialization. Raw wire-byte equality is not a general semantic comparison rule. Digest equality alone proves neither Producer authority, Tenant authority nor contract validity.

| Alternative | Determinism | Benefit | Main risk | Current status |
| --- | --- | --- | --- | --- |
| Versioned canonical semantic projection | High when field selection and normalization are explicit | Clean separation from transport serialization | Requires complete normative specification | Preferred logical direction |
| Schema-native canonical encoding | Depends on schema technology | Tooling and validation alignment | Coupling and cross-language differences | Permissible; decision required |
| Self-describing canonical representation | Potentially portable | Easier inspection/evolution | Ambiguity in null, ordering, numbers and Unicode | Permissible with explicit rules |
| Typed field-by-field comparison | High within a consistent implementation | Serialization-independent | Cross-language drift; harder portable integrity evidence | Permissible with conformance evidence |
| Raw wire-byte equality | Byte-deterministic only | Simple | False conflicts from equivalent serializers | Rejected as general rule |
| Digest-only comparison | Deterministic only after canonicalization | Compact evidence | Cannot establish provenance, authorization or semantic validity | Auxiliary only |

Separate reviewer decisions are required for absent/null/default behavior, Unicode normalization, numeric representation, timestamp instant/timezone/precision, enum and unknown-field handling, semantic-field participation, canonicalization-version binding, and failure when comparison rules are invalid or missing.

Exact encoding, hash, signature, integrity mechanism and implementation library remain pending.

## E. Contract Compatibility Matrix

| Transition or condition | Required logical behavior | Contract Governance decision | Messaging/API Event Architecture decision |
| --- | --- | --- | --- |
| Same supported version | Interpret under the recorded version | Semantic rules | Preserve and validate version |
| Additive non-semantic metadata | May be compatible | Classification | Transport preservation |
| Additive optional semantic field | Compatible only with explicit absent/default rule | Equality and compatibility rule | Capability/version signaling |
| Required or meaning-changing field | Breaking unless explicitly governed | New version/transformation policy | Reject, route or negotiate supported version |
| Unknown enum | No silent default | Enum evolution | Unsupported disposition behavior |
| Unknown semantic field | No guessed equality | Compatibility classification | Reject/hold under approved rules |
| Unsupported `ContractVersion` | Cannot produce successful ingestion | Support matrix | Durable unsupported disposition |
| Unauthorized downgrade | Reject | Downgrade prohibition | Preserve original and attempted version evidence |
| Pending old obligation after upgrade | Preserve original committed semantics | Coexistence/deprecation | Select compatible consumer/decoder path |
| Approved transformation | Preserve original evidence and provenance | Transformation semantics and governance | Authorized transformer/re-attestation behavior |
| Retry/re-drive/reconciliation | Preserve original key, versions and immutable content | Recovery compatibility | New transport metadata only |
| Sovereign disconnection | Locally supported contracts remain authoritative | Local compatibility policy | No mandatory synchronous Central authority |
| Sovereign reconnection conflict | No automatic winner or silent reinterpretation | Conflict/reconciliation semantics | Conflict-preserving exchange |

Numerical support windows, final version matrix, migration implementation and wire format are not approved.

## F. Audit Confirmation and Disposition Matrix

Only Audit Domain owns authoritative durable-ingestion confirmation. Confirmation is candidate-bound to `AuditAuthority`, the full `ObligationKey`, confirmation contract version, safe Audit record evidence, durable processing evidence and successful ingestion outcome.

### F.1 Exchange alternatives

| Alternative | Benefit | Main constraint | Status |
| --- | --- | --- | --- |
| Authenticated Audit-owned online lookup | Clear authoritative source for recovery/reconciliation | Audit availability, caller authorization and non-disclosing denial | Preferred logical candidate; not an approved protocol |
| Independently verifiable receipt | Reduces lookup dependency | Authenticity, key lifecycle, replay and revocation complexity | Candidate; Security review required |
| Hybrid lookup and receipt | Recovery flexibility | Freshness, supersession and dual-evidence conflict | Candidate; separate decision required |

Online lookup must not become a mandatory synchronous dependency in the successful Customer mutation path merely because it is preferred for reconciliation and recovery.

### F.2 Outcome and disposition separation

| Outcome/disposition | Required meaning | May establish Audit ingestion confirmation? |
| --- | --- | --- |
| Successful authoritative ingestion | Valid supported evidence durably committed by Audit | Yes, subject to approved authenticity rules |
| Idempotent duplicate | Same full key and same semantic content | Reuses/reconstructs existing successful outcome; no second effect |
| Semantic conflict | Same full key and different immutable content | No |
| Authentication/authorization rejection | Invalid producer, Tenant or requester authority | No |
| Unsupported contract/version | Type/version cannot be processed | No |
| Invalid evidence | Contract or evidence invalid | No |
| Quarantined evidence | Evidence retained under an approved quarantine policy | No |
| Indeterminate/unresolved reconciliation | Authoritative evidence insufficient or conflicting | No |
| Confirmation-security failure | Forged, replayed, stale, mismatched or unauthorized evidence | No |

Publisher success, broker ACK, transport delivery disposition, DLQ placement, quarantine, retry and producer reconciliation do not create Audit confirmation.

Historical durable-ingestion evidence, the current authoritative disposition, freshness/supersession information and recovery reconciliation evidence must remain distinguishable. The exact trust protocol and runtime transition mechanism remain pending.

## G. Messaging Envelope and Recovery Matrix

| Concern | Producer semantic authority | Transport/broker responsibility | Recovery authority | Audit authority | Contract authority |
| --- | --- | --- | --- | --- | --- |
| Original semantic fact | Customer | Carry only | Must not rewrite | Validate/ingest | Define meaning |
| Producer provenance | Customer plus trusted authority mapping | Preserve | Preserve original provenance | Independently validate | Define required evidence |
| Tenant binding | Customer establishes authoritative scope | Preserve; mutable header not authority | Exact current action scope required | Independently validate | Define field semantics |
| Contract type/version | Producer emits supported contract | Preserve/route | Preserve original versions | Validate support | Govern compatibility |
| Immutable semantic content | Customer | Must not mutate | Must not rewrite | Compare and disposition | Define equality |
| Transport attempt identity | Not semantic | Own and record | New attempt permitted | Diagnostic only | Classify as non-semantic |
| Broker/intermediary identity | Not original producer | Peer/transport identity | Not producer authority | Must distinguish | Define re-attestation constraints |
| Authorized re-attestation | Original producer remains attributable | Intermediary identity and transformation separately recorded | Requires explicit authority | Validate chain | Govern transformation |
| Publication ACK | No ingestion claim | Transport evidence only | Recovery signal only | Not confirmation | No semantic success |
| Retry/re-drive | Original key and content unchanged | Add attempt metadata | Current operation-specific authorization | Revalidate | Original compatibility retained |
| DLQ/quarantine | Original evidence retained | Delivery/disposition state | Release/re-drive separately authorized | No success implication | Revalidate version and semantics |
| Ordering | Contract-specific | Reordering possible | Replay-safe handling | Consumer policy | Decide required ordering scope |
| Outage recovery | Customer durable evidence authoritative on producer side | Bounded retry/re-drive | Execute authorized recovery | Audit confirmation/reconciliation authoritative | Preserve version coexistence |

Event handling assumes at-least-once delivery, possible duplication and possible reordering. No end-to-end exactly-once guarantee is asserted. Receiver-verifiable provenance is a preferred logical candidate; exact envelope, broker topology, retry scheduler and protocol are pending.

## H. CG-01 through CG-05 Decision Requests

All five entries have status `PROPOSED — SPECIALIST REVIEW REQUIRED`.

### CG-01 — Obligation and Event Semantic Contract

- **Proposed invariant:** Complete `ObligationKey` defines obligation identity; version-bound immutable evidence defines semantic equality; transport attempts remain separate.
- **Preferred logical direction:** typed field classes with explicit ownership, participation and transfer boundaries.
- **Alternatives:** representation choices that preserve identical semantics and minimization.
- **Threats addressed:** producer/Tenant substitution, identity collision, sensitive-data leakage and transport metadata becoming business truth.
- **Required evidence:** normative field dictionary, ownership, validation, minimization and equality-participation matrix.
- **Open Decisions:** `OD-008`, `OD-020`.
- **Contract Governance request:** approve, amend or reject field semantics and participation.
- **Messaging/API Event Architecture request:** independently decide envelope placement and preservation requirements.
- **Dependencies:** Customer, Audit, Identity/Platform Security, Tenant Security and Security Architecture.
- **NON-AUTHORITATIVE analyst recommendation:** approve logical separation with boundaries; keep final schema and unresolved fields pending.

### CG-02 — Canonicalization and Semantic Equality

- **Proposed invariant:** Equality is typed, deterministic, version-bound and serialization-independent.
- **Preferred logical direction:** versioned canonical semantic projection.
- **Alternatives:** schema-native encoding, self-describing representation or typed field comparison.
- **Threats addressed:** false duplicate/conflict, normalization ambiguity and digest misuse.
- **Required evidence:** rules for null/default, Unicode, numbers, timestamps, enums, unknown fields and version binding.
- **Open Decisions:** `OD-008`, `OD-020`.
- **Contract Governance request:** decide the normative comparison contract.
- **Messaging/API Event Architecture request:** decide how comparison-version evidence is preserved across transport.
- **Dependencies:** Security Architecture for authenticity/integrity mechanisms.
- **NON-AUTHORITATIVE analyst recommendation:** approve the deterministic requirement only; defer encoding, algorithm and library.

### CG-03 — Contract Version Compatibility

- **Proposed invariant:** Original committed semantics are never silently reinterpreted; unsupported or downgraded versions cannot succeed.
- **Preferred logical direction:** explicit compatibility classes and coexistence governance.
- **Alternatives:** strict major-version isolation, negotiated coexistence or explicitly authorized transformation.
- **Threats addressed:** downgrade, silent reinterpretation, stranded pending obligations and Sovereign version conflict.
- **Required evidence:** supported-version matrix, upgrade/recovery scenarios and transformation provenance.
- **Open Decisions:** `OD-008`, `OD-020`.
- **Contract Governance request:** decide compatibility, deprecation and transformation rules.
- **Messaging/API Event Architecture request:** decide negotiation, routing and consumer compatibility behavior.
- **Dependencies:** Customer/Audit owners and Sovereign-specific Security/Operations.
- **NON-AUTHORITATIVE analyst recommendation:** approve foundational version preservation; keep windows and migration implementation pending.

### CG-04 — Audit Confirmation and Disposition Contract

- **Proposed invariant:** Only Audit-owned durable evidence can establish successful Audit ingestion; every other disposition remains distinct.
- **Preferred logical direction:** authenticated Audit-owned online lookup for recovery/reconciliation.
- **Alternatives:** independently verifiable receipt or hybrid lookup/receipt.
- **Threats addressed:** fake ACK-derived success, replay, cross-Tenant lookup, forged confirmation and silent supersession.
- **Required evidence:** full-key binding, requester authorization, freshness/replay, supersession and non-disclosing denial.
- **Open Decisions:** `OD-008`, `OD-011`, `OD-012`, `OD-020`.
- **Contract Governance request:** decide outcome vocabulary and semantic transitions.
- **Messaging/API Event Architecture request:** decide exchange pattern and transport behavior.
- **Dependencies:** Audit Domain, Identity/Platform Security, Tenant Security and Security Architecture.
- **NON-AUTHORITATIVE analyst recommendation:** retain online lookup as preferred candidate; keep protocol and trust mechanism pending.

### CG-05 — Messaging Envelope and Recovery Compatibility

- **Proposed invariant:** Broker mediation, retry and re-drive preserve original producer authority, Tenant binding, versions and immutable semantics.
- **Preferred logical direction:** receiver-verifiable provenance envelope.
- **Alternatives:** authenticated metadata propagation or explicitly authorized intermediary re-attestation.
- **Threats addressed:** broker-as-producer, header spoofing, unauthorized re-drive, semantic rewrite and ungoverned transformation.
- **Required evidence:** chain of custody, direct-consumer validation, retry/re-drive, version and outage-recovery cases.
- **Open Decisions:** `OD-008`, `OD-011`, `OD-012`, `OD-019`, `OD-020`.
- **Contract Governance request:** decide immutable versus transport semantics and transformation limits.
- **Messaging/API Event Architecture request:** decide envelope, attempt metadata, delivery, failure and recovery behavior.
- **Dependencies:** Identity/Platform Security, Tenant Security, Operations, Security Architecture and Sovereign-specific Security.
- **NON-AUTHORITATIVE analyst recommendation:** approve logical authority separation with boundaries; keep wire format, topology and scheduler pending.

## I. Negative-Test and Evidence Gap Matrix

All execution statuses remain `NOT_EXECUTED`. Entries marked `NEW_CANDIDATE — NOT REGISTERED` allocate no official identifier.

| Failure input | Required invariant/outcome | Evidence owner | Repository traceability/status |
| --- | --- | --- | --- |
| Same full key with changed immutable content | Semantic conflict; no confirmation | Audit | `NT-011/012` relationship; `NOT_EXECUTED` |
| Same semantics with different serializer order | Equal canonical semantics | Contract Governance evidence | `NEW_CANDIDATE — NOT REGISTERED` |
| Absent versus null/default | Apply explicit versioned rule or reject/hold | Contract Governance | `NEW_CANDIDATE — NOT REGISTERED` |
| Unicode normalization mismatch | Normalize under approved rule or reject deterministically | Contract Governance | `NEW_CANDIDATE — NOT REGISTERED` |
| Timestamp timezone/precision mismatch | Apply approved instant/precision rule; never silently guess | Contract Governance | `NEW_CANDIDATE — NOT REGISTERED` |
| Unsupported `ContractVersion` | Unsupported disposition; no success | Audit | Existing S5 gap; `NOT_EXECUTED` |
| Unauthorized downgrade | Reject and preserve original/attempted version evidence | Audit / Contract Governance | Existing S5 gap; `NOT_EXECUTED` |
| Old pending obligation after upgrade | Preserve original supported semantics | Customer/Audit | `NEW_CANDIDATE — NOT REGISTERED` |
| Forged `ProducerAuthority` | Fail closed | Audit/Security | `NT-009`; `NOT_EXECUTED` |
| Broker identity substituted for producer | Reject; original producer remains required | Audit | `NEW_CANDIDATE — NOT REGISTERED` |
| Mutable Tenant/Producer header spoofing | Reject after independent validation | Audit/Tenant Security | `NT-007/009` relationship; `NOT_EXECUTED` |
| Unauthorized intermediary re-attestation | Reject | Receiving boundary | `NEW_CANDIDATE — NOT REGISTERED` |
| Broker ACK treated as confirmation | No confirmation or state advancement | Customer/Audit | `TC-AC-006/007` relationship; `NOT_EXECUTED` |
| Old/replayed confirmation | No unauthorized state advancement | Audit/Security | `NEW_CANDIDATE — NOT REGISTERED` |
| Confirmation superseded by invalid/conflict disposition | Preserve evidence and current disposition; no silent success | Audit | `NEW_CANDIDATE — NOT REGISTERED` |
| Cross-Tenant Audit ingestion | Fail closed with no cross-Tenant disclosure/effect | Audit | `NT-007/009`; `NOT_EXECUTED` |
| Re-drive changes immutable semantics | Reject/conflict; no success | Customer/Audit | `NT-013/016` relationship; `NOT_EXECUTED` |
| Unsupported contract during Sovereign disconnection | Local unsupported disposition | Sovereign Audit | `NEW_CANDIDATE — NOT REGISTERED` |
| Reconnection with conflicting versions | Preserve conflict; no automatic winner | Sovereign authority | `NT-019/020` relationship; `NOT_EXECUTED` |

Remaining evidence gaps include final field participation, canonicalization specification, supported-version matrix, coexistence/deprecation policy, transformation/re-attestation authority, provenance authenticity, confirmation freshness/replay/supersession, executable consumer conformance tests and profile-specific recovery evidence.

## J. Contract Governance Decision Register

| Working item | Requested Contract Governance disposition | Required evidence | Status |
| --- | --- | --- | --- |
| `CG-01` | Field classes, ownership, minimization and semantic participation | Normative field dictionary | `PENDING` |
| `CG-02` | Canonicalization and equality contract | Normalization and conformance specification | `PENDING` |
| `CG-03` | Compatibility, coexistence, deprecation and transformations | Version matrix and evolution policy | `PENDING` |
| `CG-04` | Confirmation/disposition vocabulary and transitions | State/evidence semantics | `PENDING` |
| `CG-05` | Immutable versus transport semantics and transformation limits | Envelope-independent semantic rules | `PENDING` |

`CONTRACT_GOVERNANCE_APPROVAL = PENDING`

## K. Messaging/API Event Architecture Decision Register

| Working item | Requested Messaging/API Event Architecture disposition | Required evidence | Status |
| --- | --- | --- | --- |
| `CG-01` | Envelope placement and required propagation | Logical envelope mapping | `PENDING` |
| `CG-02` | Preservation of canonicalization-version evidence | Cross-serializer interoperability design | `PENDING` |
| `CG-03` | Negotiation, routing and consumer compatibility behavior | Producer/consumer compatibility design | `PENDING` |
| `CG-04` | Lookup/receipt/hybrid exchange and delivery behavior | Exchange and failure-semantics design | `PENDING` |
| `CG-05` | Provenance envelope, attempts, ACK/DLQ, ordering and re-drive | End-to-end transport/recovery design | `PENDING` |

`MESSAGING_API_EVENT_ARCHITECTURE_APPROVAL = PENDING`

## L. Cross-Specialist Dependencies and Handoffs

### L.1 Reviews that may begin independently

- Contract Governance may review field taxonomy, canonicalization properties and compatibility classes.
- Messaging/API Event Architecture may review authority separation, envelope constraints and retry/re-drive metadata.
- Identity/Platform Security may review workload-to-producer trust without choosing the final event schema.
- Tenant Security may review Tenant binding and cross-Tenant failure semantics without choosing the final transport.

### L.2 Decisions requiring coordinated but independent dispositions

- Final logical envelope requires both Contract Governance and Messaging/API Event Architecture dispositions.
- Producer provenance depends on Identity/Platform Security and Security Architecture.
- Tenant binding and confirmation lookup depend on Tenant Security.
- Confirmation authenticity depends on Audit Domain, both requested specialists and Security Architecture.
- Quarantine/re-drive lifecycle depends on Audit Domain, Messaging/Operations and Operational Policy Governance.
- Sovereign disconnection/reconnection depends on Sovereign-specific Security and Operations.
- Independent Security Review remains required after specialist dispositions; it is not replaced by them.
- Runtime contract conformance and compatibility evidence remains blocked until an approved test strategy addresses `OD-020` or an equivalent decision.

Customer and Audit Domain approvals remain bounded to their recorded authority. Neither is transferred to the requested specialists, and neither specialist may overwrite Domain-owned meaning.

## M. Independent Authorized Reviewer Disposition Templates

Blank fields are intentional. No blank field implies approval. Allowed outcomes are `APPROVE_WITH_BOUNDARIES`, `AMEND`, `REJECT`, `BLOCKED`, and `EVIDENCE_REQUIRED`.

### M.1 Template A — Contract Governance

| Reviewer field | Reviewer-supplied value |
| --- | --- |
| Reviewer identity/authenticated reference |  |
| Verified Contract Governance authority and scope |  |
| Reviewed Git baseline and document SHA-256 |  |
| Review date, if supplied |  |
| Exact accepted/rejected semantic scope |  |
| Required amendments |  |
| Evidence requests |  |
| Dependencies and limitations |  |
| Authenticated review-record reference |  |

| Item | Disposition | Accepted/rejected scope or replacement wording | Rationale/evidence | Conditions/dependencies |
| --- | --- | --- | --- | --- |
| `CG-01` |  |  |  |  |
| `CG-02` |  |  |  |  |
| `CG-03` |  |  |  |  |
| `CG-04` |  |  |  |  |
| `CG-05` |  |  |  |  |

### M.2 Template B — Messaging/API Event Architecture

| Reviewer field | Reviewer-supplied value |
| --- | --- |
| Reviewer identity/authenticated reference |  |
| Verified Messaging/API Event Architecture authority and scope |  |
| Reviewed Git baseline and document SHA-256 |  |
| Review date, if supplied |  |
| Exact accepted/rejected Messaging/API scope |  |
| Required amendments |  |
| Evidence requests |  |
| Dependencies and limitations |  |
| Authenticated review-record reference |  |

| Item | Disposition | Accepted/rejected scope or replacement wording | Rationale/evidence | Conditions/dependencies |
| --- | --- | --- | --- | --- |
| `CG-01` |  |  |  |  |
| `CG-02` |  |  |  |  |
| `CG-03` |  |  |  |  |
| `CG-04` |  |  |  |  |
| `CG-05` |  |  |  |  |

A specialist disposition is not a Security Architecture approval, Independent Security Review sign-off, risk acceptance, implementation verification or approval by the other specialist authority.

## N. Explicit Non-Approvals and Governance Preservation

This request does **not** approve:

- `CG-01` through `CG-05` or either specialist register;
- a final event/API schema, envelope, wire format or endpoint;
- canonical encoding, hash, signature, cryptographic mechanism, key infrastructure or library;
- supported-version matrix, coexistence duration, deprecation window or migration implementation;
- final lookup, receipt, confirmation or disposition protocol;
- broker topology, queue/exchange naming, retry scheduler, ordering mechanism or recovery technology;
- end-to-end exactly-once behavior;
- any SR-CAND item, risk rating, mitigation, risk acceptance or security exception;
- implementation correctness, runtime security, executed negative tests, executable DURABLE_DEFER or Production Readiness.

The following governance state is preserved exactly:

```text
V3-003 = IN PROGRESS
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
CONTRACT_GOVERNANCE_APPROVAL = PENDING
MESSAGING_API_EVENT_ARCHITECTURE_APPROVAL = PENDING
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

The next bounded activity is independent authorized specialist review of the exact content hash of this request and its pinned sources. Each reviewer must establish identity, authority, scope, reviewed baseline, limitations and item-specific rationale separately. Repository recording alone must not upgrade any approval or readiness status.
