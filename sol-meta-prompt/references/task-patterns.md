# Task Patterns

Use these patterns when they help the task. They are local synthesis; attribution
is in [sources](sources.md).

- Knowledge work: Identify the question, audience, supplied evidence, and desired
  output. When grounding matters, ask the executing agent to distinguish source
  facts, inference, and missing information. Do not add research automatically.
- Automation: Preserve the trigger or cadence, inputs, desired action, destination,
  and permission to act. Leave unresolved choices open. Include duplicate handling
  and failure behavior when the automation needs them.
- Prototypes: Preserve the intended user, core interaction, supplied platform or
  stack, and acceptance conditions. Keep optional enhancements optional; do not
  turn a prototype into production infrastructure.
- Agent workflows: Describe the outcome, available tools, permitted actions,
  stopping conditions, and how to tell the work is done. Encourage follow-through.
  Include delegation and handoffs when requested or already part of the workflow.

Prefer direct instructions over rigid microsteps. Start without examples; add a
small aligned example when formatting or decision criteria remain ambiguous.
For recurring work, try the prompt on representative tasks and important edge
cases, then refine it from the results.
