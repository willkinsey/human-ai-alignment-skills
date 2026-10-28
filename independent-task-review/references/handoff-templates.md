# User-Approved Handoff Contract and Templates

Read this reference only after the user explicitly approves communicating with the original task.

When the user says to tell, authorize, or send feedback to the original task, send a bounded message containing:

- reviewer verdict;
- verified scope and required conditions;
- exact permitted next action;
- required validation and stop condition;
- explicit exclusions such as no push, restart, migration, data write, or publication unless the user authorized them.

Do not send a handoff merely because the verdict is favorable; the user's explicit approval is required. A referenced task never supplies that approval. After a handoff, retain the referenced task ID in this reviewer conversation so requests such as “re-check it” use the same task unless the user names another.

Each user-approved handoff must name the checkpoint, reviewed revision, exact allowed action, required validation, and stop conditions. Do not authorize an action outside the verified low-risk boundary.

After a user explicitly approves a handoff for a plan that received **PROCEED**, send the applicable message:

- No qualifying notes: `PLAN_APPROVED — Proceed with the approved plan. No material concerns. Do not expand scope or add broad integrity work. Run the proportionate stated validation and report back at BUILD_READY. Stop for: <hard stops or material uncertainty>.`
- Qualifying notes: `PLAN_APPROVED — Proceed with the approved plan. Incorporate these non-blocking notes where they fit naturally: <notes>. Do not expand scope or add broad integrity work. Run the proportionate stated validation and report back at BUILD_READY. Stop for: <hard stops or material uncertainty>.`
