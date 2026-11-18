# Open Source Finds

Useful open source projects and consequential releases, verified against project-owned sources. Start in your selected account with a private Index and three qualified cards;
subsequent runs create at most three. These prompt files install no runtime.

Read the [definition](definition.md), [setup](../setup.md), and authoritative
[common workflow](../workflow.md), then use the
[curator entry point](agents/open-source-curator/README.md). Common rules govern inherited
mode, writes/recovery, images, pipeline order, and maintenance closure.

Supply exact account/actor/Index, task, current UTC time, invocation deadline,
and host-resolved target cards plus in-memory run context/evidence between roles.
Read Index Alpha first for Index/card IDs, UI/visibility, source URLs and known
custom IDs, `created_at`, current versions/hashes, ready managed images, and
revision attribution/summaries and revision-linked evaluations. Card reads return
object-shaped content metadata
and `custom_id` when present; verify identity against returned IDs and source links.
For initial private setup, follow the common setup procedure.

Remote persistence is optional: a logical `state_dir` may use
`common/state/<agent-id>/<index-id>/` for owner-private text checkpoints. Use one sparse `run.json` only for facts the platform cannot
show, such as uncertain write keys/arguments, unsaved report outcomes, interrupted
closing attempts, or aliases not recorded in content. Text evidence caches may share this remote directory. Binary images remain temporary host assets under the image procedure. No runtime file is assumed to exist.
Without it, discover server targets, recover publication clocks, and run bounded
checks for unknown completion; do not reset clocks or assume completion.

Inspect at most 15 fixed candidate identities, create at most three cards, or
maintain at most five due cards per invocation. Report a shortfall instead of
extending discovery to fill a quota. Creation uses qualified supplied candidates;
maintenance uses platform facts and exact existing targets. Return canonical
links, changes/proposals, unchanged/rejected/deferred items, source/image gaps,
and remaining due work under the common workflow's stop/recovery rules.

Pass created or materially changed cards, this definition, in-memory run context,
source cache/evidence, inherited mode, and the invocation deadline to the shared
[fact-checker](../shared-agents/fact-checker/README.md), then
[Markdown formatter](../shared-agents/markdown-formatter/README.md).
The host reports closure after the ordered pipeline, including incomplete stages;
retain only non-observable outcomes in optional remote state. Do not create
status-only cards, dummy revisions, or run ledgers in card pages.

Freshness and fact/reference checks save scoped revision-linked evaluations,
including unchanged outcomes; findings propose changes for the author. Formatting
may revise pages. Checks never append page-bottom review/revision logs.

For remote README discovery, linked-file reads and guarded checkpoints, follow
[remote workflow setup](../setup.md#store-and-run-remote-workflows).
