# ADR-0003: The workshop is an individual challenge from Stage 1 to Stage 3

> **Path:** [Team Kit](../../README.md) › [Docs](../README.md) › [ADRs](README.md) › **ADR-0003**

| Field | Value |
|---|---|
| **Status** | accepted |
| **Date** | 2026-09-24 |
| **Authors** | Kit maintainers |
| **Supersedes** | The team/pair format described in `00-TEAM-FLOW.md` before this date |

---

## Context

The kit was designed for five participants working as five role pairs over an
eight-hour day. It had four stages with 260 minutes of stage work, plus three
live handoffs (H1, H2, H3) between pairs.

The event now runs from 14:00 to 17:40 (220 minutes). Each participant works
alone and does the whole modernization. The first two participants who prove a
correct result win. With that format:

- the team-based stage budget does not fit;
- pairs and handoffs between different people no longer exist;
- independent QA cannot come from a second participant;
- Stage 4 (evolution with the coding agent) does not fit in the time available.

We also evaluated a parallel sub-agent orchestrator for Stage 3. Its gain is
limited by serial work (data migration, reconciliation, test runs). It would
make comparisons between participants unfair and hide the exercise behind
automation.

## Decision

1. **Individual format.** Each participant covers all 10 roles. Roles stay
   skills ([ADR-0002](0002-team-roles-as-skills-not-agents.md)); the participant
   only switches stage agents.
2. **Schedule.** The participant starts directly in `@archaeologist` at 14:00.

   | Time | Step | Agent |
   |---|---|---|
   | 14:00-14:50 | Stage 1 - Archaeology | `@archaeologist` + `@dba` |
   | 14:50-15:30 | Stage 2 - Specification | `@architect` + `@dba` |
   | 15:30-17:10 | Stage 3 - Implementation and data migration | `@builder` + `@dba` |
   | 17:10-17:40 | Final judge validation | Judge |

   Setup and the authorized, populated Adabas source are pre-work, finished
   before 14:00.
3. **Stage 4 is out of the challenge.** Its files stay in the kit, marked as not
   used.
4. **Handoffs become self-checkpoints** C1, C2, and C3. They use the same
   artifacts and definition of done as before. C3 is the submission.
5. **Fixed target capability.** Everyone must list, search, and show the detail
   of **all** beneficiaries migrated from Adabas to PostgreSQL, applying the
   legacy validation rules they discover.
6. **Finish line.** CI is green (including `legacy-traceability`), every
   requirement has a REQ-ID, EARS, and `source_legacy:`, tests pass, the data is
   reconciled (source = loaded + explained rejects; keys and aggregates match;
   rerun without duplicates), and the queries cover the whole population.
7. **Winners.** The first two submissions that pass judge validation win. The
   timestamp is the creation of the PR `impl/<NNN>-<feature>` -> `develop`.
   17:10 is the submission deadline. A rejected submission can be fixed and
   resubmitted with a new timestamp.
8. **Independence.** The judge's verification replaces cross-pair review and
   independent QA. Judge scripts and expected values stay in the private
   instructor repository.
9. **No orchestrator.** Parallel sub-agent orchestration is not allowed.

## Consequences

- Faster to run and easy to compare: one fixed capability and one objective
  finish line.
- Less practice in collaboration and delegation. Stage 4 content remains
  available for a later session.
- The judge becomes a single point of verification, so the judge validates
  continuously as submissions arrive.
- The rule "reduce capability breadth, never the migrated population or the
  verification standard" still applies. An incomplete submission does not win.
