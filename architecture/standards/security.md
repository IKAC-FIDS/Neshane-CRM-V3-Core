# Security standard

## Identity and authorization

- Authenticate user and workload identities at every service trust boundary; internal network location is not trust.
- Validate token signature, issuer, audience, expiry, and required claims according to an approved identity ADR.
- The owning service authorizes every operation and object. Gateways and upstream services cannot be the sole authorizer.
- Apply least privilege to application, migration, administrative, and integration identities.

## Tenant isolation

- Establish Tenant Context only from authenticated, validated membership or trusted workload provenance.
- Client-provided tenant headers or fields are selectors only. Missing, conflicting, or invalid context fails closed before domain or persistence work.
- Preserve the validated Tenant Context across synchronous calls, messages, jobs, logging, and persistence transactions.
- Enforce tenant isolation in application authorization and PostgreSQL RLS for tenant-owned data.

## Data and secrets

- Never commit secrets, credentials, private keys, tokens, or production values. Inject secrets through an approved external mechanism.
- Minimize sensitive data in APIs, events, logs, traces, and error responses; apply explicit redaction.
- Security-sensitive state changes require audit records with safe actor, tenant, action, target, outcome, and correlation data.

## Approval gaps

Identity provider, token/session lifecycle, authorization model, secret manager, audit retention, and cryptographic policies require approved V3 ADRs before production implementation.

