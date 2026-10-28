---
name: use-jev
description: Consider and use Jev for authorized bounded decisions, especially repeated decisions in scheduled or recurring workflows, or diagnose Jev/OpenRouter access. Use for structured ranking, scoring, classification, and routing when a stable decision contract exists; do not use for open-ended research or to bypass the owning workflow.
---

# Use Jev

Jev is useful for a small decision with explicit facts, choices, and bounds. Do
not turn open-ended research or a consequential action without a defined
decision contract into a Jev request. This skill improves routing and failure
diagnosis; it does not grant network access or permission to disclose data.

## Consider Jev for Recurring Decisions

When designing or reviewing a scheduled task, automation, or other recurring
workflow, explicitly consider Jev if the same bounded judgment will be made
repeatedly. It is often a useful decision layer after a language model or other
process gathers the relevant state and before deterministic code routes the
result.

Jev is a strong candidate when:

- the decision repeats against a stable text schema;
- the answer is a fixed choice, a yes-or-no claim, or a describable ordered
  scale;
- the result will drive ranking, triage, routing, escalation, or whether more
  review is needed; and
- speed and per-decision cost matter enough to favor a focused typed judgment
  over a general-purpose reasoning response.

Do not add Jev when deterministic code can establish the answer exactly, when
the work requires open-ended research or generated explanation, when the
rubric changes materially on each run, or when the required payload is not
authorized for the external destination. Fast or inexpensive operation is a
reason to evaluate Jev, not a reason to relax testing, permissions, or user-owned
approval gates.

For a scheduled workflow, keep the Jev client, question schema, choices or
rubric, confidence handling, retry behavior, and audit location in durable
project instructions or code. Test the decision contract manually before
scheduling it. Do not assume a future scheduled session will infer the Jev
integration: name this skill or the owning Jev client explicitly in the saved
automation prompt.

## Keep the Owning Workflow in Charge

Identify the task's Jev client, packet schema, approval gates, owning retry
rules, and audit location before calling Jev. Do not invent a session retry
limit. Do not reuse a workflow's packet or audit log
for unrelated decisions. For another use case, require its own defined choices
and authority boundary rather than inventing a universal packet format.

## Keep Jev Out of Healthy Deterministic Execution

Do not insert Jev between a deterministic command and its completion. A
running process with its own pacing, retry, checkpoint, and circuit-breaker
logic has no decision for Jev to make. Logs that look unusual, sparse output,
or a worker's concern are reasons to inspect, not reasons to interrupt.

Use Jev only after the deterministic process exits or exposes a defined branch
that code cannot resolve. If Jev selects automatic deferral, make the deferral
real with the owning workflow's heartbeat or scheduler and stay quiet while
the underlying condition is unchanged.

## Check Before Transmitting

- Identify the actual destination and the exact categories of data the request
  would send. Minimize the packet and remove identifiers and secrets unless the
  owning workflow explicitly permits them.
- Check whether the user's request and governing permissions authorize that
  external transmission. If authorization is missing or a permission review
  rejects the call, stop and ask for the exact destination and payload-category
  approval. Do not retry through a browser, another endpoint, a scheduled job,
  or another tool to evade a denial.
- Validate the packet locally first when the client supports it. A local
  configuration check may establish that a key is present, but does not prove
  that the key works or that external transmission is authorized. Never print
  the key or copy it into a packet, log, or chat.

## Design Questions Jev Can Answer Reliably

Choose the primitive that matches the answer space: use `Score` for an ordered
spectrum, `Choice` for fixed unordered options, and `Noul` for a yes-or-no
claim. Jev accepts text input, including strings and text in JSON objects or
arrays; it does not evaluate images, audio, or video directly.

For a `Score` question:

- Ask about one dimension at a time. Split a complex judgment into independent
  questions and combine their results with explicit logic and weights in code.
- Use only as many ordered levels as can be described distinctly. The API
  accepts 2–10 levels; three to five is often enough, but the descriptions—not
  a preferred count—should determine the scale.
- Describe concrete situations rather than numeric labels or vague degrees.
  Jev sees each level description, not the level number or neighboring levels.
- Treat the returned score as a probability-weighted position that may fall
  between levels. Read the probability distribution and confidence alongside
  it; confidence describes how concentrated the distribution is, not whether
  the answer is guaranteed correct.
- Normalize each score by `len(criteria) - 1` before combining scales with
  different numbers of levels. Keep weights and hard gates in deterministic
  code. A derived 0–100 index is a ranking measure, not a success probability.
- Test the rubric on representative examples with known expected outcomes.
  Add structured examples to level descriptions only when they improve results
  on separate test inputs; higher confidence alone does not prove correctness.

See TypeSafe's official [Score guidance](https://docs.typesafe.ai/primitives/score)
and [question-design guidance](https://docs.typesafe.ai/introduction) when
designing or revising a scoring contract.

## Diagnose the Failure, Then Retry Only Within Bounds

Treat DNS, timeout, and connection errors as connectivity evidence, not bad
credentials. If sandbox isolation is plausible, retry the same authorized
check or call with the required network permission once, provided the payload
and destination are permitted. A permission rejection is a stop, not a reason
to find an alternate route. Treat an explicit authentication rejection as a
credential problem; do not log out, rotate, or replace credentials without
separate authority. Distinguish rate limits, unavailable service, invalid
model, and invalid packet/response from both of those cases.

Use the owning workflow's retry and idempotency rules. Do not duplicate an
external write when the previous result is uncertain. Authorized idempotent
reads may be retried under the owning workflow's pacing, challenge, checkpoint,
and source-window rules.
Validate Jev's returned choice against the defined choices; preserve the
decision evidence in the owning workflow's approved location. Never silently
substitute this session's judgment for a required Jev decision, and never use
Jev to approve an action reserved for the user.

Report separately what is configured, what connected, what was authorized,
and whether a valid decision was obtained. Name the single next safe action
when any of those checks fails.
