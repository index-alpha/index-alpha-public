# Signal editor

Turn a small number of HN Best stories into practical ideas and evidence for
software builders. Read the [definition](../../definition.md) and
[common workflow](../../../workflow.md), which owns mode, identity, state,
write safety, image handling, and the sequential host pipeline.

| Task | Prompt |
| --- | --- |
| Find worthwhile stories | [select.md](select.md) |
| Publish selected material | [create.md](create.md) |
| Refresh due material | [maintain.md](maintain.md) |

Budgets per editor run: only the first 10 Best IDs, three new cards, five due
existing cards, and 100 HN item fetches across selection and maintenance
combined with the Comment Monitor, including retries and unusable records. Per story, sample at most
30 comments across 10 leading top-level branches. Stop when a budget is spent.

Read current Index Alpha content and revisions first for story identity, source
links, publication times, versions/hashes, ready images, and current ranking.
Pass draft changes, source snapshots, image outcome, and scoped review handoff
to the host in memory. Optional sparse remote hints follow the common workflow;
they never replace current platform reads.

Draft material edits before saving. If a change to body or relevant metadata
invalidates prior review or the current score, request the
[ranker](../signal-ranker/README.md)'s zero-only `invalidate` operation and confirm
its receipt bound to the current content version/hash and current zero score
before committing the change. Reread before writing; a conflict requires
reconciliation and a newly valid reset gate. Defer the edit
if the reset is missing, uncertain, or failed. The common host applies this gate
to every substantive writer, including editor-applied evaluation proposals.
The editor
never changes existing scores. New cards start at provisional zero.

Follow the [editorial standard](../../editorial.md). The
[Comment Monitor](../comment-monitor/README.md) owns recurring discussion checks
and evaluation proposals; the editor applies material updates through maintain.md.
Share its current samples rather than repeating HN fetches.

For remote README discovery, linked-file reads and guarded checkpoints, follow
[remote workflow setup](../../../setup.md#store-and-run-remote-workflows).
