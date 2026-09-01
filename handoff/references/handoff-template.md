# Handoff Template

Use this structure exactly. Omit an empty section only when it adds no value.

```markdown
# Handoff: <short outcome>

**Prepared:** <local time and timezone>
**Source task/session:** <ID if known; otherwise “Not available”>
**Destination focus:** <user-provided focus or “Resume the current objective”>

## Objective
<Desired outcome and material exclusions.>

## Current State
- **Verified now:** <facts directly checked>
- **Reported, not rechecked:** <claims needing caution>
- **Open / unknown:** <blockers or questions>

## Decisions and Constraints
- **Accepted:** <decision and important nuance>
- **Rejected:** <alternative and reason>
- **Required order/defaults:** <only when material>

## Evidence and Artifacts
- <absolute path, URL, task ID, commit SHA, or run ID — and what it proves>

## Working Copy and External State
- **Repository/worktree/branch:** <actual state or “Not applicable”>
- **Changes and checkpoint:** <scoped files, commit SHA, or no checkpoint>
- **Validation:** <passed, failed, skipped, or not run>
- **External state:** <relevant draft/job/browser/API state; no sensitive contents>

## Next Safe Move
<One action, required validation, and stop condition.>

## Authority Boundary
<Actions still unauthorized, such as push, send, deploy, data write, merge, restart, or delete.>

## Suggested Skills
- `$<skill>` — <why it is directly useful next>

## Bootstrap Prompt
```text
I am resuming work from a previous AI task or session. The handoff package follows below.

Treat only “Verified now” items as confirmed. Before making changes or external actions, inspect the named project instructions and current state. Continue only with the “Next Safe Move,” stay within its Authority Boundary, and stop for any listed decision or validation failure.
```
```
