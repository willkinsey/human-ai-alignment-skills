---
name: watchdog
description: Monitor another Codex task, thread, or session on a repeating heartbeat and stop it if clear evidence shows unauthorized, destructive, unsafe, or grossly off-course behavior. Use when the user says watchdog, watch, babysit, supervise, keep an eye on, check every few minutes, or repeat a heartbeat until a specified Codex task completes.
---

# Watchdog

Supervise one existing Codex task without managing or redirecting its work.
Default to a two-minute cadence and continue until the watched task completes,
is stopped, or the user cancels monitoring.

## Notify on Attention-Needed Issues

When an observed `STOP_REQUIRED` or recoverable `BLOCKED` condition needs the
user's attention, invoke `$ntfy-me` once with a concise, safe summary of the
evidence and the immediate state. Notification delivery is separate from
monitoring: do not include private task content, retry a failed delivery, or
send duplicate alerts for the same unchanged issue.

Immediately after the notification attempt, re-read the watched task. Keep the
heartbeat active only when the task is still continuing (`PROGRESSING` or
`WAITING`) and a later check could add value. Disable it when the task has
stopped, completed, or been interrupted. A notification never authorizes
coaching, redirecting, restarting, or otherwise changing the watched task.

## Durable Controller Gate

Use a **chat heartbeat attached to a separate, durable primary Codex task**.
Never use a side chat, ephemeral controller, watched task, or
automation-created wrapper. Before scheduling, verify the controller appears in
task discovery as a normal Codex task and its recent turns are readable. If the
current context cannot meet both checks, report `BLOCKED` and tell the user to
invoke Watchdog from a standard primary task; do not create a schedule or
silently substitute a standalone scheduled task.

After creation, prove all three before calling the watch active: the heartbeat
is active at the requested cadence; the controller remains readable and
durable; and the first follow-up heartbeat re-entered that controller and
inspected the exact watched-task ID. If that cycle has not appeared after one
cadence plus reasonable scheduling allowance, disable the heartbeat and report
`BLOCKED`. Read the [watch procedure](references/watch-procedure.md) for the
durable setup and terminal handling details.

## Observe, Do Not Direct

Resolve the exact target ID and read its newest state, thread-local user
instructions, active turn, and recent actions before creating the watch and on
each heartbeat. The newest target instruction is authoritative. Classify state
as `PROGRESSING`, `WAITING`, `COMPLETED`, `STOP_REQUIRED`, or `BLOCKED`.
Silence, elapsed time, slow tests, reasonable alternatives, ordinary diagnosed
errors, and plausible external waits are not failures.

Treat task status and turn status as different layers. `idle`, a completed turn,
a finished delegated subtask, a safe checkpoint, an approval wait, or a handoff
back to a coordinating task is not proof that the overall watched outcome is
complete. The newest instruction governs the target's current work, but it does
not redefine the Watchdog's terminal boundary. When coordination messages or
tool outputs carry the target's instructions, include enough recent turns and
output content to read them; do not make a terminal decision from a one-turn
summary that omits that evidence.

Use `COMPLETED` only when fresh evidence explicitly shows the overall watched
outcome is terminal and successful. Before disabling for completion, re-read the
target and confirm that evidence still holds. If the target may receive another
delegated turn, the broader outcome is unfinished, or the evidence is
ambiguous, classify `WAITING` and keep the heartbeat active.

## Stop Only on Concrete Evidence

Use `STOP_REQUIRED` only for wrong repository/task/customer/item/environment;
unauthorized mutation; destructive or credible data-loss risk outside explicit
authority; credential/security or prohibited sensitive-data handling; conflict
with the newest instruction or mandatory approval; gross divergence from the
outcome; or repeated material failure without diagnosis or progress. When
ambiguous, keep observing.

If stopping is required, re-read the newest target state immediately, use the
thread interruption control with exactly `/stop`, and never coach, redirect,
repair, restart, fork, replace, or continue the target. Disable the heartbeat,
confirm resulting state before claiming it stopped, notify the user as required
above, and report the evidence.
Never create more than one active heartbeat per target/controller, broaden
permissions, or treat liveness or the target's self-assessment as proof.
