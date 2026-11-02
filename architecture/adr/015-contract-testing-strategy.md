# ADR-V3-015: Risk-based contract testing strategy

- Status: ACCEPTED
- Authoring task: OD-020 governance package
- Related decision/open decision: DEC-015 / OD-020
- Decision owner: API/Event Architecture + Quality Authority
- Required approval authority: Technical Architecture Owner + Quality Authority
- Technical Architecture Owner disposition: APPROVED — COMPLETE ADR CONTENT
- Quality Authority disposition: APPROVED — SCOPED INTERIM QUALITY AUTHORITY; DUAL ROLE DISCLOSED
- Additional substantive provisions disposition: APPROVED — CONSOLIDATED OWNER DISPOSITION
- Approval provenance: Explicit CPO / Technical Architecture Owner OD-020 finalization direction; separate Quality review recorded against SHA-256 `387954415AFF1F470170236A28825CD09B16FA6D309F2F9975B753461636F2FA`
- Effective date: Upon traceable Level 2 commit of the synchronized decision package
- Architecture revision: `NESHANE-V3-ARCH-P00-005` upon traceable commit
- Supersedes: None
- Superseded by: None

## Approval boundary

The Technical Architecture Owner has completely approved these five architectural choices:

1. risk-based Consumer-driven Contract Testing;
2. Provider Conformance before Merge and before Release;
3. risk-based Real Integration Testing;
4. Service Owner ownership of each contract baseline with an auditable change trail; and
5. limited, documented and time-bound exceptions.

Those choices do not require repeated approval while their meaning remains unchanged. The
Technical Architecture Owner has now also explicitly approved the complete supplementary content
of this ADR. The separately recorded scoped Quality Authority review approves the applicable
testing policy, evidence, risk, baseline and exception provisions.

The consolidated Technical Architecture Owner disposition also approves these additional
substantive provisions without reopening the five choices:

- the complete eight-layer hybrid control model, including mandatory schema/specification,
  compatibility and negative-regression controls;
- the exact risk triggers, evidence thresholds and re-execution rules for Consumer-driven and Real
  Integration Testing;
- the detailed Provider Conformance coverage and controlled-substitute boundary;
- the minimum Audit Trail fields and responsibility allocation;
- the exact blocking CI/Merge/Release evidence rules and Manual Review routing;
- the Quality Authority operating responsibilities and Quality exception approval path; and
- the detailed non-waivable Security boundaries, exception prohibitions and closure conditions.

The Quality Authority disposition is recorded separately in
[OD-020 Quality Authority review and approval](../reviews/OD-020-quality-approval.md). The dual
role is disclosed and does not satisfy any independent Security Authority or Level 3/4 gate.

## Context and scope

Neshane V3 services own their contracts and can build, release and upgrade independently. Static
schema validity alone cannot prove that a Provider behaves according to its published contract or
that an existing Consumer's semantic expectations remain satisfied.

ADR-V3-008 requires contract-first controlled compatibility. ADR-V3-014 establishes the REST and
event versioning rules. The accepted V3-011 HTTP and V3-012 Event engineering baselines provide
bounded local validation and conservative compatibility tooling, but explicitly do not provide CI
evidence, universal compatibility proof, runtime security assurance or Production Readiness.

This proposal covers published HTTP and Event contracts, their Providers and known Consumers. It
does not select a testing product, CI provider, schema registry, broker topology or runtime
delivery implementation.

## Proposed decision

Neshane V3 uses a hybrid, risk-based Contract Testing model consisting of complementary controls:

1. Schema and Specification Validation;
2. Static Compatibility Verification;
3. Automated Negative Regression Testing;
4. Provider Conformance Testing;
5. risk-based Consumer-driven Contract Testing;
6. risk-based Real Integration Testing;
7. Semantic and Security Review where applicable; and
8. blocking CI and Release Gates.

No individual layer, and no architecture acceptance of this strategy, proves complete operational
compatibility, runtime security or Production Readiness.

### Common contract controls

- Every published HTTP or Event contract has a stable identity, version, accountable Service
  Owner and accepted comparison baseline.
- HTTP validation uses OpenAPI 3.1 and the bounded V3-011 conventions. Event validation uses the
  CloudEvents 1.0-compatible envelope, JSON Schema Draft 2020-12 and bounded V3-012 conventions.
- Contract changes run specification/schema validation, directional compatibility analysis and
  negative regression tests as blocking CI controls.
- Unsupported or uncertain constructs must fail closed in automated acceptance or be routed to a
  recorded Manual Review. Lack of an automated breaking-change finding is not compatibility proof.
- Accepted baselines remain immutable evidence and are never rewritten merely to make an
  incompatible candidate pass.

### Provider Conformance

- A change affecting a published contract or Provider behavior requires Provider Conformance
  before Merge.
- Before Release, the final traceable Provider artifact or revision must be shown to conform to
  the contract revision being released.
- Conformance exercises the real contract-producing or contract-processing implementation path,
  including applicable request/response or event payload shapes, status and error behavior,
  required fields, validation rules, media type and version behavior.
- Validating only the OpenAPI document or JSON Schema is not Provider Conformance.
- An isolated environment with controlled substitutes is permitted when the actual contract path
  is exercised and its limitations are recorded.

### Risk-based Consumer-driven Contract Testing

Consumer-driven testing is not universally mandatory. It is required when the approved risk
classification identifies one or more of these conditions:

- security-sensitive identity, authentication or authorization interaction;
- behavioral or semantic dependency not covered by schema validation;
- business- or operations-critical Consumer;
- independently deployed Provider and Consumer versions with material compatibility exposure; or
- known Consumers relying on specific behavioral assumptions.

The Consumer Owner records testable expectations. The Provider Owner produces evidence that the
implementation satisfies applicable expectations. This ADR does not mandate Pact or another
specific tool.

### Risk-based Real Integration Testing

Real Integration Testing is required for approved critical paths and changes with material
integration risk. Candidate scopes include security-sensitive identity/access paths,
business-critical service interactions and behavior dependent on real infrastructure.

For HTTP this may include real service-to-service communication and selected network behavior. For
Events it may include a real broker, duplicate delivery, retry, DLQ, ordering and recovery
scenarios. Each executable task must state which components were real, simulated or absent.
OD-020 does not establish RabbitMQ delivery semantics, Outbox/Inbox correctness or recovery policy.
The Quality Authority must approve and maintain the critical-path inventory, risk-classification
criteria and mandatory re-execution triggers.

### Baseline ownership and audit trail

The Service Owner owns its contract and accepted baseline. A baseline change requires explicit
Service Owner approval and an Audit Trail containing at least:

- contract identity and version;
- previous and candidate revisions;
- reason for change;
- compatibility-verification result;
- approving authority and recorded approval time;
- migration or deprecation plan where applicable; and
- references to evidence and Manual Review decisions.

Service Owner approval does not replace required Quality or Security approval.

### Blocking CI, Merge and Release gates

- Before Merge, applicable schema/specification validation, compatibility diff, negative
  regression and Provider Conformance gates are blocking.
- Consumer-driven and Real Integration gates are blocking when the approved risk classification
  makes them applicable.
- Before Release, every applicable gate runs against the traceable final artifact or revision.
- Release evidence records test results, artifact identity, contract/baseline revisions, affected
  Consumer status, Manual Review decisions and active exceptions.
- Local tooling or local test execution is not CI evidence. Until a real CI run produces traceable
  evidence, CI approval remains unavailable.

### Manual Review and security boundaries

Manual Review is mandatory for unsupported automated constructs and for semantic changes that
cannot be proved by structural comparison. Authentication, authorization, Tenant Context and
isolation, workload/producer trust, idempotency/delivery semantics, ordering, error semantics,
business meaning/defaults, data classification and sensitive-data exposure retain their
applicable Security Review.

Contract Testing must not weaken RLS, token validation, Tenant Context validation, domain-owned
authorization, workload identity, producer validation or other accepted security boundaries.
Tenant or producer metadata remains provenance and never confers access authority.

### Limited and time-bound exceptions

An exception is permitted only for a bounded non-critical gate and records its reason, exact
scope, owner, approval authority, expiry, compensating controls and remediation plan.

- Quality-related exceptions require the Quality Authority and affected Service Owner.
- Security-impacting exceptions require the independent Security/Risk Acceptance path.
- An exception never converts a failed test to PASS; the test result and exception disposition
  remain separate evidence.
- Incompatible change without approved migration/coexistence, mandatory security-control bypass
  and sensitive-data exposure cannot use the ordinary exception path.

## Responsibilities requiring final approval

| Role | Proposed responsibility |
| --- | --- |
| Service Owner | Contract/baseline ownership, baseline approval, migration and deprecation evidence |
| Provider Team | Provider implementation and Provider Conformance evidence |
| Consumer Owner | Testable Consumer expectations and Consumer-driven evidence |
| Platform Team | Shared tooling, CI gates and isolated test infrastructure |
| Quality Authority | Risk policy, critical-path inventory, acceptance evidence and Quality exceptions |
| Security Architecture | Review of security-sensitive semantic changes and protection of trust boundaries |

## Alternatives and rationale

- **Schema validation alone:** rejected because it cannot prove Provider behavior or Consumer
  semantic compatibility.
- **Static compatibility analysis alone:** rejected because supported syntax is necessarily
  bounded and runtime behavior remains untested.
- **Consumer-driven testing for every interaction:** rejected because its cost is disproportionate
  for low-risk interactions; the approved principle is risk-based application.
- **Real integration testing for every change:** rejected because environment and maintenance cost
  would undermine service independence; critical paths and material-risk changes remain covered.
- **Uncontrolled Service Owner baseline replacement:** rejected because it destroys reproducible
  evidence and can conceal incompatibility.
- **Permanent or implicit waivers:** rejected because they evade the blocking evidence model.

The hybrid model combines inexpensive structural controls with targeted behavioral and real
integration evidence while keeping cost proportional to risk.

## Consequences

- Contract changes gain earlier, layered incompatibility detection and auditable release evidence.
- Provider, Consumer and integration tests create maintenance and environment cost.
- Service Owners must maintain consumer and baseline evidence; Quality must maintain risk policy.
- CI and Release pipelines need independently implemented gates before CI evidence exists.
- Security-sensitive semantics cannot be approved solely through schema or compatibility results.

## Compatibility and consumer impact

V3-011 and V3-012 remain the accepted engineering baselines for their bounded HTTP and Event
validators and comparison rules. Their documented unsupported OpenAPI/JSON Schema constructs
remain Manual Review cases. This proposal neither changes their executable contracts nor upgrades
their local evidence into CI evidence.

ADR-V3-014 continues to govern versioning, coexistence, consumer inventory, migration ownership
and retirement evidence. OD-007 remains open for the public REST/GraphQL/hybrid strategy. OD-019
and runtime messaging decisions remain outside this proposal.

## Migration and rollback/forward recovery

No executable migration is authorized by this proposal. Implementation tasks must add CI gates,
Provider Conformance, risk-classification records, Consumer-driven tests and Real Integration
tests without rewriting accepted V3-011/V3-012 baselines. A failed candidate is reverted or
advanced through the approved new-major/coexistence path; the accepted comparison baseline and
failure evidence remain traceable.

## Verification expectations and evidence gate

Architecture acceptance and executable evidence are separate:

- **Architecture acceptance** requires explicit final approval of this ADR by the Technical
  Architecture Owner and Quality Authority, synchronized governance records and a traceable Level
  2 commit.
- **Runtime/CI evidence** requires actual Provider, Consumer and integration test execution in the
  applicable environment against a traceable artifact/revision.
- **Security evidence** requires the applicable Security Review and tests for security-sensitive
  semantics.
- **Release evidence** requires all applicable blocking gates, Manual Reviews and valid exceptions.

No unexecuted test, proposed CI workflow or architecture approval may be reported as PASS,
Security Sign-off or Production Readiness.

## Approval completion and activation boundary

The required architecture and Quality dispositions are complete:

1. the Technical Architecture Owner approved the five choices and complete supplementary content;
2. the scoped Quality Authority approved the hybrid model, responsibilities, risk policy,
   critical-path governance, baseline management and exception policy;
3. ADR-V3-015 and DEC-015 are accepted and governance references are synchronized; and
4. OD-020 is closed as approved, becoming effective only through the traceable Level 2 commit.

Closure would establish the architecture strategy only. It would not prove CI implementation,
Provider/Consumer/Integration execution, runtime compatibility, Security Sign-off or Production
Readiness.

## Traceability

Related records: OD-020; DEC-015; ADR-V3-002; ADR-V3-007; ADR-V3-008;
ADR-V3-012; ADR-V3-014; the accepted [Contract Change Protocol](../contract-change-protocol.md);
[API design standard](../standards/api-design.md); [messaging standard](../standards/messaging.md);
Backend V3-011 HTTP Contract Engineering Baseline; Backend V3-012 Event Contract Engineering
Baseline; [Quality Authority review](../reviews/OD-020-quality-approval.md); OD-007; OD-019.
