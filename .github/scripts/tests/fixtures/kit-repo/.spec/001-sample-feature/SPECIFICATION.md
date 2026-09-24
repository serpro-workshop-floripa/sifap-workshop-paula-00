---
title: "Specification: Sample Feature"
feature_id: "001-sample-feature"
status: "Draft"
implementation_status: "Not started"
constitution: "../CONSTITUTION.md"
---

# Specification: Sample Feature

## Problem and outcome

Registrations with invalid document numbers reach downstream systems.

## Scope and non-goals

- In scope: document-number validation during registration.
- Out of scope: identity verification with external registries.

## Actors and dependencies

| Actor or dependency | Role | Source |
| --- | --- | --- |
| Registration clerk | Submits registrations | SRC-001 |

## Source register

| Source ID | Evidence | Relevance | Confidence |
| --- | --- | --- | --- |
| SRC-001 | `docs/requirements.md` | Governs both requirements | High |

## Requirements

- **REQ-001:** When a clerk submits a registration with an invalid document number, the registration service shall reject it with error code DOC-01.
  source_legacy: SRC-001, docs/requirements.md#L3
  - Priority: P0. Source: SRC-001. Status: Draft.
  - Pattern: Event-driven
  - Rationale: Invalid documents corrupt downstream records.
  - Acceptance: AC-REQ-001-01 Given an invalid document number, When the clerk submits, Then the service returns DOC-01.
  - Verification: TST-001
- **NFR-001:** While the registration service is under nominal load, the registration service shall answer 95% of validation requests within 300 ms.
  source_legacy: SRC-001, docs/requirements.md#L4
  - Priority: P1. Source: SRC-001. Status: Draft.
  - Pattern: State-driven
  - Rationale: Clerks work interactively.
  - Acceptance: AC-NFR-001-01 Given nominal load, When 1000 validations run, Then the 95th percentile is at most 300 ms.
  - Verification: TST-002

## Assumptions, blockers, and open questions

| ID | Type | Statement | Owner | Impact |
| --- | --- | --- | --- | --- |
| Q-001 | question | Which load counts as nominal? | Product owner | NFR-001 measurement |

## Dispositions

NOT APPLICABLE: no requirement has been split, merged, or retired.

## Review record

NOT APPLICABLE: no review has taken place yet.
