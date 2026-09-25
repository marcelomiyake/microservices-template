# Repository guidance

> Human entry point: [README.md](README.md) · [Documentation index](docs/README.md)

## Purpose and boundaries

- Keep this repository a reusable Kind-first Rust/Vue PoC starter. The sample request path is `web` → `web-api` → `example-service`; replace it with a real bounded context in generated projects.
- `example-service` owns `/example` and its response. `web-api` owns `/api/example` and translates downstream failure into HTTP 502. `web` is a client and must not contain backend secrets or authoritative domain rules.
- Keep the Helm chart as the Kind deployment source of truth. Add storage, messaging, and shared crates only when a concrete use case needs them. Assign each state and contract one owner; document known producers and consumers.
- For non-trivial domain changes, use [DDD agent workflow](docs/agent-workflow.md): state actor, outcome, language, invariants, context, data owner, cross-context contract, failure behavior, and observable acceptance. Do not equate a folder or pod with a bounded context. Keep unresolved policy decisions with their domain owner.
- For substantial frontend work, use [OpenDesign](https://github.com/nexu-io/open-design) when available. Update [web/DESIGN.md](web/DESIGN.md), review a rendered prototype, then implement in Vue and verify states, keyboard behavior, and responsiveness. If unavailable, record the limitation and actual alternative review.

## Changes and checks

- Start non-trivial work with the [agent-job brief](docs/templates/agent-job.template.md): cite the inspected revision and paths, separate facts from assumptions, name the domain decision owner, and map each acceptance case to observable evidence. Stop dependent work when a missing domain decision changes the behavior to implement.
- Before editing, read this file and the scoped `AGENTS.md` for every touched component. Trace the request through the owned contract, code, tests, and Kind chart. Keep the change small enough to review and report what remains uncertain.
- Update the authoritative source, [HTTP contract](docs/contracts/openapi.yaml), component guides, and [system design](docs/system-design.md) together when behavior or ownership changes.
- Keep `README.md` human-facing. Use `AGENTS.md` for agent instructions and `CLAUDE.md` only to import them. Follow the [documentation standard](docs/documentation-standard.md).
- Run `./scripts/check-local.sh` before handoff: it checks Rust, Vue, Helm, and per-component coverage. Use `./scripts/check-local.sh --quick` while iterating. After a Kind deployment, use `./scripts/test-kind-e2e.sh` for the real browser path. [GitHub Actions](.github/workflows/validate.yml) runs the full local checks and Kind browser path on pull requests and `main` pushes.
- Use `./scripts/coverage.sh` for per-component line coverage and `./scripts/sonar-scan.sh` for separate SonarQube analyses. Require the configured server gate, at least 80% overall coverage, less than 3% duplication, zero active issues, and zero measured security hotspots for each project. Inspect server conditions and hotspot details; a missing or stale scan is incomplete. Keep startup-code coverage exclusions explicit and do not weaken meaningful analysis to meet a number.
- Jev can assess a sanitized [agent brief or implementation summary](docs/jev-quality.md) when authorized. Review the score distribution and confidence; it does not certify code or replace tests, SonarQube, or domain-owner decisions. State when Jev was not called.
- Record only checks actually run in `docs/verification/`. Do not imply local results prove production throughput or reliability.
- Hand off with the [pull request evidence format](.github/pull_request_template.md): requirement, command or review, observed result, revision, and remaining owner. Mark unavailable checks explicitly; never paste starter verification as evidence for a generated project.
- Use synthetic example data. Do not commit tokens, credentials, personal data, `.env` files, or generated build artifacts. Verify the active `kind-*` context before deployment; use a dedicated namespace, ClusterIP Services, and loopback port forwarding. Set CPU/memory requests and limits on every new container and document them. Preserve persistent data on undeploy when a generated project adds it.
- Follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for every commit: `type[optional scope]: description`; mark breaking changes with `!` or a `BREAKING CHANGE:` footer.
