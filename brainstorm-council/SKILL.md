---
name: brainstorm-council
description: Brainstorm a subject through three independent GPT-6 Luna subagents with practical, inventive, and first-principles perspectives, then have the primary session select or combine the strongest ideas. Use for council brainstorming, exploring alternatives, or developing a direction through multiple perspectives; ordinary brainstorming does not require a council.
---

# Brainstorm Council

Use three independent Luna thinkers to explore the same subject. The primary session owns the user's intent, compares every report, and recommends the best option or a stronger combination. Agreement is not proof, and every agent need not contribute to the final answer.

## Frame the Shared Brief

Extract the subject, desired outcome, audience, relevant facts, constraints, and user preferences from the conversation and any directly relevant sources. Infer routine details; ask only when missing information would materially change the brainstorming. State material assumptions briefly and keep moving where useful work is possible.

Give all three agents the same factual brief and the same definition of success. Preserve the user's stated preferences, but omit the primary session's tentative answer so it does not anchor the workers. Select a few task-relevant comparison criteria, such as usefulness, originality, feasibility, or fit for the audience.

Tell the user that three Luna thinkers will work independently and the primary session will synthesize their reports.

## Launch Three Independent Thinkers

Use native subagents inside the current chat, with GPT-6 Luna at Max reasoning for all three. Where available, use `agent_type: "luna_worker"`, which fixes that model and effort. Otherwise explicitly select `model: "gpt-6-luna"` and `reasoning_effort: "max"`. Use `fork_turns: "none"` and supply the complete brief so each worker starts without the primary session's earlier speculation. Do not create separate user-owned chats or change global agent settings.

Launch all three before waiting for their results. Each explores the whole problem through a different emphasis:

| Persona | Emphasis |
| --- | --- |
| Practical Thinker | Find useful, achievable ideas and a clear path to making them work. Look for simplicity and resource fit without defaulting to the safest or most familiar answer. |
| Inventive Thinker | Explore unexpected connections, alternative forms, and possibilities beyond the obvious. Explain why an unusual idea would serve the goal. |
| First-Principles Thinker | Examine assumptions, distinguish actual requirements from habits, and rebuild an approach around the underlying goal. Respect explicit constraints while questioning inferred ones. |

These are thinking styles, not rigid characters. All three must generate complete solutions and consider tradeoffs. No worker is limited to criticism, implementation planning, or novelty alone.

Use this compact assignment structure, filling it with the actual task and persona:

```text
Role: One independent thinker on a three-person brainstorming council.
Persona: Your assigned thinking emphasis, applied without caricature.
Objective: Develop strong options for the subject in the shared brief.
Shared brief: The user's goal, audience, facts, preferences, constraints,
material assumptions, and comparison criteria.
Scope and authority: Brainstorm and read relevant sources as needed. Do not
implement ideas, edit shared files, write to external services, or delegate.
You are not alone in the workspace. Report to the primary session only;
do not inspect or discuss the other thinkers' work.
Method: Explore several materially different possibilities before choosing
your strongest. Treat your persona as an emphasis, not a restriction.
Deliverable: A concise report, normally 300-500 words, containing your
strongest options (usually three), your recommended option and why it wins,
its main weakness, and assumptions or unknowns that could change your choice.
Include sources for consequential factual claims you researched; distinguish
those claims from creative proposals. Flag any material gap in the brief.
Completion: Return your independent report to the primary session and stop.
```

Keep the initial reports independent: do not share one worker's ideas with another or supply an emerging winner while the others are still brainstorming. Workers may research when the subject needs evidence; do not turn every brainstorming request into a research project.

If Luna or three concurrent worker slots are unavailable, report the limitation and retain completed work. Do not silently substitute models or claim a full council ran. Resume missing assignments when capacity becomes available; otherwise explain what is needed to finish.

## Compare and Synthesize in the Primary Session

Wait for all three reports and read each in full. The primary session performs the final judgment; do not spawn a separate chairman by default.

- Compare substance against the shared brief and criteria. Do not reward length, confidence, arrival order, or agreement alone.
- Identify each report's strongest contribution, main limitation, and useful differences from the others. Keep strong minority ideas in consideration.
- Choose the strongest complete option as the starting point. Combine elements only when they are compatible and improve the result; check that the combination still works as a whole.
- Check consequential factual claims before relying on them. Three agents repeating an assumption does not verify it. Preserve uncertainty that could change the recommendation.
- If none of the options meets the goal, say what is missing rather than declaring a winner. One focused follow-up to the relevant worker is appropriate for a specific gap; repeated debate and peer-review rounds are not the default.

## Return a Useful Recommendation

Lead with the recommended idea and why it best serves the user's goal. Briefly show what each thinker contributed and explain whether the result selects one proposal or combines specific elements. Include the meaningful tradeoff or unresolved assumption and one concrete next step.

Keep the answer proportional to the request. A compact comparison table can help; full worker transcripts and numerical scoring are unnecessary unless requested. Keep brainstorming separate from implementing the recommendation, and follow the user's existing authorization for any next action.

For the sources and rationale behind this workflow, read [Design Notes](references/design-notes.md) only when maintaining the skill or explaining its design.
