# User-Approved Handoff

Read this reference only after the user explicitly authorizes messaging, authorizing, or sending feedback to the referenced task, or explicitly asks for managed coordination.

A task reference is context to inspect, not permission to contact the task. A favorable verdict is an assessment for the user, not a worker authorization. Until the user explicitly approves a handoff, complete the review in the current conversation and make no call that messages, prompts, authorizes, or otherwise directs the referenced task.

After explicit approval, act as the controller: review, decide, and send precise instructions; let only the worker task edit its working copy and commit. Never have the reviewer and worker edit the same working copy concurrently. Approval to hand off does not authorize a push unless the user explicitly includes that push in the approval.

Use these checkpoint markers in handoffs and task updates:

`PLAN_READY` → `PLAN_APPROVED` → `BUILD_READY` → `ACCEPTED` → `COMMITTED` → `PUSHED`

Record the reviewed plan or commit revision with each checkpoint. Do not re-review an unchanged revision or repeat an already-completed action. Treat a **cycle** as one plan review or one completed-work review followed by one worker response. Stop after three unresolved cycles or 90 minutes, whichever comes first.

Once a user-approved handoff is active, prefer event-driven coordination: have the worker send the reviewer a message when it reaches a checkpoint, requests a decision, or encounters a failed check. Use a scheduled reviewer check only as a fallback when the user has explicitly asked to set up a managed loop. Do not create a recurring automation merely because this mode is named.

Approve routine actions only when all of the following are directly verified:

- the change remains within the requested outcome and intended files;
- no customer or production data write, migration, bulk update, deletion, credential/secret change, auth or billing change, permission change, or production configuration change is involved;
- required validations pass, with no unresolved material failure or skipped acceptance check;
- the working tree contains no unrelated changes being swept into the commit;
- the commit is narrowly scoped and the branch, upstream, and remote are the expected ones;
- any proposed push has separate explicit user approval, is a normal non-force push, and is not known to trigger a deployment or release.

Before relaying a user-approved routine push, independently verify the diff, validation evidence, commit contents, target branch, upstream, and remote. After it completes, verify that the expected commit SHA is present on the remote branch. State clearly whether deployment verification remains outside scope.

Interpret `required validations` as the user-requested and proportionate checks above. Do not promote optional integrity work into an acceptance gate without meeting the broader-validation rule.

Stop for a user decision immediately on any hard stop: force push or history rewrite; protected-branch or remote divergence problem; merge conflict; migration; bulk or customer-data write; deletion or destructive command; secret, credential, permission, billing, or auth change; production configuration, deployment, or release; a material scope change; a failed material check; contradictory requirements; or an unknown branch/remote effect.

User-approved handoff is a workflow decision boundary, not a bypass of the app's action-safety permissions. Respect any approval prompt or sandbox restriction that still applies.
