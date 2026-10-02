# Task Patterns

Local synthesis for this meta-prompting workflow, adapted from Sol's task patterns
and [Astra guidance](sources.md). Use only the details the task needs.

- Knowledge work: Preserve the question, audience, supplied evidence, and desired
  output. Where grounding matters, request source support and distinguish inference
  from facts. Keep material gaps visible without adding research automatically.
- Automation: Preserve the trigger or cadence, inputs, action, destination, and
  permission to act. Include duplicate handling and failure behavior when needed.
  Leave unresolved choices open rather than inventing a schedule or recipient.
- Prototypes: Preserve the intended user, core interaction, supplied platform or
  stack, and acceptance conditions. Keep optional enhancements optional. Ask for
  checks of the core interaction, scaled to a prototype's purpose.
- Agent workflows: Describe the result, available tools and context, permitted
  actions, stopping conditions, and completion criteria. Encourage follow-through
  within that scope. When delegation belongs to the workflow, give each worker a
  bounded objective, needed context, and usable handoff; keep integration owned.

Prefer outcomes and decision criteria over rigid microsteps. Start without
examples; add a small aligned example when format or decision criteria need it.
For recurring work, refine the prompt using representative tasks and important
edge cases. A prompt alone does not provide tools, scheduling, or permissions.
