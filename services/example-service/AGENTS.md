# Example service guidance

- Follow [repository guidance](../../AGENTS.md) and [the service README](README.md).
- This service owns the `/example` response. Do not add browser-specific presentation or downstream client behavior here.
- Keep the [OpenAPI contract](../../docs/contracts/openapi.yaml) and [system design](../../docs/system-design.md) aligned with route changes.
- Run `cargo fmt --all --check`, `cargo clippy -p example-service --all-targets -- -D warnings`, and `cargo test -p example-service` for relevant changes.
