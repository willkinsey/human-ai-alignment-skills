---
name: ntfy-me
description: Send one concise Codex job notification to a configured ntfy topic on macOS. Use when an automation or explicitly requested workflow needs a completion, failure, or attention-needed push notification; do not use for chat, bulk messaging, or unapproved outbound communication.
---

# Ntfy Me

Use this skill only when the calling workflow explicitly asks for an ntfy notification. It does not create a topic, subscribe a device, or send a message merely because the skill is available.

## Configure Once

This skill currently supports macOS. Read [the setup instructions](references/setup.md) before the first send or whenever Keychain configuration is missing. The topic is a bearer-like secret: keep it out of repository files, automation prompts, command output, and Git history.

## Use From a Workflow

When an automation needs notification, include an explicit instruction such as:

> At the end, invoke `$ntfy-me` once. Send a concise result to the user: state whether the job completed, needs attention, or failed; include counts and the next action when useful. Do not include private source material, credentials, or a long report. If sending fails, report that separately and do not repeatedly retry.

Finish and validate the underlying work first, then send one message. A successful job and a successful notification are separate outcomes.

## Message Guidance

- Use a short title such as `Codex: Daily Brief Complete` or `Codex: Review Needed`.
- Keep the body to the result, important count, and next action; target fewer than 500 characters.
- Use `white_check_mark` for completion, `warning` for attention needed, and `x` for failure.
- Use ntfy priority `default` unless the user has explicitly requested a different urgency. Do not use `max` for ordinary job completion.
- Do not send customer data, personal data, secrets, full document contents, raw logs, or unsafe local paths.

## Helper Interface

Run the bundled `scripts/notify_ntfy.sh` from the installed skill folder with:

```text
--message TEXT       Required notification body
--title TEXT         Optional notification title
--priority LEVEL     min, low, default, high, or max; default: default
--tags TAGS          Optional comma-separated ntfy tags
```

Use one invocation per notification. The helper sends through `https://ntfy.sh`, validates its inputs, and returns a nonzero status when it cannot send. Do not bypass it with an unreviewed URL or a different topic.

## Failure Handling

If Keychain lookup, validation, or the HTTP send fails, surface `Notification failed` with the safe error summary. Do not claim delivery, expose the topic, or start repeated retries. The calling workflow remains responsible for deciding whether its primary job succeeded.
