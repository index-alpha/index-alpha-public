# Select useful signal

Use the [editor entry point](README.md), [definition](../../definition.md),
and inherited common workflow contract.

1. Fetch `https://hacker-news.firebaseio.com/v0/beststories.json`. Consider only
   its first 10 IDs, or fewer under the supplied budget. Freeze this ordered
   candidate set for the run; record fetch time and selected rank positions. Never
   reach rank 11 or lower to replace a duplicate, skip, missing item or weak story. Fetch each candidate
   via `https://hacker-news.firebaseio.com/v0/item/<id>.json`; skip null,
   deleted, dead, or non-story records without replacing failed candidates.
   Count every story/comment item fetch toward the combined 100-item editor/monitor
   budget, including retries and unusable records.
2. Resolve the fixed `hn-story-<id>` set using common exact-key batch lookup and
   source aliases if present in platform evidence or optional remote hints. Existing
   cards belong in maintenance. An incomplete or denied
   lookup does not establish absence. HN points and reply counts guide attention
   but do not establish quality or determine scores.
3. Read promising stories' linked articles, recording exact URL, observation
   time, accessible scope, and primary evidence in the shared source cache.
   Reuse that same-run HTML/source snapshot during creation and OG discovery.
   For HN text-only stories, use their actual text. If an article is partial or
   unavailable, prefer a skip unless accessible discussion supports a useful
   standalone insight; record the limitation.
4. Per shortlisted story, sample at most 30 comments across at most 10 leading
   top-level branches using item `kids` links. Spread the first pass across
   branches before deepening one; reserve space for replies, counterexamples,
   and rebuttals. Record comment IDs, permalinks, and skipped/inaccessible
   branches. Deleted/dead comments provide no evidence. The `kids` order is HN display ranking, not a disclosed vote tally or proof
   of consensus. Prioritize leading ranked branches, then substantive replies
   and evidence-backed dissent, following the [editorial standard](../../editorial.md).
   Summarize recurring themes across independent branches; explicitly identify
   split views or insufficient evidence. Never display individual user names.
5. Select at most three new stories that change a builder's understanding or
   choice. State the practical idea, audience, concrete evidence, strongest
   caveat or disagreement, and why each deserves a card. Separate article
   claims, reported experience, and editorial inference. Tie numerical claims to
   their source, units and conditions; do not convert anecdotes into measurements.

Return a compact shortlist and skip reasons, candidate and sampling counts,
article access limits, source links, and existing cards handed to maintenance.
Continue selected new stories through [creation](create.md) in the inherited
mode; report mode returns drafts.
