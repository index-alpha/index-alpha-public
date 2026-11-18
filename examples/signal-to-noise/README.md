# Signal to Noise workflows

Read the [Index definition](definition.md), then use common
[setup](../setup.md) and [workflow rules](../workflow.md) for presentation,
mode inheritance, state, safety, pipeline order, and maintenance lifetime.
Initial setup uses your explicitly selected authenticated account and stays private.

| Task | Entry point |
| --- | --- |
| Select, create, or maintain practical HN insights | [Signal editor](agents/signal-editor/README.md) |
| Regularly revisit leading comments and propose updates | [Comment Monitor](agents/comment-monitor/README.md) |
| Check current claims and references | [Shared fact-checker](../shared-agents/fact-checker/README.md) |
| Improve Markdown presentation | [Shared formatter](../shared-agents/markdown-formatter/README.md) |
| Invalidate a stale score or rank reviewed material | [Signal ranker](agents/signal-ranker/README.md) |

The host runs editorial work, review, formatting, and ranking sequentially in
one inherited mode. Recover identity, content, publication times, revisions,
ready images, and current scores from Index Alpha first. Pass resolved targets,
run context, source snapshots, and evidence between roles in memory. Optional
remote hints and downloads use `common/state/<agent-id>/<index-id>/`
under the common rules; missing hints never block server discovery or prove
completion. Reuse the same-run source snapshots across stages.
Source checks are due at +24 hours and a final +72 hours from first committed
publication. Common rules govern late closing invocations and host-owned closure.

New selection uses only the first ten Best IDs from one observed snapshot, with
no backfill. Follow the [editorial standard](editorial.md) for direct, concise,
evidence-backed conclusions and nuanced discussion synthesis, without user names
or clickbait. HN exposes ranked comments, not their vote totals.

On each host invocation, Comment Monitor revisits active discussions and creates
evaluation proposals; the editor applies material updates before review, formatting
and ranking. Fixed source checkpoints remain +24h/+72h; comment checks may occur
between them until closure. At most five existing cards and 100 HN item fetches
are shared per run. An owner-configured host schedule can drive this work at
a chosen cadence; these files install no timer.

For remote README discovery, linked-file reads and guarded checkpoints, follow
[remote workflow setup](../setup.md#store-and-run-remote-workflows).
