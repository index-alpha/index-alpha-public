# Create selected cards

Use the [editor entry point](README.md), [selection](select.md), and common
[write protocol](../../../workflow.md). Create at most three cards per run;
do not fill a quota. Use the inherited mode and host-supplied run context.

1. For each confirmed-new `hn-story-<id>`, draft a specific title and concise
   subtitle exposing the practical idea. Set `source` to `Hacker News`. Link
   `https://news.ycombinator.com/item?id=<id>` and the article separately.
   Follow the [editorial standard](../../editorial.md). Open the Markdown with
   the exact card title as its H1, a two-sentence introduction, and the key
   takeaway. Follow with concrete evidence, discussion synthesis with strongest
   dissent, practical implication, and Sources and scope. Aim for 200–400 words.
   Surface the useful tradeoff in a declarative title/subtitle and avoid clickbait.
   Summarize leading ranked threads without quoting or naming individual users.
   Link the story's comments section and original source separately. Use nuanced,
   frank language proportional to the evidence; do not invent a consensus.

2. Keep article claims, discussion claims, and inference distinct. If the
   article was unreadable, label the card's discussion-only scope clearly.
   For every selected HN story with an article URL, try the original article's
   `og:image` first. Reuse selection's cached article HTML when available and
   follow the [image workflow](../../../images.md) to find and validate a usable
   image within its attempt budget. Do not search for affirmative reuse permission
   or skip solely because permission is missing or unclear; honor an explicit
   source request not to reuse the image.
3. Reconfirm absence through the common candidate-resolution/write protocol.
   In edit mode, prepare any usable image through the managed upload workflow.
   Place its returned Markdown destination immediately after the takeaway as the
   first managed image so it becomes the card preview. Record the image outcome
   and use the text-only fallback if the image cannot be finalized.
   Use `create_card` in edit mode with the stable custom ID and provisional
   `custom_score: 0`. Return the receipt and current content to the host in
   memory. Recover first publication from server `created_at`; common rules
   derive fixed +24-hour interim and +72-hour final checks. Preserve an uncertain
   write's key/arguments in optional sparse remote hints when needed and reconcile
   the creation before advancing the pipeline.
4. Hand current content, versions, and essential claims needing
   review to the shared [fact-checker](../../../shared-agents/fact-checker/README.md).
   Identify claims supporting the takeaway and material qualifications. Use the
   default bounded review budget or record a coverage gap; do not hide essential
   claims to fit the budget. The host then runs the
   [formatter](../../../shared-agents/markdown-formatter/README.md) as needed
   and [ranker](../signal-ranker/README.md) using the same evidence cache.

Return drafts or saved canonical links/receipts, source and image limitations,
and review handoff. The editor does not award scores beyond initial zero.
