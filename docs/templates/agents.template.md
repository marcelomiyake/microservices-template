# {{ Project or component }} guidance

> Human guide: [README]({{ relative path }}) · [Documentation index]({{ relative path }})

## Sources of truth and boundaries

- Architecture: [System design]({{ relative path }}).
- Contract: [{{ authoritative schema or code }}]({{ relative path }}).
- This component owns {{ responsibilities }}. {{ Explicit adjacent ownership boundary. }}

## Work and verification

- Build: `{{ exact command }}`.
- Focused checks: `{{ exact command }}`; required fixtures: {{ dependencies or none }}.
- Keep source, contracts, component README, architecture docs, and Helm chart aligned. Report only checks actually run.
- Use a DDD job brief for non-trivial domain work. For frontend work, update the OpenDesign handoff. Run unit, integration, and Kind E2E checks relevant to the change; verify coverage and the SonarQube gate. Jev scores are advisory and require sanitized evidence.

## Safety and conventions

- Verify the intended Kind context and namespace before deployment. Set CPU and memory requests and limits for every container.
- {{ Data, secrets, coding, and commit conventions that apply here. }}
