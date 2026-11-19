# Customer Master — Decision Coverage Matrix (v1.7.0 bounded candidate)

Maps all 95 user-confirmed product decisions (CM1-PD-001..095). Coverage means documentation/scenario coverage, never software execution or formal acceptance. Eighteen new rows PARTIAL with explicit residual contracts/evidence/authorization and proposed scenarios. Prior classes retained; historical row gaps refined by new packages are current-dispositioned in customer-bounded-readiness.json and PDR refinementsV170, not treated as unanswered policy by copying stale text. Exact field/operation/scenario/question references in JSON. No IAM/setting field schema invented.

**Coverage counts:** BLOCKED_BY_OPEN_DECISION=2, DOCUMENTED_ONLY=5, FULL=3, PARTIAL=85

New decision coverage (details in JSON):

| Decision ID | Class | Requirement/rule | New scenario IDs |
| --- | --- | --- | --- |
| CM1-PD-078 | PARTIAL | Bounded accountability | CM1-BND-01 |
| CM1-PD-079 | PARTIAL | Actor/resource/disclosure | CM1-BND-02, CM1-BND-41, CM1-BND-49 |
| CM1-PD-080 | PARTIAL | Selected scope boundaries | CM1-BND-03, CM1-BND-04, CM1-BND-05, CM1-BND-06 |
| CM1-PD-081 | PARTIAL | Synthetic/profile/applicability | CM1-BND-07, CM1-BND-08, CM1-BND-40 |
| CM1-PD-082 | PARTIAL | Minimum mapped fields | CM1-BND-09, CM1-BND-10, CM1-BND-11, CM1-BND-12 |
| CM1-PD-083 | PARTIAL | Multi-identifier namespace/evidence | CM1-BND-13, CM1-BND-14, CM1-BND-15, CM1-BND-16 |
| CM1-PD-084 | PARTIAL | Basic duplicate signals/exception | CM1-BND-17, CM1-BND-18, CM1-BND-19, CM1-BND-20, CM1-BND-21 |
| CM1-PD-085 | PARTIAL | Critical facts/evidence basis | CM1-BND-22, CM1-BND-23, CM1-BND-24 |
| CM1-PD-086 | PARTIAL | Immutable Relationship/day/END | CM1-BND-25, CM1-BND-26, CM1-BND-27, CM1-BND-28, CM1-BND-29, CM1-BND-30 |
| CM1-PD-087 | PARTIAL | Applicable archive dependencies | CM1-BND-31, CM1-BND-32, CM1-BND-33, CM1-BND-34 |
| CM1-PD-088 | PARTIAL | Reactivation/restoration guards | CM1-BND-35, CM1-BND-36 |
| CM1-PD-089 | PARTIAL | Evidence methods/information | CM1-BND-37, CM1-BND-38, CM1-BND-39, CM1-BND-40 |
| CM1-PD-090 | PARTIAL | Three mandatory SoD cases | CM1-BND-41, CM1-BND-42 |
| CM1-PD-091 | PARTIAL | Verification/history/dispute | CM1-BND-43, CM1-BND-44 |
| CM1-PD-092 | PARTIAL | Audit/reason/access policy | CM1-BND-45, CM1-BND-46, CM1-BND-47, CM1-BND-48, CM1-BND-49 |
| CM1-PD-093 | PARTIAL | Logical safe Audit information | CM1-BND-50 |
| CM1-PD-094 | PARTIAL | Durable failure/ingestion/security | CM1-BND-51, CM1-BND-52, CM1-BND-53 |
| CM1-PD-095 | PARTIAL | Retention/legal/synthetic boundary | CM1-BND-54 |

| Decision ID | Coverage | Summary | Fields | Acceptance criteria | Related OPEN |
| --- | --- | --- | --- | --- | --- |
| CM1-PD-073 | PARTIAL | RC-017/021 own-Tenant Hide/Unhide reason/Audit | FLD-002-15, REL-002-05 | CM1-ROL-46, CM1-ROL-47, CM1-ROL-48, CM1-ROL-63, CM1-ROL-66, CM1-ROL-69 | PDQ-002-08, PDQ-002-10 |
| CM1-PD-074 | PARTIAL | RC-018/021 metadata governance / old-new values | REL-002-06, REL-002-05, FLD-002-15 | CM1-ROL-49, CM1-ROL-50, CM1-ROL-51, CM1-ROL-52, CM1-ROL-53, CM1-ROL-63, CM1-ROL-65, CM1-ROL-66, CM1-ROL-69 | PDQ-002-08, PDQ-002-10 |
| CM1-PD-075 | PARTIAL | RC-019 current/event-time title preservation | REL-002-06, REL-002-05 | CM1-ROL-53, CM1-ROL-54, CM1-ROL-55, CM1-ROL-56, CM1-ROL-66, CM1-ROL-68 | PDQ-002-08, PDQ-002-10 |
| CM1-PD-076 | PARTIAL | RC-020/006 three logical categories / Backend | — | CM1-ROL-48, CM1-ROL-50, CM1-ROL-57, CM1-ROL-58, CM1-ROL-59, CM1-ROL-60, CM1-ROL-61, CM1-ROL-64, CM1-ROL-67, CM1-ROL-68 | PDQ-002-08, PDQ-002-10 |
| CM1-PD-077 | PARTIAL | RC-021 mandatory coverage/reasons/integrity/durability | FLD-002-15, REL-002-06 | CM1-ROL-46, CM1-ROL-48, CM1-ROL-49, CM1-ROL-50, CM1-ROL-55, CM1-ROL-62, CM1-ROL-63, CM1-ROL-64, CM1-ROL-65, CM1-ROL-66, CM1-ROL-67, CM1-ROL-68, CM1-ROL-69, CM1-ROL-70 | PDQ-002-08, PDQ-002-10 |
| CM1-PD-068 | PARTIAL | RC-012 defaults and prior setting preservation | — | CM1-ROL-30, CM1-ROL-31, CM1-ROL-32, CM1-ROL-33 | PDQ-002-08 |
| CM1-PD-069 | PARTIAL | RC-013 canonical namespace uniqueness | REL-002-05 | CM1-ROL-34, CM1-ROL-35, CM1-ROL-36, CM1-ROL-37, CM1-ROL-43, CM1-ROL-45 | PDQ-002-08 |
| CM1-PD-070 | PARTIAL | RC-014 permanent reservation / identity | REL-002-05 | CM1-ROL-35, CM1-ROL-38, CM1-ROL-39, CM1-ROL-43, CM1-ROL-45 | PDQ-002-08 |
| CM1-PD-071 | PARTIAL | RC-015 conflicting-new-Role gate / privacy | REL-002-05 | CM1-ROL-40, CM1-ROL-41, CM1-ROL-45 | PDQ-002-08 |
| CM1-PD-072 | PARTIAL | RC-016 basic normalization / validation | REL-002-05 | CM1-ROL-42, CM1-ROL-43, CM1-ROL-44, CM1-ROL-45 | PDQ-002-08 |
| CM1-PD-066 | PARTIAL | RC-009 initial vocabulary v1.0 / no implicit authority | REL-002-03, REL-002-05, REL-002-06 | CM1-ROL-17, CM1-ROL-18, CM1-ROL-26, CM1-ROL-29 | PDQ-002-08 |
| CM1-PD-067 | PARTIAL | RC-010/011 Tenant selectability / effective eligibility | REL-002-03, REL-002-05, REL-002-07, REL-002-10 | CM1-ROL-19, CM1-ROL-20, CM1-ROL-21, CM1-ROL-22, CM1-ROL-23, CM1-ROL-24, CM1-ROL-25, CM1-ROL-26, CM1-ROL-27, CM1-ROL-28, CM1-ROL-29 | PDQ-002-08, PDQ-002-10, PDQ-002-12 |
| CM1-PD-058 | PARTIAL | RC-001 hybrid catalog; no IAM/RBAC grants | REL-002-05 | CM1-ROL-01, CM1-ROL-13, CM1-ROL-14 | PDQ-002-08 |
| CM1-PD-059 | PARTIAL | RC-002 applicability / new assignments | REL-002-03, REL-002-05 | CM1-ROL-02, CM1-ROL-08, CM1-ROL-09 | PDQ-002-08 |
| CM1-PD-060 | PARTIAL | RC-003 lifecycle and authorized transitions | — | CM1-ROL-03, CM1-ROL-04 | PDQ-002-08 |
| CM1-PD-061 | PARTIAL | RC-004 immutable identity / no deletion | REL-002-05 | CM1-ROL-05, CM1-ROL-06, CM1-ROL-15 | PDQ-002-08 |
| CM1-PD-062 | PARTIAL | RC-005 Relationship preservation | REL-002-05, REL-002-07, REL-002-08, REL-002-09 | CM1-ROL-07 | PDQ-002-08 |
| CM1-PD-063 | PARTIAL | RC-006 controlled scope change | REL-002-03, REL-002-05 | CM1-ROL-08, CM1-ROL-09, CM1-ROL-10, CM1-ROL-11 | PDQ-002-08, PDQ-002-10 |
| CM1-PD-064 | PARTIAL | RC-007 system/Tenant authority | — | CM1-ROL-12, CM1-ROL-13, CM1-ROL-14 | PDQ-002-08 |
| CM1-PD-065 | PARTIAL | RC-004/008 history / overlap safeguards | REL-002-05, REL-002-06, REL-002-10 | CM1-ROL-15, CM1-ROL-16, CM1-REL-09, CM1-REL-10 | PDQ-002-08, PDQ-002-10, PDQ-002-12 |
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

## v1.8.0 current inventory

106 decisions: FULL=3, PARTIAL=96, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2.

| Decision | Topic | Criteria | Coverage |
| --- | --- | --- | --- |
| CM1-PD-96 | Actor operation and disclosure matrix | CM1-V18-01, CM1-V18-02 | PARTIAL |
| CM1-PD-97 | Profile scope | CM1-V18-03, CM1-V18-04 | PARTIAL |
| CM1-PD-98 | Conditional roadmap branches | CM1-V18-05, CM1-V18-06 | PARTIAL |
| CM1-PD-99 | Dynamic Customer Document Catalog | CM1-V18-07, CM1-V18-08 | PARTIAL |
| CM1-PD-100 | Document requirement stage and change policy | CM1-V18-09, CM1-V18-10 | PARTIAL |
| CM1-PD-101 | Evidence upload and metadata | CM1-V18-11, CM1-V18-12 | PARTIAL |
| CM1-PD-102 | Document state and completeness | CM1-V18-13, CM1-V18-14 | PARTIAL |
| CM1-PD-103 | Document authority and Audit | CM1-V18-15, CM1-V18-16 | PARTIAL |
| CM1-PD-104 | Date and time | CM1-V18-17, CM1-V18-18 | PARTIAL |
| CM1-PD-105 | Field validation | CM1-V18-19, CM1-V18-20 | PARTIAL |
| CM1-PD-106 | Multiple contact channels and addresses | CM1-V18-21, CM1-V18-22 | PARTIAL |
