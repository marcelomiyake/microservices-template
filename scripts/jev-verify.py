#!/usr/bin/env python3
"""Ask TypeSafe Jev to score a manually sanitized work brief or evidence summary."""

import argparse
import json
import os
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://api.typesafe.ai/v1/systemone"
LEVELS = {
    "domain_fit": [
        "The outcome conflicts with confirmed domain behavior or is unsafe.",
        "The actor, outcome, or applicable context is missing.",
        "Actor and context are named, but important terms or rules remain ambiguous.",
        "Actor, outcome, context, terms, and unresolved domain choices are explicit.",
    ],
    "scope_evidence": [
        "The work is contradictory, unbounded, or supported by no evidence.",
        "Scope, sources, or dependencies needed to start are missing.",
        "The main scope is clear, but exclusions, evidence, ownership, or contracts are incomplete.",
        "Scope, exclusions, evidence, owners, dependencies, and relevant contracts are explicit.",
    ],
    "acceptance": [
        "There is no observable deliverable to hand off.",
        "The brief describes activity without a verifiable result.",
        "A deliverable is named, but one or more acceptance checks are subjective or unavailable.",
        "Deliverables and observable checks are traceable to requirements and can be run or reviewed.",
    ],
    "risk_ownership": [
        "The brief exceeds authorization or hides material risk.",
        "Affected data, failure modes, or decision owners are omitted.",
        "Main risks are named, but permission, recovery, owner, or stop conditions are unclear.",
        "Data and permission limits, failures, decision owners, and stop conditions are explicit.",
    ],
    "implementation_readiness": [
        "No coherent design, runnable artifact, or repeatable verification exists.",
        "A partial design or implementation exists; major requested boundaries or acceptance cases are missing.",
        "The core design and implementation work, but important tests, Kind deployment, quality analysis, or end-to-end evidence is missing.",
        "The requested local design, code, tests, Kind flow, and quality checks have evidence; educational limits are disclosed.",
        "Evidence is complete and independently reproducible for the stated PoC scope; significant acceptance gaps and operational risks are addressed.",
    ],
}


def questions(mode: str) -> dict:
    keys = ("implementation_readiness",) if mode == "implementation" else (
        "domain_fit", "scope_evidence", "acceptance", "risk_ownership"
    )
    return {
        key: {
            "type": "score",
            "instructions": f"How well does the supplied evidence meet the {key.replace('_', ' ')} rubric for this PoC?",
            "criteria": LEVELS[key],
        }
        for key in keys
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("job", "implementation"), required=True)
    parser.add_argument("--brief", type=Path, required=True, help="Sanitized evidence summary only")
    parser.add_argument("--output", type=Path, default=Path("target/jev-result.json"))
    args = parser.parse_args()
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        print("Set TYPESAFE_API_KEY in the environment.", file=sys.stderr)
        return 2
    state = args.brief.read_text(encoding="utf-8").strip()
    if not state or "{{" in state or len(state) > 12000:
        print("Provide a filled, concise sanitized brief without template markers.", file=sys.stderr)
        return 2
    payload = {"model": "jev-latest", "state": state, "questions": questions(args.mode)}
    request = Request(
        API_URL,
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        result = json.load(response)
    answers = result["answers"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"model": result["model"], "answers": answers}, indent=2) + "\n")
    print(f"Jev model: {result['model']}; result: {args.output}")
    for name, answer in answers.items():
        print(
            f"{name}: score={answer['score']:.2f}, confidence={answer['confidence']:.2f}, "
            f"probabilities={answer['probabilities']}"
        )
    if args.mode == "job":
        for name, answer in answers.items():
            low = sum(answer["probabilities"].get(str(level), 0) for level in range(3))
            if answer["score"] < 2.5 or low > 0.20:
                print(f"Review {name}: local job-readiness guardrail not met.")
    print("Advisory judgment only; verify the underlying evidence and decisions independently.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError) as error:
        print(f"Jev evaluation unavailable: {error}", file=sys.stderr)
        raise SystemExit(2)
