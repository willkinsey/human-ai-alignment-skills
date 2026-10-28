---
name: delegate-bounded-work
description: Delegate a clearly bounded task to an available AI subagent using a task-specific persona, objective, scope, context, authority, deliverable, and success criteria. Use when the user asks to delegate a bounded task that would benefit from a separate review, research, analysis, or implementation thread.
---

# Delegate Bounded Work

Remain the orchestrator: own framing, authority, quality, synthesis, and the final answer.

## Decide the Assignment

Delegate one independent, bounded task; split broad work first and never delegate mere repetition. Give the worker a task-specific persona and objective. For code, name file ownership, behavior, constraints, and validation. For review, name perspective, audience, purpose, criteria, and findings. For research, name the question, sources, freshness, citations, and evidence standard. Otherwise name the domain perspective, supported decision, and completed result.

## Explain the Launch

Before launch, show:

> Delegating a bounded task to a separate AI subagent.
>
> - **Persona:** <task-specific role and perspective>
> - **Objective:** <one concrete completion condition>
> - **Scope:** <included work and important exclusions>
> - **Returns:** <deliverable the subagent will return to the main session>

Populate all labels. A generic `subagent` or `assistant` is not a persona. Do not imply the user must manage it.

## Build the Launch Packet

Send every field below. Infer clear details; ask only when a missing choice materially changes outcome or authority.

```text
Persona: Task-specific role and perspective.
Objective: One concrete completion condition.
Scope: Included targets and explicit exclusions.
Context: Required facts, intent, audience, decisions, and evidence.
Authority: Read/write permission and prohibited actions.
Deliverable: Exact output, structure, detail, and artifact location.
Success Criteria: Required checks, evidence, citations, or validation.
Handoff: Outcome, evidence, changes, validation, risks/blockers, and next step.
```

Include material paths, IDs, URLs, and sources; exclude irrelevant conversation and secrets. Never launch with blank/generic fields or only `review`, `research`, or `fix this`.

## Launch the Subagent

Use an available subagent capability. Use limited/no inherited context when the packet and artifacts suffice; full context only when the conversation is material. Always state persona and objective. If delegation or the requested method is unavailable, report it and keep the task in the main session rather than silently substituting.

## Review the Handoff

Wait when its result is required. Check the handoff and material evidence against the packet; use a bounded follow-up when needed. Synthesize in the main session, distinguishing reported from directly verified facts. The main session remains accountable.

## Boundaries

- Invoking this skill never authorizes push, merge, deployment, external messages, destructive actions, or production/customer-data writes.
- Avoid overlapping writes with the main session or another worker.
- Do not let the subagent spawn additional agents unless the user explicitly authorizes that expansion.
