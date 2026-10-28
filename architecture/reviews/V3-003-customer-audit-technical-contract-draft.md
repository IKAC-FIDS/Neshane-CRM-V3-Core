# V3-003 Customer/Audit Technical Contract Draft

## A. Document Control

| Field | Value |
| --- | --- |
| Status | **DRAFT — NOT APPROVED** |
| Task | V3-003 — NFR and Threat Assumptions |
| Scope | CUS-CREATE / CUS-UPDATE |
| Applicable Owner-approved decisions | V3-003-DEC-009 through V3-003-DEC-014 |
| Architecture baseline | NESHANE-V3-ARCH-P00-002 |
| Customer Domain Owner approval | **PENDING** |
| Audit Domain Owner approval | **PENDING** |
| Messaging/Operations Owner approval | **PENDING** |
| Security Review | **NOT_SIGNED_OFF** |
| Executable DURABLE_DEFER | **NOT APPROVED** |
| Implementation Evidence | **NOT_VERIFIED** |
| Negative Test Execution | **NOT_EXECUTED** |

This document materializes a proposed technical contract for review. Owner-approved architectural invariants are stated normatively only where V3-003-DEC-009 through V3-003-DEC-014 or the approved architecture already require them. Every new field, state, response rule, confirmation form and reconciliation behavior in this document is **PROPOSED — PENDING APPROVAL** unless explicitly identified as an approved invariant.

The document does not allocate a new V3-003 decision identifier, approve an executable operation-specific DURABLE_DEFER policy, or authorize implementation.

### Authoritative basis

- Architecture baseline NESHANE-V3-ARCH-P00-002.
- ADR-V3-002, ADR-V3-003, ADR-V3-004, ADR-V3-005, ADR-V3-007 and ADR-V3-008.
- V3-003-DEC-009 through V3-003-DEC-014.
- Security, Messaging, Persistence, Service Architecture and API Design standards.
- Open Decisions OD-001 through OD-023, all of which remain Open.

## B. Ownership and Consistency Boundaries

| Responsibility | Approved invariant | Proposed technical responsibility | Prohibited interpretation |
| --- | --- | --- | --- |
| Customer Domain | Owns Customer Master, CUS-CREATE/CUS-UPDATE business facts, final Customer authorization, Customer persistence and the originating consistency boundary. A successful covered mutation requires a consistently and durably recorded mandatory Audit publication obligation. | Generate the ObligationId once; bind it to the accepted mutation; atomically record the authoritative mutation and obligation where they share the Customer-owned transactional resource; expose authorized producer evidence for delivery and reconciliation. | Customer cannot claim authoritative Audit ingestion, write Audit private persistence, or treat broker publication as ingestion confirmation. |
| Audit Domain | Owns authoritative platform-wide Audit records, authorized Audit projections, Audit resource authorization and Audit-owned durable ingestion evidence. | Validate producer, contract, tenant provenance and semantic identity; perform idempotent ingestion; durably record the Audit evidence and processing result; issue or expose authoritative ingestion confirmation. | Audit cannot access Customer private persistence, authorize Customer mutations, or change Customer Business Facts. |
| Publication component | Reliable publication of Customer-owned durable obligations is part of the producing boundary. At-least-once delivery, duplicates and possible reordering are assumed. | Discover eligible pending obligations, create transport attempts, publish without changing semantic content, retain attempt evidence, and support authorized re-drive. | It is not the authority for Customer mutation success or Audit ingestion confirmation. A publication acknowledgement is not an Audit confirmation. |
| Messaging transport | RabbitMQ is the approved asynchronous baseline; transport is not a business authority. | Carry a versioned contract and return transport-level dispositions or acknowledgements. | Transport acceptance, routing or delivery cannot prove Consumer authorization, valid provenance, durable Audit storage or reconciliation completion. |
| Reconciliation authority | Service-owned persistence and no cross-service database access remain mandatory. Dedicated Sovereign retains local final authority. | Customer owns producer-side obligation truth; Audit owns ingestion truth; an explicitly authorized reconciliation workflow compares contract evidence and records resolution without directly reading either private database. Operations coordinates execution; the applicable Domain resolves its owned facts. | No shared reconciliation database may become an implicit source of truth. Operations cannot fabricate Customer or Audit evidence. |
| Operations and Security | Operational access is scoped and audited; Security controls remain effective during retry, re-drive and recovery. | Operations owns monitoring, authorized recovery execution and escalation. Security reviews provenance, integrity, tenant isolation, authorization and failure-path controls. | Operator status does not confer Domain authorization, cross-tenant access, risk acceptance or Security sign-off. |

The Customer transaction boundary ends at Customer-owned persistence. The Audit ingestion boundary is a separate Audit-owned durable boundary. No distributed transaction across the two Domains is required or approved.

## C. Obligation Identity Contract

### C.1 Recommended semantic key

**PROPOSED — PENDING CUSTOMER, AUDIT AND SECURITY APPROVAL**

The semantic reconciliation key is:

**ProducerAuthority + TenantScope + ObligationId**

The tuple, rather than ObligationId alone, is the uniqueness and lookup scope. It binds an obligation to the authoritative producer and validated tenant scope and prevents an identifier collision from becoming cross-producer or cross-tenant evidence.

| Identity | Meaning | Owner | Stability and use | Approval status |
| --- | --- | --- | --- | --- |
| Command identity | One client-visible submission/retry intent for CUS-CREATE or CUS-UPDATE. | Customer Domain contract | Stable for retries of the same submitted command; reuse for a different intent is invalid. Exact client contract is unresolved. | **PROPOSED; Customer approval required** |
| Business mutation identity | One accepted authoritative Customer state transition. | Customer Domain | Stable for the committed transition; independent concurrent updates require distinct identities. | **PROPOSED; Customer approval required** |
| Audit obligation identity | One mandatory Audit publication obligation arising from one covered successful mutation. | Customer Domain | Generated once before durable recording; stable across publication retries, re-drive, process recovery and reconciliation. | **PROPOSED; Customer and Audit approval required** |
| Transport attempt identity | One delivery attempt of an existing obligation. | Publication component / transport adapter | May change for every attempt and must not alter obligation meaning. | **PROPOSED; Messaging/Operations approval required** |
| Audit record identity | One authoritative Audit-owned record or accepted representation. | Audit Domain | Assigned and governed by Audit; returned only through Audit-owned evidence. | **PROPOSED; Audit approval required** |

### C.2 Candidate identity invariants

1. Customer generates ObligationId and records it with the obligation before the obligation is eligible for publication.
2. The complete semantic key remains stable across retries, redrive and confirmation recovery.
3. Audit validates the producer authority and authoritative TenantScope before using the key for idempotency or lookup.
4. A same-key/same-semantic-content redelivery is a duplicate candidate and must not create a second authoritative effect.
5. A same-key/different-semantic-content delivery is a content conflict. It must not be reported as successful ingestion; it requires durable disposition, escalation and reconciliation.
6. Identifier representation and generation technology remain unresolved. Uniqueness evidence and collision handling require Customer and Audit approval.
7. Canonical semantic comparison and any integrity or authenticity mechanism require Independent Security Review.

## D. Command, Mutation and Audit Idempotency

The following are three separate boundaries. None establishes end-to-end exactly-once execution.

| Boundary | Protected effect | Identity | Owner | Retry behavior | Unresolved decision |
| --- | --- | --- | --- | --- | --- |
| Customer Command Idempotency | Prevents one retried submission from being interpreted as multiple independent commands. | Command identity | Customer Domain | A retry with the same identity must resolve against the original command outcome before creating another mutation. | Retention, duplicate response, conflict response and ambiguous-outcome behavior. |
| Customer Business Mutation Consistency | Prevents duplicate authoritative state transitions and coordinates the covered mutation with its durable obligation. | Business mutation identity plus Customer aggregate/version rules | Customer Domain | The same accepted transition must not create multiple Customer effects or multiple semantic obligations. | Create uniqueness, optimistic/concurrent update rules, no-op definition and correction behavior. |
| Audit Obligation Ingestion Idempotency | Prevents duplicate delivery from creating duplicate authoritative Audit effects. | ProducerAuthority + TenantScope + ObligationId | Audit Domain | Same-key/same-content redelivery returns or reconstructs the same successful ingestion evidence after durable handling. | Exact Inbox/equivalent design, semantic comparison, retention and conflict disposition. |

### D.1 Scenario rules

| Scenario | Proposed contract treatment | Approval boundary |
| --- | --- | --- |
| Duplicate CUS-CREATE command | Resolve by Command identity before creating another Customer Master. If the original result is known, return the approved representation of that result; if identity is reused with different intent, reject as a conflict. | Final duplicate response, Customer uniqueness semantics and retention are **unresolved Customer decisions**. |
| Duplicate CUS-UPDATE command | A retry of the same command must not apply the same intended transition twice. | Final version/conflict semantics are **unresolved Customer decisions**. |
| Independent concurrent CUS-UPDATE operations | Treat independently submitted updates as distinct commands and candidate mutations, then apply Customer-owned concurrency and authorization rules. | Merge, rejection and ordering policy are **unresolved Customer decisions**. |
| No-op CUS-UPDATE | DEC-012 mandates an obligation for a successful durable authoritative change. A proposed no-op produces no successful-mutation obligation. | The definition of no-op and whether a separate attempt/decision event is required remain **unresolved**. |
| Failed mutation | No successful-mutation obligation is created. Failure or denial Audit coverage is not generalized by DEC-012. | Any separate failure/denial catalog entry requires later approval. |
| Audit redelivery | Use Audit obligation identity, not Command identity, to deduplicate. Same-key/same-content must not create a duplicate authoritative Audit effect. | Audit durable processing design is **pending Audit approval**. |
| ACK loss after durable Audit commit | Audit remains authoritative. Producer or publisher retrieves or receives confirmation using the stable ObligationKey; redelivery must resolve idempotently. | Confirmation retrieval and transport mechanism remain **proposed**. |

## E. Producer Contract

This is a conceptual contract, not a schema or an approved Event Contract. Field names are stable draft labels only.

| Candidate field | Purpose | Semantic owner | Validation responsibility | Status | Privacy and security constraints |
| --- | --- | --- | --- | --- | --- |
| ProducerAuthority | Identifies the Customer producing authority. | Customer | Audit validates authenticated workload provenance and expected producer. | **PROPOSED field; approved concern** | Must not be inferred from an untrusted header. |
| TenantScope | Binds the obligation to validated authoritative Tenant Context. | Customer | Customer establishes; Audit independently validates trusted provenance and consistency. | **PROPOSED field; approved concern** | No cross-tenant fallback; conflicting or missing scope fails closed. |
| ObligationId | Stable producer-issued identity for the mandatory obligation. | Customer | Customer enforces generation/recording rules; Audit validates format and tuple uniqueness. | **PROPOSED** | Identifier technology is not selected. |
| ContractType | Identifies the semantic Audit obligation contract. | Customer contract owner | Audit verifies supported type. | **PROPOSED field; versioned contracts approved** | Must not be interpreted as authorization. |
| ContractVersion | Governs compatibility and semantic interpretation. | Customer contract owner | Audit accepts only supported, compatible versions. | **PROPOSED field; versioning approved** | Unsupported version must not be treated as successful ingestion. |
| OperationType | Distinguishes CUS-CREATE from CUS-UPDATE. | Customer | Audit validates against contract. | **PROPOSED** | Limited to approved operation vocabulary. |
| MutationId | Correlates the obligation with one accepted Customer mutation. | Customer | Customer validates relationship; Audit treats it as producer evidence, not direct Customer database proof. | **PROPOSED** | Must not expose private persistence keys unnecessarily. |
| SafeCustomerRef | Provides the minimum safe reference needed for accountability. | Customer | Customer applies reference policy; Audit validates presence/shape. | **PROPOSED field; safe reference objective approved** | No full Customer record or sensitive identifier unless separately approved. |
| ActorRef | Provides a safe reference to the validated initiating actor or accountable workload. | Customer / Identity provenance | Customer establishes; Audit validates provenance required by the contract. | **PROPOSED field; actor evidence concept approved** | No credentials, tokens or unnecessary identity attributes. |
| Outcome | States the covered successful mutation outcome. | Customer | Audit validates allowed value. | **PROPOSED field; successful outcome coverage approved** | Must not generalize unapproved failure/denial events. |
| ChangeCategoryRef | Classifies an update without carrying old/new values. Applicable to CUS-UPDATE. | Customer | Customer defines; Audit validates against an approved vocabulary. | **PROPOSED; Customer approval required** | Exact categories and sensitive-field treatment remain unresolved. |
| OccurredAt | Producer-observed time of the authoritative mutation. | Customer | Customer supplies; Audit validates plausible contract form without treating time as identity. | **PROPOSED** | Clock policy and skew handling are unresolved. |
| CorrelationRef | Links the operation to authorized diagnostic and accountability context. | Customer | Customer establishes; Audit preserves safely. | **PROPOSED field; correlation evidence concept approved** | Must be sanitized and must not carry sensitive request content. |
| CausationRef | Links the obligation to the initiating command or prior authorized cause where applicable. | Customer | Customer validates relationship. | **PROPOSED** | Must not expose a raw token or client secret. |
| SemanticContentVersion | Identifies the semantic comparison form used for same-key conflict detection. | Contract owners | Customer creates; Audit validates supported form. | **PROPOSED; Security Review required** | Canonicalization and integrity mechanisms are unresolved. |
| ProducerEvidenceRef | Enables authorized producer-side discovery and reconciliation of the durable obligation. | Customer | Customer authorizes access; reconciler validates scope. | **PROPOSED** | Must not be a private database locator or allow database access. |

The Customer-owned durable obligation record must preserve enough immutable semantic content to reproduce the contract after a crash without reconstructing sensitive values from mutable Customer state. The exact storage schema is not approved.

## F. Audit Consumer and Confirmation Contract

### F.1 Proposed Audit-owned durable processing boundary

1. Authenticate and authorize the producing workload at the Audit trust boundary.
2. Validate ProducerAuthority, TenantScope provenance, contract type/version and required minimized content.
3. Resolve the ObligationKey in Audit-owned durable idempotency evidence.
4. For a new valid obligation, durably coordinate the authoritative Audit record and Audit-owned processing evidence within an Audit-owned consistency boundary.
5. Only after durable handling, return the applicable transport disposition.
6. Make Audit-owned ingestion confirmation available for a successfully committed authoritative Audit record.
7. For invalid, unsupported or conflicting delivery, record an authorized durable invalid/quarantine disposition where policy permits, but never present that disposition as successful Audit ingestion.

The exact Inbox/equivalent schema, transaction mechanism, quarantine store and acknowledgement protocol remain **PROPOSED — PENDING AUDIT, OPERATIONS AND SECURITY APPROVAL**.

### F.2 Proposed authoritative confirmation

| Candidate confirmation evidence | Purpose | Authority | Status and constraint |
| --- | --- | --- | --- |
| ConfirmationContractVersion | Supports compatible confirmation interpretation. | Audit | **PROPOSED**; versioning mechanism unresolved. |
| ProducerAuthority + TenantScope + ObligationId | Binds confirmation to the original semantic obligation. | Customer values confirmed by Audit | **PROPOSED**; all components must match. |
| AuditAuthority | Identifies the authoritative Audit issuer. | Audit | **PROPOSED**; trust mechanism requires Security Review. |
| AuditRecordRef | References the authoritative Audit-owned record. | Audit | **PROPOSED**; safe reference only, never a private database locator. |
| IngestionOutcome | Distinguishes successful authoritative ingestion from invalid/quarantine/rejection outcomes. | Audit | **PROPOSED**; only the approved success value may support AUDIT_INGESTION_CONFIRMED. |
| DurableCommitEvidenceRef | Provides Audit-owned evidence that the authoritative record and required processing evidence crossed the durable boundary. | Audit | **PROPOSED**; representation and authenticity unresolved. |
| ConfirmedAt | Records the Audit-observed confirmation time. | Audit | **PROPOSED**; time semantics are not an identity or freshness policy. |

**AUDIT_INGESTION_CONFIRMED** may be asserted only when valid Audit-owned evidence binds the full ObligationKey to a successfully committed authoritative Audit record under a supported confirmation contract.

The following are explicitly different:

| Signal | Meaning | May establish AUDIT_INGESTION_CONFIRMED? |
| --- | --- | --- |
| Broker publication acknowledgement | Transport accepted a publication according to transport semantics. | **No** |
| Transport delivery disposition | A delivery was ACKed, retried, rejected or dead-lettered. | **No** |
| Durable invalid-event/quarantine disposition | Audit durably classified an invalid, unsupported or conflicting delivery. | **No** |
| Authoritative Audit ingestion confirmation | Audit attests to a valid durable authoritative record bound to the obligation. | **Yes, subject to approved authenticity and validation rules** |
| Producer reconciliation completion | Producer records that valid Audit evidence was matched and its pending state resolved. | **No; it consumes confirmation rather than creating it** |

Duplicate confirmations must be idempotently accepted only when their binding and semantic content agree. Confirmation loss must be recoverable through an authorized Audit evidence lookup or equivalent exchange; the exact interface is not approved.

## G. Immutable Semantic Content vs Transport Metadata

| Immutable obligation meaning | Retry/transport-attempt metadata |
| --- | --- |
| ProducerAuthority | TransportAttemptId |
| TenantScope | Broker delivery identifier |
| ObligationId | Attempt number |
| ContractType and semantic ContractVersion | Publication timestamp |
| OperationType and MutationId | Route/exchange/queue observation |
| SafeCustomerRef | Delivery/ACK/NACK observation |
| ActorRef, Outcome and applicable ChangeCategoryRef | Retry/backoff/dead-letter metadata |
| OccurredAt, CorrelationRef and applicable CausationRef | Transport diagnostic trace references |
| SemanticContentVersion | Publisher instance or dispatcher observation |

Transport retries may add or vary attempt metadata but must not mutate the obligation meaning.

- **Same key + same semantic content:** proposed duplicate path; Audit returns/reconstructs the same authoritative outcome without a second authoritative effect.
- **Same key + different semantic content:** proposed content-conflict path; no successful ingestion confirmation, durable conflict visibility, suspension of reconciliation for that obligation and authorized escalation.
- **Different transport metadata only:** not a semantic conflict.

The canonicalization rules used to decide semantic equality, content-integrity protection, signing or hashing, key custody and cryptographic algorithms are not selected. They require contract-owner agreement and Independent Security Review.

## H. Reconciliation Contract

### H.1 Proposed reconciliation states

| State | Required evidence | Proposed owner action | Resolution boundary |
| --- | --- | --- | --- |
| MATCH_CONFIRMED | Customer durable obligation plus valid Audit ingestion confirmation with matching key/content. | Customer records producer-side reconciliation completion. | Customer may close its pending reconciliation state; Audit record remains Audit-owned. |
| PRODUCER_ONLY_PENDING | Valid Customer obligation; no valid Audit confirmation found. | Publication/Operations continues authorized delivery/recovery while eligibility remains valid. | Does not prove loss or ingestion. |
| AUDIT_CONFIRMED_PRODUCER_UNAWARE | Valid Audit confirmation exists; Customer has not recorded it. | Retrieve and validate confirmation, then update Customer-owned reconciliation evidence. | No duplicate Audit record. |
| INVALID_DISPOSITION | Audit has a durable rejection/quarantine disposition. | Escalate to the responsible Domain/Operations owner; do not mark ingestion confirmed. | Resolution policy pending. |
| CONTENT_CONFLICT | Same ObligationKey maps to different semantic content. | Suspend automatic resolution, preserve both evidence views and escalate to Domain and Security owners. | Must not choose a winner automatically. |
| TENANT_OR_PRODUCER_MISMATCH | Evidence does not match authoritative tenant or producer binding. | Fail closed, isolate the case and initiate security escalation. | Never reconcile across tenant/producer scope. |
| PARTIAL_RECOVERY | Some durable evidence is available but completeness or authenticity is indeterminate. | Suspend deferred-path eligibility where DEC-014 evidence gates are not satisfied; perform authorized recovery. | No assumption of success. |
| UNKNOWN_OR_UNRECOVERABLE | Required obligation, ingestion or recovery evidence cannot be established. | Escalate under an approved operation-specific policy; do not fabricate confirmation or rollback. | Policy and risk disposition pending. |

### H.2 Reconciliation flow

1. Customer discovers pending and unresolved obligations from Customer-owned durable evidence.
2. An authenticated, authorized reconciliation interaction asks Audit for evidence by the full ObligationKey and validated scope.
3. Audit authorizes the lookup and returns only Audit-owned confirmation or disposition evidence.
4. The reconciler validates contract version, authority, TenantScope, producer binding, semantic binding and evidence authenticity.
5. Customer records its reconciliation result without modifying Audit evidence; Audit does not modify Customer Business Facts.
6. Mismatch, invalid evidence or unknown recovery state becomes visible to Operations and the responsible Domain owner and, where security-relevant, Security.
7. Re-drive repeats the normal validation and idempotency path. It cannot bypass authorization, tenant validation or compatibility checks.

Direct cross-service database access, cross-service SQL and shared persistence are forbidden.

### H.3 Deployment profile obligations

| Profile | Contract requirement |
| --- | --- |
| Shared SaaS | Every discovery, lookup, publication, confirmation and reconciliation action preserves validated Tenant Context, application authorization and non-bypass tenant isolation. No cross-tenant batching may weaken evidence binding. |
| Dedicated Managed | Physical dedication does not remove service ownership, workload authentication, Domain authorization, tenant binding, idempotency or confirmation requirements. |
| Dedicated Sovereign | Customer obligation custody, Audit ingestion, confirmation, backlog visibility, reconciliation, recovery authorization and escalation remain locally authoritative. Central availability or acknowledgement is not required for legitimate local evidence. Full Air-Gap and disconnected-duration targets remain unapproved. |

## I. Customer Commit and Response Semantics

No row below approves an executable Customer response policy.

| Condition | Approved boundary | Proposed contract treatment | Remaining approval |
| --- | --- | --- | --- |
| Failed Customer commit | A successful authoritative mutation cannot be reported when mutation and mandatory obligation were not durably established. | Return a non-success outcome under the future Customer API contract; no successful-mutation Audit obligation is claimed. | Customer error/response contract. |
| Unknown commit outcome | Success cannot be guessed and duplicate mutation must be prevented. | Preserve the Command identity; resolve authoritative command/mutation/obligation evidence before accepting a retry as new work. | Customer ambiguous-outcome and lookup policy. |
| Committed mutation with pending Audit ingestion | Durable Customer mutation plus obligation satisfies only the foundational durability prerequisite, not executable deferred authorization. | Mark producer evidence pending. A success response is permitted only if an approved operation-specific policy is active and every DEC-014 eligibility gate is currently satisfied. | Project/Domain policy approval, Operations evidence and Security Review. |
| Confirmed Audit ingestion | Only valid Audit-owned evidence can establish confirmation. | Validate and record reconciliation completion; duplicate confirmation has no additional business effect. | Customer/Audit confirmation contract approval. |
| Deferred eligibility suspended after commit | DEC-014 does not authorize rollback or automatic shutdown of all Customer operations. | Preserve the already committed Customer mutation and obligation; suspend use of the deferred pathway; escalate and reconcile. Do not claim post-commit rollback. | Operation-specific recovery, response and incident policy. |
| Retried command after ambiguous client response | Retries must not create prohibited duplicate effects. | Reuse the original Command identity, resolve the prior outcome, and return the approved representation or an indeterminate/conflict outcome. | Customer command idempotency and retention policy. |

Candidate successful deferred sequence:

1. Customer validates identity and authoritative Tenant Context.
2. Customer performs final resource/action authorization.
3. Customer accepts the command and determines one candidate business mutation.
4. Within the Customer-owned consistency boundary, Customer durably commits the authoritative mutation and its mandatory Audit obligation.
5. Customer evaluates the currently approved operation-specific response policy and all DEC-014 gates.
6. Only if such executable policy exists and its gates are satisfied may that policy permit a success response before Audit ingestion. **No such executable policy is approved by this draft.**
7. Publication delivers the immutable obligation asynchronously.
8. Audit validates and durably handles it idempotently.
9. Audit makes authoritative ingestion confirmation available.
10. Customer/Operations reconciles the pending obligation against valid Audit evidence.

## J. Failure and Recovery Matrix

| Scenario | Approved invariant | Proposed contract behavior | Required evidence | Responsible owner | Deferred eligibility | Remaining policy blocker |
| --- | --- | --- | --- | --- | --- | --- |
| Customer transaction fails | No successful mutation without durable obligation. | Report no successful authoritative mutation; retain only policy-approved diagnostic evidence. | Transaction outcome. | Customer | Not applicable. | Customer response/error semantics. |
| Obligation persistence fails | Mutation and obligation must share the approved consistency boundary where applicable. | Abort the shared commit; do not report success. | Atomic boundary evidence. | Customer | Ineligible. | Concrete Customer transaction design. |
| Crash after commit, before publication | Durable obligation must be recoverable and visible. | Rediscover and publish the same semantic obligation with a new attempt identity. | Durable obligation and recovery scan evidence. | Customer publication / Operations | Eligible only under an approved policy and trustworthy gates. | Recovery ownership, scheduling and thresholds. |
| Broker outage | Broker status does not alter obligation truth. | Keep obligation pending; monitor, retry and escalate under approved policy. | Pending backlog and transport failure evidence. | Messaging/Operations | Conditional; suspend when visibility/recoverability becomes indeterminate. | Retry, escalation and capacity policy. |
| Duplicate delivery | At-least-once and idempotent handling apply. | Same-key/same-content returns the existing durable result. | Audit idempotency evidence. | Audit | Maintained if evidence remains valid. | Inbox/equivalent design and retention. |
| Conflicting duplicate | Integrity/provenance concerns cannot be ignored. | No successful confirmation; durable conflict disposition and escalation. | Both semantic representations and provenance. | Audit + Customer + Security | Suspended for affected obligation/path. | Conflict resolution and incident policy. |
| Out-of-order delivery | No global ordering guarantee is approved. | Evaluate contract-specific preconditions; do not infer ordering from arrival time. | Mutation/contract relationship evidence. | Audit + Customer contract owners | Case-specific. | Ordering semantics if the contract requires them. |
| Audit ingestion/storage outage | Silent loss is forbidden; synchronous ingestion is not universally required. | Preserve producer obligation and pending state; do not fabricate confirmation. | Customer obligation plus trusted outage/backlog evidence. | Audit Operations + Customer Operations | Conditional; requires active approved policy and valid DEC-014 gates. | Executable operation-specific failure policy. |
| ACK or confirmation loss after Audit commit | Transport ACK is not ingestion truth. | Redeliver or query by ObligationKey; Audit returns/reconstructs the same confirmation. | Audit durable record/idempotency evidence. | Audit + Messaging/Operations | Maintained if evidence is recoverable and trusted. | Confirmation lookup/exchange contract. |
| Unknown backlog | DEC-014 requires trusted visibility. | Suspend deferred-path eligibility until valid visibility and recovery status are restored. | Backlog completeness/health evidence. | Operations | Suspended. | Detection criteria and operational action catalog. |
| Invalid provenance or TenantScope | Missing/conflicting authority fails closed. | Reject or quarantine without successful confirmation; isolate and escalate. | Validation and durable disposition evidence. | Audit + Security | Suspended for affected evidence. | Trust mechanism, quarantine and incident policy. |
| Integrity/recovery evidence failure | Indeterminate integrity or recovery evidence cannot qualify. | Suspend affected deferred path; preserve evidence; authorized investigation/recovery. | Integrity and recovery verification evidence. | Security + Operations + Domains | Suspended. | Integrity mechanism and recovery policy. |
| Producer/Audit mismatch | Neither Domain may overwrite the other's truth. | Enter the matching reconciliation state; expose discrepancy and escalate. | Both contract evidence sets. | Reconciliation workflow + owning Domains | Case-specific; indeterminate gates suspend it. | Resolution authority and correction policy. |
| Sovereign Central disconnection | Local final authority; no mandatory synchronous Central dependency. | Continue locally only under locally valid policy, custody, visibility, integrity and recovery authority. | Sovereign-local evidence. | Sovereign Operations + local Domains | Not suspended solely by Central loss. | Full Air-Gap and duration targets remain Open. |
| Sovereign local Audit outage | Local Audit evidence remains mandatory; Central cannot substitute implicitly. | Preserve local obligations; apply only an approved local policy; suspend deferred path if local gates fail. | Local outage, backlog, custody and recovery evidence. | Sovereign Operations + Audit + Customer | Conditional or suspended according to local evidence. | Local executable policy and validated recovery design. |

## K. Candidate Acceptance Criteria

All criteria are **NOT APPROVED as final Security Requirements** and **NOT_EXECUTED**. They are future-verifiable candidates only.

| ID | Candidate criterion | Contract section | Status |
| --- | --- | --- | --- |
| TC-AC-001 | A covered successful Customer mutation cannot durably commit without its mandatory obligation in the approved Customer-owned consistency boundary. | B, I | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-002 | A mutation is not reported as successful when the required durable obligation was not consistently recorded. | I, J | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-003 | ObligationKey remains stable across publication retry, re-drive, crash recovery and reconciliation. | C | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-004 | Command, mutation, obligation, transport-attempt and Audit-record identities remain distinguishable. | C, D | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-005 | Same-key/same-content Audit redelivery does not create a second authoritative Audit effect. | D, G | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-006 | Missing, invalid or conflicting producer/Tenant provenance cannot produce successful ingestion confirmation. | E, F, J | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-007 | Unsupported contract versions do not produce successful authoritative ingestion. | E, F | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-008 | Audit emits or exposes successful confirmation only after its authoritative record and required processing evidence are durably committed. | F | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-009 | Broker publication acknowledgement and transport delivery disposition are never represented as AUDIT_INGESTION_CONFIRMED. | F | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-010 | Lost acknowledgement or confirmation can be resolved idempotently using the full ObligationKey and Audit-owned evidence. | F, H, J | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-011 | Pending, failed and unresolved producer obligations are discoverable without direct access to Audit persistence. | H | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-012 | Reconciliation preserves tenant isolation, owner authorization and private-database boundaries. | H | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-013 | Dedicated Sovereign performs obligation custody, confirmation, reconciliation and recovery under local authority without mandatory synchronous Central dependency. | H, J | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-014 | Indeterminate backlog, provenance, integrity or recovery evidence suspends the affected deferred pathway and does not fabricate success or rollback. | H, I, J | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-015 | After an ambiguous Customer commit outcome, retry with the same Command identity resolves the prior authoritative outcome before any new mutation is accepted. | D, I | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-016 | Loss of deferred eligibility after commit preserves the committed mutation and obligation, suspends the deferred path and triggers authorized escalation without claiming automatic rollback. | I, J | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-017 | Variation only in transport-attempt metadata is not a semantic conflict, while same-key/different-semantic-content is durably exposed as a conflict and never confirmed as successful ingestion. | G, H | NOT_APPROVED / NOT_EXECUTED |
| TC-AC-018 | A durable rejection or quarantine disposition is distinguishable from, and never reported as, successful authoritative Audit ingestion. | F, H | NOT_APPROVED / NOT_EXECUTED |

Candidate negative tests include duplicate delivery, conflicting content, missing or cross-tenant provenance, unsupported version, crash after Customer commit, broker outage, Audit commit followed by ACK loss, forged confirmation, unauthorized reconciliation lookup, unknown backlog, local Sovereign Audit outage and Central disconnection. Their exact fixtures, tools and expected transport responses remain unapproved.

## L. Technical Contract Approval Register

No signature or approval is implied by this register.

| Approver | Exact clauses requiring approval | Required design evidence | Status |
| --- | --- | --- | --- |
| Customer Domain Owner | C identity generation and uniqueness; D command/mutation/no-op semantics; E producer fields; I commit, ambiguous outcome and response boundaries; Customer-owned parts of H and J. | Customer transaction-boundary design; command and mutation identity lifecycle; concurrency/no-op rules; safe reference and change-category policy; recovery evidence. | **PENDING APPROVAL** |
| Audit Domain Owner | F durable ingestion and confirmation; same-key behavior in G; Audit-owned parts of H and J; Audit fields and dispositions. | Audit durable consistency boundary; idempotency evidence lifecycle; confirmation authority/retrieval; invalid/quarantine semantics; minimized Audit record mapping. | **PENDING APPROVAL** |
| Messaging/Operations Owner | Publication and transport parts of B, G, H and J; backlog discovery, monitoring, re-drive, escalation and profile operation. | Failure detection; authorized re-drive; backlog completeness and recovery evidence; confirmation exchange operations; Dedicated Sovereign local operation plan. No numeric threshold is requested by this draft. | **PENDING APPROVAL** |
| Independent Security Reviewer | Tenant/producer provenance; ObligationKey binding; semantic comparison; confirmation authenticity; conflict/quarantine; reconciliation authorization; negative-test sufficiency. | Threat-boundary review; data minimization; fail-closed paths; cross-tenant denial; integrity/authenticity design; evidence limitations and explicit sign-off scope. | **NOT_SIGNED_OFF** |

### Pending policy and Open Decision dependencies

- OD-008: final API/event versioning and envelope evolution rules.
- OD-011: workload identity used to authenticate producer and reconciliation interactions.
- OD-012: secrets/keys and any future evidence-authenticity mechanism.
- OD-013 and OD-014: concrete migrations and tenant/RLS integration for future implementation.
- OD-019: any scheduling mechanism for publication, recovery or reconciliation.
- OD-020: contract-testing approach.
- OD-023: numeric availability, recovery, backlog and capacity objectives.

These dependencies do not weaken the approved architectural invariants and are not closed by this draft.

### Explicit non-approvals

This draft does not approve:

- An executable or unconditional DURABLE_DEFER policy.
- A Customer API response contract, Event schema, endpoint, database schema or state machine.
- Identifier generation technology, cryptographic algorithm or canonicalization mechanism.
- Retry counts, timeouts, backlog limits, retention, SLO, RTO or RPO.
- A universal failure policy or automatic suspension of all Customer operations.
- Automatic rollback or compensation of a committed Customer mutation.
- A complete Mandatory Audit Event Catalog or read-only Customer Audit policy.
- SR-CAND-001 through SR-CAND-024 as final Security Requirements.
- Any implementation control, executed Negative Test, Security sign-off, risk acceptance or Production Readiness.

V3-003 remains IN PROGRESS. OD-001 through OD-023 remain OPEN.
