# ADR-0001: Use Rust for backend services

- **Status:** Implemented for template baseline
- **Recorded:** 2026-09-25
- **Decision owner:** Template maintainer

## Context

The requested PoC template needs a backend language that can produce small, independently runnable services. The five reference projects use Rust backend services.

## Options

| Option | Benefit | Cost |
| --- | --- | --- |
| Rust with Axum | Aligns with the reference projects; typed contracts and one workspace | Compilation and ownership model add learning time |
| Another backend language | May be familiar to a generated project's team | Diverges from the requested baseline |

## Decision

Use Rust and a Cargo workspace for the starter's two services. Keep service-specific dependencies and ownership in their own directories. This is a baseline choice, not a requirement that every future use case use two services.

## Consequences and evidence

The [workspace](../../Cargo.toml), [example service](../../services/example-service/src/main.rs), and [web API](../../services/web-api/src/main.rs) implement this decision. A generated project should revisit it if team skills, platform constraints, or measured needs change.
