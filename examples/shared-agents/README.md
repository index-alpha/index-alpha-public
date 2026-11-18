# Shared Agents

Reusable workflows live outside any one Index. Index examples link here instead
of copying prompts.

| Agent | Purpose | Entry point |
| --- | --- | --- |
| Fact-checker | Check consequential claims, references and uncertainty | [Start here](fact-checker/README.md) |
| Markdown formatter | Apply shared style while preserving content/evidence | [Start here](markdown-formatter/README.md) |

```text
examples/
  shared-agents/
    README.md
    completion.md
    fact-checker/
      README.md
      review.md
    markdown-formatter/
      README.md
      style.md
      format.md
```

Follow [common rules](../workflow.md) for run inputs, inherited mode, platform-first
state and host sequencing, and [completion.md](completion.md) before new work.
Pass current tool results, scoped coverage and source snapshots between roles in
memory. Recover ordinary facts from Indexes, content and revisions; there is no
required local ledger or Agent-local state store. Optional sparse receipts and
text checkpoints use `common/state/<agent-id>/<index-id>/`. Downloaded binary evidence stays with the host.

A full run follows primary author, fact-checker, formatter, author disposition,
then Signal Ranker where applicable. Shared tasks rerun for changed relevant
inputs or explicit rechecks. Reviewers propose factual or reference changes as
revision-linked evaluations. The primary author applies accepted corrections under the common
Signal score gate. Formatters commit style changes and record compliant no-change
checks as evaluations. Pass actionable findings to the primary author, who
closes verified findings when the invocation authorizes closure. See
[completion.md](completion.md) for exact revision binding, reuse and disposition.
The host owns maintenance-cycle completion.

"Shared" means reusable across supplied Indexes; platform `connection_mode: open`
is separate. Personal Agents initially serve their authorized owned Indexes.
Cross-account work, when explicitly requested, needs the relationships and authority described in
[Agents and access](../../skills/index-alpha/references/agents-and-access.md).
Folder placement creates no identity, grant or scheduler.

Keep private evidence scoped to its account/Index. Never store credentials or
upload tickets, copy private material between Indexes, or treat cached hints as
current authorization. Use the [maintained skill](../../skills/index-alpha/SKILL.md).

For remote README discovery, linked-file reads and guarded checkpoints, follow
[remote workflow setup](../setup.md#store-and-run-remote-workflows).
