# Maintain a fixed discussion window

Use the [editor entry point](README.md) and common
[workflow](../../../workflow.md). Process at most five due existing cards in
one inherited mode using platform reads and host-supplied run context. Also
consume in-window discussion proposals from the Comment Monitor between fixed
source checkpoints; those do not reset or satisfy +24h/+72h source checks.

1. Read current cards/pages, server `created_at`, revisions, evaluations, and available scoped
   completion evidence for the +24-hour interim and +72-hour final checks. Use
   optional remote hints only for facts the platform cannot show. Missing checkpoints
   require reconstruction and normally a bounded recheck of ambiguous work;
   the last revision actor alone never proves full review coverage or closure.
   Common rules govern missing timing, fixed clocks,
   coalesced overdue observations, and the one allowed late closing invocation.
   The host owns closure after review, formatting, and ranking complete, or
   records `closed_incomplete` at the run deadline. Supply downstream roles
   the invocation deadline so a due final pass can finish.
2. Use the [Comment Monitor](../comment-monitor/README.md)'s current observation,
   evaluations and sample, requesting its bounded refresh if absent. Do not repeat
   its HN retrieval. Both roles share at most five existing cards and 100 HN item
   fetches per invocation, with at most 30 comments across ten branches per story.
   Refresh the linked article only as needed for a due source check or a concrete
   new factual claim. If evidence disappeared, disclose and reassess it.
3. For a due interim/final source check, record a separate exact-revision freshness
   evaluation including unchanged results, under the maintained
   [evaluation contract](../../../../skills/index-alpha/references/content-evaluations.md).
   State checkpoint, actual observation time, checked sources, gaps and proposed
   changes. Reuse proven same-checkpoint coverage; +24h is not +72h. An interim
   Comment Monitor observation alone does not prove the due source check happened.
   Report mode returns unsaved drafts. Leave evaluations open and never add logs.
   Draft only material changes: new evidence, useful counterexamples, corrected
   claims, meaningful context, or clearer source limits. Include relevant
   title/subtitle/source changes in the proposed diff. Avoid activity trivia
   and claims of consensus from repeated sampled opinions. Apply the
   [editorial standard](../../editorial.md) when revising the page. Keep the
   opening H1 in sync with the card title and put the two-sentence introduction
   before the key takeaway. Update evidence, discussion synthesis and practical
   consequence in place. Omit individual user names and retain the HN
   comments-section link. A failed fetch supports an access note, not an
   invented update.
4. Before saving a draft that invalidates prior review or the current score,
   request Ranker `invalidate`. Require its confirmed current-zero result or
   committed reset receipt for this content before saving body or metadata,
   following the common score gate. On failure/uncertainty, retain the pending
   draft and next action in host memory, optionally retaining an interrupted
   handoff in sparse remote hints, and defer the edit. Reconcile a changed version
   before proceeding. The same gate covers material corrections proposed in evaluations and applied by the editor.
5. If an image is absent and a bounded in-window attempt is due, follow the
   [image workflow](../../../images.md). When the story links to an article, try
   the article's `og:image` first. Place a new image after the takeaway as the
   first managed image. Apply the prepared draft through the common
   current-read/version/write protocol, preserving stable identity,
   first-publication time, ready images, and unrelated edits. Skip unchanged writes.
6. Hand changed current claims and versions to the shared
   [fact-checker](../../../shared-agents/fact-checker/README.md), identifying
   essential claims covering the takeaway and qualifications. Use its default
   bounded budget or record missing coverage for an explicit extension.
   Earlier review applies only where coverage still holds. The host proceeds
   through [formatting](../../../shared-agents/markdown-formatter/README.md)
   and [ranking](../signal-ranker/README.md) in order with cached evidence.

Return actual observation time, changed/unchanged outcome, versions, scoped
review coverage, reset receipt or pending handoff, and image limits to the host
in memory. Use optional sparse remote hints only for non-observable completion
or interruption facts; do not add status-only cards or dummy revisions. Existing
scoped evaluations, meaningful references and human-readable revision summaries may
support reconstruction within their stated scope. Report remaining due work
and incomplete stages. The editor never changes existing scores or closes
maintenance itself.
