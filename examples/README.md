# Example Indexes and Agents

Prompt-only workflows for creating and maintaining useful Indexes from public
information. This repository is the authoring source; [deploy changes](deploy.md)
to Index Alpha Agent/common storage for scheduled execution. Each Index has a definition, an entry-point README, and specialized
Agent folders. Open the README first; task files are instructions for the host
Agent, not custom programs or an installed scheduler.

| Index | Purpose | Default presentation |
| --- | --- | --- |
| [Open Source Finds](open-source-finds/README.md) | Useful projects and meaningful releases with evidence and limitations | Card view, newest first |
| [Space & Earth Discoveries](space-earth-discoveries/README.md) | Visual observations explained with scientific context and credits | Card view, newest first |
| [Signal to Noise](signal-to-noise/README.md) | HN Best 10 stories with concise evidence and refreshed discussion synthesis | Card view, ranked by signal quality |

Shared [fact-checking and formatting Agents](shared-agents/README.md) work across
explicitly selected Indexes. Keep reusable standards there instead of copying
them into each Index's workflows.

## Start a run

1. For an existing deployment, load its stored bindings/routing, then the selected Index's
   definition and Agent README through their owning MCP connections.
2. Follow [setup.md](setup.md) for requested platform setup, or supply the exact
   existing resources. Choose your authenticated account explicitly; new
   resources default to private. Account and Agent IDs are runtime inputs.
3. Apply the [common workflow](workflow.md) and [image procedure](images.md).
   Use direct public HTTP/browser retrieval and authorized Index Alpha MCP tools.
   No Python application, custom ingestion script, or package install is needed.
4. The host runs requested stages sequentially with inherited mode/deadline and
   platform results passed in memory. It tracks edit-mode invocations in
   account-private `common/runs/<run-id>.json` files. Host invocations drive maintenance.

Use [remote workflow setup](setup.md#store-and-run-remote-workflows) to keep
README/task files, definitions, bindings, run records and sparse text checkpoints
in Index Alpha as the execution source. Author changes in this repo and deploy
the selected revision or explicitly authorized working tree; deployed runs report missing remote files
instead of silently falling back to them. No local checkout,
GitHub repository, package installation or custom runtime is required to set up
the workflow. Recover ordinary content facts from Indexes, content and revisions;
keep only otherwise invisible progress in sparse remote checkpoints and compact
host-owned run records. Common storage is private per account; use explicit
owner routing for shared Agent workflows. Binary
images and host process logs remain host-owned. Never save credentials or upload tickets.

The README/definition/task split follows the [shared folder conventions](shared-agents/README.md).
For repository validation and contributions, see [CONTRIBUTING.md](../CONTRIBUTING.md).
Document and schema checks do not prove live content creation or image rendering.

For optional headless execution and local cron setup, see
[Run workflows on a local schedule](scheduling/README.md).

Use the [evaluation flow](evaluations.md) to showcase revision-linked proposals,
no-change checks, author corrections and explicit verified closure.
