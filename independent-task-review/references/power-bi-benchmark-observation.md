# Power BI Benchmark Extension

Read this reference only when the reviewed task is a Power BI task, including
a Power BI planning gate, browser build audit, or re-check. Read
[Generic Benchmark Observation](benchmark-observation.md) first. This document adds Power BI detail to the
generic record; it never creates a second benchmark record, changes a verdict,
authorizes browser control, or permits worker contact or database writes.

## Applicability and One-Record Rule

Classify a browser build as `task_family: power_bi` and
`interaction_mode: browser_computer_use` (or `mixed` when the task also uses
another mode). Power BI and browser/computer use are independent dimensions,
so retain both concepts in the same generic record. Keep exact report,
workspace, semantic-model, source, customer, and private URL details in the
human review only when needed and authorized; never put them in
`benchmark_id`, tags, or benchmark labels.

Use the reviewed task or session ID as `task_or_session_id`. Carry forward the
plan's stable opaque `benchmark_id`; if none exists, generate one without
customer, report, workspace, model, source, or business labels. Record builder
model, reasoning effort, and usage only when directly available. Do not infer
them from a route hypothesis or the reviewer's model.

## Plan Gates Versus Executed Reviews

For a `plan_gate`, carry the plan's action and meaningful state-transition
estimates in the generic `planned_*` fields and, where useful, in
`domain_metrics.power_bi.plan_estimates`. Set execution, completion,
intervention, retry/recovery, and Save/Apply/reopen/Reading-view fields to
`not_observed_plan_only` or `null`. Assess the plan, but never claim that a
report was edited, saved, reopened, or verified.

For a `completed_work_audit` or `recheck`, record observed execution only from
auditable task history, artifacts, browser/computer evidence, or a monitor
join. Never replace missing observations with plan estimates. Set
`observation_basis` to describe a partial trace when the full run is not
available. The generic top-level fields carry outcomes, evidence strength,
intervention, retries, recoveries, rework, usage joins, and issue counts.

## Action and State-Transition Capture

Use the generic planned fields for Power BI estimates:

- `planned_actions_minimum`, `planned_actions_expected`,
  `planned_actions_risk_low`, and `planned_actions_risk_high`;
- `planned_transitions_minimum`, `planned_transitions_expected`,
  `planned_transitions_risk_low`, and `planned_transitions_risk_high`;
- `recovery_allowance_actions`, `recovery_allowance_transitions`, and
  `estimate_confidence`.

Count each auditable atomic operator input separately from each meaningful
application/browser state transition. Passive waiting, rendering, and a
tool's internal retry do not become planned actions. Put the observed totals in
`observed_actions` and `observed_transitions` only when the trace supports
them. If only a partial trace is available, leave uncertain totals null and
state the boundary.

Within `domain_metrics.computer_use`, include only evidenced values for:

- `planned_atomic_ui_actions` and `observed_atomic_ui_actions`;
- `planned_state_transitions` and `observed_state_transitions`;
- `incorrect_target_count` for wrong visual, page, pane, or artifact targets;
- `repeated_navigation_count` for a navigation repeated after the first
  attempt without a new state-based reason;
- `retry_count`, `recovery_count`, and `checkpoint_redos`.

Do not double-count the same event merely because it is also described in an
issue. Keep the issue as the causal explanation and the count as the observed
control metric.

## Power BI Domain Metrics

When applicable, add `domain_metrics.power_bi` to the one generic record. Use
only values supported by the plan or executed evidence; set the object to
`null` or omit it when it does not apply.

`domain_metrics.power_bi` may contain these lightweight groups:

- `plan_estimates`: privacy-safe `task_class`, phase-specific
  action/transition ranges, recovery
  allowances, named `critical_or_uncertain_transitions`, `route_signal`,
  `route_reasons`, and `sol_escalation_triggers` from the plan. These remain
  hypotheses until an executed review observes them.
- `persistence`: `save_status`, `apply_status`, `reopen_status`, and
  `reading_view_status`. Keep prepared, previewed, applied, saved, reopened,
  and verified as distinct states; a visible editor is not proof of a saved
  artifact.
- `recovery_and_escalation`: `escalated_to_astra`,
  `rescue_task_or_session_id`, and `rescue_model`. Escalation or rescue is an
  observed event, not automatically an issue or a failed review.
- `validation`: directly evidenced query/model validation, filter or
  interaction checks, and exact report reopen/Reading-view checks. Use
  descriptive booleans or statuses only when the evidence supports them; do
  not invent KPI or row-count precision.

For a completed report build, persistence is verified only when evidence
covers the exact saved report, the explicit Save result where applicable, the
exact report reopen, and Reading-view behavior. Missing any required part
means the relevant status is unknown or not verified, not successful by
default. A plan gate always uses `not_observed_plan_only` for these execution
statuses.

## Sol/Astra Routing and Recovery

Preserve the planner's provisional route signal and the builder's observed
recovery events. A short action estimate does not prove low risk. Record a
trigger when evidence shows any of the following: two incorrect or uncertain
targets; the same navigation repeated twice; two rebind/recovery cycles
without progress; uncertain Save, Apply, upload, or model mutation; state loss
requiring more than one checkpoint redo; no checkpoint by roughly 30% of the
budget; or human correction of state, scope, or completion.

Do not treat the following as automatic model failures: browser disconnect,
runtime reset, Mac lock, file-picker timeout, stale handle, or service outage.
Capture them as counts and issues only when observed, and classify their cause
using the generic root-cause taxonomy.

## Power BI Issue Codes and Root-Cause Boundaries

Use the generic issue object keys and ordinal severity. Power BI-specific codes
may include `wrong_target`, `navigation_loop`, `stale_binding`, `state_loss`,
`uncertain_mutation`, `save_failure`, `model_validation`, `permission`,
`browser_disconnect`, `runtime_reset`, `mac_lock`, `upload_picker`,
`service_outage`, `plan_omission`, and `requirements_change`.

Choose one generic `root_cause` per supported issue:

- `model` — wrong targeting, repeated navigation, or a missed step not
  explained by the plan or control surface;
- `plan` — a missing, contradictory, or materially incorrect plan step or
  estimate;
- `environment_tool` — browser disconnect, runtime reset, stale binding,
  native picker, lock, or other control-surface failure;
- `application_service` — Power BI validation, query, refresh, save, or
  product-state failure;
- `source_data` — source/schema/content evidence caused the failure;
- `permission_authority` — permission, Build, owner, RLS, tenant, or other
  authority boundary prevented the requested operation;
- `human_requirements` — changed requirements, missing approval, or human
  intervention that is not a builder defect;
- `unknown` — evidence cannot distinguish the cause.

Do not use `power_bi` as a root-cause value; it is a task-family value. Do not
manufacture an issue because a usage join or optional metric is unavailable.
Benchmark severity remains independent from blocking/non-blocking review
classification and from the final verdict. An observed severity-2 recovery
can coexist with `ACCEPT`; a severity-1 plan omission can be blocking when it
prevents the requested result.

## Output Reminder

Do not expose a `Benchmark Record` JSON object or raw Power BI benchmark fields
in the user-facing review unless the user explicitly asks to see them. If an
authorized benchmark capture mechanism is available, put Power BI metrics
inside the single internal record's `domain_metrics.power_bi` and
`domain_metrics.computer_use`; never create a second Power BI record.
