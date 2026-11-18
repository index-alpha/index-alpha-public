# Select observations and discoveries

Read the [definition](../../definition.md) and [common workflow](../../../workflow.md).
Selection is read-only; the host passes its handoff and source cache in memory.

1. Resolve the supplied account, actor, and exact Index. Fix a set of at most
   15 candidate identities from official NASA Webb/Earth Observatory articles; failures and
   rejections count toward the budget. Do not replenish the set to fill a quota.
2. Canonicalize identities using the definition, then batch exact `get_cards`
   custom-ID lookups for candidates and known aliases recovered from platform
   content/source URLs, current run context, or optional sparse remote state
   before further deduplication discovery. Never scan all Index cards. For
   ambiguous cross-posts/redirects, permit at most two additional discovery pages of
   at most 20 cards each across this run. Defer unresolved ambiguity when that
   budget ends; denial or incomplete reads never prove absence.
3. Read full primary sources via host HTTP/browser tools; an unavailable page
   is an evidence gap, never a summary inferred from a headline. Identify observation, significance, interpretation, and limits. Record article
   publication and observation/acquisition dates separately; do not imply linked
   research was read when inaccessible. Explain old observations without false
   recency.
4. Prefer an eligible existing card over a duplicate. A cross-post does not create a new discovery.
   Inspect the official asset page, image type, caption, full collaborators'
   credit, and scientific context. Do not search for affirmative reuse permission;
   skip for rights reasons only for an explicit source request not to reuse.
   Record text-only status when reuse is explicitly prohibited or suitable assets
   are missing.
5. Return at most three qualified selections with canonical identity, valid
   custom ID, aliases, title/angle, source links, dates, limits, image status,
   and rationale. Retain same-run source/HTML snapshots in the host's in-memory
   source cache, or optional ignored cache files, for creation and OG extraction; shared reviewers
   may still perform independent targeted checks. Record rejections and gaps.

Stop at the fixed candidate budget, three selections, invocation deadline, or
exhausted sources. Pass qualified records and cached evidence in memory to
[create.md](create.md); selection is not publication proof.
