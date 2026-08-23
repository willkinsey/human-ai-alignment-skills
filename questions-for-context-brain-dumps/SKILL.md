---
name: questions-for-context-brain-dumps
description: Create an easy-to-speak set of open-ended questions that helps a user record a rich, transcribed context brain dump about a topic, problem, decision, or idea. Return a focused recording aim and 8–16 spacious questions; do not research, answer the questions, draw conclusions, make a proposal, edit files, or advance a project workflow.
---

# Questions for Context Brain Dumps

## Get Context

Use the supplied topic, notes, constraints, audience, and stakes. Treat notes as material to explore, not validated facts or conclusions. If input is thin, use broad questions without asking follow-ups. Stay read-only: do not research, solve the topic, or start another workflow.

## Build the Questions

- Return 10–14 questions by default; use 8 for a narrow topic and up to 16 only when the supplied notes contain several distinct threads.
- Make each question one sentence, open-ended, easy to speak from, and spacious enough for roughly five minutes of reflection.
- Use the user's vocabulary. Explore gaps, tensions, examples, and alternatives instead of repeating covered points.
- Move from context to experience, possibilities, tradeoffs, and reflection. Explore what matters now, relevant history, affected perspectives, uncertainty, assumptions, examples, options, consequences, needed clarity, and open questions.
- Avoid compound questions, yes/no wording, forced choices, leading questions, and questions that demand a plan, title, recommendation, or final answer.
- Do not request sensitive information. For personal, work, health, legal, financial, customer, credential, or private third-party topics, add one note requesting placeholders and no identifying details.

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
