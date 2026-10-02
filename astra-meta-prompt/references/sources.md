# Sources and Applicability

Official pages searched and fetched: 2026-10-02. This is the retrieval date, not
a publication date. Refresh official documentation for current model/API settings.

## Documented Astra Target

The [model catalog](https://developers.openai.com/api/docs/models) and
[GPT-6 Astra model page](https://developers.openai.com/api/docs/models/gpt-6-astra)
identify the target as `gpt-6-astra`, a reasoning model for demanding reasoning,
coding, computer use, research, and document creation. The model page lists
`low`, `medium`, `high`, `xhigh`, and `max` reasoning effort. This skill does not
change the client's model or effort settings.

The [GPT-6 API guide](https://developers.openai.com/api/docs/guides/latest-model#migration-quickstart)
requires Responses for Astra tool calling. Chat Completions supports requests
without tools. Astra does not support `none` reasoning or custom `temperature`,
`top_p`, or log probabilities. These API facts do not establish identical Codex
client controls; include settings only when the user needs them.

## Official Prompting Guidance

The [Astra prompting section](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices)
was fetched directly. The same guidance appears in the
[GPT-6 family guide](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices).
OpenAI presents it as family-wide starting guidance based on Astra observations:

- Astra may seek clarification where routine assumptions and continued work would
  serve the user. Encourage completion within the intended scope.
- Astra follows instructions strongly and can be sensitive to conflicting skill
  or `AGENTS.md` guidance. Clarify how user intent and skill guidance interact.
- Astra tends toward detailed, formatted writing. Specify the desired style.
- Astra may delegate less than a workflow needs. Specify delegation when useful
  for that workflow and available in its harness.
- Astra can test small coding changes more broadly than necessary. Calibrate
  checks and repeat them when there is a reason.

The [reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices#how-to-prompt-reasoning-models-effectively)
support direct prompts, clear separation of inputs, zero-shot first, aligned
examples when needed, and avoiding internal chain-of-thought requests. That page
also contains older o-series claims; its legacy settings and formatting rules
are not Astra-specific recommendations.

## Local Adaptation

The smallest-complete-prompt structure, task patterns, prompt-only boundary, and
selective use of Astra considerations are local synthesis for this meta-prompting workflow.
They are not a claim that every Astra prompt needs all five considerations.

The embedded cleanup uses the `remove-audit-language` editing principles: remove
ceremonial caution while preserving material uncertainty, genuine requirements,
real checks, and user boundaries. It is local editing guidance, not an official
OpenAI model rule.
