# Revisit leading discussion

Follow the [entry point](README.md), [selection sampling rules](../signal-editor/select.md)
and [evaluation contract](../../../../skills/index-alpha/references/content-evaluations.md).
Share one cache, 100 HN item fetches and at most five existing cards with the
editor for the entire Signal invocation. Per story read no more than 30 comments
across ten top-level branches, including any already fetched in the same run.
Count retries/unusable items; defer remaining work when the budget/deadline ends.

1. Resolve the existing `hn-story-<id>` card and its current page/revision,
   publication clock and relevant prior discussion evaluations. Read the latest
   story item and its ranked `kids`; fetch comments in leading branches before
   deepening one. Inspect substantive replies, corrections and counterexamples.
   Use direct public retrieval; no custom scraper, packages or private API.
2. Compare actual current evidence to the last applicable observation: leading
   branch order, new substantial arguments, changed/deleted comments and material
   rebuttals. Do not rely on unchanged `descendants` or IDs alone: comment bodies
   can change. Reuse same-run reads, but fetch the current sampled bodies before
   claiming a new check. Keep comment IDs/permalinks, exact snippets or snapshots,
   observation time, branch/sample counts and source limits in run evidence.
   Do not describe rank changes as measured vote changes.
3. Assess whether the page's synthesis is still fair. State recurring observations,
   qualified convergence or divided views with strongest evidence-backed dissent.
   A technical correction, credible counterexample or substantial consequence
   can matter more than rank. Popularity alone is no evidence of factual truth.
   Follow the concise, frank editorial standard; no usernames, quote compilations
   or claim of community-wide consensus from a limited sample.
4. In edit mode create a plain-text evaluation bound to the exact page revision
   inspected, using actor, Index, Content UUID, verified revision UUID and stable
   request key. Include actual observation time/checkpoint, checked scope/sample,
   supporting source/discussion links, limits and precise proposed replacement
   of affected synthesis or “no material change.” Reuse matching proven checks
   under the entry point's rules. A failed fetch yields an incomplete observation,
   not a successful no-change check. Leave evaluations open; report mode saves none.
5. Pass evaluation receipts, affected claims, proposed text and cached samples to
   the [editor's maintenance task](../signal-editor/maintain.md). The editor owns
   material page/metadata updates after the Signal Ranker confirms zero, then
   targeted fact review, formatting and reranking. Keep changes within the
   authorized active lifecycle. Incomplete stages remain pending; the monitor
   never marks a proposal applied or closes the maintenance cycle.

Return canonical links, changed/no-change/incomplete results, actual observation
and sample evidence, proposal/evaluation receipts and deferred cards. Never
append timestamps or review logs to the article merely to record the check.
