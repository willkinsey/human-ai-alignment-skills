---
name: enhance-agent-prompt
description: Rewrite a human-written request into a lean, explicit, paste-ready prompt for an AI agent without changing the user's intent or authority. Use when the user asks to strengthen, clarify, or structure a prompt for an agent, or provides a rough new-task or follow-up prompt they plan to reuse.
---

# Enhance Agent Prompt

Turn the user's draft into a direct task contract an agent can execute without guessing. Perform prompt editing only; do not carry out the underlying task.

## Preserve the Request

- Preserve the intended outcome, reasoning, facts, names, paths, URLs, IDs, quantities, examples, priorities, and meaningful uncertainty.
- Preserve authority limits exactly. Never turn review into implementation, a draft into a sent message, a local change into a push, or a tentative idea into a settled decision.
- Remove filler and accidental repetition, but keep context that explains why a constraint or preference matters.
- Do not invent requirements, tools, files, branches, deadlines, tests, evidence, or user decisions.
- Do not weaken explicit prohibitions such as `do not send`, `do not push`, `read-only`, or `draft-only`.

## Build the Smallest Complete Contract

Identify and make explicit only the fields the task needs:

1. **Objective:** one concrete completed outcome.
2. **Context:** facts and prior decisions needed to understand the request.
3. **Scope:** included work, exact targets when known, and material exclusions.
4. **Authority:** allowed actions and actions that still require approval.
5. **Execution:** the required approach or sequence only when it affects the result.
6. **Deliverable:** the exact result, artifact, or decision the user expects.
7. **Success Criteria:** observable checks, evidence, or acceptance conditions.
8. **Handoff:** what the agent should report when finished, including blockers or unverified items.

Use plain Markdown labels when they improve clarity. Omit labels that would be empty or redundant. State each instruction once.

Convert vague verbs into observable work while preserving the requested action level. For example, replace `look into this` with the specific inspection and report expected, and replace `make it better` with the named behavior, audience need, or acceptance condition present in the user's draft.

## Adapt to the Task

- **New task:** Make the prompt self-contained enough to start in a fresh agent task.
- **Existing agent task:** Write a delta prompt. Start from the context and decisions already established in that task, state the new direction precisely, and tell the agent not to reopen settled decisions or repeat completed work unless verification requires it.
- **Review, diagnosis, research, or planning:** Name the question, evidence standard, and return format. Do not add implementation authority.
- **Implementation:** Name the requested change, write scope, constraints, validation, and completion evidence that the user's request or established project rules support.
- **External, destructive, production, or persistent-data work:** State the approval boundary and stop condition explicitly. Never infer permission.

If a harmless detail is missing, direct the agent to use the established project convention. If a missing choice would materially change the outcome or authority, tell the agent to inspect available context first and ask one focused question only if it cannot resolve the choice safely. Do not fabricate an answer merely to make the prompt look complete.

## Keep It Lean

- Prefer a compact explicit contract over a long explanation.
- Do not add generic instructions such as `think step by step`, `be thorough`, or `use best practices`.
- Do not add token budgets, model settings, subagents, tools, research, commits, or workflow stages unless the user requested them or supplied context requires them.
- Do not compare models inside the rewritten prompt.
- Avoid XML unless the user's original workflow already depends on XML.

## Return the Result

Return only the finished, paste-ready prompt. Do not include a critique, score, explanation, or a second version unless the user asks for it.

If the user has not supplied a draft or a substantive request to transform, ask them to paste it. If the draft contains a material contradiction that cannot be preserved safely, ask one concise question instead of silently choosing a side.

Before returning, verify that the prompt:

- states one clear outcome;
- preserves the user's action level and approval boundaries;
- contains enough context for a new task or a precise delta for an existing task;
- defines the expected deliverable and useful proof of completion;
- handles material ambiguity without guessing; and
- adds no work the user did not request.
