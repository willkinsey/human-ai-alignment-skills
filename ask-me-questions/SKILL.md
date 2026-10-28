---
name: ask-me-questions
description: Ask up to five tailored, decision-changing questions before proceeding with a proposed approach. Use when the user invokes $ask-me-questions and clarification could materially change the work.
---

# Ask Me Questions

Before proceeding, run this gate when the current context leaves a material
decision unresolved.

1. Form a broad internal candidate set spanning objectives, assumptions, constraints, alternatives, risks, success criteria, and decision authority.
2. Remove duplicates and questions whose answers would not change the approach.
3. Select up to five questions with the greatest expected effect on scope, sequencing, design, risk, cost, reversibility, validation, or ownership.
4. If one to five material questions remain, ask only those questions. Tailor each to the current proposal and known context, then wait for the answers before endorsing the approach or taking the gated action.
5. If no material question remains, state that no clarification is needed and proceed. Never pad the set to reach five.

## Question Standard

Make every question:

- Specific to the plan, decision, and available evidence.
- Decision-oriented: explain the concrete choice, tradeoff, boundary, or owner it clarifies.
- Material: an answer should plausibly change the proposed approach.
- Answerable without asking the user to rediscover information already available in context.

Avoid generic discovery questions, repeated questions, implementation trivia, and questions with no meaningful effect on the recommendation. Do not show the internal candidate set, ranking, or selection rationale unless the user asks for it.

## Format

When material questions remain, open with one short sentence stating that the answers will determine the recommended approach. Then present a numbered list of only those questions, up to five. Do not include a plan, recommendation, additional questions, or an implied extra question in the same response. When none remain, state that no clarification is needed and continue with the proposed work.

If the user has already supplied an answer, treat it as settled context rather
than asking again. If an answer remains unclear, do not repeatedly re-ask it:
state the unresolved decision and use the narrowest safe assumption when the
task can continue safely; otherwise stop at that gate.
