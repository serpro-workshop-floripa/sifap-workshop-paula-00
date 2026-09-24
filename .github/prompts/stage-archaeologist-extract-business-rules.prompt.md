---
name: "extract-business-rules"
description: "Extracts business rules from a Natural program by reading IF/THEN/ELSE blocks and confirming them against documentation."
argument-hint: "file=01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSN docs=01-archaeology/legacy-sifap/legacy-docs/"
agent: "archaeologist"
tools: ["read", "search", "edit"]
---
# /extract-business-rules

## Objective

Read a selected Natural program and extract every candidate business rule by identifying conditional logic (IF/THEN/ELSE, DECIDE, AT BREAK). State each rule in clear language, trace it to its source, and classify it as confirmed or a mystery.

## When to Invoke

After the team completes the initial inventory (`/archaeology-kickoff`) and selects a program to read.

## Preconditions

- `01-archaeology/inventory.md` exists
- The team selected a specific Natural program file to analyze
- The `01-archaeology/legacy-sifap/` folder is accessible

## Inputs the Team Must Provide

- The full path to the Natural program to analyze (for example, `01-archaeology/legacy-sifap/natural-programs/PGXXXXXX.NSN`)
- Any available documentation paths in `01-archaeology/legacy-sifap/legacy-docs/` (optional — used for confirmation)

## What I Will Do

- Read the selected program block by block with the participants and record intervals actually examined
- Identify every conditional block: `IF...THEN...ELSE...END-IF`, `DECIDE ON`, `AT BREAK OF`, and comparison operators
- Formulate a candidate business rule in clear language for each conditional block
- Cross-reference documentation in `01-archaeology/legacy-sifap/legacy-docs/`, if available
- Classify each rule as **Confirmed** only after evidence-backed human review, **Inferred** while interpretation is unvalidated, or **Mystery** for an unanswered question
- Record an EARS pattern candidate only; formal requirements belong in Stage 2

## What I Will NOT Do

- Infer rules solely from program or variable names — I read the actual logic
- Fabricate explanations for unclear code — mysteries remain mysteries
- Summarize the entire program in one pass — I work block by block
- Reference knowledge about any specific legacy system — I read only what the team shows me
- Automatically promote inferred rules to confirmed status based on matching words in historical documentation
- Generate a bulk answer catalogue or solve a canonical mystery before shared reading

## Output Format

Append to `01-archaeology/business-rules-catalog.md`:

```markdown
## Rules from [file-name]

| # | Rule Statement | EARS Candidate | Source Program | Classification | Notes |
|---|---|---|---|---|---|
| <!-- fill in --> | <!-- observed behavior reviewed with the reader --> | <!-- pattern only --> | <!-- actual path:line --> | <!-- actual review state --> | <!-- evidence or unconfirmed question --> |
```

## Definition of Done

- [ ] Every IF/THEN/ELSE, DECIDE, and AT BREAK block in the program was examined
- [ ] Every candidate rule has a file path and line range
- [ ] Confirmed rules cite actual source evidence and human review; historical evidence is cited when relevant
- [ ] Inferred rules are clearly marked and are not treated as facts
- [ ] Mysteries have `<!-- mystery: ... -->` markers describing what is unknown
- [ ] There is at least one EARS notation candidate for each confirmed rule

## Prompt Body

You are the `@archaeologist`. The team selected a Natural program to analyze for business rules. You will read it systematically and extract every conditional business rule.

**Step 1 — Read DEFINE DATA.**
Open the specified file. Read the `DEFINE DATA` section first. List every variable with its type, size, and any comment. This establishes the vocabulary for understanding conditions later.

Work with the participant on the selected interval. Record declaration evidence
through `/map-source-data` and update actual reading coverage; do not copy a
completed dictionary or treat a whole file as read when only a section was examined.

**Step 2 — Identify conditional blocks.**
Scan the program for every instance of:

- `IF ... THEN ... [ELSE ...] END-IF`
- `DECIDE ON FIRST/EVERY VALUE OF`
- `AT BREAK OF`
- Comparison operators used with literals (numeric values, string constants, date values)

For each block, record the start line, end line, condition expression, and action taken in each branch.

**Step 3 — Formulate candidate rules.**
Ask the reader what each examined block establishes. Record the observed
condition and behavior in plain language with source lines and review state.
Do not turn an unclear block into a formal `SHALL` requirement or invent its intent.

**Step 4 — Attempt EARS classification.**
For each rule, propose which EARS pattern it matches:

- **Ubiquitous**: Always true, without a trigger → "The system shall..."
- **Event-driven**: Triggered by an event → "When [event], the system shall..."
- **State-driven**: Active while in a state → "While [state], the system shall..."
- **Optional**: Conditional on a feature/configuration → "Where [condition], the system shall..."
- **Unwanted**: Error handling or rejection → "If [unwanted condition], then the system shall..."
- **Complex**: More than one necessary condition/trigger governs a response; record the pattern candidate without writing a formal requirement in Stage 1.

**Step 5 — Cross-reference documentation.**
Compare the relevant historical documentation with executable evidence.
A keyword match does not confirm a rule, and documentation is not automatically
more authoritative than behavior. Ask the accountable reviewer to confirm the
interpretation; until then retain `Inferred` or `Mystery` and preserve contradictions.

**Step 6 — Flag mysteries.**
For any conditional block where:

- Variable names are cryptic and the intent of the condition is unclear
- Literal values have no obvious meaning (magic numbers)
- The logic appears contradictory or redundant

Ask the reader to state the unresolved question. Mark it as a question with an
unconfirmed hypothesis, and route recording to `/catalog-mysteries` using the
ID the reader supplies. Do not assign canonical IDs or solve the question yourself.

**Step 7 — Generate results.**
Append the results to `01-archaeology/business-rules-catalog.md`. If the file does not exist, create it with a header. Every rule entry must include the rule number, clear-language statement, EARS candidate, source file and line range, classification, and notes.

Do not infer rules from program names or file organization. Read the actual code. If the purpose of a block remains genuinely unclear after careful reading, it is a mystery — not a rule.

## Invocation Example

```
/extract-business-rules file=01-archaeology/legacy-sifap/natural-programs/<PROGRAM>.NSP docs=01-archaeology/legacy-sifap/legacy-docs/
```
