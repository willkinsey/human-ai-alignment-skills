---
name: screenshot-feedback
description: Turn visual feedback into a testable review packet, then make and visibly verify only revisions the user explicitly authorizes.
---

# Screenshot Feedback

Use `$screenshot-feedback` to review or revise a slide, diagram, image, PDF page, video frame, animation, or dashboard. A screenshot is preferred, not required: accept an image, file/page, open-app view, or notes.

Default to review-only. Invocation or an attachment never authorizes edits.

## Orient

Identify the target/version, requested mode (`review only` or `revise`), and supplied evidence. Treat callouts as feedback, not final artwork. If a needed change is unclear, ask one focused question. Do not infer hidden content or intent from a partial image.

## Review Packet

Return a compact packet containing:

- **Target and evidence** reviewed.
- **Observed** issue(s), distinct from inference.
- **Requested changes**, prioritized and concrete.
- **Keep unchanged**, including user-named protected elements.
- **Visual acceptance checks** for a revision.
- **Unknown:** one decision only when it blocks a safe revision.

Use plain visual language: position, spacing, size, alignment, contrast, crop, hierarchy, motion, or legibility. Preserve the user's wording and creative judgment; do not replace it with a generic style preference.

## Authorized Revision

Revise only after the user explicitly asks to revise, fix, update, or make the changes. Protect the original and use the appropriate artifact-specific workflow. Make only approved changes; do not publish, upload, share, overwrite an original, or change unrelated content.

After a revision, render, reopen, or inspect the updated artifact at a useful size. Report what changed, what stayed unchanged, and whether each acceptance check passed, failed, or remains unverified. Do not claim visual verification from source code or a change summary alone.

If the artifact may be shared publicly, flag visible private, customer, personal, credential, or copyrighted material for sanitization; do not disclose or publish it.
