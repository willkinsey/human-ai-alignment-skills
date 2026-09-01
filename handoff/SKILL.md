---
name: handoff
description: Create a compact, evidence-backed handoff package directly in chat so a fresh AI task, agent, model, or future session can safely continue current work without rereading the full conversation. Use only when the user explicitly invokes `$handoff` or `/handoff`, asks to hand work off, wrap up for later, continue in a new task, save context before switching agents/models/devices, or requests a paste-ready continuation prompt. Create a file only when the user explicitly asks to save one. Do not use merely because a phase ended when the current task can continue normally.
---

# Handoff

Create a portable restart package, not a conversation summary. Preserve the outcome, current truth, load-bearing decisions, evidence, and one safe next move.

## Choose the Right Route

Use this only when work must move to another task, agent, model, device, directory, or person. If work can remain here, say so. A fork inherits task history; a fresh task does not. Ask which is wanted when unclear. A worktree is not a conversation handoff.

Prepare the package only. Do not create, fork, or message tasks; commit, push, or perform external work.

## Gather Only Grounded State

Read the conversation and only lightweight evidence needed for accuracy: relevant instructions, changed files, repository state, commits, validation, and named artifacts. Do not alter state or run broad checks.

Label material claims **Verified now**, **Reported, not rechecked**, or **Open / unknown**. Never convert an unverified claim into completion. Reference existing specifications, commits, runs, and outputs by absolute path, URL, or SHA instead of copying them.

## Preserve the Load-Bearing Decisions

Include accepted choices and material constraints; tempting rejected alternatives and why; unfinished work, blockers, and missing authority; completed and next validation; and relevant branch, worktree, draft, job, or browser state. Include only details that prevent rediscovery or a wrong next action.

## Create the Package in Chat

Return one complete, copyable Markdown block using [the exact template](references/handoff-template.md). Read that reference before writing. Omit empty optional sections. Suggest only available, directly useful skills.

Create a file only when explicitly asked to save, download, attach, preserve, or share it. Use a platform-appropriate temporary directory and name it `codex-handoff-YYYYMMDD-HHMM.md`; do not place it in the project or commit it.

Replace secrets, credentials, personal contacts, customer identifiers, and sensitive messages with `[REDACTED]`. State the minimum safe way to regain needed access.

## Finish Cleanly

Return the complete block, including its bootstrap prompt, plus one sentence naming the next task type: resume, fork, or fresh task. If a file was requested, include its exact path. Never imply a new task automatically receives this context.
