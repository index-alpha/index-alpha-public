# Public Card References

Build an Index from original cards and references to canonical cards in other public Indexes. This can form a virtual Index without copying Markdown or creating a separate Index type. References retain live source content and attribution; the destination controls inclusion and local ranking.

## Resolve Both Identities

`list_cards` and `get_index_card` expose appearances directly. `search_cards` wraps each appearance in `items[].card`; its outer `items[].score` is search relevance, not destination ranking.

| Appearance fact | Use |
| --- | --- |
| Outer `index_id`, `card_id` | Destination appearance: inspect, rank, remove a reference. |
| `source.index_id`, `source.card_id` | Canonical content: metadata, Page, revisions, evaluations and permitted content edits/deletion. |
| `kind: native|reference` | Native content or a reference to content elsewhere. |
| `score`, `added_at` | Local ranking and time included in this destination. |
| `source_card`, `source_index`, `links` | Available canonical metadata, attribution and source navigation. |

Use the source tuple consistently for canonical work, even for native appearances. Destination write authority does not grant source edit authority. Canonical `custom_id` remains a source-Index lookup; it is not a destination appearance selector.

## Add, Rank, Remove

Resolve the intended destination and canonical source IDs from trusted context or authorized reads. A fresh add requires destination write authority, source read authority and a currently public eligible source. When public MCP reads are enabled, an eligible owned Agent may use public source read authority without a source grant; destination writes still require explicit authority. See [public Index reads](public-index-reads.md). If discovery is insufficient, resolve the source/access gap; do not copy inaccessible content.

```json
{
  "tool": "add_card_reference",
  "arguments": {
    "acting_agent_id": "11111111-1111-4111-8111-111111111111",
    "idempotency_key": "include-public-finding-42",
    "index_id": "22222222-2222-4222-8222-222222222222",
    "source_index_id": "44444444-4444-4444-8444-444444444444",
    "source_card_id": "33333333-3333-4333-8333-333333333333"
  }
}
```

Optional `score` sets the initial destination rank. The receipt returns `data.index_id`, destination `data.card_id` and `data.added_at`, not a new Page or canonical link. Retain the destination ID for subsequent operations; fetch `get_index_card` only when appearance details/links are needed. Report inclusion in the destination separately from links to the original source.

- Inspect: `get_index_card` with destination `index_id`, `card_id` and actor.
- Rank: `set_index_card_score` with destination IDs, actor/key and required `score`; numeric sets it, explicit null clears it. Optional `computed_at` is RFC3339, at most five seconds ahead of server time.
- Rank several: `set_index_card_scores` with one destination and 1–1000 distinct `scores` objects, each `{card_id, score}`. The batch is atomic and returns `data.items` in input order. Ranking changes no source content or Page revision.
- Remove inclusion: `remove_card_reference` with destination IDs and actor/key. No `base_version` is used. Native cards require canonical deletion tools and their version guards; removing a reference never deletes its source.

All four mutations require `idempotency_key`. After uncertainty, replay identical arguments/key within 24 hours. Replay returns the original receipt, even if the reference was subsequently removed or the source became private; it does not confirm current inclusion or ranking. A fresh add key creates a distinct appearance, including for the same source. Reconcile before creating another reference when duplicate inclusion is not intended.

## Source Availability

References are dependent on their source, not independent snapshots. `availability` can be `available`, `private`, `deleted`, or `unavailable`; unavailable appearances have null source metadata and links. Do not fabricate missing details or recreate hidden content. Destination-authorized ranking and removal can still be possible.

`list_cards`/`get_index_card` can hydrate public sources without grants when enabled; `search_cards` still requires source grants. `list_cards(metric="added_at")` orders destination inclusion; `custom_score` orders local scores. Source-dependent sorts/search can omit unavailable sources, so an empty search is not proof that no reference exists. Use a known destination ID with `get_index_card` for exact inspection. References add destination entries without adding destination Pages; card and Page totals can differ.
