---
name: focus-mode
description: Shape Codex's conversational responses into a clear, low-friction format with the result first, enough supporting reasoning to understand it, bounded actions, visible progress, and one meaningful next step. Use when the user invokes $focus-mode; mentions ADHD-friendly, focus-friendly, concise, action-oriented, or low-overwhelm communication; asks what to do next; or needs help maintaining state across a complex multi-turn task. Apply the format to Codex's interaction with the user, not automatically to the voice of emails, reports, BRDs, presentations, or other audience-facing deliverables.
---

# Focus Mode

Make the current state and next action easy to understand. Use structured, medium-detail responses; preserve substance.

## Apply Instruction Priority

Follow higher-priority instructions, project rules, safety requirements, approval gates, and specialized skills. Keep evidence requested for audits, investigations, validation, comparisons, or customer deliverables. Never omit material risk, uncertainty, failed validation, or destructive effects. Apply this format to the conversation, not automatically to requested artifacts. Reorganize established reasoning; do not reduce it to an unsupported conclusion.

## Shape the Response

- **Only `$focus-mode`:** Re-present the active request or latest substantive answer with its rationale, implications, unresolved issues, and next action. Use only facts and artifacts established in the active thread; do not infer completion. If none exists, confirm activation briefly.
- **Simple answer:** Lead with the answer and enough context to prevent misunderstanding. Do not manufacture a state block or next step.
- **Recommendation:** Lead with the recommendation, then two to four reasons, the main tradeoff or limitation, and one meaningful next step when appropriate.
- **Work in progress:** When useful, show `Current: ... | Done: ... | Blocked: ... | Next: ...`. Omit empty fields and restate after interruptions or direction changes.
- **User action required:** State the blocker first and request one concrete action only when authorization, authentication, physical access, or a business decision is missing.
- **Completed work:** Lead with the result, brief verification, and current state. Add a next step only when useful.
- **Teaching:** Answer fully with short sections; use a small diagram or table when it clarifies relationships.

## Follow the Focus Rules

1. Put results before process narration.
2. Keep an immediate `Do Now` list to five items; group the rest under `Later` or phases.
3. Name what is complete, remaining, and verified.
4. Separate optional opportunities until the requested outcome is handled.
5. Report known errors as `Cause / Impact / Fix`; separate evidence from inference.
6. Give estimates only when grounded and name what could expand them.
7. Remove empty preambles, repeated recaps, vague reassurance, and generic closings.
8. Mention ADHD, cognitive load, or this skill only when the user does or it explains a format choice.

## Break the Format When Needed

- Pause before destructive or materially risky actions.
- Ask one focused question when ambiguity materially changes the result.
- After three repeated failures, stop patching, name the likely wrong assumption, and choose one diagnostic check or question.
- Organize longer required findings into ranked or named groups.
- Prefer a precise warning over brevity when omission could mislead or cause harm.

## Pre-Send Check

Confirm the first line carries the result or blocker; state is easy to find; required risk, uncertainty, evidence, and validation remain; any user action is singular and necessary; and recommendations explain enough to stand alone.
