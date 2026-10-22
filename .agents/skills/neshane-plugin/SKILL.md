---
name: neshane-plugin
description: Implement or review Neshane V3 plugin manifests, installations, grants, Extension Gateway interactions, events, and hooks.
---

# Neshane plugin

Apply when a task changes plugin definitions, installation lifecycle, grants, Extension Gateway behavior, plugin events, or hooks.

Read the root `AGENTS.md` and all relevant API, security, messaging, persistence, and service standards. Confirm plugin ownership and the approved plugin ADR/contract; if none exists, limit work to an explicit proposal and do not invent the model. Treat manifests as untrusted input, validate version/capabilities, scope installations and grants to the validated tenant, enforce authorization in the owning service, and keep the gateway from bypassing domain ownership. Version hooks/events and make retries idempotent. Do not expose secrets to manifests, payloads, logs, or plugin code.

Deliver only the Task ID's requested contracts or implementation, relevant unexecuted security/lifecycle tests, configuration requirements, and approval gaps. Never run builds, tests, plugins, gateways, containers, or deployments.

