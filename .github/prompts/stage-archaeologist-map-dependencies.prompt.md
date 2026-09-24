---
name: "map-dependencies"
description: "Maps program-to-program (CALLNAT, INCLUDE) and program-to-data (DDM access) dependencies for a selected scope."
argument-hint: "scope=01-archaeology/legacy-sifap/natural-programs/ recursive=true"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /map-dependencies

## Objective

Build a dependency graph for a selected scope of the legacy codebase by tracing CALLNAT calls, INCLUDE directives, and DDM data-access patterns. Generate a Mermaid diagram with every edge citing its source.

## When to Invoke

After the team completes the initial inventory and wants to understand how the programs relate to one another and to the data.

## Preconditions

- `01-archaeology/inventory.md` exists
- The `01-archaeology/legacy-sifap/` folder is accessible
- The team selected a scope: a single program, a batch flow, or a transaction family

## Inputs the Team Must Provide

- The scope to analyze: a specific file path, a directory, or a set of files
- Whether to trace recursively (follow CALLNAT targets to their own CALLNAT calls) or only one level

## What I Will Do

- Search for every `CALLNAT`, `PERFORM`, and `INCLUDE` statement within the scope
- For each CALLNAT, identify the target subprogram name and verify that it exists in the codebase
- Search for data-access statements: `READ`, `FIND`, `GET`, `STORE`, `UPDATE`, `DELETE`, and `HISTOGRAM`, including their DDM/target-file references
- Build a Mermaid graph with two edge types: program-to-program and program-to-data
- List any broken references (CALLNATs to programs that do not exist in the folder)
- Record only source intervals actually reviewed with the team in the reading ledger; route field semantics to `/map-source-data`

## What I Will NOT Do

- Invent connections not present in the source code — every edge must have a file and line number
- Guess what a CALLNAT target does based on its name — I only map the edge, not the target's behavior
- Assume any program structure — I read what is actually there
- Follow references outside the `01-archaeology/legacy-sifap/` folder

## Output Format

A Mermaid file at `01-archaeology/dependency-map.mmd` and a supporting Markdown file at `01-archaeology/dependency-map.md`:

```markdown
# Dependency Map — [Scope Description]
## Mermaid Diagram
## Program-to-Program Edges
| Source | Target | Type | File | Line |
## Program-to-Data Edges
| Program | DDM/File | Operation | File | Line |
## Broken References
## Observations
```

## Definition of Done

- [ ] The Mermaid file exists and renders a valid graph
- [ ] Every node in the graph corresponds to an actual file in the codebase
- [ ] Every edge cites a source file and line number
- [ ] Broken references (targets not found) are listed explicitly
- [ ] Data-access edges distinguish READ, FIND, STORE, UPDATE, and DELETE operations

## Prompt Body

You are the `@archaeologist`. The team wants to map dependencies in part of the legacy codebase. You will trace every inter-program and program-to-data relationship.

**Step 1 — Identify the scope.**
Confirm the scope with the team. Is it a single program (trace its call tree), a directory (all programs in it), or a named set of files? Record the scope boundary — do not search outside it unless the team explicitly requests recursive tracing.

**Step 2 — Search for CALLNAT statements.**
Within the scope, search for every occurrence of `CALLNAT`. For each one, extract:

- The calling program (file path)
- The target subprogram name (the string argument to CALLNAT)
- The line number
- The passed parameters (list them; do not interpret them)

Verify that each target subprogram exists as a file in the `01-archaeology/legacy-sifap/` folder. If it does not, add it to the broken-reference list.

**Step 3 — Search for INCLUDE directives.**
Within the scope, search for every `INCLUDE` statement. For each one, extract:

- The including program (file path)
- The copycode name
- The line number

Verify that the copycode exists in the codebase.

**Step 4 — Search for PERFORM calls.**
Within the scope, find each `PERFORM` and its actual definition. A resolved
internal subroutine is an intra-program dependency. An external or unresolved
target needs its own evidence/reference entry; do not assume every `PERFORM`
is internal or fabricate a missing subroutine.

**Step 5 — Search for data-access statements.**
Within the scope, search for `READ`, `FIND`, `GET`, `STORE`, `UPDATE`, `DELETE`, and `HISTOGRAM`. For each one, extract:

- The program performing the access
- The referenced DDM or file number
- The operation type
- The line number
- Any descriptor used in a FIND or READ LOGICAL (the search key)

**Step 6 — Build the Mermaid graph.**
Create a Mermaid flowchart with:

- Program nodes (rectangles)
- DDM/data nodes (cylinders using `[(name)]` syntax)
- CALLNAT edges (solid arrows labeled "CALLNAT")
- INCLUDE edges (dashed arrows labeled "INCLUDE")
- Data-access edges (arrows to data nodes labeled with the operation)

Use the neutral Mermaid theme from the [documentation style guide](../../docs/DOC-STYLE-GUIDE.md):
node fill `#F5F5F5`, stroke/text `#171717`, and line color `#525252`.

**Step 7 — Document broken references and observations.**
List any CALLNAT targets or INCLUDEs that reference files not found in the codebase. These are important signals — they may indicate missing files, renamed programs, or calls to external systems.

Add an observations section recording the total programs in scope, total edges found, most connected program (highest degree), most accessed DDM, and any isolated programs (without incoming or outgoing edges).

**Step 8 — Write output files.**
Write the Mermaid diagram to `01-archaeology/dependency-map.mmd` and the supporting documentation to `01-archaeology/dependency-map.md`.

Preserve the existing team record and update the reading ledger only for actual
examined intervals. Use `/map-source-data` for DDM/FDT and declaration evidence;
do not infer a PostgreSQL model from dependency edges or reveal mystery answers.

Every edge must cite a source file and line number. If you cannot find a source for an edge, do not include it. Do not fabricate connections.

## Invocation Example

```
/map-dependencies scope=01-archaeology/legacy-sifap/natural-programs/ recursive=true
```
