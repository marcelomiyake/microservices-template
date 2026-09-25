# Example service

This Rust service owns the sample `/example` response. It has no storage or external dependency. Replace its name and behavior with one real service boundary in a generated PoC.

## Contract and consumers

- Owner: `services/example-service`.
- Known consumer: `services/web-api`.
- Authority: [OpenAPI contract](../../docs/contracts/openapi.yaml) and [handler](src/lib.rs).
- Parent architecture: [system design](../../docs/system-design.md).

## Build, run, and verify

From the repository root:

```sh
cargo run -p example-service
cargo test -p example-service
```

The default listener is `127.0.0.1:8082`; set `PORT` and `BIND_ADDRESS` to change it. The Kind chart sets `BIND_ADDRESS=0.0.0.0` inside the container and deploys two replicas behind a ClusterIP Service. `GET /health` returns `ok`; `GET /example` returns a JSON message. Stop local development with Ctrl-C; use the root undeploy script for Kind. There is no persistent data.

The HTTP contract test is in [tests/http.rs](tests/http.rs). The [coverage script](../../scripts/coverage.sh) reports library behavior separately from process startup. See [testing and quality gates](../../docs/quality-gates.md).

[Project README](../../README.md) · [Agent guidance](AGENTS.md) · [Documentation index](../../docs/README.md)
