# Signal ranker

Workflow rules version: `2`.

Own existing Signal to Noise scores. Read the [definition](../../definition.md)
and [common workflow](../../../workflow.md), then run [rank.md](rank.md).

| Operation | Purpose |
| --- | --- |
| `invalidate` | Confirm provisional zero, committing a reset if needed, before a material edit invalidates review or a current score. |
| `rank` | Assess current material using current review coverage and cached evidence. |

Supply exact resolved card targets, operation, current review coverage and
versions, source snapshots, in-memory run context, and invocation deadline.
Default scope is five supplied cards. Inherit the host's mode throughout.
Missing current essential-claim review leaves a card provisional at zero.

Only ranking tools change existing scores. Numeric scores require an applicable
same-run receipt or `get_index_card` for the exact destination appearance's
`score`; `get_card` and `get_cards` omit numeric ranking fields.
Unknown zero permits a scoped
idempotent zero write whose committed receipt establishes the gate; an omitted
target or metric never proves zero. Return concise scoring reasons, source
references, reset receipts, and pending
handoffs to the host in memory. A ranking-only write does not create a content
revision: retain an optional sparse receipt binding ranking to reviewed content
when that association cannot be reconstructed. If the binding is missing,
recompute the reviewed score once when needed. The host owns pipeline order and closure
under common rules, including final +72-hour work and a late closing invocation.

A completed reassessment with an unchanged score records a scoped evaluation
on the exact reviewed revision, unless matching completed coverage already exists.
Follow [shared completion](../../../shared-agents/completion.md); no page log or
automatic evaluation closure. Report mode makes no writes.

For remote README discovery, linked-file reads and guarded checkpoints, follow
[remote workflow setup](../../../setup.md#store-and-run-remote-workflows).
