# Comment Monitor

Workflow rules version: `1`.

Own recurring observation of discussion on existing Signal to Noise cards.
Read the [definition](../../definition.md), [editorial standard](../../editorial.md),
[common workflow](../../../workflow.md) and [refresh task](refresh.md).
The monitor checks and proposes; it does not edit pages or scores.

Supply the exact existing Index/cards, an eligible Comment Monitor identity,
inherited mode, invocation deadline, server publication times, current page and
evaluation receipts, and shared HN retrieval budget/cache. Evaluation creation
requires Index write authority. Setup defines a dedicated restricted personal
Agent; missing identity/grants must be reported, never replaced silently by the
editor's identity or a new broadly authorized Agent.

Run once per host invocation for active cards, selecting at most five existing
cards across monitor/editor maintenance combined. Prefer overdue +24h/+72h work,
then least recently observed active discussions, with stable card-ID tie breaks.
Use original publication times; stop at the fixed +72h window except its one
allowed late final pass. Existing cards can leave the Best 10 and still be
monitored. New story selection remains strictly within the current Best 10.

An owner-configured host schedule supplies check opportunities at its chosen cadence;
this prompt installs no timer and does not resume paused jobs. No perpetual
monitoring or catch-up guarantee while the Mac sleeps. Closed cards require an
explicit bounded follow-up.

In edit mode create revision-linked evaluations for actual material changes,
new limitations or completed no-change checks. Reuse matching same-invocation
checks; do not emit repeated evaluations for identical observed thread evidence
and unchanged scope/rules within a checkpoint. Save only sparse observation
bindings when needed to establish that reuse. If no new evaluation is saved,
retain the actual latest observation time in a sparse optional remote checkpoint
so least-recently-observed selection advances. If that receipt cannot be retained,
create the scoped no-change evaluation instead. Missing prior timing means
unknown/oldest coverage, never an assumed recent check. A new mandatory +24h/+72h checkpoint
needs its own actual source observation. Report mode returns an unsaved draft.
No automatic evaluation closure, page logs, grants or resource creation.

For remote README discovery, linked-file reads and guarded checkpoints, follow
[remote workflow setup](../../../setup.md#store-and-run-remote-workflows).
