# SonarQube verification

This record covers the template source at `70edfed` on 2026-09-25. It does not certify projects generated from the template.

## Environment and command

- Local SonarQube Community Build: `26.9.0.129388`, reached at `http://127.0.0.1:9000`.
- Docker SonarScanner CLI: `8.1.0.6389`.
- Ran `./scripts/sonar-scan.sh` with an environment-provided `SONAR_TOKEN`. The script generated coverage and Clippy reports, scanned the three project scopes, waited for each server gate, and ran `scripts/check-sonar-gate.py`.
- After adding explicit active-issue and hotspot checks to that checker, reran `python3 scripts/check-sonar-gate.py` at 19:22 UTC; all three passed. The scanned application revision was unchanged.

## Observed results

| SonarQube project key suffix | Server gate | Sonar overall coverage | Duplicated lines | Active issues | Measured security hotspots |
| --- | --- | ---: | ---: | ---: | ---: |
| `example-service` | OK | 100.0% | 0.0% | 0 | 0 |
| `web-api` | OK | 100.0% | 0.0% | 0 | 0 |
| `web` | OK | 97.6% | 0.0% | 0 | 0 |

Each project key starts with `microservices-template-`. The server's reported new-code conditions were OK. The two Rust projects reported OK for new coverage, duplicated lines, and violations. The Vue project reported OK for new duplicated lines and violations; a new-coverage condition was absent from its response. The local checker independently required overall coverage of at least 80%, duplicated lines below 3%, zero active issues, and zero measured security hotspots for every project.

The raw LCOV line-coverage check reported 86.7% for `example-service`, 89.7% for `web-api`, and 93.8% for `web`. SonarQube uses its own executable-line calculation, so its overall coverage percentages differ. Rust startup glue in `src/main.rs` is excluded from LCOV and Sonar coverage and is exercised by the Kind path.

## Limits

The analysis token received HTTP 403 from the direct hotspot-detail endpoint, so this record confirms the zero-hotspot metric but does not claim a manual hotspot-detail review. The result reflects the local server's gate configuration and the scanned revision. Generated repositories need new Sonar project keys, a meaningful server gate, and their own scan and review.
