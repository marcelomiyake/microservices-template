# Jev quality verification

On 2026-09-25, the template maintainer sent two manually sanitized summaries of revision `70edfed` to the TypeSafe System One API with `jev-latest`. The returned model was `jev-1.13.0`. The API key came from the environment; neither source code nor credentials were included in the summaries. The input and full JSON responses remain in ignored `target/` files. These are advisory judgments, separate from tests and SonarQube.

## Agent-job brief

Command: `python3 scripts/jev-verify.py --mode job --brief target/jev-agent-job.md --output target/jev-job-revised-result.json`.

The summary named the template maintainer, the future generated-project domain owner, component ownership, scope and exclusions, executable acceptance checks, local Kind limits, secret handling, recovery, and stop conditions. An initial run flagged both acceptance and risk ownership. After clarifying decision owners and exact checks, the revised run returned:

| Dimension | Score / 3 | Confidence | Probability for levels 0, 1, 2, 3 | Local guardrail |
| --- | ---: | ---: | --- | --- |
| Domain fit | 2.99 | 0.99 | 0.00, 0.00, 0.01, 0.99 | Met |
| Scope and evidence | 2.97 | 0.97 | 0.00, 0.00, 0.02, 0.98 | Met |
| Acceptance | 2.50 | 0.50 | 0.01, 0.06, 0.34, 0.59 | **Review**: 0.41 probability on levels 0–2 |
| Risk and decision ownership | 2.99 | 0.99 | 0.00, 0.00, 0.00, 1.00 | Met |

The remaining acceptance flag is consistent with the fact that a future generated project's domain acceptance cases still need an owner and concrete requirements; Jev did not provide a causal explanation. The starter's observable checks are listed in [the quality verification record](quality-harness.md). The score does not establish that an OpenDesign review occurred.

## Implementation evidence

Command: `python3 scripts/jev-verify.py --mode implementation --brief target/jev-implementation-evidence.md --output target/jev-implementation-result.json`.

The sanitized summary cited the two Rust services, Vue browser path, Kind deployments, contract and ownership docs, unit/integration/E2E results, LCOV and SonarQube results, and limits. Jev returned implementation readiness **3.09/4**, confidence **0.92**, with probability **0.00, 0.00, 0.00, 0.91, 0.09** for levels 0–4. The record disclosed that the starter page has no OpenDesign prototype review and that hotspot-detail API access returned 403.

Review the underlying [test evidence](quality-harness.md) and [SonarQube evidence](sonarqube.md) directly. A model score is not proof that code works or that future projects meet their own requirements.
