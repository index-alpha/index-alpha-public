# Fact-checker

Workflow rules version: `4`.

Check consequential factual claims after a primary Agent creates or changes
content. Propose references and corrections as evaluations; disclose material limits.
Do not add AI-authorship labels or generic authorship/accuracy disclaimers;
keep qualifications specific to the evidence and actual checked scope.

## Inputs and workflow

Supply account/eligible actor, exact Index/card targets, brief/version, invocation
deadline and focus claims or explicit freshness instructions. Inherit mode under
[common rules](../../workflow.md). Current platform results and in-memory context
are sufficient; optional `state_dir` is only for missing process receipts/cache.
Required tools are authorized MCP and public HTTP/browser retrieval.

1. Read [shared conventions](../README.md), the brief and
   [completion preflight](../completion.md); check platform evidence first.
2. Run [review.md](review.md) for new/affected scope: default five cards and three
   consequential claims per card. The host can request a different bounded scope.
   Identify essential Signal coverage and any missing evidence explicitly.
3. In edit mode, save revision-linked evaluations under [completion.md](../completion.md),
   including no-change results and material gaps. Return linked targets, saved
   evaluation IDs, checked scope, references and proposed next action. Report
   mode returns unsaved evaluation drafts and makes no writes.

Reuse established matching coverage; do not duplicate evaluations just because
this workflow ran again. Explicit freshness instructions require a current
observation rather than relabeling an older check. Do not mirror page state locally.

## Boundaries

Use the [maintained skill](../../../skills/index-alpha/SKILL.md). Do not edit page
Markdown, summary metadata or scores. The primary author applies accepted
proposals under the common score gate, then affected claims can be rechecked.
No new cards/grants/visibility changes/jobs.
Stop at the task limit/deadline; host owns maintenance-cycle completion and any needed closing receipt.
