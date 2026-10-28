# V3-003 Tenant Security Authority Specialist Review Request

## Document Control

| Field | Recorded value |
| --- | --- |
| Task | `V3-003 — NFR and Threat Assumptions` |
| Document status | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |
| Specialist scope | Tenant Security Authority |
| Tenant Security Authority approval | `PENDING` |
| Security Architecture approval | `PENDING` |
| Independent Security Review | `NOT_SIGNED_OFF` |
| Implementation evidence | `NOT_VERIFIED` |
| Negative-test execution | `NOT_EXECUTED` |
| Executable DURABLE_DEFER | `NOT APPROVED` |

This document requests bounded review by an actual authorized Tenant Security Authority. It records no specialist opinion, approval, reviewer identity, signature, review date, risk acceptance, implementation evidence or test result.

`TS-01` through `TS-05` are local working labels in this request. They are not official DEC, ADR, OD, SR, threat or test identifiers and must not be cited as approved decisions.

## A. Verified Baseline and Document Control

### A.1 Repository and revision identity

| Field | Verified value |
| --- | --- |
| Repository | `IKAC-FIDS/Neshane-CRM-V3-Core` |
| Branch | `main` |
| Preparation HEAD | `73d962ce6e1b7a6e297a9277f0b71d62a3b90bdd` |
| HEAD subject | `docs(security): prepare identity platform specialist review request` |
| Local tracking state before creation | `main...origin/main [ahead 15]` |
| Worktree and index before creation | Clean |
| Target document in preparation HEAD | No |
| Remote publication claim | None; no fetch, stage, commit or push performed |

The preparation HEAD contains the Technical Contract, Consolidated Security Design Review Manifest, Identity/Platform Security Review Request, SEC-01 through SEC-05 and the V3-003 Decision Record. This new request is working-tree content until separately committed; the preparation HEAD must not be represented as containing it.

### A.2 Exact review references

| Document | Git blob in preparation HEAD | SHA-256 | Recorded status |
| --- | --- | --- | --- |
| `architecture/reviews/V3-003-customer-audit-technical-contract-draft.md` | `60cb1e3043a66e587c7b20428e2c68cdd361007a` | `56e71f3ee0537bfc70d0e3f02602175d0e0eb87510fbb7ab43125f37c4010412` | `DRAFT — CROSS-DOMAIN REVIEW REQUIRED` |
| `architecture/reviews/V3-003-consolidated-security-design-review-manifest.md` | `3b0ff1657ff5b8a3218f81d8626242292bd5fb29` | `9592b9e9190d2182132d5eebefbd9fdcb7c802f7f8a8e305b8209db699b90c3e` | `PINNED_FOR_SPECIALIST_REVIEW` |
| `architecture/reviews/V3-003-identity-platform-security-review-request.md` | `28d51bce2c5c840b4913c9c81f3d9675ec0e570a` | `99f64d857ee22b3090bf9ad07fc270c903dab0c620190fba7ac3590c8631cc1e` | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |
| `architecture/reviews/V3-003-SEC-01-bounded-security-design-decision-sheet.md` | `fe176682b60f7aefa4c34ac656b9d0a76369f1f8` | `0394a08682ed911f5c61839ca371e0852072e5621f9b33ffb0e322fec738ca7b` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-02-bounded-security-design-decision-sheet.md` | `3435f546bdfa2ddb6b6bd4a534f7b72782c435af` | `f0b6d9816324cd6f2c0a1bde239a772a677aba41cb05645379f880d65f7fa645` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-03-bounded-security-design-decision-sheet.md` | `30e962d821eb7e9b0e44ac242e2d6960cc81ca12` | `69c1a5de357438cebd2bfd55da0b110fd476c92ca05d21adf0dae3ff2961c655` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-04-bounded-security-design-decision-sheet.md` | `2c6dd64a13d04844012453f7d3d6a7ecd082d077` | `2d03d1cda36c3e9f379824ed46b2c6affb362b504f098a95f137db2e1349f6e6` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-05-bounded-security-design-decision-sheet.md` | `c06e57fb1d90c01e604933482c10860d612b9875` | `a7bf6191f252d20a334d9a315e77fedbff6bec689382edbb528e952dcf809a82` | `DRAFT — SECURITY REVIEW REQUIRED` |

Applicable authority is bounded by ADR-V3-002, ADR-V3-003, ADR-V3-004, ADR-V3-005, ADR-V3-007, ADR-V3-008, ADR-V3-010 and ADR-V3-012; `architecture/standards/security.md`, `persistence.md`, `messaging.md` and `service-architecture.md`; and the still-open OD-001 through OD-023. Existing bounded Owner dispositions are preserved, not expanded.

## B. Tenant Security Authority and Scope

### B.1 Requested authority

The authorized specialist is requested to review only the logical Tenant-security properties of:

- authoritative Tenant Context construction, propagation, immutability and revalidation;
- workload-to-Tenant binding, delegation and multi-tenant workload containment;
- application authorization plus persistence isolation and RLS non-bypass;
- Tenant isolation across Audit ingestion, confirmation, reconciliation, quarantine, re-drive, recovery and monitoring;
- Sovereign-local Tenant authority during connection, disconnection and reconnection.

### B.2 Authority boundaries

The review does not grant the reviewer authority to approve resource-specific business authorization, Identity technology, final database schema, final RLS implementation, event schema, broker design, privileged operational policy, Eligibility Policy Authority, numeric thresholds, implementation correctness or Production Readiness. Specialist conclusions outside verified authority must be recorded as dependencies, not approvals.

### B.3 Core question

Is the following logical invariant sufficient and correctly bounded?

> A Tenant identifier is a selector, not proof of authority. Authoritative Tenant Context must derive from authenticated association or validated provenance plus operation-specific authority; remain immutable for the protected operation and transaction; be revalidated at trust boundaries; and fail closed when missing, invalid, conflicting, stale or indeterminate.

## C. Authoritative Tenant Context Matrix

| Boundary/operation | Candidate authoritative source | Required binding and validation | Prohibited inference | Required failure behavior | Evidence requested |
| --- | --- | --- | --- | --- | --- |
| User authentication | Valid Principal plus active Tenant association | Re-evaluate association when constructing or switching Tenant Context | Authentication/session implies Membership, Entitlement or business authorization | Fail closed | Context-construction contract and switch denial cases |
| Workload authentication | Valid workload identity plus server-controlled Tenant/operation authority | Bind exact workload, Tenant, purpose, operation and validity | Credential, token or header alone establishes Tenant authority | Fail closed | Workload mapping and revocation evidence |
| Customer command | Validated Tenant Context and Customer Domain authorization | Bind Principal/workload, Tenant, resource/action and correlation | Tenant ID implies Customer access | Reject before mutation/disclosure | Authorization decision trace |
| Customer mutation | Customer-owned authorization decision | Keep context immutable across mutation transaction | Later publisher selects a different Tenant | Roll back/reject mismatch | Transaction and context-lifecycle evidence |
| Durable obligation creation | Mutation-bound Tenant Context | Mutation and obligation share the same authoritative Tenant in one transaction boundary | Payload Tenant is independently trusted | Do not create obligation on mismatch/absence | Atomicity and negative-path evidence |
| Publication and redelivery | Tenant preserved from durable obligation | Publisher/re-drive may add attempt metadata but cannot rewrite Tenant truth | Broker identity or mutable header replaces original Tenant | Reject/quarantine without successful ingestion | Envelope/provenance design |
| Audit ingestion | Audit-owned independent validation | Validate producer, contract and Tenant before durable effect | Producer claim automatically trusted | Fail closed; no success confirmation | Ingestion validation evidence |
| Confirmation lookup | Current requester authorization plus immutable obligation Tenant/full key | Bind requester, purpose and `ProducerAuthority + TenantScope + ObligationId` | Knowledge of identifier permits lookup | Deny without existence/status disclosure | Lookup authorization contract |
| Reconciliation | Customer and Audit durable evidence plus current execution authority | Compare exact Tenant and complete identity | One side silently overwrites the other | Preserve conflict and escalate | Reconciliation decision record |
| Manual re-drive | Current privileged identity, explicit scope and original immutable Tenant | Separate execution authority from original producer authority | Generic admin role grants all-Tenant access | Deny unauthorized scope | Privileged authorization evidence |
| Background/recovery worker | Durable job/obligation Tenant plus current workload authorization | Bind each unit of work before access | Worker identity is blanket multi-tenant authority | Fail closed per unit of work | Worker scoping and isolation tests |
| Persistence transaction | Validated transaction-local Tenant Context | Set and clear on the same connection; application authorization plus RLS | Connection/session default or stale pooled value is authoritative | Abort and clear on error | Connection and transaction lifecycle evidence |
| Monitoring | Explicit Tenant/Cell/Profile coverage metadata | Aggregate only authorized and attributable evidence | Missing coverage means zero backlog/healthy | Mark unknown/incomplete | Coverage-integrity evidence |
| Sovereign federation | Locally approved mapping and local authority | Validate local scope, purpose, validity and revocation | Central assertion alone establishes local Tenant authority | Reject/hold pending local decision | Local federation and reconnect evidence |

## D. Delegation and Multi-Tenant Workload Matrix

| Alternative | Architectural status | Security benefit | Primary exposure | Minimum evidence/constraint | Specialist disposition requested |
| --- | --- | --- | --- | --- | --- |
| Tenant-dedicated workload identity | Permissible candidate | Small Tenant blast radius | Credential proliferation and lifecycle complexity | Per-Tenant issuance, rotation, revocation and least privilege | Boundaries and acceptable use cases |
| Multi-tenant workload with server-side per-operation mapping | Preferred logical candidate, not approved implementation | Scalable while retaining explicit scope | Mapping compromise or over-broad grants | Exact Tenant/action mapping, version, revocation, audit and current evaluation | Sufficiency and required containment |
| Tenant-scoped delegated assertion | Conditional candidate | Portable operation-scoped delegation | Replay, stale grant, issuer/audience confusion | Issuer, audience, purpose, expiry, replay defense and revocation semantics | Whether and under what boundaries permissible |
| Authorized intermediary delegation | Conditional candidate | Supports controlled gateway/worker mediation | Confused deputy and scope expansion | Verifiable delegation chain and non-escalation | Required chain constraints |
| Gateway-derived Tenant authority alone | Insufficient/prohibited as sole authority | None sufficient | Gateway compromise or header substitution | Must be corroborated by authoritative mapping and destination authorization | Confirm prohibition |
| Blanket multi-tenant service authority | Architecturally prohibited candidate | Operational convenience only | Cross-tenant blast radius | No blanket authority; every operation scoped | Confirm prohibition |
| Generic operator/admin implied authority | Architecturally prohibited candidate | None sufficient | Privilege escalation and untraceable access | Explicit action, Tenant/Platform scope, authorization and Audit | Confirm prohibition |
| Tenant header/payload as authority | Architecturally prohibited | None | Spoofing and confused deputy | Selector only; never standalone proof | Confirm prohibition |

Every accepted delegation is expected to preserve: original/delegating authority, delegate identity, exact Tenant, operation/contract, resource constraints, purpose, validity and revocation state, delegation chain, correlation and current authorization result. Representation and protocol remain unselected.

## E. Persistence Isolation and RLS Non-Bypass Matrix

| Area | Required logical invariant | Bypass/failure path to address | Required design evidence | Negative-test candidate |
| --- | --- | --- | --- | --- |
| Tenant key | Every Tenant-owned row has explicit Tenant ownership | Missing/ambiguous ownership | Ownership and mapping specification | Missing/wrong Tenant key denied |
| Dual enforcement | Application authorization and RLS both apply | Treating either layer as replacement for the other | Request-to-query authorization trace | App denial cannot be bypassed by SQL; RLS blocks cross-Tenant access |
| Runtime role | Runtime role is non-owner and lacks `BYPASSRLS` | Owner/BYPASS role used at runtime | Role/grant matrix | Runtime identity cannot bypass RLS |
| Read/write policy | Read and write paths are constrained | Incomplete write policy | Policy coverage matrix | Cross-Tenant insert/update/delete denied |
| Transaction-local context | Tenant Context is bound for the transaction on the same connection | Context set after query or on a different connection | Transaction/connection lifecycle design | Query before binding fails |
| Pool reuse | Context is cleared after commit, rollback and error | Stale Tenant leaks to next borrower | Reset and contamination design | Tenant A context not visible to Tenant B request |
| Context immutability | Tenant cannot change mid-transaction | Context-switch attack | Guard/invariant design | Mid-transaction switch aborts |
| Native/bulk SQL | Equivalent isolation applies to alternate query paths | ORM bypass through native or bulk operations | Query-path inventory and controls | Native/bulk cross-Tenant attempt denied |
| Background jobs | Each unit is explicitly Tenant-bound | Worker executes with missing/default Tenant | Job binding contract | Missing/invalid job Tenant fails closed |
| Recovery/Audit consumer | Original Tenant and current authority both apply | Retry/re-drive rewrites Tenant or uses generic scope | Worker and evidence contract | Wrong-Tenant re-drive/ingestion denied |
| Identity separation | Runtime, migration and privileged identities are distinct | Migration/privileged credentials used by runtime | Credential-use and bootstrap boundaries | Runtime cannot assume migration identity |
| Service ownership | No cross-service SQL or shared ownership | Foreign service database access | Ownership and network/credential evidence | Cross-service database access denied |

OD-014 leaves the implementation pattern open. Transaction interceptor, explicit Unit of Work, connection wrapper, repository/session hook or a carefully governed combination remain candidates only. The specialist is asked to approve or amend the logical invariants, not select a framework mechanism.

## F. Audit, Recovery and Monitoring Tenant Isolation Matrix

| Activity | Tenant-isolation rule proposed for review | Failure/misuse concern | Required outcome/evidence |
| --- | --- | --- | --- |
| Durable Audit ingestion | Full identity includes `ProducerAuthority + TenantScope + ObligationId`; Audit validates independently | Cross-Tenant ingestion or forged Tenant | Reject/quarantine without successful confirmation; attributable evidence |
| Duplicate detection | Same `ObligationId` in different Tenants is not the same complete identity | Cross-Tenant deduplication collision | Tenant-partitioned identity evidence |
| Semantic conflict | Conflict comparison occurs only after authority and Tenant validation | Treating mismatch as ordinary semantic conflict | Tenant/provenance mismatch fails closed first |
| Confirmation | Audit-owned confirmation binds full key, durable-ingestion evidence and Audit authority | Forged or cross-Tenant confirmation | Reject without state advancement |
| Confirmation lookup | Current requester must be authorized for exact Tenant and purpose | Existence/status oracle across Tenants | Non-disclosing denial evidence |
| Quarantine inspection/release | Both inspection and release are Tenant-scoped privileged actions | Cross-Tenant evidence disclosure or release | Separate authorization and Audit evidence |
| Reconciliation | Original committed Tenant truth is immutable; execution is currently authorized | Silent conflict winner or Tenant rewrite | Preserved conflict and escalation trail |
| Re-drive/recovery | Preserve original Tenant; re-authorize present action | Stale/generic authority changes another Tenant | Explicit action/Tenant scope and idempotent outcome |
| Authorization change after commit | Original evidence remains; future privileged action uses current authorization | Retroactive rewrite or stale privilege | Separate historical truth from current execution authority |
| Monitoring aggregation | Every result declares Tenant/Cell/Profile coverage and freshness | Hidden partial coverage or cross-Tenant disclosure | Unknown/incomplete is explicit; access-controlled aggregation |
| Tenant suspension | Suspension semantics are explicit per action | Continued mutation/recovery under stale state | Defined fail-closed and exception authority, if any |
| Tenant restoration | Restoration does not silently revive stale credentials or work | Unauthorized replay after restoration | Revalidation and controlled resumption evidence |

## G. Sovereign-local Tenant Authority Matrix

| Concern | Candidate boundary | Prohibited behavior | Evidence requested |
| --- | --- | --- | --- |
| Tenant identity/association | Locally final source or locally approved federation mapping | Central assertion automatically creates local association | Local association lifecycle |
| Tenant Context | Constructed and validated locally for local operations | Mandatory central round trip for basic authority | Disconnected context-validation design |
| Workload mapping | Locally governed workload-to-Tenant/action mapping | Central credential implies unrestricted local authority | Local mapping and revocation evidence |
| Privileged scope | Local explicit Tenant/Platform scope and authorization | Remote operator/admin implied privilege | Local privileged-access contract |
| Audit boundary | Local Audit authority and Tenant isolation remain final | Central override of local Audit truth | Local ingestion/lookup/recovery design |
| Recovery | Locally authorized and based on local durable evidence | Remote re-drive without local authorization | Recovery authorization and evidence |
| Disconnection | Essential local authorization remains operable or fails closed by approved policy | Fail-open due to central unavailability | Disconnected-mode decision and tests |
| Local revocation | Local revocation takes effect locally | Reconnection reactivates stale central grant | Revocation precedence and reconciliation evidence |
| Reconnection | Differences are reconciled without automatic winner | Silent Central overwrite or cross-Tenant merge | Conflict-preserving reconciliation contract |
| Residency | Tenant evidence stays within approved residency boundary | Unapproved export through monitoring/federation | Data-flow and disclosure evidence |

`Full Air-Gap` behavior, maximum disconnection periods, federation protocol, conflict policy and technology remain unapproved. ADR-V3-004's Sovereign-local final authority is not weakened.

## H. TS-01 through TS-05 Decision Requests

### TS-01 — Authoritative Tenant Context

**Status:** `PROPOSED — TENANT SECURITY AUTHORITY REVIEW REQUIRED`

- **Proposed clause:** Tenant identifiers are selectors, not authority. An authoritative Tenant Context derives from authenticated association or validated provenance plus operation-specific authority, remains immutable for the protected operation and persistence transaction, is revalidated at trust boundaries and fails closed when missing, invalid, conflicting, stale or indeterminate.
- **Preferred logical direction:** one explicit operation-bound context with server-controlled construction and transaction binding.
- **Alternatives retained:** association-based user context, workload delegation and profile-local mapping, provided each meets the invariant.
- **Rejected boundary:** caller-controlled header, payload, session or gateway claim as standalone authority.
- **Threats/abuse:** `AB-002`, `AB-003`, `AB-007`, `AB-009`.
- **Evidence required:** construction, propagation, switch, conflict, transaction binding, denial and disclosure behavior.
- **Related Open Decisions:** `OD-011`, `OD-014`, `OD-020`.
- **Dependencies:** Identity/Platform Security, Customer and Audit Domain authorities, Security Architecture.
- **Reviewer questions:** What minimum facts make context authoritative? Which fields are immutable versus selectors? At which boundaries is revalidation mandatory?

### TS-02 — Workload Tenant Binding and Delegation

**Status:** `PROPOSED — TENANT SECURITY AUTHORITY REVIEW REQUIRED`

- **Proposed clause:** A valid workload credential alone grants no Tenant authority. Each operation requires explicit, current and non-escalating workload-to-Tenant/action authority with bounded validity and revocation.
- **Preferred logical direction:** server-controlled, per-operation mapping for multi-tenant workloads.
- **Alternatives retained:** Tenant-dedicated identity, Tenant-scoped delegated assertion and authorized intermediary delegation within approved boundaries.
- **Rejected boundary:** blanket multi-tenant authority, generic operator authority, or gateway/header-derived authority alone.
- **Threats/abuse:** `AB-004`, `AB-005`, `AB-007`, `AB-009`.
- **Evidence required:** exact scope, expiry, revocation, delegation chain, purpose, blast-radius and current-evaluation behavior.
- **Related Open Decisions:** `OD-011`, `OD-012`, `OD-020`.
- **Dependencies:** Identity/Platform Security, Contract Governance, Messaging/API Event Architecture.
- **Reviewer questions:** Which delegation chains are permissible? What revocation/freshness conditions fail closed? What maximum logical authority may one workload hold absent a separate exception decision?

### TS-03 — Persistence Isolation and RLS Enforcement

**Status:** `PROPOSED — TENANT SECURITY AUTHORITY REVIEW REQUIRED`

- **Proposed clause:** Tenant-owned persistence requires application authorization, explicit Tenant ownership, transaction-local validated Tenant Context and non-bypass RLS. Runtime identities are non-owner, lack `BYPASSRLS`, and are separate from migration and privileged identities.
- **Preferred logical direction:** explicit transaction lifecycle on the same connection with deterministic cleanup after commit, rollback and error.
- **Alternatives retained:** OD-014 integration patterns that demonstrably preserve the same invariants.
- **Rejected boundary:** unscoped/default Tenant access, runtime owner/BYPASS role, shared cross-service SQL or privileged credential reuse.
- **Threats/abuse:** `AB-002`, `AB-006`, `AB-007`.
- **Evidence required:** role/grant matrix, policies, pool lifecycle, rollback/reuse, native/bulk paths and multi-Tenant negative tests.
- **Related Open Decisions:** `OD-013`, `OD-014`, `OD-020`.
- **Dependencies:** Data/Backend Architecture, each persistence-owning service, Security Architecture.
- **Reviewer questions:** What minimum transaction/connection invariant is mandatory? Which role properties are prohibited? How must workers, consumers and recovery paths establish context?

### TS-04 — Audit and Recovery Tenant Isolation

**Status:** `PROPOSED — TENANT SECURITY AUTHORITY REVIEW REQUIRED`

- **Proposed clause:** Original Tenant evidence is immutable; every later lookup, quarantine, reconciliation, re-drive and recovery action also requires current authorization for its exact Tenant and purpose. Complete obligation identity includes Tenant and producer authority.
- **Preferred logical direction:** full-key isolation plus current authorization at every privileged action.
- **Rejected boundary:** original authorization alone, generic operator scope or identifier knowledge as current authority.
- **Threats/abuse:** `AB-007`, `AB-009`, `AB-013`, `AB-016`, `AB-017`.
- **Evidence required:** cross-Tenant collisions, non-disclosing lookup denial, quarantine, re-drive and authorization-change scenarios.
- **Related Open Decisions:** `OD-008`, `OD-011`, `OD-014`, `OD-019`, `OD-020`.
- **Dependencies:** Audit Domain, Messaging/Operations, Contract Governance, Security Architecture.
- **Reviewer questions:** Which actions require fresh re-authorization? What is the mandatory disposition for Tenant mismatch? What denial response prevents an existence oracle?

### TS-05 — Sovereign-local Tenant Authority

**Status:** `PROPOSED — TENANT SECURITY AUTHORITY REVIEW REQUIRED`

- **Proposed clause:** Dedicated Sovereign retains locally final Tenant association, context validation, workload mapping, privileged scope, revocation, Audit and recovery authority during connected, disconnected and reconnection states.
- **Preferred logical direction:** locally authoritative operation with explicitly bounded and locally approved federation metadata.
- **Alternatives retained:** local-only or assisted provisioning that never displaces local final authority.
- **Rejected boundary:** Central authority as automatic local authority or automatic conflict winner.
- **Threats/abuse:** `AB-019`, `AB-020` and cross-Tenant federation misuse.
- **Evidence required:** local mapping/revocation, disconnected operation, Central-denial and conflict-preserving reconnection behavior.
- **Related Open Decisions:** `OD-001`, `OD-011`, `OD-012`, `OD-015`, `OD-023`.
- **Dependencies:** Sovereign Operations, Identity/Platform Security, Messaging/Operations, Security Architecture.
- **Reviewer questions:** Which local authorities are final? How is stale Central state handled after local revocation? How is reconnection prevented from selecting an automatic winner?

## I. Threat and Negative-Test Traceability

| Security concern | Threat/abuse reference | Existing candidate test reference | Additional candidate | Execution status |
| --- | --- | --- | --- | --- |
| Spoofed `TenantScope` | `AB-002` | `NT-002`; `SR-CAND-003/004` context | — | `NOT_EXECUTED` |
| Cross-Tenant mutation/disclosure | `AB-003`, `AB-007` | `NT-003`, `NT-007`; `SR-CAND-005/007/008` context | — | `NOT_EXECUTED` |
| Cross-Tenant Audit ingestion | `AB-007`, `AB-009` | `NT-007`, `NT-009`; `SR-CAND-011/012` context | — | `NOT_EXECUTED` |
| Confirmation lookup oracle | `AB-007`, `AB-009` | `NT-002/007/009` family | `NEW_CANDIDATE — NOT REGISTERED`: deny wrong-Tenant lookup without status/existence disclosure | `NOT_EXECUTED` |
| Wrong-Tenant re-drive | `AB-009`, `AB-013` | `NT-009`, `NT-013` | `NEW_CANDIDATE — NOT REGISTERED`: exact Tenant/action authorization on re-drive | `NOT_EXECUTED` |
| Excessive multi-tenant workload scope | `AB-004`, `AB-007`, `AB-009` | `NT-004/007/009` family | `NEW_CANDIDATE — NOT REGISTERED`: workload cannot exceed mapped Tenant scope | `NOT_EXECUTED` |
| Stale delegated authority | `AB-005` | `NT-005` | `NEW_CANDIDATE — NOT REGISTERED`: revoked/expired delegation fails closed | `NOT_EXECUTED` |
| Confused deputy | `AB-004` | `NT-004` | `NEW_CANDIDATE — NOT REGISTERED`: purpose/resource constraint cannot expand | `NOT_EXECUTED` |
| RLS bypass | `AB-007` | `NT-007`; `SR-CAND-007/008` context | — | `NOT_EXECUTED` |
| Pooled connection Tenant leakage | `AB-007` | `NT-007` family | `NEW_CANDIDATE — NOT REGISTERED`: commit/rollback/error reuse contamination | `NOT_EXECUTED` |
| Missing worker Tenant Context | `AB-002`, `AB-007` | `NT-002/007` family | `NEW_CANDIDATE — NOT REGISTERED`: background/recovery work fails closed | `NOT_EXECUTED` |
| Generic admin Tenant bypass | `AB-013` | `NT-013`; `SR-CAND-015/016` context | — | `NOT_EXECUTED` |
| Cross-Tenant quarantine disclosure | `AB-017` | `NT-017`; `SR-CAND-019/020` context | `NEW_CANDIDATE — NOT REGISTERED`: inspect/release isolation | `NOT_EXECUTED` |
| Hidden monitoring coverage | `AB-013`, `AB-016` | `NT-013`, `NT-016`; `OPS-AC-002/016` | — | `NOT_EXECUTED` |
| Central override of Sovereign authority | `AB-019`, `AB-020` | `NT-019`; `SR-CAND-021/022` context | `NEW_CANDIDATE — NOT REGISTERED`: stale Central state cannot revive local revocation | `NOT_EXECUTED` |

These mappings are review inputs only. They neither register additional official tests nor approve any SR-CAND item.

## J. Evidence Gaps and Specialist Dependencies

| Gap | Required completion artifact | Primary responsible authority | Specialist dependency | Current status |
| --- | --- | --- | --- | --- |
| Authoritative Tenant Context fact model | Reviewed logical context contract and boundary matrix | Tenant Security Authority | Identity/Platform; Domain authorities | `PENDING` |
| Tenant switching and association freshness | Context-switch and revocation policy | Tenant Security + Identity/Platform | Security Architecture | `PENDING` |
| Multi-tenant workload delegation | Delegation model, scope and revocation contract | Tenant Security + Identity/Platform | Messaging/Contract Governance | `PENDING` |
| Persistence/RLS integration | Transaction/connection lifecycle and role-policy design | Data/Backend Architecture | Tenant Security; Security Architecture | `PENDING` |
| Pool contamination prevention | Cleanup/error/reuse design and executable test plan | Persistence owners | Tenant Security | `DESIGN_EVIDENCE_MISSING` |
| Worker/consumer Tenant binding | Background/recovery execution contract | Owning Domain + Operations | Tenant Security; Identity/Platform | `PENDING` |
| Audit lookup disclosure policy | Resource/action authorization and denial semantics | Audit Domain | Tenant Security; Security Architecture | `PENDING` |
| Quarantine and re-drive isolation | Privileged action catalog and scope contract | Audit + Operations | Tenant Security; Operational Policy | `PENDING` |
| Monitoring coverage integrity | Tenant/Cell/Profile coverage and access-control contract | Operations | Tenant Security | `PENDING` |
| Sovereign-local Tenant authority | Local authority, revocation and reconnect policy | Sovereign Operations | Tenant Security; Identity/Platform; Security Architecture | `PENDING` |
| Eligibility exceptions | Explicit authority assignment and eligibility policy | Not yet assigned | Owner decision | `DEFERRED` |
| Implementation and negative tests | Executable evidence against approved design | Implementation owners | Independent Security Review | `NOT_VERIFIED / NOT_EXECUTED` |

## K. Authorized Reviewer Disposition Template

This section must be completed only by a verified reviewer acting within documented Tenant Security Authority. Blank fields are intentional.

### K.1 Reviewer provenance

| Field | Reviewer-supplied value |
| --- | --- |
| Reviewer identity/authenticated reference |  |
| Tenant Security authority basis |  |
| Independence and conflicts |  |
| Review scope |  |
| Exact Git revision reviewed |  |
| Exact document SHA-256 reviewed |  |
| Review date, if supplied |  |
| Limitations |  |
| Sign-off scope/status |  |

### K.2 Per-item disposition

Permitted values: `APPROVE_WITH_BOUNDARIES`, `AMEND`, `REJECT`, `BLOCKED`, `EVIDENCE_REQUIRED`.

| Item | Reviewer disposition | Approved/amended boundaries or replacement wording | Rationale and evidence | Conditions/dependencies | Reviewer reference |
| --- | --- | --- | --- | --- | --- |
| `TS-01` |  |  |  |  |  |
| `TS-02` |  |  |  |  |  |
| `TS-03` |  |  |  |  |  |
| `TS-04` |  |  |  |  |  |
| `TS-05` |  |  |  |  |  |

### K.3 Cross-cutting findings

| Field | Reviewer-supplied value |
| --- | --- |
| Additional evidence requests |  |
| Conflicts with approved architecture |  |
| Required separate decisions |  |
| Residual limitations |  |
| Independent Security Review handoff notes |  |

No blank field implies approval. A specialist disposition is not an Independent Security Review sign-off, risk acceptance or implementation verification.

## L. Explicit Non-Approvals and Governance Status

This request does **not** approve:

- `TS-01` through `TS-05` or any final Tenant-security design;
- Tenant Context schema, token claims, delegation protocol or credential technology;
- final RLS policy, physical schema, database role/grant matrix or OD-014 integration pattern;
- final event/API schema, broker topology, confirmation protocol or canonicalization;
- privileged role model, quarantine/re-drive policy, Eligibility Policy Authority or operational exception;
- Full Air-Gap behavior, numeric disconnection limits or federation conflict policy;
- any SR-CAND item, risk rating, mitigation, risk acceptance or security exception;
- implementation correctness, runtime security, executed negative tests, executable DURABLE_DEFER or Production Readiness.

The following governance state is preserved exactly:

```text
V3-003 = IN PROGRESS
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
TENANT_SECURITY_AUTHORITY_APPROVAL = PENDING
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

The next bounded action is an actual authorized Tenant Security Authority review of the exact content hash of this request and its pinned references. Any resulting disposition must preserve reviewer provenance, reviewed baseline, authority scope, limitations and candidate-specific rationale. No repository status may be upgraded merely because this request exists.
