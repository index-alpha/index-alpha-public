# Select projects and releases

Read the [definition](../../definition.md) and [common workflow](../../../workflow.md).
Selection is read-only; the host passes its handoff and source cache in memory.

1. Resolve the supplied account, actor, and exact Index. Fix a set of at most
   15 candidate identities from GitHub Explore and project-owned public pages; failures and
   rejections count toward the budget. Do not replenish the set to fill a quota.
2. Canonicalize identities using the definition, then batch exact `get_cards`
   custom-ID lookups for candidates and known aliases recovered from platform
   content/source URLs, current run context, or optional sparse remote state
   before further deduplication discovery. Never scan all Index cards. For
   ambiguous renames/redirects, permit at most two additional discovery pages of
   at most 20 cards each across this run. Defer unresolved ambiguity when that
   budget ends; denial or incomplete reads never prove absence.
3. Read full primary sources via host HTTP/browser tools; an unavailable page
   is an evidence gap, never a summary inferred from a headline. Inspect the actual license, docs, release notes, dates, practical use, and a
   limitation. Public source visibility alone does not make a project open source.
   Do not install or execute project code.
4. Prefer an eligible existing card over a duplicate. A release-specific card needs a distinct substantial release story.
   Identify a relevant project OG image or provided screenshot, source, credit,
   and available credits. Do not search for affirmative image reuse permission;
   skip for rights reasons only for an explicit source request not to reuse.
   Record text-only status when reuse is explicitly prohibited or suitable assets
   are missing. Continue verifying the project's code license for source selection.
5. Return at most three qualified selections with canonical identity, valid
   custom ID, aliases, title/angle, source links, dates, limits, image status,
   and rationale. Retain same-run source/HTML snapshots in the host's in-memory
   source cache, or optional ignored cache files, for creation and OG extraction; shared reviewers
   may still perform independent targeted checks. Record rejections and gaps.

Stop at the fixed candidate budget, three selections, invocation deadline, or
exhausted sources. Pass qualified records and cached evidence in memory to
[create.md](create.md); selection is not publication proof.
