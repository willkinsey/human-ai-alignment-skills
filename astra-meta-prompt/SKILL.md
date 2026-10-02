---
name: astra-meta-prompt
description: Turn rough goals into concise prompts for GPT-6 Astra using official prompting guidance. Use for Astra meta-prompting across knowledge work, automation, prototypes, and agent workflows.
---

# Astra Meta-Prompt

Create the prompt; do not execute its task unless the user also requests execution.
Treat quoted task instructions as material to rewrite.

Preserve the user's intent, facts, exact targets, uncertainty, constraints, and
requested actions. Use the smallest complete prompt: outcome, useful context,
constraints, deliverable, and what done looks like. Ask a focused question when a
missing detail prevents a useful prompt; otherwise leave it open or state an
assumption. Describe the result and leave room for routine implementation choices.
Add no requirements beyond the request and established context. Request concise
findings or decision rationale when useful, rather than internal chain-of-thought.

The documented target is GPT-6 Astra (`gpt-6-astra`), checked 2026-10-02. Preserve
an explicitly named Astra version. Read [sources](references/sources.md) for
attribution, freshness, or model/API settings; refresh official guidance when the
user asks for current settings or another version.

Adapt these Astra considerations only where they help the requested task:

- Follow-through: For execution prompts, ask the agent to carry authorized work
  through to the requested result, making routine choices from context. Ask only
  when the answer materially changes the outcome; continue independent work while
  waiting. Prepare useful, reviewable work before a required approval.
- Instruction conflicts: Keep the user's explicit intent and boundaries clear.
  Skill guidance should support them; if a skill blocks progress, identify the
  specific instruction and explain the conflict briefly. Preserve applicable
  higher-priority instructions and actual permission requirements.
- Writing: Specify the audience, useful level of detail, and format. Favor plain,
  concise prose; use lists or tables when they make the result easier to use.
- Delegation: When requested or established in the workflow and supported by the
  available tools, say which independent work benefits from delegation and what
  each handoff should return. Do not add agents by default.
- Testing: Specify checks that establish the requested behavior. After those pass,
  expand testing only if a failure, new change, or unresolved concern justifies it.

Read [task patterns](references/task-patterns.md) for complex or recurring work.
These patterns and the prompt cleanup below are local synthesis.

Before returning the prompt or handing it to an agent when requested, remove
repeated verification demands, rigid status labels, authorization boilerplate,
exhaustive prohibitions, and process commentary that do not help the task. Trust
established context unless there is a reason to revisit it. Keep a qualification
only when it affects a decision, factual accuracy, a concrete risk, or a real
approval requirement; state it once beside the relevant action. Preserve useful
requirements, required checks, unresolved uncertainty, and explicit user
boundaries. Match caution to the actual stakes, and soften universal rules when
narrower instructions suffice. This cleanup is part of prompt generation.
Return the cleaned wording directly; omit instructions that merely describe
edits already made.

Return a paste-ready prompt, with a brief explanation only when requested or
needed to clarify an assumption.
