---
name: handoff-side
description: Create a compact, paste-ready context transfer from a material side chat into its main task. Use when the user asks to bring a side chat back to the main chat, summarize a side-session's decisions, or prepare a main-chat update. Do not use for a full fresh-task handoff or an ordinary conversational recap.
---

# Side-Chat Handoff

Create a small, accurate update the main task can use without reopening the side conversation.

## Gather the Load-Bearing Context

Use the side conversation and only enough evidence to avoid carrying forward a stale claim. Preserve:

- the side chat's purpose and its resulting recommendation, decision, or finding;
- facts, files, paths, commands, task IDs, and validation the main task needs;
- any open question, blocker, assumption, or authority limit that changes what the main task may do next; and
- rejected approaches only when likely to be reconsidered incorrectly.

Distinguish **Verified**, **Reported, not rechecked**, and **Open** information. Do not imply the side chat completed work that it only proposed, explored, or inspected.

Prefer paths, SHAs, URLs, and short identifiers over copied logs, tables, artifacts, or long quotations. Redact sensitive content.

## Make It Easy to Paste

Return one copyable Markdown block in this format, normally no more than eight bullets. Omit empty sections.

```markdown
## Side-Chat Context: <short topic>

- **Purpose:** <why this side chat happened>
- **Result:** <decision, finding, or recommendation>
- **Verified:** <only facts directly checked>
- **Reported / not rechecked:** <only if relevant>
- **Decisions and constraints:** <accepted/rejected choice or important boundary>
- **Evidence:** <path, SHA, URL, identifier, or “Conversation only”>
- **Open / blocked:** <what remains unresolved, if anything>
- **Main chat next move:** <one concrete action or “No action needed; retain as context.”>
```

Do not add a bootstrap prompt, working-copy inventory, generic next steps, or authority section unless it changes the next move.

## Finish Cleanly

After the block, say it is ready to paste. Do not create, fork, message, or alter another task or save a file unless explicitly requested.
