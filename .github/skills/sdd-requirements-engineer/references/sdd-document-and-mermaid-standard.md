# SDD document and Mermaid standard

Use this as a content reference for official Spec-Kit artifacts under `specs/`.
The [kit binding](../SKILL.md#binding-to-this-participant-kit) is authoritative:
uppercase names below describe responsibilities within `spec.md`, `plan.md`,
and `tasks.md`, not required additional files or a parallel `.specs/` tree.

## Artifact responsibilities

| Artifact | Required responsibility |
| --- | --- |
| `SPECIFICATION.md` | Canonical REQ/NFR statements, acceptance, assumptions, dependencies, open decisions, and evidence-based implementation status |
| `ANALYSIS.md` | Gate summary, bidirectional traceability, dated evidence, findings, approval conditions, and sign-off |
| `DESIGN.md` | Architecture, context, components, deployment, state, sequences, data, interfaces, failures, security, observability, implementation surface, delivery traceability, and phased state |
| `TASKS.md` | Pre-gate, execution rules, dependency DAG, test mapping, phased checkboxes, completion gate, and execution ledger |
| `TESTING.md` | Named tests, deterministic commands, failure injection, evidence contract, exit criteria, and dated verification state |
| `DECISIONS.md` | Stable decisions, status, context, alternatives, consequences, traces, evidence, and revisit triggers |
| `checkpoints/` | Machine-readable requirement-to-plan-to-task-to-test closure |
| `contracts/` | Versioned API/state contracts or a reviewed non-applicability manifest |

## Universal Mermaid theme

Follow the [kit documentation style guide](../../../../docs/DOC-STYLE-GUIDE.md).
Begin Mermaid blocks with the kit's neutral directive:

```text
%%{init: {'theme':'neutral','themeVariables':{'fontFamily':'ui-sans-serif, system-ui, sans-serif','primaryColor':'#F5F5F5','primaryTextColor':'#171717','primaryBorderColor':'#171717','lineColor':'#525252','secondaryColor':'#FFFFFF','tertiaryColor':'#FAFAFA','background':'#FFFFFF'}}}%%
```

For `flowchart`, `graph`, and `classDiagram`, include these
definitions exactly once:

```text
classDef default fill:#F5F5F5,stroke:#171717,color:#171717
classDef zone fill:#FFFFFF,stroke:#525252,color:#171717
classDef external fill:#FAFAFA,stroke:#A3A3A3,color:#404040
```

Use `zone` for owned boundaries and logical groupings, and `external` for
actors, external systems, neighboring specifications, or evidence sources
outside the feature boundary. `stateDiagram`, `sequenceDiagram`, `erDiagram`,
and `gantt` inherit the universal theme and must not contain `classDef`.
Current `stateDiagram-v2` renderers treat `default` as a reserved token.

Keep diagrams reviewable:

- fewer than 40 nodes per block;
- short labels, with detail in adjacent tables;
- quoted edge labels;
- explicit subgraph IDs;
- no chromatic colors;
- separate current, partial, planned, blocked, and target states.

## Required design portfolio

When material to the feature, `DESIGN.md` includes:

1. Architecture Overview
2. System Context
3. Component or Service Map
4. Deployment View
5. State Model
6. Critical Sequences
7. Data Flow or Data Lifecycle
8. Data Model
9. Interfaces and Contracts
10. Error, Security, Threat, and Observability design
11. Implementation Surface
12. Delivery and Traceability View
13. Risks and Trade-Offs
14. Phased Development

The delivery view maps real REQ/NFR IDs to design components, plan items and
tasks, dependency IDs or neighboring specs, tests/evidence, and
current-versus-target state. Do not invent an implementation or approval to
complete a diagram.

## Task contract

Use one checkbox entry per task:

```text
- [ ] **T001 [S] [Plan:P1.1] RED** Add a failing contract test. Traces REQ-001.
  - Files: `<actual test path for the selected Java or TypeScript feature>`.
  - Acceptance: TST-C001 fails before implementation and passes afterward.
```

- `[S]` means sequential; `[P]` means dependency- and change-surface independent.
- The dependency DAG contains every task exactly once.
- The test map names the governing requirements and planned or executed tests.
- `[x]` is allowed only when the task appears in the dated
  `Marked complete by verification sweep:` ledger and its acceptance evidence
  exists.
- Existing partial code stays unchecked until the complete acceptance signal is
  demonstrated.

## Required validation

Use the actual checks defined in
[spec-quality.yml](../../../workflows/spec-quality.yml) and the existing
primitive validator when primitives change. Inspect available scripts before
running them. Generic SDD generators and validators are not shipped by this kit;
do not claim they exist or fabricate their output. Use reviewed artifact
evidence for checks that have no executable gate.

Report a failing or blocked check as such. Never weaken a gate, add a baseline,
or create empty evidence merely to obtain a green result.
