---
description: "Use when designing or reviewing Modular Monolith architecture, package-by-feature boundaries, JPA mapping, and Strangler Fig migration."
applyTo: "backend/src/main/java/**,backend/pom.xml,backend/build.gradle*"
---

# Modular Monolith Architecture Guide

This file activates when you work on Java source files or backend build configurations. It teaches the target architecture: a **Modular Monolith** — not microservices — with package-by-feature boundaries, bounded contexts, Adabas FDT to JPA mapping, Spring Boot 3.3 architectural conventions, and the Strangler Fig migration shape. It does **not** define controller, DTO, validation, or error-response details, which belong to [`backend.instructions.md`](backend.instructions.md); security belongs to [`security.instructions.md`](security.instructions.md); schema migrations belong to [`database.instructions.md`](database.instructions.md); and legacy-source reading belongs to [`natural-adabas.instructions.md`](natural-adabas.instructions.md).

## Core Principle: One Deployable, Many Modules

The target system is a single Spring Boot application with clear internal module boundaries. Each bounded context is a Maven module (or top-level package) that owns its domain, repository, and service layers.

Why a Modular Monolith rather than microservices:

- **Workshop constraint**: the 14:00-17:40 challenge window is not enough time to manage distributed systems, service discovery, and inter-service communication.
- **Complexity budget**: One deployable avoids distributed-service coordination while the team establishes ownership and migration behavior. This is a design rationale, not a measured cost/benefit percentage.
- **Migration path**: A well-structured Modular Monolith can be decomposed into microservices later if necessary. The reverse is much harder.

## Package-by-Feature Structure

Organize code by business capability, not by technical layer:

```
src/main/java/com/example/app/
├── <feature>/                  # Bounded context defined by the team
│   ├── domain/                # Behavior and owned interfaces
│   ├── application/           # Use cases and orchestration
│   └── infrastructure/        # REST, JPA and other adapters
├── shared/                     # Shared kernel
│   ├── audit/                  # Cross-cutting: audit trail
│   └── exception/              # Cross-cutting: error handling
└── Application.java            # Spring Boot entry point
```

Rules:

- A module MUST **NEVER** directly import internal classes from another module. Use interfaces or events.
- The `shared/` package contains only cross-cutting concerns (audit, exceptions, base entities).
- Add repositories, services and controllers only where the approved module behavior needs them.

## Bounded Context Boundaries

When deciding where to draw module boundaries, ask:

1. **Who owns this data?** If two features share the same table, they may belong to the same context.
2. **What changes together?** Actual change history can inform a boundary; a shared sprint or naming prefix does not establish one.
3. **What must be isolated?** Distinguish semantic ownership from runtime failure isolation; two packages in one process do not guarantee independent availability.

Treat Adabas file identifiers (FNRs) as source inventory, not predetermined bounded
contexts. The architects and DBA establish data ownership from program access
patterns, relationships, and business evidence before choosing module boundaries.

## Data Migration Architecture

Follow the participant [data migration lifecycle](../../docs/DATA-MIGRATION.md).
The DBA owns source readiness, profiling, extraction, target loading, and migration
evidence; architects co-design the contracts and recovery boundaries. QA verifies
source-to-target reconciliation independently, while PO/RE approve consultation
coverage and Developer exposes the migrated records through API and UI.

- Base the design on an authorized populated Adabas source and a consistent snapshot, not only DDM/FDT metadata or seed definitions.
- In the feature's `plan.md`, define the extraction contract, source-key lineage, field and relationship mappings, staging boundary, dependency-aware load order, reject handling, resumability, and target recovery.
- Preserve identifiers, leading zeros, precision, date/null semantics, encoding, and MU/PE occurrence meaning according to observed data and approved mappings. The examples below illustrate options, not ready-made SIFAP decisions.
- Separate Flyway schema evolution from record migration. An empty schema or newly generated PostgreSQL fixtures cannot prove an Adabas migration.
- Keep imported domain data behind its owning module's interfaces; do not expose staging tables directly as application APIs or bypass authorization for migration validation.
- Acceptance includes all beneficiaries in the agreed authorized population, with paginated listing, search, and detail queries over PostgreSQL. Rejected records must be accounted for, but unresolved beneficiary gaps still block complete consultation.
- Require independent reconciliation and tested rerun/recovery before C3 data acceptance. Keep source records and credentials out of Git, prompts, and public logs.

## JPA Mapping from Adabas FDT

### Simple Fields

| Adabas Format | Java Type | JPA Annotation |
|---|---|---|
| `A` (alphanumeric) | `String` | `@Column(length = N)` |
| `N` (numeric, no decimal) | `Long` or `Integer` | `@Column` |
| `N` (numeric, with decimal) | `BigDecimal` | `@Column(precision = P, scale = S)` |
| `P` (packed decimal) | `BigDecimal` | `@Column(precision = P, scale = S)` |
| `D` (date) | `LocalDate` | `@Column` |
| `T` (time/datetime) | `LocalDateTime` | `@Column` |
| `B` (binary) | `byte[]` | `@Column` / `@Lob` |

### MU fields: normalized mapping first

Use a related table or `@ElementCollection` when the reviewed value semantics fit:

```java
@ElementCollection
@CollectionTable(name = "person_alternate_names")
private List<String> alternateNames;
```

JSONB is an exception requiring reviewed evidence, not the automatic equivalent
of every MU field. Preserve occurrence identity/order where behavior needs it.

### PE (Periodic Groups) → @OneToMany

```java
@OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
@JoinColumn(name = "person_id")
private List<AddressHistory> addressHistory;  // Was PE group
```

Where `AddressHistory` is an `@Entity` with its own table.

## Spring Boot 3.3 Conventions

- **Constructor injection**: Use explicit constructors. Do not introduce Lombok without a dependency decision.
- **Records for DTOs**: `public record ResourceDto(Long id, String label) {}`
- **Validation in the controller layer**: `@Valid @RequestBody ResourceDto dto` with Bean Validation annotations on the DTO.
- **@Transactional only in the service layer**: NEVER in repositories, NEVER in controllers.
- **Optional for nullable returns**: `Optional<Resource> findById(Long id)` — NEVER return `null` from public methods.
- **Sealed interfaces for type unions**: `sealed interface ResourceState permits StateA, StateB {}`

## Error Handling Pattern

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ProblemDetail> handleNotFound(EntityNotFoundException ex) {
        ProblemDetail detail = ProblemDetail.forStatusAndDetail(
            HttpStatus.NOT_FOUND, ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(detail);
    }
}
```

Use `ProblemDetail` (RFC 7807) for all error responses.

## Strangler Fig Pattern

When the modern system must coexist with the legacy system:

1. **Facade**: All requests pass through a routing layer
2. **New path**: New or migrated features are handled by the Spring Boot modules
3. **Legacy path**: Unmigrated features are proxied to the legacy system
4. **Gradual migration**: As each feature is migrated, its route switches from legacy to modern

Document the coexistence boundary for the selected increment. Do not invent
an available legacy HTTP proxy or implement a facade the requirements do not
need. A planned integration is not an executed production cutover.

## Conventions

| Rule | Rationale |
|---|---|
| One Spring Boot deployable with many internal modules | Preserves workshop delivery speed while keeping boundaries explicit |
| Package by business capability | Modules map to bounded contexts instead of technical layers |
| Module internals stay private; cross-module access uses interfaces or events | Prevents hidden coupling between contexts |
| Adabas FDT types map deliberately to Java/JPA types | Avoids silent truncation, precision loss, and incorrect relationships |
| `@Transactional` only in services and constructor injection everywhere | Keeps persistence boundaries and dependencies explicit |
| `ProblemDetail` for errors | Gives every module one machine-readable error shape |

## Do / Do Not

| Do | Do not |
|---|---|
| Keep one Spring Boot application with clear internal modules | Create separate Spring Boot applications or microservices for each context |
| Put business logic in Java services | Move business logic into PostgreSQL stored procedures or functions |
| Use JPA/JPQL or Spring Data derived queries | Concatenate strings to build SQL |
| Use constructor injection | Use field injection with `@Autowired` |
| Return `Optional` when a result may be absent | Return `null` from public methods |
| Support partial migration with a Strangler Fig facade | Assume the whole legacy system is migrated at once |

## Checklist Before Opening a PR

- [ ] New code is inside one Spring Boot deployable and organized by business capability
- [ ] No module imports another module's internal classes directly; interfaces or events define the boundary
- [ ] Repositories, services, controllers, entities, and DTOs stay inside the owning module or shared kernel
- [ ] Adabas FDT fields were mapped to Java/JPA types with precision, MU, PE, and descriptor semantics preserved
- [ ] DBA and architects reviewed snapshot/extraction, source-key lineage, staging/load, and recovery contracts using measured data evidence
- [ ] QA verified source-to-target reconciliation and complete authorized beneficiary queries; schema-only migrations or fixture-only tests did not substitute for acceptance
- [ ] `@Transactional` appears only in services, dependencies use constructor injection, and public methods do not return `null`
- [ ] The design can coexist with unmigrated legacy paths through the Strangler Fig routing shape
