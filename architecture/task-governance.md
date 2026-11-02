# Neshane V3 proportionate task governance

## Document control

| Field | Value |
| --- | --- |
| Status | `APPROVED — PROJECT GOVERNANCE` |
| Authorizing task | `V3-003` |
| Requesting authority | `CPO` |
| Scope | Project-level development, documentation, architecture, security-decision and production-release approval routing |
| Governance baseline label | `NESHANE-V3-GOV-P00-000A` unchanged; no new label was authorized by this task |
| Narrow amendment | `V3-004` CPO direction: documentation-only R0 Design Consistency Acceptance route |
| Level 2 protocol amendment | `ACCEPTED — V3-006 R0`; CPO/Technical Architecture Owner direction: general project architecture ownership and proportionate decision workflow |
| Development execution amendment | `ACCEPTED — V3-005`; controlled local build/test execution under explicit Task scope |
| Development-first amendment | `APPROVED — V3-010`; routine local implementation, trusted dependency resolution and isolated Docker development no longer require repeated approval |
| V3-006 task status | `CLOSED — ADR AND CONTRACT CHANGE GOVERNANCE BASELINE` |

## Authority basis and evidence boundary

The Root Workspace owns cross-repository architecture and review policy. Existing Root records accept explicit Project Owner decisions as project authority and do not require a corporate identity certificate, delegation matrix, organizational digital signature or independent reviewer signature for ordinary task acceptance. No independently authoritative corporate policy, contract or external requirement imposing those artifacts on development/documentation task closure is present in this repository.

The CPO direction recorded under `TASK_ID = V3-003` therefore authorizes this narrow project-governance change. It does not create, replace or override corporate policy and must not be cited as evidence of a corporate appointment, delegation or signature.

## Approval levels

### LEVEL 1 — DEVELOPMENT / DOCUMENTATION TASK

The designated Task Owner or CPO may accept and close an ordinary development or documentation task when all of the following are present:

1. an explicit Task ID and bounded scope;
2. explicit in-repository acknowledgment by the Task Owner or CPO;
3. referenced deliverables and evidence;
4. evaluated acceptance criteria;
5. a traceable Git change recording the decision and status;
6. explicit preservation of every higher-level gate that remains applicable.

A separate corporate identity certificate, delegation matrix or organizational digital signature is not required by default. A task-specific rule, independently authoritative corporate policy, contract, regulatory requirement or higher-level gate may still require stronger evidence.

#### Development-first local execution

The CPO/Technical Architecture Owner approves a prospective development-first workflow for explicitly identified development Tasks. Routine implementation evidence is produced through bounded local execution and does not require a new approval for each build, test, trusted dependency resolution, local service run, Docker smoke test, debugging cycle or defect fix.

The ordinary workflow is:

```text
TASK ASSIGNED -> IMPLEMENT -> BUILD AND TEST -> FIX FAILURES -> REVIEW EVIDENCE -> COMMIT -> CLOSE
```

R0 or R1 remains a distinct step only when the Task's actual acceptance criteria require it. A local commit is made only when the Task explicitly authorizes committing; push, publishing, deployment and release remain separate actions.

For an explicitly identified development Task, Codex may by default:

1. create and edit in-scope code, tests, configuration, build files, templates and development documentation;
2. run the repository's Java, Gradle, Node.js and other approved local development tooling;
3. run and repeat unit, integration, architecture, contract, formatting, static-analysis and smoke tests;
4. debug and fix implementation defects discovered by those checks;
5. resolve pinned or controlled dependencies and plugins from repository-declared approved official registries; and
6. build, run and stop Task-owned local services, Docker images/containers and disposable test infrastructure.

Dependency acquisition uses HTTPS with normal certificate validation, controlled versions, and dependency verification/locking where supported. Maven Central and the Gradle Plugin Portal are approved for the accepted Backend toolchain. Other official registries must be explicitly declared in repository configuration or an approved Task/toolchain decision. Untrusted mirrors, arbitrary executable installation scripts, disabled integrity checks and unrelated software installation remain prohibited. Material dependency changes are recorded and reviewed.

Local Docker and service execution uses development-only resources: trusted base images with approved provenance/integrity controls, localhost port binding by default, non-root containers where practical, no production credentials/customer data, no privileged mode or host networking by default, no sensitive host/Docker-socket mounts, bounded resource use, and cleanup limited to disposable resources created by the Task. Local databases, brokers, caches and fixtures follow the same isolation rules.

This policy does not authorize destructive operations against non-disposable resources, remote infrastructure mutation, production access, publishing, CI/CD, Git push, deployment or release. It never establishes Security Sign-off, risk acceptance, runtime assurance for another profile or Production Readiness.

### LEVEL 2 — ARCHITECTURE DECISION

Material architecture decisions require approval by the designated architecture authority under the existing ADR and Open Decision process. A Level 1 task acceptance cannot approve or close an ADR or Open Decision unless that architecture process is expressly completed.

#### Project Technical Architecture Owner designation

Under `V3-006`, the user explicitly declares the following project roles:

```text
TECHNICAL_ARCHITECTURE_OWNER = CPO (dual project role)
DESIGNATION_SCOPE = Neshane V3 project architecture and Level 2 architecture decisions
DESIGNATION_SOURCE = Explicit CPO and Technical Architecture Owner declaration in V3-006
```

The existing project governance contains no separation-of-duties rule that prohibits this dual role for Level 2 architecture decisions. The designation is therefore valid as a project authority record; it is not a corporate credential, legal appointment, independent review or security sign-off.

Within Level 2, the Technical Architecture Owner is the final architecture approval authority for Java/build toolchains, Backend and Frontend engineering conventions, service and module architecture, API and event architecture, and data architecture. Affected domain, engineering, operations, developer-experience and product owners provide evidence and consequences proportional to impact. When an existing decision or security control explicitly requires another approval, specialist review or separation of duties, that requirement remains in force.

This designation does not authorize Independent Security Sign-off, security-critical risk acceptance, privileged-operation exceptions, executable `DURABLE_DEFER`, verification of runtime controls or Production Release. Those decisions remain at Level 3 or Level 4 as applicable.

#### OD-020 interim Quality Authority designation

For the current Neshane V3 development stage, the CPO explicitly designates the existing Technical
Architecture Owner role holder to also serve as the interim Quality Authority for OD-020 contract
testing policy and related development-stage quality governance:

```text
DESIGNATING_AUTHORITY = CPO
QUALITY_AUTHORITY = EXISTING_TECHNICAL_ARCHITECTURE_OWNER_ROLE_HOLDER
DESIGNATION_SCOPE = NESHANE_V3_CURRENT_DEVELOPMENT_STAGE_AND_OD_020
DESIGNATION_SOURCE = EXPLICIT_CPO_AND_TECHNICAL_ARCHITECTURE_OWNER_OD_020_FINALIZATION_DIRECTION
DESIGNATION_EFFECTIVE = EXPLICIT_CPO_DECLARATION_IN_OD_020_FINALIZATION_TASK
REPOSITORY_EFFECT = UPON_TRACEABLE_LEVEL_2_COMMIT
DURATION = UNTIL_SUPERSEDED_BY_FORMAL_ORGANIZATIONAL_DESIGNATION
```

The dual role is permitted for this bounded Level 2 development-stage decision because current
project governance contains no prohibition or independently authoritative separation-of-duties
rule for Quality Authority assignment. Architecture and Quality dispositions remain logically
separate and must be recorded separately against the exact reviewed revision. The Quality role
owns testing policy, evidence requirements, risk classification, Quality exceptions and
release-quality governance; it does not gain Security Authority, risk-acceptance, runtime-control
verification or Production Release authority.

The role holder must disclose the dual capacity. A material Architecture/Quality conflict must be
recorded rather than silently resolved; if it affects a Level 3/4 gate or cannot be resolved within
the approved policy, it is escalated to the applicable independent Security, Release or later
formally designated Quality authority. Failed evidence remains failed, and this designation cannot
convert it to PASS or waive a non-waivable control. The designation is project-scoped, temporary
and does not generalize to another project or organizational appointment.

#### Proportionate Level 2 workflow

1. Identify the decision, affected scope, owner and related `DEC-*`, `OD-*`, ADR, contract and Task IDs.
2. Record the context, viable alternatives, rationale, consequences, compatibility impact, and migration/rollback needs in proportion to the decision's impact.
3. Obtain an explicit disposition from the Technical Architecture Owner and every additional authority explicitly required by an existing decision or higher-level gate.
4. Create or update the ADR, update the Open Decision and decision registers, and preserve rejected or superseded history.
5. Validate internal references and affected API, event, persistence, SDK and integration contracts using the [contract change protocol](contract-change-protocol.md).
6. Commit the decision and its registry updates as one traceable Git change before treating it as effective.

The ADR lifecycle and required record fields are defined in the [ADR catalog](adr/README.md). Conversation analysis, a Task definition, implementation code or a Git commit alone does not approve an architecture decision. Corporate certificates and external signatures are not required for ordinary Level 2 decisions unless an independently authoritative policy, contract, regulation or an explicit higher-level gate requires them.

### LEVEL 3 — SECURITY-CRITICAL DECISION

Security-critical decisions require the designated or independent security review and documented authorization required by the applicable security control, decision record or review gate. Level 1 closure does not constitute Security Sign-off, risk acceptance or verification of a runtime control.

### Documentation-only R0 Design Consistency Acceptance

A documentation-only R0 baseline may use a proportionate Design Consistency Acceptance route when it records existing approved architecture and product scope without creating a security-critical decision, risk acceptance, security exception or production claim.

This route requires all of the following:

1. explicit CPO Product acceptance of the bounded scope;
2. actual approval by an identifiable, project-designated Technical Architecture Owner that the exact baseline is consistent with accepted ADRs, standards and security invariants;
3. evidence references, evaluated acceptance criteria and a traceable Git change;
4. explicit carry-forward of unresolved Open Decisions, proposed Security Requirements, specialist reviews and implementation evidence; and
5. clear separation from Security Sign-off, runtime assurance and Production Readiness.

Codex-assisted security consistency analysis may be retained as supporting evidence only. It cannot appoint the Technical Architecture Owner, issue the required approval or replace a human decision. The Technical Architecture Owner need not be an independent Security Reviewer for this bounded route, but the identity, project designation, reviewed revision, scope and disposition must be recorded. This route does not assign or satisfy `AUTH-IP`, `AUTH-TS`, `AUTH-SS`, `AUTH-SA`, `AUTH-ISR` or another specialist authority.

The route is unavailable for approval of security-critical authorization, risk acceptance, privileged-operation policy, executable `DURABLE_DEFER`, a Security Requirement, a security exception, Independent Security Review, runtime control effectiveness or production release. A material architecture change still follows Level 2; a security-critical decision still follows Level 3; production authorization still follows Level 4.

The CPO authorizes `V3-004` to use this route for its documentation-only Support Matrix. This authorization does not itself supply the required Technical Architecture Owner approval or close `V3-004`.

#### V3-004 project role designation

For the bounded `V3-004` documentation-only R0 baseline, the user explicitly declares the following project roles:

```text
TECHNICAL_ARCHITECTURE_OWNER = CPO (dual role)
DESIGNATION_SCOPE = Neshane V3 project architecture and V3-004 R0 design baseline
DESIGNATION_SOURCE = Explicit project-owner declaration in conversation
```

The declaration is accepted as a project-role designation under this route. It does not claim a legal identity, corporate credential, signature, appointment certificate or independent review. No separation-of-duties rule in the current project governance prohibits the combined role for documentation-only Design Consistency Acceptance. This combined role is not valid for the Level 3 or Level 4 exclusions listed above and does not appoint or satisfy any specialist or Independent Security authority.

### LEVEL 4 — PRODUCTION RELEASE

Production release requires executable validation, all required Security Sign-off, operational evidence and explicit release authorization. Documentation acceptance, architecture approval and implementation completion do not establish Production Readiness.

## Classification and escalation

- Task acceptance applies only to the scope and acceptance criteria of the named task.
- A task containing a material architecture choice is routed to Level 2 for that choice even if the remaining work is Level 1.
- A security-sensitive decision is routed to Level 3 where the relevant control requires it.
- Any production claim or release action is routed to Level 4.
- When multiple levels apply, satisfying a lower level never satisfies a higher level.
- Missing evidence is reported at the level where it is required; it does not automatically block unrelated lower-level work.

## Transition rule

This policy is prospective and is not retroactively applied to earlier tasks by default. The CPO expressly authorizes one bounded transition for `V3-003`: its Analytical / Documentation Closure is evaluated as Level 1 using the already recorded analytical deliverables, acceptance criteria, Evidence Matrix and explicit CPO direction.

For this transition, `V3-003-AC-P-12` is satisfied by the CPO's explicit task-scoped direction, the authoritative in-repository closure acknowledgment, the accepted analytical scope and criteria, and the traceable repository change. Historical requests for a corporate authority certificate or organizational digital signature are retained as historical preparation but are not applicable Closure prerequisites under the amended Level 1 policy.

This transition does not authenticate or validate previously asserted corporate evidence identifiers. It does not approve `OD-001..023`, `SR-CAND-001..024`, specialist dispositions, executable `DURABLE_DEFER`, Security Design Sign-off, runtime assurance, risk acceptance or Production Readiness.

## Repository propagation

This change alters Root task-acceptance routing only. Backend and Frontend continue to require explicit Task IDs and retain their existing architecture, security and execution restrictions. No repository-local rule conflicts with this policy, so no local governance file is changed by `V3-003`.

The `V3-004` narrow amendment also remains Root-only. It creates no Backend/Frontend acceptance, Security Sign-off or production authorization and requires no repository-local governance change.

The `V3-005` controlled-execution amendment updated Root and Backend build/test permissions. `V3-010` supersedes its repeated-approval restrictions prospectively with the development-first policy above and propagates compatible execution guidance to Root, Backend and Frontend. Repository-local work still requires an explicit Task ID and remains subject to architecture, security and production boundaries.
