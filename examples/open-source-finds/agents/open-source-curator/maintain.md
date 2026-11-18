# Maintain due cards

Read the [definition](../../definition.md) and [common workflow](../../../workflow.md).
Use platform facts, host-resolved targets/run context, current UTC time, and
invocation deadline; mode carries through all requested stages.

1. Take at most five due exact cards, earliest due first with stable card ID as
   tie-breaker. Recover first-publication time from server `created_at` before
   dependent work. Missing remote state does not prove completion; edits and
   reviews never reset the +24h interim/+72h final schedule.
2. Coalesce missed checks into one current inspection. At/past +72h, perform
   one final pass with the actual observation time; never fabricate a historical
   snapshot. The host closes only after the ordered pipeline finishes, including
   an honest incomplete outcome if a stage fails or the deadline ends the run.
3. Read current card metadata/full page and the relevant primary sources for
   consequential corrections, withdrawals, or clarified claims. Do not run code,
   chase every patch release, or replace the card's topic.
   Save/reuse same-run source/HTML evidence. If relevant inputs are unchanged,
   skip shared tasks only when the common completion preflight proves them
   satisfied from current versions/hashes, scoped evaluations, revision evidence, and
   available run context. If completion is unknown, do the ordinary bounded
   check; do not invent a completion marker or dummy revision.
4. Record the freshness check through `create_evaluation` under the checking
   Agent in edit mode, even when no update is needed. Follow the maintained
   [evaluation contract](../../../../skills/index-alpha/references/content-evaluations.md):
   bind the exact read version to its saved revision, use a stable request key,
   and state interim/final checkpoint, actual observation time, sources checked,
   findings/limits and precise proposed corrections in plain text. Reuse a saved
   evaluation only when it proves this same checkpoint and scope; a +24h check
   does not satisfy +72h. Report mode returns an unsaved evaluation draft.
   Leave evaluations open; a new revision is not proof of resolution. Never
   append a review/revision log or make a no-change page revision.
   Primary-author edits may apply concrete proposals under inherited mode and
   the common current version/recovery rules. Preserve title, `source`/`sub_title`,
   added references, managed images/credits, and unrelated edits. Keep valid
   images; for a materially wrong image or credit use the shared image procedure
   for supported correction/replacement or an explicit text-only fallback.
5. Pass source outcomes/cache, actual check times, current versions/receipts,
   image status, changed inputs, and remaining due work in memory. Keep useful
   evidence/credits in card content and ordinary summaries when already editing.
   Route materially changed cards to shared fact-checking then formatting with
   exact cards, this definition, inherited mode, run context/evidence, and
   invocation deadline (even when the maintenance cutoff has passed).
   Shared roles do not close the card.
6. After the pipeline, the host reports the interim outcome/next due time or
   final closure and any incomplete stages. Optional sparse `run.json` retains
   non-observable report outcomes or interrupted closing attempts; no
   status-only cards, dummy revisions, or page run ledgers. Return linked
   changes/proposals, unchanged/deferred items, missed checks, and evidence gaps.

Stop at five cards, invocation deadline, end of due list, or unresolved failure
under the common workflow. Closed cards need a separately requested correction.
