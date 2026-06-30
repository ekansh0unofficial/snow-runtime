# Snow Runtime - Architecture v1.0

## Vision

Snow Runtime is a **CLI-first runtime for Snowflake** inspired by tools such as Git, Docker and Firebase.

Rather than being another SQL client, Snow Runtime provides a long-running authenticated runtime that manages Snowflake sessions, context, metadata exploration and query execution. Multiple interfaces consume the same Runtime, ensuring a single implementation of business logic.

---

# High-Level Architecture

```text
                     Deployment
─────────────────────────────────────────────────
PyPI      Homebrew      VS Marketplace

                     │

                    Distribution
─────────────────────────────────────────────────
pip      pipx      uv tool      VS Code Extension

                     │

                     Consumers
─────────────────────────────────────────────────
Terminal      VS Code      Python      CI/CD

                     │

                     Interfaces
─────────────────────────────────────────────────
CLI
Terminal UI (TUI)
Web UI

                     │

                Application Layer
─────────────────────────────────────────────────
Runtime
Config
Context
SQL
Transaction
Metadata
Explore
Data
History
Logs
Doctor

                     │

                  Services Layer
─────────────────────────────────────────────────
Core Services
Supporting Services

                     │

                    Domain Layer
─────────────────────────────────────────────────
Entities
Value Objects
Enums
Exceptions

                     │

                  Provider Layer
─────────────────────────────────────────────────
Snowflake, Configuration, Secret
History, Logging, Runtime, Process
File, Cache

                     │

          Snowflake + External Systems
```

---

# Deployment

Deployment defines **where Snow Runtime is published**.

| Deployment     | Purpose                              |
| -------------- | ------------------------------------ |
| PyPI           | Official Python package distribution |
| Homebrew       | macOS/Linux installation             |
| VS Marketplace | VS Code integration                  |

Deployment is purely a publishing concern.

---

# Distribution

Distribution defines **how users install or obtain Snow Runtime**.

| Distribution      | Purpose                            |
| ----------------- | ---------------------------------- |
| pip               | Python package installation        |
| pipx              | Standalone CLI installation        |
| uv tool           | Standalone isolated installation   |
| VS Code Extension | Runtime integration inside VS Code |

Distribution is an installation mechanism and is independent of the runtime architecture.

---

# Consumers

Consumers represent **where the Runtime is consumed**.

| Consumer        | Description                           |
| --------------- | ------------------------------------- |
| Terminal        | Primary execution environment         |
| VS Code         | IDE integration through the extension |
| Python          | Runtime consumed as a Python SDK      |
| CI/CD Pipelines | Automation and scripting              |

Consumers invoke the Runtime but do not contain business logic.

---

# Interfaces

Interfaces define **how users interact with the Runtime**.

## CLI

Primary interface.

Responsibilities:

* Runtime management
* SQL execution
* Configuration
* Context management
* Data operations
* Metadata commands
* Diagnostics

---

## Terminal UI (TUI)

Interactive metadata explorer.

Responsibilities:

* Browse databases
* Browse schemas
* Browse tables
* Inspect columns
* Explore relationships
* Preview data

The TUI is launched from the CLI and shares the same Runtime.

---

## Web UI

Browser-based interface.

Will expose the same Runtime capabilities as the TUI while providing richer visualization and navigation.

---

# Application Layer

The Application Layer defines **what the Runtime can do**.

Each application represents a business capability that is independent of the user interface.

| Application | Scope                                                            |
| ----------- | ---------------------------------------------------------------- |
| Runtime     | Runtime lifecycle, daemon management and active sessions         |
| Config      | Connection profiles and authentication configuration             |
| Context     | Active database, schema, warehouse and role                      |
| SQL         | SQL execution from commands, files or stdin                      |
| Transaction | Transaction lifecycle (begin, commit, rollback)                  |
| Metadata    | Discover and inspect Snowflake objects                           |
| Explore     | Interactive metadata exploration through the TUI or Web UI       |
| Data        | Preview, profiling, statistics and export operations             |
| History     | Command and query history                                        |
| Logs        | Runtime logging and diagnostics logs                             |
| Doctor      | Runtime health checks and environment validation                 |

Each application may use multiple Services internally but exposes a single cohesive capability to the user.

---

# Services Layer

The Services Layer contains the **business logic** of Snow Runtime.

Services implement the capabilities exposed by the Application Layer.

Responsibilities:

* Implement business rules.
* Coordinate workflows across multiple services.
* Operate on Domain Models.
* Use Providers for all external communication.
* Remain independent of CLI, TUI and other interfaces.

The Application Layer orchestrates Services, while Services collaborate with one another to complete business operations.

---

## Core Services

Core Services implement the primary business capabilities of Snow Runtime.

| Service               | Responsibility                                                                          |
| --------------------- | --------------------------------------------------------------------------------------- |
| Configuration Service | Manage connection profiles and runtime configuration.                                   |
| Session Service       | Authentication, session lifecycle, daemon management, MFA reuse and connection reuse.   |
| Context Service       | Manage the active database, schema, warehouse and role.                                 |
| Execution Service     | Execute SQL, transactions, query cancellation and result streaming.                     |
| Catalog Service       | Discover databases, schemas, tables, views, warehouses and roles.                       |
| Schema Service        | Inspect object structure including columns, constraints and dependencies.               |
| Data Service          | Preview data, profiling, statistics, duplicate detection and candidate PK/FK discovery. |
| History Service       | Maintain command history and query history.                                             |
| Logging Service       | Structured runtime logging.                                                             |
| Diagnostics Service   | Validate runtime health, connectivity and environment configuration.                    |

---

## Supporting Services

Supporting Services assist Core Services but do not implement primary business capabilities.

| Service                   | Responsibility                                                                           |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| Secret Service            | Secure storage and retrieval of credentials using the operating system credential store. |
| Export Service            | Export Query Results to CSV, JSON and Parquet.                                           |
| Object Resolution Service | Resolve partially qualified object names using the active Context.                       |

---

## Application → Service Mapping

| Application | Primary Service(s)              | Supporting Services                                            |
| ----------- | ------------------------------- | -------------------------------------------------------------- |
| Runtime     | Session Service                 | Configuration, Secret, Logging, Diagnostics                    |
| Config      | Configuration Service           | Secret                                                         |
| Context     | Context Service                 | Session, Catalog                                               |
| SQL         | Execution Service               | Session, Context, History, Logging, Export                     |
| Transaction | Execution Service               | Session, Context, History                                      |
| Metadata    | Catalog Service, Schema Service | Context, Object Resolution                                     |
| Explore     | Catalog Service, Schema Service | Context, Data, Object Resolution                               |
| Data        | Data Service                    | Execution, Context, Catalog, Schema, Export, Object Resolution |
| History     | History Service                 | Logging                                                        |
| Logs        | Logging Service                 | —                                                              |
| Doctor      | Diagnostics Service             | Session, Configuration, Secret                                 |

---

## Service Collaboration Examples

Applications should invoke as few Services as possible.

Services collaborate with one another to complete business workflows.

### Example 1: SQL Execution

```text
SQL Application
        │
        ▼
Execution Service
        │
        ├── Session Service
        ├── Context Service
        ├── History Service
        └── Logging Service
```

### Example 2: Data Preview & Analysis

```text
Data Application
        │
        ▼
Data Service
        │
        ├── Execution Service
        ├── Catalog Service
        ├── Schema Service
        ├── Context Service
        ├── Export Service
        └── Object Resolution Service
```

### Example 3: Metadata Exploration

```text
Metadata Application
        │
        ▼
Catalog Service
        │
        ├── Schema Service
        ├── Context Service
        └── Object Resolution Service
```

This keeps the Application Layer lightweight while allowing Services to encapsulate business workflows.

---

## Service Design Principles

1. Every Service owns a single business capability.
2. Services may collaborate with other Services.
3. Applications orchestrate; Services implement.
4. Services never communicate directly with Interfaces.
5. Providers are the only layer allowed to communicate with external systems.
6. Services operate exclusively on shared Domain Models.
7. Supporting Services enable Core Services but do not implement business workflows.

---

# Domain Layer

The Domain Layer defines the business model of Snow Runtime.

Every layer communicates using Domain Objects rather than dictionaries, tuples or third-party library objects.

Providers convert external data into Domain Objects, while Services operate exclusively on these objects.

The Domain Layer is independent of:

* Interfaces
* Applications
* Services
* Providers
* Snowflake Connector

It represents the common language shared across the entire Runtime.

---

## Entities

Entities have unique identity and lifecycle. They encapsulate business entities that change over time.

### Configuration Entities

| Entity              | Responsibility                                                |
| ------------------- | ------------------------------------------------------------- |
| ConnectionProfile   | Snowflake connection profile and authentication configuration |
| SavedContext        | Named reusable context configuration                          |

### Runtime Entities

| Entity   | Responsibility                                |
| -------- | --------------------------------------------- |
| Session  | Authenticated Snowflake connection            |
| Database | Database metadata and structure                |
| Schema   | Schema metadata and structure                  |
| Table    | Table metadata, columns, and constraints      |

### Infrastructure Entities

| Entity    | Responsibility                          |
| --------- | --------------------------------------- |
| Command   | Executed Runtime command                |
| HistoryEntry | Stored command or query history     |
| LogEntry  | Runtime log entry                       |

---

## Value Objects

Value Objects are immutable and have no identity. They represent domain values passed between services.

| Object              | Responsibility                                                |
| ------------------- | ------------------------------------------------------------- |
| Context             | Active database, schema, warehouse, and role                  |
| Query               | SQL execution request                                         |
| QueryResult         | Result of SQL query execution (see expanded definition below) |
| Column              | Column metadata (name, type, nullable, etc.)                  |
| Constraint          | Table constraint (primary key, foreign key, unique)           |
| Dependency          | Object dependency relationship                               |
| DataProfile         | Dataset profiling and statistical information                |
| ColumnStatistics    | Statistical information for a column                          |
| RuntimeStatus       | Runtime process status and information                        |
| ExportJob           | Export operation state and metadata                           |

---

### QueryResult (Detailed)

The most frequently used domain object. Returned by Execution Service and used throughout the Runtime.

**Properties:**

* `query_id` (string) - Unique query identifier
* `query_text` (string) - SQL text executed
* `columns` (List[Column]) - Result column metadata
* `rows` (Iterator[Row]) - Result rows (lazy-loaded or streamed for large result sets)
* `row_count` (int) - Total number of result rows
* `execution_time_ms` (int) - Query execution time in milliseconds
* `metadata` (dict) - Query statistics (bytes_scanned, rows_produced, etc.)
* `error` (Optional[ExecutionError]) - Error information if query failed
* `status` (QueryStatus) - RUNNING, COMPLETED, FAILED, CANCELLED

---

## Enumerations

Enumerations eliminate magic strings throughout the application.

| Enumeration    | Values |
| -------------- | ------ |
| SessionState   | ACTIVE, IDLE, EXPIRED, CLOSED |
| TransactionState | ACTIVE, COMMITTED, ROLLED_BACK |
| RuntimeState   | STARTING, RUNNING, SHUTTING_DOWN, STOPPED |
| WarehouseState | RUNNING, SUSPENDED, RESIZING |
| ExportFormat   | CSV, JSON, PARQUET |
| LogLevel       | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| ObjectType     | TABLE, VIEW, ICEBERG_TABLE, DYNAMIC_TABLE, TEMPORARY_TABLE |
| ConstraintType | PRIMARY_KEY, FOREIGN_KEY, UNIQUE, CHECK |
| QueryStatus    | RUNNING, COMPLETED, FAILED, CANCELLED |

---

## Exceptions

All Runtime exceptions inherit from a common base exception.

| Exception | Responsibility |
| --------- | --------------- |
| SnowRuntimeError | Base exception for all Runtime errors |
| AuthenticationError | Authentication or credential issues |
| ConfigurationError | Invalid configuration or missing profiles |
| ContextError | Context switching or validation errors |
| ExecutionError | SQL execution failures |
| MetadataError | Metadata discovery or inspection failures |
| ExportError | Data export operation failures |
| ObjectNotFoundError | Requested object not found in Snowflake |
| SessionError | Session lifecycle errors |

External exceptions from third-party libraries (Snowflake Connector, OS, filesystem) should never propagate beyond the Provider Layer. Providers convert third-party exceptions into Domain Exceptions.

---

## Domain Relationships

```text
ConnectionProfile
        │
        ▼
Session
        │
        ▼
Context
        │
        ▼
Query
        │
        ▼
QueryResult

Database
    │
    ├── Schema
    │   │
    │   ├── Table
    │   │   │
    │   │   ├── Column
    │   │   ├── Constraint
    │   │   └── Dependency
    │   │
    │   └── View
    │       │
    │       ├── Column
    │       └── Dependency
    │
    └── Warehouse / Role

Table
    │
    ▼
DataProfile
    │
    ▼
ColumnStatistics
```

---

## Domain Object Principles

1. Domain Objects represent business concepts.
2. Domain Objects never contain infrastructure logic.
3. Domain Objects are independent of Snowflake Connector classes.
4. Domain Objects are immutable whenever practical.
5. Every layer communicates using Domain Objects.
6. Providers convert external data into Domain Objects.
7. Services operate exclusively on Domain Objects.
8. Entities have identity and lifecycle; Value Objects do not.
9. Exceptions inherit from a common base.

---

# Provider Layer

The Provider Layer is responsible for communicating with external systems.

Providers abstract third-party libraries, operating system APIs, storage mechanisms and external services from the rest of the Runtime.

Business logic **must never** exist inside Providers.

Instead, Providers expose a clean API to the Services Layer while hiding implementation details.

Responsibilities:

- Communicate with external systems.
- Convert external responses into Domain Models.
- Hide implementation details.
- Isolate third-party libraries.
- Never contain business rules.

The Services Layer depends on Providers, while Providers never depend on Services.

---

## Provider Overview

| Provider | External System | Used By |
|----------|-----------------|---------|
| Snowflake Provider | Snowflake Connector | Session, Execution, Catalog, Schema, Data |
| Configuration Provider | Configuration Files (TOML) | Configuration, Context |
| Secret Provider | Operating System Credential Store | Secret, Session |
| History Provider | SQLite | History |
| Logging Provider | Filesystem | Logging |
| Runtime Provider | IPC Socket | Runtime, Diagnostics |
| Process Provider | Operating System | Runtime, Diagnostics |
| File Provider | Filesystem | Export, SQL |
| Cache Provider | SQLite (reserved) | Catalog, Schema |

---

## Snowflake Provider

The Snowflake Provider is the primary integration point with Snowflake.

This is the **only** component that directly communicates with the Snowflake Python Connector.

Responsibilities:

- Establish connections
- Authenticate users
- Execute SQL
- Execute metadata queries
- Execute transactions
- Stream results
- Cancel running queries
- Manage Snowflake sessions

No other layer should directly import or use the Snowflake Connector.

---

## Configuration Provider

Responsible for persistent runtime configuration.

Owns:

- config.toml
- contexts.toml

Responsibilities:

- Read configuration
- Write configuration
- Update configuration
- Validate configuration
- Configuration migrations

---

## Secret Provider

Responsible for secure credential storage.

Uses:

- Windows Credential Manager
- macOS Keychain
- Linux Secret Service

Responsibilities:

- Store credentials
- Retrieve credentials
- Delete credentials

Passwords are never stored inside configuration files.

---

## History Provider

Responsible for persistent history storage.

Owns:

- history.db (SQLite)

Responsibilities:

- Store command history
- Store query history
- Retrieve history
- Delete history
- Search history

---

## Logging Provider

Responsible for runtime logging.

Owns:

- Runtime log files

Responsibilities:

- Write logs
- Read logs
- Rotate logs
- Archive logs

Logging implementation remains hidden from Services.

---

## Runtime Provider

Responsible for Runtime communication.

Owns:

- Local IPC Socket

Responsibilities:

- Send Runtime requests
- Receive Runtime responses
- Serialize requests
- Deserialize responses
- Runtime communication protocol

Every Interface communicates with the Runtime through this Provider.

---

## Process Provider

Responsible for interacting with the operating system.

Responsibilities:

- Start Runtime
- Stop Runtime
- Restart Runtime
- Runtime status
- Process discovery
- PID management

This Provider abstracts platform-specific process management.

---

## File Provider

Responsible for general filesystem operations.

Responsibilities:

- Read SQL files
- Write exported files
- Temporary files
- File validation

Business logic for exporting remains inside the Export Service.

The File Provider is only responsible for filesystem interaction.

---

## Cache Provider (Reserved)

Responsible for metadata and schema caching.

Owns:

- cache.db (SQLite)

Responsibilities:

- Cache metadata queries
- Invalidate stale caches
- Store schema information
- Manage cache lifecycle

Currently reserved for future use. Will optimize metadata-heavy operations.

---

## Service → Provider Mapping

| Service | Provider(s) |
|----------|-------------|
| Configuration Service | Configuration Provider |
| Session Service | Snowflake Provider, Secret Provider |
| Context Service | Configuration Provider |
| Execution Service | Snowflake Provider |
| Catalog Service | Snowflake Provider, Cache Provider (reserved) |
| Schema Service | Snowflake Provider, Cache Provider (reserved) |
| Data Service | Snowflake Provider |
| History Service | History Provider |
| Logging Service | Logging Provider |
| Diagnostics Service | Runtime Provider, Process Provider, Configuration Provider |
| Secret Service | Secret Provider |
| Export Service | File Provider |
| Object Resolution Service | — |

---

## Provider Design Principles

1. Providers never contain business logic.
2. Providers communicate with a single external system.
3. Providers hide implementation details.
4. Providers isolate third-party libraries.
5. Providers convert external data into Domain Models.
6. Services communicate with Providers instead of external systems directly.
7. Providers should be replaceable without affecting the Services Layer.

---

## Dependency Flow

```text
Interface
      │
      ▼
Application
      │
      ▼
Services
      │
      ▼
Domain Models
      │
      ▼
Providers
      │
      ▼
External Systems

Snowflake
Filesystem
SQLite
Operating System
Credential Store
IPC Socket
```

---

## External Systems

The Runtime interacts with the following external systems through Providers only.

| External System | Provider |
|-----------------|----------|
| Snowflake | Snowflake Provider |
| Filesystem | Configuration, Logging, File Providers |
| SQLite | History, Cache Providers |
| Operating System | Process Provider |
| Credential Store | Secret Provider |
| IPC Socket | Runtime Provider |

No Service, Application or Interface may directly communicate with these systems.

---

# Runtime Flow

This section illustrates how requests flow through the entire architecture. Understanding these flows validates that all layers work together correctly.

---

## Flow 1: SQL Execution (`snow sql`)

```text
User types:  snow sql "SELECT * FROM my_table"
                 │
                 ▼
            CLI Interface
                 │
                 ▼
           SQL Application
                 │
        ┌────────┴────────┐
        ▼                 ▼
 Resolve Session    Resolve Context
        │                 │
        └────────┬────────┘
                 ▼
        Execution Service
                 │
        ┌────────┼────────┬──────────┐
        ▼        ▼        ▼          ▼
     Session  Context  History    Logging
     Service  Service  Service    Service
        │        │        │          │
        └────────┼────────┼──────────┘
                 ▼
         Snowflake Provider
                 │
                 ▼
            Snowflake
                 │
                 ▼
          QueryResult (Domain)
                 │
        ┌────────┴────────┐
        ▼                 ▼
    Rich Table        History Entry
   (CLI Output)        (Stored)
```

---

## Flow 2: Metadata Exploration (`snow explore`)

```text
User runs:   snow explore
                 │
                 ▼
            CLI Interface
                 │
                 ▼
       Launch Explore Application
       (Catalog + Schema Services)
                 │
        ┌────────┴─────────┐
        ▼                  ▼
  Catalog Service    Schema Service
        │                 │
        ├── Session       ├── Session
        ├── Context       ├── Execution
        └── Snowflake     └── Snowflake
            Provider          Provider
                 │                 │
                 └────────┬────────┘
                 ▼
    Domain Objects (Database, Schema, Table, Column)
                 │
                 ▼
         Textual UI (TUI)
                 │
                 ▼
       Interactive Terminal Display
```

---

## Flow 3: Runtime Startup (`snow runtime start`)

```text
User runs:   snow runtime start
                 │
                 ▼
            CLI Interface
                 │
                 ▼
       Runtime Application
                 │
        ┌────────┴──────────┬────────────┐
        ▼                   ▼            ▼
  Configuration        Secret          Session
     Service           Service         Service
        │                 │              │
        ├── Config        └── OS         ├── Secret Provider
        │   Provider      Credential    ├── Snowflake Provider
        │                 Store         └── Create Authenticated
        └─────────────────┬────────────┘    Session
                         ▼
                  RuntimeStatus (Domain)
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
  Store Context              Listen on IPC Socket
        │                         │
        ▼                         ▼
  Ready for                   CLI can now connect
  CLI connections             and send requests
```

---

## Flow 4: Data Export

```text
User runs:   snow data export my_query --format parquet
                 │
                 ▼
            CLI Interface
                 │
                 ▼
        Data Application
                 │
        ┌────────┴────────────────┐
        ▼                         ▼
   Data Service            Object Resolution Service
        │                         │
        ├── Execution Service     └── Resolve full table name
        │   (fetch results)
        ├── Catalog Service
        │   (get metadata)
        ├── Schema Service
        │   (inspect columns)
        │
        ├── Export Service
        │   (format data)
        │
        └── File Provider
            (write parquet)
                 │
                 ▼
            Parquet File
                 │
                 ▼
           Success Message
```

---

# Repository Structure

The repository mirrors the architecture layers exactly.

```
snow-runtime/
├── interfaces/
│   ├── cli/
│   ├── tui/
│   └── web/
│
├── application/
│   ├── runtime_app.py
│   ├── config_app.py
│   ├── context_app.py
│   ├── sql_app.py
│   ├── transaction_app.py
│   ├── metadata_app.py
│   ├── explore_app.py
│   ├── data_app.py
│   ├── history_app.py
│   ├── logs_app.py
│   └── doctor_app.py
│
├── services/
│   ├── configuration_service.py
│   ├── session_service.py
│   ├── context_service.py
│   ├── execution_service.py
│   ├── catalog_service.py
│   ├── schema_service.py
│   ├── data_service.py
│   ├── history_service.py
│   ├── logging_service.py
│   ├── diagnostics_service.py
│   ├── secret_service.py
│   ├── export_service.py
│   ├── object_resolution_service.py
│   └── query_parser.py
├── domain/
│   ├── entities/
│   │   ├── connection_profile.py
│   │   ├── session.py
│   │   ├── database.py
│   │   ├── schema.py
│   │   └── table.py
│   │
│   ├── value_objects/
│   │   ├── context.py
│   │   ├── query.py
│   │   ├── query_result.py
│   │   ├── column.py
│   │   ├── constraint.py
│   │   ├── runtime_status.py
│   │   └── data_profile.py
│   │
│   ├── enums/
│   │   ├── session_state.py
│   │   ├── transaction_state.py
│   │   ├── runtime_state.py
│   │   ├── query_status.py
│   │   └── export_format.py
│   │
│   └── exceptions/
│       ├── snow_runtime_error.py
│       ├── authentication_error.py
│       ├── configuration_error.py
│       ├── execution_error.py
│       └── ...
│
└── providers/
    ├── snowflake_provider.py
    ├── configuration_provider.py
    ├── secret_provider.py
    ├── history_provider.py
    ├── logging_provider.py
    ├── runtime_provider.py
    ├── process_provider.py
    ├── file_provider.py
    └── cache_provider.py
```

---

# Roadmap

This architecture describes the system as it stands today. The following enhancements are planned for future releases but do not affect the core design.

## Planned Enhancements

* **Cache Provider** — Metadata and schema caching to reduce Snowflake API calls.
* **GraphQL Interface** — Programmatic queries over the Runtime.
* **Workspace Isolation** — Multi-tenant project workspaces.
* **Query Optimization** — Cost estimation and query plan analysis.
* **Advanced Analytics** — Built-in profiling, anomaly detection, and lineage tracking.

These additions will follow the same architectural principles and require no refactoring of existing layers.

---

# Architectural Principles

These principles guide all design decisions in Snow Runtime.

1. **Runtime is the single source of truth** — All business logic flows through the Runtime. No logic lives in Interfaces.

2. **Business logic exists only once** — A capability is implemented in a Service, not duplicated across Interfaces.

3. **Interfaces contain no business logic** — Interfaces only translate user input into Service calls and format responses.

4. **Consumers communicate only through the Runtime** — The CLI, TUI, Web UI, and Python SDK all invoke Services through the Application Layer.

5. **Services remain independent of interfaces** — A Service never imports CLI, TUI, or Web UI code.

6. **Providers isolate all external dependencies** — Services never communicate directly with Snowflake, the filesystem, or external systems.

7. **Domain models are shared throughout the Runtime** — Every layer speaks the same language via immutable Domain Objects.

8. **Layers have strict dependencies** — Interfaces → Applications → Services → Domain ↔ Providers → External Systems. No circular dependencies.

9. **Services collaborate, Applications orchestrate** — Services work together to complete workflows; Applications decide which Services to call.

10. **Providers are replaceable** — Swapping a Provider (e.g., moving from local SQLite to cloud storage) should not require changes to Services.

11. **No technology-specific objects cross layer boundaries** — Snowflake Connector classes, filesystem objects, and third-party library types stay in Providers.

12. **Explicit over implicit** — Type-safe Domain Objects replace dictionaries, tuples, and loosely-typed structures. Interfaces are explicit contracts.

---

# Design Rationale

## Why Layered Architecture?

Layering cleanly separates concerns. Each layer has one job and knows only about the layer below. This enables:

- **Independent testing** — Mock Providers, test Services in isolation.
- **Parallel development** — Teams can work on Interfaces while others build Services.
- **Easy to understand** — New developers see exactly where code belongs.

## Why Services Layer?

The Services Layer prevents business logic from scattering across the codebase. A single Execution Service owns all SQL execution logic, regardless of whether it's called from CLI, TUI, or Python SDK.

## Why Providers Layer?

Providers isolate third-party code and external dependencies. If Snowflake changes their connector API, only the Snowflake Provider needs updating. The rest of the Runtime doesn't notice.

## Why Domain Layer?

Domain Models are the contract between Services and Providers. Services depend on Domain objects; Providers produce them. This bidirectional dependency prevents any layer from assuming it knows how the other works internally.

---

# Success Criteria

The architecture succeeds when:

✅ **Single source of truth** — Business logic is implemented once and reused by all Interfaces.

✅ **Easy to test** — Services can be tested without a running Snowflake instance.

✅ **Easy to extend** — Adding a new Interface (REST API, Slack bot, VSCode extension) requires no changes to Services.

✅ **Easy to maintain** — A developer can locate any piece of business logic within 2 minutes.

✅ **Resilient to change** — Snowflake API updates are isolated to the Snowflake Provider.

✅ **Clear responsibilities** — No ambiguity about which layer owns a feature or where to add new code.

---

# Document Status

**Version:** 1.0  
**Status:** Frozen  
**Date:** 2026-06-29

This document describes the complete architecture. Implementation should proceed with confidence that the design is sound. Changes to the architecture should only occur when implementation reveals a genuine design flaw, not preemptively.
