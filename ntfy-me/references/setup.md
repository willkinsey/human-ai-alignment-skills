# Setup

`ntfy-me` supports macOS and uses the built-in Keychain to keep the ntfy topic out of repository files and shell history. It does not require the ntfy command-line tool.

## Subscribe on a Phone

In the ntfy app, subscribe to a long, hard-to-guess topic on `ntfy.sh`, then allow notifications for the app. Treat the topic like a password: anyone who knows an unprotected topic can publish to or subscribe to it.

## Save the Topic in Keychain

In Terminal, run the following command. Type the topic when prompted; it is not shown or saved in shell history.

```zsh
read -s NTFY_TOPIC
printf '\n'
security add-generic-password -a "$USER" -s codex-ntfy-topic -w "$NTFY_TOPIC" -U
unset NTFY_TOPIC
```

## Verify Delivery

From the installed `ntfy-me` skill folder, run:

```zsh
scripts/notify_ntfy.sh \
  --title "Codex test" --tags white_check_mark --message "ntfy is configured"
```

The script sends one HTTPS request to `https://ntfy.sh`. A successful command is silent; a nonzero exit or a `Notification failed` message means delivery was not confirmed.

## Allow Codex to Reach Keychain and ntfy

A Terminal test can succeed while a Codex task fails inside its restricted sandbox. When Codex invokes the helper, it must request outside-sandbox execution for that command so it can read macOS Keychain and reach `https://ntfy.sh`.

The task should request permission with a narrow explanation such as: `Allow one explicitly requested ntfy notification using the configured macOS Keychain topic.` A sandboxed Keychain or network failure is not proof that setup is missing. Retry such a blocked call once with the required permission, then stop if the permitted call fails.

## Use in an Automation

Add an explicit instruction such as: `At the end, invoke $ntfy-me once with a concise result.` The skill does not send merely because it is installed.
