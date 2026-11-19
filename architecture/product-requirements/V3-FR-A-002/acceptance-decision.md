# V3-FR-A-002 — bounded requirements acceptance

**ACCEPTED — BOUNDED REQUIREMENTS BASELINE**

- Authority: Farzad, Business Owner/product requirements decision authority, explicit conversation confirmation (2026-11-19); existing governance preserved. No signature or exact issuance time claimed.
- Core branch `codex/v3-fr-a-002`; reviewed commit `df6463d16390518bc5607e0a5c3d300128b75a9e`; v1.8.0.
- This record is the acceptance overlay for that immutable reviewed candidate. Historical PENDING statements in its artifacts are not rewritten.

## Accepted product scope

- Approved Company/Person registration and maintenance; Branch, contacts, addresses, Relationship and Role Catalog
- Basic duplicate detection, lifecycle activation/deactivation, field validation and calendar/time rules
- Dynamic Customer Document Catalog, bounded evidence upload and history as product requirements only
- Customer search/review selected scope; A-003 remains separate
- Shared SaaS/Shared Cell initial synthetic-only development scope; independent Dedicated Managed/Sovereign evidence deferred

## Conditional and excluded scope

- Archive/restore: applicable dependency clearance proven; unknown blocks
- Manual verification: approved issuer/evidence/legal/SoD and secure attachment contracts; upload does not verify identity
- Attachments selected, but A-011 and downstream contracts remain separately governed
- Real data/documents; production unauthorized; offline prohibited
- Merge, physical deletion, Pending Submission, direct external access excluded
- Real external verification, advanced matching, executable Branch transfer, OCR, automatic document authenticity, general document service deferred

## Open questions and implementation blockers

All 19 original questions remain OPEN: PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-049, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053, PDQ-002-01, PDQ-002-02, PDQ-002-03, PDQ-002-04, PDQ-002-05, PDQ-002-06, PDQ-002-07, PDQ-002-08, PDQ-002-09, PDQ-002-10, PDQ-002-11, PDQ-002-12.

- Actual actor bindings, precise masking and authorization examples; no IAM grants
- Issuer/evidence/legal/retention/disclosure/SoD and secure file contracts
- Archive dependency clearance and race-safe contracts
- Unsettled character-count/normalization, authoritative country/identifier formats, document completeness edge cases and timezone-change evaluation; affected rules excluded from independent candidate
- Applicable OD, API/schema, runtime, Audit reliability and downstream prerequisites remain OPEN

## Evidence and canonical disposition

106 product decisions; five canonical and 229 detailed criteria (234 total). Reviewed manifest covers 24 files and was independently verified 24/24 against remote Git blob bytes. Manifest digest: `92f921eb8b20082008adf8b9b5009fb7a8ac98796079699127ef6e9adcc620b3`. The manifest itself and reviewed files remain unchanged; this separate acceptance overlay is not counted in the historical manifest. No application tests/build/runtime executed; no proposed, deferred, blocked or unknown case is relabeled PASS.

| Canonical ID | Bounded review disposition | Evidence |
| --- | --- | --- |
| V3-FR-A-002-AC-01 | BOUNDED_DOCUMENTATION_REVIEWED | sha256-manifest.json, README.md, customer-bounded-readiness.md |
| V3-FR-A-002-AC-02 | BOUNDED_PRODUCT_DIRECTION_AND_EXPLICIT_RESIDUALS_ACCEPTED | source-traceability.json, customer-master-product-decision-record.json, customer-decision-coverage-matrix.json, customer-v180-scope-and-document-catalog.md |
| V3-FR-A-002-AC-03 | GAPS_RETAINED_BLOCKING_AFFECTED_EXECUTION | customer-bounded-readiness.json, open-product-decisions.md, actor-resource-policy-matrix.md, customer-operation-catalog.md |
| V3-FR-A-002-AC-04 | REQUIREMENTS_EXAMPLES_RETAINED_NOT_SOFTWARE_PASS | acceptance-criteria.md, cm1-acceptance-criteria-addendum.md, validation-report.md |
| V3-FR-A-002-AC-05 | BOUNDED_AUTHORITY_PRESERVED | customer-v180-scope-and-document-catalog.md, deployment-profile-scenarios.md, customer-bounded-readiness.json |

## Authorization boundary and next action

This accepts product requirements within the stated boundaries, not complete CM-1 delivery, executable contracts, IAM or production. No architecture decision closed. G-RUNTIME BLOCKED; FE-BE and AUTH/IAM PENDING; Offline PROHIBITED; Local-Infra ACCEPTED — DEVELOPMENT-ONLY; Production NOT AUTHORIZED.

V3-FR-F-000 is the next independent-rule candidate, with A-002 its sole direct canonical prerequisite. Separate explicit implementation authorization and exact design/repository/file/test scope are required before starting; no Spring, persistence, API, trust integration, live data or runtime. Any unresolved observable behavior must be excluded. No next task started.
