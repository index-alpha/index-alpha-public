# Invalidate or rank signal

Use the [ranker entry point](README.md), [definition](../../definition.md), and
common [workflow](../../../workflow.md). Process supplied cards within the
invocation budget/deadline and inherited mode. The host owns maintenance closure.

## Invalidate before editing

1. Read the current card and proposed material change. This zero-only operation
   needs no full article/comment research or component scoring.
2. In edit mode, confirm the current content version/hash. `get_card` and
   `get_cards` omit numeric ranking fields. Use an applicable same-run ranking
   receipt or `get_index_card` for the exact destination appearance's `score`.
   A missing score or unavailable appearance
   does not establish zero. If already confirmed zero, record the observation
   without another score write. If nonzero or still unknown,
   use a scoped idempotent ranking write under the Ranker's identity to commit
   provisional zero; do not scan the whole Index. Bind the committed receipt to
   the current content and pending change before releasing the writer's edit;
   that receipt establishes the gate without mandatory readback. Defer the edit
   if the reset is uncertain or failed. A changed version/hash requires
   reconciliation and re-establishing the gate.
3. Return the target, pending draft/change, reset receipt, confirmed zero, and
   next review/rank stage to the host in memory. Optional sparse remote hints may
   retain uncertain keys/arguments or an otherwise non-observable binding to
   the current content. If interrupted or uncertain, reconcile the pending reset
   before the writer commits. A successful
   reset without a subsequent edit remains provisional zero for safe resume.
   Report mode returns a proposed reset and draft only; it authorizes no write.

The editor and shared reviewer never perform score writes. The common host
applies this gate to every substantive writer before body or relevant metadata
changes invalidate prior review or a current score, including when the old
content already has complete review.

## Rank current reviewed material

1. Read the current card/page and shared fact-checker's scoped claims, coverage,
   and revision-linked evaluations with cached evidence/source snapshots. Read
   evaluation messages and exact revision coverage rather than inferring a verdict
   from open/closed counts. A no-change evaluation starts open too; it is not an
   adverse finding. Unresolved consequential factual proposals require author
   resolution and applicable review before a positive score. Review must cover the essential claims
   supporting the current takeaway and material qualifications. The reviewer
   defaults to three consequential claims per card; if essential coverage needs
   more, request a bounded extension or keep provisional zero with the gap.
   Do not omit a material claim merely to fit the default budget.
   Formatting alone preserves unchanged claim evidence; old versions do not
   automatically cover substantive changes.
2. Follow the [editorial standard](../../editorial.md) when returning any
   reader-facing rationale: no named-user quotes, invented comment votes or
   community-wide consensus from a sample. Use cached article evidence and discussion samples. Do not routinely refetch
   the original article or comments. If a specific gap matters, request targeted
   review or make an optional bounded probe for that gap; otherwise report it.
   An inaccessible article can support a reviewed discussion-only card only
   after unsupported article claims are removed or resolved through the writer
   gate. Never infer unread contents or consensus from sampled comments.
3. Score covered material out of 100 using the rubric below. Return a compact
   four-component breakdown, sum, concise reasons/limits, and supporting source
   or comment references; avoid long per-component essays.

| Component | Maximum | Evidence to assess |
| --- | ---: | --- |
| Relevance | 35 | A specific software-building decision, technique, or tradeoff; clear audience and conditions. |
| Evidence | 30 | Primary results, inspectable examples, reproducibility, and honest limits; distinguish anecdotes. |
| Novel insight | 20 | An illuminating mechanism, counterexample, or synthesis beyond a familiar headline. |
| Useful discussion | 15 | Substantive experience, technical corrections, and rebuttals, with sampling limits. |

Use zero through each component maximum. Votes, views, HN points, reply volume,
and API order cannot replace the reasons. Missing discussion earns no invented
points. A current essential claim without applicable review keeps the total at
`0`, status `provisional`; that fallback is not a negative quality judgment.

4. In edit mode, use `set_index_card_score` or `set_index_card_scores`
   with common current-state/idempotency/recovery rules. Skip unchanged normal
   ranking writes when confirmed by an applicable same-run receipt or the bounded
   score lookup above. A completed reassessment needing no score change records
   a scoped `create_evaluation` on the exact reviewed saved revision under
   [shared completion](../../../shared-agents/completion.md), with score/rubric,
   checked coverage and limits. Reuse matching proven coverage instead of making
   a duplicate; report mode returns an unsaved draft. A prerequisite `invalidate`
   zero confirmation alone is not a completed rank reassessment. Never edit
   card/page content for rationale or score labels.
5. Return current/reviewed versions, scoped coverage, component points, concise
   rationale, references, provisional/reviewed status, and receipt or proposal
   to the host in memory. A ranking-only write creates no content revision;
   optionally retain a sparse receipt binding the ranking to reviewed content
   when the association is not recoverable from platform evidence. Read numeric
   rank through the bounded lookup above or an applicable same-run receipt,
   never from remote hints. If a checkpoint binding is missing, reconstruct available
   evidence and recompute the reviewed score once when needed;
   the last revision actor alone does not prove full coverage. Do not write
   status-only cards or dummy revisions to persist workflow progress. Return
   unprocessed targets and gaps. During the final +72-hour pass, use the
   invocation deadline and report stage completion; only the host records final
   closure or `closed_incomplete`.
