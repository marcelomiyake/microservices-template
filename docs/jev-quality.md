# Jev quality verification

[TypeSafe Jev](https://docs.typesafe.ai/introduction/coding-agents) can return typed rubric scores and probability distributions. In this template it is an **advisory** check for agent-job clarity or implementation readiness, separate from SonarQube and software tests.

## Prepare evidence

For an agent job, fill [the DDD job template](templates/agent-job.template.md). For an implementation, fill [the evidence summary template](templates/jev-evidence.template.md) from actual design, tests, Kind, coverage, and SonarQube results. Remove placeholders, source code, credentials, personal data, raw user data, and unrelated private material. Cite revision and paths in the local record, but send only the minimal sanitized summary.

## Run

With an authorized `TYPESAFE_API_KEY` in the environment, run one of:

```sh
python3 scripts/jev-verify.py --mode job --brief path/to/sanitized-job.md
python3 scripts/jev-verify.py --mode implementation --brief path/to/sanitized-evidence.md
```

The script calls the current TypeSafe System One endpoint with `jev-latest`, prints the returned model, scores, confidence, and full level probabilities, and writes the response to ignored `target/jev-result.json`. Job mode asks four independent Score questions for domain fit, scope/evidence, acceptance, and risk/decision ownership. The local initial guardrail flags a dimension when its score is below 2.5 or probability on levels 0–2 exceeds 0.20; this is a project rubric, not a TypeSafe default. Improve weak briefs with evidence and an owner for open decisions before dependent implementation. Implementation mode asks one 0–4 readiness question; review the answer alongside actual verification.

Record model, date, revision, rubric, each score, distribution, confidence, input scope, and limitations in a new [verification record](verification/README.md). A high score is not proof that code works. If Jev is unavailable, use the rubric manually and say that no model call occurred. See [Score](https://docs.typesafe.ai/primitives/score) and [TypeSafe API](https://docs.typesafe.ai/api) for the live contract.
