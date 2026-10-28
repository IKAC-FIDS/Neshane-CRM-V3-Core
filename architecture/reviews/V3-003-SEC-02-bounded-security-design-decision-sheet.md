# V3-003 SEC-02 — Semantic Integrity and Contract Compatibility

## A. Verified Baseline and Document Control

| Field | Value |
| --- | --- |
| Status | **DRAFT — SECURITY REVIEW REQUIRED** |
| Task | V3-003 — NFR and Threat Assumptions |
| Scope | Semantic identity, deterministic comparison, contract compatibility, conflict disposition and recovery integrity for Customer-produced Audit Obligations |
| Working labels | SI-01 through SI-05 are local working labels only; they are not official V3-003-DEC, ADR or Security Requirement identifiers |
| Project and Domain bounded dispositions | **APPROVED_WITH_BOUNDARIES** |
| Messaging/API Event Architecture approval | **PENDING** |
| Contract Governance approval | **PENDING** |
| Security Architecture approval | **PENDING** |
| Repository | `IKAC-FIDS/Neshane-CRM-V3-Core` |
| Branch at materialization | `main` |
| Git HEAD at materialization | `25e54a6fbd25ffee85fa97b6ee54509c31ae41e9` |
| Worktree and index before materialization | Clean |
| Customer/Audit Technical Contract SHA-256 | `56e71f3ee0537bfc70d0e3f02602175d0e0eb87510fbb7ab43125f37c4010412` |
| Security Review Input Manifest SHA-256 | `a73fc9346361fcd95ca6f4914cff53be7201dcfc35df9a71334d14d442d3ef22` |
| SEC-01 Decision Sheet SHA-256 | `0394a08682ed911f5c61839ca371e0852072e5621f9b33ffb0e322fec738ca7b` |
| Independent Security Review | **NOT_SIGNED_OFF** |
| Implementation evidence | **NOT_VERIFIED** |
| Negative-test execution | **NOT_EXECUTED** |
| Executable DURABLE_DEFER | **NOT APPROVED** |

This document records five bounded Project/Domain Owner design dispositions. It does not record approval by Messaging/API Event Architecture, Contract Governance, Security Architecture or an Independent Security Reviewer. It does not establish a fully approved SEC-02 Security Contract, an approved Event schema, implementation authorization or runtime evidence.

### A.1 Recorded disposition authority

| Field | Recorded value |
| --- | --- |
| Confirmed authority | Project Owner; Customer Domain Owner; Audit Domain Owner; Messaging/Operations Owner |
| Approval evidence | Explicit user instruction authorizing the five bounded dispositions recorded in section H |
| Approval date | Not recorded |
| Messaging/API Event Architecture authority | Not claimed; approval remains pending |
| Contract Governance authority | Not claimed; approval remains pending |
| Security Architecture authority | Not claimed; approval remains pending |
| Independent Security Reviewer authority or sign-off | Not claimed; review remains not signed off |

### A.2 Authoritative and analytical basis

- `architecture/reviews/V3-003-customer-audit-technical-contract-draft.md`.
- `architecture/reviews/V3-003-security-review-input-manifest.md`, particularly S4 through S8 and Work Package 2.
- `architecture/reviews/V3-003-SEC-01-bounded-security-design-decision-sheet.md`.
- `V3-003-DEC-009` through `V3-003-DEC-014` in the V3-003 Decision Record.
- ADR-V3-002, ADR-V3-003, ADR-V3-004, ADR-V3-005, ADR-V3-007, ADR-V3-008, ADR-V3-010 and ADR-V3-012.
- Messaging, Security, Persistence, Service Architecture and API Design standards.
- `OD-008`, `OD-011`, `OD-012`, `OD-014`, `OD-019`, `OD-020` and `OD-023`.

All existing Customer, Audit, Messaging/Operations and SEC-01 bounded dispositions retain their recorded scope. SEC-02 does not reopen or broaden them.

## B. Six-Class Semantic Field Classification Matrix

The complete authoritative obligation identity remains:

`ProducerAuthority + TenantScope + ObligationId`

| Class | Candidate conceptual fields or evidence | Semantic role | Boundary and unresolved choices |
| --- | --- | --- | --- |
| A — Identity-defining | `ProducerAuthority`, `TenantScope`, `ObligationId` | Together define the complete `ObligationKey` and lookup/idempotency scope | Key principle is already approved with boundaries; field representation, identifier generation and validation mechanics remain pending |
| B — Immutable semantic evidence | `ContractType`, `ContractVersion`, `OperationType`, `MutationId`, `SafeCustomerRef`, `ActorRef`, `Outcome`, `OccurredAt`, `CorrelationRef` | Candidate immutable meaning used to establish semantic equality for one committed obligation | Conceptual evidence baseline only; exact schema, field representation, inclusion and comparison significance remain unapproved |
| C — Conditional semantic evidence | `ChangeCategoryRef` for CUS-UPDATE; `CausationRef` where an approved causal need exists; `SemanticContentVersion`; any additional field expressly required by the approved comparison contract | Participates only when the applicable contract and semantic version require it | Taxonomy, canonical inclusion, sensitivity and compatibility rules remain pending |
| D — Transport-attempt metadata | `TransportAttemptId`, broker delivery ID, attempt number, publication timestamp, route/exchange/queue observations, ACK/NACK, retry/backoff/DLQ information, dispatcher instance | Describes one transport attempt and may vary without changing obligation meaning | Must never establish semantic equality, ProducerAuthority, Tenant authority or Audit ingestion |
| E — Customer-owned recovery evidence not transferred by default | `CommandIdentityRef`, Customer commit evidence, durable mutation/obligation outcome evidence, pending/recovery lifecycle state, `ProducerEvidenceRef`, transport-attempt history | Enables Customer-owned recovery, reproduction and reconciliation | Transfer requires a separately approved and minimized cross-domain need; private persistence references remain prohibited |
| F — Prohibited sensitive content | Credentials, tokens, complete Customer snapshots, unnecessary Customer data, unnecessary sensitive old/new values, raw private-database locators | Never valid comparison or convenience payload | Must not cross the Customer/Audit contract boundary |

### B.1 Classification boundaries

- `MutationId` is Customer mutation traceability evidence; it is not Audit ingestion identity or authorization proof.
- `ContractType`, `ContractVersion` and `SemanticContentVersion` govern interpretation; they are not transport metadata.
- `SafeCustomerRef` must remain a minimized reference and cannot silently become a full Customer snapshot.
- `ChangeCategoryRef` is conceptually required for CUS-UPDATE, but its taxonomy remains unapproved.
- `CausationRef` is conditional and shall not be populated without an approved causal purpose.
- `OccurredAt`, `CorrelationRef` and `ActorRef` are immutable evidence candidates, but their exact comparison significance requires explicit contract-owner agreement.
- The Customer-owned durable obligation must preserve enough immutable evidence to reproduce its historical meaning after recovery without reconstructing it from mutable current Customer state.
- Not every metadata field participates in semantic comparison. The future comparison specification must define the exact field projection for each `SemanticContentVersion`.

## C. Canonicalization Requirements and Alternative Comparison

### C.1 Required properties

A future approved canonicalization contract shall define:

1. An explicit semantic field projection for each supported `ContractVersion` and `SemanticContentVersion`.
2. Deterministic field inclusion and ordering.
3. The distinct treatment of absent, optional, explicit `null` and default values.
4. Unicode and string normalization without implicit trimming, locale conversion or case folding unless the field contract explicitly requires it.
5. Domain-defined numeric representations that avoid floating-point or textual ambiguity.
6. Timestamp normalization by instant, timezone and precision without changing the original business meaning.
7. Enum evolution and unsupported-value handling without silent default mapping.
8. Unknown-field behavior for each compatibility relationship.
9. Explicit version binding so a newer implementation cannot silently apply new rules to an older committed obligation.
10. Independence from incidental serializer behavior, property order and transport representation.
11. Diagnostic evidence sufficient to explain a mismatch without exposing prohibited sensitive content.
12. Separate integrity and provenance validation; semantic equality alone does not authenticate a producer or authorize a Tenant.

### C.2 Approach comparison

| Approach | Strength | Failure mode or trade-off | Proposed disposition |
| --- | --- | --- | --- |
| Typed semantic projection followed by deterministic encoding | Makes field ownership, types and semantic-version selection explicit | Requires a governed projection and encoding contract shared through versioned contract definitions | **PREFERRED LOGICAL DIRECTION — NOT SELECTED OR APPROVED** |
| Schema-bound canonical binary form | Structurally constrained and compact | Determinism, unknown-field preservation and schema evolution may vary by implementation | Permissible; final technology and rules pending |
| Canonical JSON or other textual form | Inspectable and broadly portable | Unicode, number, null/default and serializer differences create ambiguity unless exhaustively specified | Permissible only with a complete canonical specification |
| Direct typed field-by-field comparison | Transparent and avoids raw serialization coupling | Producer and consumer implementations can diverge without shared conformance evidence | Permissible for bounded designs; contract tests required later |
| Raw wire-byte comparison | Simple to implement | Treats harmless serialization changes as semantic conflict and couples meaning to transport bytes | Rejected as the general equality criterion |
| Digest/hash-only comparison | Compact comparison hint | Hides canonicalization errors, is difficult to diagnose and proves neither authority nor authorization | Rejected as sole authoritative proof |

### C.3 Canonical representation versus integrity representation

A canonical semantic representation answers which approved fields and normalization rules define equality. A digest, MAC or signature—if later approved—binds an integrity value to a particular representation under a selected mechanism.

A matching digest alone does not prove:

- authenticated `ProducerAuthority`;
- authoritative `TenantScope` or Tenant authorization;
- contract compatibility;
- absence of semantic ambiguity;
- durable Audit ingestion; or
- reconciliation completion.

No canonical encoding, digest, signature, cryptographic algorithm, key hierarchy or implementation library is selected by this document.

## D. Contract Version Compatibility Matrix

| Transition or condition | Candidate classification | Required candidate behavior |
| --- | --- | --- |
| Same supported `ContractVersion` and `SemanticContentVersion` | Compatible candidate | Interpret and compare using the exact rules bound to those versions |
| Add optional non-semantic field | Potentially backward-compatible | Older consumers may ignore it only when it cannot affect meaning, authorization or required validation |
| Add optional semantic field | Conditional | Requires explicit inclusion rules and normally a new `SemanticContentVersion` |
| Add a required field | Incompatible by default | Requires a new versioned contract path or an explicitly approved compatibility and migration plan |
| Remove a required semantic field | Incompatible | Must not be treated as the prior semantics |
| Rename a field without an explicit version mapping | Incompatible or ambiguous | Requires an approved mapping and coexistence behavior |
| Reinterpret an existing field | Breaking semantic change | Requires a new contract version; silent reinterpretation is prohibited |
| Add an enum value | Conditional | Unsupported consumers reject or durably classify it; no silent default mapping |
| Receive an unknown field | Conditional | May be ignored only where the governing compatibility contract permits it and it is outside the applicable semantic projection |
| Introduce a later default | Unresolved | Must not retroactively change a committed obligation's semantics |
| Replay an old committed obligation after upgrade | Supported only while its original versions remain supported | Use its original contract and semantic comparison rules |
| Receive an old version outside an approved support window | Unsupported contract | Do not ingest successfully; preserve a durable unsupported disposition where policy permits |
| Attempt an unapproved downgrade | Rejected | Must not remove mandatory semantics, provenance or validation |
| Change serialization while preserving semantics | Potentially compatible | Compare the canonical semantic projection rather than raw bytes |
| Transform an existing obligation to a newer representation | Separate migration decision required | Preserve original evidence, original versions and traceable transformation provenance |

An obligation's original semantics shall not silently change because newer software or a newer contract version has been deployed.

No exact compatibility matrix, support window, coexistence duration, version numbering convention, deprecation policy, migration procedure or compatibility tool is approved here. These remain dependent on `OD-008` and `OD-020`.

## E. Conflict and Disposition Matrix

| Input condition | Conceptual classification | Required candidate outcome |
| --- | --- | --- |
| Complete key matches and canonical semantic content matches | Idempotent duplicate | Reuse or reconstruct the original authoritative Audit outcome; create no second authoritative effect |
| Complete key matches and canonical semantic content differs | Semantic conflict | No successful ingestion confirmation; preserve durable conflict visibility; suspend automatic resolution; escalate |
| Complete key matches but semantic version is unsupported | Unsupported contract | Do not guess equality or ingest successfully; record an authorized unsupported disposition where policy permits |
| Same `ObligationId` with altered `ProducerAuthority` | Authentication/provenance rejection | This is not the same complete `ObligationKey`; fail closed and escalate |
| Same `ObligationId` with altered `TenantScope` | Tenant authorization mismatch | This is not the same complete `ObligationKey`; isolate and fail closed; never reconcile across Tenants |
| Semantic content matches and only transport metadata differs | Transport-attempt variation | Not a semantic conflict; continue the duplicate/retry path |
| Required producer or Tenant provenance is incomplete | Authentication/authorization rejection | No ingestion confirmation and no automatic reconciliation |
| Customer and Audit authoritative evidence disagree | Unresolved reconciliation | Preserve both evidence views; no automatic winner or cross-domain overwrite |
| Invalid or quarantine disposition exists | Invalid/quarantined evidence | Remains distinct from successful Audit ingestion |
| Raw bytes differ but canonical semantic projection matches | Idempotent duplicate candidate | Serializer differences alone do not create a conflict |
| Canonicalization version is missing or ambiguous | Unsupported or indeterminate | No comparison-based success; perform authorized escalation/recovery |
| Matching semantic fingerprint but invalid authority evidence | Authentication/authorization rejection | A matching digest cannot override failed trust or Tenant validation |
| Confirmation binding is invalid despite matching content | Confirmation-security failure | Do not close Customer reconciliation or assert Audit ingestion |

Conflict handling must not mutate Customer Business Facts, overwrite Audit-owned evidence, fabricate confirmation or convert quarantine into successful ingestion.

The final conflict state machine, disposition retention, correction authority, quarantine release and escalation workflow remain pending.

## F. Recovery Integrity Matrix

| Scenario | Required integrity property | Prohibited interpretation or action |
| --- | --- | --- |
| Normal publication | Publish only a durably committed obligation with its original key, versions and immutable semantic content | Reconstruct historical meaning from mutable current Customer state |
| Duplicate delivery | Apply Audit-owned idempotency using the complete key and canonical semantic form | Create a second authoritative Audit effect |
| Customer crash before durable commit | Obligation is ineligible unless the Customer-owned durability boundary completed | Publish an in-memory or partially committed obligation |
| Customer crash after durable commit | Recover from Customer-owned durable evidence | Treat process-memory loss as loss of authoritative semantic truth |
| Concurrent publishers or re-drive workers | Preserve one semantic obligation and use distinct attempt identities | Generate a new obligation or effect per attempt |
| Automated retry | Preserve original key, contract versions and semantic content | Upgrade the obligation silently to the newest representation |
| Manual re-drive | Revalidate authority, Tenant, pending evidence, compatibility and conflict state | Allow the operator to mutate original semantics or provenance |
| Audit outage | Keep the producer obligation pending and recoverable | Treat publisher success or broker acknowledgement as ingestion |
| Consumer crash | Acknowledge only after the applicable durable Audit processing boundary | Acknowledge before durable handling and silently lose the effect |
| Long-lived pending obligation during upgrade | Retain the original semantic rules throughout the approved coexistence window | Apply new defaults or reinterpret old fields |
| Original version no longer supported | Produce unsupported disposition and escalation evidence | Silently upgrade, downgrade or discard the obligation |
| Lost confirmation | Recover through authenticated, authorized Audit-owned lookup or an independently approved equivalent | Infer ingestion from transport history |
| Dedicated Sovereign disconnection | Use locally authoritative contracts, evidence and recovery authority | Introduce mandatory synchronous Central authority |
| Dedicated Sovereign reconnection | Reconcile without overwriting locally authoritative Customer or Audit evidence | Automatically select Central evidence as the winner |

Recovery logic may generate new transport-attempt metadata, monitoring evidence and authorized operational Audit evidence. It shall not modify the authoritative `ObligationKey`, original contract versions or immutable semantic truth.

Claiming/leasing, scheduling, concurrency implementation, retry limits, support windows, profile-specific runbooks and operational thresholds remain pending.

## G. Negative-Test Candidates and Required Evidence

All execution statuses remain **NOT_EXECUTED**. Entries marked `NEW_CANDIDATE — NOT REGISTERED` do not allocate official test identifiers.

| Test input | Required assertion | Required observable evidence | Traceability/status |
| --- | --- | --- | --- |
| Same full key and same canonical content with a different attempt ID | One authoritative Audit effect; duplicate path | Existing outcome and duplicate disposition | `NT-010`; **NOT_EXECUTED** |
| Malicious replay outside authorized provenance/context | No new effect or confirmation | Durable rejection/security evidence | `NT-011`; **NOT_EXECUTED** |
| Valid messages delivered out of order | Contract-specific ordering behavior; no global-order assumption | Ordering disposition and correlation | `NT-012`; **NOT_EXECUTED** |
| Same semantic values with different field order | Equal canonical semantics | Selected semantic version and matching result | `NEW_CANDIDATE — NOT REGISTERED` |
| One message omits a field and another sends explicit null | Apply the explicit versioned rule; otherwise indeterminate | Comparison/disposition evidence | `NEW_CANDIDATE — NOT REGISTERED` |
| Visually equivalent strings use different Unicode forms | Apply the approved normalization or reject deterministically | Normalization rule/version | `NEW_CANDIDATE — NOT REGISTERED` |
| Equivalent-looking numeric forms differ | Use the domain-defined numeric form | Canonical value/version | `NEW_CANDIDATE — NOT REGISTERED` |
| Same instant expressed with different timezone offsets | Apply the approved instant/precision rule | Normalized time evidence | `NEW_CANDIDATE — NOT REGISTERED` |
| Same key contains timestamp precision loss | Conflict or expressly approved equivalence; never silent | Precision rule and disposition | `NEW_CANDIDATE — NOT REGISTERED` |
| Unknown enum value | Unsupported contract/value; no default mapping | Durable unsupported evidence | `NEW_CANDIDATE — NOT REGISTERED` |
| Unknown semantic field without compatible rules | No silent equality decision | Version/compatibility rejection | `NEW_CANDIDATE — NOT REGISTERED` |
| Newer obligation is relabeled as an older version | Reject downgrade | Original and attempted version evidence | Existing S5 downgrade gap; **NOT_EXECUTED** |
| Pending old obligation is processed after upgrade | Preserve original supported semantics | Decoder/version selection evidence | `NEW_CANDIDATE — NOT REGISTERED` |
| Same full key contains an altered semantic field | No success confirmation; semantic conflict | Both evidence views and escalation | `NT-011/012` relationship; **NOT_EXECUTED** |
| Same `ObligationId` has an altered producer | Fail closed as provenance mismatch | Authentication and mismatch evidence | `NT-009`; **NOT_EXECUTED** |
| Same `ObligationId` has an altered Tenant | Fail closed; no cross-Tenant ingestion | Tenant-scoped denial evidence | `NT-007/009`; **NOT_EXECUTED** |
| Only transport metadata changes | Not a semantic conflict | Distinct attempt evidence | `NEW_CANDIDATE — NOT REGISTERED` |
| Digest matches but producer/Tenant authority is invalid | Reject | Authority-validation failure | `NEW_CANDIDATE — NOT REGISTERED` |
| Quarantined evidence is re-driven without release authority | Reject; no confirmation | Quarantine and authorization evidence | `NT-016/017/018` relationship; **NOT_EXECUTED** |
| Central evidence conflicts with Sovereign-local evidence after reconnection | No automatic overwrite | Local authority and unresolved reconciliation evidence | `NT-019/020` relationship; **NOT_EXECUTED** |

Existing acceptance-candidate traceability remains:

- S4: `TC-AC-003/004/014/017`; `OPS-AC-004–006/013`.
- S5: `TC-AC-003–005/017`; `OPS-AC-004/005/012`.
- S6: `TC-AC-018`; `OPS-AC-012/013`.
- S7: `TC-AC-011/014/016`; `OPS-AC-001–003/010/011/013/016`.
- S8: `TC-AC-013/014`; `OPS-AC-014/015`.

No PASS, FAIL or risk-acceptance result is recorded.

## H. SI-01 through SI-05 Proposed Decision Records

### H.1 SI-01 — Semantic Identity

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

#### Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- The complete `ObligationKey` as obligation identity.
- Version-bound immutable semantic content as the basis of semantic equality.
- `MutationId` as traceability evidence rather than Audit ingestion identity.
- Separation of identity, immutable semantics, conditional semantics, transport attempts, Customer-owned recovery evidence and prohibited sensitive data into the six field classes defined in section B.
- Mandatory minimization of cross-domain evidence.

The final schema and field representations, exact semantic participation of `OccurredAt` and `CorrelationRef`, conditional-field inclusion, `SemanticContentVersion` representation, Security Architecture review and Contract Governance review remain pending.

#### Approved bounded decision clause

The complete `ObligationKey` defines obligation identity. Immutable, version-bound semantic content defines equality. `MutationId` remains Customer mutation traceability evidence and is not Audit ingestion idempotency identity or authorization proof. Identity fields, immutable semantics, conditional evidence, transport metadata, Customer-owned recovery evidence and prohibited sensitive content remain the six distinct classes defined in section B.

Customer shall preserve enough immutable producer-owned evidence to reproduce the obligation after recovery without reconstructing historical meaning from mutable Customer state. Audit shall receive only the minimum approved cross-domain evidence.

#### Preferred logical direction

Adopt the six-class matrix as the conceptual field-governance baseline, without approving a final Event schema.

#### Pending approval and design

- Exact field names and representations.
- `SafeCustomerRef`, `ActorRef` and `ChangeCategoryRef` vocabularies.
- Semantic field inclusion by operation/version.
- Timestamp and correlation comparison significance.
- Customer/Audit field-level agreement, classification and retention.

### H.2 SI-02 — Canonicalization

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

#### Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- The requirement for a deterministic, typed and version-bound semantic comparison contract.
- Definition of comparison semantics independently from incidental transport serialization.
- Explicit rules for absent/null/default values, field ordering, Unicode, numeric values, timestamps, enums and unknown fields.
- The rule that raw wire-byte differences alone do not establish semantic conflict.
- The rule that digest-only comparison is not authoritative proof of provenance, Tenant authorization or semantic integrity.

Final canonical encoding, exact normalization, hash/signature/integrity mechanisms, implementation library, Security Architecture approval and Contract Governance approval remain pending.

#### Approved bounded decision clause

Semantic comparison shall use a deterministic, typed and version-bound semantic projection. The projection and its comparison rules shall be bound to both `ContractVersion` and `SemanticContentVersion`. Field inclusion, ordering, absent/null/default behavior, Unicode, numbers, timestamps, enums and unknown fields shall be explicitly defined.

Raw wire bytes are not the general equality criterion. A digest alone is not authoritative proof of semantic correctness, producer provenance, Tenant authorization or Audit ingestion. Integrity and provenance verification remain independent of canonical equality.

#### Preferred logical direction

Use a typed semantic projection followed by a deterministic encoding contract, without selecting that encoding in this decision.

#### Pending approval and design

- Canonical encoding and full normalization specification.
- Digest/signature or other integrity mechanism.
- Cryptographic algorithm and key custody.
- Implementation library and producer/consumer conformance evidence.

### H.3 SI-03 — Contract Version Compatibility

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

#### Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- Preservation of the original `ContractType`, `ContractVersion` and `SemanticContentVersion` for existing committed obligations.
- The prohibition on silently reinterpreting earlier committed semantic evidence after a newer deployment.
- Explicit version governance for breaking semantic changes.
- The rule that unsupported contract versions cannot produce successful ingestion.
- Rejection of unauthorized downgrade attempts.
- Preservation of original evidence and provenance by any separately approved transformation.

The final supported-version matrix, compatibility and coexistence windows, deprecation and migration policy, contract-testing mechanism, Contract Governance approval and Security Architecture approval remain pending.

#### Approved bounded decision clause

Every committed obligation preserves its original `ContractType`, `ContractVersion` and `SemanticContentVersion`. Software upgrades shall not silently reinterpret committed obligations. Additive compatibility requires explicit approved semantic rules. Breaking or reinterpreting changes require a new version and explicit migration/coexistence governance. Unsupported versions shall never produce successful ingestion. Downgrade shall not remove mandatory semantics or bypass provenance, Tenant or contract validation.

#### Preferred logical direction

Retain support for the original interpretation of pending obligations throughout an explicitly approved coexistence window.

#### Pending approval and design

- Version-numbering and compatibility matrix.
- Support/coexistence window and deprecation policy.
- Consumer inventory and migration/transformation procedures.
- Compatibility tooling and `OD-020` contract-test selection.

### H.4 SI-04 — Conflict Disposition

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

#### Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve the distinct conceptual dispositions of idempotent duplicate, semantic conflict, authentication/authorization rejection, unsupported contract, invalid/quarantined evidence, unresolved reconciliation and confirmation-security failure.

They also approve these boundaries:

- Same complete key and same semantic content is idempotent.
- Same complete key and different semantic content is a conflict and receives no successful confirmation.
- Invalid Producer or Tenant provenance fails closed.
- Quarantine never constitutes successful ingestion.
- No automatic conflict winner or authoritative evidence overwrite is permitted.

The final disposition state machine, quarantine access/release lifecycle, correction and retention policy, Security review and Security Architecture approval remain pending.

#### Approved bounded decision clause

Idempotent duplicate, semantic conflict, authentication/authorization rejection, unsupported contract, invalid/quarantined evidence, unresolved reconciliation and confirmation-security failure are distinct outcomes.

- Same complete key plus same canonical content is idempotent.
- Same complete key plus different canonical content shall not receive successful ingestion confirmation.
- Producer or Tenant mismatch fails closed and is not ordinary duplicate processing.
- No Domain or operator may automatically select a conflict winner or overwrite another Domain's authoritative evidence.
- Quarantine is not successful Audit ingestion.

#### Preferred logical direction

Use durable typed dispositions and disable automatic resolution for conflict, authority mismatch and indeterminate evidence.

#### Pending approval and design

- Final disposition state machine and persistence representation.
- Quarantine ownership, access, retention and release/correction authority.
- Escalation, reconciliation and superseding-disposition lifecycle.
- Security incident classification and response integration.

### H.5 SI-05 — Recovery Integrity

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

#### Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- Preservation of the original `ObligationKey`, versions and semantic content through retry, re-drive and recovery.
- Use of Domain-owned durable evidence as the authoritative recovery basis.
- Addition of transport metadata by new attempts without rewriting semantic truth.
- The requirement that concurrent recovery not create a second authoritative Audit effect.
- The prohibition on silently treating unsupported or conflicting evidence as success.
- Dedicated Sovereign local final authority for recovery and reconciliation.

Scheduler and claiming/concurrency implementation, retry limits and backoff, contract coexistence periods, final recovery/escalation runbooks, numeric operational thresholds, Security approval and final Operations policy approval remain pending.

#### Approved bounded decision clause

Retry, re-drive, crash recovery, duplicate consumer processing, upgrade recovery and Sovereign reconciliation shall preserve the original `ObligationKey`, original versions and immutable semantic content. Recovery relies on Domain-owned durable evidence. New transport attempts may add only transport metadata. Crash, concurrency and re-drive shall not create a second Customer mutation, producer obligation or authoritative Audit effect.

Long-lived pending obligations remain governed by their original semantic rules. Unsupported versions and conflicting evidence shall not be silently converted into success. Dedicated Sovereign recovery and reconciliation retain local final authority.

#### Preferred logical direction

Recover from Domain-owned durable evidence and route every retry or re-drive through the normal authorization, Tenant, provenance, compatibility, idempotency and conflict checks.

#### Pending approval and design

- Claiming/leasing, scheduling and concurrency mechanism.
- Retry, backoff, DLQ and terminal-failure rules.
- Coexistence windows and old-version operational support.
- Profile-specific recovery, reconnection and escalation runbooks.
- Numeric backlog, freshness and recovery objectives.

## I. Owner and Security Approval Dependencies

### I.1 Approval register

| Dimension | Recorded status |
| --- | --- |
| `PROJECT_AND_DOMAIN_BOUNDED_DISPOSITIONS` | **APPROVED_WITH_BOUNDARIES** |
| `MESSAGING_API_EVENT_ARCHITECTURE_APPROVAL` | **PENDING** |
| `CONTRACT_GOVERNANCE_APPROVAL` | **PENDING** |
| `SECURITY_ARCHITECTURE_APPROVAL` | **PENDING** |
| `INDEPENDENT_SECURITY_REVIEW` | **NOT_SIGNED_OFF** |
| Full SEC-02 Security Contract | **NOT APPROVED** |

| Proposed decision | Recorded Project/Domain disposition | Outstanding specialist authority | Safely deferred implementation choices |
| --- | --- | --- | --- |
| SI-01 | **APPROVED WITH BOUNDARIES** | Messaging/API Event Architecture, Contract Governance and Security Architecture review of field participation and contract governance | Storage schema, serializer, identifier technology |
| SI-02 | **APPROVED WITH BOUNDARIES** | Messaging/API Event Architecture, Contract Governance and Security Architecture approval of canonical rules | Encoding, digest, signature, library and key infrastructure |
| SI-03 | **APPROVED WITH BOUNDARIES** | Contract Governance, Messaging/API Event Architecture and Security Architecture approval of compatibility governance | Support duration, migration tooling and contract-test technology |
| SI-04 | **APPROVED WITH BOUNDARIES** | Security Architecture and applicable Contract Governance review of dispositions and quarantine boundaries | State-machine implementation, quarantine store and final runbooks |
| SI-05 | **APPROVED WITH BOUNDARIES** | Security Architecture, specialist Messaging/API Event Architecture and final Operations policy approval | Scheduler, leasing, retry parameters, topology and operational tooling |

### I.2 Independent Security Reviewer dependencies

The reviewer must assess:

- whether the semantic projection is unambiguous and excludes prohibited content;
- whether canonicalization differences can create collision, downgrade or bypass conditions;
- whether a matching integrity value can be misused as producer or Tenant authority;
- whether version transitions preserve mandatory semantics and fail safely;
- whether conflict/quarantine dispositions prevent false successful ingestion;
- whether retry, re-drive and recovery preserve provenance and authority; and
- whether Sovereign reconnection can overwrite locally authoritative evidence.

No reviewer identity, finding, conclusion or sign-off is recorded.

### I.3 Open Decision dependencies

- `OD-008`: final API/event versioning and envelope evolution rules.
- `OD-011`: workload identity used for producer and recovery interactions.
- `OD-012`: secrets, keys and any future integrity/authenticity mechanism.
- `OD-014`: Tenant/RLS integration for persisted Tenant-bound evidence.
- `OD-019`: scheduling mechanism for publication and recovery.
- `OD-020`: compatibility and contract-testing approach.
- `OD-023`: numeric availability, recovery, backlog and capacity objectives.

These dependencies do not weaken approved invariants and are not closed by SEC-02.

## J. Explicit Non-Approvals

This document does not approve:

- A fully approved SEC-02 Security Contract or any scope beyond the five recorded bounded Project/Domain dispositions.
- Messaging/API Event Architecture approval.
- Contract Governance approval.
- Security Architecture approval or Independent Security Review sign-off.
- A final Event schema, API, envelope or field representation.
- A final canonical semantic field set or comparison specification.
- JSON, binary or any other canonical encoding.
- A hash, digest, MAC, signature, cryptographic algorithm or key hierarchy.
- A version numbering scheme, support/coexistence window, deprecation or migration policy.
- A final compatibility matrix or contract-testing technology.
- A conflict, quarantine, correction, release or escalation state machine.
- Retry, scheduling, claiming, retention or numeric NFRs.
- Risk acceptance or Security exception.
- `SR-CAND-001` through `SR-CAND-024` as approved Security Requirements.
- Executed tests, verified runtime controls, implementation readiness or Production Readiness.
- Executable or unconditional DURABLE_DEFER.

## K. Governance Status and Next Bounded Action

- `PROJECT_AND_DOMAIN_BOUNDED_DISPOSITIONS = APPROVED_WITH_BOUNDARIES`
- `MESSAGING_API_EVENT_ARCHITECTURE_APPROVAL = PENDING`
- `CONTRACT_GOVERNANCE_APPROVAL = PENDING`
- `SECURITY_ARCHITECTURE_APPROVAL = PENDING`
- `INDEPENDENT_SECURITY_REVIEW = NOT_SIGNED_OFF`
- `V3-003 = IN PROGRESS`
- `OD-001..OD-023 = OPEN`
- `SR-CAND-001..SR-CAND-024 = PROPOSED — NOT APPROVED`
- `SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF`
- `IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED`
- `NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED`
- `EXECUTABLE_DURABLE_DEFER = NOT APPROVED`

The next bounded activity is an explicit, separately authorized review and disposition by Messaging/API Event Architecture, Contract Governance and Security Architecture. Each authority must record only its own scope, evidence requests and unresolved dependencies. After the required specialist dispositions and missing design evidence are available, the package may be submitted to an authenticated Independent Security Reviewer.

The bounded Project/Domain approvals shall not be interpreted as selection of a protocol, schema, canonical encoding, cryptographic algorithm, implementation library, migration policy, operational control, runtime verification, Security sign-off or executable DURABLE_DEFER authorization.
