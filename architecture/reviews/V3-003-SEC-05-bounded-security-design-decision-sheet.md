# V3-003 — SEC-05 Sovereign-local Trust and Reconnection Security Design

**Document Status:** `DRAFT — SECURITY REVIEW REQUIRED`  
**Project/Domain Owner Dispositions:** `APPROVED_WITH_BOUNDARIES_OR_AMENDMENTS`  
**Security Architecture Approval:** `PENDING`  
**Operational Policy Approval:** `PENDING`  
**Independent Security Review:** `NOT_SIGNED_OFF`  
**Executable DURABLE_DEFER:** `NOT APPROVED`

> شناسه‌های `SL-01` تا `SL-05` فقط labels محلی این Decision Sheet هستند و هیچ `DEC`، `ADR` یا `Security Requirement` رسمی جدیدی ایجاد نمی‌کنند.

## A. Verified Baseline and Document Control

### A.1 Repository baseline

| مورد | مقدار بررسی‌شده |
|---|---|
| Repository | `E:\Neshane-CRM-V3` |
| Branch | `main` |
| Git HEAD | `1bebc667b12a37ca0494491890fb4808560b03ec` |
| Remote tracking at preflight | `main` دوازده commit جلوتر از `origin/main` |
| Worktree / index at preflight | پاک؛ index خالی |
| Customer/Audit Technical Contract SHA-256 | `56E71F3EE0537BFC70D0E3F02602175D0E0EB87510FBB7AB43125F37C4010412` |
| Security Review Input Manifest SHA-256 | `A73FC9346361FCD95CA6F4914CFF53BE7201DCFC35DF9A71334D14D442D3EF22` |
| SEC-01 SHA-256 | `0394A08682ED911F5C61839CA371E0852072E5621F9B33FFB0E322FEC738CA7B` |
| SEC-02 SHA-256 | `F0B6D9816324CD6F2C0A1BDE239A772A677ABA41CB05645379F880D65F7FA645` |
| SEC-03 SHA-256 | `69C1A5DE357438CEBD2BFD55DA0B110FD476C92CA05D21ADF0DAE3FF2961C655` |
| SEC-04 SHA-256 | `2D03D1CDA36C3E9F379824ED46B2C6AFFB362B504F098A95F137DB2E1349F6E6` |
| SEC-01 through SEC-04 revision state | همگی tracked، committed و موجود در HEAD |

### A.2 Authoritative and supporting sources

- ADR-V3-003, ADR-V3-004, ADR-V3-005, ADR-V3-007, ADR-V3-008, ADR-V3-010 and ADR-V3-012.
- `V3-003-DEC-009`, `V3-003-DEC-013` and `V3-003-DEC-014`, with related decisions `DEC-010` through `DEC-012` preserved.
- Pinned Customer/Audit Durable Delivery Technical Contract, especially H.3 through H.8 and J.
- V3-003 Security Review Input Manifest, especially S7 and S8.
- SEC-01 through SEC-04 bounded decision sheets.
- Security, Messaging, Persistence and Service Architecture standards.
- `TA-012`, `TS-003`, `AS-019`, `AS-020`, `TB-016`, `AB-019`, `AB-020`, `NT-019`, `NT-020` and `SR-CAND-021..024`.
- Open Decisions `OD-001`, `OD-011`, `OD-012`, `OD-015`, `OD-019`, `OD-020` and `OD-023`.

### A.3 Existing approved boundary

Dedicated Sovereign has locally authoritative security and operational control. Central identities have no implicit local administrative rights; Central availability or acknowledgement is not a mandatory synchronous prerequisite for legitimate local evidence. Customer retains local obligation truth، Audit retains local ingestion/confirmation/disposition truth، and Domain-owned authorization remains final for Domain resources.

These approved boundaries do not select identity، trust، key-management، federation، topology or disconnected-operation technologies and do not establish Full Air-Gap support.

### A.4 Approval boundary

این سند پنج disposition محدود Project/Customer/Audit/Operations Owner را برای `SL-01` تا `SL-05` ثبت می‌کند. هیچ approval از سوی Identity/Platform Security، Tenant Security، Sovereign-specific Security Authority، Security Architecture، Operational Policy Governance، Eligibility Policy Authority یا Independent Security Reviewer ثبت نمی‌کند. این dispositions تأیید نهایی security trust model نیستند و هیچ implementation، runtime یا production evidence از آن‌ها استنتاج نمی‌شود.

## B. Sovereign-local Trust and Authority Matrix

### B.1 Candidate logical authority classes

| Authority class | Candidate owned fact or decision | Required locally final behavior | Forbidden substitution |
|---|---|---|---|
| Local Identity Authority | Principal identity، authenticator و authentication/session validity | validation و local revocation قابل‌اعمال در Sovereign | Central identity به‌تنهایی Principal یا access محلی ایجاد نکند |
| Local Workload Trust Authority | Workload identity، credential state و server-controlled authority mapping | issuer/trust، audience، validity، revocation و applicable workload authority محلی | network location، header یا Central assertion دلخواه `ProducerAuthority` نسازد |
| Local Tenant Authority | Tenant/Membership evidence و authoritative Tenant Context | Tenant scope هر operation محلی validate شود | Central Tenant claim بدون local validation پذیرفته نشود |
| Local Audit Evidence Authority | Local Audit ingestion، confirmation، conflict و disposition facts | Audit Domain محلی تنها مرجع Audit fact باشد | Central confirmation یا broker acknowledgement جایگزین local Audit fact نشود |
| Local Operational Execution Authority | اجرای authorized recovery، re-drive و privileged action | execution به action-specific authorization و local evidence متصل باشد | Operations مالک Customer/Audit truth یا Domain authorization نشود |
| Local Security/Policy Authority | local trust policy، incident containment، security constraints و local approval | اثر امنیتی نهایی تحت authority محلی باشد | Central administrator یا config delivery خودکار policy محلی را override نکند |
| Central Federation Identity | هویت participant بیرونی در `TB-016` | فقط input authenticated، scoped و locally approved باشد | هیچ implicit administration، recovery، reconciliation یا restoration authority ایجاد نکند |

### B.2 Trust and authority matrix

| Actor / authority | Owned facts or decisions | Permitted influence | Forbidden authority substitution | Required local evidence | Pending approval |
|---|---|---|---|---|---|
| Local Customer Domain | Customer mutation، obligation و producer-side recovery truth | publication/recovery evidence و producer reconciliation | اعلام Audit ingestion یا تغییر Audit-owned facts | authorization، Tenant Context و durable obligation evidence | Customer detailed design |
| Local Audit Domain | ingestion، confirmation، conflict، quarantine/disposition truth | authorized lookup و Audit reconciliation evidence | تغییر Customer fact یا authorizing Customer operation | producer/Tenant validation و durable Audit evidence | Audit/Security contract |
| Local Identity/Platform Security | identity/workload trust و credential lifecycle | authenticated identity and authority mapping | Business resource authorization | local issuer/trust، audience، validity and revocation evidence | Identity/Platform Security |
| Local Tenant Authority | Membership/Tenant association and Context evidence | operation-scoped Tenant validation | Entitlement یا Domain authorization | locally valid Tenant evidence | Tenant Security Authority |
| Local Operations | monitoring، incident coordination and authorized execution | execute scoped recovery/re-drive | fabricate Domain evidence، select conflict winner or authorize restoration | action identity، scope، authorization and outcome evidence | Operational Policy Governance |
| Local Security Incident Authority | incident containment and compromise response | constrain actions under authorized incident process | silent risk acceptance or Domain authority replacement | incident identity، affected scope and approvals | Security policy |
| Future Eligibility Policy Authority | final suspension/restoration decision under DEC-014 | evaluate authorized eligibility policy | implicit assignment to Operations or monitoring component | complete applicable gate evidence | `NOT_YET_ASSIGNED` |
| Central Control Plane | approved package/configuration candidate | supply bounded input for local validation | direct local administrative effect | authenticated source، version، purpose and local approval | Federation/configuration policy |
| Central Federation Service | bounded evidence/metadata exchange | exchange approved references and projections | overwrite local Customer/Audit evidence | mutual authentication، Tenant/Profile scope and provenance | Federation contract |
| Independent Security Reviewer | scoped review finding | assess design evidence and gaps | Owner decision، authority assignment or runtime verification | pinned baseline and explicit review scope | Reviewer feedback absent |

Candidate trust controls:

1. Every receiving local boundary independently validates identity، Tenant، producer/contract authority and operation scope.
2. Central identity، control-plane availability or configuration delivery does not independently create local authorization.
3. Missing، expired، revoked، indeterminate or conflicting local authority fails closed for the affected operation.
4. Central unavailability does not invalidate otherwise valid local authority.
5. Central availability does not compensate automatically for failed local Identity، Audit، monitoring، key or recovery authority.

## C. Local Key and Secret Custody Matrix

### C.1 Custody and lifecycle concerns

| Custody concern | Candidate local requirement | Central-assisted alternative boundary | Required evidence | Pending decision |
|---|---|---|---|---|
| Local trust anchors | custody and final validation remain local | Central may provide candidate material؛ activation requires local approval | inventory، provenance، activation، revocation and custody evidence | trust technology / `OD-012` |
| Workload credentials | issuance/activation where applicable، validation and revocation usable locally | Central enrollment assistance only under locally approved workflow | credential-to-workload mapping، audience، scope and state | workload identity / `OD-011` |
| Signing/verification keys | applicable signing authority and verification trust remain local | public verification metadata may be federated | key identity، purpose، state، custody and compromise evidence | algorithm/key hierarchy |
| Secret distribution | local authorization، least privilege and auditable delivery | Central-delivered package only after local verification | recipient، scope، version، source and outcome | secret manager / `OD-012` |
| Rotation | local continuity and controlled overlap | Central may propose schedule or material؛ local activation remains final | old/new state، overlap، activation and retirement evidence | numeric lifetime/rotation |
| Revocation | final revocation effect available locally while disconnected | Central revocation signal is input only | locally effective revocation record and propagation evidence | revocation protocol |
| Compromise response | local containment، disablement and incident handling | Central may assist investigation without acquiring authority | affected keys/workloads، scope، actions and outcome | incident runbook |
| Backup and recovery | locally authorized protected recovery | external escrow/recovery candidate only under explicit approval | chain of custody، integrity، approver and restore outcome | backup medium/topology |
| Operator credentials | distinct، scoped، revocable and auditable identities | federated operator identity only with local authorization | operator/action/Tenant/scope evidence | privileged identity policy |
| Audit confirmation trust | confirmation must bind local Audit authority and authoritative evidence | Central reference cannot substitute local confirmation | Audit authority، full ObligationKey and durable evidence | confirmation authenticity mechanism |
| Emergency recovery | explicit local emergency authority and bounded evidence | Central assistance cannot self-authorize | break-glass identity، justification، expiry، actions and review | emergency policy |

### C.2 Candidate logical custody models

| Candidate model | Benefit | Boundary / risk | Status |
|---|---|---|---|
| Fully local lifecycle | maximum disconnected independence | higher local operational/custody burden | `CANDIDATE — NOT SELECTED` |
| Central-assisted provisioning with local approval | automation and common governance | must not create synchronous dependency or implicit activation | `CANDIDATE — NOT SELECTED` |
| Federated trust subject to local validation | bounded cross-profile interoperability | issuer، scope، replay and revocation semantics unresolved | `CANDIDATE — NOT SELECTED` |
| Split custody/recovery | stronger separation of duties candidate | recovery complexity and availability trade-offs | `CANDIDATE — NOT SELECTED` |
| Authorized offline recovery package | recovery during disconnection candidate | chain of custody، freshness and compromise risk | `CANDIDATE — NOT SELECTED` |

Private keys، credentials and raw secrets must not be transferred without a separate explicit authority، purpose، custody and security decision. No product، PKI، KMS/HSM، secret manager، cryptographic algorithm، key hierarchy، credential profile، lifetime or rotation target is approved.

## D. Disconnected Operation Matrix

| Scenario | Authoritative local evidence / available authority | Candidate operation behavior | DEC-014 gate evaluation | Deferred eligibility implication | Escalation / recovery dependency | Missing policy / negative-test need |
|---|---|---|---|---|---|---|
| Normal connected operation | local Customer/Audit/trust/Tenant evidence | Central exchange remains bounded input | gates evaluated locally | according to local evidence and future policy | normal local ownership | federation policy; `NT-019/020` unexecuted |
| Central Control Plane outage | local authorities remain available | valid local operations need no synchronous Central dependency | locally evaluable | not suspended solely by Central outage | local incident visibility | continuity evidence; `NT-020` |
| Central federation outage | local trust and last locally approved state | stop federation exchange؛ continue valid local decisions | locally evaluable | not suspended solely by federation outage | reconnect after recovery | reconnect policy; `NT-020` |
| WAN partition | local custody، identity، Audit and monitoring | operate only under valid local policy/evidence | locally evaluable where local sources remain valid | local evidence decides | local escalation and later reconciliation | duration unapproved; `NT-020` |
| Central configuration unavailable | current locally approved configuration | do not infer invalidity or apply unverified replacement | existing local policy may remain evaluable | not failed solely by Central loss | configuration recovery | version/expiry policy Pending |
| Local Identity Authority outage | authentication/revocation evidence may be unavailable | uncertain new trust decisions fail closed | affected authority gate unknown/failed | affected operation/path ineligible or unknown | restore local trust authority | session/credential outage policy; new candidate |
| Local Audit Domain outage | Customer obligations and outage evidence remain local | preserve obligations؛ no fabricated confirmation | Audit/reconciliation gate may fail | conditional only under future executable policy؛ otherwise suspended | restore local Audit and reconcile | `NT-020`; local Audit outage policy |
| Local monitoring outage | Domain facts may remain but visibility is incomplete | zero backlog forbidden | Observability Gate cannot be established | affected scope suspended/unknown | restore coverage/checkpoints | SEC-04 tests; `NT-013/016` |
| Local key/secret authority outage | current local credential/trust state may be incomplete | operations requiring unavailable trust decision fail closed | integrity/authority gate may fail | affected path suspended/unknown | authorized custody recovery | key recovery policy; new candidate |
| Loss of authorized local operators | Domain evidence remains؛ execution authority absent | privileged recovery not executed | recovery authority unavailable | affected recovery path ineligible | emergency staffing/authority | `NT-013`; emergency policy |
| Disconnected recovery after Customer obligation commit | durable Customer obligation truth | recover from Domain evidence، not memory or transport state | recoverability/visibility/integrity gates required | only under future approved local policy | local publication/Audit/reconciliation | scheduler and recovery policy; `NT-020` plus crash candidates |

Central disconnection alone does not invalidate legitimate local authority. Conversely، Central availability does not automatically compensate for failed local trust or missing local Audit authority. Full Air-Gap، guaranteed disconnected duration، numeric continuity targets، final outage policy and final runtime topology remain unapproved.

## E. Reconnection and Federation Matrix

### E.1 Information classification

| Information class | Authority classification | Candidate permitted exchange | Prohibited or pending behavior |
|---|---|---|---|
| Local Customer facts and obligation truth | `LOCALLY_AUTHORITATIVE — NON_OVERWRITABLE` | approved contract/reference only | Central record cannot overwrite or become Customer truth |
| Local Audit ingestion/confirmation/disposition | `LOCALLY_AUTHORITATIVE — NON_OVERWRITABLE` | authorized evidence reference or approved replication candidate | Central confirmation cannot replace local Audit authority |
| Local trust/revocation state | `SECURITY-SENSITIVE — RESTRICTED` | minimum approved status/reference metadata | raw trust state transfer or remote activation without local approval |
| Private keys، credentials and raw secrets | `PROHIBITED FROM TRANSFER` absent separate approval | none by default | any cross-boundary transfer without explicit security/custody decision |
| Customer/Audit reconciliation references | `FEDERATED REFERENCE CANDIDATE` | Tenant/Profile-bound approved evidence references | shared reconciliation truth or cross-service DB access |
| Monitoring projection | `DERIVED OPERATIONAL PROJECTION` | approved aggregate/telemetry | projection must not become Domain authority |
| Versioned configuration/package metadata | `FEDERATED CANDIDATE` | authenticated، versioned package/reference | automatic local activation or downgrade |
| Sensitive business payload | `RESTRICTED / PURPOSE-BOUND` | only under separate contract، authorization and residency approval | reconnect is not a data-residency exception |
| Incident/security evidence | `SECURITY-SENSITIVE — RESTRICTED` | minimized، policy-controlled exchange | unnecessary secrets، credentials or business content |

### E.2 Reconnection trust and conflict controls

| Concern | Candidate security boundary |
|---|---|
| Reconnection authentication | both participants independently authenticated؛ Central identity is not a local issuer by implication |
| Federation trust establishment | `TB-016` enforced by Sovereign-local authority and locally approved trust state |
| Tenant/Profile/purpose scope | every exchange bound to explicit Tenant، profile، contract and purpose |
| Version compatibility | approved contract versions only؛ unsupported or unauthorized downgrade fails closed |
| Replay and delay | stale/replayed configuration or evidence detected؛ arrival order is not authority |
| Duplicate handling | applicable idempotency preserved؛ duplicate exchange creates no second authoritative effect |
| Local key rotation/revocation | evidence signed under revoked/stale local trust must not regain validity from Central state |
| Customer/Audit ownership | federation does not change Domain evidence ownership |
| Evidence conflict | preserve both views؛ no automatic Central-wins، local-wins or last-writer-wins |
| Reconciliation authority | authorized local workflows compare evidence without overwriting another authority's facts |
| Chain of custody | source، actor، scope، version، transfer، local decision and outcome remain traceable |
| Central administrative action | no privileged local effect without local identity، scope، policy and Domain authorization |
| Data disclosure/residency | transfer requires separately approved contract، minimization، authorization and residency basis |

Final federation protocol، replication topology، data-sharing policy، migration policy، conflict-resolution mechanism and residency exception remain Pending.

## F. Local Recovery and Eligibility Matrix

| Existing DEC-014 principle | Required Sovereign-local evidence | Local failure implication | Candidate recovery action | Restoration constraint |
|---|---|---|---|---|
| Durable Deferred Audit Eligibility Gate | local Customer authorization، Tenant Context and durable mutation/obligation | affected deferred path ineligible | recover authoritative Customer evidence | local durability/authorization re-established |
| Evidence-State Separation | local obligation، attempt، delivery and Audit confirmation remain distinct | Central/broker state cannot establish local Audit ingestion | recover local Domain evidence through authorized contracts | valid local Audit-owned confirmation where applicable |
| Recoverability and Observability Gate | local backlog visibility، recovery capability and reconciliation evidence | indeterminate visibility/recovery suspends affected path | restore local source coverage and recovery evidence | trustworthy local observability and recoverability |
| Integrity, Provenance and Recovery Safety Gate | local producer/Tenant/version/integrity evidence | invalid/conflicting evidence fails closed | preserve evidence، investigate and recover under local authority | integrity/provenance valid and incident constraints cleared |
| Dedicated Sovereign Local Eligibility Gate | local custody، monitoring، security policy، recovery and reconciliation authority | Central cannot substitute missing local gate | restore locally authoritative evidence and authority | all applicable local gates plus explicit policy authorization |

Authority boundaries:

- Customer owns local obligation and producer-side recovery truth.
- Audit owns local ingestion، confirmation، conflict and disposition truth.
- Monitoring projections do not become Domain authority.
- Privileged recovery requires operation-specific identity، scope and authorization.
- Dedicated Sovereign restoration requires locally authoritative decisions.
- Sovereign Operations responsibility does not imply Eligibility Policy Authority.

```text
RECOVERY_COMPLETED
ELIGIBILITY_GATES_REESTABLISHED
RESTORATION_AUTHORIZED
```

No state automatically implies the next.

```text
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

Final blast-radius، emergency intervention، suspension، recovery and restoration policies remain Pending.

## G. Negative-Test Candidates

All tests remain `NOT_EXECUTED`. Additional proposals remain `NEW_CANDIDATE — NOT REGISTERED`.

| Exact fault | Required invariant | Authoritative evidence / observable result | Candidate verifier | Traceability |
|---|---|---|---|---|
| Central identity falsely presented as local issuer | fail closed؛ no local identity/authority | local issuer/trust validation denial | Identity/Sovereign Security | `NT-019`; coverage extension candidate |
| Central admin attempts local policy override | no privileged local effect | local policy decision and denial Audit | Sovereign Security | `NT-019` |
| Central Audit confirmation substitutes local confirmation | reconciliation must not complete | negative/indeterminate local Audit lookup | Audit/Security | `NT-009/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Replayed Central configuration | activation rejected | local version/revocation state and replay evidence | Platform Security | `NT-011/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Reconnection with wrong Tenant or profile | fail closed؛ no disclosure/effect | Tenant/Profile binding denial | Tenant Security | `NT-002/007/019` |
| Locally revoked workload accepted from stale Central information | request denied | local revocation state | Workload Security | `NT-009`; `NEW_CANDIDATE — NOT REGISTERED` |
| Local trust anchor compromise | affected trust contained/suspended | incident and local trust state | Security Architecture | `NEW_CANDIDATE — NOT REGISTERED` |
| Local Identity Authority outage | uncertain authentication fails closed | local authority health and denial evidence | Identity Security | `NT-020`; `NEW_CANDIDATE — NOT REGISTERED` |
| Local Audit outage during WAN partition | no fabricated confirmation | local obligation and outage evidence | Audit/Sovereign Operations | `NT-020` |
| Local monitoring failure represented as zero backlog | visibility remains unknown/incomplete | local coverage/checkpoint evidence | Operations/Security | `NT-013/016`; SEC-04 candidates |
| Local operator authorization unavailable | privileged recovery rejected | action authorization denial | Operations/Security | `NT-013` |
| Central evidence overwrites local Customer/Audit truth | overwrite rejected/detected | original local evidence and conflict record | Domain owners/Security | `NT-016/019` |
| Reconnection with semantic-content conflict | no automatic winner or confirmation | both semantic representations preserved | Customer/Audit/Security | `NT-011/012` |
| Cross-boundary data disclosure without authorization | no transfer | disclosure decision، Tenant scope and denial evidence | Data/Sovereign Security | `NT-017/018`; `NEW_CANDIDATE — NOT REGISTERED` |
| Unauthorized restoration after reconnection | restoration denied | DEC-014 evidence and authority denial | Security/Future Eligibility Authority | `NT-013/019`; `NEW_CANDIDATE — NOT REGISTERED` |
| Locally valid operation blocked only because Central is unavailable | local decision remains possible under valid local policy | local trust/authorization evidence | Sovereign Operations/Security | `NT-020` |

## H. SL-01 through SL-05 Proposed Decision Records

### SL-01 — Sovereign-local Trust Authority

**Status:** `APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE`

Approved within the recorded Owner scope:

- Architectural separation of Local Identity Authority، Local Workload Trust Authority، Local Tenant Authority، Local Audit Evidence Authority، Local Operational Execution Authority، Local Security/Policy Authority and Central Federation Identity.
- Locally authoritative Customer/Audit operations cannot require mandatory synchronous Central authority.
- Central identity or availability cannot independently grant local Domain، Security، administrative or operational authority.

Pending: local issuer and workload-trust design؛ Tenant Security mechanisms؛ trust-anchor and identity lifecycle؛ Identity/Platform Security approval؛ Sovereign-specific Security approval؛ and Security Architecture approval. This disposition does not imply approval of the final security trust model.

### SL-02 — Local Key and Secret Custody

**Status:** `APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE`

Approved within the recorded Owner scope:

- Locally final validation، authorization، revocation effect and applicable credential lifecycle must not depend on mandatory synchronous Central connectivity.
- Central-assisted provisioning and federated trust remain permissible candidates only when local final validation and authority are preserved.
- Final validation authority remains separate from provisioning assistance.

Pending: final PKI، HSM/KMS and secret-management architecture؛ private-key custody and trust-anchor governance؛ issuance/rotation mechanisms؛ revocation protocols؛ recovery and break-glass policies؛ cryptographic algorithms and key hierarchy؛ and Security/Operational Policy approvals. No cryptographic or custody implementation is approved.

### SL-03 — Disconnected Operation

**Status:** `APPROVED WITH BOUNDARIES — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE`

Approved within the recorded Owner scope:

- Central outage or WAN partition does not automatically invalidate otherwise valid local authority.
- Existing locally authorized operations may continue subject to applicable local policy and evidence.
- Central availability cannot replace failed local Identity، Audit، monitoring، cryptographic or recovery authority.
- Missing or indeterminate local authority must fail closed for the affected operation or deferred pathway.
- Customer-owned committed facts remain authoritative during disconnection.

Pending: exact service continuity matrix and runtime topology؛ final session/credential behavior during outages؛ numeric availability and disconnected-operation objectives؛ operational incident runbooks؛ Full Air-Gap decision under `OD-001`؛ and specialist Security review. Unconditional offline operation and Full Air-Gap support are not approved.

### SL-04 — Secure Reconnection and Federation

**Status:** `APPROVED WITH AMENDMENTS — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE`

Approved within the recorded Owner scope:

- Mutual authentication and locally validated authorization are required for federation.
- Tenant/Profile scope، purpose، contract version، provenance and replay protection remain mandatory design constraints.
- Customer and Audit authoritative local facts cannot be overwritten by Central federation records.
- Central administration cannot create a local privileged effect without local authorization.
- Reconnection does not itself authorize sensitive-data replication، cross-border transfer or residency exceptions.

**Recorded amendment:** `NON_OVERWRITABLE` local Domain facts do not imply automatic `LOCAL_WINS` conflict resolution. Central-wins، local-wins and last-writer-wins must not be adopted as automatic conflict-resolution policies. Conflicting authoritative views remain preserved with traceable source provenance until an explicitly authorized reconciliation decision is made.

Pending: federation protocol؛ reconnection authentication implementation؛ contract compatibility and migration mechanisms؛ data-exchange schemas and residency approval؛ conflict-resolution governance؛ Tenant/Sovereign Security review؛ and final Security Architecture approval.

### SL-05 — Local Recovery and Eligibility Authority

**Status:** `APPROVED WITH AMENDMENTS — PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE`

Approved within the recorded Owner scope:

- Customer retains local authoritative obligation truth.
- Audit retains local authoritative ingestion and confirmation truth.
- Monitoring remains derived evidence.
- Recovery execution requires action-specific authorization.
- All applicable DEC-014 gates require locally valid evidence.
- Central services cannot silently supply missing local authoritative facts or approvals.

**Recorded amendments:** the following states remain explicitly separate:

```text
RECOVERY_COMPLETED
ELIGIBILITY_GATES_REESTABLISHED
RESTORATION_AUTHORIZED
```

None automatically implies the next. Sovereign Operations responsibility does not constitute an assignment of Eligibility Policy Authority. No operational authority to execute restoration is granted.

```text
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

Pending: explicit Eligibility Policy Authority assignment؛ Sovereign-specific restoration policy؛ final blast-radius and suspension rules؛ local emergency and privileged-recovery policy؛ Security Architecture and Operational Policy approval؛ and Independent Security Review.

### H.6 Approval Register

| Local decision | Recorded disposition | Authority scope |
|---|---|---|
| `SL-01` | `APPROVED WITH BOUNDARIES` | `PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE` |
| `SL-02` | `APPROVED WITH BOUNDARIES` | `PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE` |
| `SL-03` | `APPROVED WITH BOUNDARIES` | `PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE` |
| `SL-04` | `APPROVED WITH AMENDMENTS` | `PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE` |
| `SL-05` | `APPROVED WITH AMENDMENTS` | `PROJECT/CUSTOMER/AUDIT/OPERATIONS OWNER SCOPE` |

```text
PROJECT_AND_DOMAIN_BOUNDED_DISPOSITIONS = APPROVED_WITH_BOUNDARIES_OR_AMENDMENTS
IDENTITY_PLATFORM_SECURITY_APPROVAL = PENDING
TENANT_SECURITY_AUTHORITY_APPROVAL = PENDING
SOVEREIGN_SECURITY_AUTHORITY_APPROVAL = PENDING
SECURITY_ARCHITECTURE_APPROVAL = PENDING
OPERATIONAL_POLICY_APPROVAL = PENDING
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
INDEPENDENT_SECURITY_REVIEW = NOT_SIGNED_OFF
```

The overall SEC-05 document remains `DRAFT — SECURITY REVIEW REQUIRED`. These bounded Project/Domain Owner dispositions do not constitute specialist Security، final Operational Policy or Dedicated Sovereign production-readiness approval.

## I. Specialist Authority and Governance Dependencies

| Authority | Exact pending decision or evidence |
|---|---|
| Project and Domain Owners | Bounded principles recorded؛ detailed Critical Local Operation scope، permitted federation data، Domain continuity and reconciliation contracts remain pending |
| Sovereign Operations | Bounded Operations-owner disposition recorded؛ local continuity evidence، custody، operator availability، disconnected-operation and reconnect runbooks remain pending |
| Identity/Platform Security | local issuer/workload trust، credential lifecycle، revocation and compromise response |
| Tenant Security Authority | local Membership/Tenant Context، Tenant/Profile binding and cross-boundary validation |
| Sovereign-specific Security Authority | local trust custody، federation acceptance، incident and emergency constraints |
| Security Architecture | trust anchors، integrity، cryptography، federation، compromise and recovery controls |
| Operational Policy Governance | outage behavior، escalation، blast radius، reconnect and restoration workflow |
| Eligibility Policy Authority | suspension/restoration authorization؛ authority remains unassigned and deferred |
| Independent Security Reviewer | sufficiency of local trust، Central denial، reconnect conflict، custody and negative-test coverage |

Open dependencies remain `OD-001`, `OD-011`, `OD-012`, `OD-015`, `OD-019`, `OD-020` and `OD-023`. None is closed or modified here.

## J. Explicit Non-Approvals

This document does not approve:

- `SL-01` through `SL-05` as final architecture، security or operational-policy decisions.
- Project/Domain Owner approval، specialist Security approval or Independent Security Review sign-off.
- Full Air-Gap support.
- Guaranteed disconnected-operation duration or numeric continuity/recovery targets.
- Local IdP، PKI، KMS/HSM، secret manager، orchestration or runtime product.
- Cryptographic algorithm، key hierarchy، credential profile، lifetime، rotation or revocation mechanism.
- Federation protocol، replication topology، configuration-delivery mechanism or Central provisioning product.
- Automatic Central-wins، local-wins or last-writer-wins conflict resolution.
- Cross-boundary data replication، residency exception or unrestricted transfer of secrets/credentials.
- Emergency/break-glass operations، final outage policy or recovery/restoration runbook.
- Assignment of Eligibility Policy Authority.
- Any `SR-CAND-001..024` as an approved Security Requirement.
- Any `NEW_CANDIDATE — NOT REGISTERED` test as an official identifier.
- Any Negative Test as executed، passed or failed.
- Implementation correctness، runtime security، risk acceptance or Production Readiness.
- Executable or unconditional `DURABLE_DEFER`.

## K. Governance Status and Next Bounded Action

```text
V3-003 = IN PROGRESS
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

All existing Customer، Audit، Messaging/Operations and SEC-01 through SEC-04 bounded dispositions remain unchanged. No missing authority is inferred from earlier Project/Domain approvals.

**Next bounded activity:** prepare separate specialist review packages for Identity/Platform Security، Tenant Security Authority، Sovereign-specific Security Authority، Security Architecture and Operational Policy Governance. Preserve Eligibility Policy Authority as unassigned and deferred. Any Independent Security Reviewer disposition must be separately authorized and recorded against a pinned baseline after the required specialist evidence is available.
