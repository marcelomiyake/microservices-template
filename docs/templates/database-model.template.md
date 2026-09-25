# {{ Database or schema }} model

{{ Scope, current status, and authoritative migration/schema source. Remove this document if the project has no owned database. }}

## Ownership and consumers

- **Owner:** {{ repository/component }}
- **Writers/producers:** {{ known components }}
- **Readers/consumers:** {{ known components or Unknown }}
- **Authority:** [{{ migration/schema }}]({{ path }})

## Relations or collections

### {{ Table or collection }}

| Field | Type | Null/default/constraint | Meaning |
| --- | --- | --- | --- |
| {{ name }} | {{ type }} | {{ rule }} | {{ plain-language meaning }} |

{{ Document keys, indexes, relationships, generated fields, retention/cascade rules, and seed-data limits. }}

## Consistency and lifecycle

{{ Transaction boundary, migration procedure, backup/restore, deletion, and retention policy. }}

## Related documentation

- [System design]({{ path }})
- [Contract catalog]({{ path }})
