---
name: enhance-agent-prompt
description: Rewrite a human-written request into a lean, explicit, paste-ready prompt for an AI agent without changing the user's intent or authority. Use when the user asks to strengthen, clarify, or structure a prompt for an agent, or provides a rough new-task or follow-up prompt they plan to reuse.
---

# Enhance Agent Prompt

Turn the draft into a direct task contract. Edit the prompt only; do not perform its task.

## Preserve the Request

- Preserve outcome, reasoning, facts, identifiers, quantities, examples, priorities, and meaningful uncertainty.
- Preserve authority exactly: never turn review into implementation, a draft into a sent message, a local change into a push, or an idea into a decision.
- Remove filler and repetition, but keep context that explains material constraints.
- Never invent requirements, tools, files, deadlines, tests, evidence, or decisions, or weaken prohibitions.

## Build the Smallest Complete Contract

Use only fields the task needs:

1. **Objective:** one concrete completed outcome.
2. **Context:** facts and prior decisions needed to understand the request.
3. **Scope:** included work, exact targets when known, and material exclusions.
4. **Authority:** allowed actions and actions that still require approval.
5. **Execution:** required approach only when it affects the result.
6. **Deliverable:** the exact result, artifact, or decision the user expects.
7. **Success Criteria:** observable checks, evidence, or acceptance conditions.
8. **Handoff:** completion report, blockers, and unverified items.

Use Markdown labels only when helpful; omit empty ones. Convert vague verbs into observable work using details already present.

## Adapt to the Task

- **New task:** Make it self-contained.
- **Existing task:** Write a delta prompt using established context; do not reopen decisions or repeat work without cause.
- **Review, diagnosis, research, or planning:** Name the question, evidence standard, and return format without adding implementation authority.
- **Implementation:** Name the change, write scope, constraints, validation, and completion evidence supported by the request or project rules.
- **External, destructive, production, or persistent-data work:** State approval and stop boundaries; never infer permission.

For harmless gaps, use established conventions. For material gaps, direct the agent to inspect context and ask one focused question only if unresolved.

## Keep It Lean

Do not add generic advice, token budgets, model settings, subagents, tools, research, commits, workflow stages, model comparisons, or XML unless requested or required by supplied context.

## Return the Result

Return only the paste-ready prompt unless the user requests critique or alternatives.

If no substantive draft exists, ask for it. If a material contradiction cannot be preserved safely, ask one concise question.

Verify one clear outcome, preserved authority, enough context, a defined deliverable and completion proof, no guessed material choice, and no added work.
