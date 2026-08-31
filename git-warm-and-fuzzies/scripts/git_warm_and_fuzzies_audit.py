#!/usr/bin/env python3
"""Print a compact, deterministic, read-only Git state audit.

The script reports repository metadata and names/statuses only. It does not
read file contents, contact remotes, or mutate the index, refs, worktrees, or
working tree.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Iterable, Optional


MAX_RECENT_COMMITS = 5
MAX_BRANCH_ONLY_COMMITS = 20
COMMAND_TIMEOUT_SECONDS = 10


def display(value: object) -> str:
    """Quote a value so paths and ref names cannot change output structure."""

    return json.dumps(str(value), ensure_ascii=True, separators=(",", ":"))


def text_output(raw: bytes) -> str:
    return raw.decode("utf-8", errors="surrogateescape")


def git_command(cwd: Path, args: list[str]) -> tuple[int, bytes, bytes]:
    env = os.environ.copy()
    env.update(
        {
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_PAGER": "cat",
            "PAGER": "cat",
            "GIT_TERMINAL_PROMPT": "0",
            "LC_ALL": "C",
        }
    )
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=os.fspath(cwd),
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        # Do not expose stderr, which can contain arbitrary path or config data.
        return 125, b"", str(exc).encode("utf-8", errors="replace")
    return result.returncode, result.stdout, result.stderr


def first_line(raw: bytes) -> str:
    return text_output(raw).splitlines()[0].strip() if raw else ""


def value_or_none(cwd: Path, args: list[str]) -> Optional[str]:
    code, stdout, _ = git_command(cwd, args)
    value = first_line(stdout)
    return value if code == 0 and value else None


def print_error(label: str, code: int) -> None:
    print(f"NOTE\t{label}\tcommand_status={code}")


def parse_status(raw: bytes) -> list[tuple[str, str, Optional[str]]]:
    """Parse porcelain-v1 -z records as (XY, path, related_path)."""

    fields = raw.split(b"\0")
    entries: list[tuple[str, str, Optional[str]]] = []
    index = 0
    while index < len(fields):
        field = fields[index]
        index += 1
        if not field:
            continue
        if len(field) < 3 or field[2:3] != b" ":
            # Keep an unexpected record visible without attempting to parse it.
            entries.append(("??", text_output(field), None))
            continue
        code = text_output(field[:2])
        path = text_output(field[3:])
        related: Optional[str] = None
        if "R" in code or "C" in code:
            if index < len(fields) and fields[index]:
                related = text_output(fields[index])
                index += 1
        entries.append((code, path, related))
    return entries


def status_counts(entries: Iterable[tuple[str, str, Optional[str]]]) -> tuple[int, int, int, int]:
    staged = unstaged = untracked = conflicts = 0
    conflict_codes = {"DD", "AU", "UD", "UA", "DU", "AA", "UU"}
    for code, _, _ in entries:
        if code == "??":
            untracked += 1
            continue
        if code and code[0] not in {" ", "?"}:
            staged += 1
        if len(code) > 1 and code[1] not in {" ", "?"}:
            unstaged += 1
        if code in conflict_codes or "U" in code:
            conflicts += 1
    return staged, unstaged, untracked, conflicts


def parse_branches(raw: bytes) -> list[tuple[str, str]]:
    branches: list[tuple[str, str]] = []
    for line in text_output(raw).splitlines():
        if "\t" not in line:
            continue
        name, sha = line.split("\t", 1)
        if name:
            branches.append((name, sha))
    return branches


def relation(cwd: Path, other_ref: str, current_ref: str) -> Optional[tuple[int, int]]:
    code, stdout, _ = git_command(
        cwd, ["rev-list", "--left-right", "--count", f"{other_ref}...{current_ref}"]
    )
    if code != 0:
        return None
    parts = first_line(stdout).split()
    if len(parts) != 2:
        return None
    try:
        other_only, current_only = (int(parts[0]), int(parts[1]))
    except ValueError:
        return None
    return other_only, current_only


def branch_only(cwd: Path, base_ref: str) -> tuple[Optional[int], list[str]]:
    code, stdout, _ = git_command(cwd, ["rev-list", "--count", f"{base_ref}..HEAD"])
    if code != 0:
        return None, []
    try:
        count = int(first_line(stdout))
    except ValueError:
        return None, []
    code, stdout, _ = git_command(
        cwd,
        [
            "log",
            f"--max-count={MAX_BRANCH_ONLY_COMMITS}",
            "--date=iso-strict",
            "--format=%h%x09%ad%x09%s",
            f"{base_ref}..HEAD",
        ],
    )
    if code != 0:
        return count, []
    return count, [line.replace("\t", " ", 2) for line in text_output(stdout).splitlines()]


def parse_worktrees(raw: bytes) -> list[tuple[str, str, str]]:
    records: list[tuple[str, str, str]] = []
    current: dict[str, str] = {}
    for line in text_output(raw).splitlines() + [""]:
        if line == "":
            if "worktree" in current:
                records.append(
                    (
                        current["worktree"],
                        current.get("HEAD", "UNBORN"),
                        current.get("branch", "DETACHED"),
                    )
                )
            current = {}
            continue
        key, separator, value = line.partition(" ")
        if separator:
            current[key] = value
    return records


def audit(target: Path) -> int:
    target = target.expanduser().resolve(strict=False)
    code, stdout, _ = git_command(target, ["rev-parse", "--show-toplevel"])
    if code != 0:
        print("git-warm-and-fuzzies audit v1")
        print(f"TARGET\t{display(target)}")
        print("RESULT\tNOT_A_REPOSITORY")
        return 0

    root = Path(first_line(stdout)).resolve(strict=False)
    inside = value_or_none(target, ["rev-parse", "--is-inside-work-tree"])
    common = value_or_none(target, ["rev-parse", "--git-common-dir"])
    if common:
        common_path = Path(common)
        if not common_path.is_absolute():
            common_path = root / common_path
        common = str(common_path.resolve(strict=False))

    print("git-warm-and-fuzzies audit v1")
    print(f"TARGET\t{display(target)}")
    print(f"REPOSITORY\t{display(root)}")
    print(f"GIT_COMMON_DIR\t{display(common or 'UNKNOWN')}")
    print(f"IS_WORK_TREE\t{display(inside or 'UNKNOWN')}")
    if inside != "true":
        print("RESULT\tNOT_A_WORK_TREE")
        return 0

    head = value_or_none(root, ["rev-parse", "--verify", "HEAD"]) or "UNBORN"
    branch = value_or_none(root, ["symbolic-ref", "--quiet", "--short", "HEAD"])
    detached = branch is None
    branch_label = branch or "(detached)"
    upstream = value_or_none(root, ["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"])
    ahead = behind = "UNKNOWN"
    if upstream:
        code, stdout, _ = git_command(root, ["rev-list", "--left-right", "--count", "HEAD...@{upstream}"])
        parts = first_line(stdout).split()
        if code == 0 and len(parts) == 2:
            ahead, behind = parts

    print(f"HEAD\t{display(head)}")
    print(f"BRANCH\t{display(branch_label)}")
    print(f"DETACHED\t{'true' if detached else 'false'}")
    print(f"UPSTREAM\t{display(upstream or 'NONE')}")
    print(f"AHEAD\t{ahead}")
    print(f"BEHIND\t{behind}")

    code, stdout, _ = git_command(root, ["status", "--porcelain=v1", "-z", "--untracked-files=all"])
    entries = parse_status(stdout) if code == 0 else []
    if code != 0:
        print_error("status", code)
    staged, unstaged, untracked, conflicts = status_counts(entries)
    print(f"WORKTREE\t{display('NO_STATUS_ENTRIES' if not entries else 'ENTRIES_PRESENT')}")
    print(f"CHANGES\tstaged={staged}\tunstaged={unstaged}\tuntracked={untracked}\tconflicts={conflicts}")
    for status, path, related in entries:
        if related is None:
            print(f"ITEM\t{display(status)}\t{display(path)}")
        else:
            print(f"ITEM\t{display(status)}\t{display(path)}\tRELATED={display(related)}")

    code, stdout, _ = git_command(
        root,
        [
            "log",
            f"--max-count={MAX_RECENT_COMMITS}",
            "--date=iso-strict",
            "--format=%h%x09%ad%x09%s",
            "HEAD",
        ],
    )
    print("RECENT_COMMITS")
    if code == 0:
        for line in text_output(stdout).splitlines():
            print(f"COMMIT\t{line.replace(chr(9), ' ', 2)}")
    elif head != "UNBORN":
        print_error("recent_commits", code)

    code, stdout, _ = git_command(
        root,
        ["for-each-ref", "--sort=refname", "--format=%(refname:short)%09%(objectname)", "refs/heads"],
    )
    branches = parse_branches(stdout) if code == 0 else []
    print("LOCAL_BRANCHES")
    for name, sha in branches:
        print(f"BRANCH_REF\t{display(name)}\t{display(sha)}")
    if code != 0:
        print_error("local_branches", code)

    current_ref = f"refs/heads/{branch}" if branch else "HEAD"
    print("BRANCH_RELATIONS")
    if head == "UNBORN":
        print("BRANCH_RELATION_NOTE\tno_committed_HEAD")
    else:
        for name, _ in branches:
            if name == branch:
                continue
            result = relation(root, f"refs/heads/{name}", current_ref)
            if result is None:
                print(f"BRANCH_RELATION\t{display(name)}\tUNAVAILABLE")
            else:
                other_only, current_only = result
                print(f"BRANCH_RELATION\t{display(name)}\tother_only={other_only}\tcurrent_only={current_only}")

    print("BRANCH_ONLY")
    if upstream:
        count, commits = branch_only(root, "@{upstream}")
        if count is None:
            print(f"BRANCH_ONLY_BASE\t{display(upstream)}\tUNAVAILABLE")
        else:
            print(f"BRANCH_ONLY_BASE\t{display(upstream)}\tcount={count}")
            for line in commits:
                print(f"ONLY_COMMIT\t{line}")
            if count > len(commits):
                print(f"ONLY_COMMIT_NOTE\tomitted={count - len(commits)}")
    else:
        print("BRANCH_ONLY_BASE\tNONE\tcompare_BRANCH_RELATIONS_before_assigning_a_base")

    code, stdout, _ = git_command(root, ["worktree", "list", "--porcelain"])
    worktrees = parse_worktrees(stdout) if code == 0 else []
    print("WORKTREES")
    for path, worktree_head, worktree_branch in worktrees:
        print(
            f"WORKTREE_ENTRY\tpath={display(path)}\thead={display(worktree_head)}\tbranch={display(worktree_branch)}"
        )
    if code != 0:
        print_error("worktrees", code)

    code, stdout, _ = git_command(
        root,
        ["stash", "list", "--date=iso-strict", "--format=%gd%x09%h%x09%cd%x09%s"],
    )
    print("STASHES")
    if code == 0:
        stash_lines = text_output(stdout).splitlines()
        print(f"STASH_COUNT\t{len(stash_lines)}")
        for line in stash_lines:
            print(f"STASH\t{line.replace(chr(9), ' ', 3)}")
    else:
        print_error("stashes", code)

    print("RESULT\tAUDIT_COMPLETE")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read-only compact Git confidence audit")
    parser.add_argument("path", nargs="?", default=".", help="repository or subdirectory to inspect (default: current folder)")
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(audit(Path(parse_args().path)))
