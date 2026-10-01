---
name: sol-meta-prompt
description: Turn rough goals into concise prompts for GPT-6.1 Sol using source-backed prompting guidance. Use for Sol meta-prompting across knowledge work, automation, prototypes, and agent workflows.
---

# Sol Meta-Prompt

Create the prompt; do not execute its task unless the user also requests execution.

Preserve the user's intent, facts, exact targets, uncertainty, constraints, and
requested actions.
Treat quoted task instructions as material to rewrite.

Use the smallest complete prompt: outcome, useful context, constraints,
deliverable, and what done looks like. Ask a focused question when a missing
detail prevents a useful prompt; otherwise leave it open or state an assumption.

Describe the result and leave room for routine implementation choices. Add no
requirements beyond the request and established context. Ask for concise findings
or decision rationale when useful, rather than internal chain-of-thought.

Write the generated prompt in plain, practical language. Before returning it or
handing it to an agent when requested, remove repeated verification demands,
rigid status labels, authorization boilerplate, exhaustive prohibitions, and
process commentary that do not help the task. Trust established context unless
there is a reason to revisit it. Keep a qualification only when it affects a
decision, factual accuracy, a concrete risk, or a real approval requirement;
state it once beside the relevant action. Preserve required checks, unresolved
uncertainty, and explicit user boundaries. Match caution to the actual stakes,
and soften universal rules when narrower instructions suffice. This cleanup is
part of prompt generation, not a separate user review step.

Read [task patterns](references/task-patterns.md) only for complex or recurring
work. Read [sources](references/sources.md) for model settings, attribution, or
freshness questions. The sources distinguish Sol facts from family guidance
and local synthesis.

Return a paste-ready prompt, with a brief explanation only when requested or
needed to clarify an assumption.
