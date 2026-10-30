---
name: neshane-review
description: Review Neshane V3 changes for task scope, approved architecture, service boundaries, tenant isolation, contracts, and proportionate execution evidence.
---

# Neshane review

Apply when reviewing an implementation or before reporting an implementation task complete.

Read the root `AGENTS.md`, the standards matching changed files, and applicable approved V3 ADRs. Review only the requested Task ID and inspect narrowly. Check: unrelated changes; dependency direction; service/data ownership; cross-service imports or SQL; tenant propagation and owning-service authorization; secrets; DTO/entity separation; versioned contracts; error/log safety; configuration validation; tests written for the changed risks; and claims supported by evidence.

Report findings by severity with precise file locations, then list open decisions and unverified assumptions. If there are no findings, say so while retaining limitations. Follow the active `AGENTS.md` controlled-execution policy: execute only the exact local build, test, analysis, or isolated integration commands explicitly authorized by the current Task ID; otherwise provide manual commands. Never infer network/dependency-install permission, production access, deployment, CI/CD, publishing, or Git push authorization. Record commands, results, failures, skipped checks, resource assumptions, and evidence boundaries.

