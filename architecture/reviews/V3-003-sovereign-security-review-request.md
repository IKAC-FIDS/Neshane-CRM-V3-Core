# V3-003 Sovereign-specific Security Specialist Review Request

## Document Control

| Field | Recorded value |
| --- | --- |
| Task | `V3-003 — NFR and Threat Assumptions` |
| Target deployment profile | Dedicated Sovereign |
| Document status | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |
| Sovereign Security Authority approval | `PENDING` |
| Identity/Platform Security approval | `PENDING` |
| Tenant Security Authority approval | `PENDING` |
| Security Architecture approval | `PENDING` |
| Operational Policy approval | `PENDING` |
| Independent Security Review | `NOT_SIGNED_OFF` |
| Implementation evidence | `NOT_VERIFIED` |
| Negative-test execution | `NOT_EXECUTED` |
| Executable DURABLE_DEFER | `NOT APPROVED` |

This document requests review by an actual authorized Sovereign-specific Security reviewer. It records no reviewer opinion, approval, identity, signature, review date, risk acceptance, implementation evidence or test result.

`SS-01` through `SS-05` are local working labels in this request. They are not official DEC, ADR, OD, SR, threat or test identifiers.

## A. Verified Baseline and Document Control

### A.1 Repository and revision identity

| Field | Verified value |
| --- | --- |
| Repository | `IKAC-FIDS/Neshane-CRM-V3-Core` |
| Branch | `main` |
| Preparation HEAD | `4c4488f7f1bc852fc19397beb48429f78cbca550` |
| HEAD subject | `docs(security): prepare contract and messaging specialist review request` |
| Local tracking state before creation | `main...origin/main [ahead 17]` |
| Worktree and index before creation | Clean |
| Target document in preparation HEAD | No |
| Remote publication claim | None; no fetch, stage, commit or push performed |

The HEAD change since the preceding analysis is documentation-only and records the Contract/Messaging Specialist Review Request. Exact pinned source bytes remain unchanged. This request is working-tree content until separately committed; the preparation HEAD must not be represented as containing it.

### A.2 Exact review references

| Document | Git status in preparation HEAD | SHA-256 | Recorded status |
| --- | --- | --- | --- |
| `architecture/reviews/V3-003-consolidated-security-design-review-manifest.md` | Tracked and committed | `9592b9e9190d2182132d5eebefbd9fdcb7c802f7f8a8e305b8209db699b90c3e` | `PINNED_FOR_SPECIALIST_REVIEW` |
| `architecture/reviews/V3-003-contract-messaging-specialist-review-request.md` | Tracked and committed | `c3e5943bc2063d4c7067ca41bed4fcb8f031525ffbed14c0a1e2251db86bf48a` | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWERS` |
| `architecture/reviews/V3-003-SEC-05-bounded-security-design-decision-sheet.md` | Tracked and committed | `a7bf6191f252d20a334d9a315e77fedbff6bec689382edbb528e952dcf809a82` | `DRAFT — SECURITY REVIEW REQUIRED` |
| `architecture/reviews/V3-003-customer-audit-technical-contract-draft.md` | Tracked and committed | `56e71f3ee0537bfc70d0e3f02602175d0e0eb87510fbb7ab43125f37c4010412` | `DRAFT — CROSS-DOMAIN REVIEW REQUIRED` |
| `architecture/reviews/V3-003-identity-platform-security-review-request.md` | Tracked and committed | `99f64d857ee22b3090bf9ad07fc270c903dab0c620190fba7ac3590c8631cc1e` | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |
| `architecture/reviews/V3-003-tenant-security-review-request.md` | Tracked and committed | `b2364c4d4469209e48e28e8a3f59d3f794337c194a79b18b4a7bece7976a0701` | `SPECIALIST_REVIEW_REQUEST — PENDING AUTHORIZED REVIEWER` |

### A.3 Applicable authority baseline

- ADR-V3-003 preserves stable Tenant identity across Shared SaaS, Dedicated Managed and Dedicated Sovereign.
- ADR-V3-004 establishes a locally authoritative Sovereign Control Plane with final local security and operational authority; Central identities have no implicit local administrative rights.
- ADR-V3-010 requires independent profile-specific evidence for trust, secrets, recovery, observability, audit, upgrade and rollback.
- ADR-V3-005 preserves Domain-owned resource/action authorization.
- ADR-V3-007 preserves service-owned persistence, validated Tenant Context and reliable messaging boundaries.
- ADR-V3-008 preserves explicit versioned contract compatibility.
- ADR-V3-012 separates architecture documentation from implementation and Production Readiness evidence.
- DEC-009 through DEC-014 remain bounded Owner decisions and do not approve final protocols, policies, technologies or executable DURABLE_DEFER.
- `TA-012`, `TS-003`, `AS-019`, `AS-020`, `TB-016`, `AB-019`, `AB-020`, `NT-019`, `NT-020` and `SR-CAND-021..024` are the primary verified Sovereign traceability identifiers.

Existing Project, Customer, Audit and Messaging/Operations Owner authority does not establish Sovereign-specific Security Authority.

## B. Sovereign-specific Security Authority and Scope

### B.1 Requested review scope

- S8 Sovereign-local trust and federation.
- Local producer identity and provenance aspects of S1.
- Local Tenant authority aspects of S2.
- Local Audit confirmation authenticity aspects of S3.
- Privileged recovery authorization aspects of S4.
- Monitoring, eligibility and recovery evidence aspects of S7.
- Contract compatibility and quarantine dependencies from S5 and S6.

### B.2 Authority limitations

The requested reviewer may issue dispositions only within verified Sovereign-specific Security authority. This request does not assign authority over Customer or Audit business facts, final Identity/Platform design, Tenant Security, Contract Governance, Messaging/API Event Architecture, Operational Policy, Eligibility Policy, implementation technology, numeric service objectives or Independent Security Review.

### B.3 Core boundary

Central identity, availability, configuration or administrative assertion does not independently grant local authority. Conversely, Central disconnection alone does not invalidate otherwise valid local authority. Missing, invalid, revoked, conflicting or indeterminate local authority fails closed for the affected operation; Central availability does not automatically compensate for it.

## C. Sovereign-local Trust Authority Matrix

| Actor/authority | Candidate locally owned decision or fact | Permitted effect | Forbidden substitution | Required evidence |
| --- | --- | --- | --- | --- |
| Local Identity Authority | Principal identity, authenticator and authentication/session validity | Authenticate and enforce local revocation | Central identity alone creates local Principal/access | Local issuer/trust, audience, validity and revocation state |
| Local Workload Trust Authority | Workload identity, credential state and server-controlled authority mapping | Establish applicable workload and producer authority | Network location, header or arbitrary Central assertion creates `ProducerAuthority` | Credential state, workload mapping, purpose and scope |
| Local Tenant Authority | Tenant association and authoritative Tenant Context | Validate operation-scoped Tenant authority | Central Tenant claim accepted without local validation | Local association, Context and action scope |
| Local Customer Domain | Customer mutation, obligation and producer recovery truth | Authorize and reproduce Customer-owned evidence | Declare Audit ingestion or alter Audit-owned truth | Domain authorization, Tenant Context and durable obligation |
| Local Audit Evidence Authority | Audit ingestion, confirmation, conflict and disposition truth | Authoritative local lookup/reconciliation evidence | Central confirmation or broker acknowledgement replaces local Audit truth | Producer/Tenant validation and durable Audit evidence |
| Local Security/Policy Authority | Local trust policy, containment and security constraints | Final local security effect | Central administrator/config silently overrides local policy | Policy version, authority and incident evidence |
| Local Operational Execution Authority | Authorized recovery, re-drive and privileged execution | Execute an already authorized scoped action | Own Domain facts, self-authorize or select conflict winner | Actor/workload, action, scope, authorization and outcome |
| Future Eligibility Policy Authority | Suspension and restoration eligibility | Final eligibility decision under a future approved policy | Implicit assignment to Operations or monitoring | Complete applicable DEC-014 gate evidence |
| Central Federation Identity | Authenticated external participant | Supply bounded, locally approved federation input | Implicit administration, recovery, reconciliation or restoration authority | Mutual authentication, purpose, Tenant/Profile scope and local approval |

The specialist is asked to preserve explicit separation between federation participant authentication, local issuer validation, local policy authority, Domain business authorization and privileged execution authorization.

## D. Credential, Key and Secret Custody Matrix

### D.1 Custody concerns

| Concern | Candidate local requirement | Central-assisted boundary | Required evidence | Pending decision |
| --- | --- | --- | --- | --- |
| Trust anchors | Custody and final validation remain local | Central may offer candidate material; local activation is final | Inventory, provenance, activation, revocation and custody | `OD-012`; trust architecture |
| Workload credentials | Local validation and revocation remain usable while disconnected | Enrollment assistance only under locally approved workflow | Workload mapping, audience, scope, validity and state | `OD-011` |
| Issuance/activation | Applicable activation requires local authority | Remote provisioning cannot self-activate | Request, approver, material version and outcome | Issuance policy |
| Signing/verification | Applicable signing authority and verification trust remain local | Approved public metadata may be federated | Key identity, purpose, state and custody | Algorithm/key hierarchy |
| Secret distribution | Local authorization and least-privilege delivery | Central package requires local authenticity and purpose validation | Recipient, scope, version, source and outcome | Secret provider |
| Rotation/trust migration | Controlled local overlap, activation and retirement | Central may propose schedule/material only | Old/new state and transition evidence | Lifetime/overlap policy |
| Revocation | Final revocation effect is enforceable locally | Central signal is input, not final authority | Locally effective record and propagation evidence | Revocation mechanism |
| Compromise containment | Local disablement, scope reduction and incident response | Central may assist without acquiring authority | Affected material, blast radius, actions and outcome | Incident policy |
| Operator/emergency credentials | Distinct, scoped, revocable, time-bounded and auditable | Federated operator still needs local authorization | Identity, reason, scope, expiry, action and review | Privileged/break-glass policy |
| Backup/recovery material | Protected and restored under local authority | External escrow only with separate approval | Chain of custody, integrity, authorization and restore outcome | Recovery custody model |
| Audit confirmation trust | Bind confirmation to local Audit authority and evidence | Central reference cannot substitute local confirmation | Audit authority, full key and durable-ingestion evidence | Authenticity mechanism |

### D.2 Logical custody alternatives

| Alternative | Authoritative control point | Availability/disconnection property | Primary risk | Status |
| --- | --- | --- | --- | --- |
| Fully local lifecycle | Local authority | Maximum disconnected independence | Local operational and custody burden | `CANDIDATE — NOT SELECTED` |
| Central-assisted provisioning with local activation | Local activation | Assistance available when connected; no synchronous dependency | Implicit activation or stale provisioning | `CANDIDATE — NOT SELECTED` |
| Locally validated federated trust | Local validation | Federation usable while valid local trust exists | Issuer, replay, scope and revocation ambiguity | `CANDIDATE — NOT SELECTED` |
| Split custody and recovery | Multiple explicitly authorized custodians | Can improve separation of duties | Recovery complexity and availability trade-off | `CANDIDATE — NOT SELECTED` |
| Protected offline recovery material | Local emergency authority | Recovery during disconnection | Theft, freshness and chain-of-custody risk | `CANDIDATE — NOT SELECTED` |

No PKI, KMS/HSM, algorithm, key hierarchy, credential format, lifecycle duration, revocation target or product is selected.

## E. Disconnected Security Continuity Matrix

| Scenario | Locally authoritative evidence/authority | Candidate permitted behavior | Required fail-closed behavior | DEC-014 implication | Gap/test |
| --- | --- | --- | --- | --- | --- |
| Central Control Plane outage | Local Identity, Tenant, Domain, Audit and policy state | Continue locally valid operations | Central-only actions stop | Gates remain locally assessable if sources are valid | `NT-020` |
| Central federation outage | Local trust and last locally approved state | Stop federation exchange; retain local decisions | Do not accept unverifiable remote changes | Locally assessable | Reconnect policy; `NT-020` |
| WAN partition | Local custody, identity, Tenant, Audit and monitoring | Operate only under valid local authority | External federation effects stop | Local evidence governs | Duration unapproved |
| Central configuration delivery failure | Current locally approved configuration | Continue under valid local state where policy permits | Reject unverified or downgraded replacement | Depends on local policy validity | Version/expiry policy |
| Local IdP/issuer outage | Existing locally verifiable evidence may be bounded | Only operations still independently verifiable | Uncertain new trust fails closed | Affected authority gate unknown/failed | `NEW_CANDIDATE — NOT REGISTERED` |
| Local workload validation failure | No valid producer/workload authority | None for affected producer-sensitive action | Fail before Domain/persistence effect | Integrity/provenance gate failed | `NEW_CANDIDATE — NOT REGISTERED` |
| Local Tenant Authority outage | Authoritative Tenant Context unavailable | Non-Tenant-independent actions only if separately valid | Tenant-aware operations fail closed | Tenant gate failed | `NT-007` family |
| Local Audit outage | Customer durable obligations and outage evidence | Preserve recoverable obligations; no fabricated success | No Audit confirmation | Audit/reconciliation gate may fail | `NT-020` |
| Local monitoring failure | Domain facts may remain; coverage incomplete | Continue only paths independent of missing evidence | Missing coverage is not zero backlog | Observability Gate unproven | `NT-013/016` |
| Local key/secret service outage | Current trusted state may be bounded | Only actions with independently valid trust evidence | New/uncertain trust decisions fail closed | Integrity/authority gate affected | Recovery policy candidate |
| Local privileged operator unavailable | Domain evidence remains | Ordinary independently authorized work may continue | Recovery/re-drive not executed | Recovery authority absent | `NT-013` |
| Security incident during disconnection | Local Security Incident Authority | Local containment and bounded incident action | Do not wait for mandatory Central approval | Gates may be suspended by evidence | Local incident runbook |
| Local revocation during disconnection | Local revocation state | Apply revocation immediately | Stale Central assertion rejected | Trust gate follows local state | `NEW_CANDIDATE — NOT REGISTERED` |
| Customer obligation recovery without Central | Customer durable obligation and local authorities | Local publication, Audit and reconciliation under approved policy | Broker/memory state not authoritative | Recoverability, visibility and integrity gates required | `NT-020` plus crash cases |

The matrix distinguishes locally valid authority, unverifiable authority, unavailable Domain service, incomplete monitoring/recovery evidence and unproven DEC-014 eligibility. Loss of deferred eligibility does not automatically roll back committed Customer mutations or shut down every Customer operation. Any alternative path must independently satisfy its own authorization, consistency, Audit and failure policy.

Full Air-Gap, numeric outage objectives, guaranteed disconnected duration and final continuity policy remain unapproved.

## F. Federation and Reconnection Security Matrix

### F.1 Information classification

| Information class | Candidate classification | Permitted exchange candidate | Prohibited behavior |
| --- | --- | --- | --- |
| Local Customer facts and obligation truth | `LOCALLY_AUTHORITATIVE — NON_OVERWRITABLE` | Approved reference/contract only | Central overwrite or shared source of truth |
| Local Audit ingestion, confirmation and disposition | `LOCALLY_AUTHORITATIVE — NON_OVERWRITABLE` | Authorized evidence reference | Central/broker substitution |
| Local trust and revocation state | `SECURITY-SENSITIVE — RESTRICTED` | Minimum approved status/reference | Remote activation or stale reactivation |
| Private keys, credentials and raw secrets | `PROHIBITED WITHOUT SEPARATE AUTHORIZATION` | None by default | Unapproved cross-boundary transfer |
| Reconciliation references | `FEDERATED REFERENCE CANDIDATE` | Tenant/Profile-bound evidence references | Cross-service database access or shared truth |
| Monitoring views | `DERIVED OPERATIONAL PROJECTION` | Approved aggregates with coverage metadata | Projection becomes Domain/security authority |
| Versioned configuration/package metadata | `FEDERATED CANDIDATE` | Authenticated versioned package/reference | Automatic activation or downgrade |
| Sensitive business payload | `RESTRICTED — PURPOSE-BOUND` | Only under approved contract, authorization and residency | Reconnection treated as residency exception |
| Incident evidence | `SECURITY-SENSITIVE — RESTRICTED` | Minimized policy-controlled exchange | Unnecessary secrets or business disclosure |

### F.2 Reconnection controls

| Concern | Candidate security boundary |
| --- | --- |
| Participant authentication | Both participants independently authenticated; Central identity is not a local issuer by implication |
| Local trust validation | Local trust state and policy determine effect |
| Tenant/Profile/purpose binding | Every exchange explicitly scoped |
| Contract compatibility | Supported versions only; unauthorized downgrade fails closed |
| Replay/delay | Stale or replayed input does not regain authority; arrival order is not authority |
| Duplicate evidence | Applicable idempotency; no second authoritative effect |
| Local rotation/revocation | Stale Central state cannot reactivate locally revoked trust |
| Customer/Audit ownership | Federation never changes Domain evidence ownership |
| Administrative actions | Central instruction requires explicit local authorization |
| Conflict preservation | Preserve both views, provenance and unresolved state |
| Data minimization/residency | Only purpose-bound authorized data crosses `TB-016` |
| Incident restrictions | Active local incident constraints remain effective during reconnect |

The following are mandatory non-selected-winner boundaries:

```text
NO AUTOMATIC CENTRAL_WINS
NO AUTOMATIC LOCAL_WINS
NO LAST_WRITER_WINS
NO AUTOMATIC TRUST REACTIVATION
NO IMPLICIT CENTRAL ADMINISTRATION
```

Final federation protocol, replication architecture, data-transfer exception and conflict-resolution winner remain pending.

## G. Recovery, Incident and Eligibility Matrix

The following are separate milestones:

```text
RECOVERY_COMPLETED
ELIGIBILITY_GATES_REESTABLISHED
RESTORATION_AUTHORIZED
```

No milestone automatically grants the next.

| Activity | Required candidate authority | Required evidence | Prohibited result |
| --- | --- | --- | --- |
| Customer obligation recovery | Customer Domain plus authorized executor | Durable obligation, authoritative Tenant and producer evidence | Recovery from memory/broker history alone |
| Local Audit confirmation/reconciliation | Audit Domain | Local full-key confirmation or explicit unresolved disposition | Central/broker creates Audit truth |
| Quarantine inspection/release | Audit resource authority; Security where incident-restricted | Tenant-scoped access, disposition, release authority and outcome | Direct quarantine-to-success transition |
| Privileged re-drive | Domain authorization plus Operations execution | Full key, original evidence, exact scope, reason and current authorization | Operator rewrites semantics or self-authorizes |
| Incident containment | Local Security Incident Authority | Incident ID, affected scope, containment actions and evidence | Mandatory wait for Central authority |
| Compromised trust recovery | Local Identity/Security Authority | Revocation, replacement, validation and compromise record | Stale credential reactivation |
| Monitoring completeness | Operations evidence owner | Source coverage, freshness, checkpoints and gaps | Missing coverage represented as healthy/zero |
| Suspend deferred eligibility | Future approved policy authority | Failed, unknown or invalid DEC-014 gate evidence | Implicit universal Customer shutdown |
| Re-establish gates | Applicable evidence owners | All required durability, visibility, integrity, authorization and recovery evidence | One successful retry treated as sufficient |
| Authorize restoration | Future Eligibility Policy Authority | Explicit approval after gate evidence and incident restrictions | Operations automatically becomes authority |

`ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED` and its assignment remains `DEFERRED`. Sovereign Operations does not automatically possess final eligibility-policy authority. No restoration execution authorization is granted by this request.

## H. Deployment Profile Comparison

| Dimension | Shared SaaS | Dedicated Managed | Dedicated Sovereign |
| --- | --- | --- | --- |
| Final identity authority | Platform-managed | Provider-managed dedicated | Locally final or locally approved federation |
| Tenant authority | Platform Tenant Management | Dedicated managed authority | Locally final Tenant authority |
| Audit evidence authority | Cell/service Audit | Dedicated managed Audit | Locally final Audit |
| Operational execution | Platform Operations | Managed dedicated Operations | Locally authorized Sovereign Operations |
| Central connectivity assumption | Normally available but not an authorization substitute | May be part of approved managed design | Critical local authority cannot require synchronous Central |
| Trust-anchor custody | Platform/cell | Provider-managed dedicated | Local custody/final activation |
| Revocation | Platform-controlled | Managed dedicated | Locally enforceable while disconnected |
| Incident containment | Platform Security | Managed Security | Locally executable and final within approved scope |
| Federation boundary | Internal/platform | Controlled management federation | Explicit `TB-016` under local approval |
| Recovery/monitoring evidence | Platform evidence | Dedicated evidence | Independently sufficient local evidence |
| Full Air-Gap | Not applicable | Not implied | Not approved; `OD-001` remains Open |

Common invariants across all profiles include Domain-owned authorization, validated Tenant Context, service-owned data, versioned contracts, fail-closed invalid authority, sensitive-data minimization and traceable Audit/recovery. Dedicated Managed and Dedicated Sovereign do not have identical local authority models.

## I. SS-01 through SS-05 Specialist Decision Requests

Every entry has status `PROPOSED — SOVEREIGN SECURITY AUTHORITY REVIEW REQUIRED`.

### SS-01 — Local Trust Anchors and Security Authority

- **Proposed invariant:** Central identity or assertion creates no implicit local authority; local receiving boundaries independently validate identity, producer, Tenant, policy and action scope.
- **Preferred logical direction:** locally final layered trust with bounded, locally approved federation.
- **Alternatives:** fully local trust, locally validated federation or assisted provisioning with local activation.
- **Threats addressed:** `AB-019`, `TA-012`, `TB-016` and authority substitution.
- **Evidence required:** authority map, local issuer validation, revocation and unauthorized-Central denial paths.
- **Open Decisions:** `OD-001`, `OD-011`, `OD-012`, `OD-015`.
- **Dependencies:** Identity/Platform Security, Tenant Security, Security Architecture and Domain Owners.
- **Reviewer questions:** Which validation decisions must remain entirely local? What is the minimum evidence for accepting a federation participant? Which missing or conflicting facts must fail closed?
- **NON-AUTHORITATIVE analyst recommendation:** approve locally final authority separation with boundaries; retain technology and trust architecture as pending.

### SS-02 — Credential, Key and Secret Custody

- **Proposed invariant:** Activation, validation, revocation, compromise containment and protected recovery remain enforceable under local authority.
- **Preferred logical direction:** local custody/final activation with optional bounded Central assistance.
- **Alternatives:** fully local lifecycle, locally validated federation, split custody or protected offline recovery.
- **Threats addressed:** compromise of `AS-019`, stale trust, unauthorized Central activation and custody loss.
- **Evidence required:** inventory, lifecycle, custody, rotation, revocation, compromise and recovery chain.
- **Open Decisions:** `OD-011`, `OD-012`, `OD-023`.
- **Dependencies:** Identity/Platform Security, Security Architecture, Sovereign Operations and incident policy.
- **Reviewer questions:** Which material must never leave the Sovereign boundary? Which Central assistance is permissible? What authority and evidence govern recovery after local authority loss?
- **NON-AUTHORITATIVE analyst recommendation:** approve local final custody boundaries only; keep product, algorithm, hierarchy and duration pending.

### SS-03 — Disconnected Security Continuity

- **Proposed invariant:** Central loss does not invalidate valid local authority; unavailable or unverifiable local authority fails closed only for the affected operation/scope.
- **Preferred logical direction:** locally assessable authority and DEC-014 gates with explicit scope of uncertainty.
- **Alternatives:** fully local continuity or bounded use of last locally approved federation state; Central-master authority is rejected by ADR-V3-004.
- **Threats addressed:** `AB-020`, `TS-003`, unavailable authority and false continuity evidence.
- **Evidence required:** Critical Local Operation Catalog, failure-mode evidence, local gate evaluation and incident escalation paths.
- **Open Decisions:** `OD-001`, `OD-015`, `OD-019`, `OD-023`.
- **Dependencies:** Domain Owners, Audit, Operations, Tenant Security and Future Eligibility Policy Authority.
- **Reviewer questions:** Which operations are critical-local? What is the fail-closed scope for each local authority outage? How is incident escalation executed without Central connectivity?
- **NON-AUTHORITATIVE analyst recommendation:** approve qualitative continuity boundaries; keep Full Air-Gap, durations and numeric objectives pending.

### SS-04 — Secure Federation and Reconnection

- **Proposed invariant:** Federation and reconnection preserve local authority, revocation, Domain ownership, residency and unresolved conflicts without automatic winner.
- **Preferred logical direction:** mutually authenticated, purpose/Tenant/Profile-scoped and conflict-preserving exchange under local approval.
- **Alternatives:** reference-only exchange, separately approved replication or authorized manual reconciliation.
- **Threats addressed:** `AB-019`, `AB-020`, replay, downgrade, stale reactivation and unauthorized disclosure.
- **Evidence required:** participant authentication, local trust validation, information-class rules, version/replay behavior and conflict records.
- **Open Decisions:** `OD-001`, `OD-008`, `OD-011`, `OD-012`, `OD-020`, `OD-023`.
- **Dependencies:** Contract Governance, Messaging/API Event Architecture, Tenant Security, Sovereign Operations and Security Architecture.
- **Reviewer questions:** Which information classes may cross `TB-016`? What conditions permit a local effect? How are stale Central trust and unresolved version conflicts handled?
- **NON-AUTHORITATIVE analyst recommendation:** approve no-auto-winner, local-validation and preservation boundaries; keep protocol and replication pending.

### SS-05 — Sovereign-local Recovery and Incident Constraints

- **Proposed invariant:** Recovery completion, gate re-establishment and restoration authorization are separate; every privileged action uses current local authority and immutable Domain evidence.
- **Preferred logical direction:** Domain-owned evidence, scoped local execution and separate eligibility-policy authority.
- **Alternatives:** policy-governed automation or controlled manual/emergency execution; neither is selected.
- **Threats addressed:** unauthorized re-drive/restoration, quarantine bypass, false monitoring and compromised credentials.
- **Evidence required:** privileged action catalog, gate checklist, monitoring coverage, incident constraints and restoration authority record.
- **Open Decisions:** `OD-015`, `OD-019`, `OD-023`.
- **Dependencies:** Customer/Audit owners, Operations, Security Architecture, Operational Policy Governance and Future Eligibility Policy Authority.
- **Reviewer questions:** Which actions require Sovereign Security approval or veto? What evidence blocks restoration? What controls constrain emergency execution?
- **NON-AUTHORITATIVE analyst recommendation:** approve milestone and authority separation with boundaries; keep final policy, execution and restoration authority pending.

## J. Threat and Negative-Test Traceability

All tests remain `NOT_EXECUTED`. Additional variants are `NEW_CANDIDATE — NOT REGISTERED` and create no official identifier.

| Failure condition | Required denial/containment | Authoritative evidence/verifier | Traceability/status |
| --- | --- | --- | --- |
| Forged Central issuer presented as local | Fail closed; no local authority | Local issuer/trust validation; Identity/Sovereign Security | `NT-019`; extension unexecuted |
| Central admin attempts local policy override | No local effect | Local policy decision and denial Audit | `NT-019`; `NOT_EXECUTED` |
| Central confirmation substitutes local Audit truth | Reconciliation remains incomplete | Local Audit lookup/evidence | `NT-009/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Stale Central configuration replay | Reject activation | Local version/revocation state | `NT-011/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Reconnect under wrong Tenant/Profile | Reject exchange/effect | Tenant/Profile scope evidence | `NT-007/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Locally revoked identity reactivated by federation | Deny | Local revocation evidence | `NT-009`; `NEW_CANDIDATE — NOT REGISTERED` |
| Local trust-anchor compromise | Contain/suspend affected trust | Incident and local trust state | `NEW_CANDIDATE — NOT REGISTERED` |
| Local Identity Authority outage | Uncertain authentication fails closed | Local authority health and denial evidence | `NT-020`; `NEW_CANDIDATE — NOT REGISTERED` |
| Local Tenant Authority outage | Tenant-aware operations fail closed | Tenant authority denial | `NT-007` family; `NEW_CANDIDATE — NOT REGISTERED` |
| Local Audit outage during WAN partition | No fabricated confirmation | Customer obligation and local outage evidence | `NT-020`; `NOT_EXECUTED` |
| Missing monitoring represented as zero backlog | Coverage remains unknown/incomplete | Source coverage/checkpoint evidence | `NT-013/016`; `NOT_EXECUTED` |
| Unauthorized local privileged recovery | Reject execution | Action-specific authorization denial | `NT-013`; `NOT_EXECUTED` |
| Central evidence overwrites local facts | Reject and preserve conflict | Customer/Audit evidence owners | `NT-019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Semantic version conflict after reconnect | Unsupported/conflict; no silent winner | Contract and reconciliation evidence | `NT-019/020`; `NEW_CANDIDATE — NOT REGISTERED` |
| Unauthorized cross-boundary disclosure | No transfer | Disclosure decision and Tenant scope | `NT-017/018`; `NEW_CANDIDATE — NOT REGISTERED` |
| Unauthorized restoration after reconnect | Deny | DEC-014 gates and authority record | `NT-013/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Valid local operation blocked solely by Central outage | Local decision remains possible under valid local policy | Local trust/authorization evidence | `NT-020`; `NOT_EXECUTED` |
| Local security incident without Central | Local containment proceeds | Incident authority and action evidence | `NT-020` extension; `NEW_CANDIDATE — NOT REGISTERED` |

## K. Evidence Gaps and Specialist Dependencies

| Gap | Required completion artifact | Primary authority | Current status |
| --- | --- | --- | --- |
| Locally final authority catalog | Approved local authority and validation matrix | Sovereign-specific Security | `SPECIALIST_DECISION_PENDING` |
| Identity/workload trust | Local issuer, credential and revocation design | Identity/Platform Security | `SPECIALIST_DECISION_PENDING` |
| Tenant authority | Local association, Context and switch/revocation design | Tenant Security | `SPECIALIST_DECISION_PENDING` |
| Custody/recovery | Key/secret lifecycle and recovery authority design | Security Architecture + Sovereign Security | `DESIGN_EVIDENCE_MISSING` |
| Federation contract | Authentication, scope, data-class and conflict design | Contract/Messaging + Sovereign Security | `DESIGN_EVIDENCE_MISSING` |
| Disconnected operation | Critical Local Operation Catalog and failure policies | Sovereign Operations + Domain Owners | `DESIGN_EVIDENCE_MISSING` |
| Local Audit confirmation | Authenticity, lookup and outage behavior | Audit + Security Architecture | `DESIGN_EVIDENCE_MISSING` |
| Privileged recovery | Action catalog, authorization and quarantine lifecycle | Operational Policy Governance | `DESIGN_EVIDENCE_MISSING` |
| Monitoring completeness | Coverage/freshness/checkpoint model | Operations | `DESIGN_EVIDENCE_MISSING` |
| Eligibility/restoration | Assigned authority and approved policy | Future Eligibility Policy Authority | `NOT_YET_ASSIGNED / DEFERRED` |
| Runtime and negative tests | Executable profile-specific evidence | Implementation owners | `NOT_VERIFIED / NOT_EXECUTED` |
| Security sufficiency | Independent review of approved specialist baseline | Independent Security Reviewer | `NOT_SIGNED_OFF` |

No handoff transfers or merges approval authority. Customer and Audit Domain Owners retain their facts; Sovereign Operations remains an execution authority only within approved scope.

## L. Authorized Reviewer Disposition Template

This section must be completed only by a verified reviewer acting within documented Sovereign-specific Security authority. Blank fields are intentional.

### L.1 Reviewer provenance

| Field | Reviewer-supplied value |
| --- | --- |
| Reviewer identity/authenticated reference |  |
| Verified Sovereign-specific Security authority |  |
| Authority scope and delegation evidence |  |
| Reviewed Git baseline and document SHA-256 |  |
| Review date, if supplied |  |
| Review limitations |  |
| Authenticated review-record reference |  |

Allowed outcomes are `APPROVE_WITH_BOUNDARIES`, `AMEND`, `REJECT`, `BLOCKED`, and `EVIDENCE_REQUIRED`.

| Item | Disposition | Approved/rejected scope or replacement wording | Required amendments | Required evidence | Dependencies/limitations |
| --- | --- | --- | --- | --- | --- |
| `SS-01` |  |  |  |  |  |
| `SS-02` |  |  |  |  |  |
| `SS-03` |  |  |  |  |  |
| `SS-04` |  |  |  |  |  |
| `SS-05` |  |  |  |  |  |

No blank field implies approval. A Sovereign-specific Security disposition is not Security Architecture approval, Independent Security Review sign-off, risk acceptance, implementation verification or authorization by another specialist.

## M. Explicit Non-Approvals and Governance Status

This request does **not** approve:

- `SS-01` through `SS-05` or a final Sovereign security design;
- a final IdP, PKI, KMS/HSM, secret manager, credential format, cryptographic mechanism or product;
- key hierarchy, credential lifetime, rotation interval or numeric revocation target;
- a federation/replication protocol, residency exception or conflict-resolution winner;
- Full Air-Gap support, guaranteed disconnected duration or numeric continuity objective;
- a final Critical Local Operation Catalog, incident policy or privileged-action model;
- Eligibility Policy Authority assignment or restoration execution authorization;
- any SR-CAND item, risk rating, mitigation, risk acceptance or security exception;
- implementation correctness, runtime security, executed negative tests, executable DURABLE_DEFER or Production Readiness.

The following governance state is preserved exactly:

```text
V3-003 = IN PROGRESS
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
SOVEREIGN_SECURITY_AUTHORITY_APPROVAL = PENDING
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

The next bounded activity is an actual authorized Sovereign-specific Security review of the exact content hash of this request and its pinned sources. The reviewer must establish identity, authority, scope, reviewed baseline, limitations and item-specific rationale. Repository recording alone must not upgrade any approval or readiness status.
