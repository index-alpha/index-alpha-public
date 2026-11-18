# Scheduled Index workflow invocation

Run the existing Index workflows in edit mode for the exact accounts, Indexes,
Agent identities and MCP server names in the stored operator bindings supplied
below. Resolve the owning connections and workspace routing, then read those
bindings and current platform state; do not invent missing authority.

Load the stored copies of the maintained Index Alpha skill, examples/workflow.md, the selected
definitions, primary Agent select/create/maintain tasks, examples/images.md,
and the shared evidence-review/formatting workflows and completion rules.
Resolve these source paths and relative links through the stored routing
manifest using explicit account, area, Agent and full logical path targets.
Do not fall back to local workflow, definition, binding or checkpoint copies.
This repo is the authoring source; execution uses its verified deployed copies.
Require each participating manifest's `deployment.status` to be `completed` and
all deployment IDs to match before content mutations. Record the deployment ID
with the observed instruction versions. Report an incomplete/mismatched
deployment instead of executing a mixed release.
Match every loaded instruction to its manifest file-version receipt or recorded
body fingerprint before following it. Missing receipts or changed files block
affected work until reconciliation/redeployment.

Use the host-supplied stable run ID, or the unique host run-directory basename
when the wrapper supplies one. Before content mutations, create the host-owned
`common/runs/<run-id>.json` record in each participating account under the
common workflow's run-tracking rules. Record the current instruction versions
and exact scope, then update stage outcomes as roles return. Read and reconcile
an existing record before resuming; never overwrite it unconditionally or infer
exclusive execution from its status. Subagents report results to the host and
do not concurrently update its run records. Keep unresolved per-Agent work in
that owning account's sparse `common/state/<agent-id>/<index-id>/` files.

For each selected Index, discover eligible Agents and verify current target
ownership, capacity and content. Maintain at most five due cards under the
existing fixed +24h and +72h rules, then select and create up to three qualified
new cards using the definition's candidate budgets and deterministic identities.
For Signal, select new cards strictly from the first ten HN Best IDs. Run the
Comment Monitor on active existing discussions each invocation, prioritizing due
source checkpoints then least recently checked cards. Share the editor/monitor
five-existing-card, 30-comments-per-story and 100-item retrieval budgets and cache;
pass monitor evaluation proposals to the editor before substantive updates.
Follow examples/signal-to-noise/editorial.md for leading-thread synthesis,
frank evidence-backed conclusions, no usernames and no clickbait. Keep the fixed
72-hour lifecycle; monitoring does not resume paused jobs by itself.
Deduplicate against live platform evidence. Zero new cards is a valid result.

Run primary authoring, independent evidence review, Markdown formatting,
author disposition of findings, and Signal ranking in order. One host owns
each Index's sequential stages. Different Indexes may run in parallel using
native subagents. Pass the invocation deadline,
source context and full mutation receipts between roles. Complete requested
shared stages under their actual Agent identities. Reviewers propose corrections
through exact-revision evaluations; due freshness and no-change checks also save
evaluations. Authors apply substantive corrections; formatters save actual style
edits. In each bound Index, the primary author must triage open evaluations on
in-scope cards and close verified findings in edit mode under
examples/shared-agents/completion.md. This invocation authorizes closure of
those resolved findings. Leave no-change checks and unresolved findings open.
Report confirmed closures, pending findings and any incomplete triage.
Follow examples/evaluations.md, keep review logs out of page content, and respect
the Signal zero-score gate for substantive changes.

Attempt relevant images using the existing bounded workflow. Do not search for
affirmative image reuse permission; skip for rights reasons only for an explicit
source request not to reuse. Preserve
ready images, existing edits and public visibility. Do not create Agents or
Indexes, change grants, delete content, schedule jobs, edit repository code,
install packages or commit files. Use direct public source retrieval; no custom
ingestion application. No AI-authorship labels or generic accuracy disclaimers.

When diagnostics are requested, keep concise MCP observations alongside content work.
Log actual errors with tool, code, recovery and outcome; separate source HTTP
failures from MCP errors and proposed efficiency improvements from observed bugs.
Note redundant round trips, batching opportunities, schema/response friction,
successful receipt reuse and approximate call usage. Raw stdout and stderr are
captured locally by the optional wrapper without filtering.
Do not copy account credentials or local client configuration into content.

Recover through stable request keys and current guards. Keep only useful sparse
text workflow checkpoints in owner-private common/state/<agent-id>/<index-id>/
through the workspace tools described in examples/setup.md. Temporary binary
assets and process logs stay with the host; logs are not an authority source. Reconcile uncertain writes before retries. Continue other
independent Indexes if one fails within their verified authority and working
tracking scopes. A tracking failure stops new mutations for the affected account
and dependent cross-account stages until tracking is repaired; preserve and
report actual committed work. Before
ending, write terminal run records with actual stage outcomes, pending work and
next actions. Report any missing terminal write rather than claiming fully
tracked completion. End with canonical links, counts, image/review/
ranking outcomes, actual blockers and next due work. Do not claim future source
checks were performed early.

## Operator bindings

Supply the authorized owning MCP connections and logical paths to stored
bindings, the routing manifest and this stored workflow in the host's minimal
bootstrap prompt. Bindings must specify exact target Indexes and primary/reviewer/formatter/ranker Agent
identities with their authenticated MCP connections, including the dedicated
Signal Comment Monitor. Report a missing monitor binding; do not invent or
silently borrow an identity. Continue independent authorized work if it is absent. If stored bindings or routing are absent, stop with a
missing-bindings result instead of writing to an inferred account.
