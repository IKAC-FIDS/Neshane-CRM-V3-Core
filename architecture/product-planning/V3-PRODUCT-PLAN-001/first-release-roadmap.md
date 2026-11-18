# First Release proposed roadmap

**V3-PRODUCT-PLAN-001 — PROPOSED, requirements engineering only.** No task in this roadmap is authorized for implementation. No architecture choice, Gate decision, staging, commit, push, deployment or release is performed.

## Source hierarchy and scope

Approved capability authority: `migration/v2-owner-review.md` §§4–5; `architecture/reviews/V3-003-decision-record.md` DEC-002 and subsequent bounded decisions; `deployment/support-matrix.md` §§5, 6, 11. All fifteen IDs and original titles are retained in the inventory. Support is a target commitment for Shared SaaS, Dedicated Managed and Dedicated Sovereign, not current availability.

Latest Core `baseline-v3.md` introductory annotations record P00-006/ADR-V3-016 design/reference effectivity at 2026-11-13T14:21:48+03:30 and limited G-R2/Security/Tenant design acceptance. Older pending text in the ADR/register/support matrix is history, not a new blocker or runtime approval. Current OD register resolves OD-002/003/004 (Java 21, Boot 4.1.2, Gradle), OD-008 (versioning), OD-020 (testing policy). Do not reopen those choices or infer runtime/CI proof. All other eighteen ODs remain OPEN.

FR-PF-001 Option B is approved by the later support matrix, superseding the earlier inventory's missing product confirmation only within minimum trusted internal access scope. Detailed IdP/session/membership policies remain OPEN. DEC-003/004 approve only bounded Customer BC scenarios; all other classifications remain unassessed. DEC-005 permits but does not require Pending Customer Submission; it is not Customer Master or an available workaround. DEC-007 candidate SR-CAND-001..024 remain proposals. DEC-011/012 require bounded privileged/Audit-access/Customer Audit obligations, not universal audit of every read. DEC-013/014 select conditional Customer Audit direction and safety gates, NOT executable DURABLE_DEFER.

## Proposed execution streams

| Phase | Work | Exit condition before dependent work |
| --- | --- | --- |
| A | Actor/owner catalog, fifteen capability requirement packages, integration matrices | Explicit product disposition; missing rules remain OPEN |
| B | OD alternatives/decision packages at original milestones; reuse/synchronization review | Explicit applicable Level 2/3 decisions and traceable effectivity |
| C | Provider-neutral trusted access/context design, then separately scoped IAM implementation | AUTH/IAM authorization, approved mechanisms and accepted-path applicability |
| D | Runtime scope/applicability, real-path remediation, reassessment submission | Explicit evidence-supported G-RUNTIME decision for relying paths |
| E | Audit/event design and approved platform capability implementations | Contracts, operation-specific policies and applicable Runtime/IAM prerequisites |
| F | Pure Customer domain candidate, then approved business services | Detailed rules and independent-scope approval for pure domain; full controls for adapters |
| G | Framework-neutral UX then approved Frontend modules/slices | OD-005/006/007; FE-BE authorization; live paths wait on Backend/IAM/Runtime |
| H | First Customer vertical slice then remaining approved cross-capability paths | Real contract/control evidence, no echo/mock substitute for E2E claims |
| I | Security requirements assessment in parallel, then acceptance execution | Explicit criteria, actual-path findings and distinct product/security/Gate decisions |
| J | Three independent profile dossiers and final release request | Measured OD-023 targets, applicable security/Gates and explicit Level 4 decisions |

## Deliberate non-dependencies

No Portal, Product Catalog, external registry/Linka, general Workflow Engine, AI, advanced analytics, public file sharing, external notification channels, general Admin UI, Full Air Gap or hosted plugin marketplace is silently added. Redis is optional and use-case justified. Business search is required; an external engine is not. Reporting needs approved Report Sets and source disclosure contracts, not cross-service SQL or universal synchronous per-record authorization. Topology is not inferred from fifteen logical capabilities.

## Planning boundaries

The proposed register is the executable-task specification candidate, not an execution order approval. Source requirements lacking detail are OPEN in each maturity row. Exact task authorization must cite approved requirements, allowed files/operations and applicable gates. Independent design is not blanket-blocked by G-RUNTIME; runtime reliance is never disguised as independent UI work. No timeline or staffing estimate is invented. See `critical-path.md`, `delivery-milestones.md`, and `product-decision-questions.md`.
