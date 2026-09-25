# {{ Project name }}

{{ One sentence describing purpose, status, and audience. }}

## Scope and architecture

{{ Key capabilities, system boundary, components, and important local/demo limits. Link the system design. }}

## Repository map

| Path | Owner | Responsibility |
| --- | --- | --- |
| {{ path }} | {{ component/team }} | {{ responsibility }} |

## Build prerequisites

- {{ Tool and supported version }}

## Use prerequisites

- {{ Running dependency, configuration, account, or test data needed by a user }}

## Build and verify

```sh
{{ Exact build and test commands; state any required fixture or environment variable }}
```

## Deploy to Kind

```sh
{{ Exact image build, Kind load, Helm install/upgrade, and loopback port-forward commands }}
```

{{ State Kind cluster, context, namespace, release, configuration, and expected healthy result. Link chart and resource budgets. }}

## Use

{{ Access path and first useful operation. Link real screenshots only after capturing them from a running UI. }}

## Undeploy

```sh
{{ Exact Helm uninstall or guarded script command }}
```

{{ Explain persistent-data retention and any separate destructive command, if applicable. }}

## Contracts and documentation

- [Documentation index](docs/README.md)
- [System design](docs/system-design.md)
- [Contract catalog](docs/contracts/README.md)
- [Verification records](docs/verification/README.md)
- [Agent guidance](AGENTS.md)
- [Testing and quality gates](docs/quality-gates.md)

## Frontend design and agent workflow

{{ Link the OpenDesign-reviewed frontend handoff, DDD agent-job practice, Jev advisory evidence if used, and Conventional Commits convention. State unavailable tools accurately. }}

## License and attribution

{{ License, external sources, and accurate project-specific attribution. Do not inherit AI/tool claims from another repository. }}
