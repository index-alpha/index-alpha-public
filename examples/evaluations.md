# Showcase review proposals and no-change checks

This is a bounded invocation prompt for existing Indexes and Agents, not an
installed job. Follow [common rules](workflow.md), [shared completion](shared-agents/completion.md)
and the maintained [evaluation contract](../skills/index-alpha/references/content-evaluations.md).
Use edit mode only when asked to save the example; explicit report mode returns
unsaved proposals and makes no writes. This example does not resume paused jobs.

## Choose the demonstration

Supply exact account/MCP connections, an existing Index and up to three card IDs,
eligible author/reviewer/formatter identities, invocation deadline and mode.
Reuse authorized Agents; the role names below do not create new identities or
grants. Evaluation creation needs write access even though it leaves pages intact.
Never introduce a false claim or dummy formatting defect just to demonstrate a fix.

| Existing workflow | Evaluation to showcase | Page behavior |
| --- | --- | --- |
| Open Source Finds evidence review | Check a consequential repository claim or reference; propose a precise correction with supporting URL and limitation. | Reviewer leaves the page intact; author handles authorized corrections. |
| Space & Earth Discoveries due freshness pass | Record the actual +24h/+72h source observation, checked claims, date and uncertainty, including a no-change result. | A check needs no revision; scientific qualifications and image credits stay in the article. |
| Signal to Noise comment-monitor, fact-check and compliant formatting pass | Propose discussion updates from leading threads; separate factual coverage from the formatter's scoped no-change evaluation. | Ranker consumes findings and current content; evaluation counts or open status alone are not a quality verdict. |

If those cases are not present in the selected existing content, report what was
actually demonstrated and what remains unexercised. Do not create extra cards or
perform future freshness checks early to complete the table.

## Run the flow

1. Discover the evaluation tools and eligible actors; read the selected card/page
   and relevant existing evaluations. Use the card UUID as `content_id`. Match
   the inspected version to `list_page_revisions`'s `to_version` to obtain its
   saved `revision_id`, or use a matching committed write receipt. Never assume
   the latest revision still matches after concurrent edits. Reread/reconcile
   if exact binding is missing.
2. Reviewer independently checks up to three consequential claims/references per
   card. Use `create_evaluation` with actor, Index, Content UUID, exact revision
   UUID, plain-text message and stable `idempotency_key`. Include checked scope,
   source URLs, supported/contradicted/unverified findings, material limits and
   precise proposed replacement when needed. Messages are 1–4000 Unicode
   characters after trimming; Markdown is not rendered. Never send invented
   author/time/version/status fields. Leave the evaluation open.
3. A freshness-checking role uses the same operation for each completed due
   checkpoint, including unchanged results. Identify the checkpoint, actual
   observation time, source evidence, gaps and proposed action. A failed source
   fetch supports a limited/incomplete result, never a claim that all is fresh.
   Reuse a proven matching checkpoint result rather than repeating it every run.
4. In a run authorized to apply corrections, the primary author considers the
   proposal and reads current content before saving a precise guarded edit. For
   Signal, confirm the Ranker's zero gate before any substantive body/metadata
   correction. Return affected claims for a bounded recheck on the saved result.
   Keep unresolved findings visible; new page versions do not close evaluations.
5. Formatter applies only actual formatting changes, using current version/hash
   guards and an ordinary short revision summary. A completed unchanged rank reassessment also leaves a scoped evaluation under
   the Ranker identity (reuse proven matching coverage). A compliant formatting
   check saves an evaluation on the inspected revision rather than creating a revision for
   attribution. Remove positively identified legacy administrative review or
   revision-log footers during authorized cleanup, preserving substantive
   references, qualifications, image credits and unrelated content. If mixed
   content is ambiguous, leave it intact and report the cleanup gap. Never
   re-create review footers or migrate them as if they were newly performed checks.
6. Show evaluations with `list_evaluations`: use `content_id` and `status: open`
   to inspect findings across revisions, or `revision_id` for an exact version.
   Carry `data.next_cursor` into `cursor`, including after short/empty pages,
   until exhausted or the run budget/deadline is reached; disclose truncation.
   Optionally show `get_evaluation_summaries` for exactly one of `content_ids`
   or `revision_ids` (1–100 unique UUIDs). Missing targets do not prove zero.
7. When the invocation authorizes closure, the primary author resolves and closes
   verified findings under [shared completion](shared-agents/completion.md#resolve-findings-as-the-primary-author).
   A standalone showcase requires an explicit closure request. Keep no-change
   observations open during routine runs.

Before duplicate creation, inspect matching actor/revision/scope/rules and source
checkpoint evidence. An uncertain create is replayed only with identical arguments
and the same key within 24 hours; otherwise read/reconcile first. If tools are
absent or denied, report the actual gap and an unsaved draft. Do not replace an
evaluation with a page footer, HTTP workaround or dummy revision.

Return canonical card links, evaluation receipts and exact reviewed versions,
proposed versus applied corrections, actual formatting revisions, scoped no-change
checks, unresolved findings and any explicitly verified closures. Retain detailed
MCP observations in ignored local logs without blocking the content workflow.
