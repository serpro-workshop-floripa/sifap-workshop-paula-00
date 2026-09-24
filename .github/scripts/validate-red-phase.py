#!/usr/bin/env python3
"""Prove the RED step of test-driven development for any test runner.

    python3 .github/scripts/validate-red-phase.py -- <test command...>
    python3 .github/scripts/validate-red-phase.py --expect-output "DOC-01" -- npm test -- sample

Passes only when the command exits with a test-failure code (not 0 and not a
runner error such as "no tests collected" or a usage error) and, optionally,
its output matches --expect-output. Record the command and result in the
task's evidence before the GREEN task starts.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

# pytest: 2 interrupted, 3 internal error, 4 usage error, 5 no tests collected.
DEFAULT_RUNNER_ERRORS = "2,3,4,5,126,127"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--runner-errors", default=DEFAULT_RUNNER_ERRORS,
                        help="comma-separated exit codes that mean the runner failed, not the test")
    parser.add_argument("--expect-output", help="regular expression the failing output must contain")
    parser.add_argument("command", nargs=argparse.REMAINDER, help="test command after --")
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("give the targeted test command after --")
    result = subprocess.run(command, cwd=sdd.repo_root(), capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    sys.stdout.write(output[-4000:])
    runner_errors = {int(code) for code in args.runner_errors.split(",") if code.strip()}
    if result.returncode == 0:
        print("RED validation failed: the tests passed, so they do not prove the missing behavior", file=sys.stderr)
        return 1
    if result.returncode in runner_errors:
        print(f"RED validation failed: exit {result.returncode} is a runner error, not a test failure", file=sys.stderr)
        return 1
    if args.expect_output and not re.search(args.expect_output, output):
        print(f"RED validation failed: output does not match {args.expect_output!r}", file=sys.stderr)
        return 1
    print(f"RED validation passed: targeted tests failed as expected (exit {result.returncode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
