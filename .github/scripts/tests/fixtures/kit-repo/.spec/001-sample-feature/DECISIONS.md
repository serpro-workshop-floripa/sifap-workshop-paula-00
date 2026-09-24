# Decisions: Sample Feature

## DR-001: Validate inside the registration service

- Status: proposed
- Requirements: REQ-001, NFR-001
- Context: Validation must answer within the NFR-001 budget.
- Decision: Validate in-process.
- Alternatives: A remote validation service, rejected for latency.
- Consequences: The rule ships with the service.
- Revisit trigger: A second consumer needs the same rule.
