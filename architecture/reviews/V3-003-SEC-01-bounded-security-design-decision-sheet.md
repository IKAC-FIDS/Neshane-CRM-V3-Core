# V3-003 SEC-01 — Bounded Security Design Decision Sheet

## A. Document Control

| Field | Value |
| --- | --- |
| Status | **DRAFT — SECURITY REVIEW REQUIRED** |
| Task | V3-003 — NFR and Threat Assumptions |
| Security scope | S1 — Producer Identity and Provenance; S2 — Tenant Isolation; S3 — Audit Confirmation Authenticity |
| Decision labels | SD-01 through SD-04 are local working identifiers only; they are not official V3-003-DEC, ADR or Security Requirement identifiers |
| Project and Domain bounded dispositions | **APPROVED_WITH_BOUNDARIES_OR_AMENDMENTS** |
| Identity/Platform Security approval | **PENDING** |
| Tenant Security Authority approval | **PENDING** |
| Security Architecture approval | **PENDING** |
| Independent Security Review | **NOT_SIGNED_OFF** |
| Implementation evidence | **NOT_VERIFIED** |
| Negative-test execution | **NOT_EXECUTED** |
| Executable DURABLE_DEFER | **NOT APPROVED** |

This document records four bounded Project/Domain Owner dispositions while preserving all Security Authority approvals and Independent Security Review as pending. The recorded dispositions are scoped architectural and Domain-design approvals only. They do not establish a fully approved SEC-01 Security Contract, a final Security Requirement, implementation authorization or runtime evidence.

### A.1 Recorded disposition authority

| Field | Recorded value |
| --- | --- |
| Confirmed authority | Project Owner; Customer Domain Owner; Audit Domain Owner; Messaging/Operations Owner |
| Approval evidence | Explicit user instruction authorizing the four bounded dispositions recorded below |
| Approval date | Not recorded |
| Identity/Platform Security Owner authority | Not claimed |
| Tenant Security Authority | Not claimed |
| Independent Security Reviewer authority or sign-off | Not claimed |

## B. Verified Baseline

| Baseline item | Verified value |
| --- | --- |
| Repository | `IKAC-FIDS/Neshane-CRM-V3-Core` |
| Branch at materialization | `main` |
| Git HEAD at materialization | `c28356f99a057ae09a5c119b9bc3e1c08f63a5d7` |
| Worktree and index before materialization | Clean |
| Technical Contract | `architecture/reviews/V3-003-customer-audit-technical-contract-draft.md` |
| Technical Contract Git blob | `60cb1e3043a66e587c7b20428e2c68cdd361007a` |
| Technical Contract SHA-256 | `56e71f3ee0537bfc70d0e3f02602175d0e0eb87510fbb7ab43125f37c4010412` |
| Security Review Input Manifest | `architecture/reviews/V3-003-security-review-input-manifest.md` |
| Manifest Git blob at materialization | `f702d1c3296cd28d921c85abee06f98262b536f9` |

The Contract bytes match the pinned Contract baseline recorded by the Security Review Input Manifest. The current Git HEAD contains both the pinned Contract and the committed Manifest. Repository recording does not constitute Owner approval or Security sign-off.

### B.1 Preserved bounded approvals

- Six Customer Domain business-semantics principles remain **APPROVED — CUSTOMER DOMAIN OWNER, BOUNDED PRINCIPLES ONLY**.
- Audit dispositions C3, C5, F and G/H remain **APPROVED — AUDIT DOMAIN OWNER, BOUNDED SCOPE ONLY**.
- Messaging/Operations dispositions O1 through O5 remain **APPROVED — MESSAGING/OPERATIONS OWNER, BOUNDED SCOPE ONLY**.
- The overall Customer/Audit Technical Contract remains **DRAFT — CROSS-DOMAIN REVIEW REQUIRED**.
- Remaining Customer, Audit and operational mechanics remain pending exactly as recorded in the Contract.

## C. SD-01 — Workload Trust Layers

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

### C.1 Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- The logical separation of Transport Peer Authentication, Authenticated Workload Identity, `ProducerAuthority`, Contract/Event Authority and Operation-scoped Tenant Authority.
- Independent validation and authorization at every receiving trust boundary.
- Server-controlled mappings from authenticated workload identity to the applicable authorities.
- Revocation-capable trust and a credential lifecycle that covers issuance, rotation, revocation and compromise response.
- Sovereign-local trust authority without mandatory synchronous Central dependency.

The disposition does not approve Identity/Platform Security policy, issuer or trust-domain configuration, credential profile, technology, final rotation/revocation mechanics or Independent Security Review.

### C.2 Approved bounded logical clause

Service-to-service trust shall preserve five logically separate layers:

1. **Transport Peer Authentication** identifies the peer participating in a protected transport connection. It does not establish Domain, contract or Tenant authority.
2. **Authenticated Workload Identity** identifies the calling workload through validated issuer or trust domain, intended audience, validity and revocation state.
3. **ProducerAuthority** is derived through a server-controlled mapping from the authenticated workload identity. A caller-provided field, arbitrary header or internal network location cannot establish it.
4. **Contract/Event Authority** limits which contract types and versions the producer is permitted to publish or invoke.
5. **Operation-scoped Tenant Authority** limits which operation the workload may perform for the authoritative `TenantScope`. A workload identity, including a multi-tenant workload identity, does not by itself grant access to every Tenant.

Every receiving trust boundary shall independently authenticate the workload and authorize the required producer, contract and Tenant authorities. Missing, expired, revoked, indeterminate or conflicting evidence shall fail closed before Domain or persistence work.

Credential lifecycle requirements shall cover issuance, activation, bounded validity, rotation, controlled overlap, revocation, compromise response, retirement and traceable administration. Dedicated Sovereign shall retain locally authoritative trust, credential validation and revocation without mandatory synchronous Central dependency.

### C.3 Preferred logical option and rationale

Adopt a technology-neutral layered trust contract capable of later realization through approved platform-issued credentials, mTLS/PKI, signed workload assertions, a SPIFFE/SPIRE-like model or a hybrid.

This option separates identity from authority, prevents network or transport identity from becoming implicit business authorization, supports least privilege at contract and Tenant scope, and avoids closing `OD-011` or `OD-012` prematurely.

### C.4 Alternatives and trade-offs

| Alternative | Disposition | Trade-off or boundary |
| --- | --- | --- |
| Internal network, address, DNS or transport connection as authority | **ARCHITECTURALLY PROHIBITED** | Network position is not trust and cannot establish ProducerAuthority or Tenant authority. |
| One shared credential with undifferentiated authority | **REJECTED CANDIDATE** | Collapses workload identity and authority and prevents least-privilege attribution and revocation. |
| mTLS/PKI only | **DEFERRED** | Strong peer authentication candidate; producer, contract and Tenant authorization still require explicit binding. |
| Signed workload token/assertion only | **DEFERRED** | Portable authority evidence candidate; issuer, audience, replay, rotation and revocation mechanics remain unresolved. |
| SPIFFE/SPIRE-like identity | **DEFERRED** | Standardized workload identity candidate; platform fit, custody and Sovereign operation remain undecided. |
| Hybrid identity model | **DEFERRED** | May separate channel and authority evidence but adds lifecycle and operational complexity. |

### C.5 Approval, evidence and review dependencies

| Dimension | Required record |
| --- | --- |
| Recorded Project/Domain authority | **APPROVED WITH BOUNDARIES** by Project, Customer, Audit and Messaging/Operations Owner authority |
| Pending Security authorities | Identity/Platform Security approval and Security Architecture approval |
| Related Open Decisions | `OD-011`, `OD-012`; profile operation also depends on `OD-015` and `OD-023` without closing them |
| Required design evidence | Trust-domain model; identity-to-ProducerAuthority mapping; contract-authority matrix; operation/Tenant authorization model; issuance/rotation/revocation/compromise lifecycle; profile-specific custody model |
| Independent Security Reviewer dependency | Validate layer separation, issuer/audience and scope checks, revocation behavior, fail-closed paths, confused-deputy resistance and Sovereign-local authority |
| Explicit unresolved implementation details | Identity provider, credential format, protocol, cryptographic algorithms, key storage, credential lifetime, rotation windows, revocation propagation and runtime technology |

### C.6 Candidate negative tests

All tests remain **NOT_EXECUTED**.

- Existing traceability: `NT-009`, `TC-AC-006/007`, `OPS-AC-006`.
- Forged workload mapped to Customer `ProducerAuthority` — `NEW_CANDIDATE — NOT REGISTERED`.
- Expired or revoked workload credential — `NEW_CANDIDATE — NOT REGISTERED`.
- Wrong issuer, trust domain or audience — `NEW_CANDIDATE — NOT REGISTERED`.
- Valid workload attempting an unauthorized contract/version — `NEW_CANDIDATE — NOT REGISTERED`.
- Multi-tenant workload attempting an unauthorized Tenant operation — `NEW_CANDIDATE — NOT REGISTERED`.
- Central identity attempting to replace Sovereign-local authority — `NEW_CANDIDATE — NOT REGISTERED`.

## D. SD-02 — Producer Provenance Across Messaging

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

### D.1 Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- Receiver-verifiable original producer provenance across publication, brokers, direct consumers, retries and re-drive.
- The prohibition on substituting broker identity for original `ProducerAuthority`.
- The rule that mutable producer headers do not establish authority.
- Preservation of original provenance during retry and re-drive.
- Explicitly authorized intermediary re-attestation as an architecturally permissible alternative.
- A trusted provenance envelope as the preferred logical candidate, not as an approved wire format.

Security approval, exact provenance encoding, integrity mechanism, chain-of-custody representation, key custody and lifecycle, and Independent Security Review remain pending.

### D.2 Approved bounded logical clause

The authenticated original Customer producer provenance shall remain receiver-verifiable across Customer publication, messaging transport, Audit consumption, direct-consumer delivery, retries and authorized re-drive.

- Customer publication shall derive provenance from authenticated workload evidence and server-controlled authority mappings.
- Broker or publication-component identity is transport or delivery identity and shall remain distinct from the original Customer `ProducerAuthority`.
- Audit and every direct consumer shall independently validate original producer provenance, contract authority and authoritative Tenant binding.
- Retry and re-drive shall preserve the same semantic obligation and original producer provenance. A changing transport-attempt identity shall not change the obligation authority or meaning.
- Operations and messaging components shall not fabricate, replace or elevate original producer authority, Tenant scope or semantic content.
- A mutable producer header alone shall never establish authority.
- Any intermediary re-attestation shall require explicit authority and shall distinguish the original producer, intermediary identity and any permitted transformation.

### D.3 Preferred logical option and rationale

Use a **receiver-verifiable trusted provenance envelope** as the preferred logical candidate. The logical envelope shall bind original `ProducerAuthority`, authoritative `TenantScope`, contract type/version, `ObligationId` and required correlation evidence to verifiable trust evidence.

This candidate preserves original authority across transport boundaries, supports direct consumers and re-drive, and prevents the broker connection from becoming the producer source of truth. It does not select an envelope representation or authenticity technology.

### D.4 Alternatives and trade-offs

| Alternative | Disposition | Trade-off or boundary |
| --- | --- | --- |
| Mutable producer or Tenant headers | **ARCHITECTURALLY PROHIBITED AS AUTHORITY** | May be selectors or carried metadata only after independent validation. |
| Broker connection identity as original producer | **REJECTED CANDIDATE** | Confuses transport authority with Domain producer authority. |
| Re-drive under operator identity replacing original provenance | **REJECTED CANDIDATE** | Destroys chain of custody and permits authority escalation. |
| Authenticated metadata propagation | **PERMISSIBLE — DESIGN DECISION REQUIRED** | Viable only where consumers can independently validate origin, integrity, scope and version. |
| Explicit intermediary re-attestation | **PERMISSIBLE — DESIGN DECISION REQUIRED** | Can support controlled mediation but must preserve original provenance and transformation evidence. |
| Trusted provenance envelope | **PREFERRED LOGICAL CANDIDATE — NOT APPROVED** | Clear receiver-verifiable boundary; final format, integrity mechanism and key lifecycle remain open. |

### D.5 Approval, evidence and review dependencies

| Dimension | Required record |
| --- | --- |
| Recorded Project/Domain authority | **APPROVED WITH BOUNDARIES** by Project, Customer, Audit and Messaging/Operations Owner authority |
| Pending Security authorities | Identity/Platform Security approval and Security Architecture approval |
| Related Open Decisions | `OD-008`, `OD-011`, `OD-012`, `OD-020` |
| Required design evidence | Canonical provenance fields and ownership; producer/contract authority rules; integrity/authenticity threat analysis; direct-consumer validation; retry/re-drive chain of custody; version/downgrade behavior; safe rejection evidence |
| Independent Security Reviewer dependency | Validate forgery resistance, confused-deputy prevention, replay handling, downgrade behavior, direct-consumer checks and privileged re-drive authority |
| Explicit unresolved implementation details | Envelope format, signature or equivalent mechanism, metadata representation, key infrastructure, broker configuration, contract schema and validation libraries |

### D.6 Candidate negative tests

All tests remain **NOT_EXECUTED**.

- Existing traceability: `NT-009`, `TC-AC-006/007`, `OPS-AC-006`.
- Mutable producer header substitution — `NEW_CANDIDATE — NOT REGISTERED`.
- Broker identity substituted for Customer producer — `NEW_CANDIDATE — NOT REGISTERED`.
- Re-drive changing original `ProducerAuthority` — `NEW_CANDIDATE — NOT REGISTERED`.
- Provenance valid for one contract reused for another — `NEW_CANDIDATE — NOT REGISTERED`.
- Unsupported or downgraded provenance version — `NEW_CANDIDATE — NOT REGISTERED`.
- Same obligation delivered with different producer or semantic content — `NEW_CANDIDATE — NOT REGISTERED`.
- Direct consumer accepting delivery without independent provenance validation — `NEW_CANDIDATE — NOT REGISTERED`.

## E. SD-03 — Authoritative Tenant Binding

**Status: APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

### E.1 Recorded bounded disposition

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve:

- Binding `TenantScope` to the same authoritative obligation throughout Customer authorization, durable obligation creation, publication, redelivery, Audit ingestion, confirmation lookup, reconciliation and privileged recovery.
- Derivation of Tenant authority from validated context plus operation authorization.
- Independent validation of Tenant and Producer binding by every receiving boundary.
- Multi-tenant workload operation only with explicit operation-scoped Tenant authorization.
- Fail-closed handling of cross-Tenant, missing or conflicting Tenant evidence.
- Shared SaaS application authorization, PostgreSQL RLS and non-bypass runtime requirements.
- Dedicated Sovereign local Tenant authority.

Tenant Security Authority approval, Data/Security Architecture approval, the `OD-014` integration mechanism, delegation representation, runtime verification, Negative Test execution and Independent Security Review remain pending.

### E.2 Approved bounded logical clause

The same authoritative Tenant binding shall remain immutable for an obligation across:

1. Customer mutation authorization.
2. Durable obligation creation.
3. Publication, retry and re-drive.
4. Audit ingestion.
5. Confirmation lookup.
6. Reconciliation and privileged recovery.

The semantic lookup and reconciliation scope is:

`ProducerAuthority + TenantScope + ObligationId`

`TenantScope` shall be established only from validated user membership or trusted workload provenance combined with operation-scoped authorization. A client field, arbitrary message header or workload identity without Tenant authority is a selector, not authority.

Every receiving trust boundary shall independently validate Tenant binding. A multi-tenant workload identity is permissible only where the specific operation carries explicit authority for the target Tenant. Missing, conflicting, defaulted or mismatched Tenant evidence and cross-Tenant lookup shall fail closed and shall not receive successful ingestion confirmation or automatic reconciliation.

Shared SaaS shall preserve both application-level authorization and PostgreSQL RLS for Tenant-owned data. Ordinary runtime roles shall not own protected tables or possess `BYPASSRLS`. Dedicated Sovereign shall retain locally authoritative Tenant validation, persistence context, confirmation lookup and recovery authority.

### E.3 Preferred logical option and rationale

Adopt **end-to-end immutable Tenant binding with independent validation at every receiving trust boundary**.

This option preserves Domain-owned authorization, service-owned persistence, Shared SaaS defense in depth and Sovereign-local authority. It prevents a valid multi-tenant workload identity from becoming implicit cross-Tenant permission.

### E.4 Alternatives and trade-offs

| Alternative | Disposition | Trade-off or boundary |
| --- | --- | --- |
| Client or message Tenant field as authority | **ARCHITECTURALLY PROHIBITED** | Untrusted input cannot establish Tenant Context. |
| Default Tenant when context is absent | **ARCHITECTURALLY PROHIBITED** | Converts missing authority into implicit access. |
| Publisher-only or gateway-only Tenant authorization | **REJECTED CANDIDATE** | Receiving Domains must enforce their own resource/action authorization. |
| Lookup by `ObligationId` alone | **REJECTED CANDIDATE** | Permits cross-producer or cross-Tenant ambiguity. |
| Explicit operation-scoped delegation for multi-tenant workloads | **PERMISSIBLE — DESIGN AND SECURITY REVIEW REQUIRED** | Supports platform workloads while preserving bounded Tenant authority. |
| Exact Java/RLS integration mechanism | **DEFERRED TO OD-014** | Must later prove transaction-local context and pooled-connection safety. |

### E.5 Approval, evidence and review dependencies

| Dimension | Required record |
| --- | --- |
| Recorded Project/Domain authority | **APPROVED WITH BOUNDARIES** by Project, Customer, Audit and Messaging/Operations Owner authority |
| Pending Security authorities | Tenant Security Authority approval; Data/Security Architecture approval; Identity/Platform Security approval |
| Related Open Decisions | `OD-011`, `OD-012`, `OD-014`; implementation evidence also depends on `OD-013` and `OD-020` |
| Required design evidence | Authoritative Tenant provenance; multi-tenant delegation matrix; propagation across messages/jobs/re-drive; lookup/reconciliation authorization; transaction-local RLS design; runtime role/grant model; Sovereign-local Tenant trust and recovery |
| Independent Security Reviewer dependency | Validate cross-Tenant denial, context-confusion resistance, operation-scoped authority, RLS non-bypass, pooled-connection safety and privileged recovery |
| Explicit unresolved implementation details | Tenant assertion format, delegation representation, Java transaction-context mechanism, RLS session-setting mechanism, database role/grant implementation and persistence tooling |

### E.6 Candidate negative tests

All tests remain **NOT_EXECUTED**.

- Existing traceability: `NT-002/007/009`, `TC-AC-006/012`, `OPS-AC-009/016`.
- Missing or conflicting Tenant Context — existing scenario family; execution remains pending.
- Tenant substitution during publication — `NEW_CANDIDATE — NOT REGISTERED`.
- Cross-Tenant re-drive or Audit ingestion — `NEW_CANDIDATE — NOT REGISTERED`.
- Cross-Tenant confirmation lookup — `NEW_CANDIDATE — NOT REGISTERED`.
- `ObligationId` collision across Tenant scopes — `NEW_CANDIDATE — NOT REGISTERED`.
- Pooled connection retaining prior Tenant context — `NEW_CANDIDATE — NOT REGISTERED`.
- Runtime database role bypassing RLS — `NEW_CANDIDATE — NOT REGISTERED`.
- Multi-tenant workload exceeding operation-scoped Tenant authority — `NEW_CANDIDATE — NOT REGISTERED`.

## F. SD-04 — Audit Confirmation Verification

**Status: APPROVED WITH AMENDMENTS — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE**

### F.1 Recorded bounded disposition and amendments

The confirmed Project, Customer, Audit and Messaging/Operations Owner authorities approve this bounded direction:

- Authenticated Audit-owned online lookup is the preferred baseline for confirmation recovery and reconciliation.
- Online lookup is not a mandatory synchronous dependency of successful Customer mutation.
- Audit Domain alone owns authoritative durable-ingestion truth.
- Confirmation binds to the complete `ObligationKey`, Audit authority and authoritative Audit evidence.
- Invalid, forged, mismatched, cross-Tenant or unsupported confirmation evidence must not complete reconciliation.
- Dedicated Sovereign uses locally authoritative Audit lookup and confirmation authority.
- Independently verifiable and hybrid models remain architecturally permissible alternatives requiring separate approval.

The approved amendment limits the direction to a preferred baseline rather than a final profile-wide verification selection. Security approval of confirmation trust, final protocol, API, cryptography, key custody, freshness and lifecycle rules, replay and superseding-disposition mechanics, profile-specific selection and Independent Security Review remain pending.

### F.2 Approved bounded logical clause

Authenticated Audit-owned online lookup is the preferred baseline candidate for confirmation recovery and reconciliation.

- Online lookup shall not be a mandatory synchronous dependency of the successful Customer mutation path.
- Customer mutation success establishes the durable Customer-owned publication obligation required by the bounded contract; it does not establish Audit ingestion.
- Audit remains authoritative for durable ingestion truth. A confirmation is valid only after authorized validation and durable Audit-owned ingestion evidence.
- Confirmation shall bind to the complete `ObligationKey`, including `ProducerAuthority`, authoritative `TenantScope` and `ObligationId`, together with the authoritative Audit evidence and supported confirmation version.
- Lookup shall authenticate the requester and authorize the Tenant, operation and requested evidence.
- Reconciliation shall treat a duplicate valid confirmation idempotently and shall reject forged, cross-obligation, cross-producer, cross-Tenant, unsupported, conflicting or superseded evidence.
- Audit outage or delayed confirmation shall not be interpreted as successful ingestion. The obligation remains unresolved and follows later-approved retry, escalation or suspension policy.
- Dedicated Sovereign confirmation lookup, durable ingestion truth and final confirmation authority shall remain local; Central cannot substitute for unavailable local Audit authority.

### F.3 Preferred logical option and rationale

Use **authenticated Audit-owned online lookup outside the successful Customer mutation path** as the preferred baseline candidate.

This model retains Audit as the authoritative source of ingestion truth, permits current authorization and superseding disposition to be evaluated at lookup time, and avoids requiring Customer to validate and retain a self-contained cryptographic proof indefinitely. It remains a proposal and does not establish an availability target or executable failure policy.

### F.4 Alternatives and trade-offs

| Model | Benefit | Limitation | Disposition |
| --- | --- | --- | --- |
| Authenticated Audit-owned online lookup | Fresh authoritative status; current authorization, revocation and superseding disposition visible | Reconciliation depends on Audit lookup availability | **PREFERRED BASELINE CANDIDATE — NOT APPROVED** |
| Independently verifiable confirmation | May permit verification without online Audit lookup | Key lifecycle, revocation, stale evidence and semantic binding are more complex | **PERMISSIBLE — SEPARATE DECISION AND SECURITY REVIEW REQUIRED** |
| Hybrid lookup plus independently verifiable evidence | May improve disconnected recovery flexibility | Adds two verification paths and greater consistency/operations complexity | **PERMISSIBLE — SEPARATE DECISION AND SECURITY REVIEW REQUIRED** |
| Broker ACK or publisher confirm as Audit confirmation | Transport evidence is available early | Does not prove consumer authorization or durable Audit ingestion | **ARCHITECTURALLY PROHIBITED INTERPRETATION** |
| Customer, Messaging or Operations as confirmation authority | May appear operationally convenient | Violates Audit ownership of ingestion truth | **ARCHITECTURALLY PROHIBITED** |
| Synchronous Audit lookup required for successful Customer mutation | Immediate confirmation | Couples Customer mutation success to a separate Domain and contradicts the bounded consistency model | **REJECTED CANDIDATE** |

A signature or integrity mechanism alone does not prove durable Audit ingestion, current authorization, freshness or reconciliation completion.

### F.5 Approval, evidence and review dependencies

| Dimension | Required record |
| --- | --- |
| Recorded Project/Domain authority | **APPROVED WITH AMENDMENTS** by Project, Customer, Audit and Messaging/Operations Owner authority |
| Pending Security authorities | Security Architecture approval; Identity/Platform Security approval; applicable Tenant Security Authority approval |
| Related Open Decisions | `OD-008`, `OD-011`, `OD-012`, `OD-014`, `OD-019`, `OD-020`, `OD-023` |
| Required design evidence | Lookup authorization contract; complete confirmation binding; durable-ingestion commit evidence; duplicate/conflict/superseding semantics; replay-safe reconciliation state model; Audit outage policy; Sovereign-local lookup; if retained, independent-evidence key lifecycle |
| Independent Security Reviewer dependency | Validate authenticity, replay resistance, stale/superseded evidence handling, lookup enumeration controls, key compromise implications and Sovereign-local authority |
| Explicit unresolved implementation details | Verification protocol, confirmation representation, signature or equivalent mechanism, key hierarchy, API, persistence representation, cache/freshness behavior, timeout, retention and numeric availability objectives |

### F.6 Candidate negative tests

All tests remain **NOT_EXECUTED**.

- Existing traceability: `NT-009/011/016`, `TC-AC-008–010/018`, `OPS-AC-007–009`.
- Fabricated confirmation from a non-Audit authority — `NEW_CANDIDATE — NOT REGISTERED`.
- Valid confirmation replayed for another obligation — `NEW_CANDIDATE — NOT REGISTERED`.
- Cross-Tenant or cross-producer confirmation — `NEW_CANDIDATE — NOT REGISTERED`.
- Confirmation issued before durable Audit commit — `NEW_CANDIDATE — NOT REGISTERED`.
- Stale confirmation after a superseding invalid or quarantine disposition — `NEW_CANDIDATE — NOT REGISTERED`.
- Unauthorized lookup or enumeration — `NEW_CANDIDATE — NOT REGISTERED`.
- Audit outage interpreted as successful ingestion — `NEW_CANDIDATE — NOT REGISTERED`.
- Duplicate confirmation causing a second reconciliation effect — `NEW_CANDIDATE — NOT REGISTERED`.
- Central lookup substituted for unavailable Sovereign-local Audit — `NEW_CANDIDATE — NOT REGISTERED`.
- Unsupported confirmation version accepted — `NEW_CANDIDATE — NOT REGISTERED`.

## G. Traceability

| Decision label | Security review scope | DEC principles | Threat, asset, boundary and abuse traceability | Security Requirement candidates |
| --- | --- | --- | --- | --- |
| SD-01 | S1 | V3-003-DEC-009, DEC-012, DEC-014 | `TA-005`, `TA-010`; `AS-015/018`; `TB-013/014/019`; `AB-009`; `NT-009` | `SR-CAND-011/012` |
| SD-02 | S1 with S3 interaction | V3-003-DEC-009, DEC-012, DEC-014 | `TA-005`, `TA-010`; `AS-015/018`; `TB-013/014/019`; `AB-009`; `NT-009` | `SR-CAND-011/012` |
| SD-03 | S2 | V3-003-DEC-012, DEC-014 | `AS-003/016/018`; `TB-005/008/014/019`; `AB-002/007/009`; `NT-002/007/009` | `SR-CAND-003/004/007/008/011/012` |
| SD-04 | S3 | V3-003-DEC-010, DEC-011, DEC-012, DEC-014 | `AS-013/018`; `TB-019`; `AB-009/011/016`; `NT-009/011/016` | `SR-CAND-011–014/019/020` |

Applicable approved architecture and standards remain:

- ADR-V3-003 — Cell-based hybrid multi-tenancy.
- ADR-V3-004 — Locally authoritative Sovereign control.
- ADR-V3-005 — Domain-owned authorization with shared policy governance.
- ADR-V3-007 — Service-owned persistence and reliable messaging.
- ADR-V3-008 — Contract-first controlled compatibility.
- `architecture/standards/security.md`.
- `architecture/standards/messaging.md`.
- `architecture/standards/persistence.md`.

The identifiers in this section are existing traceability references. This document creates no new official threat, test, requirement, DEC or ADR identifier.

## H. Independent Security Reviewer Questions

1. Does the proposed five-layer trust separation prevent transport or workload identity from becoming implicit Producer, contract or Tenant authority?
2. Can every receiving boundary validate original Customer provenance without trusting mutable headers or broker identity?
3. Does the proposed Tenant binding prevent substitution, defaulting and cross-Tenant lookup across publication, ingestion, confirmation and recovery?
4. Does the online-lookup baseline prove Audit-issued durable ingestion for the exact obligation while preventing replay, enumeration and stale-evidence acceptance?
5. Are credential revocation, provenance recovery and confirmation verification locally authoritative in Dedicated Sovereign without unapproved Central substitution?

No answer, finding, limitation or sign-off is recorded on behalf of an Independent Security Reviewer.

## I. Explicit Non-Approvals

This document does not approve:

- A fully approved SEC-01 Security Contract or any scope beyond the recorded bounded Project/Domain dispositions.
- Identity/Platform Security, Tenant Security Authority or Security Architecture approval.
- Independent Security Review findings or sign-off.
- Any new V3-003-DEC, ADR, Security Requirement, threat or test identifier.
- `SR-CAND-001` through `SR-CAND-024`.
- Workload identity technology, identity provider, protocol or credential format.
- mTLS, PKI, SPIFFE/SPIRE, token format, signature algorithm, key hierarchy or secret infrastructure.
- A final provenance envelope, authenticated-metadata or intermediary re-attestation mechanism.
- A final confirmation verification model, lookup API, confirmation schema or cryptographic representation.
- Credential lifetime, revocation delay, freshness, retry, timeout, retention, SLO, RTO, RPO or other numeric NFR.
- Java/RLS integration or any other implementation technology.
- Risk acceptance, mitigation approval or security exception.
- Implementation correctness, runtime security, Negative Test result or Production Readiness.
- Executable DURABLE_DEFER.

## J. Preserved Governance Status

- `PROJECT_AND_DOMAIN_BOUNDED_DISPOSITIONS = APPROVED_WITH_BOUNDARIES_OR_AMENDMENTS`
- `IDENTITY_PLATFORM_SECURITY_APPROVAL = PENDING`
- `TENANT_SECURITY_AUTHORITY_APPROVAL = PENDING`
- `SECURITY_ARCHITECTURE_APPROVAL = PENDING`
- `INDEPENDENT_SECURITY_REVIEW = NOT_SIGNED_OFF`
- `V3-003 = IN PROGRESS`
- `OD-001..OD-023 = OPEN`
- `SR-CAND-001..SR-CAND-024 = PROPOSED — NOT APPROVED`
- `SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF`
- `IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED`
- `NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED`
- `EXECUTABLE_DURABLE_DEFER = NOT APPROVED`

## K. Next Bounded Activity

In a separately authorized activity, the Identity/Platform Security Authority, Tenant Security Authority where applicable, and Security Architecture should review the exact bounded dispositions and record only their own scoped disposition, evidence requests and limitations. Missing authority must not be inferred from the Project/Domain approvals.

After the required Security Authority dispositions and missing design evidence are available, the package may be submitted to an authenticated Independent Security Reviewer. Independent Security Review remains separately required for the trust, provenance, Tenant binding and confirmation-verification properties. No later step may infer technology selection, runtime verification or executable DURABLE_DEFER from the bounded approvals recorded here.
