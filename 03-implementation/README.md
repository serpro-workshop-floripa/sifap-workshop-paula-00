# Stage 3 — Implementation

> **Path:** [Team Kit](../README.md) › **Stage 3 — Implementation**

**In this stage, the participant build the SIFAP 2.0 prototype from scratch: a Java 21 + Spring Boot 3.3 backend, a Next.js 15 frontend, and PostgreSQL 16, guided by the REQ-IDs from Stage 2.**

![Stage 3](https://img.shields.io/badge/Stage-3%20%C2%B7%20Implementation-171717?style=flat-square) ![Led by the participant](https://img.shields.io/badge/Lead-Participants%203%20and%204-404040?style=flat-square) ![Deliverable Code and Tests](https://img.shields.io/badge/Deliverable-Code%20%2B%20Tests-737373?style=flat-square)

| Field | Value |
|---|---|
| **Target audience** | Participants 3 (TL+Dev) and 4 (DBA+QA); the participant scaffolds CI |
| **Prerequisites** | C2 checkpoint accepted; `spec.md`, `plan.md`, and `tasks.md` ready |
| **Estimated time** | 100 min (15:30–17:10) |
| **Stage** | Stage 3 — Implementation |
| **Expected outcome** | Functional application with PostgreSQL populated from Adabas, reconciled data, beneficiary queries, and tests traced to REQ-IDs |

---

## Where this fits in the day's flow

![Day timeline: pre-event, 4 stages, and integrated validation, with the three C1, C2, and C3 checkpoints](../assets/timeline-stages.svg)

## Who works here

![Persona distribution by pair: vision, architecture, implementation, quality, and operations](../assets/personas-participant.svg)

## Contents of this folder

DBA executes the approved snapshot-to-PostgreSQL migration; QA independently
reconciles it and Developer exposes authorized listing, search, and detail
queries for all beneficiaries in the agreed population. Flyway schema history
and test seeds alone do not meet C3. Follow the
[data migration guide](../docs/DATA-MIGRATION.md).

| File | Purpose |
|---|---|
| [`GUIDE.md`](GUIDE.md) | Stage step-by-step guide |

---

### Continue reading

| Previous | Next |
|---|---|
| [Stage 2 — Specification](../02-modern-spec/README.md)<br/><sub>Modern specification summary and links to ADR templates.</sub> | [Stage 3 — GUIDE](GUIDE.md)<br/><sub>15:30–17:10 · Java 21 + Spring Boot + Next.js, with tests.</sub> |

<sub>[Back to the kit index](../README.md)</sub>
