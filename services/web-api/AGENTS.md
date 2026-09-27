# Web API guidance

- Follow [repository guidance](../../AGENTS.md) and [the service README](README.md).
- This service owns the browser-facing `/api/example` contract, not the example message. Preserve bounded downstream timeouts and an explicit failure response.
- Keep the [OpenAPI contract](../../docs/contracts/openapi.yaml), [contract catalog](../../docs/contracts/README.md), and [system design](../../docs/system-design.md) aligned with interface changes.
- Run `cargo fmt --all --check`, `cargo clippy -p web-api --all-targets -- -D warnings`, and `cargo test -p web-api` for relevant changes.
