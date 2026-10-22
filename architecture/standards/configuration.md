# Configuration standard

## Sources and naming

- Keep non-secret defaults in `application.yml`; use Spring Boot externalized configuration for environment-specific values.
- Configuration keys use lowercase kebab-case and domain-oriented namespaces.
- Bind related settings to validated typed configuration properties; fail startup on missing or invalid required values.
- Keep environment selection outside the artifact. Do not bake production endpoints or credentials into source.

## Safety

- Secrets are supplied by an approved external mechanism and must never appear in committed configuration, examples, logs, or error messages.
- Define explicit timeouts, limits, retry policies, and feature defaults at the owning integration; avoid unlimited or ambiguous defaults.
- Sensitive or authorization-affecting configuration fails closed when unavailable.
- Configuration changes that alter architecture, trust, data ownership, or public contracts require review and possibly an ADR.

## Proposed choices requiring approval

Profile strategy, secret provider, configuration refresh policy, environment variable naming prefix, and centralized configuration mechanism.

