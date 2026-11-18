# Authorization boundary analysis — no new RBAC or IAM

Existing invariants only; this is not a role-to-permission matrix, policy engine, token/session design, grant mechanism or IAM implementation. Operation names describe documented work, not authorized actors.

## AUTHB-A001-01 — Identity versus authorization

**Existing boundary:** Identity Trust owns Principal/session validity, not a business permission. Each Domain authorizes every operation/object.

**No inferred access:** Authenticated identity, token or admitted issuer is not Customer/Sales/Audit access.

**Denial / required behavior:** Invalid identity or resource authorization cannot proceed; exact role/denial policy remains OPEN.

**Evidence:** EVID-A001-054, EVID-A001-011, EVID-A001-003

## AUTHB-A001-02 — Tenant Membership versus permissions

**Existing boundary:** Tenant Management owns Tenant/Organization/Membership and its administration. Active Membership establishes validated association, not a right to every resource.

**No inferred access:** Tenant selector, Membership role or destination switch is not business resource access.

**Denial / required behavior:** Missing/conflicting Context fails closed; destination Membership and Context revalidated.

**Evidence:** EVID-A001-055, EVID-A001-001, EVID-A001-012

## AUTHB-A001-03 — Feature eligibility versus authorization

**Existing boundary:** Entitlement owns Feature Assignment/effective eligibility; each resource owner still authorizes.

**No inferred access:** Plan/Subscription evidence, feature enabled or Quota reservation does not authorize a business operation.

**Denial / required behavior:** Actual capability-to-eligibility/quota integration requires its own approved policy; unknown state not assumed permission.

**Evidence:** EVID-A001-048, EVID-A001-049, EVID-A001-003

## AUTHB-A001-04 — Resource/data ownership versus access rights

**Existing boundary:** Owning Domain is authoritative writer and final resource authorizer; a named person/team/service is not appointed by that architectural fact.

**No inferred access:** Customer record, File ID, assignment, cross-domain link or report/projection does not itself grant access.

**Denial / required behavior:** File + Attachment resource authorization distinct; Reports preserve source disclosure; no cross-service database bypass.

**Evidence:** EVID-A001-043, EVID-A001-051, EVID-A001-052, EVID-A001-050

## AUTHB-A001-05 — Platform versus Tenant administration

**Existing boundary:** Tenant administration concerns approved Tenant-owned resources; profile operations concerns scoped infrastructure/visibility. Destination Domain still authorizes business effects.

**No inferred access:** Operator/tenant-admin/support title is not universal Customer or Audit permission, break-glass access or local Sovereign administrator.

**Denial / required behavior:** Explicit scope/trust and required Audit; no unknown privileged outcome reported as successful.

**Evidence:** EVID-A001-006, EVID-A001-025, EVID-A001-023, EVID-A001-053

## AUTHB-A001-06 — Service ownership versus cross-service access

**Existing boundary:** A service owns its private data/schema/credentials/migrations and versioned contracts; other services are independent authenticated callers.

**No inferred access:** Co-deployment, internal network, broker delivery, shared administration or source ownership is not SQL/ORM/private API access authority.

**Denial / required behavior:** No cross-service SQL/entities/transaction; approved contracts/projections and tenant/provenance/consumer checks required.

**Evidence:** EVID-A001-075, EVID-A001-004, EVID-A001-047

## AUTHB-A001-07 — Project governance versus runtime local authority

**Existing boundary:** Unified final internal project decision owner is distinct from runtime Principal/Operator privileges and locally authoritative Sovereign control.

**No inferred access:** A conversation approval, technical advisor or Central identity is not an executable grant, Gate evidence or automatic local administrator.

**Denial / required behavior:** No Gate, offline or production acceptance inferred; binding obligations/non-waivable controls preserved.

**Evidence:** EVID-A001-013, EVID-A001-016, EVID-A001-025, EVID-A001-026

## Disclosure, Audit and operational restrictions

Customer successful authoritative create/update require consistently coordinated durable mandatory Audit obligations; broker ACK/Outbox is not authoritative Audit ingestion. Explicit Customer disclosure denials and covered privileged request/outcome/sensitive Audit access obligations retain their bounded scope. Recording a missing actor policy does not approve executable DURABLE_DEFER, universal audit of all reads, legal retention, break-glass access or an alternative failure path. See existing V3-003-DEC-011/012/013/014 and the pending policy questions.

Frontend permissions are UX only; resource-owning Backend remains final authorizer. Services own private persistence and authenticated incoming boundaries; shared infrastructure/admin roles, actual-pool/RLS fixtures or a passed local laboratory do not establish accepted product isolation. Actual G-RUNTIME remains BLOCKED; no Runtime proof executed here.

Deferred external customers/Portal, provider registry, Email/SMS/Push and plugin-hosting/marketplace context create no new FIRST_RELEASE or CM-1 dependency. All fifteen approved capabilities and three profile commitments remain; actor gaps do not cancel them.
