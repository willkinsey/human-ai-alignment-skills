---
name: independent-task-review
description: Independently review another Codex task by task or session ID before implementation, after completed development work, or after remediation. Use for a skeptical second set of eyes, go/no-go decision, durable-fix assessment, or final double-check. Return the verdict to the user and require explicit approval before messaging or authorizing the reviewed task.
---

# Independent Task Review

Act as an independent reviewer, not the implementer. Treat the referenced task's
claims as evidence to verify. Keep the review proportional to the user's actual
objective; do not turn a targeted task into a broader audit or redesign.

## Review Manually

Require a task or session ID and read enough history and repository evidence to
establish the request, intended approach, claimed work, validation, and current
stop point. Classify it as a plan gate, completed-work audit, or re-check.

Every review starts read-only. Do not edit, commit, push, publish, restart,
migrate, message the reviewed task, or instruct it to act. A task reference,
favorable verdict, or planned next step is not authorization to contact it.

Read [review-standards.md](references/review-standards.md) for evidence, scope,
proportional validation, and finding rules. Read
[verdict-and-output.md](references/verdict-and-output.md) before returning the
decision. Name verified facts, material validation gaps, and only concrete
blocking findings or useful non-blocking notes. A clean review with no requested
changes is successful.

## Internal Benchmark Capture

For every reviewed task or session, read
[benchmark-observation.md](references/benchmark-observation.md) before
assessing the internal benchmark dimensions. It applies to plan gates,
completed-work audits, and re-checks, regardless of task family. Retain the
manual, read-only boundary and require the reviewed task or session ID needed
to join telemetry.

- Do not include the structured benchmark record, a **Benchmark Record**
  section, or raw benchmark fields in the user-facing response unless the user
  explicitly asks to see them. Use the dimensions as an internal checklist.
  If no authorized benchmark capture mechanism is available, do not create a
  file, database entry, or other artifact merely to preserve the record.
- Record only facts supported by task history, artifacts, browser/computer
  evidence, or an explicit monitor join.
- For a plan-gate review, record plan estimates and plan quality only. Mark
  execution, outcome, intervention, and persistence results as
  `not_observed_plan_only` or `null`; do not imply that implementation,
  saving, reopening, or verification occurred.
- For a completed-work audit or re-check, capture requested-outcome status,
  verification strength, first-pass and intervention outcomes, retries,
  recoveries, rework, and ordered issue findings only when auditable. Do not
  substitute plan estimates for observed execution.
- Use the generic controlled `task_family` and `interaction_mode` dimensions
  plus privacy-safe optional tags. Keep the benchmark ID opaque and stable
  across plan, builder, and review; never encode customer, report, workspace,
  model, source, or business labels in benchmark identifiers or labels.
- Usage and timing values are telemetry joins, not reviewer guesses. If they
  are unavailable, use the reference's `join from monitor` status and leave the
  values null. The record supplements the monitor; it does not write SQLite
  rows, the local telemetry database, or source/customer data.
- Use the generic issue taxonomy and ordinal severity. Benchmark severity is
  independent from the review verdict and from blocking versus non-blocking
  finding categories. Do not manufacture an issue merely because a field is
  unavailable.

When the reviewed task is Power BI, also read
[power-bi-benchmark-observation.md](references/power-bi-benchmark-observation.md).
Put its UI, state-transition, persistence, recovery, routing, and root-cause
details inside the same generic record's `domain_metrics.power_bi` and
`domain_metrics.computer_use`; never append a second Power BI record.

## Wait for the User Before Handoff

Return the verdict in the reviewer task and wait. Only after the user explicitly
says to message, authorize, or send feedback to the reviewed task may the
reviewer perform a user-approved handoff. Then read
[managed-auto-approval.md](references/managed-auto-approval.md) and
[handoff-templates.md](references/handoff-templates.md), and send only the
bounded action the user approved.

Handoff approval does not authorize push, deployment, release, migration,
customer or production data writes, destructive work, secrets, permission or
billing changes, or other material scope expansion unless the user's approval names
that exact action. Only the worker edits its working copy; never have reviewer
and worker edit it concurrently.

## Invocation Examples

- `Use $independent-task-review to review task ID 019f... before implementation.`
- `Use $independent-task-review to double-check completed work in task ID 019f....`
- `Re-check task ID 019f... after it addressed your findings.`
