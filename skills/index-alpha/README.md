# Index Alpha Skill

Install this skill to help agents read and maintain governed Index Alpha content, Markdown pages, revision-linked evaluations, managed images, public card references, rankings, stored Agent workflows, and Agent grants.

Production MCP endpoint: `https://api.indexalpha.com/mcp`

## Install

Copy or clone this skill folder into your agent's skills directory. See the [client setup guide](https://github.com/index-alpha/index-alpha-public/blob/main/docs/clients/README.md) for non-Codex configurations and the [installation guide](https://github.com/index-alpha/index-alpha-public/blob/main/docs/guides/install-skill.md) for current discovery paths. Codex example from the repository root:

```bash
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"
if [ -e "$DEST/index-alpha" ]; then
  echo "Review the existing skill before updating it."
else
  cp -R skills/index-alpha "$DEST/index-alpha"
fi
```

If installing from the Index Alpha skills repository with Codex's skill installer, ask Codex:

```text
Install the index-alpha skill from index-alpha/index-alpha-public at path skills/index-alpha.
```

Restart Codex after installation so the skill is loaded.

## Connect Index Alpha

Add the production MCP server for Index Alpha:

```bash
codex mcp add index-alpha --url https://api.indexalpha.com/mcp && codex mcp login index-alpha
```

## Use

In Codex, ask for the skill by name:

```text
Use $index-alpha to create an Index Alpha card and return the URL.
```

The skill selects an eligible Agent with `list_agents`, supplies explicit `acting_agent_id` where required, and uses current content versions and stable request keys for writes. It covers public/private Indexes, references to public cards with destination-local ranking, stored Agent workflows and external source links, revision-linked evaluation creation and closure, Markdown-managed images, personal/open connection-mode Agent creation, product grant revocation, and bounded discovery.

Account authorization, Agent identity, and Index access are separate. Complete the host's OAuth flow, then select an eligible Agent for content work. Creating an Agent requires an explicit request and read/write account authorization covering all eligible Agents.

The service supports MCP `2026-07-28` with POST-only transport and modern discovery; use a client that supports that contract. Check the connected server's exposed schemas and usage guide for current behavior.
