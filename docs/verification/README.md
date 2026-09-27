# Verification records

The [starter verification record](starter-kind.md) reports checks run while building this template, including the Kind request path and undeployment. For new checks, copy [the verification record template](../templates/verification-record.template.md) to a dated or topic-specific Markdown file, then record the actual revision, environment, command, observed result, and remaining gaps. Link new records here and in [the documentation index](../README.md). Generated projects must run and record their own checks; these results do not transfer to new code.

The root [README](../../README.md#verify) lists baseline commands. Browser accessibility, Lighthouse, coverage, and deployment checks belong here only after they are actually run and are relevant to the generated project.

- [SonarQube verification](sonarqube.md) — separate project scans, coverage, duplication, server gates, and gaps.
- [Jev quality verification](jev-readiness.md) — model, rubric, score distribution, confidence, and evidence scope when run.
- [Quality harness verification](quality-harness.md) — observed Rust, Vue, Kind browser, Helm, and coverage checks for the current sample.
