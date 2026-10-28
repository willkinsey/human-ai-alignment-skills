# Verdict and Output Contract

Read this reference before drafting the review decision.

## Verdict

Use exactly one verdict:

- **PROCEED** — plan is sound, its risks are within the verified low-risk boundary, and any notes are non-blocking. Return the decision to the user; do not message the worker unless the user explicitly approves a handoff.
- **REVISE PLAN** — a specific, evidence-backed correction is required before implementation because the current plan cannot safely meet the requested outcome.
- **HOLD FOR DECISION** — a user decision or external fact is required.
- **ACCEPT** — completed work meets the requested outcome and available evidence.
- **FIXES REQUIRED** — completed work has concrete defects or missing required evidence.

`ACCEPT — No changes needed` is a complete and successful review outcome. The reviewer does not need to find fault, request polish, or propose additional work to demonstrate that the review added value. Verification and a clear acceptance decision are the value.

## Required Ending Sections

End every review with these sections, even when there are no findings:

1. **Verdict** — one of the exact values above and one sentence explaining why.
2. **Evidence** — concise direct checks and material validation gaps.
3. **Findings and Notes** — separate blocking findings from qualifying non-blocking notes; say `No material concerns` when neither exists.
4. **Recommended Next Step** — name the next safe, concrete action. If it involves another task, state that the user can authorize a handoff; do not authorize it yourself.
5. **Then** — the expected follow-on checkpoint. Anticipate normal operational continuity: after implementation, review; after approval, stage/commit; after commit verification, push; after push, verify the remote or deployment. Do not make the user remember the next gate.
6. **Authority Boundary** — name actions that remain blocked pending user authorization.

Do not expose a **Benchmark Record** section or raw benchmark JSON in the
user-facing review unless the user explicitly asks to see it. Follow
`references/benchmark-observation.md` as an internal assessment checklist.

For `ACCEPT — No changes needed`, recommend closing the review and state that no follow-on work is required. Do not invent a next action merely to fill the format.

Keep the recommended next step proportional to the evidence. For a sound plan with only non-blocking notes, use **PROCEED** and return the assessment to the user. Only after the user explicitly authorizes a handoff may the reviewer send `PLAN_APPROVED` and instruct the worker to proceed. If the supplied plan contains unneeded broad validation, reduce it to targeted acceptance checks unless the broader-integrity rule applies. Do not collapse multiple material gates into an unbounded “proceed.”
