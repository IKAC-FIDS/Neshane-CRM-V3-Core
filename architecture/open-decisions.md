# Neshane V3 open decisions

Status: Open. None of the alternatives below is approved. Milestones are latest responsible decision points, not implementation authorization.

| ID | Decision and alternatives | Trade-offs / affected boundaries | Milestone | Proposed owner | Cost of postponement |
| --- | --- | --- | --- | --- | --- |
| OD-001 | Full Air-Gapped support: offline-capable only; import/export bridge; fully isolated release channel | Sovereign, Operations, Identity, Plugins; isolation versus update/support complexity | Before an Air-Gapped commitment | Architecture + Sovereign Operations + Security | Cannot claim Air-Gapped support or finalize release/trust flows |
| OD-002 | Java version: supported LTS candidates | Backend compatibility, performance, support lifetime | Before Backend build initialization | Backend Architecture | Blocks compiler/toolchain baseline |
| OD-003 | Spring Boot version: supported stable line candidates | Ecosystem/security support versus dependency compatibility | Before Backend build initialization | Backend Architecture | Blocks dependency and runtime baseline |
| OD-004 | Gradle vs Maven; single/multi-project structure | Build ergonomics, boundaries, caching and team familiarity | Before Backend build initialization | Backend Architecture + Developer Experience | Blocks reproducible build layout |
| OD-005 | Frontend framework/rendering: React/Angular/Vue/other; SPA/SSR variants | UX, deployment, skills, accessibility and operations | Before first Frontend source | Frontend Architecture + Product UX | Blocks frontend implementation |
| OD-006 | State/server-cache/UI libraries: library or framework-native approaches | Consistency/productivity versus lock-in and bundle complexity | Before first affected feature/design system | Frontend Architecture + UX | Risks incompatible local patterns if delayed past coding |
| OD-007 | Public API and GraphQL BFF: REST-first, GraphQL BFF, hybrid, or per-client boundary | Composition, compatibility, security, performance and ownership | Before first public contract | API Architecture + Backend/Frontend owners | Blocks stable client/service contracts |
| OD-008 | API/event versioning: URI/header/media type; schema/envelope evolution rules | Clarity and compatibility versus operational complexity | Before first published contract/event | API + Event Architecture | Creates irreversible incompatible contracts if late |
| OD-009 | IdP integrations: generic OIDC first versus named enterprise providers/federation | Reach and conformance versus implementation/support breadth | Before production authentication | Identity + Security + Product | Blocks production trust onboarding |
| OD-010 | Session lifecycle/revocation: stateless short-lived, stateful sessions, refresh families, hybrid | UX, revocation speed, compromise recovery and Sovereign operation | Before production session implementation | Identity + Security | Blocks safe session semantics and frontend credential design |
| OD-011 | Workload identity: platform-issued credentials, mTLS PKI, SPIFFE/SPIRE, hybrid | Portability/automation versus operational complexity | Before production service-to-service trust | Security + Platform Operations | Blocks durable trust-domain and rotation design |
| OD-012 | Secrets/keys: platform-native, Vault-class, cloud KMS/HSM, Sovereign-local mix | Portability, assurance, custody and offline support | Before production credential storage/signing | Security + Operations + Sovereign owner | Blocks key lifecycle and release assurance |
| OD-013 | PostgreSQL migrations: Flyway, Liquibase, framework-native, other | Control/repeatability versus flexibility and tooling footprint | Before first schema migration | Data Architecture | Blocks migration ownership and recovery convention |
| OD-014 | Java/RLS integration: transaction interceptor, explicit unit-of-work, connection wrapper | Safety/visibility versus framework coupling | Before first tenant-aware repository | Data + Security + Backend Architecture | Risks unsafe pooled connection context if improvised |
| OD-015 | Runtime orchestration: Compose-equivalent reference, Kubernetes, Nomad, other profile-specific runtime | Portability/operations/Sovereign footprint versus complexity | Before deployment implementation | Platform Operations + Architecture | Blocks deployment, cell and recovery contracts |
| OD-016 | Managed Plugin Runtime isolation: containers, microVMs, WASM, external workers, hybrid | Language support, density, isolation and operations | Before hosted plugin execution | Plugin Platform + Security + Operations | Cannot offer managed plugin execution safely |
| OD-017 | Object storage: S3-compatible, cloud-specific, filesystem appliance, hybrid | Portability, sovereignty, lifecycle and authorization | Before file/content capability | Data + Operations + Security | Blocks durable object and retention design |
| OD-018 | Search/indexing: PostgreSQL search, external engine, hybrid projections | Capability/cost/consistency and Sovereign footprint | Before search-dependent feature | Data Architecture + owning domains | Risks premature engine coupling or inadequate search |
| OD-019 | Background scheduling: in-service scheduler, DB-coordinated jobs, workflow engine, broker scheduling | Simplicity versus durability, ownership and operations | Before durable scheduled workflows | Backend Architecture + Operations | Risks duplicate/lost work and unclear ownership |
| OD-020 | Contract testing: schema diff, consumer-driven, provider conformance, combination | Coverage and independence versus maintenance cost | Before first released contract | API/Event Architecture + Quality | Compatibility cannot be objectively gated |
| OD-021 | Marketplace/Developer Portal: internal catalog, partner portal, public marketplace | Governance/revenue/ecosystem versus security/support scope | Before external developer onboarding | Product + Plugin Platform + Legal/Security | External ecosystem scope and obligations remain unknown |
| OD-022 | Tenant migration automation: offline transfer, dual-run, event replication, cell-native workflow | Downtime, consistency, complexity and rollback | Before tenant placement migration is supported | Cell Management + Data + Security | Placement changes remain manual/high-risk |
| OD-023 | SLO/RTO/RPO/capacity: per-profile/service objectives and measurement | Cost versus availability/recovery/security freshness | Before production architecture sign-off | Product + Operations + Security + service owners | Production readiness and sizing cannot be assessed |

Decisions require documented evidence, consequences, owner approval, a V3 ADR where material, and updates to the [decision register](decision-register.md), [baseline](baseline-v3.md), and affected repository baseline references.

## Status and dependency map

Every item is currently **Open**.

| ID | Dependencies |
| --- | --- |
| OD-001 | DEC-003, DEC-004, OD-012, OD-015 |
| OD-002 | DEC-001 |
| OD-003 | DEC-001, OD-002 |
| OD-004 | DEC-001, DEC-002, OD-002, OD-003 |
| OD-005 | DEC-009, OD-007 |
| OD-006 | DEC-009, OD-005 |
| OD-007 | DEC-008, DEC-009 |
| OD-008 | DEC-006, DEC-007, DEC-008, OD-007 |
| OD-009 | DEC-005, DEC-004 |
| OD-010 | DEC-005, DEC-009, OD-009 |
| OD-011 | DEC-004, DEC-005, OD-015 |
| OD-012 | DEC-004, DEC-005, DEC-010 |
| OD-013 | DEC-007, OD-004 |
| OD-014 | DEC-005, DEC-007, OD-004, OD-013 |
| OD-015 | DEC-003, DEC-004, DEC-010, OD-023 |
| OD-016 | DEC-006, DEC-010, OD-012, OD-015 |
| OD-017 | DEC-002, DEC-003, DEC-010, OD-015 |
| OD-018 | DEC-002, DEC-003, OD-015, OD-023 |
| OD-019 | DEC-002, DEC-007, OD-015, OD-023 |
| OD-020 | DEC-008, DEC-012, OD-007, OD-008 |
| OD-021 | DEC-006, OD-016 |
| OD-022 | DEC-003, DEC-004, DEC-007, OD-015, OD-023 |
| OD-023 | DEC-003, DEC-004, DEC-010, DEC-012 |

