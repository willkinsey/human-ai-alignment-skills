# Sources and Applicability

Researched and retrieved: 2026-10-01. This is the retrieval date, not an asserted
publication date. Recheck official documentation for current model/API settings.

## GPT-6.1 Sol

[GPT-6.1 Sol model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
and [GPT-6.1 Sol in the family guide](https://developers.openai.com/api/docs/guides/latest-model#gpt-61-sol).

The exact model ID is gpt-6.1-sol; it is a reasoning model. API effort supports
low, medium (default), high, xhigh, and max; none and minimal are unsupported.
Responses is required for tool calling; Chat Completions supports requests
without tools. These API facts do not establish identical Codex client controls.

[Codex best practices](https://learn.chatgpt.com/guides/best-practices#strong-first-use-context-and-prompts)
explicitly recommends starting Sol with the reasoning effort available by default
in the client. Prompt rewriting alone need not set effort.

## Applicable Family and General Guidance

[GPT-6 prompting best practices](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices)
presents family-wide starting prompts, while attributing behavioral observations
to Astra and requiring evaluation with the chosen model/workload. Adapt autonomy,
conflict handling, writing, delegation, and testing instructions to actual user
scope.

[Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
recommends relevant context, a clear result, and task-specific constraints.
Reasoning models benefit from high-level goals. Evaluate representative tasks as
prompts change; examples should clarify requirements rather than add them.

[Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
recommends simple direct prompts, clear input separation, zero-shot first, and
aligned examples when useful. Avoid demanding internal chain-of-thought. This
page contains older o-series-specific settings and behaviors; do not apply those
details to Sol without current model-specific confirmation.

## Gap and Local Synthesis

No standalone Sol 6.1-specific prompting manual was found in the searched
official documentation. Astra observations are not verified Sol findings. The
task patterns, draft-only boundary, and concise prompting approach are local
synthesis for this meta-prompting workflow.

The prompt-cleanup principles are local editing guidance, not an OpenAI
model-specific rule. The essentials are embedded in the entrypoint.
