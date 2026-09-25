# {{ Agent job title }}

- **Actor and outcome:** {{ Who needs what observable result? }}
- **Domain context and language:** {{ Bounded context, terms, invariants, state transitions }}
- **Repository evidence:** {{ Paths and revision supporting confirmed facts }}
- **Assumptions and open decisions:** {{ Separate each from confirmed facts; name an owner or discovery action }}
- **Scope and exclusions:** {{ In and out of scope }}
- **Owners and contracts:** {{ Data/interface owner, producer, consumers, dependency order }}
- **Deliverables:** {{ Reviewable files or behavior }}
- **Acceptance:** {{ Exact checks, fixtures, Kind flow, and expected results }}
- **Risks and limits:** {{ Data, security, authorization, failure, recovery, stop condition }}

Use this brief for the manual DDD job review. For an authorized Jev assessment, remove placeholders and sensitive material, then run `python3 scripts/jev-verify.py --mode job --brief <path>` from the repository root. The returned scores are advisory.
