# Agents And Access

Use this reference for choosing an actor, creating personal/open Agents, cross-account Index work, and grant management.

## Account, Client, Agent, Index

Normal signup creates a personal Agent with full/write owner authority and a private Index. Discover and reuse them; signup does not issue a token or connect a client. Configure OAuth or a manual token through the product UI. A new client connection does not require a new Agent, and unavailable default resources must not be automatically recreated.

The account owns the client authorization. Codex or another MCP application is the client. An Index Alpha Agent is a product identity with its own owner and resource relationships; creating it does not start an autonomous process or schedule.

Account authorization has a read/write ceiling and an Agent selector: all current/future eligible owned Agents, or selected owned Agents. `list_agents` discovers eligible identities under that authorization. It does not prove that each Agent can write every Index.

All content/index/connection/grant tools require an explicit `acting_agent_id`. Account tools `list_agents`, `create_agent`, and `retrieve_account_capacity` reject this field. Workspace tools and `update_agent_metadata` also omit it; see [Agent workflows](agent-workflows.md) for their target and authority rules.

Choose a named Agent when eligible, otherwise use relevant current authority. When several materially different Agents fit, ask which identity to use. If none qualifies, explain the access gap; do not create an Agent or change credentials to bypass the result.

## Public Index Reads

An eligible owned personal or open-connection Agent can read a known public Index without
owner consent or a grant when enabled by the server. This does not create a
connection or expand a grant. Public visibility authorizes only seven current-read
tools, not writes, search, history or evaluations. Private Indexes require
applicable explicit authority; a switch to private removes public-only access.
Follow [public Index reading](public-index-reads.md) for the exact tools and calls.

## Personal And Open Connections

These are values of `connection_mode`, not the separate workflow `openness` field.

- `personal`: other accounts cannot establish viewer connections to this Agent.
- `open`: other accounts can establish viewer connections within the Agent's default policy.
- Agent connection mode does not set Index visibility. Index visibility is `private` or `public`.
- Listing/connections/profile presence, OAuth protocol scope, and previews are not proof of effective content authority.
- For grant-backed cross-account operations, an owned Agent with open connection mode can use a known other-account Index within the resource owner's grant. Enabled public-only reads use the separate public-visibility authority above. Account discovery and new Index creation remain within the account authorizing the client.

## Explicit Agent Creation

`create_agent` is an account tool. It requires read/write authorization and the all-eligible-Agents selector. A selected-Agents authorization cannot create an Agent. Creation returns Agent metadata plus the protected owner grant, not a runtime token.

Required fields:

- `idempotency_key`: stable for the requested creation.
- `agent_name`: display name.
- `owner_username`: authenticated account username from trusted account context. Ask if unavailable; never borrow a username from another account's Index or relationship.
- `connection_mode`: `personal` or `open`, reflecting the user's intent.
- `default_policy`: both `reach` and `access`.

Policy values:

| Field | Meaning |
| --- | --- |
| `reach: full` | Current/future owner Indexes; omit or empty `owner_selected_index_ids`. |
| `reach: restricted` | Only active owned Index UUIDs in `owner_selected_index_ids`; empty selection grants no Index access. |
| `access: read` | Read operations within current authority. |
| `access: write` | Read and mutations within current authority. |

Use a scope that fits the request. If creation intent leaves material connection-mode or access choices unresolved, ask for them before creating. Optional `agent_id` is a product Agent UUID, not the MCP client's OAuth identifier; omit it to let the server generate it. Optional `agent_description`, `agent_uri`, and `logo_uri` are profile metadata, not credentials. New slugs are generated and immutable.

The MCP surface currently creates Agents, discovers them, and manages eligible grant revocations. `update_agent_metadata` changes only workflow openness and the external source-code link. Other profile/policy updates, delegated-grant creation, browser consent, client authorization removal, and human account signup use their respective product UI/API workflows; do not invent MCP tools for them.

## Workflow Openness

`connection_mode: personal|open` controls whether other accounts may connect. The separate `openness: open|closed` controls workflow-file disclosure; either connection mode can have open or closed files. These fields are independent of Index visibility. New Agents start closed. MCP reads of open Agent files require credentials; browser reads can be anonymous in public app mode and require sign-in in private mode. All checkpoint files inside an open folder are disclosed; foreign readers cannot edit them or act as that Agent. Common files remain owner-private. Opening files grants no Index access. See [stored workflows](agent-workflows.md) for source links, file writes and private checkpoints.

## Grants And Revocation

A product grant has `grant_id`, `resource_owner_user_id`, `grantee_agent_id`, `acting_principal_id`, `kind`, `status`, `protected`, `policy`, and `version`. The policy includes `reach`, `access`, and `selected_index_ids`.

To inspect an owned Agent's grants, use `list_agent_grants` with `agent_id` equal to `acting_agent_id`; current owner read authority is required. Paginate with `next_token`.

To fulfill an explicit revoke request:

1. Resolve the exact non-protected grant or grants for that same Agent. Discovery of another account's Agent does not grant management rights.
2. Call `revoke_agent_grant` for one `grant_id`, or `revoke_agent_grants_batch` with `grant_ids` and a stable `idempotency_key`. Current owner write authority is required.
3. Report the committed result and its practical scope. Keep internal UUIDs out of ordinary prose unless requested.

Protected `owner` grants are not revocable through these tools. Batches cannot mix Agents or bypass self-target authority. Product grant revocation is distinct from disconnecting a client's account OAuth authorization; direct the latter to the account's Apps and tokens workflow.

## Denials And Current State

Effective access is bounded by all applicable layers: the client credential's account access and Agent selector, the selected Agent's eligibility, applicable explicit grants or enabled public-read authority, and current resource/lifecycle policy. A broader Agent grant cannot override a read-only credential, and a write-capable credential cannot grant an Agent access to an unrelated Index. Public Index visibility alone grants no MCP write authority. A past successful call or a displayed connection does not override a current denial. Correct the target, choose an authorized actor, or explain the required authorization.

Client registration, browser sign-in, OAuth approval, and Agent creation are separate actions. A client can have account access without any eligible content Agent. Use the host's normal fresh login flow when credentials expire; never construct or expose authorization tickets in a response.
