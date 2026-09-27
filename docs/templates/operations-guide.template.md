# {{ System or component }} Kind operations

{{ Supported environment and operational scope. }}

## Build prerequisites

- {{ Tools, versions, access, and target context }}

## Use prerequisites

- {{ Running dependencies, configuration, accounts, and test data }}

## Build

```sh
{{ Exact build commands }}
```

## Deploy to Kind

```sh
{{ Exact image build, Kind load, Helm install/upgrade commands with context, release, and namespace }}
```

{{ Record expected healthy state. List requests and limits for every container, including init containers and dependencies, with chart source paths. }}

## Use and verify

{{ Access path, health checks, expected observable behavior, and links to actual verification. }}

## Undeploy and data retention

```sh
{{ Remove application resources while preserving state when possible }}
```

{{ Distinguish the separate action that permanently deletes data. If no persistent state exists, say so. }}

## Recovery and limits

{{ Failure modes, recovery steps, backup/restore status, and evidence gaps. }}
