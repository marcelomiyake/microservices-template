# Web API

This Rust service is the browser-facing API. `GET /api/example` calls `example-service` with a three-second timeout and returns its message or a 502 JSON error. It has no storage.

## Contract and consumers

- Owner: `services/web-api`.
- Known consumer: `web`.
- Downstream contract owner: `services/example-service`.
- Authority: [OpenAPI contract](../../docs/contracts/openapi.yaml) and [handler](src/lib.rs).
- Parent architecture: [system design](../../docs/system-design.md).

## Build, run, and verify

Start `example-service`, then run from the repository root:

```sh
cargo run -p web-api
cargo test -p web-api
```

The default listener is `127.0.0.1:8081`. Set `PORT` and `BIND_ADDRESS` to change it and `EXAMPLE_SERVICE_URL` to change the downstream URL. The Kind chart sets `BIND_ADDRESS=0.0.0.0`, points to the `example-service` ClusterIP Service, and deploys two replicas. `GET /health` checks this process only; it does not check the downstream service. Stop local development with Ctrl-C; use the root undeploy script for Kind.

The [HTTP integration tests](tests/http.rs) use a loopback upstream to verify success and 502 translation. The [coverage script](../../scripts/coverage.sh) reports library behavior separately from process startup. See [testing and quality gates](../../docs/quality-gates.md).

[Project README](../../README.md) · [Agent guidance](AGENTS.md) · [Documentation index](../../docs/README.md)
