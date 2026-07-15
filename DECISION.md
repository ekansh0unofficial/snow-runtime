# DECISION.md

# Snow Runtime - Architecture Decision Log

This document records architectural decisions made during implementation.

Unlike the README, this file captures **why** decisions were made and helps
detect architectural drift as the project evolves.

---

## 2026-06-29

### Domain-first Development

**Decision**

Implement the Domain Layer before Services, Applications and Providers.

**Reason**

The Domain defines the business language shared across every layer.

---

### Business-first Modeling

**Decision**

Model business concepts before writing Python classes.

Every new object must answer:

- Why does it exist?
- Who owns it?
- Who uses it?
- How long does it live?

**Reason**

Responsibility and lifecycle determine the correct abstraction.

---

### Ownership over Association

**Decision**

Relationships are explicitly modeled as:

- owns
- uses
- produces

instead of generic associations.

**Reason**

Ownership determines lifecycle and keeps the domain model clear.

---

### Entity vs Value Object

**Decision**

Objects are classified by identity rather than containment.

- Entities have identity and lifecycle.
- Value Objects are defined entirely by their values.

**Reason**

A Value Object may exist independently of an Entity and still remain a Value
Object.

---

### Runtime Ownership

**Decision**

Runtime owns one or more Sessions.

ConnectionProfile is used to create Sessions but does not own them.

**Reason**

Sessions exist only while a Runtime is active.

---

### Context Scope

**Decision**

Context represents only the active execution environment.

Current scope:

- Database
- Schema
- Warehouse
- Role

**Reason**

Authentication and connection details belong to ConnectionProfile.

---

### Transaction Removed

**Decision**

Transaction is not a Domain Entity.

**Reason**

Transactions are owned by Snowflake.

Snow Runtime coordinates transaction execution but does not manage transaction
state.

---
## 2026-06-30
### Query Scope

**Decision**

Query represents SQL only.

It does not know whether SQL originated from:

- CLI
- SQL file
- SDK
- stdin

**Reason**

The Domain remains independent of Interfaces and Providers.

---

### QueryParser Introduced

**Decision**

Introduce QueryParser as the component responsible for SQL classification.

Responsibilities:

- Parse SQL
- Determine QueryType
- Normalize SQL (future)

**Reason**

Parsing is business logic and should not belong to Query.

---

### QueryType Introduced

**Decision**

Categorize SQL using QueryType.

Current categories:

- DQL
- DML
- DDL
- DCL
- TCL
- UTILITY

**Reason**

Execution behavior depends on SQL category rather than individual SQL keywords.

---
## 2026-07-01
### History Ownership

**Decision**

History belongs to ConnectionProfile.

**Reason**

History should persist across Runtime restarts and Session recreation.

---

### Metadata Boundary

**Decision**

Metadata models only concepts required for current features.

Current scope:

- Database
- Schema
- Table
- View
- Column
- Constraint
- Relationship

**Reason**

Snow Runtime focuses on metadata exploration and ER diagram generation rather
than becoming a complete Snowflake object explorer.

---

### QueryResult Deferred

**Decision**

Postpone QueryResult implementation.

**Reason**

The current abstraction does not naturally represent all SQL statement types
(SELECT, INSERT, UPDATE, DDL, etc.).

The execution model will be finalized before implementing the result model.

---

### Simplicity First

**Decision**

Avoid speculative abstractions.

Objects are introduced only when required by an implemented feature.

**Reason**

Keeps the Domain small, focused and easier to evolve.

### SQL Script as the Execution Unit

**Decision**

A SQL script becomes the primary execution unit.

A script contains one or more `Query` objects.

A single SQL statement is represented as a script containing exactly one query.

**Reason**

This removes the distinction between single-query and batch execution.

All execution paths now follow the same workflow regardless of whether SQL
originated from a terminal command or a `.sql` file.

This simplifies execution, progress reporting, rollback, history and future
batch features.

### Context Promoted to Entity

**Decision**

Context is promoted from a Value Object to an Entity.

**Reason**

Contexts are now persistent, named configurations owned by a ConnectionProfile.

Users create, rename, update and delete contexts by identity rather than by value.

This introduces lifecycle and identity, making Context an Entity.

## 2026-07-03
### Runtime is an Application Concept

**Decision**

Runtime is **not** a Domain Entity.

It belongs to the Application Layer and acts as the application's composition root and orchestrator.

**Reason**

The Runtime does not represent a business concept. It coordinates the application's lifecycle by creating and wiring Services, exposing Applications, managing IPC, and controlling the overall execution environment.

The business domain remains valid independent of the Runtime implementation. Core domain concepts such as `ConnectionProfile`, `Session`, `Context`, `Command`, and `HistoryEntry` exist regardless of whether the Runtime is implemented as a daemon, embedded library, or another hosting model.

Treating the Runtime as a Domain Entity would introduce infrastructure concerns into the Domain Layer and violate the separation between business concepts and application orchestration.

The existence of a single Runtime is considered a deployment constraint rather than a Domain rule.

### Entities Own State, Services Own Workflows

**Decision**

Entities are responsible for representing business concepts and maintaining
their own valid state.

Business workflows involving multiple entities, persistence, external systems,
or global validation belong to Services.

**Reason**

An Entity should only make decisions using its own state.

Operations requiring knowledge of other entities, repositories, providers, or
external systems belong to the Service Layer.


### Credentials Are Not Part of ConnectionProfile

**Decision**

ConnectionProfile stores connection metadata only.

Passwords and other secrets are never stored in the Domain.

**Reason**

Credential storage belongs to the Secret Provider.

The Domain models what is required to establish a connection, while the Secret
Provider manages how sensitive credentials are securely stored and retrieved.

### Commands Model User Intent

**Decision**

Commands are modelled as an abstract base entity with concrete subclasses for
each supported user intent.

A generic payload-based command model will not be used.

**Reason**

Each command represents a distinct business operation with its own required
data and invariants.

Using concrete command types provides compile-time type safety, removes
payload validation from Services, and allows new commands to be added without
expanding a central payload schema or branching on CommandType.

---

## 2026-07-11

### Context Application vs Config Application

**Decision**

Context Application manages saved contexts (CRUD) within a ConnectionProfile.
Config Application manages profiles (CRUD). They are separate Applications
operating at different levels of the same hierarchy.

**Reason**

Profiles and contexts have distinct lifecycles and responsibilities:

- Config = profile-level management (name, org, account, username, password)
- Context = context-level management (name, database, schema, warehouse, role)

Separating them keeps each Application focused on a single concern and allows
them to evolve independently.

### Application Layer Contracts First

**Decision**

Define Application layer contracts (method signatures, inputs, outputs,
dependencies) before implementing Services.

**Reason**

Applications define the orchestration surface area. Writing them first
establishes exactly what Service methods are needed, preventing speculative
abstraction in the Service Layer.

Application implementations may not run until Services are built, but they
serve as a design document validated by actual usage.

### Application Categorization and Session Dependency

**Decision**

Applications are grouped into three categories:

- **Lifecycle** — Config, Context, Runtime
- **Work** — SQL, Metadata, Data, Explore
- **Observability** — History, Logs, Doctor

Work Applications require an active Snowflake Session and communicate
through Session Service. Lifecycle and Observability Applications operate
locally (TOML, SQLite, filesystem) and do not require a Session.

**Reason**

This categorization clarifies which Applications depend on Session Service
and which are purely local. It prevents unnecessary coupling between
Applications that manage local state and Applications that need live
Snowflake connectivity.

### No ContextService

**Decision**

There is no separate ContextService.

- ContextApplication manages saved contexts (CRUD) via ConfigurationService.
- The active context lives on the Session entity, managed by SessionService.

**Reason**

The active context (current database, schema, warehouse, role) is runtime
state that belongs to an active Session. There is no need for a separate
Service to manage what is already a property of Session. ContextApplication
handles persistence of named context configurations in TOML, while
SessionService owns the active context during a live session.

### SQL Application Has One Method

**Decision**

SQLApplication exposes a single method: `execute(sql: str)`.

It does not have separate methods for file execution, stdin execution,
or command-line execution.

**Reason**

The source of SQL (command string, file, stdin) is an Interface concern.
The CLI Interface reads SQL from its source and passes extracted text
to the Application. The Application only receives and executes SQL text,
remaining independent of how it was obtained.

### Metadata and Explore Merged

**Decision**

Metadata Application and Explore Application are merged into a single
ExploreApplication.

Catalog Service and Schema Service remain separate Services to preserve
SOLID compliance — each owns a single business capability.

**Reason**

Metadata and Explore both deal with discovering and inspecting Snowflake
objects. Splitting them into two Applications created unnecessary
duplication. A single ExploreApplication exposes a unified surface area
while delegating to focused Services underneath.