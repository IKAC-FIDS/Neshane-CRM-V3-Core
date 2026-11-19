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

Role Catalog product policy is user-confirmed in CM1-PD-058..065, not wholly undecided. [customer-role-catalog.md](customer-role-catalog.md) RC-001..008 is the detailed rule catalog: hybrid system/Tenant roles, applicability, lifecycle, immutable identity/no deletion, preservation, controlled scope changes, Tenant/system authority and overlap/history. Formal acceptance remains pending; exact executable contracts remain OPEN.

**Initial vocabulary / Tenant selectability:** CM1-PD-066/067 / RC-009..011 confirm the exact 12-entry initial System vocabulary and locally managed assignment restriction. Global ACTIVE, target applicability, Tenant selectability, Relationship authority and existing guards are jointly necessary, enforced by Customer Domain. Hide/unhide cannot modify global definitions, other Tenants or existing Relationships/history, grant permissions/legal authority, or bypass global INACTIVE. It has no inferred mandatory-reason rule and does not replace RC-006 management authority for incompatible scope changes. Preserve ordinary authorized overlap's no-extra-supervisor rule and conceptual roleCode key; technical reference/key remains OPEN.

**v1.5.0 product answers (not implementation):** CM1-PD-068..072 / `customer-role-catalog.md` RC-012..016 confirm ACTIVE System Role default selectability for new Tenants/new releases with prior settings preserved; canonical System-global versus owning-Tenant uniqueness; permanent scope-bound reservation; blocking only the conflicting new System Role without destructive resolution; and trim-uppercase / ASCII A-Z, 0-9, underscore / length 3..64. Matching custom codes across independent Tenants are allowed. No new lexical first-letter/underscore-placement restriction or central Tenant-private-data inspection right. Formal acceptance remains PENDING.

## PROPOSED IMPLEMENTATION/CONTRACT

- Persistence/API schema for fields, relationships, and verification state (all unapproved).
- Overlap conflict-set token/snapshot/locking/transactional mechanics (technical design, not API contract).
- Branch reparenting coordination workflow and activity-transfer contracts.

## OPEN DECISION

- Other Customer field/identifier validation remains unresolved. For Role codes, defaults/uniqueness/permanent reservation/future collision blocking/basic normalization are ANSWERED at product level. Exact schema/configuration/default materialization, namespace/enforcement/concurrency, authorized cross-Tenant detection/privacy, publication/rollback/resolution, Unicode/encoding edge cases, IAM/operation/Audit/reason policy, history/reference and temporal/API contracts remain OPEN (PDQ-002-08). Identifier namespace/scope remains separately OPEN.
- Merge/deletion/retention/legal-hold; operation-specific Audit failure/recovery owner and policy.
- Sensitive-process catalog and SoD actor mapping; trusted provider catalog; evidence acceptance/retention.
