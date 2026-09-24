#!/usr/bin/env python3
"""Validate tasks.md as an executable, test-first dependency graph.

Checks unique task IDs, dependencies that exist and form no cycle, Mermaid
edges that name real tasks, every task tracing a requirement, RED before GREEN
for each requirement when TDD applies, `[P]` tasks that do not depend on each
other, and checked tasks that appear in the verification-sweep ledger.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sdd_lib as sdd  # noqa: E402

CHECK = "task-graph"


def _cycle(graph: dict[str, set[str]]) -> list[str] | None:
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node: str) -> list[str] | None:
        state[node] = 1
        stack.append(node)
        for dep in sorted(graph.get(node, ())):
            if state.get(dep) == 1:
                return stack[stack.index(dep):] + [dep]
            if dep not in state:
                found = visit(dep)
                if found:
                    return found
        stack.pop()
        state[node] = 2
        return None

    for node in sorted(graph):
        if node not in state:
            found = visit(node)
            if found:
                return found
    return None


def _ancestors(graph: dict[str, set[str]], node: str) -> set[str]:
    seen, todo = set(), list(graph.get(node, ()))
    while todo:
        current = todo.pop()
        if current not in seen:
            seen.add(current)
            todo.extend(graph.get(current, ()))
    return seen


def tdd_applies(config: dict, tasks: list) -> bool:
    if config["tdd"] == "required":
        return True
    if config["tdd"] == "off":
        return False
    return any(t.phase for t in tasks)


def check(root, config, sroot, pkgs, reporter, args=None) -> None:
    for pkg in pkgs:
        path = pkg.role("tasks")
        if not path or not path.is_file():
            continue
        where = sdd.rel(root, path)
        tasks, ledger, edges = sdd.parse_tasks(sdd.read(path), config)
        if not tasks:
            reporter.error(CHECK, where, None,
                           "no checkbox tasks (- [ ] T001 ...) found")
            continue
        ids: dict[str, int] = {}
        for task in tasks:
            if task.id in ids:
                reporter.error(
                    CHECK, where, task.line, f"{task.id} is duplicated (first at line {ids[task.id]})")
            ids.setdefault(task.id, task.line)
        graph = {t.id: set(t.depends) for t in tasks}
        for before, after in edges:
            for node in (before, after):
                if node not in ids:
                    reporter.error(
                        CHECK, where, None, f"dependency graph names unknown task {node}")
            graph.setdefault(after, set()).add(before)
        if edges:
            drawn = {n for e in edges for n in e}
            missing = sorted(set(ids) - drawn)
            if missing and len(ids) > 1:
                reporter.warning(
                    CHECK, where, None, "tasks absent from the dependency graph: " + ", ".join(missing))
        for task in tasks:
            for dep in sorted(task.depends - set(ids)):
                reporter.error(CHECK, where, task.line,
                               f"{task.id} depends on unknown task {dep}")
            if not task.traces:
                reporter.error(CHECK, where, task.line,
                               f"{task.id} traces no requirement ID")
            if task.checked and task.id not in ledger:
                reporter.error(CHECK, where, task.line,
                               f"{task.id} is checked but missing from the 'Marked complete by verification sweep:' ledger")
        for tid in sorted(ledger - set(ids)):
            reporter.error(CHECK, where, None,
                           f"ledger names unknown task {tid}")
        for tid in sorted(ledger):
            task = next((t for t in tasks if t.id == tid), None)
            if task and not task.checked:
                reporter.error(CHECK, where, task.line,
                               f"{tid} is in the ledger but unchecked")
        cycle = _cycle(graph)
        if cycle:
            reporter.error(CHECK, where, None,
                           "dependency cycle: " + " -> ".join(cycle))
            continue
        by_id = {t.id: t for t in tasks}
        for task in tasks:
            if task.parallel:
                for other in sorted(graph.get(task.id, ())):
                    if other in by_id and by_id[other].parallel:
                        reporter.error(
                            CHECK, where, task.line, f"{task.id} is [P] but depends directly on [P] task {other}")
        if tdd_applies(config, tasks):
            order = {t.id: i for i, t in enumerate(tasks)}
            for task in tasks:
                if task.phase != "GREEN":
                    continue
                for rid in sorted(task.traces):
                    reds = [t for t in tasks if t.phase ==
                            "RED" and rid in t.traces]
                    if not reds:
                        reporter.error(
                            CHECK, where, task.line, f"{task.id} is GREEN for {rid} with no RED task")
                    elif not any(order[r.id] < order[task.id] or r.id in _ancestors(graph, task.id) for r in reds):
                        reporter.error(
                            CHECK, where, task.line, f"{task.id} GREEN for {rid} precedes its RED task")


if __name__ == "__main__":
    sdd.run_main(check, "Task graph and TDD ordering.")
