# Sol Meta-Prompt

Turn rough goals into concise, paste-ready prompts for GPT-6.1 Sol. Audit-language
cleanup happens during generation, preserving useful checks and explicit boundaries.

Copy this complete folder into your agent's discoverable skills directory, then use:

```text
$sol-meta-prompt Turn this rough goal into a prompt for GPT-6.1 Sol: ...
```

Provide your goal, relevant context, and any constraints you already know. The skill
returns a prompt; it executes the resulting task only when you request that too.
It supports knowledge work, automation, prototypes, and agent workflows.

The [dated source notes](references/sources.md) distinguish Sol facts from general
and family guidance. No standalone Sol-specific prompting manual was found;
family behavior observations concern Astra and need evaluation on your workload.
This skill does not select or configure a model. A small independent behavior
check confirmed concise prompt output with required checks, data preservation,
and a no-deployment boundary; it was not a Sol performance benchmark.

Written instructions are covered by the repository's [MIT License](../LICENSE).
The skill contains no media assets; see [Content Rights](../CONTENT-RIGHTS.md).
