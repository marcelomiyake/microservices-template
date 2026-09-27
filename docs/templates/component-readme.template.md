# {{ Component name }}

{{ Purpose, runtime, and role in the parent system. }}

## Ownership and contracts

- **Owner:** {{ repository/component or team }}
- **Producers/callers:** {{ known callers }}
- **Consumers:** {{ known consumers or Unknown if not inspected }}
- **Authoritative contract:** [{{ OpenAPI, event schema, or source }}]({{ path }})
- **Parent design:** [System design]({{ path }})

## Build prerequisites

- {{ Toolchain and dependency versions }}

## Build and run

```sh
{{ Exact commands and working directory }}
```

## Verify

```sh
{{ Focused checks and required fixtures }}
```

{{ Link actual verification records; state unrun checks as gaps. }}

{{ Distinguish unit, integration, and real Kind E2E checks. Link coverage and SonarQube evidence when this component is in scope. }}

## Use and operations

{{ Access path, configuration, runtime dependencies, health behavior, stop/undeploy, and data effects where applicable. }}

## Related documentation

- [Project README]({{ path }})
- [Documentation index]({{ path }})
- [Agent guidance]({{ path }})
