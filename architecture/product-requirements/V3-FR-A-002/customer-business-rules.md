# Customer business-rule catalog — V3-FR-A-002

Classification legend: **APPROVED SOURCE INVARIANT** (baseline architecture/audit) · **USER-CONFIRMED PRODUCT DIRECTION** (product policy, acceptance pending) · **PROPOSED IMPLEMENTATION/CONTRACT** · **OPEN DECISION**.

## APPROVED SOURCE INVARIANT

- Customer Domain owns Customer Master data; authoritative writer and final resource/action authorizer (V3-002B-DEC-002).
- Validated Tenant Context; client selector untrusted; cross-tenant fails closed.
- Durable CUS-CREATE/CUS-UPDATE require coordinated mandatory Audit obligation; success not reported without the durably recorded obligation (DEC-012).
- Explicit disclosure denial carries disclosure-safe Audit obligation; zero-result search is not a denial (DEC-012 p3).
- Broker ACK / Outbox record is not authoritative Audit ingestion (DEC-013/014).
- Pending Submission PERMITTED NOT REQUIRED; never authoritative; external recording prohibited (DEC-005).

## USER-CONFIRMED PRODUCT DIRECTION

**Entity model:** Company and Person independent; Branch subordinate to Company; Person may have multiple concurrent relationships without duplicating identity (CM1-PD-001..004).

**Duplicates (policy confirmed):** probabilistic match → warning + suggestion; authorized CUS-CREATE override with mandatory reason; no supervisor approval; verified identifier collision cannot be overridden; no automatic merge (CM1-PD-005..007, CM1-PD-052). *Still OPEN: exact matching algorithm, identifier namespace/uniqueness enforcement, full merge/delete/retention workflows.*

**Lifecycle:** ACTIVE/INACTIVE/ARCHIVED with the transition matrix in customer-lifecycle.md §B (CM1-PD-008..012, CM1-PD-054).

**CUS-UPDATE / concurrency (policy confirmed):** optimistic concurrency; reject stale versions; no auto-merge/last-write-wins (CM1-PD-013..015, CM1-PD-055). *Still OPEN: exact API contract and persistence enforcement.*

**Identity verification (policy confirmed):** system/manual verification; separate verification authority; evidence-based validity; no universal expiry; SoD for sensitive processes (CM1-PD-019..028, CM1-PD-056/057). *Still OPEN: trusted provider catalog, formal evidence acceptance, sensitive-process catalog, provider failure/recovery.*

**Relationship and overlap (authoritative):** multiple concurrent relationships; controlled overlap exception (warning + authority + mandatory reason + Audit); distinct roles/targets overlap freely; supersedes absolute-overlap prohibition (CM1-PD-029..041).

**Branch:** subordinate; immutable companyId; no direct reparenting; transfer via new Branch; only ACTIVE/INACTIVE (CM1-PD-042..047).

**Audit boundaries:** durable mutations honor coordinated obligations; proposed Branch/Relationship/Verification operations require auditability requirement (contract pending); no assumed mandatory Audit for warnings/rejected validations/reads; controlled evidence references; ACK != ingestion (CM1-PD-048..051).

## PROPOSED IMPLEMENTATION/CONTRACT

- Persistence/API schema for fields, relationships, and verification state (all unapproved).
- Overlap conflict-set token/snapshot/locking/transactional mechanics (technical design, not API contract).
- Branch reparenting coordination workflow and activity-transfer contracts.

## OPEN DECISION

- Exact field validation/uniqueness/normalization; role catalog; identifier namespace/scope.
- Merge/deletion/retention/legal-hold; operation-specific Audit failure/recovery owner and policy.
- Sensitive-process catalog and SoD actor mapping; trusted provider catalog; evidence acceptance/retention.
