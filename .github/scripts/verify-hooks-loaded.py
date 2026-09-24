#!/usr/bin/env python3
"""Verify the static preconditions that let repository agent hooks load.

Checks every flat descriptor in `.github/hooks/*.json`: valid JSON, `version:
1`, known events, a supported handler type, a positive `timeoutSec`, and an
executable handler script for each `bash` command. It also rejects nested
`hooks.json` files that are never discovered and a `disableAllHooks` setting
in `.vscode/settings.json`. Static readiness is not proof that a hook ran;
confirm execution in the target harness (VS Code hooks output channel or a
Copilot CLI session log).

    python3 .github/scripts/verify-hooks-loaded.py [--require preToolUse ...]
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "hooks"
EVENTS = {
    "sessionStart", "sessionEnd", "userPromptSubmitted", "userPromptTransformed", "preToolUse",
    "postToolUse", "postToolUseFailure", "agentStop", "subagentStart", "subagentStop",
    "errorOccurred", "notification", "permissionRequest", "preCompact",
}
TYPES = {"command", "http", "prompt"}


def _check_handler(root: Path, where: str, event: str, handler: dict, reporter) -> None:
    kind = handler.get("type", "command")
    if kind not in TYPES:
        reporter.error(CHECK, where, None, f"{event}: handler type '{kind}' is not one of {sorted(TYPES)}")
    timeout = handler.get("timeoutSec")
    if timeout is not None and (not isinstance(timeout, (int, float)) or timeout <= 0):
        reporter.error(CHECK, where, None, f"{event}: timeoutSec must be a positive number")
    command = handler.get("bash")
    if kind == "command" and not (command or handler.get("powershell") or handler.get("command")):
        reporter.error(CHECK, where, None, f"{event}: command handler declares no bash, powershell, or command")
    if isinstance(command, str) and command.strip():
        script = shlex.split(command)[0]
        if "/" in script:
            path = root / (handler.get("cwd") or ".") / script
            if not path.is_file():
                reporter.error(CHECK, where, None, f"{event}: handler script {script} does not exist")
            elif not os.access(path, os.X_OK):
                reporter.error(CHECK, where, None, f"{event}: handler script {script} is not executable")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--require", action="append", default=[], help="event that must have a handler")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    root = sdd.repo_root()
    reporter = sdd.Reporter()
    hooks_dir = root / ".github/hooks"
    descriptors = sorted(hooks_dir.glob("*.json")) if hooks_dir.is_dir() else []
    for nested in sorted(hooks_dir.rglob("hooks.json")) if hooks_dir.is_dir() else []:
        if nested.parent != hooks_dir:
            reporter.error(CHECK, sdd.rel(root, nested), None, "nested hooks.json is never discovered; use a flat .github/hooks/<name>.json")
    seen_events: set[str] = set()
    for path in descriptors:
        where = sdd.rel(root, path)
        try:
            data = json.loads(sdd.read(path))
        except json.JSONDecodeError as exc:
            reporter.error(CHECK, where, None, f"invalid JSON: {exc}")
            continue
        if data.get("version") != 1:
            reporter.error(CHECK, where, None, "version must be 1")
        for event, handlers in (data.get("hooks") or {}).items():
            if event not in EVENTS:
                reporter.error(CHECK, where, None, f"unknown event '{event}'")
            seen_events.add(event)
            for handler in handlers if isinstance(handlers, list) else [handlers]:
                if isinstance(handler, dict):
                    _check_handler(root, where, event, handler, reporter)
    for event in args.require:
        if event not in seen_events:
            reporter.error(CHECK, ".github/hooks", None, f"no descriptor handles required event '{event}'")
    settings = root / ".vscode/settings.json"
    if settings.is_file():
        try:
            if json.loads(sdd.read(settings)).get("chat.hooks.disableAllHooks") or json.loads(sdd.read(settings)).get("disableAllHooks"):
                reporter.error(CHECK, sdd.rel(root, settings), None, "hooks are disabled by disableAllHooks")
        except json.JSONDecodeError:
            reporter.warning(CHECK, sdd.rel(root, settings), None, "settings.json has comments or invalid JSON; disableAllHooks not checked")
    if not descriptors:
        print("No hook descriptors in .github/hooks/; nothing to verify.")
    return reporter.emit(args.format, f"Hook readiness ({len(descriptors)} descriptor(s))")


if __name__ == "__main__":
    sys.exit(main())
