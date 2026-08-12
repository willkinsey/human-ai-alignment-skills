---
name: questions-for-context-brain-dumps
description: Create an easy-to-speak set of open-ended questions that helps a user record a rich, transcribed context brain dump about a topic, problem, decision, or idea. Return a focused recording aim and 8–16 spacious questions; do not research, answer the questions, draw conclusions, make a proposal, edit files, or advance a project workflow.
---

# Questions for Context Brain Dumps

## Get Context

1. Use the topic and any notes, constraints, audience, stakes, or context the user supplied.
2. Treat supplied notes as material to explore, not facts to validate or conclusions to endorse.
3. If the input is thin, use broad questions. Do not ask follow-up questions before creating the guide.
4. Stay read-only. Do not research, solve the topic, or start a specialized workflow such as business planning, coaching, diagnosis, or advice.

## Build the Questions

- Return 10–14 questions by default; use 8 for a narrow topic and up to 16 only when the supplied notes contain several distinct threads.
- Make every question one sentence, open-ended, and easy to scan or speak from. Each should leave room for roughly five minutes of speaking.
- Use the user's vocabulary. Do not repeat points already fully covered in the notes; use them to find gaps, tensions, examples, and alternatives.
- Move from broad context to concrete experience, then possibilities, tradeoffs, and reflection. Cover relevant areas such as:
  - why this matters now;
  - what is actually happening;
  - useful history or experience;
  - affected people and perspectives;
  - confusion, risk, or uncertainty;
  - assumptions;
  - examples and counterexamples;
  - unexplored options or interpretations;
  - tradeoffs and second-order effects;
  - what would clarify the picture;
  - what now feels important; and
  - what remains open.
- Avoid compound questions, yes/no wording, forced choices, leading questions, and questions that demand a plan, title, recommendation, or final answer.
- Do not request sensitive information. When the topic implies personal, work, health, legal, financial, customer, credential, or private third-party material, add one privacy note that asks the user to use placeholders and leave out identifying details.

## Return This Exact Shape

```markdown
## Brain-Dump Prompt
[One sentence describing what this recording is meant to explore.]

## Questions
1. [Open-ended question]
2. [Open-ended question]
...

[Only if needed: Privacy note: Speak in placeholders; leave out names, account details, customer information, and anything you would not want in the transcript.]
```

Give no introduction, answers, analysis, or closing recommendation. The question list is the recording guide.
