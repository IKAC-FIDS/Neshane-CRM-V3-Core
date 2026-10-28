# V3-003 Identity/Platform Security Specialist Review Request

## Document Control

| Field | Recorded value |
| --- | --- |
| Task | `V3-003 — NFR and Threat Assumptions` |
| Document status | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |
| Specialist scope | Identity/Platform Security |
| Primary security areas | S1; identity-related aspects of S2, S3 and S8 |
| Identity/Platform Security approval | `PENDING` |
| Security Architecture approval | `PENDING` |
| Independent Security Review | `NOT_SIGNED_OFF` |
| Implementation evidence | `NOT_VERIFIED` |
| Negative-test execution | `NOT_EXECUTED` |
| Executable DURABLE_DEFER | `NOT APPROVED` |

This document is a decision and evidence request for an actual authorized Identity/Platform Security reviewer. It records no specialist opinion, disposition, approval, reviewer identity, approval date, risk acceptance or implementation evidence.

`IP-01` through `IP-05` are local working labels in this review request. They are not official DEC, ADR, OD, SR, threat or test identifiers.

## A. Verified Review Baseline

### A.1 Repository and revision identity

| Field | Verified value |
| --- | --- |
| Repository | `IKAC-FIDS/Neshane-CRM-V3-Core` |
| Branch | `main` |
| Pinned source HEAD | `52518d394c2988d208b7b6a8a5b90cca69e1e7a6` |
| Source commit subject | `docs(architecture): record bounded SEC-05 sovereign security decisions` |
| Local tracking state at preparation | `main...origin/main [ahead 13]` |
| Source worktree/index qualification | Source files are committed and unchanged; the Consolidated Manifest is an untracked working-tree snapshot |
| Remote publication claim | None; no fetch, stage, commit or push performed |

The source HEAD contains the Technical Contract, previous Security Review Input Manifest, SEC-01 through SEC-05 and the V3-003 Decision Record. The Consolidated Manifest was created after that source HEAD and is not contained in it. Its exact bytes are identified separately below. This distinction must be retained in every reviewer response.

### A.2 Pinned review references

| Document | Git blob in source HEAD | SHA-256 | Source status |
| --- | --- | --- | --- |
| `architecture/reviews/V3-003-customer-audit-technical-contract-draft.md` | `60cb1e3043a66e587c7b20428e2c68cdd361007a` | `56e71f3ee0537bfc70d0e3f02602175d0e0eb87510fbb7ab43125f37c4010412` | `DRAFT — CROSS-DOMAIN REVIEW REQUIRED` |
| `architecture/reviews/V3-003-security-review-input-manifest.md` | `f702d1c3296cd28d921c85abee06f98262b536f9` | `a73fc9346361fcd95ca6f4914cff53be7201dcfc35df9a71334d14d442d3ef22` | Prepared; not signed off |
| `architecture/reviews/V3-003-SEC-01-bounded-security-design-decision-sheet.md` | `fe176682b60f7aefa4c34ac656b9d0a76369f1f8` | `0394a08682ed911f5c61839ca371e0852072e5621f9b33ffb0e322fec738ca7b` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-02-bounded-security-design-decision-sheet.md` | `3435f546bdfa2ddb6b6bd4a534f7b72782c435af` | `f0b6d9816324cd6f2c0a1bde239a772a677aba41cb05645379f880d65f7fa645` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-03-bounded-security-design-decision-sheet.md` | `30e962d821eb7e9b0e44ac242e2d6960cc81ca12` | `69c1a5de357438cebd2bfd55da0b110fd476c92ca05d21adf0dae3ff2961c655` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-04-bounded-security-design-decision-sheet.md` | `2c6dd64a13d04844012453f7d3d6a7ecd082d077` | `2d03d1cda36c3e9f379824ed46b2c6affb362b504f098a95f137db2e1349f6e6` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-SEC-05-bounded-security-design-decision-sheet.md` | `c06e57fb1d90c01e604933482c10860d612b9875` | `a7bf6191f252d20a334d9a315e77fedbff6bec689382edbb528e952dcf809a82` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-decision-record.md` | `b2c84da93105d6a91f1b42c3c578fc6878bda899` | `178d447fc642a385c20fecd866de5e87e518944da3f65a005fc6118034000e18` | `V3-003 = IN PROGRESS` |

Consolidated review snapshot:

| Document | Git status | SHA-256 | Status |
| --- | --- | --- | --- |
| `architecture/reviews/V3-003-consolidated-security-design-review-manifest.md` | Not in source HEAD; untracked at preparation | `9592b9e9190d2182132d5eebefbd9fdcb7c802f7f8a8e305b8209db699b90c3e` | `PINNED_FOR_SPECIALIST_REVIEW`; not remotely published |

### A.3 Applicable authority and architecture baseline

- Existing Project/Domain bounded dispositions remain exactly as recorded: six Customer, four Audit, five Messaging/Operations and the bounded SEC-01 through SEC-05 dispositions.
- ADR-V3-004 preserves locally final Sovereign security and operational authority.
- ADR-V3-005 preserves Domain-owned resource/action authorization and rejects identity-equals-permission.
- ADR-V3-007 preserves service-owned persistence, validated Tenant Context, RLS and reliable messaging.
- ADR-V3-008 preserves explicit versioned contract compatibility.
- ADR-V3-010 requires profile-specific operational evidence.
- ADR-V3-012 separates documentation, implementation evidence and Production Readiness.
- `architecture/standards/security.md` requires workload authentication at each trust boundary, issuer/audience/expiry validation under an approved design, least privilege and fail-closed Tenant handling.
- `architecture/standards/messaging.md` requires validated producer/Tenant provenance without trusting arbitrary message headers.

No Identity/Platform Security Owner authority, Security Architecture authority or Independent Security Reviewer authority is claimed in this request.

## B. Specialist Authority and Scope

### B.1 In scope

- Logical trust-layer separation and workload identity validation.
- Server-controlled mapping from authenticated workload identity to `ProducerAuthority`.
- Issuer, audience, validity, revocation and delegation security properties.
- Identity-related Tenant authority and multi-tenant workload constraints.
- Original producer provenance through messaging, retry and re-drive.
- Authentication and authorization properties of Audit-owned confirmation exchange.
- Workload credential lifecycle, compromise containment and recovery.
- Dedicated Sovereign local validation, revocation and reconnect trust.

### B.2 Authority limitations

The requested reviewer may issue only a disposition within verified Identity/Platform Security authority. The review does not grant authority to decide:

- Resource-specific Customer or Audit business authorization.
- Tenant Security, RLS or database integration outside identity-related requirements.
- Final Security Architecture sufficiency or Independent Security Review sign-off.
- Contract field semantics or Messaging/API Event Architecture approval.
- Operational Policy, privileged action execution or Eligibility Policy Authority assignment.
- Final product, protocol, credential, cryptographic or infrastructure technology selection unless separately authorized.

### B.3 Current specialist status

```text
IDENTITY_PLATFORM_SECURITY_APPROVAL = PENDING
AUTHORIZED_REVIEWER_IDENTITY = UNFILLED
AUTHORIZED_REVIEWER_SCOPE = UNFILLED
SPECIALIST_DISPOSITIONS_IP_01_TO_IP_05 = UNFILLED
```

## C. Identity Trust Boundary Matrix

| Trust boundary | Authenticated principal | Authority source | Required validation | Tenant scope | Required evidence | Failure behavior | Outstanding decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Customer Publisher → Messaging | Customer publication workload | Server-controlled workload-to-authority mapping | Issuer/trust domain, audience, validity, revocation, producer and contract authority | Explicit operation-scoped `TenantScope` | Authentication result, mapping version, authority scope, correlation | Fail closed; no valid publication authority established | Credential model and mapping governance |
| Messaging → Audit Consumer | Broker peer for transport; original Customer producer for provenance | Peer authentication plus receiver-verifiable original producer evidence | Keep broker identity separate from `ProducerAuthority`; validate producer, contract/version and Tenant | Exact authoritative Tenant | Original provenance, delivery identity, immutable obligation binding | Reject or quarantine without successful confirmation | Provenance mechanism and chain of custody |
| Direct Customer Consumer Path → Audit | Authenticated Customer workload | Approved producer/contract authority mapping | Producer, contract, audience and Tenant independently validated by Audit | Exact authoritative Tenant | Workload evidence and original obligation provenance | Fail closed before Audit Domain or persistence effect | Direct-consumer trust contract |
| Retry/Re-drive → Messaging | Authorized recovery workload or operator | Recovery Execution Authority plus original producer evidence | Execution identity, action authorization, affected scope and immutable original provenance | Explicit affected Tenant/Platform scope | Authorization reference, full `ObligationKey`, reason, correlation, attempt identity | Deny unauthorized scope; never replace original producer | Privileged identity and delegation policy |
| Customer Reconciliation → Audit Lookup | Customer reconciliation workload or authorized recovery actor | Audit resource/action authorization | Requester authentication, audience, purpose, Tenant and lookup scope | Full `ProducerAuthority + TenantScope + ObligationId` | Lookup request, authorization decision, correlation and Audit response reference | Deny without disclosing unauthorized status or existence | Lookup authorization contract |
| Audit → Confirmation Consumer | Audit-owned workload and Audit confirmation authority | Audit Domain | Audit identity, confirmation contract/version and durable-ingestion binding | Exact Tenant and obligation | Audit authority, full `ObligationKey`, durable evidence reference and disposition | Reject forged, stale, mismatched or unsupported evidence | Final confirmation trust model |
| Central Federation → Sovereign | Central federation identity | Locally approved federation mapping | Mutual authentication, local scope/purpose approval, validity and revocation | Explicit local Tenant/Profile scope | Local approval and federation provenance | Reject Central assertion without local authority | Federation trust policy |
| Sovereign Issuer/Validator → Local Workload | Locally issued or locally validated workload identity | Sovereign-local trust authority | Local trust, audience, validity, revocation and applicable authority mapping | Local operation scope | Local trust state and mapping evidence | Missing or indeterminate local trust fails closed | Local issuer and custody design |
| Reconnection after Local Rotation/Revocation | Federated peer under local validation | Locally authoritative trust anchors and reconciliation policy | Preserve local revocation and rotation state; prevent stale trust reactivation | Tenant/Profile constrained | Local and remote trust versions, provenance and conflict record | Preserve conflict; no automatic Central overwrite | Reconnect trust governance |

Mandatory logical boundaries submitted for review:

1. Transport peer identity is not workload, producer, contract or Tenant authority.
2. Authenticated workload identity does not independently establish `ProducerAuthority`.
3. `ProducerAuthority` derives only from a server-controlled mapping.
4. Contract/Event Authority and operation-scoped Tenant Authority remain independently validated.
5. Multi-tenant workload identity grants no universal Tenant authorization.
6. Missing, expired, revoked, indeterminate or conflicting evidence fails closed before Domain or persistence work.

## D. Producer Provenance Alternatives

The required invariant is receiver-verifiable original Customer producer provenance across publication, broker mediation, direct consumption, retry and re-drive. A mutable header, broker connection or operator identity cannot independently establish `ProducerAuthority`.

Minimum logical binding under review:

```text
Original ProducerAuthority
Authoritative TenantScope
ContractType
ContractVersion
SemanticContentVersion
ObligationId
Required Correlation/Causation Evidence
Provenance Version
```

This is a conceptual binding list, not an approved schema or wire format.

| Candidate | Security benefit | Attack surface / trust assumption | Required dependency | Current treatment |
| --- | --- | --- | --- | --- |
| Receiver-verifiable trusted provenance envelope | Preserves producer authority across transport, retry, re-drive and direct consumers | Key compromise, replay, downgrade, incorrect field/version binding | Identity lifecycle, Contract Governance, Messaging/API Event Architecture and Security Architecture | Preferred logical candidate; not final |
| Authenticated metadata propagation | May reduce envelope duplication on controlled paths | Every hop must preserve and authenticate origin; intermediary mutation and header confusion risks | Explicit hop validation and end-to-end provenance rules | Conditional alternative |
| Explicitly authorized intermediary re-attestation | Supports permitted mediation or approved transformation | Authority escalation, broken chain of custody and ambiguous transformation | Explicit intermediary authority, original producer retention and transformation evidence | Conditional alternative |
| Broker connection identity as original producer | Operationally simple | Shared broker/publisher identity replaces Domain provenance | None sufficient | Rejected; cannot establish original producer |
| Mutable producer/Tenant headers as authority | Easy to carry | Spoofing and cross-Tenant substitution | None sufficient | Architecturally prohibited as authority |
| Re-drive identity replacing original producer | Simple operational attribution | Destroys origin and enables privilege escalation | None sufficient | Rejected |

Reviewer assessment is requested on forgery resistance, confused-deputy resistance, downgrade/replay handling, intermediary trust, direct-consumer validation and credential compromise impact. No signing, hash, key or encoding technology is selected.

## E. Audit Confirmation Trust Alternatives

Only Audit Domain owns authoritative durable-ingestion truth. Broker acknowledgement, publisher confirmation, monitoring state, Customer evidence or Operations state cannot manufacture Audit ingestion confirmation.

| Property | Authenticated Audit-owned online lookup | Independently verifiable receipt | Hybrid lookup plus receipt |
| --- | --- | --- | --- |
| Requester authentication | Evaluated at lookup | Evaluated when obtaining and later verifying receipt | Required on both paths |
| Current authorization | Can evaluate current Tenant, purpose and operation authority | Receipt may outlive requester authority unless separately constrained | Lookup can supplement but creates two decision paths |
| Exact binding | Full `ObligationKey`, Audit authority and durable evidence | Same binding must be inside verifiable evidence | Both representations must remain semantically consistent |
| Freshness | Current Audit disposition can be returned | Requires explicit freshness/revocation/supersession model | Two freshness rules must agree |
| Replay resistance | Request/response and reconciliation state must be replay-safe | Receipt must not be reusable for another obligation or state | Replay resistance required twice |
| Superseding invalid/quarantine state | Current state can be observed | Prior receipt may become stale unless supersession is represented | Conflict/reconciliation policy required |
| Audit outage | Outcome remains unresolved; no success fabricated | Prior receipt may remain verifiable, but current validity may be indeterminate | Degraded behavior requires explicit policy |
| Dedicated Sovereign | Local Audit lookup and local authorization | Locally verifiable evidence and local key lifecycle | Both paths remain locally authoritative |
| Main risk | Availability dependency during recovery/reconciliation | Key lifecycle, stale proof and revocation complexity | Increased ambiguity and operational complexity |

Authenticated Audit-owned online lookup remains a preferred design candidate for recovery and reconciliation. It is not an approved final protocol and is not a mandatory synchronous dependency in the successful Customer mutation path.

The reviewer must explicitly assess:

- Authentication and authorization of the lookup requester.
- Complete `ObligationKey`, Audit authority and durable-evidence binding.
- Replay, cross-obligation and cross-Tenant resistance.
- Freshness and behavior after a superseding invalid or quarantine disposition.
- Audit outage and delayed confirmation without fabricated success.
- Sovereign-local Audit authority without Central substitution.

## F. Credential Lifecycle and Sovereign-local Trust Matrix

| Lifecycle stage | Minimum security property | Required evidence | Failure or incident behavior | Pending specialist choice |
| --- | --- | --- | --- | --- |
| Issuance | Identity and authority assignment remain distinct and explicitly authorized | Issuer, subject, purpose, requested scope and authorization provenance | Unauthorized issuance rejected and made traceable | Issuer/trust-domain model |
| Activation | Credential cannot authorize use before controlled activation | Activation state and effective scope | Fail closed before activation | Activation mechanism |
| Validation | Issuer/trust, audience, validity, revocation and required authority checked at each receiving boundary | Validation result and trust-policy version | Invalid or indeterminate evidence rejected | Evidence format and validation contract |
| Expiration | Expired credential creates no authority | Validity interval and validation result | Fail closed | Lifetime policy; no number approved |
| Rotation | Old/new overlap is controlled and bounded without scope expansion | Rotation event, activation and retirement state | Ambiguous overlap cannot broaden authority | Overlap and rollout model |
| Revocation | Revocation has enforceable semantics at every required boundary | Revocation source, authority, effective semantics and propagation evidence | Stale acceptance prohibited; exact delay unresolved | Enforcement and disconnected behavior |
| Compromise containment | Affected credentials, mappings and trust paths are bounded and recoverable | Incident, affected authority map, suspension/revocation and recovery evidence | Suspend/escalate affected paths; no silent fallback | Blast radius and incident integration |
| Retirement | Retired credential and mapping cannot be reused | Retirement and residual-access evidence | Reuse rejected | Retention and cleanup policy |
| Trust-anchor change | Anchor lifecycle is independently authorized and traceable | Old/new anchors, approvals, activation and retirement evidence | Unknown or conflicting chain rejected | Custody and transition model |
| Authority recovery | Restored trust is validated before use | Recovery provenance and restored-state verification | No activation from unverified backup/state | Recovery evidence and authority |
| Central-assisted provisioning | Assistance cannot become final local authority | Local approval, locally validated issuance or mapping | Central assertion alone rejected | Federation/provisioning contract |
| Sovereign disconnection | Local validation and revocation remain final | Local trust, revocation and continuity evidence | Missing local authority fails closed for affected operation | Local issuer and continuity model |
| Reconnection | Local revocation/rotation cannot be silently reversed | Local/remote trust versions and conflict record | Preserve conflict; no automatic stale-trust restoration | Reconciliation policy |

No PKI, KMS/HSM, IdP, secret manager, credential format, key hierarchy, lifetime, rotation interval or cryptographic mechanism is selected.

## G. IP-01 through IP-05 Specialist Decision Requests

Each entry has status:

`PROPOSED — IDENTITY/PLATFORM SECURITY AUTHORITY REVIEW REQUIRED`

Analyst recommendations are explicitly non-authoritative and do not select a reviewer disposition.

### G.1 IP-01 — Workload Identity Trust Model

**Proposed security invariant**

Transport peer identity, authenticated workload identity, server-controlled `ProducerAuthority`, Contract/Event Authority and operation-scoped Tenant Authority remain logically separate and are independently validated at every receiving trust boundary.

**Preferred logical direction**

A technology-neutral layered trust contract with server-controlled mappings and revocation-capable credentials.

**Alternatives for comparison**

- PKI/mTLS-oriented peer identity plus separate authority evidence.
- Signed workload assertion/token model.
- SPIFFE/SPIRE-like workload identity model.
- Hybrid channel and authority evidence.

No alternative is preselected.

**Threats addressed**

`AB-001`, `AB-004`, `AB-009`, `AB-019`; related `NT-001`, `NT-004`, `NT-009`, `NT-019`.

**Required evidence**

Trust-domain model; identity-to-`ProducerAuthority` mapping; audience/contract authority matrix; operation/Tenant authority model; issuance/rotation/revocation lifecycle; profile-specific custody and compromise response.

**Pending cross-specialist decisions**

Tenant Security delegation and Tenant provenance; Security Architecture sufficiency; Sovereign custody; OD-011 and OD-012.

**Exact reviewer questions**

1. Does the five-layer separation prevent transport or workload identity from becoming implicit Producer, contract or Tenant authority?
2. What minimum issuer, audience, validity, revocation and delegation properties are mandatory?
3. What evidence must each receiving boundary validate independently?

**NON-AUTHORITATIVE analyst recommendation**

Consider `APPROVE_WITH_BOUNDARIES` for the logical separation only. Keep technology, credential format, issuer topology, lifecycle timing and runtime verification pending.

### G.2 IP-02 — Producer Provenance Validation

**Proposed security invariant**

Original Customer producer provenance remains receiver-verifiable through brokers, direct consumption, retry and authorized re-drive. Broker identity, operator identity and mutable headers cannot independently establish `ProducerAuthority`.

**Preferred logical direction**

A receiver-verifiable trusted provenance envelope as the preferred logical candidate, without approving a wire format or cryptographic implementation.

**Alternatives for comparison**

Authenticated metadata propagation and explicitly authorized intermediary re-attestation with preserved origin and transformation evidence.

**Threats addressed**

`AB-004`, `AB-009`, `AB-011`; related `NT-004`, `NT-009`, `NT-011`.

**Required evidence**

Canonical provenance concerns; origin/contract/Tenant binding; chain of custody; version/downgrade behavior; direct-consumer validation; retry/re-drive preservation; safe rejection evidence.

**Pending cross-specialist decisions**

Contract Governance field semantics; Messaging/API Event Architecture envelope/version rules; Security Architecture integrity mechanism; Sovereign trust custody.

**Exact reviewer questions**

1. Can Audit prove original Customer producer authority without trusting broker identity or mutable headers?
2. Under what explicit authority may an intermediary re-attest, and what origin/transformation evidence must remain visible?
3. How must credential revocation or compromise affect provenance validation and historical evidence?

**NON-AUTHORITATIVE analyst recommendation**

Consider `APPROVE_WITH_BOUNDARIES` for receiver-verifiable original provenance. Keep format, signature or equivalent mechanism, key custody and contract schema pending.

### G.3 IP-03 — Audit Confirmation Trust

**Proposed security invariant**

Only Audit Domain may establish authoritative durable-ingestion confirmation. Confirmation binds the full `ObligationKey`, Audit authority and durable Audit-owned evidence and cannot be created from transport, publication or monitoring signals.

**Preferred logical direction**

Authenticated Audit-owned online lookup outside the successful Customer mutation path as the preferred recovery/reconciliation candidate.

**Alternatives for comparison**

Independently verifiable receipt and a separately approved hybrid model.

**Threats addressed**

`AB-009`, `AB-011`, `AB-016`; related `NT-009`, `NT-011`, `NT-016`.

**Required evidence**

Requester authentication and purpose authorization; full binding; durable-ingestion commit evidence; replay/freshness rules; duplicate/conflict/superseding semantics; outage behavior; Sovereign-local lookup and authority.

**Pending cross-specialist decisions**

Audit Domain lookup contract; Tenant Security authorization; Contract Governance compatibility; Security Architecture authenticity; Sovereign Security local trust.

**Exact reviewer questions**

1. What proves that confirmation was issued by Audit authority after durable Audit commit for the exact obligation?
2. How must stale confirmation behave after a superseding invalid, conflict or quarantine disposition?
3. Can a receipt remain valid after requester revocation, Audit key rotation or confirmation-contract upgrade?
4. How must Audit outage be represented without manufacturing success?

**NON-AUTHORITATIVE analyst recommendation**

Consider `APPROVE_WITH_AMENDMENTS` only for the preferred online-lookup direction. Keep final protocol, receipt/hybrid selection, cryptography, freshness and lifecycle pending.

### G.4 IP-04 — Credential Lifecycle and Revocation

**Proposed security invariant**

Workload credentials and their authority mappings have controlled issuance, activation, validity, expiration, rotation, revocation, compromise containment, retirement, trust-anchor change and recovery semantics.

**Preferred logical direction**

A profile-aware, locally enforceable and revocation-capable lifecycle in which provisioning assistance cannot replace receiving-boundary validation or local final authority.

**Alternatives for comparison**

Short-lived credentials, online revocation, local revocation state or hybrid approaches. No specific model is selected.

**Threats addressed**

`AB-001`, `AB-004`, `AB-009`, `AB-020`; related `NT-001`, `NT-004`, `NT-009`, `NT-020`.

**Required evidence**

Identity-to-authority mapping lifecycle; validity and rotation state; revocation enforcement boundaries; compromise blast radius; recovery provenance; disconnected behavior; audit trail for lifecycle operations.

**Pending cross-specialist decisions**

Security Architecture trust mechanisms; Operational Policy incident handling; Sovereign Security custody; OD-011, OD-012, OD-015 and OD-023.

**Exact reviewer questions**

1. At which boundaries and under what semantics must revocation be enforced?
2. What overlap behavior during rotation avoids both outage and privilege extension?
3. How is a compromised workload-to-authority mapping contained and recovered?
4. What locally available evidence is required during Central disconnection?

**NON-AUTHORITATIVE analyst recommendation**

Consider `APPROVE_WITH_BOUNDARIES` for the lifecycle stages and fail-closed requirement. Keep lifetime, rotation intervals, revocation delay and mechanism pending.

### G.5 IP-05 — Sovereign-local Identity Validation

**Proposed security invariant**

Dedicated Sovereign retains locally final workload identity validation, authority mapping and revocation effect without mandatory synchronous Central dependency. Central identity or provisioning creates no implicit local administration.

**Preferred logical direction**

A locally authoritative trust domain with optional, locally approved and policy-controlled federation or provisioning assistance.

**Alternatives for comparison**

Fully local issuance, federated trust and Central-assisted provisioning with local final validation. Full Air-Gap is not approved.

**Threats addressed**

`AB-019`, `AB-020`; related `NT-019`, `NT-020`.

**Required evidence**

Local issuer/validator and custody model; revocation and compromise behavior; Central-denial evidence; local authority recovery; reconnect reconciliation; trust-version conflict handling.

**Pending cross-specialist decisions**

Sovereign-specific Security, Tenant Security, Security Architecture, Operational Policy; OD-001, OD-011, OD-012, OD-015 and OD-023.

**Exact reviewer questions**

1. Which identity, validation and revocation authorities must remain completely local?
2. How does loss of local trust authority fail closed without unauthorized Central substitution?
3. How are local revocation and key rotation protected from stale Central information during reconnection?
4. What parts of Central-assisted provisioning are permissible without transferring final authority?

**NON-AUTHORITATIVE analyst recommendation**

Consider `APPROVE_WITH_BOUNDARIES` for local final validation and Central non-authority. Keep issuer architecture, custody, recovery, continuity and Full Air-Gap decisions pending.

## H. Threat and Negative-Test Traceability

All tests remain `NOT_EXECUTED`. A `NEW_CANDIDATE — NOT REGISTERED` entry is not an official or approved test identifier.

| Scenario | Existing traceability | Candidate expected denial/evidence | Gap status |
| --- | --- | --- | --- |
| Forged `ProducerAuthority` | `AB-009`, `NT-009`, `SR-CAND-011/012` | Receiver rejects producer authority; no Audit success | Design and runtime evidence missing |
| Broker identity substituted for Customer producer | `AB-009`, `NT-009` family | Transport identity cannot establish original producer | `NEW_CANDIDATE — NOT REGISTERED` variant |
| Mutable producer/Tenant header spoofing | `AB-002/009`, `NT-002/009` | Header remains selector/metadata only; fail closed | `NEW_CANDIDATE — NOT REGISTERED` variant |
| Replayed obligation with invalid producer provenance | `AB-009/011`, `NT-009/011`, `SR-CAND-011–014` | No duplicate business/Audit effect or confirmation | Replay/provenance design incomplete |
| Cross-Tenant workload authorization attempt | `AB-002/007/009`, `NT-002/007/009`, `SR-CAND-003/004/007/008/011/012` | Operation-scoped Tenant authority required; deny mismatch | Delegation and runtime evidence missing |
| Stale or revoked credential use | `AB-001`, `NT-001`, `SR-CAND-001/002` | Revoked/expired evidence rejected | Revocation semantics missing |
| Wrong issuer or audience | `AB-001/004`, `NT-001/004` family | Boundary validation rejects credential | Exact variants unregistered |
| Unauthorized intermediary re-attestation | `AB-004/009`, `NT-004/009` | Re-attestation rejected; origin preserved | `NEW_CANDIDATE — NOT REGISTERED` |
| Forged Audit confirmation | `AB-009/016`, `NT-009/016`, `SR-CAND-011–014/019/020` | No reconciliation completion or success | Confirmation mechanism missing |
| Cross-Tenant confirmation lookup | `NT-002/007/009` family | Deny without cross-Tenant disclosure | `NEW_CANDIDATE — NOT REGISTERED` |
| Replayed confirmation | `AB-011/016`, `NT-011/016` | Replay cannot complete another obligation/effect | `NEW_CANDIDATE — NOT REGISTERED` |
| Stale confirmation after invalid/quarantine disposition | `AB-016`, `NT-016` family | Current superseding disposition prevents success | `NEW_CANDIDATE — NOT REGISTERED` |
| Central identity substituted for Sovereign-local issuer | `AB-019`, `NT-019`, `SR-CAND-021/022` | Local validation rejects implicit Central authority | Sovereign evidence missing |
| Local issuer/trust-authority outage | `AB-020`, `NT-020`, `SR-CAND-023/024` | Affected operation fails closed; Central not substituted | Continuity policy missing |
| Compromised workload credential | `AB-001/004/009`, `NT-001/004/009` | Scope containment, revocation and traceable recovery | Incident lifecycle missing |
| Reconnection using revoked trust | `AB-019/020`, `NT-019/020` | Stale trust not restored; conflict preserved | `NEW_CANDIDATE — NOT REGISTERED` |

## I. Evidence Requests and Blocking Dependencies

### I.1 Design evidence requested from Identity/Platform Security

1. Workload trust-domain and issuer-boundary model.
2. Authenticated workload identity to `ProducerAuthority` mapping rules and lifecycle.
3. Audience, contract authority and operation-scoped Tenant authority matrix.
4. Credential issuance, activation, rotation, revocation, compromise and retirement model.
5. Service-to-service delegation constraints and evidence.
6. Receiver-verifiable original producer provenance requirements.
7. Authorized intermediary re-attestation constraints, if permitted.
8. Audit confirmation requester and Audit responder authentication requirements.
9. Confirmation replay, freshness and superseding-disposition security properties.
10. Dedicated Sovereign local issuer/validator, revocation and recovery constraints.
11. Central-assisted provisioning and federation limits.
12. Reconnection behavior after local rotation, revocation or compromise.

### I.2 Implementation/runtime evidence not currently available

- No credential or identity implementation exists as verified evidence for this review.
- No issuer/audience/revocation runtime behavior has been verified.
- No workload-to-authority mapping implementation has been verified.
- No producer provenance or confirmation authenticity control has been verified.
- No Shared SaaS, Dedicated Managed or Dedicated Sovereign execution evidence exists.
- No listed negative test has been executed.

### I.3 Blocking dependencies

- `OD-011`: workload identity model remains Open.
- `OD-012`: secrets, keys and custody model remains Open.
- `OD-014`: Java/RLS Tenant-context integration remains Open for runtime evidence.
- `OD-015`: profile runtime/orchestration remains Open.
- `OD-020`: contract-testing approach remains Open.
- `OD-023`: numeric identity/revocation/availability/recovery targets remain Open.
- Security Architecture, Tenant Security, Sovereign Security, Contract Governance, Messaging/API Event Architecture and Operational Policy dispositions remain Pending.

## J. Cross-specialist Handoffs

| Specialist authority | May review independently now | Requires Identity/Platform Security disposition or evidence |
| --- | --- | --- |
| Tenant Security | Fail-closed Tenant rules, RLS/non-bypass expectations and cross-Tenant denial | Identity-to-Tenant authority mapping, multi-tenant delegation and credential scope |
| Security Architecture | Layer separation, prohibited trust shortcuts and threat coverage | Required trust properties, revocation, provenance and confirmation directions |
| Sovereign-specific Security | Local final authority, Central non-authority and local-fact preservation | Local issuer/validator, trust-anchor lifecycle, revocation and compromise recovery |
| Contract Governance | Semantic fields, versioning, coexistence and compatibility | Authenticated provenance and confirmation identity/binding requirements |
| Messaging/API Event Architecture | Producer ownership, delivery, retry/re-drive and envelope evolution | Workload-to-producer mapping and receiver validation properties |
| Operational Policy Governance | Privileged identity separation, incident workflow and recovery execution | Credential incident, emergency identity, revocation and authority-recovery constraints |
| Audit Domain | Audit-owned confirmation and lookup resource semantics | Audit responder identity and requester authentication requirements |
| Customer Domain | Producer-owned obligation and original provenance facts | Customer publisher identity and `ProducerAuthority` mapping requirements |

No handoff transfers approval authority between specialists.

## K. Reviewer Disposition Template

The fields below are intentionally unfilled. They may be completed only from actual authenticated Identity/Platform Security reviewer input.

### K.1 Reviewer provenance

| Reviewer field | Reviewer response |
| --- | --- |
| Authorized reviewer identity | |
| Authenticated reviewer reference | |
| Verified authority and scope | |
| Independence/role limitation statement | |
| Reviewed source HEAD | |
| Reviewed Consolidated Manifest SHA-256 | |
| Reviewed request SHA-256 or immutable reference | |
| Review date, if supplied | |
| General review limitations | |

### K.2 Per-decision response — repeat for IP-01 through IP-05

| Reviewer field | Reviewer response |
| --- | --- |
| Local working decision label | |
| Disposition: `APPROVE_WITH_BOUNDARIES / AMEND / REJECT / BLOCKED / EVIDENCE_REQUIRED` | |
| Exact approved or rejected scope | |
| Required amendments | |
| Required design evidence | |
| Required implementation/runtime evidence | |
| Dependencies and limitations | |
| Related threat/test observations | |
| Review record reference | |

No disposition is selected in advance. The analyst recommendations in section G are non-authoritative and are not reviewer findings.

## L. Explicit Non-Approvals and Governance Status

This request does not approve:

- IP-01 through IP-05 as official decisions or approved specialist dispositions.
- Identity/Platform Security, Tenant Security, Sovereign-specific Security or Security Architecture approval.
- Independent Security Review findings or sign-off.
- Workload identity protocol, IdP, mTLS, PKI, SPIFFE/SPIRE, OAuth/token format or credential product.
- Signature, hashing, cryptographic algorithm, KMS/HSM, secret manager, key hierarchy or custody implementation.
- A final provenance envelope, authenticated metadata, intermediary re-attestation or confirmation protocol.
- Credential lifetime, rotation interval, revocation delay, freshness, timeout, retention or numeric NFR.
- A final Tenant delegation, RLS, contract or Operational Policy design.
- Any `SR-CAND-001` through `SR-CAND-024` as a final Security Requirement.
- A PASS/FAIL result for any Negative Test, `TC-AC-*` or `OPS-AC-*` candidate.
- Risk rating, risk acceptance, mitigation approval or security exception.
- Implementation authorization, runtime-security evidence or Production Readiness.
- Executable or unconditional `DURABLE_DEFER`.
- Eligibility Policy Authority assignment or restoration execution authority.
- Closure of V3-003 or any Open Decision.

Preserved status:

```text
V3-003 = IN PROGRESS
OD-001..OD-023 = OPEN
SR-CAND-001..SR-CAND-024 = PROPOSED — NOT APPROVED
IDENTITY_PLATFORM_SECURITY_APPROVAL = PENDING
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

The next bounded activity is delivery of this exact request to an authenticated Identity/Platform Security authority. Any returned disposition must identify reviewer authority, reviewed baseline, exact scope, limitations and evidence requests. No response may be inferred from silence or from the analyst recommendations recorded here.
