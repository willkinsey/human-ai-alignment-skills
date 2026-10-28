# Watchdog Procedure

Read this reference when creating a watch, writing the heartbeat prompt, or
handling a heartbeat result. The entrypoint's durable-controller, first-proof,
stop-only, fail-closed, and teardown gates always apply.

## Establish the Watch

1. Resolve the exact target task/thread ID. Use the user's ID. If none is
   supplied, select a task only when discovery yields one unambiguous target;
   otherwise ask for the ID.
2. Read the target's latest state, newest user instructions, active turn, and
   recent actions before creating the watch. The newest thread-local user
   instruction is authoritative; never expand its scope or invent requirements.
3. Verify the Watchdog controller is a separate, durable primary task. If it is
   not, stop with `BLOCKED`; do not create a monitor or substitute a standalone
   scheduled task.
4. Create or update one heartbeat attached to that controller. Name it
   `Watchdog — <short target ID>` and avoid duplicates. Use the requested
   cadence, otherwise two minutes.
5. Put the target's full ID, this invocation, and required terminal cleanup in
   the heartbeat prompt so every wake has durable instructions.

## Inspect Each Heartbeat

Read the target's current state before deciding anything. Use:

- `PROGRESSING`: coherent work within the latest authorized scope.
- `WAITING`: a plausible long command, test, external check, or approval.
- `COMPLETED`: a terminal successful result.
- `STOP_REQUIRED`: concrete evidence meets a stop condition.
- `BLOCKED`: the target cannot be reliably inspected or stopped.

Healthy silence, slow progress, ordinary diagnosed errors, a reasonable design
choice, long tests, and waiting for external results are not stop conditions.

Read enough recent turns, including relevant coordination-message or tool-output
content, to distinguish the overall watched outcome from the current turn. A
target can be `idle` because a delegated subtask ended while its coordinating
task prepares the next instruction. Likewise, a final answer that completes the
latest bounded assignment can still leave the watched build unfinished. Treat
those states as `WAITING`, not `COMPLETED`.

`COMPLETED` requires explicit, current evidence that the overall outcome named
by the watch is terminal and successful. Immediately re-read the exact target
before teardown. Keep the heartbeat active as `WAITING` when completion depends
on a coordinator, another delegated turn remains possible, unfinished work is
reported, or the evidence is otherwise ambiguous. Do not use elapsed time or
repeated idle snapshots as a substitute for completion evidence.

## Terminal Handling

- `PROGRESSING` or `WAITING`: send nothing and keep the heartbeat active.
- `COMPLETED`: after the required confirmation re-read, disable the heartbeat
  and report completion briefly.
- `STOP_REQUIRED`: stop the target only under the entrypoint's concrete-evidence
  rule, then invoke `$ntfy-me` once with a safe, concise alert. Re-read the
  target after that attempt and disable the heartbeat once it is stopped.
- `BLOCKED`: invoke `$ntfy-me` once when the limitation needs user attention;
  include only a safe summary. Re-read the target after that attempt. Keep the
  heartbeat only if it is still continuing and a later wake could reasonably
  recover; otherwise disable it.
- User cancellation: disable the heartbeat immediately and do not alter the
  watched task unless separately asked to stop it.

An ntfy delivery result does not change the target state. Do not retry a failed
delivery or repeatedly alert on the same unchanged condition; continue or end
the watch based on the post-alert target read.

When a first follow-up heartbeat has not appeared after one cadence plus a
reasonable scheduling allowance, disable the ineffective heartbeat and report
`BLOCKED`; never claim monitoring is continuing.
