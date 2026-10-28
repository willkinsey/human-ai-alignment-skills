# Generic Benchmark Observation

Read this reference for every independent review: `plan_gate`,
`completed_work_audit`, and `recheck`. The record supplements task history,
artifacts, and the usage monitor; it is not a replacement for the human
review or its verdict.

## Internal Capture and User-Facing Exclusion

Use these dimensions as an internal review checklist. Do not emit a fenced
JSON object, a `Benchmark Record` section, or raw benchmark fields in the
user-facing response unless the user explicitly asks to see them. When an
authorized benchmark capture mechanism is available, capture at most one
record and nest any Power BI extension in that record's `domain_metrics`
object. When no such mechanism is available, do not create a file, database
entry, or other artifact merely to preserve the record.

The benchmark assessment does not authorize writing SQLite, the local
telemetry or usage database, task history, source data, or customer data. The
review remains manual and read-only.

## Review Kind, Join, and Classification

- Require the reviewed task or session ID and use it as `task_or_session_id`,
  the join key. Never infer that ID from a title, report name, or file name.
- Carry forward one stable opaque `benchmark_id` across plan, execution, and
  review. If one does not exist, generate a privacy-safe value such as
  `bench-20260910-a1b2c3d4`. Do not encode a customer, report, workspace,
  semantic model, source, or business label in the ID. `benchmark_id` is not
  the task/session join key.
- Set `review_kind` to `plan_gate`, `completed_work_audit`, or `recheck`.
  Use `phase: plan_review` for a plan gate and `phase: observation` for an
  execution review.
- Use the controlled `task_family` values `power_bi`, `software_build`,
  `data_analysis`, `research`, `document`, `spreadsheet`, `presentation`,
  `communication`, `business_process`, `automation`, `review`, and `other`.
- Use the independent controlled `interaction_mode` values
  `browser_computer_use`, `terminal_code`, `file_artifact`, `mixed`,
  `advisory_only`, and `unknown`. The dimensions intentionally support
  overlapping concepts: Power BI browser work is `task_family: power_bi` and
  `interaction_mode: browser_computer_use`. Use optional `tags` for additional
  evidence-backed concepts, not private labels or a new uncontrolled taxonomy.

## Observation Rules

For a `plan_gate`, record plan estimates and plan quality only. Set execution,
outcome, intervention, and persistence fields to `not_observed_plan_only` or
`null`; do not turn a sound plan into a claim that work ran, saved, reopened,
or verified. Do not create execution issues for events that have not occurred.

For a `completed_work_audit` or `recheck`, record execution and outcome only
from auditable task history, artifacts, browser/computer evidence, test output,
or an explicit monitor join. A partial trace must say so in
`observation_basis`; estimates are not observations. If the required evidence
is absent, use `null` or an appropriate unknown status rather than guessing.

`evidence_strength` describes the quality of the evidence available to the
review (`strong`, `moderate`, `weak`, or `unknown`).
`verification_strength` describes how directly the requested outcome was
verified (`strong`, `moderate`, `weak`, `not_observed_plan_only`, or `unknown`).
Use the outcome booleans only when the evidence supports them:
`requested_outcome_met`, `verified_completion`, `first_pass_verified`, and
`successful_without_intervention`.

Capture, when available, `human_intervention_count`,
`human_intervention_minutes`, `retry_count`, `recovery_count`,
`rework_count`, and `rework_minutes`. A retry or recovery must be supported by
the trace; passive waiting and a tool's internal retry are not automatically
operator actions. Keep the review verdict (`PROCEED`, `REVISE PLAN`, `HOLD FOR
DECISION`, `ACCEPT`, or `FIXES REQUIRED`) separate from benchmark outcomes and
issue severity.

## Planned and Observed Counts

The optional plan estimate fields are generic so a reviewer can carry forward
an auditable plan without inventing domain precision:

- `planned_actions_minimum`, `planned_actions_expected`,
  `planned_actions_risk_low`, and `planned_actions_risk_high`;
- `planned_transitions_minimum`, `planned_transitions_expected`,
  `planned_transitions_risk_low`, and `planned_transitions_risk_high`;
- `recovery_allowance_actions`, `recovery_allowance_transitions`, and
  `estimate_confidence`.

These numbers are hypotheses from the plan. For executed work, put observed
atomic operator inputs in `observed_actions` and meaningful state changes in
`observed_transitions` only when they are auditable. If the reviewer cannot
count them reliably, leave them `null` and explain the boundary in
`observation_basis` or `review_notes`.

## Usage and Monitor Annotations

Usage values are joins, never reviewer estimates. Set `usage_status` to
`join from monitor` when values are unavailable and leave `model`,
`reasoning_effort`, `model_attribution_status`, `models_used`,
`reasoning_efforts_used`, `turns`, `input_tokens`, `cached_input_tokens`,
`output_tokens`, `reasoning_tokens`, `total_tokens`, `duration_seconds`, and
`tool_calls` null. Populate them only when directly available from the task or
monitor; do not substitute the reviewer's model or effort.

Set `model_attribution_status` to `single_model`, `mixed_model`, or `unknown`.
For a single-model task, populate `model` and `reasoning_effort`; for a mixed
task, leave those singular fields null unless a primary builder is directly
established and list the observed values in `models_used` and
`reasoning_efforts_used`. The monitor's turn-level rows remain authoritative
for allocating usage across models.

The nullable monitor annotations are included as proposed fields:
`task_type`, `outcome`, `rework_minutes`, `usefulness_rating`, and
`reviewed_at`. They describe a possible monitor join and do not authorize or
perform a telemetry write.

## Issues and Severity

Use the general issue taxonomy only when evidence supports a material issue.
Allowed `root_cause` values are `model`, `plan`, `environment_tool`,
`application_service`, `source_data`, `human_requirements`,
`permission_authority`, and `unknown`. Choose one root cause per issue when
the evidence supports it; otherwise use `unknown`. Useful general `code`
values include `requirement_gap`, `plan_omission`, `wrong_target`,
`navigation_loop`, `stale_binding`, `state_loss`, `uncertain_mutation`,
`reasoning_error`, `factual_error`, `code_defect`, `data_error`,
`artifact_quality`, `validation_failure`, `persistence_failure`,
`delivery_failure`, `scope_expansion`, `permission`, `source_contract`,
`test_gap`, `environment_failure`, `service_outage`, `requirements_change`,
and `unknown`. A domain extension may add a more specific code while retaining
the same root-cause boundaries.

Order issues by highest impact first, then rework or intervention impact, then
occurrence order. Use ordinal severity `1`, `2`, or `3`:

- `1` — minor friction or bounded rework with no incorrect result and no
  material human rescue;
- `2` — material recovery, rework, delay, or intervention, but the requested
  result was ultimately verified;
- `3` — the result failed, was partial or unverified, left an incorrect saved
  state or lost work, or required substantial human rescue.

Severity is not a blocking flag. Each issue's
`review_classification` is independently `blocking` or `non_blocking_note`
under the review standards. An empty `issues` array means no material issue;
do not add a severity-0 placeholder or manufacture an issue because a field is
unavailable. Keep `issue_count` and `max_issue_severity` consistent with the
array.

Every issue uses exactly these keys: `rank`, `code`, `severity`,
`review_classification`, `root_cause`, `root_cause_confidence`, `evidence`,
`impact`, and `recovery_or_rework`.

## Optional Domain Metrics

Set `domain_metrics` to `null` or omit it when no domain shape applies. Do not
fill optional metrics with fake precision. When a shape is useful, include only
directly evidenced values. Lightweight shapes are:

- `computer_use`: `planned_atomic_ui_actions`, `observed_atomic_ui_actions`,
  `planned_state_transitions`, `observed_state_transitions`,
  `incorrect_target_count`, `repeated_navigation_count`, `retry_count`,
  `recovery_count`, and `checkpoint_redos`.
- `software_build`: `files_changed`, `tests_run`, `tests_passed`,
  `build_verified`, and `commit_created`.
- `artifact_creation`: `artifact_types`, `artifacts_created`,
  `render_verified`, `reopen_verified`, and `export_verified`.
- `research_analysis`: `sources_consulted`, `source_quality_checked`,
  `calculations_reproducible`, and `citations_verified`.

Read the conditional Power BI extension only when the reviewed task is a Power
BI task. It defines `domain_metrics.power_bi` and the additional
`domain_metrics.computer_use` values for that case.

## Generic Record Template

Use one object with these fields, retaining `null` for unavailable values. The
template is intentionally generic; do not copy Power BI-only fields into
non-Power BI records merely because they appear in a past review.

```json
{
  "record_type": "benchmark_observation",
  "benchmark_id": "bench-20260910-a1b2c3d4",
  "phase": "observation",
  "review_kind": "completed_work_audit",
  "task_or_session_id": null,
  "task_family": "software_build",
  "interaction_mode": "terminal_code",
  "tags": [],
  "observation_basis": "complete",
  "evidence_strength": "strong",
  "verification_strength": "strong",
  "plan_quality": null,
  "requested_outcome_met": null,
  "verified_completion": null,
  "first_pass_verified": null,
  "successful_without_intervention": null,
  "review_verdict": null,
  "completion_status": null,
  "human_intervention_count": null,
  "human_intervention_minutes": null,
  "human_intervention_summary": null,
  "retry_count": null,
  "recovery_count": null,
  "rework_count": null,
  "rework_minutes": null,
  "planned_actions_minimum": null,
  "planned_actions_expected": null,
  "planned_actions_risk_low": null,
  "planned_actions_risk_high": null,
  "planned_transitions_minimum": null,
  "planned_transitions_expected": null,
  "planned_transitions_risk_low": null,
  "planned_transitions_risk_high": null,
  "recovery_allowance_actions": null,
  "recovery_allowance_transitions": null,
  "estimate_confidence": null,
  "observed_actions": null,
  "observed_transitions": null,
  "usage_status": "join from monitor",
  "model": null,
  "reasoning_effort": null,
  "model_attribution_status": "unknown",
  "models_used": [],
  "reasoning_efforts_used": [],
  "turns": null,
  "input_tokens": null,
  "cached_input_tokens": null,
  "output_tokens": null,
  "reasoning_tokens": null,
  "total_tokens": null,
  "duration_seconds": null,
  "tool_calls": null,
  "task_type": null,
  "outcome": null,
  "usefulness_rating": null,
  "reviewed_at": null,
  "issue_count": 0,
  "max_issue_severity": 0,
  "issues": [],
  "review_notes": null,
  "domain_metrics": null
}
```

For a plan gate, set `phase` to `plan_review`, `review_kind` to `plan_gate`,
populate only the supported plan estimate and plan-quality information, and
set execution/outcome fields such as `observation_basis`,
`requested_outcome_met`, `verified_completion`, `completion_status`, and
`human_intervention_count` to `not_observed_plan_only` or `null` as
appropriate. A completed-work audit or recheck must not reuse that plan-only
status after execution evidence exists.
