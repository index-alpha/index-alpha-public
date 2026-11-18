# Index Alpha MCP Server Map

Reference snapshot: 2026-11-18. The connected server's exposed schemas and `platform://mcp/usage-guide` remain the runtime authority. This reference is self-contained; consumers do not need a backend checkout.

## Connection And Discovery

Streamable HTTP endpoint: `https://api.indexalpha.com/mcp`. Use the existing authenticated host connection. Do not replace a working connection automatically.

The service supports MCP `2026-07-28`, POST-only transport and modern discovery. Hosts must support that server contract. Browser OAuth authorizes an account/client relationship; actor selection is a separate operation.

Resources:

- `platform://mcp/usage-guide`
- `index://{index_id}/summary{?acting_agent_id}`
- `index://{index_id}/feed{?acting_agent_id,metric,limit,after_token}`
- `index://{index_id}/cards/{card_id}{?acting_agent_id}`

Every dynamic Index resource requires the acting Agent query argument. Prefer tools when the host cannot discover or read resources.

Prompts:

- `plan_index_setup`: required `goal`, optional `visibility` (`public` or `private`).
- `safe_batch_update`: required `operation` (`delete_cards`, `revoke_agent_grants_batch`, or `set_index_card_scores`), optional `batch_size`.

## Registered Tool Inventory

This reference lists 48 tools. Discover the connected server to verify availability and current schemas.

<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_START -->
- add_card_reference
- clear_agent_workspace
- close_evaluation
- create_agent
- create_card
- create_evaluation
- create_index
- create_index_image_uploads
- delete_card
- delete_cards
- delete_index
- delete_index_avatar
- delete_workspace_file
- edit_workspace_file
- flag_content
- flag_evaluation
- get_card
- get_cards
- get_evaluation
- get_evaluation_summaries
- get_index_card
- get_page
- get_page_revision
- get_pages
- list_agent_grants
- list_agents
- list_cards
- list_connections
- list_evaluations
- list_index_connections
- list_indexes
- list_page_revisions
- list_workspace_files
- patch_page_markdown
- read_workspace_files
- remove_card_reference
- retrieve_account_capacity
- retrieve_index_info
- revoke_agent_grant
- revoke_agent_grants_batch
- search_cards
- set_index_card_score
- set_index_card_scores
- update_agent_metadata
- update_card
- update_index
- update_page_markdown
- write_workspace_file
<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_END -->

## Public-Only Access

The tool inventory is not a public permission list. Only `retrieve_index_info`,
`list_cards`, `get_card`, `get_cards`, `get_page`, `get_pages`, and `get_index_card`
allow enabled public-only reads. Summary/feed/card resources share this policy.
Private or disabled targets need explicit authority. See
[public Index reads](public-index-reads.md) for arguments, source references and
request budgets. Public detail omits management capacity/upload/connection facts.

## Invocation Contracts

Account tools `list_agents`, `create_agent`, and `retrieve_account_capacity` forbid `acting_agent_id`. Workspace file tools and `update_agent_metadata` also forbid it, using explicit targets instead. All remaining tools require it.

The following writes require `idempotency_key`:

- `create_agent`, `create_index`, `create_card`, `create_index_image_uploads`, `create_evaluation`
- `update_index`, `update_card`, `update_page_markdown`, `patch_page_markdown`
- `add_card_reference`, `remove_card_reference`, `set_index_card_score`, `set_index_card_scores`, `revoke_agent_grants_batch`

Canonical deletion tools, workspace/metadata writes, single `revoke_agent_grant`, `close_evaluation`, and `flag_evaluation` are keyless. After uncertainty, read and reconcile even when an operation is state-idempotent. Key-bearing replay requires the same arguments/key within 24 hours.

### Indexes

- `create_index`: `display_name` (max 40), optional `description` (max 300), `custom_id`, `ui_defaults`, and `visibility` (`public` / `private`, default private). New Index belongs to the authorizing account; creation needs an included Agent with full write authority.
  Creation `ui_defaults` is a strict optional object: `default_sort` accepts `new` / `score`, and `default_view` accepts `list` / `card`. Omit the object or either field to retain defaults; null and unknown fields are invalid.
- `list_indexes`: authorized ID/name discovery, optional `required_access: read|write`, `limit`, `next_token`. It is not an owned/starred metadata catalog.
- `retrieve_index_info`: current metadata, counts, capacity, version, and links for one `index_id`. Detail/create/update Index responses expose a numeric int64 Catalog `version`; preserve the exact integer for `expected_version` without floating-point rounding.
- `update_index`: provided metadata fields only; optional `expected_version` guard. Null `description` clears it. `ui_defaults.default_sort` accepts `new` / `score` / null, `default_view` accepts `list` / `card` / null.
- `delete_index`: deletes the Index and its retained contents; resolve the exact requested target.
- `delete_index_avatar`: deletes the current avatar and returns deleted image IDs. This does not manage Content images.

### Cards, Pages, And Ranking

- `create_card`: required `index_id`, `title` (max 160), non-blank `markdown` (max 256 KiB / 262,144 UTF-8 bytes); optional `custom_id`, `source`, `sub_title`, `custom_score`. Managed images are embedded in Markdown.
- The browser app can display other stored card families and metadata. That does not add external-card creation, image ID attachment, comment metadata, or source-icon inputs to these MCP tools.
- Canonical card `content` is an object of metadata, not a string; appearance responses nest it under `source_card.content` when available. `custom_id` is returned when present.
- `get_card`: exactly one `card_id` or `custom_id`; returns metadata, authoritative version/hash, and links.
- `get_cards`: ordered batch of `cards` selectors in one Index; metadata only.
- `update_card`: exactly one `card_id` or `custom_id`, required `title` and `base_version`, optional `base_hash`. Optional `source` / `sub_title` are replaced or cleared by omission.
- `list_cards`: `metric` is `created_at`, `updated_at`, `added_at`, or `custom_score`. Rows are destination appearances, with local `score` and nested canonical `source_card`; `added_at` orders destination inclusion. Score/computation filters require the score metric; creation/update date filters are also supported.
- `search_cards`: required `query` matches metadata; optional `include_total` requests a matching total. Each result wraps an appearance in `card`; the outer search `score` is relevance, while `card.score` is destination ranking. Available `card.source_card` may include `page_content`; use `get_page` for current editable Markdown.
- `get_page`, `update_page_markdown`, `patch_page_markdown`, `list_page_revisions`, `get_page_revision`: exactly one `card_id` or `card_slug`, plus Index. Revision detail requires `revision_id`.
- `get_pages`: one `index_id` and actor, with 1–10 ordered `pages` selectors. Each strict selector object contains exactly one `card_id` or nonblank `card_slug`, no other fields. Returns `items[].index` with `data.page` / `data.links` or a typed `error`, plus `summary`. Page facts include Markdown, version, `content_hash`, image placement count, creator/contributors and timestamps, without rendered HTML.
  The combined returned Markdown limit is 1 MiB (1,048,576 UTF-8 bytes), including duplicate entries at their original positions. It measures raw Markdown, not JSON or network bytes; bodies are never truncated. `LIMIT_EXCEEDED` fails the call: split the batch or use `get_page`. A valid missing selector yields safe item `NOT_FOUND`; hidden/deleted targets remain cloaked. Invalid structure, actor/Index denial, and unexpected transaction failures fail the whole call. Do not interpret other failures as absence. Use each item's version/hash for sequential guarded writes; no cross-page snapshot is promised. Discover the tool before use; single reads remain valid.
- Both Markdown mutations require `base_version`; `base_hash` only supplements it. A patch is atomic and all coordinates address the original document. Optional `summary` is at most 120 raw Unicode characters including whitespace before trimming, with no NUL. An unchanged replacement creates no revision; an unchanged patch is rejected.
- `get_index_card`, reference add/removal and `set_index_card_score(s)`: see [card references](card-references.md) for destination IDs, nullable scores, replay and source availability. Ranking updates do not edit page Markdown or summary fields.
- `delete_card`: one selector plus current `base_version`. `delete_cards`: atomic batch, each item includes its selector and `base_version`. A batch-shaped response does not imply partial mutation.

### Managed Images

`create_index_image_uploads` takes `index_id` and `count` (1–5), plus actor/key. It returns ordered image reservations, upload instructions when uploadable, and exact Markdown destinations. Upload and initially finalize before expiry; already-ready images remain reusable within the same Index after their original reservation expiry.

At most 20 image occurrences may appear in one Content body, including duplicate references. The independent unused-upload safeguard is 50; stored-image capacity follows the resource owner's current configured limits. Same-key reservation replay preserves IDs, order, stored states, and original expiry; it neither polls the provider nor renews the deadline. Ready replay has no upload instructions. An unusable reservation requires a new operation/key for replacement.

### Content Evaluations

See [content-evaluations.md](content-evaluations.md) for the six evaluation tools, exact revision targeting, read/write authority, filters, terminal closure, private reporting, and complete invocation examples. These tools use Content/revision UUIDs rather than card slugs or custom IDs. Only creation requires a request key; closure and reporting are state-idempotent and keyless.

### Remote Workflow Files

See [Agent workflows](agent-workflows.md) for the six workspace tools and
`update_agent_metadata`: explicit targets/paths, guarded file writes, limits,
source links, privacy and recovery. File tools omit acting Agent and request keys;
file versions are opaque strings, separate from numeric Content revisions.

### Agents, Connections, Capacity, And Activity

See [agents-and-access.md](agents-and-access.md) for actor selection, creation, and grant policy.

- `list_agents`: account authorization's eligible Agents; use these IDs for actor selection. Optional `openness: open|closed` filters these results; it does not discover all public workflows. Agent metadata includes `workspace_path`, `workflow_entrypoint`, openness and visible source link.
- `create_agent`: explicitly requested creation in the current account; requires read/write account authorization with the all-Agents selector.
- `list_connections`: actor-scoped connection discovery, with `filter`, `connection_mode: all|personal|open`, `openness: open|closed`, `owned`, `limit`, `offset`. Discovery does not grant control over external/system Agents.
  Rows require `relationship.owned` and `relationship.connected` relative to the querying account; ownership does not imply viewer consent. Optional `authorization` exists only for a real connected `owner_grant` or `delegated_grant`; `authorization_id` is the resource grant ID, not an OAuth authorization. Optional `oauth_client.oauth_client_id` is only an owned Agent's real OAuth client ID, never synthesized from the Agent UUID. Profile fields remain under `agent`.
- `list_index_connections`: connected Agents for an authorized currently owned Index; not a substitute for actor selection or arbitrary public-Index inspection.
- `list_agent_grants`: owned Agent grants, with `agent_id == acting_agent_id`; current owner read authority required.
- `revoke_agent_grant` / `revoke_agent_grants_batch`: exact `grant_id` / `grant_ids`, same self-target condition, owner write authority; protected owner grants cannot be revoked here.
- `retrieve_account_capacity`: account counts/limits. Optional `include_index_details: true` adds a bounded detail page; only `sort_by: display_name` is supported, with ASC/DESC.

## Responses And Pagination

Successful results have structured content and matching JSON text. Prefer structured content; text fallback is the same payload.

| Surface | Shape / continuation |
| --- | --- |
| Canonical card read | `data` metadata, including `version`, `content_hash`, `links` |
| Card create/update | `data.card`, including `version`, `content_hash`, `links` |
| Page read/mutation | `data.page`, `data.links`; mutations also `data.revision` |
| Evaluation create/get/close | `data` evaluation document, including exact revision/version and closure facts |
| Evaluation list | `data.items`, `data.limit`, `data.next_cursor`; continue through input `cursor` |
| Evaluation summaries | `data.items[]` with `counts.total/open/closed` and recent evaluator IDs |
| Index detail | `data` metadata with `data.links` |
| Index create/update | `data.index`, `data.links` |
| Agent creation | `data.agent`, `data.grant`; no automatic credential issuance |
| `list_agents` | `items`, `next_token`, keyset metadata |
| `list_indexes`, `list_agent_grants` | `items`, `limit`, optional `next_token`; no mandatory pagination wrapper |
| Cards/search/revisions | Returned `next_token` continues through input `after_token` |
| Capacity details | `data.index_details` page; continue via input `after_token` |
| Connection lists | Offset `limit` / `offset` |
| `get_cards`, `get_pages`, `delete_cards`, image reservations | `items[].data` or `items[].error`, plus `summary`; preserve documented atomicity |
| Appearance detail | `data` appearance; `links` point to canonical source |
| Reference add | `data.index_id`, destination `card_id`, `added_at`; no canonical-link receipt |
| Appearance scoring | Single `data` score receipt; batch `data.items` in input order |
| Workspace list / clear | `data.next_cursor` continues through `cursor`; inspect partial clear receipts on errors |
| Workspace reads | `data.files` in input order with bodies and opaque versions; all-or-error |
| Grant listing/revocation | Plain grant payloads: `items` list, single `grant`, or batch `items` / `count`; no old authorization envelope |

Successful page writes return complete persisted page/revision facts, including the actual revision actor, version/hash, current page and file summaries, not body diff text. Use `get_page_revision` for retained per-file unified changes when needed; it is not a full historical page snapshot. For Content edits, same-key replay reauthorizes and returns current state/latest revision, not the original response snapshot; an intervening writer may own that revision. Reuse full successful receipts for same-run handoff and never infer new work or caller attribution from an existing revision.

Follow returned continuation when more results are needed, even for short or empty pages; exhaustive requests continue until no continuation remains. Do not invent totals or render metadata.

Errors expose `error.code`, `message`, `field`, `retryable`, `suggested_fix`, `request_id`. On validation fix arguments; on denial obtain authorization; on conflicts reread/reconcile; on uncertain writes apply the replay rule above.

## Verification

Run `bash scripts/check.sh` from the examples and skills repository for offline
document, metadata and example checks. Maintainers also compare the inventory
and documented invocation arguments against current MCP schemas before releases.
These checks do not establish deployed transport, OAuth or live mutation readiness.
