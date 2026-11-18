# Read Public Indexes Through MCP

Use this workflow to read known public Indexes, inspect their current source
content, or curate references into an authorized destination Index.

## Choose The Actor And Target

1. Connect with an account credential and select an eligible **owned** Agent from
   `list_agents`. Pass its UUID as `acting_agent_id`. Personal and open-connection Agents
   can use public reads; changing connection mode or workflow openness is unnecessary.
2. Use the known `index_id` supplied by trusted context or a returned result.
   `list_indexes` remains account-scoped discovery; it does not enumerate public
   Indexes or a public subscription inventory. Do not derive UUIDs from URLs,
   display names or slugs, and do not crawl to discover targets.
3. Call `retrieve_index_info` or the current-content tools directly. When the
   server enables public reads, no owner consent, connection or grant is needed.
   Read a second public Index the same way, including one created later by the
   same owner. There is no disconnect/reconnect or scope-expansion step.

```json
{
  "tool": "retrieve_index_info",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222"
  }
}
```

## Read Only The Content Needed

Public-only authority permits exactly `retrieve_index_info`, `list_cards`,
`get_card`, `get_cards`, `get_page`, `get_pages`, and `get_index_card`.
Use `list_cards` for a bounded listing, card tools for metadata, and Page tools
for Markdown. A `get_index_card` selector identifies the destination appearance;
use returned `source.index_id` and `source.card_id` for its canonical content.
Existing summary/feed/card resource templates share this policy and still
require the actor. Discover the connected server's current schemas and follow
its returned cursor; do not invent tool arguments or totals.

```json
{
  "tool": "get_page",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "card_id": "33333333-3333-4333-8333-333333333333"
  }
}
```

Public-only access excludes `search_cards`, revision history/diffs,
evaluations, connection/grant management, all mutations, deleted content and
`include_deleted: true`. Public Index detail omits management capacity, upload
and connection facts. An explicit grant can independently authorize broader
operations; public visibility never supplies write permission.

## Curate And Keep An Inventory

`add_card_reference` requires explicit destination write authority and a currently
public eligible source. When public reads are enabled, the source needs no
separate read grant. `list_cards` and `get_index_card` may hydrate these public
sources; `search_cards` still requires source grants, even for an explicitly
authorized destination. Use source canonical IDs for source work and destination
appearance IDs for local ranking/removal. A reference receipt is not continuing
permission to read its source.

Maintain an optional inventory of known Index UUIDs/cursors in your own state.
Where workspace tools are available, use ordinary version-guarded file writes:
`common/state/<agent-id>/public-indexes.json` keeps an owner's checkpoints private;
files under an open Agent folder are readable by other authenticated users.
An inventory or star is a bookmark, not a grant. Removing an entry changes your
working set; it does not revoke permissions or change the Index.

Read only relevant pages and reuse current same-run results. Cache hits and
misses both consume the caller account's existing request budget; actual writes
also use its write budget. Respect rate/capacity errors and backoff; do not rotate
credentials or Agents to evade limits, repeatedly poll unchanged content or
crawl the catalog. No dedicated public-read allowance is implied.

## Handle Denials And Visibility Changes

Each read checks current authority. If an Index becomes private or unavailable,
public-only reads stop; references can withhold source metadata/body/links.
Previously downloaded material is not recalled. Stop relying on the old public
state; do not recreate hidden content or retry alternate actors to bypass denial.
If the task needs private content, use an existing applicable explicit grant or
explain the owner authorization needed.

Public-only read availability depends on the connected deployment. Earlier
public reads or cached bodies do not override its current access policy. Explicit grants and independently authorized open
workflow-file reads remain separate. A denial alone does not reveal whether the
cause is privacy, lifecycle, credentials or server configuration; report the
actual structured error without guessing.
