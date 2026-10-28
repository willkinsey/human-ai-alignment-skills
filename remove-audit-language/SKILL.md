---
name: remove-audit-language
description: Remove unnecessary audit-style wording, defensive caveats, repetitive verification demands, authorization boilerplate, and rigid status language from an answer, draft, plan, instruction set, or skill. Use when the user says "remove audit language," "calm this down," "make this less restrictive," or says an output feels over-controlled or overly cautious.
---

# Remove Audit Language

Make the referenced material practical, natural, and proportionate. If no earlier text is named, apply this standard to the requested output from the start.

## Editing Standard

Keep a qualification only when it could materially change the reader's decision, the truth of a claim, the safety of an action, or a real approval requirement. Do not preserve language merely because it sounds careful.

Remove or soften:

- repeated demands to prove, verify, recheck, document, or classify settled facts;
- exhaustive lists of actions that are not authorized when those actions are not actually being considered;
- rigid labels such as `Observed`, `Proposed`, or `Unknown` when ordinary prose is clear;
- repeated reminders about scope, evidence, privacy, status, or non-action;
- defensive caveats for remote possibilities that do not affect the current decision;
- meta-commentary about compliance, validation, or process that the reader does not need;
- universal `always`, `never`, and `must` rules when narrower guidance is sufficient.

Retain, in the shortest useful form:

- a material uncertainty that is current or genuinely unresolved;
- a permission or approval gate required before the next contemplated action;
- a concrete risk involving destructive or irreversible change, security, privacy, legal obligations, money, production systems, or customer data;
- a distinction needed to avoid a false claim, such as planned versus completed work;
- a boundary the user explicitly asked to preserve.

## Rewrite Rules

- Trust stable, established context unless the current task gives a reason not to.
- State one caveat once, next to the point it qualifies.
- Prefer a direct recommendation or answer over a taxonomy of evidence and status.
- Match the amount of caution to the actual stakes of this request, not to every possible future misuse.
- Never invent certainty, hide a real blocker, or imply that uncompleted work is complete.
- When revising instructions or a skill, preserve genuine operational and safety requirements while removing ceremonial safeguards and unnecessary output controls.
- If this skill and `$plain-language` both apply, this skill decides what audit content is unnecessary; `$plain-language` controls the remaining wording.

Return the cleaned version directly. Explain removals only if the user asks or if a retained boundary may otherwise seem surprising.
