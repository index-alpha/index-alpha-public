# Revision-Linked Content Evaluations

Use this workflow to read or leave review messages and manage their open/closed
state. Discover the connected tools first; an older connection may expose none
of them. Report that gap and provide an unsaved draft if useful. Do not substitute
an HTTP call or a content edit for a missing evaluation operation.

## Authority And Revision Selection

Select an eligible Agent with `list_agents`; every evaluation tool requires its
`acting_agent_id` and the target `index_id`. Reading, summaries, and private
reporting require Index read authority. Creating and closing require current
Index write authority. Evaluations are visible to Index readers, so keep private
material out of messages on public Indexes.

Use the card's UUID as `content_id`, not its slug or `custom_id`. Assess the body from `get_page`/`get_pages` or complete current same-run evidence. Reuse a committed receipt's `data.revision.revision_id` when its `to_version` and `target_hash` match the assessed body/version. Otherwise use `list_page_revisions` to locate that matching saved revision; a version number is not a revision UUID. Do not assume the latest history row still matches after concurrent edits. Replay can return another writer's latest revision; check the receipt's facts. If no matching saved revision can be identified, reread/reconcile before creation.

Page-write receipts contain revision headers and file summaries, not unified diff text. Use `get_page_revision` only when the retained per-file changes are needed. It is not a full historical snapshot or restore operation; if only a change-set was assessed, state that scope rather than claiming to have read the full historical page. Recording an evaluation stores your assessment; it does not run an evaluation engine, edit the page or create a Content revision. Reviews are not compulsory after saves.

The server derives the content version, evaluator Agent, and timestamp. Do not
send caller-invented author, version, timestamp, or status fields. An evaluation
remains attached to the reviewed revision even when newer content exists.

## Create And Leave Open

`create_evaluation` requires `content_id`, `revision_id`, `message`, and an
`idempotency_key`, in addition to actor and Index. The message is plain text,
1–4000 Unicode characters after outer whitespace is trimmed. State the finding
and supporting evidence clearly; Markdown is not rendered.

```json
{
  "tool": "create_evaluation",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "content_id": "33333333-3333-4333-8333-333333333333",
    "revision_id": "44444444-4444-4444-8444-444444444444",
    "idempotency_key": "finding-42-source-check-v8",
    "message": "The cost estimate omits storage charges. Verify the provider's storage pricing before using this total."
  }
}
```

Creation returns the saved evaluation under `data`, including `evaluation_id`,
`content_id`, `revision_id`, `content_version`, `agent_id`, `created_at`, `message`,
`status`, and nullable `closed_at`, `closed_by`, `close_reason`. New evaluations
are `open`. Leave one open by making no closure call. Multiple evaluations from
the same Agent on the same revision are allowed; avoid accidental duplicates by
replaying an uncertain create only with identical arguments and the same key
within 24 hours. Otherwise read/reconcile before another mutation.

## Read, Filter, And Summarize

- `get_evaluation`: actor, Index, and `evaluation_id`; returns `data` as above.
- `list_evaluations`: optional `content_id`, `revision_id`, evaluator `agent_id`,
  `status` (`open`, `closed`, `all`; default `all`), `version_min`, `version_max`,
  `limit` (default 50, max 100), and `cursor`.
- To inspect one Content's findings across revisions, supply `content_id` without
  `revision_id`; add `status: "open"` for open findings. Omit both identity filters
  for an Index-wide list. `agent_id` filters authors, independently of the actor.
- For one exact revision, use `revision_id`. Positive int64 version bounds require
  `content_id` and cannot accompany `revision_id`; when both bounds are supplied,
  `version_min` must not exceed `version_max`. Preserve integer precision.

```json
{
  "tool": "list_evaluations",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "content_id": "33333333-3333-4333-8333-333333333333",
    "status": "open",
    "limit": 50
  }
}
```

Lists return `data.items`, `data.limit`, and `data.next_cursor`. Pass the exact
non-null continuation into input `cursor`, retaining the query filters. Continue
even after a short or empty page: bounded scanning can omit unavailable targets
while still returning continuation. Do not substitute `after_token`/`next_token`.

For counts, `get_evaluation_summaries` takes exactly one of `content_ids` or
`revision_ids`, with 1–100 unique UUIDs in the chosen array:

```json
{
  "tool": "get_evaluation_summaries",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "content_ids": ["33333333-3333-4333-8333-333333333333"]
  }
}
```

`data.items[]` includes Content identity, revision identity/version when requested,
`counts.total`, `counts.open`, `counts.closed`, and up to three recent evaluator
IDs with their latest evaluation ID/time. Content summaries span revisions;
revision summaries describe only that revision. Unavailable targets are omitted,
not zero-count proof. Use returned counts for readable evaluations, not an
assumption that retained or cached card metadata equals current visible totals.

## Close Explicitly

Use `close_evaluation` for an exact finding within the closure scope the user
authorized directly or through a workflow. Read its message and revision,
inspect the relevant evidence, and leave other findings open. A newer content
version alone does not establish that a finding was fixed.
Any currently authorized writer may close, including an Agent other than the
author. Optional `reason` is plain text, at most 1000 Unicode characters after
trimming; omitted, null, or blank means no reason.

```json
{
  "tool": "close_evaluation",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "evaluation_id": "55555555-5555-4555-8555-555555555555",
    "reason": "Verified the revised estimate includes the cited storage charges."
  }
}
```

Closure is keyless and state-idempotent. Repeated closure returns the original
stored actor/time/reason without overwriting them. After an uncertain result,
read `get_evaluation` and reconcile before another call; do not add a request key.
Report the committed `status` and closure facts without claiming every closure
means fixed. Messages cannot be edited; closure is terminal, with no reopen or
individual delete tool. If follow-up is needed, create a new evaluation on the
appropriate reviewed revision within the user's scope.

## Private Reporting

For requested abuse reporting, use `flag_evaluation` with the observed `open` or
`closed` surface. `reason` is one of `spam`, `harmful`, `misleading`,
`rights_violation`, `other`; optional `details` is at most 2000 characters.

```json
{
  "tool": "flag_evaluation",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "evaluation_id": "55555555-5555-4555-8555-555555555555",
    "observed_status": "closed",
    "reason": "spam",
    "details": "The observed message and closure contain repeated advertising."
  }
}
```

This keyless operation returns a private report receipt and deduplicates by
reporting account, evaluation, and observed surface. A closed-surface report
covers the message plus closure. Reporting leaves lifecycle and visibility
unchanged. Quarantine and restoration belong to trusted moderation workflows;
Agent tools do not expose those actions. After uncertainty, reread the target
and reconcile the report before resubmission.

Evaluation receipts have no canonical evaluation link. Present an already-returned page link and the assessed version when useful; do not invent evaluation/revision URLs or imply the current page opens the historical revision.
