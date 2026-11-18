# Customer business-rule catalog — V3-FR-A-002

**No business rule is approved beyond source invariants.**

## APPROVED (source invariants)

- Customer Domain owns Customer Master data; authoritative writer and final resource/action authorizer (V3-002B-DEC-002).
- Durable CUS-CREATE/CUS-UPDATE require coordinated mandatory Audit publication obligation; success not reported without the durably recorded obligation (DEC-012 principles 1/2/4).
- Explicit disclosure denial carries disclosure-safe Audit obligation; zero-result search is not a denial (DEC-012 principle 3).
- Pending Submission PERMITTED NOT REQUIRED; never authoritative; external recording prohibited (DEC-005).
- Broker ACK / Outbox record is not authoritative Audit ingestion (DEC-013/014).
- Validated Tenant Context; owning-Domain authorization; fail closed.

## PROPOSED (candidate, not approved)

- Duplicate detection criteria and handling.
- Merge / deletion / retention policy.
- Concurrency control for CUS-UPDATE.
- Customer classification taxonomy and status semantics.

## OPEN

- Exact field validation/uniqueness/normalization rules.
- Lifecycle state machine and transition guards.
- Operation-specific Audit failure policy (no executable DURABLE_DEFER).
- Referential integrity for Branch/Relationship and deletion semantics.

Every PROPOSED/OPEN rule blocks dependent implementation until explicitly dispositioned.

## Relationship and overlap (user-confirmed — authoritative)

- Each Person may have multiple concurrent Relationships with Company/Branch; each role is a distinct Relationship (CM1-PD-029).
- Same Person + same target + same role + overlapping interval → warning; allowed only through a controlled exception (warning + valid authority + mandatory reason + Audit); reuse existing OR create with mandatory exception reason (no supervisor approval) (CM1-PD-033/035).
- Distinct role codes / different targets / Company-vs-Branch overlap freely (CM1-PD-034).
- ENDED intervals participate in historical overlap detection (CM1-PD-037).
- Idempotent retries must not create duplicate Relationship records (CM1-PD-039).
- Overlap exception does not bypass stale-version, Tenant isolation, validation, or disclosure control (CM1-PD-040).
- Supersedes any prior absolute-overlap prohibition (CM1-PD-041).

## Branch reparenting (user-confirmed)

- Direct Branch reparenting prohibited; branchId/companyId immutable (CM1-PD-044).
- Transfer = new Branch under target Company + deactivate original; no automatic transfer of activities/relationships; optional succession reference does not transfer ownership/permissions (CM1-PD-045).

## Audit boundaries (user-confirmed)

- Durable Customer mutations honor coordinated Audit obligations; proposed Branch/Relationship/Verification operations require auditability requirement with formal operational contract pending (CM1-PD-048).
- Rejected validations/warnings/read-only queries have no assumed mandatory Audit event (CM1-PD-049).
- Controlled evidence references over copying identity docs/private identifiers into Audit (CM1-PD-050).
- Mandatory coordinated Audit failure must not report success; ACK/outbox != authoritative ingestion (CM1-PD-051).
