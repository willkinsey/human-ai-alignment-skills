---
name: plain-language
description: Write or rewrite an answer in clear, everyday language without losing material facts, caveats, uncertainty, status, decisions, approval gates, or required actions.
---

Write the relevant output in plain language.

Choose the direction from the user's request:

- If the user refers to a prior reply, rewrite that reply so it is easier to understand.
- If the user asks for plain language in a new request, create the requested output in plain language from the start.

In either case:

- Give the bottom line or requested artifact first. Put any decision, approval, or required action near the top in a separate `Decision needed:` or `Approval needed:` block; do not bury it in supporting detail.
- Keep every material fact, caveat, uncertainty, limitation, status, blocker, decision, approval gate, and required action. Shorten wording, not substance.
- Preserve the difference between `Observed`, `Likely`, `Proposed`, `Approved`, `Blocked`, and `Unknown`, and between completed, proposed, unapproved, and not-done work. Keep explicit no-change, no-send, and no-attachment statements.
- Never turn a possibility into a confirmed finding, a candidate into a recommendation, or a proposal into completed or approved work. Do not strengthen a recommendation while simplifying it.
- Use short, everyday wording and explain unavoidable technical terms once.
- Omit only background or options that cannot affect a decision; keep relevant tradeoffs and alternatives.
- Use bullets or short headings when they make decisions, caveats, and next steps easier to scan.
