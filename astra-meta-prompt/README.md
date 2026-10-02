# Astra Meta-Prompt

Turn rough goals into concise prompts for GPT-6 Astra across knowledge work,
automation, prototypes, and agent workflows. The skill preserves your intent and
cleans unnecessary audit language before returning a paste-ready prompt.

## Use

Copy this folder into your Codex skills directory, then invoke:

```text
$astra-meta-prompt Turn this goal into an Astra prompt: [your goal and relevant context]
```

Provide the goal, useful context, constraints, and desired output. The skill asks
for missing information only when it prevents a useful prompt.

It generates the prompt; task execution requires a separate request. It does not
change model settings or supply tools, scheduling, or permissions.

## Guidance and Sources

[SKILL.md](SKILL.md) contains the workflow and built-in cleanup rules.
[Task patterns](references/task-patterns.md) support complex or recurring work.
[Dated sources](references/sources.md) distinguish official Astra guidance from
local adaptation. Model/API guidance was checked on 2026-10-02; recheck official
documentation for current settings.

## License

The written instructions are covered by the repository's [MIT License](../LICENSE).
See [Content Rights](../CONTENT-RIGHTS.md) for the scope of reuse.
