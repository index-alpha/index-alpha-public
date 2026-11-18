# Signal to Noise

Brief version: 2

## Purpose

Extract rare, practical ideas and evidence for people building software from
the first ten items of Hacker News Best at selection time. Select for a useful engineering decision, a concrete technique,
or an illuminating disagreement. Popularity is a discovery aid, not the thesis.

- Display name: `Signal to Noise`.
- Stable Index custom ID: `signal-to-noise`.
- Description: `Practical ideas, evidence, and useful disagreements for software builders, selected from Hacker News Best.`

Use common [setup](../setup.md) and [workflow rules](../workflow.md) for private
setup in the selected account, card-view presentation, platform-first recovery,
and maintenance lifetime.

## Editorial contract

Use the official public Firebase HN API over direct HTTP: Best IDs from
`https://hacker-news.firebaseio.com/v0/beststories.json`, then story and comment
items from `https://hacker-news.firebaseio.com/v0/item/<id>.json`.
Read the linked article separately. A story record, title, image, or comment
thread does not establish the article's contents. If the article cannot be read,
disclose that limit and publish only if accessible HN material independently
contains enough useful, attributable signal.

Consider only the first 10 returned Best IDs, never backfilling from rank 11 or
lower after duplicates, skips or fetch failures. Record selection time, ordered
IDs and each selected position in run evidence. Create at most three cards and maintain
at most five due existing cards per editor run; zero new cards is a good result.
Fetch at most 100 HN story/comment items across selection and maintenance
combined across the editor and Comment Monitor, including retries and unusable
records. Share cached samples within a run rather than fetching twice. Skip deleted/dead records.
Per story per run, read at most 30 comments across at most 10 leading top-level branches,
reserving space for substantive replies and rebuttals. Describe sampling gaps;
never invent comment scores, unanimity, or community consensus.

One story maps to `custom_id: "hn-story-<numeric-story-id>"`, retained through
updates. Existing cards remain eligible for refresh after leaving the Best 10;
the restriction applies to new selection. Follow the [editorial standard](editorial.md)
for concise, frank, data-backed synthesis without named-user quotes or clickbait.
Link the HN discussion and article separately and identify the claims
each supports. Extract the idea, applicability, evidence, limitations, and
useful disagreement. Avoid generic summaries. Reuse the same-run article
HTML/source snapshot for drafting and OG discovery under the common
[image guide](../images.md); an absent, unsuitable, or failed image permits a
reported text-only card.

The [Comment Monitor](agents/comment-monitor/README.md) checks active discussions
on each host invocation, including changes in leading threads and important
rebuttals, and proposes material updates through evaluations. It never edits pages.
The editor owns editorial meaning; the shared fact-checker reviews current
claims and proposes corrections through revision-linked evaluations; the formatter
preserves meaning and edits only actual formatting. Review checks never append
page-bottom logs; unchanged checks leave scoped evaluations instead.
The ranker alone changes existing scores. New cards start at provisional zero.
Before any writer saves body or relevant metadata changes that invalidate prior
review or the current score, the common host pipeline requires Ranker-confirmed
zero for the current content, committing a reset first if needed. This applies
even when the old content already has complete review. Reviewed scoring follows
review and formatting.

Use one interim +24-hour source check and one final +72-hour source check.
Record freshness outcomes, including unchanged checks, as exact-revision
evaluations with actual checkpoint and observation times. Primary authoring may
apply proposed substantive changes through the score gate; check-only roles
leave evaluations. Do not append review/revision logs to pages.
The common workflow owns fixed-clock, late-invocation, and closure mechanics.

Discussion monitoring runs at most once per card per host invocation until the
fixed +72h cutoff, including the allowed final closing pass. When the owner configures a two-hour host schedule, it provides a check
opportunity at that cadence while the host is available.
No schedule is installed or resumed by these prompts. Monitor work shares the
five-existing-card and 100-item budgets; report deferrals instead of overrunning.
