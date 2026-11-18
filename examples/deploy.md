# Deploy repository workflows to Agent storage

Use this prompt when asked to deploy example workflow changes. This repository
is the authoring source; verified deployed Agent/common files are the execution
source for scheduled runs. Source edits take effect after deployment, not when
a client happens to have a newer checkout. Follow the [common workflow](workflow.md)
and [storage setup](setup.md#store-and-run-remote-workflows).

## Inputs and preflight

Resolve the requested source revision or explicitly authorized working tree,
target accounts/connections, current deployment manifest and bindings, selected
Agent folders, and deployment run ID/deadline. Record the source commit and
whether uncommitted source changes are included. A commit alone does not identify
dirty contents: fingerprint the exact selected source file bytes as well.

Validate the repository using its required checks and inspect the proposed
instruction diff. Resolve each source file to its owning MCP connection, area,
Agent selector and full logical path. Include the complete linked text dependency
graph and the maintained skill references used by the selected workflows.
Keep runtime IDs, bindings, credentials and deployment receipts out of public
source files. Resolve cross-account links explicitly; common is owner-private.

Acquire and hold the same host overlap guard honored by every affected scheduled
launcher before deployment writes. Establish that no affected content run is
active, and retain exclusion through all instruction writes, final manifest
readback, and failure recording. Release the guard only after those steps finish.
If that exclusion cannot be established, stop before deployment writes. A stored
run status or manifest does not grant ownership or act as a distributed lock.
Create private host-owned
`common/runs/<deployment-run-id>.json` records for the participating accounts.

## Deploy a bounded instruction set

1. Read current manifests and target files, retaining opaque versions. Compare
   repository source, previous deployment fingerprints and current stored bodies.
   Reconcile unexpected remote instruction edits instead of overwriting them.
   Preserve explicitly recorded operator overlays, including account routing and
   authorized deployment scope; do not copy them into generic source templates.
2. Mark each target manifest's deployment status `deploying` with a shared
   deployment ID, using its current `expected_version`. Record partial results;
   account writes are separate operations, not one atomic deployment.
3. Publish only authorized changed instruction files: Agent READMEs/tasks into
   their owning Agent folders; definitions, shared rules and skill references
   into common. Rewrite relative links and map plain source paths to the stored
   graph. Use `create_only:true` for absent files and `expected_version` from a
   current receipt for replacements. Skip unchanged bodies. On conflict or an
   uncertain result, read and reconcile before another mutation.
4. Preserve runtime-owned bindings, `common/state/`, `common/runs/`, content and
   evaluations. Deploying instructions does not reset checkpoints, complete a
   content review, create resources, change openness/grants, or resume a timer.
   Removed source files require an explicitly scoped retirement decision; do
   not delete stored files or clear an Agent folder as incidental cleanup.
5. Read back the full required instruction set and verify intended bytes, target
   routing and linked dependencies. Record per-file source and deployed body
   fingerprints plus the current deployed file versions. Fingerprints describe
   source/transform identity; opaque file versions guard workspace writes.
6. Only after verification publish `deployment.status: completed` in every target
   manifest with the same deployment ID, exact source identification, transforms,
   per-file receipts and completion time. Preserve manifest routing and runtime
   metadata. Read back the final manifests, then close the deployment run records.

On failure leave the affected deployment `failed` or `deploying`, record committed
file changes and blockers, and report incomplete deployment. Reconcile partially
published manifests before retrying. Do not claim an atomic rollback or turn
partial writes into successful deployment. Any restore uses an identified prior
source plus the same guarded deploy-and-verify process; runtime state is retained.

## Scheduled execution and report

### Using the example host guard

For the supplied scheduled runner, the guard is the directory
`$RUN_LOG_ROOT/.lock`. The default log root is `examples/.state/scheduled-runs/`
under the checkout; use the scheduled launcher's actual override if configured.
Acquire it with `mkdir "$RUN_LOG_ROOT/.lock"`; an existing directory means stop
and establish whether a run or deployment owns it. Invoke the deployment through
your authorized client while retaining that directory, rather than calling
`run.sh`, which would attempt to acquire it again and skip. After final manifest
readback and terminal run recording, release it with
`rmdir "$RUN_LOG_ROOT/.lock"`. On interruption, reconcile the deployment before
removing the guard. This recipe coordinates one shared host/log root; other
launchers must honor the same exclusion before it can protect their runs.

### Minimal storage conventions

The following is an illustrative manifest fragment, not a complete installed
release. Populate `files` for the entire required dependency graph from actual
deployment receipts; never publish these placeholder versions as completed.

```json
{
  "deployment": {"id": "example-release", "status": "deploying"},
  "account_routing": {"example-owner": "example-mcp"},
  "files": [{
    "source": "examples/workflow.md",
    "account": "example-owner",
    "area": "common",
    "target": "common/examples/workflow.md",
    "deployed_version": "replace-with-actual-file-version"
  }]
}
```

Bindings identify the intended resources independently of file routing:

```json
{
  "indexes": [{"account": "example-owner", "index_id": "11111111-1111-4111-8111-111111111111"}],
  "agents": [{
    "account": "example-owner",
    "agent_id": "22222222-2222-4222-8222-222222222222",
    "role": "primary",
    "index_id": "11111111-1111-4111-8111-111111111111"
  }]
}
```

A minimal private host bootstrap can say:

> Through my authorized `example-mcp` connection, read the common-area files
> `common/examples/storage-manifest.json`, `common/examples/bindings.json` and
> `common/examples/scheduling/prompt.md`. Require a completed deployment and
> verify loaded instruction versions against its receipts. Resolve linked files
> through the manifest, follow the stored workflow, and track this invocation
> in common storage using the supplied run-directory basename. Stop on missing
> files, denied authority or deployment drift; do not use checkout fallbacks.

Start with one account. For open-connectable Agents owned elsewhere, add that owning
connection explicitly and keep each account's common files private to it.

Scheduled hosts load stored manifests, bindings and workflows through MCP.
Require completed manifests with matching deployment IDs across the accounts
participating in the invocation; otherwise stop before content mutations.
Capture the deployment ID and observed instruction versions in the invocation's
run record. Before following each required file, match its observed version to
its manifest receipt or verify its deployed body fingerprint. Missing receipts
or drift block affected execution until reconciliation/redeployment. Execute
verified stored instructions without local checkout fallback.
Platform records remain authoritative for content, evaluations and permissions;
private MCP run records/checkpoints track workflow progress.

Report deployed source identity, changed/unchanged files, readback evidence,
deployment readiness and any validation gaps. Document checks and file readback
prove deployment consistency; actual scheduled/content execution requires its
own evidence. The existing host still owns the timer, credentials, raw process
logs and temporary binary assets.
