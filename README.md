# Human-AI Alignment Skills

Practical skills for helping professionals and AI work together more clearly.

These skills help you create shared understanding around the goal, context, standards, and next steps so you get less rework and higher quality results.

## Install

With Git installed, run these commands in a terminal (macOS, Linux, or WSL):

```sh
git clone https://github.com/willkinsey/human-ai-alignment-skills.git
cd human-ai-alignment-skills
```

Choose your agent and install all skills or just one. These commands keep existing files.

### OpenAI Codex

The [official user-level skill directory](https://learn.chatgpt.com/docs/build-skills) is `~/.agents/skills/`.

Install all skills:

```sh
mkdir -p ~/.agents/skills
for skill in */SKILL.md; do
  cp -Rn "${skill%/SKILL.md}" ~/.agents/skills/
done
```

Or install one skill folder, such as `plain-language-reset`:

```sh
mkdir -p ~/.agents/skills
cp -Rn plain-language-reset ~/.agents/skills/
```

### Claude Code

The [official personal skill directory](https://code.claude.com/docs/en/skills) is `~/.claude/skills/`.

Install all skills:

```sh
mkdir -p ~/.claude/skills
for skill in */SKILL.md; do
  cp -Rn "${skill%/SKILL.md}" ~/.claude/skills/
done
```

Or install one skill folder, such as `plain-language-reset`:

```sh
mkdir -p ~/.claude/skills
cp -Rn plain-language-reset ~/.claude/skills/
```

Restart or reload your agent if your tool requires it to discover new skills.

### Which skill should I start with?

- [plain-language-reset](plain-language-reset/): Re-explain a confusing response in short, plain language.
- [questions-for-context-brain-dumps](questions-for-context-brain-dumps/): Get open-ended questions to help you record useful context about a topic or decision.
- [sol-meta-prompt](sol-meta-prompt/): Turn a rough goal into a concise prompt for GPT-6.1 Sol.
- [astra-meta-prompt](astra-meta-prompt/): Turn a rough goal into a concise prompt for GPT-6 Astra.
- [delegate-bounded-work](delegate-bounded-work/): Give a subagent a clear task, scope, and definition of success.
- [ntfy-me](ntfy-me/): Send one requested job notification to a configured ntfy topic on macOS.

## What You’ll Find Here

- Clearer ways to start AI assisted work
- Simple methods to define goals and constraints
- Better handoffs between people and AI
- [Sol Meta-Prompt](sol-meta-prompt/) — turn rough goals into concise GPT-6.1 Sol prompts, with audit-language cleanup built in
- [Astra Meta-Prompt](astra-meta-prompt/) — turn rough goals into concise GPT-6 Astra prompts, with audit-language cleanup built in
- Practical review steps before acting on AI output

## The Goal

Help AI understand how you work and help you quickly understand, evaluate, and use what AI produces.

## Getting Started

[Install a skill](#install) that matches the work in front of you, then adapt it to your role.

---

Built for professionals who need higher quality AI outputs.

## License and Content Rights

The skills, prompts, code, and written instructions in this repository are available under the [MIT License](LICENSE). Logos, trademarks, photographs, illustrations, templates, PDFs, screenshots, and other visual or media assets are not licensed for reuse unless their folder explicitly says otherwise. See [Content Rights](CONTENT-RIGHTS.md).
