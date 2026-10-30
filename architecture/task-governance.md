# Neshane V3 proportionate task governance

## Document control

| Field | Value |
| --- | --- |
| Status | `APPROVED — PROJECT GOVERNANCE` |
| Authorizing task | `V3-003` |
| Requesting authority | `CPO` |
| Scope | Project-level development, documentation, architecture, security-decision and production-release approval routing |
| Governance baseline label | `NESHANE-V3-GOV-P00-000A` unchanged; no new label was authorized by this task |

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

### LEVEL 2 — ARCHITECTURE DECISION

Material architecture decisions require approval by the designated architecture authority under the existing ADR and Open Decision process. A Level 1 task acceptance cannot approve or close an ADR or Open Decision unless that architecture process is expressly completed.

### LEVEL 3 — SECURITY-CRITICAL DECISION

Security-critical decisions require the designated or independent security review and documented authorization required by the applicable security control, decision record or review gate. Level 1 closure does not constitute Security Sign-off, risk acceptance or verification of a runtime control.

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
