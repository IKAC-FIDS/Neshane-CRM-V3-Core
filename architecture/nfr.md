# Neshane CRM V3 — Non-Functional Requirements Analytical Baseline

**Document Status:** `DRAFT — ANALYTICAL BASELINE — NOT APPROVED`
**Related Task:** `V3-003 — NFR and Threat Assumptions`
**Architecture Revision:** `NESHANE-V3-ARCH-P00-002`
**Governance Baseline:** `NESHANE-V3-GOV-P00-000A`

## 1. Purpose and approval boundary

این سند یک Baseline تحلیلی، Source-grounded و قابل Review برای NFRهای Neshane CRM V3 است. ثبت یک Statement در این سند، Scope، Requirement، Technology، Numeric target، Security control، Implementation یا Readiness جدیدی را تصویب نمی‌کند.

Classificationها:

- `APPROVED_INVARIANT`: Statement مستقیماً از ADR/DEC مصوب یا یک bounded Owner disposition با همان Scope محدود استخراج شده است. این Classification به معنی Specialist approval، Implementation یا Runtime verification نیست.
- `PROPOSED`: Statement برای تحلیل یا Design Review پشتیبانی می‌شود، اما Authorityهای لازم آن را به Requirement نهایی تبدیل نکرده‌اند.
- `UNRESOLVED`: منبع، نیاز به تصمیم را نشان می‌دهد ولی مقدار، Policy، Mechanism یا Authority نهایی هنوز تعیین نشده است.

Evidence statusها مستقل از Classification هستند. `DESIGN_SOURCE_PRESENT` فقط وجود Source را نشان می‌دهد؛ هیچ Validation اجراشده‌ای در این سند `PASS` نیست.

## 2. Pinned source baseline

| Field | Value |
| --- | --- |
| Repository | `E:\Neshane-CRM-V3` |
| Branch | `main` |
| Git HEAD | `afa19bd5ffe881ff52def2a0b754679a1e1e2855` |
| Working tree at draft start | Proposal زیر Untracked بود؛ دو Target حاضر نبودند |
| Analytical Closure Contract Proposal | `architecture/reviews/V3-003-analytical-closure-contract-proposal.md`; SHA-256 `5dc92f9a13f39d496ea068880416a6f73f785f1ebdba159b139af92ef4656175`; `PROPOSED — NOT APPROVED` |
| V3-003 Decision Record | `architecture/reviews/V3-003-decision-record.md`; SHA-256 `178d447fc642a385c20fecd866de5e87e518944da3f65a005fc6118034000e18` |
| Consolidated Security Manifest | `architecture/reviews/V3-003-consolidated-security-design-review-manifest.md`; SHA-256 `9592b9e9190d2182132d5eebefbd9fdcb7c802f7f8a8e305b8209db699b90c3e` |
| Specialist Tracking Register | `architecture/reviews/V3-003-specialist-review-tracking-register.md`; SHA-256 `c3a4b6c04bc31589d7d6e485c747e31f865805aadca8d8708064450d436c296e` |

Authoritative source families are `architecture/baseline-v3.md`, `architecture/decision-register.md`, `architecture/open-decisions.md`, `architecture/adr/001-*.md` through `012-*.md`, `architecture/standards/*.md`, and Owner-approved decisions inside the V3-003 Decision Record. The Customer/Audit Contract and SEC-01 through SEC-05 are bounded design evidence; their complete contracts and specialist approvals remain pending.

یادداشت Metadata: بخش‌های `DEC-010..014` دارای عبارت تاریخی `Repository Recording: PENDING VERIFICATION` هستند، در حالی که Decision Record در Baseline فعلی داخل Git وجود دارد. Consolidated Security Manifest این مورد را Documentary metadata gap می‌داند؛ این Draft آن را Status یا Authority جدید تلقی نمی‌کند و Metadata منبع را اصلاح نمی‌کند.

Deployment Profile abbreviations: `ALL` = Shared SaaS + Dedicated Managed + Dedicated Sovereign; `SS` = Shared SaaS; `DM` = Dedicated Managed; `DS` = Dedicated Sovereign.

## 3. Analytical NFR register

### 3.1 Security and identity

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-SEC-001` | در هر service trust boundary، User و Workload identity باید authenticate شوند؛ internal network location به‌تنهایی Trust نیست و Missing/invalid required identity or authority evidence باید fail closed شود. | `architecture/standards/security.md` § Identity and authorization؛ ADR-V3-005 | `APPROVED_INVARIANT` | ALL | Identity Trust + receiving Service | Service-boundary authentication and invalid/missing-evidence denial matrix | `DESIGN_SOURCE_PRESENT; RUNTIME_NOT_VERIFIED; NT-001_NOT_EXECUTED` | OD-009..012؛ SR-CAND-001/002 | Identity/Platform Security + Security Architecture؛ Implementation/Security gate |
| `NFR-SEC-002` | Authentication، Tenant Membership، Entitlement و Resource/Action Authorization تصمیم‌های مستقل‌اند؛ Identity یا Session به‌تنهایی Business Authorization ایجاد نمی‌کند. | ADR-V3-005؛ `baseline-v3.md` § Platform Core / Trust | `APPROVED_INVARIANT` | ALL | Platform Core + resource-owning Domain | Direct-service authorization-denial matrix | `DESIGN_SOURCE_PRESENT; RUNTIME_NOT_VERIFIED` | OD-009..012؛ SR-CAND-005/006 | Domain owners + Security Architecture |
| `NFR-SEC-003` | Workload call به Identity احراز‌شده و Audience/Scope مناسب نیاز دارد؛ Transport peer identity یا Network location معادل `ProducerAuthority` نیست. | ADR-V3-005؛ SEC-01 § SD-01/SD-02؛ Technical Contract § E | `APPROVED_INVARIANT` | ALL | Workload trust / producer-consumer boundary | Authenticated producer-provenance and confused-deputy negative tests | `BOUNDED_OWNER_DESIGN_PRESENT; SPECIALIST_PENDING; NT-004/009_NOT_EXECUTED` | OD-011/012؛ SR-CAND-011/012 | Identity/Platform Security + Messaging/API Event Architecture + Security Architecture |
| `NFR-SEC-004` | Issuance، rotation، revocation، compromise recovery و receiving-boundary freshness برای Workload credentials باید در Contract مستقل تعیین شود. | Specialist Register `IP-01/IP-04`؛ SEC-01 § SD-01 | `UNRESOLVED` | ALL | Identity/Platform trust | Approved lifecycle model + revocation-transition tests | `DESIGN_DECISION_MISSING; IMPLEMENTATION_NOT_VERIFIED` | OD-011/012/015/023 | Identity/Platform Security؛ Final Security Design Sign-off |

**Candidate boundary — `NFR-SEC-001`:** Validation در non-service receiving boundaries، revoked-evidence freshness و credential/session lifecycle نهایی تحت `SR-CAND-001/002`، `IP-01/IP-04` و `OD-009..012` همچنان `PROPOSED` یا `UNRESOLVED` هستند و بخشی از این `APPROVED_INVARIANT` نیستند.

### 3.2 Tenant isolation and data protection

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-TEN-001` | Tenant Context فقط از authenticated, validated Membership یا trusted Workload provenance ایجاد شود؛ client-provided Tenant values فقط selector هستند. Context معتبر باید در synchronous calls، messages، jobs، logging و persistence transactions حفظ شود و Missing/conflicting/invalid Context پیش از Domain یا Persistence work fail closed شود. | `architecture/standards/security.md` § Tenant isolation؛ ADR-V3-003/005 | `APPROVED_INVARIANT` | ALL | Tenant Management + tenant-aware consuming capability | Context establishment/propagation and missing/conflicting/invalid-context denial tests | `DESIGN_SOURCE_PRESENT; RUNTIME_NOT_VERIFIED; NT-002_NOT_EXECUTED` | OD-011/014/020؛ SR-CAND-003/004 | Tenant Security + Identity/Platform Security |
| `NFR-TEN-002` | برای Tenant-owned data در Shared SaaS، Domain authorization و PostgreSQL RLS مکمل یکدیگرند؛ هیچ‌کدام جای دیگری را نمی‌گیرد. | ADR-V3-003/007؛ `persistence.md`؛ DEC-006 `TB-008` | `APPROVED_INVARIANT` | SS؛ منطقی در DM/DS حفظ می‌شود | Owning Service persistence boundary | Actual runtime-role read/write isolation matrix with multiple tenants | `DESIGN_SOURCE_PRESENT; RUNTIME_NOT_VERIFIED; NT-007_NOT_EXECUTED` | OD-013/014/020؛ SR-CAND-007/008 | Data Architecture + Tenant Security + service owner |
| `NFR-TEN-003` | Ordinary runtime database identity نباید protected table owner یا دارای `BYPASSRLS` باشد و transaction-local Tenant Context باید از operation دیگر نشت نکند. | ADR-V3-007؛ `persistence.md`؛ Specialist Register `TS-03` | `APPROVED_INVARIANT` | SS | Service-owned persistence | Real connection pool/role/policy verification and context-cleanup tests | `IMPLEMENTATION_EVIDENCE_NOT_VERIFIED; NEGATIVE_TEST_NOT_EXECUTED` | OD-013/014؛ SR-CAND-007/008 | Data Architecture + Tenant Security؛ Runtime Security gate |
| `NFR-TEN-004` | تعداد Tenant در Shared Cell، per-Tenant data scale و isolation-aware capacity envelope باید تعیین و اندازه‌گیری شود. | `open-decisions.md` `OD-023`; baseline § Risks | `UNRESOLVED` | SS | Product + Operations + service owners | Approved workload/capacity model and measured profile evidence | `NO_NUMERIC_TARGET; NO_RUNTIME_EVIDENCE` | OD-023 | Product + Operations + Security + service owners؛ before Production Architecture Sign-off |

**Candidate boundary — `NFR-TEN-001`:** Frequency بازاعتبارسنجی در هر boundary و enforcement mechanics ویژه هر boundary تحت `SR-CAND-003/004`، `TS-01/TS-02` و `OD-011/014/020` همچنان `PROPOSED` یا `UNRESOLVED` هستند؛ semantics مصوب establishment، preservation و fail-closed بدون تغییر باقی می‌مانند.

### 3.3 Authorization and auditability

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-AUT-001` | Resource-owning Domain تصمیم نهایی Resource/Action Authorization را می‌گیرد؛ Gateway، UI، IdP، Operator یا calling service جای آن نیست. | ADR-V3-005؛ baseline § Platform Core؛ DEC-007 `SR-CAND-005/006` | `APPROVED_INVARIANT` | ALL | Every resource-owning Domain | Direct-boundary denial and non-disclosing error matrix | `DESIGN_SOURCE_PRESENT; RUNTIME_NOT_VERIFIED; NT-003_NOT_EXECUTED` | OD-010/011؛ SR-CAND-005/006/016 | Domain owners + Security Architecture |
| `NFR-AUD-001` | Audit evidence باید append-oriented، traceably correctable، purpose-scoped و data-minimized باشد؛ Secret/credential/token یا Business Fact غیرضروری نباید صرفاً برای convenience ثبت شود. | DEC-010 Principles 3, 5, 6؛ `security.md` | `APPROVED_INVARIANT` | ALL | Audit Domain + producing Domains | Field allowlist/classification review and tamper/disclosure tests | `ARCHITECTURAL_PRINCIPLE_PRESENT; POLICY/IMPLEMENTATION_PENDING; NT-016..018_NOT_EXECUTED` | OD-019/023؛ SR-CAND-019/020 | Audit + Security + Data/Compliance authorities |
| `NFR-AUD-002` | برای CUS-CREATE/CUS-UPDATE موفق، authoritative Customer mutation و mandatory Audit publication obligation باید در Customer-owned consistency boundary به‌صورت consistent و durable ثبت شوند. | DEC-011/012/014؛ Technical Contract §§ B/C/I | `APPROVED_INVARIANT` | ALL | Customer Domain → Audit obligation boundary | Atomicity/crash-boundary design review and future executable tests | `OWNER_DECISION_PRESENT; IMPLEMENTATION_NOT_VERIFIED; TC-AC-001/002_NOT_EXECUTED` | OD-008/014/019؛ SR-CAND-019/020 | Customer/Audit/Operations + Security review |
| `NFR-AUD-003` | Confirmation موفق Audit باید از Audit-owned durable evidence، full `ObligationKey` و authenticated/authorized evidence exchange به دست آید؛ Broker ACK، DLQ یا quarantine success نیست. | Technical Contract § F؛ SEC-01 SD-04؛ Consolidated Manifest S3 | `PROPOSED` | ALL | Audit confirmation trust boundary | Authenticity, lookup authorization, replay/freshness and outage tests | `PREFERRED_CANDIDATE_ONLY; SPECIALIST_PENDING; NT-009/011/016_NOT_EXECUTED` | OD-008/011/012/014/019/020/023؛ SR-CAND-011/019 | Audit + Identity/Tenant Security + Contract Governance + Security Architecture |
| `NFR-AUD-004` | Audit retention، archive، legal hold، deletion، integrity cadence و recovery periods باید per category/jurisdiction/profile تعیین شوند. | DEC-010 Principles 8/10؛ `open-decisions.md` OD-019/023 | `UNRESOLVED` | ALL | Audit + Legal/Compliance + Operations | Approved policy hierarchy and profile-specific evidence | `POLICY_MISSING; NUMERIC_TARGETS_MISSING` | OD-019/023؛ SR-CAND-020 | Audit + Legal/Compliance + Security + Operations |

### 3.4 Reliability and resilience

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-REL-001` | Reliable event flow از transactional Outbox در producer-owned transaction و durable Inbox/equivalent idempotency evidence در consumer استفاده می‌کند؛ ACK فقط پس از durable processing مجاز است. | ADR-V3-007؛ `messaging.md`؛ DEC-009 | `APPROVED_INVARIANT` | ALL | Producing/consuming service boundaries | Crash-boundary، broker outage، duplicate and redelivery tests | `DESIGN_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED; NT-010_NOT_EXECUTED` | OD-008/019/020؛ SR-CAND-013/014 | Messaging/API Event Architecture + service owners |
| `NFR-REL-002` | Valid duplicate، malicious replay، forged provenance و delayed/out-of-order delivery distinct هستند؛ idempotency باید contract/operation-specific باشد. | DEC-009 Principles 1/2/6 | `APPROVED_INVARIANT` | ALL | Event contract + consumer | Contract-specific duplicate/replay/order scenario matrix | `OWNER_PRINCIPLE_PRESENT; DETAILED_POLICY_PENDING; NT-009..012_NOT_EXECUTED` | OD-008/020؛ SR-CAND-011..014 | Contract Governance + Messaging/API Event Architecture + Security |
| `NFR-REL-003` | End-to-end exactly-once و global ordering فرض نمی‌شوند؛ external effects، retry/re-drive، terminal failure و reconciliation به Policy مستقل نیاز دارند. | ADR-V3-007؛ DEC-009 Principles 5–7 | `APPROVED_INVARIANT` | ALL | Messaging + affected Domain | Failure/recovery model review and external-effect tests | `DESIGN_SOURCE_PRESENT; DETAILED_POLICY/IMPLEMENTATION_MISSING` | OD-008/019/020؛ SR-CAND-013/014 | Messaging/API Event Architecture + Domain/Operations |

### 3.5 Availability and recoverability

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-AVL-001` | Install، upgrade، rollback، backup/restore، observability، security operation و recovery باید برای هر Deployment Profile مستقلاً قابل اثبات باشند. | ADR-V3-010/012؛ baseline § Operations | `APPROVED_INVARIANT` | ALL، جداگانه | Operational Platform + each service/profile | Profile-specific acceptance evidence | `ARCHITECTURE_ONLY; PROFILE_RUNTIME_EVIDENCE_MISSING` | OD-015/023 | Operations + Security + service owners؛ Production Readiness gate |
| `NFR-AVL-002` | Availability SLO، RTO، RPO، MTD و acceptable degradation/deferral duration باید per service/profile تعیین شوند؛ هیچ عددی فعلاً مصوب نیست. | OD-023؛ DEC-010/014 Explicit Non-approvals | `UNRESOLVED` | ALL | Product + Operations + Security + service owners | Approved objective/measurement matrix and observed evidence | `NO_APPROVED_NUMERIC_TARGET` | OD-023 | Existing milestone: before Production Architecture Sign-off |
| `NFR-REC-001` | Recovery باید ownership، contract compatibility، Tenant isolation، Auditability و Sovereign-local authority را حفظ کند؛ recovery evidence با Architecture intent یکسان نیست. | ADR-V3-004/008/010/012 | `APPROVED_INVARIANT` | ALL | Service + Operational Platform | Restore/reconcile/rollback evidence per profile | `ARCHITECTURE_SOURCE_PRESENT; RUNTIME_NOT_VERIFIED` | OD-001/008/015/023 | Operations + Security + service owners |
| `NFR-REC-002` | `RECOVERY_COMPLETED`، `ELIGIBILITY_GATES_REESTABLISHED` و `RESTORATION_AUTHORIZED` milestoneهای جدا هستند؛ recovery به‌تنهایی restoration را مجاز نمی‌کند. | SEC-04 ME-05؛ SEC-05 SL-05؛ DEC-014 | `PROPOSED` | ALL | Operations + future Eligibility Policy Authority | Authorized restoration workflow and evidence-chain review | `BOUNDED_OWNER_DISPOSITION; POLICY_AUTHORITY_NOT_ASSIGNED; NOT_EXECUTED` | OD-015/019/023 | Operational Policy + Eligibility Policy Authority + Security Architecture |

### 3.6 Observability and monitoring

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-OBS-001` | Services نیازمند structured logs، metrics، distributed tracing و safe correlation هستند؛ Sensitive data، credential و token نباید افشا شود. | baseline § Operations؛ `security.md`; `configuration.md` | `APPROVED_INVARIANT` | ALL | Each service + Operational Platform | Schema/redaction review and profile-specific telemetry evidence | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED` | OD-023؛ SR-CAND-019 | Service owners + Operations + Security |
| `NFR-OBS-002` | Monitoring projection derived evidence است؛ missing/untrusted coverage باید `UNKNOWN`/incomplete باقی بماند و `UNKNOWN` eligibility یا restoration را اثبات نمی‌کند. | SEC-04 ME-01..05؛ DEC-014 Principle 3 | `PROPOSED` | ALL | Monitoring/Operations + evidence owners | Coverage/checkpoint provenance and false-zero-backlog negative tests | `BOUNDED_OWNER_DISPOSITION; SPECIALIST/POLICY_PENDING; NT-013/016_NOT_EXECUTED` | OD-015/019/023 | Operational Policy + Security Architecture + Eligibility Policy Authority |
| `NFR-OBS-003` | Freshness windows، coverage thresholds، alert/escalation deadlines، cardinality، retention و sampling باید تصویب شوند. | SEC-04 §§ C/I؛ OD-023 | `UNRESOLVED` | ALL | Operations + affected Domain/Security | Approved measurement policy and profile evidence | `NO_NUMERIC_POLICY; NO_RUNTIME_EVIDENCE` | OD-023 | Operations + Security + service owners |

### 3.7 Performance, capacity and scalability

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-PERF-001` | p95/p99 latency، throughput، event-processing latency، queue delay و critical-operation performance budgets باید per operation/profile تعیین شوند. | OD-023؛ V3-003 DEC-001 non-approval of numeric NFRs | `UNRESOLVED` | ALL | Product + service owners + Operations | Approved workload model and measured percentile evidence | `NO_APPROVED_NUMERIC_TARGET` | OD-023 | Product + Operations + Security + service owners |
| `NFR-CAP-001` | Tenant/user/session/request/data-growth، queue/backlog و recovery capacity targets باید بر مبنای Business evidence و Deployment Profile تصویب شوند. | OD-023؛ baseline § Risks | `UNRESOLVED` | ALL | Product + Operations + service owners | Capacity model, load/recovery evidence and saturation criteria | `NO_APPROVED_NUMERIC_TARGET` | OD-023 | Product + Operations + Security + service owners |
| `NFR-SCL-001` | Scale و placement نباید Tenant identity، domain ownership، authorization، contract semantics یا service independence را تغییر دهد. | ADR-V3-001/002/003/011 | `APPROVED_INVARIANT` | ALL | Cells + services | Placement/migration and scale-boundary design/runtime evidence | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED` | OD-015/022/023 | Architecture + Operations + service owners |

### 3.8 Data integrity and consistency

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-DAT-001` | هر Service مالک data، schema/migration، credential و transaction boundary خود است؛ cross-service SQL، shared ORM/entity و private-database access ممنوع است. | ADR-V3-002/007؛ `service-architecture.md`; `persistence.md` | `APPROVED_INVARIANT` | ALL | Every service persistence boundary | Dependency/DB-role/topology evidence and access-denial tests | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED; NT-006_NOT_EXECUTED` | OD-013/014/020؛ SR-CAND-007 | Service/Data owners + Security |
| `NFR-DAT-002` | Retry، re-drive و recovery باید full immutable `ObligationKey`، version و original committed semantic content را حفظ کنند؛ `MutationId` obligation identity نیست. | Technical Contract §§ C/G/H؛ SEC-02 SI-01/SI-05 | `APPROVED_INVARIANT` | ALL | Customer/Audit/Messaging contract | Same-key/content/conflict and recovery-integrity tests | `BOUNDED_OWNER_DESIGN_PRESENT; SPECIALIST_PENDING; NT-010..012_NOT_EXECUTED` | OD-008/014/020؛ SR-CAND-013/014/019 | Contract Governance + Messaging/API Event Architecture + Security Architecture |
| `NFR-DAT-003` | Original Audit evidence نباید بدون traceability silently overwrite شود؛ در Customer/Audit durable-delivery scope، Customer-owned original obligation evidence و Audit-owned confirmation/disposition/conflict evidence باید authority و provenance جداگانه خود را حفظ کنند و correction/reconciliation باید رابطه با original evidence را نگه دارد. | V3-003-DEC-010 Principle 3؛ Technical Contract §§ B/H؛ SEC-02 SI-04/SI-05 | `APPROVED_INVARIANT` | ALL | Customer Domain ↔ Audit Domain | Audit correction and Customer/Audit conflict/reconciliation evidence review | `ARCHITECTURAL/BOUNDED_OWNER_DESIGN_PRESENT; SPECIALIST/POLICY_PENDING` | OD-008/019/020؛ SR-CAND-019/020 | Customer/Audit + Contract Governance + Security/Operations |

**Candidate boundary — `NFR-DAT-003`:** تعمیم منع overwrite به authoritative facts همه Domainهای دیگر `UNRESOLVED` است و به تأیید Domain owner مربوط به‌همراه Architecture/Security نیاز دارد؛ این تعمیم بخشی از این `APPROVED_INVARIANT` نیست.

### 3.9 Contract compatibility and versioning

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-CON-001` | Public/internal API و Event contractها explicit، owned و versioned هستند؛ breaking change نیازمند version جدید، coexistence، deprecation و consumer migration است. | ADR-V3-008؛ `api-design.md`; `messaging.md` | `APPROVED_INVARIANT` | ALL | Contract owner + consumers | Compatibility/consumer inventory and profile-skew tests | `ARCHITECTURE_SOURCE_PRESENT; TOOLING/IMPLEMENTATION_PENDING` | OD-007/008/020 | Contract Governance + Messaging/API Event Architecture |
| `NFR-CON-002` | Semantic equality برای Audit obligation باید deterministic، typed و version-bound باشد و از incidental wire serialization مستقل بماند. | SEC-02 SI-01/SI-02/SI-03 | `APPROVED_INVARIANT` | ALL | Customer/Audit semantic contract | Cross-serializer/canonicalization conformance and downgrade tests | `PROJECT/DOMAIN_BOUNDED_APPROVAL; SPECIALIST_PENDING; NOT_EXECUTED` | OD-008/020 | Contract Governance + Messaging/API Event Architecture + Security Architecture |
| `NFR-CON-003` | Canonical field set، absent/null/default، Unicode، numeric/timestamp، unknown-field، digest/signature و supported-version matrix هنوز باید تصویب شوند. | SEC-02 §§ C/D/I/J | `UNRESOLVED` | ALL | Contract Governance + Security | Normative semantic specification and conformance suite | `DESIGN_DECISION_MISSING; TEST_NOT_EXECUTED` | OD-008/020 | Contract Governance + Messaging/API Event Architecture + Security Architecture |

### 3.10 Operational control and privileged access

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-OPS-001` | Privileged operation به Identity محدود، Tenant/Platform scope صریح، destination-Domain authorization و durable Audit نیاز دارد؛ generic admin authority کافی نیست. | baseline § Operational Platform؛ DEC-010 Principle 4؛ SEC-03 PR-01/02 | `APPROVED_INVARIANT` | ALL | Operational Platform → destination Domain | Privileged action/SoD/revocation/denial matrix | `ARCHITECTURE_AND_BOUNDED_OWNER_SOURCE; POLICY/RUNTIME_PENDING; NT-013_NOT_EXECUTED` | OD-011/012/015/023؛ SR-CAND-015/016 | Operational Policy + Domain owners + Security Architecture |
| `NFR-OPS-002` | Build/release artifact باید reproducible، versioned و integrity-verifiable باشد و promotion/deployment authority per profile حفظ شود. | ADR-V3-010؛ baseline § Operations؛ DEC-006 `AB-021/TB-024/025` | `APPROVED_INVARIANT` | ALL | Supply chain + profile-local release authority | Provenance/signing/promotion/rollback evidence | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED; NT-021_NOT_EXECUTED` | OD-002..004/015/020 | Release/Supply-Chain Security + service owners |
| `NFR-OPS-003` | Operations Standard، Privileged Action Catalog، quarantine/re-drive policy، incident/escalation و restoration governance باید به‌صورت standalone تصویب شوند. | Consolidated Manifest § G؛ Specialist Register `OP-01..05` | `UNRESOLVED` | ALL | Operational Policy Governance | Authenticated policy approval and traceable operational acceptance criteria | `STANDARD_MISSING; AUTHORITY_UNASSIGNED; NOT_SUBMITTED` | OD-008/015/019/023 | Operational Policy Governance + Security Architecture + Eligibility Policy Authority where applicable |

### 3.11 Sovereign-local continuity and disconnected operation

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-SOV-001` | Dedicated Sovereign دارای final local security/operational authority است و critical local operation نباید به synchronous Central availability یا implicit Central administration وابسته باشد. | ADR-V3-004؛ DEC-009 Principle 8؛ DEC-010 Principle 9 | `APPROVED_INVARIANT` | DS | Sovereign-local Control/Data Plane | Central-loss and unauthorized-Central-action denial evidence | `ARCHITECTURE_SOURCE_PRESENT; PROFILE_RUNTIME_NOT_VERIFIED; NT-019/020_NOT_EXECUTED` | OD-001/011/012/015/023؛ SR-CAND-021..024 | Sovereign-specific Security + Operations + Security Architecture |
| `NFR-SOV-002` | Reconnection conflict باید هر دو evidence view و provenance را حفظ کند؛ automatic Central-wins، Local-wins یا Last-writer-wins مجاز نیست. | SEC-05 SL-04؛ Technical Contract § H | `APPROVED_INVARIANT` | DS | Sovereign federation/reconciliation | Conflict-preserving reconnect and authorization tests | `BOUNDED_OWNER_APPROVAL; SPECIALIST/RUNTIME_PENDING` | OD-001/008/020/023؛ SR-CAND-021..024 | Sovereign-specific Security + Contract/Messaging + Security Architecture |
| `NFR-SOV-003` | Full Air-Gap scope، disconnected duration، local capacity، federation data classes و reconciliation policy هنوز تعیین نشده‌اند. | ADR-V3-003/004؛ OD-001/023؛ SEC-05 | `UNRESOLVED` | DS | Sovereign Operations/Security | Approved Critical Local Operation Catalog and profile evidence | `POLICY/TARGETS_MISSING` | OD-001/015/023؛ SR-CAND-023/024 | Sovereign-specific Security + Product/Operations + affected Domains |

### 3.12 Maintainability, evolvability and user experience

| ID | Requirement or constraint | Exact source | Classification | Profile | Boundary/owner | Verification approach | Current evidence | OD / SR-CAND | Required authority / future gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NFR-MNT-001` | هر Business Service باید independent build/test boundary، version، artifact، deployment و lifecycle داشته باشد؛ Release آن نباید rebuild Service دیگر را الزام کند. | ADR-V3-001/011؛ baseline § Principles | `APPROVED_INVARIANT` | ALL | Every Business Service | Repository/build/release boundary evidence | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED` | OD-002..004/015/020 | Architecture + service/release owners |
| `NFR-MNT-002` | Domain logic باید infrastructure-independent و Hexagonal باشد؛ cross-service implementation import و shared business framework ممنوع است. | ADR-V3-001/002؛ `service-architecture.md` | `APPROVED_INVARIANT` | ALL | Service code boundary | Dependency-direction review and future boundary enforcement | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED` | OD-004/020 | Architecture + service owners |
| `NFR-MNT-003` | Co-deployment فقط با حفظ ownership، contract، authorization، data boundary و extraction readiness مجاز است؛ Co-location به معنی shared database/authority نیست. | ADR-V3-011 | `APPROVED_INVARIANT` | ALL | Logical capability/deployment boundary | Independent artifact/release and forbidden-dependency evidence | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED` | OD-015/020 | Architecture + Operations + service owners |
| `NFR-UX-001` | Frontend باید Persian، RTL، responsive behavior و accessibility را پشتیبانی کند؛ client permission checks فقط UX هستند. | ADR-V3-009؛ baseline § Frontend integration | `APPROVED_INVARIANT` | ALL | Frontend + Design System + backend authorization | Accessibility/RTL/responsive and backend-denial evidence | `ARCHITECTURE_SOURCE_PRESENT; IMPLEMENTATION_NOT_VERIFIED` | OD-005..007/010/023 | Product/Frontend + Domain owners؛ Implementation/Production gates |

## 4. Quantitative decision register

هیچ Numeric NFR در این Draft Approved نیست. موارد زیر همگی `UNRESOLVED` و وابسته به `OD-023` هستند:

| Metric family | Missing business/operational input | Required approval | Existing milestone |
| --- | --- | --- | --- |
| Tenant per Shared Cell، User، Concurrent Session | segmentation، adoption، peak behavior، isolation margin | Product + Operations + Security + service owners | Before Production Architecture Sign-off |
| RPS، peak throughput، data volume/growth | Journey mix، seasonality، retention، import/export workload | Product + service owners + Operations | Before Production Architecture Sign-off |
| p95/p99 latency | Critical operation list، user-impact boundary، measurement point/profile | Product + Domain owners + Operations | Before Production Architecture Sign-off |
| Availability SLO | Business interruption tolerance and dependency model | Product + Operations + Security | Before Production Architecture Sign-off |
| RTO/RPO/MTD | Data-loss/business-impact evidence and recovery profile | Product + Operations + Domain/Security | Before Production Architecture Sign-off |
| Event rate/latency، queue/backlog capacity | contract workload، burst/retry/re-drive behavior | Messaging/API Architecture + Operations + Domains | Before Production Architecture Sign-off |
| Sovereign disconnected capacity/duration | Critical Local Operation Catalog، local resource and support model | Sovereign Operations/Security + Product | Before Production Architecture Sign-off |

`OD-023 = OPEN`. Analytical documentation، Architecture approval یا bounded Owner principle نباید عددی را به‌عنوان Approved جایگزین این Decision کند.

## 5. Specialist and evidence dependencies

۳۶ Specialist disposition در Tracking Register همگی `NOT_SUBMITTED`، Reviewerها `UNASSIGNED` و Authenticated dispositionها `NOT_RECEIVED` هستند. این Draft آن‌ها را تکمیل یا Approved نمی‌کند. مهم‌ترین dependencyها:

- Identity/Platform Security: `IP-01..05`؛
- Tenant Security: `TS-01..05`؛
- Sovereign-specific Security: `SS-01..05`؛
- Contract Governance و Messaging/API Event Architecture: ده disposition مستقل `CG-01..05`؛
- Operational Policy Governance: `OP-01..05`؛
- Security Architecture: `SA-01..06`؛
- Independent Security Reviewer: `NOT_SIGNED_OFF`؛
- Eligibility Policy Authority: `NOT_YET_ASSIGNED / DEFERRED`.

## 6. Explicit non-approvals and preserved status

این Draft:

- Analytical Closure Contract یا Mandatory بودن این Deliverable را تصویب نمی‌کند؛
- هیچ Numeric NFR، Security exception، Risk rating یا Risk acceptance را تصویب نمی‌کند؛
- هیچ Technology، Protocol، Schema، API/Event Contract، IdP، cryptography، retention یا operational mechanism را انتخاب نمی‌کند؛
- هیچ Specialist disposition، Security Requirement Candidate یا Open Decision را تصویب یا نمی‌بندد؛
- Logical design sufficiency را با verified runtime performance/security یکسان نمی‌گیرد؛
- هیچ Build، Test، Validator، Runtime verification یا Production evidence ثبت نمی‌کند.

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
PRODUCTION_READINESS = NOT ESTABLISHED
```
