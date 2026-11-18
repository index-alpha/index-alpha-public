# Index Alpha Workflows

Read only the relevant section. Examples are complete tool-invocation shapes checked against the effective schemas. Replace example UUIDs, account names, versions, and request keys with trusted current values. The surrounding host may expose tool names with a server prefix.

## Identity And Version Fields

| Field | Meaning and use |
| --- | --- |
| Canonical `card_id` / evaluation `content_id` | The source Content UUID. From an appearance use `source.card_id` with `source.index_id`; evaluation `content_id` uses that canonical UUID. |
| Appearance `index_id` / `card_id` | Destination inclusion/ranking identity returned by list/search/get_index_card and reference add; see [card references](card-references.md). |
| File `version` / `expected_version` | Opaque workspace version string, distinct from numeric Content versions; see [Agent workflows](agent-workflows.md). |
| `custom_id` | Optional lookup identity unique among active cards in one Index. Card metadata tools accept it; page tools need the returned `card_id` or `card_slug`. Creation remains create, not upsert. |
| `card_slug` and canonical links | Page selector and navigation supplied by the service. Agent/Index slugs are generated independently of names and immutable on rename; page slugs retain title-based behavior. Use returned links rather than constructing routes. |
| `revision_id` | UUID of one saved change. Match its `to_version` and `target_hash` to the assessed version/hash before recording an evaluation. A version number is not a revision UUID. |
| `version` / `base_version` | Current numeric Content version and required content-update conflict guard. Index metadata instead uses its returned Catalog `version` with optional `expected_version`. Preserve integer precision. |
| `content_hash` / `base_hash` | Content-state evidence and optional additional content-update guard; does not replace `base_version`. |
| `idempotency_key` | Identity of one logical write where required by schema. Identical-argument/same-key replay is bounded to 24 hours. It is independent of resource lookup identity. |

A recurring item can keep one `custom_id` across many edits, each with its own write key and current version. Changing a request key does not turn a duplicate create into an update. Resolve card lookup identity before body reads; retain full receipts between same-run steps when sufficient.

For including an existing public Index Alpha card, follow [card references](card-references.md) instead of copying its Markdown. For remote instructions and checkpoints, follow [Agent workflows](agent-workflows.md).

## Save To An Existing Index Or Create An Intended Collection

Normal signup supplies a personal Agent and private Index. Reuse the intended resources from trusted context after selecting an eligible actor through `list_agents`. When a writable destination is unknown, use `list_indexes(required_access="write")`; inspect only plausible candidates when names are ambiguous. An empty list or denied lookup is not permission to recreate resources.

For an ordinary save, prepare a complete card and use the `create_card` example below with the existing Index ID. Create an additional Index only when requested or clearly intended. Creation needs full write authority; a restricted actor may be able to edit an existing Index without being able to create one:

```json
{
  "tool": "create_index",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "idempotency_key": "research-index-create-2026-10-19",
    "display_name": "Research Notebook",
    "visibility": "private",
    "description": "Evidence and decisions for the current project",
    "custom_id": "project-research",
    "ui_defaults": {"default_view": "card", "default_sort": "new"}
  }
}
```

Use the intended existing Index UUID, or the returned UUID after an intended creation, for a useful standalone report. The custom ID and score below illustrate optional recurring/ranked content; omit them for a simple save when unnecessary:

```json
{
  "tool": "create_card",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "idempotency_key": "research-finding-42-create",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "custom_id": "finding-42",
    "title": "Decision and supporting evidence",
    "sub_title": "The recommendation and why it matters",
    "source": "Project research",
    "custom_score": 10,
    "markdown": "# Decision\n\nThe recommendation.\n\n## Evidence\n\n[Primary source](https://example.com/research)\n\n## Next steps\n\n- [ ] Verify the remaining assumption"
  }
}
```

Return the committed `data.card.links.content_url` and useful Index link. Use public visibility only when publishing is requested; follow privacy intent instead of turning a link-sharing request into public publication. The supported visibility values are public and private.

## Recurring Digests And Stable Identity

Use a durable Index and stable `custom_id` per logical item. Resolve existing cards with `get_card` or `get_cards`; create only confirmed-missing entries. A permission error or incomplete page is not proof that a card is absent.

For an existing item, change only what the task requires: summary with `update_card`, body with page tools, ranking with score tools. Each logical write gets its own stable request key. An uncertain create is replayed with its original key and identical arguments, not a new key just because a custom ID exists.

The skill does not schedule runs. Use the host's scheduling capability only if recurring execution was requested.

## Preserve Summary Fields During Updates

Use complete current summary evidence from `get_card` or a sufficient same-run receipt and retain current `source` and `sub_title` when changing the title. Supply the latest `version` as `base_version`, preserving its integer precision; optional `base_hash` comes from the returned `content_hash`.

```json
{
  "tool": "update_card",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "idempotency_key": "finding-42-summary-v7",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "custom_id": "finding-42",
    "base_version": 7,
    "title": "Updated decision headline",
    "source": "Project research",
    "sub_title": "The recommendation and why it matters"
  }
}
```

Omit a summary field only if clearing it is intended. Source URLs belong in Markdown links; do not add unsupported source/icon/comment/image fields to this call.

## Edit Markdown And Keep History

Use complete current body/version evidence from a sufficient same-run receipt, or read `get_page` with Index plus exactly one of `card_id` or `card_slug`. Resolve a known `custom_id` through card metadata to a returned card ID before reading its page. For selected multi-page reviews, optionally use discovered `get_pages`:

```json
{
  "tool": "get_pages",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "pages": [
      {"card_id": "33333333-3333-4333-8333-333333333333"},
      {"card_slug": "second-finding"}
    ]
  }
}
```

The batch limit is 10 pages and 1 MiB of returned UTF-8 Markdown, duplicates included; split on `LIMIT_EXCEEDED` or use single reads. Preserve each item's current body/version/hash for sequential guarded edits; the batch promises no cross-page snapshot. See the server map for item versus whole-call failures.

```json
{
  "tool": "patch_page_markdown",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "idempotency_key": "finding-42-risks-v8",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "card_id": "33333333-3333-4333-8333-333333333333",
    "base_version": 8,
    "summary": "Clarify the risk",
    "edits": [
      {
        "operation": "replace",
        "start_line": 3,
        "end_line": 3,
        "expected_text": "The recommendation.",
        "text": "The recommendation, with its known limitation."
      }
    ]
  }
}
```

Line coordinates refer to the original document for the entire atomic patch. Keep the resulting body non-blank. On conflict, reread/reconcile and use a new key for the changed request.

Each page body is limited to 256 KiB (262,144 UTF-8 bytes). Markdown supports headings, lists, blockquotes, fenced code, links, GFM tables/tasks/strikethrough/autolinks, footnotes, definition lists, emoji shortcodes, `[TOC]`, and heading anchors. Consult the server guide for current syntax. A useful report can include recommendation, evidence, caveats, and next steps without a fixed required template.

Keep optional page-write `summary` within 120 raw Unicode characters including whitespace before trimming, with no NUL. Use a short description; keep verbose scope/rules evidence in same-run context, with input hashes in guards. Reuse full successful mutation receipts for sequential role handoffs without compulsory rereads or history queries. Receipts contain the current page plus persisted revision actor/version/hash and file summaries, not body diff text; replay can return a later writer's latest revision. An unchanged replacement creates no revision, and a no-change patch is rejected; neither establishes fresh contribution.

Use `list_page_revisions` for revision headers and `get_page_revision` for retained per-file unified changes when needed. Revision detail is not a full historical page snapshot or a restore command; describe a change-set-only review as such. Revision changes cover structured content history; do not reconstruct authorship from display names when creator/contributor metadata is supplied.

For requested review findings attached to those revisions, read [content-evaluations.md](content-evaluations.md). Evaluations stay open until explicitly closed; editing the page does not close them.

## Publish Managed Images

1. Select an authorized actor and target Index. Reserve `count: 1..5` through `create_index_image_uploads` with a stable key.
2. For each uploadable reservation, POST to `upload.upload_url` as multipart/form-data with binary `file`, filename, and image MIME type. Never attach the Platform bearer.
3. For a new upload, before the original `expires_at`, save the exact `markdown_destination` in a Markdown image, for example `![Architecture diagram](media:<returned UUID>)`. New Content uses `create_card`; existing Content uses a versioned page mutation. Saving verifies/finalizes the upload. Already-ready images may be reused within the same Index after their original reservation expiry.
4. Report success only after the Content save commits. Use returned read-only delivery links for user-facing previews.
5. Removing an image reference from Markdown unlinks it from that Content. Ready images can be reused within the same Index. External image URLs and HTML image loading are rejected.

At most 20 image occurrences per Content body, duplicates included. A same-key reservation replay preserves original IDs/order/expiry and stored state; it cannot renew tickets or poll the provider. Do not upload on a ready replay. Replace an unusable reservation with a new logical request/key after reconciling its state.

If upload is unavailable in the host, explain the unfinished image step without exposing upload tickets or inventing an attachment operation.

## Rank And Inspect A Collection

Read candidate appearances with `list_cards` or `search_cards`, retain destination appearance IDs, then compute scores from the user's criterion. Use `get_index_card` for an exact current score; canonical card reads omit it. Use `score` for score-update calls (`custom_score` is the initial create field).

```json
{
  "tool": "set_index_card_scores",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "idempotency_key": "research-ranking-2026-10-19",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "scores": [
      {"card_id": "33333333-3333-4333-8333-333333333333", "score": 98},
      {"card_id": "55555555-5555-4555-8555-555555555555", "score": 91}
    ]
  }
}
```

The batch is atomic and returns ordered `data.items`. Explicit null clears a score; omission is invalid. Replay returns original score receipts, so read current state when needed. Read `list_cards(metric="custom_score")` when the user needs the resulting order. Distinguish the displayed subset from a total.

`search_cards` searches metadata rather than page Markdown. `include_total: true` requests the matching total. Use `get_page` for current body evidence and edits.

## Activity, Capacity, And Connections

- For changes to known cards, use `list_page_revisions` and `get_page_revision` with the canonical source identity. These provide retained per-card change history, not an Index-wide activity feed; do not infer missing actions from them.
- For capacity, call account tool `retrieve_account_capacity` with no actor. To request Index details, set `include_index_details: true`; use bounded `limit`, `after_token`, and display-name sorting. Do not promise remaining-capacity server sorting.
- For personal/open connection inventories, use actor-scoped `list_connections` with `connection_mode` and `owned` when relevant. Use `list_agents` to choose an eligible actor.
- `list_index_connections` requires an authorized owned source Index and current actor authority; connection display does not establish control.
- For explicit product-grant revocation and account/client distinctions, read [agents-and-access.md](agents-and-access.md).

## Deletions And Outcome Reporting

Resolve the exact target and current versions before requested deletion. `delete_card` requires `base_version`; `delete_cards` requires each item's version and is atomic. These keyless calls need state reconciliation after an uncertain result. Deleting an Index removes its retained contents, so do not use it as a duplicate-cleanup shortcut.

Prefer concise outcomes: created/updated title with returned content link, requested ranking with linked entries, or committed deletion/revocation scope. Do not emit raw envelopes, internal UUIDs, request keys, or upload URLs unless the user's task specifically needs machine data.
