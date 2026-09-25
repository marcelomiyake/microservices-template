# Contract catalog

The [OpenAPI definition](openapi.yaml) describes the current local HTTP endpoints. Keep it synchronized with handlers and clients.

| Contract | Owner | Producer | Known consumer | Authority |
| --- | --- | --- | --- | --- |
| `GET /example` | `services/example-service` | `services/example-service` | `services/web-api` | [OpenAPI](openapi.yaml) · [handler](../../services/example-service/src/lib.rs) |
| `GET /api/example` | `services/web-api` | `services/web-api` | `web` | [OpenAPI](openapi.yaml) · [handler](../../services/web-api/src/lib.rs) |

The example has no event, queue, or database contract. A generated project should add a record for each new interface with owner, producer, consumers, version, errors, retry and compatibility behavior. See [the contract template](../templates/api-contract.template.md).
