# SonarQube Cloud verification

Each Rust backend service has a dedicated SonarQube Cloud project. The [GitHub Actions workflow](https://github.com/marcelomiyake/microservices-template/actions/workflows/sonarcloud-microservices.yml) runs one coverage and analysis job per service on pushes to `main`; `workflow_dispatch` supports a manual rerun. The organization setting that auto-imports newly created GitHub repositories is disabled, so this workflow owns project analysis.

Each matrix job runs `cargo llvm-cov --lcov --output-path target/coverage/lcov.info -- --test-threads=1` from its service directory, then imports that report with `cargo sonar-scanner`. It reads the GitHub repository secret named `SONAR_TOKEN`. The `src/main.rs` startup entrypoints are excluded for both sample services. No local Sonar scan script is used.

## Projects and coverage

Coverage below is SonarCloud's overall line coverage for `main`, not new-code or local coverage. The baseline is the latest Cloud result before the coverage-test updates; the current column is the latest result after them. Values are from the 2026-09-27 snapshot.

| Microservice | SonarCloud project | Before | Current | Change |
| --- | --- | ---: | ---: | ---: |
| `example-service` | [project](https://sonarcloud.io/project/overview?id=marcelomiyake_microservices-template_example-service) | 100.0% | 100.0% | — |
| `web-api` | [project](https://sonarcloud.io/project/overview?id=marcelomiyake_microservices-template_web-api) | 100.0% | 100.0% | — |

Both projects have a passing Quality Gate, zero open or confirmed issues, zero hotspots awaiting review, zero bugs, zero vulnerabilities, zero code smells, and 0.0% duplicated lines.

## Verification

For a report, check that the latest workflow completed for the pushed commit and that each SonarCloud project's `main` analysis matches that revision. Review overall coverage, active issues, security hotspots, duplication, and the Quality Gate. Current project links above open the live Cloud dashboards; the workflow link shows the CI run history. Local tests and coverage reports are useful checks but do not replace the Cloud analysis.
