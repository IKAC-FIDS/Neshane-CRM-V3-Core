---
name: neshane-security
description: Implement or review Neshane V3 identity, workload authentication, Tenant Context, authorization, secrets, or audit-sensitive behavior.
---

# Neshane security

Apply to authentication, Tenant Context, authorization, service identity, secret handling, or security audit changes.

Read the root `AGENTS.md` plus `architecture/standards/security.md` and every changed boundary's standard. Identify the trust boundary, identity, tenant provenance, owning-service authorization, denial behavior, and sensitive data before editing. Fail closed on missing or conflicting context. Never treat a client tenant header, gateway decision, or internal network as authority. Preserve context through calls/messages/transactions, use least privilege, and redact logs and errors. Do not invent token, session, cryptographic, or retention policy; mark missing choices for architecture/security approval.

Deliver the security path, denial cases, relevant unexecuted tests, configuration requirements without secret values, and unresolved threat assumptions. Never run builds, tests, services, containers, or deployments.

