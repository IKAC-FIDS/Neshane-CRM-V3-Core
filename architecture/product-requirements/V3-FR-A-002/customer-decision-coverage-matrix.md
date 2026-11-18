# Customer Master — Decision Coverage Matrix (v1.2.1)

Maps all 57 user-confirmed product decisions (CM1-PD-001..057) to requirements, rules, fields, operations, acceptance criteria and OPEN questions. Coverage classification: FULL / PARTIAL / DOCUMENTED_ONLY / BLOCKED_BY_OPEN_DECISION.

**Coverage counts:** BLOCKED_BY_OPEN_DECISION=2, DOCUMENTED_ONLY=5, FULL=3, PARTIAL=47

| Decision ID | Coverage | Summary | Fields | Acceptance criteria | Related OPEN |
| --- | --- | --- | --- | --- | --- |
| CM1-PD-001 | PARTIAL | Company and Person are independent customer types; Branch is a Company subordinate, with i | FLD-002-01, FLD-002-02 | CM1-FLD-01, CM1-FLD-02, CM1-BRN-01 | PDQ-002-01, PDQ-002-07 |
| CM1-PD-002 | DOCUMENTED_ONLY | CRM activities may reference Branch as an attribution target, while Company remains the pa | FLD-002-11 | CM1-BRN-01 | PDQ-A001-052 |
| CM1-PD-003 | PARTIAL | One Person may have multiple concurrent relationships with Companies and Branches in the s | REL-002-01, REL-002-02, REL-002-04 | CM1-REL-01 | PDQ-002-07 |
| CM1-PD-004 | DOCUMENTED_ONLY | A corporate contact is represented by Person, even without individual active commercial en | FLD-002-06, FLD-002-07 | CM1-FLD-02 | PDQ-002-07 |
| CM1-PD-005 | PARTIAL | Potential matches generate an access-controlled warning and existing-record suggestion; au | — | CM1-DUP-02, CM1-DUP-04 | PDQ-002-03 |
| CM1-PD-006 | PARTIAL | A user authorized for CUS-CREATE may override a probabilistic duplicate warning with a req | — | CM1-DUP-02 | PDQ-002-03 |
| CM1-PD-007 | PARTIAL | Ordinary duplicate override must not bypass a collision with a validated authoritative uni | FLD-002-04, FLD-002-05 | CM1-FLD-05, CM1-DUP-03, CM1-UPD-08 | PDQ-002-03 |
| CM1-PD-008 | PARTIAL | Record lifecycle is separate from commercial engagement/classification; commercial taxonom | FLD-002-09, FLD-002-10 | CM1-LC-01, CM1-VER-18 | PDQ-002-02 |
| CM1-PD-009 | FULL | Record states are ACTIVE, INACTIVE, ARCHIVED; after successful authorized creation and val | FLD-002-10 | CM1-LC-04 | PDQ-002-02 |
| CM1-PD-010 | FULL | ACTIVE -> INACTIVE may occur with ongoing activities preserved; initiating new activities  | — | CM1-LC-05 | PDQ-002-02 |
| CM1-PD-011 | PARTIAL | ACTIVE/INACTIVE -> ARCHIVED is blocked until every applicable open activity/dependency is  | — | CM1-LC-07, CM1-LC-08, CM1-BRN-09 | PDQ-002-02 |
| CM1-PD-012 | FULL | ARCHIVED -> INACTIVE is the only restore transition; INACTIVE -> ACTIVE requires revalidat | — | CM1-LC-09, CM1-LC-10 | PDQ-002-02 |
| CM1-PD-013 | PARTIAL | CUS-UPDATE permits authorized users to edit identity facts, including sensitive business i | — | CM1-UPD-06, CM1-UPD-07 | PDQ-002-04 |
| CM1-PD-014 | PARTIAL | CUS-UPDATE requires a record version; stale-version writes are rejected fully. No automati | REL-002-10 | CM1-UPD-01 | PDQ-002-04 |
| CM1-PD-015 | PARTIAL | An edit reason is mandatory only for changes to sensitive identity identifiers and excepti | — | CM1-UPD-06, CM1-UPD-07 | PDQ-002-04 |
| CM1-PD-016 | PARTIAL | Company legal/display name and Person given/family names are required for initial registra | FLD-002-01, FLD-002-02 | CM1-FLD-01, CM1-FLD-02, CM1-FLD-03 | PDQ-002-01 |
| CM1-PD-017 | PARTIAL | Official Person and Company identifiers are optional at initial create; workflows requirin | FLD-002-04, FLD-002-05, FLD-002-06, FLD-002-07 | CM1-FLD-01, CM1-FLD-02, CM1-FLD-06 | PDQ-002-01 |
| CM1-PD-018 | PARTIAL | A sufficiently verified official identifier must be unique within its approved identity/is | FLD-002-04, FLD-002-05 | CM1-FLD-05, CM1-UPD-08 | PDQ-002-01, PDQ-002-03 |
| CM1-PD-019 | PARTIAL | Formal identity verification is distinct from record lifecycle and commercial status. Its  | FLD-002-17 | CM1-VER-01, CM1-VER-17 | PDQ-002-07 |
| CM1-PD-020 | PARTIAL | Both trusted external/system verification and evidence-backed manual verification by separ | — | CM1-VER-02, CM1-VER-03 | PDQ-002-07 |
| CM1-PD-021 | PARTIAL | An actor who created the customer may manually verify that customer if independently permi | — | CM1-VER-04, CM1-VER-05 | PDQ-002-11 |
| CM1-PD-022 | PARTIAL | No universal time-based identity verification expiry. Effective validity depends on underl | — | CM1-VER-09, CM1-VER-10 | — |
| CM1-PD-023 | PARTIAL | Expiry/loss of validity of evidence necessary to substantiate an otherwise valid earlier v | — | CM1-VER-06 | — |
| CM1-PD-024 | PARTIAL | If prior verification is proven fundamentally invalid (false/misattributed/invalid from ou | — | CM1-VER-07, CM1-VER-08 | — |
| CM1-PD-025 | PARTIAL | Verification decisions preserve method (SYSTEM/MANUAL), source/issuer, verified actor/serv | — | CM1-VER-15, CM1-AUD-04 | — |
| CM1-PD-026 | PARTIAL | Generic CUS-UPDATE must not directly set VERIFIED; trusted verification workflow authorize | — | CM1-VER-03, CM1-VER-11, CM1-VER-12 | PDQ-002-07 |
| CM1-PD-027 | PARTIAL | NOT_VERIFIED and REQUIRES_REVERIFICATION can coexist with ACTIVE Customer; any consuming o | — | CM1-VER-18 | — |
| CM1-PD-028 | BLOCKED_BY_OPEN_DECISION | Verification expiry/revocation preserves Customer ID, historical relationships and an audi | — | CM1-VER-13 | PDQ-002-10 |
| CM1-PD-029 | PARTIAL | Each Person may have multiple concurrent Relationships with Company and/or Branch. Each in | REL-002-01, REL-002-02, REL-002-04 | CM1-REL-01 | PDQ-002-08 |
| CM1-PD-030 | DOCUMENTED_ONLY | Recommended conceptual Relationship fields: relationshipId, personId, targetType (COMPANY/ | REL-002-01, REL-002-02, REL-002-03, REL-002-04, REL-002-05, REL-002-06, REL-002-07, REL-002-08, REL-002-09, REL-002-10, REL-002-11, REL-002-12, REL-002-13, REL-002-14 | CM1-REL-01 | PDQ-002-08 |
| CM1-PD-031 | PARTIAL | Relationship lifecycle states are ACTIVE and ENDED (proposed for formal review). An ENDED  | REL-002-07 | CM1-REL-02 | PDQ-002-08 |
| CM1-PD-032 | PARTIAL | Use the conceptual half-open interval [startDate, endDate): start inclusive, end exclusive | REL-002-08, REL-002-09 | CM1-REL-03, CM1-REL-15 | PDQ-002-08 |
| CM1-PD-033 | PARTIAL | For the same Person, TargetType, TargetId and RoleCode, overlapping Relationship intervals | REL-002-05, REL-002-08, REL-002-09 | CM1-REL-04, CM1-REL-06 | PDQ-002-12 |
| CM1-PD-034 | PARTIAL | Distinct role codes may overlap freely; the same role may overlap across different compani | — | CM1-REL-05 | — |
| CM1-PD-035 | PARTIAL | Same Person + same target + same role + overlapping intervals produces a warning. The user | — | CM1-REL-06 | — |
| CM1-PD-036 | PARTIAL | A reason is required for each newly authorized overlap decision; old reasons do not author | — | CM1-REL-07 | — |
| CM1-PD-037 | PARTIAL | Even ENDED Relationship intervals participate in historical overlap detection. | — | CM1-REL-08 | — |
| CM1-PD-038 | BLOCKED_BY_OPEN_DECISION | Two cases are distinguished: (1) updating the same Relationship rejects stale record versi | REL-002-10 | CM1-REL-09, CM1-REL-10 | PDQ-002-12 |
| CM1-PD-039 | PARTIAL | Idempotent retries must not produce unintended additional Relationship records. An intenti | — | CM1-REL-11 | PDQ-002-12 |
| CM1-PD-040 | PARTIAL | Overlap exception authorization does not bypass stale-version checks, Tenant isolation, in | — | CM1-REL-12, CM1-REL-13 | — |
| CM1-PD-041 | DOCUMENTED_ONLY | The controlled-exception overlap policy SUPERSEDES any prior rule prohibiting all overlapp | — | CM1-REL-04 | — |
| CM1-PD-042 | PARTIAL | Branch has only two independent record states: ACTIVE and INACTIVE. Branch does not have a | — | CM1-BRN-01 | — |
| CM1-PD-043 | PARTIAL | Deactivating Company does not automatically change stored Branch statuses. Deactivating Br | — | CM1-BRN-04, CM1-BRN-08 | — |
| CM1-PD-044 | PARTIAL | Direct Branch reparenting is prohibited. branchId and companyId are immutable after creati | FLD-002-11 | CM1-BRN-02, CM1-UPD-02 | — |
| CM1-PD-045 | PARTIAL | When a Branch is genuinely transferred, create a new Branch under the target Company with  | — | CM1-BRN-03 | PDQ-002-09 |
| CM1-PD-046 | PARTIAL | Archiving Company requires resolution of applicable open dependencies across Company and B | — | CM1-BRN-09, CM1-BRN-05 | — |
| CM1-PD-047 | PARTIAL | Branch is subordinate to Company (not an independent Customer), has its own stable ID and  | FLD-002-11 | CM1-BRN-06, CM1-REL-14 | PDQ-002-08 |
| CM1-PD-048 | PARTIAL | Customer durable mutations honor existing coordinated persistent Audit obligations. Propos | — | CM1-AUD-01, CM1-AUD-02 | PDQ-002-10 |
| CM1-PD-049 | PARTIAL | Rejected validations, warnings, or read-only queries do not carry an assumed mandatory Aud | — | CM1-AUD-05 | — |
| CM1-PD-050 | PARTIAL | Prefer controlled references to sensitive evidence over copying entire identity documents  | — | CM1-AUD-04 | — |
| CM1-PD-051 | PARTIAL | A mandatory coordinated Audit failure must not result in a successful mutation being repor | — | CM1-AUD-01, CM1-AUD-02, CM1-AUD-03, CM1-UPD-10 | PDQ-002-10 |
| CM1-PD-052 | PARTIAL | Similar names, shared phone numbers, or shared emails alone are not conclusive identity ma | — | CM1-DUP-01, CM1-DUP-03, CM1-DUP-04, CM1-DUP-05 | PDQ-002-03 |
| CM1-PD-053 | PARTIAL | Address and Latin name are optional unless a specific consuming workflow requires them. Of | FLD-002-03, FLD-002-04, FLD-002-05, FLD-002-08 | CM1-FLD-06, CM1-DUP-01 | PDQ-002-01 |
| CM1-PD-054 | PARTIAL | Deactivation is allowed even with open activities; existing open activities and historical | — | CM1-LC-02, CM1-LC-03, CM1-LC-05, CM1-LC-11 | — |
| CM1-PD-055 | PARTIAL | Updating Company must not silently reparent Branches; updating Person must not silently al | — | CM1-UPD-02, CM1-UPD-03, CM1-UPD-04, CM1-UPD-05, CM1-UPD-09 | — |
| CM1-PD-056 | PARTIAL | A record can be ACTIVE and NOT_VERIFIED, and can be VERIFIED without automatically receivi | — | CM1-VER-17, CM1-VER-18 | — |
| CM1-PD-057 | DOCUMENTED_ONLY | Effective time and recording time are recorded distinctly when relevant. The specific evid | — | CM1-VER-15 | — |
