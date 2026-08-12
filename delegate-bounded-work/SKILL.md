---
name: delegate-bounded-work
description: Delegate a clearly bounded task to an available AI subagent using a task-specific persona, objective, scope, context, authority, deliverable, and success criteria. Use when the user asks to delegate a bounded task that would benefit from a separate review, research, analysis, or implementation thread.
---

# Delegate Bounded Work

Act as the orchestrator. Retain ownership of task framing, authority, quality control, synthesis, and the final user-facing answer. Treat the launch instructions as part of the work, not as clerical detail.

## Decide the Assignment

Delegate one concrete, bounded task that can be completed independently. Split a broad request before launching a subagent. Do not delegate merely to repeat the main session's work.

Choose the worker's task-specific persona and objective. Do not make the subagent infer them from a generic agent profile or inherited conversation.

Adapt the assignment to the work:

- **Coding:** name the engineering role, repository or files, file ownership, required behavior, constraints, and validation.
- **Business document review:** name the reviewer perspective, intended audience, document purpose, rating criteria or scale, and required findings.
- **Research:** name the research role, exact question, acceptable sources, freshness and citation requirements, and evidence standard.
- **Other work:** define the domain perspective, decision being supported, and what a useful completed result must contain.

## Explain the Launch

Before delegating, show the user this populated launch summary:

> Delegating a bounded task to a separate AI subagent.
>
> - **Persona:** <task-specific role and perspective>
> - **Objective:** <one concrete completion condition>
> - **Scope:** <included work and important exclusions>
> - **Returns:** <deliverable the subagent will return to the main session>

Populate and retain all four labels. `Subagent`, `assistant`, or another generic label is not a sufficient persona. Keep each value concise and do not imply that the user must manage the subagent task.

## Build the Launch Packet

The main session must supply every labeled field below in the task sent to the subagent. Infer clear details from the user's request and available evidence; ask only when a missing choice would materially change the outcome or authority.

```text
Persona: Who the subagent is for this task and the perspective or expertise it must apply.
Objective: One concrete outcome stated as a completion condition.
Scope: Included files, systems, sources, questions, or decisions; explicit exclusions.
Context: Task facts, user intent, audience, prior decisions, and evidence the subagent must know.
Authority: Read/write permissions and prohibited actions; preserve the user's existing boundaries.
Deliverable: Exact output, structure, level of detail, and where any artifact belongs.
Success Criteria: Checks, rubric, evidence, citations, or validation required before completion.
Handoff: Ask for outcome, evidence, changes, validation, risks or blockers, and next step.
```

Include exact artifact paths, task IDs, URLs, or source references when they matter. Keep irrelevant conversation and secrets out of the packet. Never send only a generic instruction such as `review this`, `research this`, or `fix this`.

Before launching, confirm that `Persona`, `Objective`, `Scope`, `Authority`, `Deliverable`, and `Success Criteria` are specific to the current task. Do not launch with a blank, generic, or implied value.

## Launch the Subagent

Use an available subagent capability and send the complete launch packet as its task. If subagent delegation is unavailable, say so and retain the task in the main session.

Choose inherited context deliberately:

- Use no or limited inherited context when the packet and named artifacts are sufficient.
- Use full inherited context only when the current conversation itself is material.
- Always state persona and objective explicitly, even when context is inherited.

Do not silently substitute a different capability if the requested delegation method is unavailable. Report the problem and retain the task in the main session.

## Review the Handoff

Wait for the subagent when its result is required for the user's request. Check the result against the launch packet and inspect material evidence before relying on it. Resolve gaps with a bounded follow-up to the same subagent when appropriate.

Present a synthesized answer in the main session. Distinguish what the subagent reported from what the main session directly verified. The main session remains accountable for correctness and scope.

## Boundaries

- Preserve the user's authority limits; invoking this skill does not authorize push, merge, deployment, external messages, destructive actions, or production or customer-data writes.
- Avoid overlapping writes with the main session or another worker.
- Do not let the subagent spawn additional agents unless the user explicitly authorizes that expansion.
