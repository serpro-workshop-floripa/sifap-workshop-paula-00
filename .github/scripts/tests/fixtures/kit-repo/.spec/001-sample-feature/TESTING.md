# Testing: Sample Feature

## Test catalog

| Test | Requirements | Location | Level | Status |
| --- | --- | --- | --- | --- |
| TST-001 | REQ-001 | `tests/test_sample.py` | unit | Planned |
| TST-002 | NFR-001 | `tests/test_sample.py` | performance | Planned |

## Commands

Run `python3 -m pytest tests/test_sample.py`.

## Failure and measurement

TST-001 must fail before T002; TST-002 measures the 95th percentile over 1000 runs.

## Evidence contract

Each run stores command, revision, date, and exit status in `evidence/`.

## Exit criteria

Every test passes and its evidence is stored in `evidence/`.
