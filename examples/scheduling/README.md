# Run workflows on a local schedule

Codex CLI can run these same prompt workflows headlessly. This example is a
shell wrapper around `codex exec`, not an ingestion service. Install and sign in
to Codex CLI, configure the authorized MCP connections, and confirm live access
before scheduling. The desktop app's tools are not proof of CLI connectivity.

The runner selects `gpt-6.1-sol` with low reasoning, enables source research,
and uses workspace-write with network access and no interactive approvals.
Current workflow rules and MCP authority still apply. See OpenAI's
[non-interactive documentation](https://learn.chatgpt.com/docs/non-interactive-mode).

## Configure and run

Install [prompt.md](prompt.md), the required role workflows, definitions and
shared dependencies through [remote setup](../setup.md#store-and-run-remote-workflows).
Store exact resource bindings and a routing manifest in each owning account's
common area. Author instructions in this repository, then use the
[deployment workflow](../deploy.md) to publish and verify changes. Scheduled
runs use the deployed copies as their execution source; private runtime state
and run history remain in MCP storage across deployments.

Create a minimal ignored bootstrap prompt under `examples/.operations/` that
names the authorized MCP connections and full logical paths for the stored
manifest, bindings and scheduled workflow. It should read those files, resolve
Agent/common targets through the manifest, and follow the stored instructions.
It must report missing files instead of using local workflow copies. Supply one
completed deployment ID shared by the participating account manifests; stop
before content mutations if deployment is incomplete or IDs differ. Supply one
stable invocation run ID, or let the workflow use the unique run-directory
basename supplied by the wrapper. Keep actual identities out of public templates.
Select the already-authorized targets; scheduling does not grant access or
authorize publication by itself. Keep the public example account-neutral.

Run it manually first:

```sh
bash /absolute/path/to/index-alpha/examples/scheduling/run.sh \
  /absolute/path/to/index-alpha/examples/.operations/scheduled-prompt.md
```

Each invocation creates a unique directory under
`examples/.state/scheduled-runs/` containing raw `events.jsonl` stdout,
`stderr.log`, `summary.md` (the final model response), the submitted `prompt.md`,
start/finish timestamps, `exit-code`, and the Agent's `mcp-observations.md`.
Logs are deliberately unfiltered and may contain temporary tool credentials;
keep them local. The runner uses private file permissions and does not delete
logs. A missing summary or observations file can mean the model failed before
producing it; inspect the exit code and stderr.

The host records edit-mode invocation progress and terminal results through MCP
in `common/runs/<run-id>.json` for each participating account. Follow the
[run-tracking contract](../workflow.md#mcp-storage-owns-deployed-workflows-and-run-tracking):
create-only start, guarded stage/terminal updates, one host writer, and current
platform reconciliation after interruption. Run records are workflow tracking,
not copies of content or raw logs and not distributed locks. A zero CLI exit
does not establish completed stages or a successfully saved terminal record.
Keep credentials, raw logs and temporary binary files with the host; keep sparse
Agent state in owner-private common storage. An explicitly read-only smoke
does not write run records unless separately authorized.

Set `CODEX_BIN` to an absolute CLI path and `RUN_LOG_ROOT` to override the log
location. Set PATH explicitly for cron, including the directory containing
Node when the installed Codex executable uses `/usr/bin/env node`.

## Optional manual bearer token

If your MCP server accepts a manually generated account token, Codex can read
it from an environment variable instead of MCP OAuth/Keychain. Keep the token
in an ignored local `.env` file with mode 0600. Source and export it in the
operator's shell wrapper; never put the value in the CLI arguments or public
configuration. Use a separate variable for each account connection.

The runner forwards arguments after the prompt path to `codex exec`, allowing
run-specific configuration without changing desktop OAuth settings:

```sh
set -a
source /absolute/path/to/index-alpha/examples/.operations/.env
set +a
bash /absolute/path/to/index-alpha/examples/scheduling/run.sh \
  /absolute/path/to/index-alpha/examples/.operations/scheduled-prompt.md \
  -c 'mcp_servers.example.bearer_token_env_var="INDEX_ALPHA_TOKEN"' \
  -c 'mcp_servers.example.required=true'
```

Replace `example` with the exact configured MCP server name. The token must
permit the named Agents and required read/write operations; expiry and revocation
still apply. `required=true` makes failed server initialization fail the CLI
instead of letting the model report blocked work with a successful process exit.
This mode can run directly from cron without Keychain access for MCP auth.
See Codex's [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference).

## Headless MCP write approvals

`-a never` prevents interactive approval prompts; it does not automatically
approve every MCP write. Tools requiring a prompt will fail in that mode.
For operations the owner has authorized for the scheduled workflow, use
per-tool overrides in the local wrapper, alongside the bearer settings:

```sh
-c 'mcp_servers.example.tools.create_evaluation.approval_mode="approve"'
-c 'mcp_servers.example.tools.update_page_markdown.approval_mode="approve"'
-c 'mcp_servers.example.tools.create_index_image_uploads.approval_mode="approve"'
-c 'mcp_servers.example.tools.write_workspace_file.approval_mode="approve"'
-c 'mcp_servers.example.tools.edit_workspace_file.approval_mode="approve"'
```

Pass these as additional arguments to run.sh, like the token overrides above.
List the authoring/page/image/ranking operations your workflow actually needs;
each participating account connection also needs the authorized workspace writes
for its host-owned run record and sparse checkpoints.
Reviewer connections need `create_evaluation`; formatter connections need
`create_evaluation` for compliant checks plus the two page-edit tools for actual
formatting. Author connections also need `create_evaluation` for freshness checks.
Do not auto-approve closure unless separately included in the requested workflow.
No account or resource authority is added by this host-side approval setting.
Use run-specific overrides to preserve desktop behavior. Codex documents these
settings in its [MCP tool configuration](https://learn.chatgpt.com/docs/extend/mcp).

## Schedule with cron

Create a small local wrapper that sets PATH and invokes the command above, then
add a crontab entry with `crontab -e`, preserving existing entries:

```cron
0 */2 * * * /bin/bash /absolute/path/to/local-wrapper.sh >> /absolute/path/to/cron.log 2>&1
```

This runs every two hours, on even-numbered hours in the Mac's system timezone. Verify that
timezone before installing. Cron runs while the computer is awake; it does not
replay missed launches after sleep. Raw logs and the minimal bootstrap stay in
Git-ignored folders; deployed bindings, instructions and run tracking use MCP storage.

## macOS Keychain: let cron dispatch a LaunchAgent

Direct cron execution may fail to read MCP OAuth credentials from the login
Keychain even when the same CLI command works in Terminal. Matching HOME and UID
does not recreate the GUI login session's security context. Apple explains this
in its [execution-context guidance](https://developer.apple.com/forums/thread/712005).
Use a GUI-session LaunchAgent for the credential-consuming process; cron can
remain the timer. Codex and its workflow still run headlessly.

1. Copy [launchagent.plist](launchagent.plist) to
   `~/Library/LaunchAgents/com.example.index-alpha-workflows.plist`.
2. Replace every absolute-path placeholder, including the Node/CLI directory,
   prompt, working directory and logs. Create the log directory before loading.
   Keep the file owned by your user and disallow group/world writes.
3. While logged into the Mac, validate and load it:

```sh
plutil -lint "$HOME/Library/LaunchAgents/com.example.index-alpha-workflows.plist"
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.example.index-alpha-workflows.plist"
launchctl kickstart "gui/$(id -u)/com.example.index-alpha-workflows"
```

Use a read-only connectivity prompt first. Confirm all configured MCP connections
work in the agent's logs, then stop the finished service with `launchctl bootout`,
configure your authorized edit prompt and load it again. Repeat the actual cron
handoff check; a successful Terminal invocation alone is insufficient evidence.

4. Have the existing cron wrapper call only:

```sh
exec /bin/launchctl kickstart "gui/$(/usr/bin/id -u)/com.example.index-alpha-workflows"
```

Leave out `-k`: it kills an already-running instance. The example agent has no
calendar schedule or RunAtLoad, so cron remains the single timer. A dispatch
exit code is not the workflow result; inspect the runner's summary and exit-code.
If using launchd's own StartCalendarInterval instead, remove the equivalent cron
entry to avoid two independent timers.

The user must have a GUI login session and an available login Keychain. If an
item-specific access prompt remains, authorize the actual requesting Codex
executable for the relevant items using Apple's
[Keychain access controls](https://support.apple.com/en-gb/guide/mac-help/kychn002/26/mac/26).
Do not grant every application access or put the login password in a script.
Do not copy signing-key partition commands into OAuth password-item repair.
This arrangement does not promise operation while logged out or with a locked
Keychain. Apple [prefers launchd for timed jobs](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html).

The runner's directory lock skips overlapping launches. A hard kill or reboot
can leave `RUN_LOG_ROOT/.lock`; after confirming no run is active, remove the
empty lock directory with `rmdir` before the next launch. The 45-minute limit is
an instruction to the Agent, not a process timeout. Each invocation is a fresh
Codex session and recovers content state from the platform.

Twelve invocations with three new cards per Index can create up to 108 cards per
day across the three examples. Due maintenance retains its existing per-run
limits; monitor backlogs and capacity in the summaries. Content quality may
yield fewer or no new cards. Stop the experiment by removing its cron entry;
that does not terminate an already-running process.

## Restart after a fresh database

Keep the local wrapper paused while rebuilding resources. Old Index/Agent IDs,
OAuth sessions, bearer tokens and grants are not proof of authority after a reset.
Follow [setup](../setup.md) to discover or recreate the intended resources and
update the stored MCP bindings/routing with actual returned IDs, including
Comment Monitor. Redeploy and verify instruction routing when identities change.
Verify the intended visibility explicitly; setup defaults new Indexes to private.

Before restoring the timer's content work:

1. Check every configured CLI connection using fresh `list_agents` and concrete target reads.
   Reauthorize or replace local tokens when required; do not print them.
2. Run one bounded manual invocation on the freshly bound targets. Confirm one
   exact-revision review evaluation, a compliant formatter evaluation or a real
   style revision, and Signal's reviewed ranking/monitor handoff. Verify committed
   receipts; a zero CLI exit alone does not prove completed workflow stages.
3. Keep findings open unless closure was explicitly requested. Record incomplete
   stages and the actual MCP error rather than declaring the pipeline successful.
4. Only after the owner requests resumption, remove the local pause guard and
   verify the intended single timer. Do not reinstall cron if its paused wrapper
   is already called by the existing entry. Logs from the previous database are
   historical evidence, not current resource bindings or completed checks.

This guide does not perform setup, smoke publication or schedule resumption.
