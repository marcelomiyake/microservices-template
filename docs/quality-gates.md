# Testing and quality gates

The starter has distinct checks for behavior, coverage, static analysis, and the deployed Kind path. Record exact commands, revision, environment, and observed results in [verification](verification/README.md). Generated projects must rerun these checks for their own code.

Run `./scripts/check-local.sh` as the local handoff check. It runs Rust formatting, Clippy, tests, Vue typecheck/build, Helm lint, and the per-component coverage gate. Use `./scripts/check-local.sh --quick` during implementation; it skips coverage but still runs unit and integration tests. [The GitHub Actions workflow](../.github/workflows/validate.yml) runs the full local check and a Kind browser test for pull requests and `main` pushes. A generated repository should protect its main branch with these required checks after confirming the workflow runs successfully there.

## Test levels

| Level | Starter check | What it proves |
| --- | --- | --- |
| Unit/component | `cd web && npm ci && npm run test:unit` | Vue success, failure/retry, and malformed response states with a controlled API response. |
| HTTP integration | `cargo test --workspace --locked` | Example service contract and web API behavior against a loopback HTTP upstream, including 502 translation. It does not use a database or Kind. |
| Kind end-to-end | Deploy with `./scripts/deploy-kind.sh`, then run `./scripts/test-kind-e2e.sh` | Chromium opens the real Nginx/Vue page through port forwarding and sees the response across both Rust Services. |

Add domain unit tests for invariants, integration tests with disposable dependencies, and browser acceptance tests for user flows as the generated project grows. Do not label mocked browser tests as Kind end-to-end evidence.

## Coverage

Run `./scripts/coverage.sh` to create per-service Rust LCOV reports and the Vue LCOV report, then enforce at least 80% line coverage for each. Rust reports cover service library behavior; `src/main.rs` startup glue is excluded from line coverage and is exercised by the Kind path. Report that scope with any percentages. Browser E2E coverage is not imported into LCOV.

The Rust coverage tool is `cargo-llvm-cov`; install it before running the script. Generated projects should revisit exclusions when moving behavior into startup code. Do not add exclusions merely to raise a number.

## SonarQube quality and duplication gate

The three project scopes are in [`.sonar/`](../.sonar/): example service, web API, and Vue frontend. Set `SONAR_TOKEN` in the environment and optionally `SONAR_HOST_URL` (default `http://127.0.0.1:9000`), then run `./scripts/sonar-scan.sh`. Docker runs the scanner against the host SonarQube server, imports current LCOV/Clippy evidence, and waits for each server quality gate. Rename the project keys after generating a repository to avoid collisions.

The local check additionally requires each project to have **at least 80% overall coverage**, **less than 3% duplicated lines**, **zero active issues**, and **zero measured security hotspots**. The server gate must report `OK`; inspect its actual new-code conditions and hotspot details in SonarQube. Configure a meaningful server gate for no new issues, reviewed hotspots, new-code coverage, and duplication, as described in [SonarQube's quality-gate documentation](https://docs.sonarsource.com/sonarqube-community-build/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates). Scanner upload alone does not establish a passing gate. If the server, token, analyzer, or current result is unavailable, report the gate incomplete.

The source template's SonarQube server is local. To run this gate in a generated repository's CI, provide a network-reachable SonarQube instance and configure its URL, token, project keys, and required branch check. Until then, run the gate in the authorized local environment and record its result; the GitHub workflow does not claim SonarQube passed.

Review duplication by domain meaning. Share behavior only when a real rule and owner are shared; similar-looking code in distinct contexts can remain separate. Do not weaken thresholds or exclude meaningful code to clear a metric.

## DDD, Jev, and commits

For domain work, use [the agent workflow](agent-workflow.md) to state actor, outcome, terms, invariants, owners, contracts, failure modes, and acceptance checks before implementation. Use Jev as an optional structured, advisory quality assessment of a sanitized agent brief or verified implementation summary; see [Jev verification](jev-quality.md). It does not replace tests or a product decision.

Use [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) for commits: `type[optional scope]: description`; mark breaking changes with `!` or a `BREAKING CHANGE:` footer. Examples: `feat(api): add item lookup`, `fix(web): recover from a timed-out request`.
