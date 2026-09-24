---
description: "Use when creating or reviewing automated tests, test strategy, coverage gaps, regression tests, and quality gates in any stack."
applyTo: "**/*.test.*,**/*.spec.*,**/test_*.py,**/*_test.*,**/*Test.java,**/*Tests.cs,**/tests/**,**/test/**,**/__tests__/**"
---

# Test Conventions — Structure, Traceability, and Coverage

This file opens for any test file, backend or frontend. It covers test structure and naming, tool choice per stack, REQ-ID traceability, and coverage targets. Tests are written **during** implementation, never afterwards. JUnit assertion detail lives in [java-junit5-assertions.instructions.md](java-junit5-assertions.instructions.md).

The effective test stack (framework, commands, and coverage thresholds) is the one declared in [copilot-instructions.md](../copilot-instructions.md) or the project constitution. The tables below are a reference until the project decides.

## Test Pyramid

| Layer | What it proves | Share |
| --- | --- | --- |
| Unit (pure logic, services) | Business rules without I/O | Most |
| Integration (repositories, APIs, components) | Behavior with real dependencies or rendering | Fewer |
| End to end | Critical user flow | Few |

## Reference Tools per Stack

| Stack | Unit | Integration | E2E |
| --- | --- | --- | --- |
| JavaScript/TypeScript (Node) | `node:test`, Vitest, or Jest | Supertest, Testcontainers | Playwright |
| Frontend (React/Vue) | Vitest + Testing Library | Testing Library + MSW | Playwright |
| Java | JUnit 5 + AssertJ | Testcontainers | Playwright |
| Python | pytest | pytest + Testcontainers | Playwright |
| .NET | xUnit or NUnit | Testcontainers | Playwright |

Adopt only tools the project already uses or that an ADR approved.

## Structure: Arrange-Act-Assert

Each test has three visible phases and verifies one behavior. Mock only external boundaries (network, clock, third-party services), never the class or function under test.

```ts
import { describe, it, expect } from 'vitest';
import { calculateTotal } from './cart';

describe('calculateTotal', () => {
  it('should_apply_discount_when_coupon_is_valid', () => { // REQ-002
    const items = [{ price: 100 }, { price: 50 }];            // Arrange
    const total = calculateTotal(items, { coupon: 'OFF10' }); // Act
    expect(total).toBe(135);                                  // Assert
  });
});
```

## Naming

Name tests `should_<expected behavior>_when_<condition>`, or express the same intent in natural language in `it(...)` or `@DisplayName`. Keep one language per project.

```text
should_return_409_when_identifier_already_exists
should_render_empty_state_when_no_items
should_reject_sequence_when_fewer_than_three_numbers
```

## Real Dependencies Versus Test Doubles

- When data behavior matters (queries, transactions, constraints), use the real dependency in a container (Testcontainers or equivalent) instead of an in-memory substitute with different semantics.
- Use doubles only for slow, non-deterministic, or non-existent collaborators.
- Do not mock types you do not own; wrap them in a thin abstraction first.

## Frontend

Query elements by accessible role or label, never by `data-testid` when a role exists. Drive interaction with `user-event`. Avoid snapshot-only tests.

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { ArchiveButton } from './ArchiveButton';

describe('ArchiveButton', () => {
  it('should call onArchive when clicked', async () => { // REQ-032
    const onArchive = vi.fn().mockResolvedValue(undefined);
    render(<ArchiveButton id="1" onArchive={onArchive} />);
    await userEvent.click(screen.getByRole('button', { name: /archive/i }));
    expect(onArchive).toHaveBeenCalledWith('1');
  });
});
```

## REQ-ID Traceability and TDD

Every test that verifies a requirement cites its ID in a comment on the same line or just above (`// REQ-NNN`, `# NFR-NNN`). That feeds the test-binding check in [sdd-artifacts.instructions.md](sdd-artifacts.instructions.md), which lists requirements no test references yet.

For every business rule, the RED task in `tasks.md` runs first and must fail for the missing behavior; `python3 .github/scripts/validate-red-phase.py -- <test command>` proves the failure before the GREEN task starts.

## Coverage Targets

Use the thresholds the project defines. If none exist, propose thresholds and record them as a team decision (a common start is 80% lines and 70% branches, higher for business rules). Configure them in the coverage tool so the test command fails below the minimum.

> [!NOTE]
> Coverage is a floor, not a goal. A branch without an assertion is untested even when the line counts as covered. Verify behavior, not just the call.

## Conventions

| Rule | Rationale |
| --- | --- |
| Arrange-Act-Assert, one behavior per test | Readable and isolates the failure |
| Mock only external boundaries | Real dependencies catch real bugs |
| Names `should_<behavior>_when_<condition>` | Clear intent in the report |
| `REQ-NNN` or `NFR-NNN` comment in requirement tests | Keeps spec-to-test traceability live |
| RED proven before GREEN | A test that never failed proves nothing |
| Written during implementation | Untested code is not integrated |

## Do / Do Not

| Do | Do not |
| --- | --- |
| Use the real containerized dependency when data matters | Replace the database with an in-memory equivalent with different semantics |
| Query by role or label | Query by `data-testid` when a role exists |
| Verify behavior and edge branches | Rely only on snapshots or line coverage |
| Write the test together with the code | Add tests after the feature is "done" |
| Skip or weaken a test only with an issue and justification | Skip tests to force a green pipeline |

## Checklist Before Opening a PR

- [ ] New behavior has unit tests; persistence has an integration test with a real dependency where applicable.
- [ ] Tests follow Arrange-Act-Assert and the project naming convention.
- [ ] Requirement-driven tests carry a `REQ-NNN` or `NFR-NNN` comment.
- [ ] Business rules cover the happy path, validation failure, and authorization failure where it exists.
- [ ] Coverage meets the project minimum.
- [ ] Every external boundary is mocked and no required real dependency was replaced by a mock.
