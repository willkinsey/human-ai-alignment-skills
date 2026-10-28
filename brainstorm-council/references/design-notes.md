# Design Notes

## Agreed Design

The author requested three independent GPT-6 Luna brainstormers reporting to the primary session. The primary session may select one proposal intact or combine two or three. The agreed personas are practical, inventive, and first-principles thinkers. Each generates complete ideas; their emphasis encourages variety without requiring artificial disagreement.

The default is one parallel brainstorming round followed by primary-session synthesis. Peer review and debate are optional responses to a demonstrated gap, not mandatory stages. Native subagents avoid a separate service, API credentials, or a new application.

## Sources Reviewed on October 16, 2026

- [Qubica LLM Council skill](https://github.com/Qubica/llm-council/blob/main/SKILL.md): A close skill-shaped example using five thinking styles, independent responses, anonymous peer review, and chairman synthesis. Borrow the shared neutral brief and distinct perspectives. Omit its mandatory peer-review round, broad triggers, and pressure to lean into an extreme perspective.
- [Karpathy LLM Council](https://github.com/karpathy/llm-council): Independent responses from different models, anonymized ranking, and chairman synthesis. Useful conceptual precedent; its author describes it as an unsupported exploratory project. Our same-model council does not reproduce its model diversity.
- [Microsoft AutoGen Mixture of Agents](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/mixture-of-agents.html): Concrete worker-and-orchestrator implementation with parallel collection and critical synthesis. Borrow the orchestration shape without adding multiple refinement layers or a framework dependency.
- [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents): Describes parallelization for multiple perspectives and orchestrator-worker synthesis. Supports the general pattern, not a claim that three Luna agents are optimal for creativity.
- [Ueda et al., Exploring the Design of Multi-Agent LLM Dialogues for Research Ideation, SIGDIAL 2025](https://aclanthology.org/2025.sigdial-1.26/): Reports diversity benefits from varied personas in research ideation experiments. The tested dialogue setups differ from this skill; they do not establish that our exact personas or model consistently outperform one session.

## Practical Limits and Next Validation

Different prompts on the same model can still produce overlapping ideas and shared mistakes. Independence, distinct emphases, explicit tradeoffs, and primary-session judgment address these risks without treating consensus as evidence. Combining proposals is useful only when the result is coherent and stronger than the best standalone option.

Initial validation covers skill structure, metadata, references, and inspection of the delegation instructions. The first live trial is intentionally left for the first real request. In that trial, check that exactly three Luna workers run independently, their reports offer meaningfully different options, and the primary session explains a defensible selection or synthesis. Adjust the skill based on observed behavior rather than adding speculative process.
