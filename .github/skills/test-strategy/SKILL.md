---
name: "test-strategy"
description: "Use when designing a test strategy, choosing the test-pyramid shape, defining coverage targets, or evaluating testing investments across unit, integration, and E2E layers. Triggers include \"test strategy\", \"test pyramid\", \"coverage target\", \"E2E vs integration\", and \"testing investment\"."
---
# Test strategy

## When to invoke

- "Design a test strategy for…"
- "How much unit vs integration vs E2E testing?"
- "What coverage target is right?"
- "Audit our test pyramid."

## Workflow

1. **Inventory** the code under test: modules, public APIs, external integrations, and critical paths.
2. **Classify risk** by module (P0 / P1 / P2) based on the blast radius if it fails.
3. **Allocate tests by risk**: prefer fast focused tests, real persistence integration checks, and only the necessary end-to-end flows; do not invent a mandatory percentage mix.
4. **Use the kit C3 floors**: 70% backend and 60% frontend line coverage, plus meaningful critical-branch and REQ-ID checks. Stricter targets need an explicit participant decision.
5. **Review flaky tests** under the team-approved policy; no automatic percentage-triggered quarantine or deletion of required verification.
6. **Reuse existing approved tools**: JUnit 5, Testcontainers, Vitest and Testing Library. Additional tools require a reviewed need and dependency decision.
7. **Output**: a one-page strategy document with per-layer targets, tools, coverage thresholds, and quarantine rules.

## Heuristics

- If an E2E test can be rewritten as an integration + contract test, do it—E2E is expensive and flaky.
- Contract tests beat mocks for anything that crosses a service boundary.
- Mutation testing can supplement review of assertions when already approved; it is not the only way to assess test quality or permission to add new tooling.

## Anti-patterns

- Inverted pyramid: many slow E2E tests sitting on top of few unit tests.
- One global coverage number with no higher target for P0 modules.
- Mocked service boundaries that never catch a real integration break.
- Coverage treated as the goal instead of a proxy for confidence.

## Output template

```markdown
## Test strategy - <system or module>

| Layer | Target mix | Tools | Coverage target |
|---|---|---|---|
| Unit | <risk-based scope> | JUnit 5 / Vitest | <REQ-ID and critical-branch coverage> |
| Integration | <required persistence/data paths> | Testcontainers | <source-to-target and query checks> |
| UI / end-to-end | <approved user flows> | <existing approved tools> | <observable acceptance> |

**Flaky-test policy**: <reviewed owner, evidence, review date and replacement verification>
**Risk classification**: P0 <modules> / P1 <modules> / P2 <modules>
```

## Quality gate

- [ ] Every module is risk-classified (P0/P1/P2) with a coverage target.
- [ ] The test mix follows actual risk and available tools, not an arbitrary 70/20/10 quota.
- [ ] Each layer names its tool and threshold.
- [ ] A flaky-test budget and quarantine rule are defined.

## References

- [Google Testing Blog - Test Sizes](https://testing.googleblog.com/2010/12/test-sizes.html)
- [ISTQB Foundation Syllabus](https://www.istqb.org/certifications/certified-tester-foundation-level)
- [Martin Fowler - Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
