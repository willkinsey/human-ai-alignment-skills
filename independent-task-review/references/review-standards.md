# Review Standards

Read this reference for every independent review.

## Review Safely

Start every review in manual, read-only mode. Do not edit files, commit, push, restart services, run migrations, publish, message the original task, or instruct it to do anything until the user explicitly authorizes a handoff. A task reference and a favorable review verdict are not authorization to contact that task.

Read enough task history to establish the original request, approved plan or intended approach, decisions, claimed implementation, validation, and current stop point. Fetch older task pages when the recent history does not establish those facts.

Independently inspect relevant repository instructions, working-tree and branch state, diffs, tests, and artifacts. Distinguish facts you directly verified from claims made by the original task. Use non-mutating browser or other read-only checks only when they materially test the requested outcome and current access permits them.

In manual review, do not rerun tests, builds, formatters, or commands that may change state without user authorization. State any validation gap plainly; never fill it with confidence theater.

## Anchor Scope and Acceptance

Establish the acceptance baseline in this order:

1. the user's explicit requested outcome, exclusions, and decisions;
2. behavior necessarily implied for that outcome to work in its stated or normal current use; and
3. applicable project instructions and acceptance criteria that do not expand the request.

Treat an implication as in scope only when the requested result would otherwise be incomplete, incorrect, unsafe, or unusable in its intended current context. Do not expand scope based on what a different future user, task, session, environment, or workflow might do incorrectly. Future-proofing, generalized proofing, extra documentation, defensive controls, and support for hypothetical reuse are outside acceptance unless the user requested durability across that boundary or current evidence shows the requested result depends on it.

Do not substitute the reviewer's preferred architecture, process maturity, or definition of “complete” for the user's objective. Review the delivered result, not an imagined larger program.

## Keep the Review Proportionate

Use the acceptance baseline above as the scope anchor. Treat the builder's stated criteria as supporting context, not permission to narrow or expand the user's objective. Do not require a full data audit, a source-fingerprint program, an all-row omission ledger, new reconciliation infrastructure, a cross-market rebuild, or a new fail-closed gate merely because a report, import, or data-derived output is involved.

For a normal code or report change, require only the smallest validation set that directly proves the requested outcome: the reported scenario or targeted regression, an existing focused check when the changed code already has one, and an artifact or user-flow inspection when the result is visible to a user. Treat broader checks as optional unless the user explicitly asks for them.

Require broader integrity validation only when at least one is true:

- the user asks for a full audit, reconciliation, migration, or population-wide correctness guarantee;
- the change writes, migrates, bulk-updates, deletes, or publishes customer or production data;
- direct evidence shows that a targeted check cannot detect the demonstrated failure; or
- the existing system has a known systemic integrity failure that the requested change must correct.

Before making any broad check or new gate required, state the direct evidence, the specific failure it prevents, and why a narrower check is insufficient. If that case is not made, present it as an optional future improvement and do not delay `PROCEED` or `PLAN_APPROVED` for it.

Do not turn a routine source disagreement, a benign data variance, or a possible future edge case into a blocking source-contract decision unless it prevents the requested output from being correct under the established source-of-truth policy.

## Apply the Review Standard

For a plan gate, check requirement coverage, design correctness, direct failure modes, data/security/privacy risk, rollback where relevant, verification, and scope control. Require resolution only for decisions that materially affect the requested outcome, safety, or an explicit hard stop. Do not demand a complete architecture, governance model, or every hypothetical edge case before a scoped task can proceed.

For completed-work audits and re-checks, compare the requested behavior with the actual diff and available validation evidence. Check for unintended files, unverified claims, regressions, missing tests, data changes, branch/worktree drift, operational side effects, and whether the original acceptance criteria were actually met.

Favor concrete, severity-ranked findings. Do not manufacture findings merely to be skeptical.

A blocking finding must identify all three:

- the in-scope requirement or necessary implied behavior that is not met;
- direct evidence from the current plan, diff, artifact, validation, or intended execution path; and
- the material consequence for the requested result.

If any part is missing, it is not a blocking finding. A possibility that a future session may misuse, omit, misunderstand, or fail to preserve something is not evidence that the current result failed. Do not require proofing against hypothetical future behavior unless that cross-session durability is itself in scope.

Separate every finding into one of two categories:

- **Blocking** — it creates a material correctness, safety, scope, validation, or hard-stop concern. Require a revised plan or a user decision.
- **Non-blocking note** — it is a minor improvement that does not change whether the plan safely delivers the requested outcome. Include it as guidance, not as a condition to proceed.

Do not describe a sound plan as having caveats merely because it has non-blocking notes.

### Apply the Caveat Admission Test

Do not add a non-blocking note merely to demonstrate diligence or produce value. Admit a note only when it is specific to the current plan and its likely benefit clearly outweighs the added implementation or review effort. A qualifying note must materially reduce the likelihood of a bug, data/security problem, failed validation, costly rework, or unwanted scope change.

Do not add notes about style preferences, alternate designs, speculative edge cases without supporting evidence, hypothetical future-session behavior, or polish that does not materially improve the requested outcome. Do not set a quota for notes: zero notes is a successful review when the plan is clean.

When no note qualifies, say `No material concerns` and proceed. When notes qualify, keep them concise and grouped; never turn them into hidden conditions for a `PROCEED` verdict.

### Apply the Validation Admission Test

Do not add a required test, reconciliation, source check, or fail-closed gate merely to be thorough. Require it only when it directly proves a stated acceptance criterion or meets the broader-integrity conditions in **Keep the Review Proportionate**. Otherwise label it `Optional future hardening` and do not make it part of the worker handoff.
