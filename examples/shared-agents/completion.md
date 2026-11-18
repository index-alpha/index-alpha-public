# Reuse completed work from platform evidence

Use current Index/card/page reads, saved evaluations and full committed mutation
receipts. Pass results between roles in memory; a remote checkpoint is optional.
Follow the maintained [evaluation contract](../../skills/index-alpha/references/content-evaluations.md).

## Cheap preflight

1. Read current card/page version and `content_hash`, agreeing metadata and body
   reads. Reuse fresh same-run reads and committed responses.
2. Identify the exact saved revision reviewed. Match the read version to
   `list_page_revisions`' `to_version`, using `get_page_revision` when needed.
   A receipt's `data.revision.revision_id` is usable only when its facts identify
   that reviewed version; replay may return another writer's latest revision.
   Never attach findings to an assumed latest row after concurrent edits.
3. Read relevant `list_evaluations` with the card UUID as `content_id`, exact
   `revision_id` when appropriate, and evaluator `agent_id` to filter authors.
   Follow `data.next_cursor` through input `cursor`, even after empty pages,
   within the run budget. Incomplete retrieval is not proof of absence.
   Establish checked scope, rules/brief versions and evidence from the message
   or matching same-run context; author identity or counts alone prove no coverage.
4. Reuse matching completed checks instead of creating a duplicate on each run.
   New evidence, changed claims/sources, substantive rules, expanded scope, a due
   freshness checkpoint or explicit recheck can require a new bounded evaluation.
   If later edits intervened, inspect at most three recent revisions and needed
   diffs. Proven formatting-only changes can retain unaffected factual coverage.
   Compare title/subtitle/source too; page diffs do not prove metadata equality.
5. Keep optional remote checkpoints only for context not recoverable remotely,
   including report-only proposals, pending request keys and unfinished handoffs.
   Missing proof means a bounded check, not assumed completion or unlimited scans.

## Record checks as evaluations

In edit mode, reviewers create an immutable plain-text `create_evaluation` for
findings, proposed corrections/references, freshness checks and completed checks
needing no content change. Formatters save real style changes as page revisions;
when no style change is needed, create an evaluation instead of a dummy revision.
Report mode returns unsaved proposals and performs no writes, including evaluations.

Use the eligible actor and Index, the card UUID as `content_id`, the verified
`revision_id`, a stable `idempotency_key`, and `message` (1–4000 Unicode characters
after trimming). Include the checked scope and rules/brief version, evidence
URLs, actual observation time when freshness matters, outcome and material gaps.
Clearly distinguish proposed changes from applied corrections. Split separate
findings when necessary; do not imply three checked claims cover every assertion.
The server supplies author/version/time/status. Markdown is not rendered.

New evaluations start open. The evaluator hands actionable findings to the
primary author and leaves them open for disposition. No-change evaluations are
coverage records and stay open in routine runs.

Replay uncertain creation with identical arguments/key within 24 hours; otherwise
read/reconcile before retrying. Do not invent calls or fall back to page footers
if evaluation tools are unavailable: report the gap and return an unsaved draft.
On concurrent edits, preserve the original reviewed revision binding and make
clear what is still current; reread/recheck before evaluating changed content.

## Resolve findings as the primary author

In edit mode with closure authorized by the invocation, the primary author owns
disposition for cards already in scope. Reuse same-run findings and read open
evaluations for those cards across revisions with `list_evaluations` and
`status: open`. Follow cursors within the invocation budget and report any
unread scope. Report mode returns proposed dispositions only.

1. Read each actionable finding and its evaluated revision. Check the finding
   against current content and relevant evidence. Apply supported corrections
   through the existing version and Signal score gates and obtain the required
   recheck on the saved result.
2. Close a finding when evidence confirms the correction, shows it was already
   addressed, or supports declining the proposed change. Reconcile any
   intervening edit that affects the finding before closing it. Keep unresolved,
   deferred or unverified findings open and report their next action.
3. Use `close_evaluation` with the primary author's eligible acting Agent,
   exact Index and evaluation ID, and a concise reason explaining the verified
   outcome within the contract's 1000-character limit. The operation is keyless
   and terminal. On uncertainty, read `get_evaluation` before retrying.
   Report confirmed closures separately from
   open findings and no-change coverage. Use a new evaluation for any later
   follow-up on the appropriate revision.

## Keep articles free of administrative logs

Do not append administrative review/revision logs, check timestamps, hidden
markers or status boilerplate to pages. A definition may require a meaningful
source/discussion observation time in its normal Sources and scope section;
that evidence context is not a review footer. Do not edit it solely to record
a no-change check. Attribution belongs to evaluation and revision receipts.
During an authorized formatter/content edit, remove identifiable legacy bottom
review/revision-log sections and their purely administrative separator, preserving
article references, qualifications, image credits and unrelated content. Leave
ambiguous substantive material intact and report it. Do not manufacture a page
revision merely to attribute a check or bulk-rewrite out-of-scope pages.

Use descriptive summaries for real page edits: at most 120 raw Unicode characters
including whitespace before trimming, with no NUL. Preserve managed images and
all unrelated content; on conflicts reread and reconcile. Proven administrative
footer removal or formatting-only changes need no Signal score reset; substantive
corrections by the primary author still obey the common score gate. Evaluations
alone do not change content or scores. Host owns maintenance-cycle completion,
which is distinct from evaluation closure.
