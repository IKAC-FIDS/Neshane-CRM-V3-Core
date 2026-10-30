# ADR-V3-013: Backend foundation toolchain and build layout

- Status: ACCEPTED
- Authoring task: V3-005
- Authoring task status: CLOSED — ENGINEERING FOUNDATION R0 BASELINE; Backend commit `8f1cfaca40c0471a03418831aacfbe2689417cad`
- Related decision/open decision: DEC-013; OD-002, OD-003, OD-004
- Decision owner: Technical Architecture Owner / CPO
- Required approval authority: Technical Architecture Owner under the accepted Level 2 protocol
- Approval disposition: ACCEPTED
- Approval provenance: Explicit Technical Architecture Owner/CPO direction in V3-005
- Effective date: 2026-10-30 upon traceable commit of this decision package
- Architecture revision: `NESHANE-V3-ARCH-P00-003`
- Supersedes: None
- Superseded by: None
- Independent Security/Quality/Operations approval: Not claimed

## Context and scope

ADR-V3-001 established Java/Spring Boot independent Business Services but left the Java version, Spring Boot version, build system and project layout open as OD-002 through OD-004. V3-005 requires a reproducible Backend engineering foundation before source or build initialization.

This decision applies to the independent Backend repository and its engineering foundation. It does not define Business Service topology, API/event contracts, persistence, identity, deployment infrastructure or Production Readiness.

## Decision

### OD-002 — Java baseline

Use **Java 21 LTS** as the Backend source, compiler and runtime compatibility baseline. Build configuration must use an explicit Java toolchain and must not depend implicitly on the developer machine's default JDK.

### OD-003 — Spring Boot baseline

Use **Spring Boot 4.1.2** as the initial Backend framework dependency baseline. Dependency versions managed by Spring Boot must use its published dependency management rather than independently drifting versions.

Approval of the architectural version choice is separate from verification of remote artifacts, BOM coordinates, transitive dependencies, signatures or repository availability. Those must be verified from authoritative distribution sources before the first dependency-resolving build.

### OD-004 — Build system and layout

Use a **Gradle multi-project build with Groovy DSL and the Gradle Wrapper**. The Wrapper distribution version, checksum and URL must be pinned from authoritative Gradle evidence during V3-005 implementation; none is selected or fabricated by this decision.

The multi-project root is an engineering aggregator and conventions boundary, not a shared Business Service runtime or release unit. Each defined Business Service retains its own build/test boundary, artifact, version and release path. Cross-service implementation dependencies and shared business logic remain forbidden.

## Alternatives and rationale

### OD-002 alternatives

Other supported Java LTS or non-LTS releases were possible. Java 21 LTS was selected for a stable long-term foundation, current language/runtime capabilities and reduced upgrade churn compared with a non-LTS baseline. Exact vendor distribution remains an implementation/operations choice.

### OD-003 alternatives

Other stable Spring Boot lines or delayed framework selection were possible. Spring Boot 4.1.2 was explicitly selected by the Technical Architecture Owner to establish one dependency baseline for the first foundation. Repository policy prevented network verification during this task, so release existence and Java/Gradle compatibility require authoritative verification before dependency resolution.

### OD-004 alternatives and Developer Experience considerations

Maven, Gradle Kotlin DSL, independent unrelated builds and a single-project layout were considered alternatives represented by OD-004. Gradle multi-project with Groovy DSL was selected to support centralized domain-neutral build conventions, discoverable module tasks, consistent formatting/boundary checks and an incremental path for multiple independently owned modules.

The Gradle Wrapper reduces developer workstation prerequisites and supports a reproducible pinned distribution. Developer Experience evidence considered here is limited to the accepted repository standards and the V3-005 roadmap direction; no separate Developer Experience reviewer disposition is claimed. Current governance assigns final Level 2 toolchain authority to the Technical Architecture Owner and contains no mandatory separate DX approval gate.

## Consequences

- V3-005 may create the Backend Gradle foundation only after this package is committed and the Backend local architecture reference is synchronized to `NESHANE-V3-ARCH-P00-003`.
- A pinned Wrapper distribution, checksum and authoritative source remain required implementation evidence.
- Spring Boot 4.1.2 coordinates and compatibility with Java 21 and the selected Gradle distribution must be verified before the first dependency-resolving build.
- Root conventions may standardize compilation, reproducibility, formatting and dependency-boundary checks, but may not create shared business implementation.
- A root aggregate build is permitted for developer/CI convenience; a Business Service release must remain targetable without rebuilding unrelated Business Services.
- Architecture approval does not prove that the toolchain is installed, downloadable, secure, executable or production-ready.

## Compatibility and consumer impact

There is no existing V3 Backend application or published Backend build contract to migrate. Backend contributors and future CI become consumers of the pinned Java/Gradle conventions. Backend local governance currently references `NESHANE-V3-ARCH-P00-002` and must be synchronized before architecture-sensitive implementation proceeds.

This decision does not change API, event, database, SDK or external integration contracts.

## Migration and rollback/forward recovery

No runtime data migration exists. Before implementation evidence is accepted, a clean checkout must be able to obtain the approved Wrapper distribution from its recorded authoritative source and execute module-scoped tasks using Java 21.

If authoritative verification shows that Spring Boot 4.1.2 or the future pinned Gradle distribution is unavailable or incompatible, implementation must stop and a new Level 2 decision must amend or supersede this ADR; silent substitution is prohibited.

## Verification expectations

Later V3-005 evidence must include the committed Wrapper scripts/JAR/properties, pinned distribution and checksum, Java toolchain configuration, dependency management, reproducible clean build, formatting and module-boundary checks, dependency reporting, and proof that representative modules can be built without forbidden cross-module implementation dependencies.

No build, test, dependency download or runtime verification was executed by this decision task.

## Traceability

Related: V3-005; DEC-001; DEC-002; DEC-012; DEC-013; OD-002; OD-003; OD-004; ADR-V3-001; ADR-V3-002; ADR-V3-011; ADR-V3-012; V3-006 Level 2 protocol; repository-structure and Java coding standards.
