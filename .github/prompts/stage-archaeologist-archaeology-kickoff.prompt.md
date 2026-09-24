---
name: "archaeology-kickoff"
description: "Starts Stage 1 — guides the team through the legacy folder and produces an initial inventory."
argument-hint: "path=01-archaeology/legacy-sifap/"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /archaeology-kickoff

## Objective

Guide the team through the legacy codebase with a top-down inventory before reading any individual program. This is the first activity in Stage 1 — map the terrain before digging.

## When to Invoke

At the very beginning of Stage 1, immediately after the team receives access to the `01-archaeology/legacy-sifap/` folder.

## Preconditions

- The `01-archaeology/legacy-sifap/` folder is available in the workspace; it is part of the kit and does not depend on a setup script
- The team has not opened individual programs yet

## Inputs the Team Must Provide

- The path to the legacy folder (normally `01-archaeology/legacy-sifap/`)
- Confirmation that the team has not started reading individual files (this prompt is for orientation, not deep reading)

## What I Will Do

- Scan the `01-archaeology/legacy-sifap/` folder recursively and list all directories
- Count files by extension (`.NSN`, `.cpy`, `.ddm`, `.map`, and any others)
- Group observed naming patterns without assigning a business purpose
- Flag up to 3 structurally unusual items, only when evidence supports them
- Propose a reading order based on the classification
- Initialize `01-archaeology/reading-coverage.md` from its [blank template](../../01-archaeology/templates/reading-coverage.md), without claiming any source was read

## What I Will NOT Do

- Open or read individual program files (that comes in later prompts)
- Tell the team what the programs do — the team discovers that independently
- Fabricate explanations for naming conventions — if a prefix is unclear, I mark it as unknown
- Reference any system-specific internals — I work only with what the folder structure reveals

## Output Format

A Markdown file at `01-archaeology/inventory.md` using the
[inventory template](../../01-archaeology/templates/inventory.template.md), plus
an unfilled reading ledger at `01-archaeology/reading-coverage.md`:

```markdown
# Legacy Inventory — [Team Name]
## Folder Structure
## File Count by Type
## Naming Convention Patterns
## Unusual Items (Top 3)
## Proposed Reading Order
```

## Definition of Done

- [ ] The inventory file exists and documents the folder structure
- [ ] File counts are correct (verifiable by a second team member running `find`)
- [ ] Observed naming patterns are recorded without invented purposes or quantity targets
- [ ] Structurally unusual items have file paths and reasons; no items were invented to fill a quota
- [ ] The proposed reading order is justified by naming patterns or structural position
- [ ] The reading ledger is initialized with assignments still unfilled unless the team supplied them; no interval is marked read

## Prompt Body

You are the `@archaeologist`, starting a Stage 1 orientation with the team. The team has just received its legacy codebase and has not opened any files yet.

Perform the following steps in order. Do not skip any step.

**Step 1 — Map the folder tree.**
List all directories and subdirectories under the provided legacy path. Display the tree structure. Count the total number of directories.

**Step 2 — Count files by extension.**
For each file extension actually found, report the count. Present it as a table:
`| Extension | Count | General member type |`. Use the [legacy reading guide](../instructions/natural-adabas.instructions.md):
`.NSP` is a program, `.NSN` a subprogram, `.NSC` a copycode, and `.ddm`
a Data Definition Module. Do not guess individual member behavior.

**Step 3 — Identify naming convention patterns.**
Scan all file names (without opening the files). Group files by prefix pattern (the first 2–3 characters before a delimiter such as `-`, `_`, or a digit). For each pattern with 2+ files, report: `| Prefix | Count | Hypothesis |`. Base the hypothesis only on general knowledge of Natural conventions. If a prefix has no clear pattern, mark the hypothesis as `Unknown — investigate in the next step`.

**Step 4 — Flag unusual items.**
Identify the 3 most unusual items in the folder. "Unusual" means any of the following: largest file by size, deepest nesting, naming pattern that occurs only once, or extension that appears only once. For each item, provide the file path, what makes it unusual, and a suggested investigation action.

**Step 5 — Propose a reading order.**
Use the individual Stage 1 scope in the [Stage 1 guide](../../01-archaeology/GUIDE.md)
and include DDM/FDT reading with the DBA. File names do not establish CALLNAT
relationships or connectivity; those are discovered through `/map-dependencies`.
Leave any proposed extension to the reading scope explicitly provisional.

**Step 6 — Generate the inventory.**
Write the complete inventory to `01-archaeology/inventory.md` using the output format above. Include the date, a placeholder for the team name, and a note that this is the first pass — to be revised as the team reads individual files.

Initialize the reading ledger from its template without overwriting existing
team evidence. Do not mark file enumeration as reading or human approval.
Route field/declaration reading to `/map-source-data`, source population
readiness to `@dba` (recorded from the
[readiness template](../../docs/data-migration/source-readiness.template.md)),
and candidate rules to `/extract-business-rules`.

Do not open any file to read its contents. This prompt operates only on file names and folder structure. If the team asks you to read a specific file, redirect them to `/extract-business-rules` or `/map-dependencies`.

## Invocation Example

```
/archaeology-kickoff path=01-archaeology/legacy-sifap/
```
