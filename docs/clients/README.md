# Client setup

Connect a client to the remote HTTP MCP endpoint `https://api.indexalpha.com/mcp`, then complete browser OAuth. Installing a skill supplies instructions; authorizing the MCP client supplies tools and bounded access. The client must support the current server protocol; configuration format alone does not establish compatibility.

See [skill installation](../guides/install-skill.md) for portable package setup, [concepts](../concepts.md) for permissions, and the [interactive connection guide](https://indexalpha.com/agents) for website setup. Start with your client's supported remote HTTP configuration, and confirm current options with its help/documentation.

## Codex

Install the skill by asking Codex:

```text
Install the index-alpha skill from index-alpha/index-alpha-public at path skills/index-alpha.
```

```bash
codex mcp add index-alpha --url https://api.indexalpha.com/mcp && codex mcp login index-alpha
```

Restart Codex after installation so it loads the new skill.

## Claude Code

Install the skill into `~/.claude/skills` or `.claude/skills`, then add the remote MCP server:

```bash
claude mcp add --transport http index-alpha https://api.indexalpha.com/mcp
```

If the server requires OAuth, start Claude Code and run `/mcp` to complete authentication.

## VS Code / GitHub Copilot

Install the skill into one of the VS Code skill locations described in the [skill installation guide](../guides/install-skill.md). Then add this to user MCP configuration or workspace `.vscode/mcp.json`:

```json
{
  "servers": {
    "indexAlpha": {
      "type": "http",
      "url": "https://api.indexalpha.com/mcp"
    }
  }
}
```

You can also use the Command Palette command `MCP: Add Server` or `MCP: Open User Configuration`.

## Cursor

Install the skill into `.cursor/skills/index-alpha` for Cursor-specific use, or `.agents/skills/index-alpha` for a portable project-local install. Then add this to `.cursor/mcp.json` in the project, or `~/.cursor/mcp.json` globally:

```json
{
  "mcpServers": {
    "index-alpha": {
      "url": "https://api.indexalpha.com/mcp"
    }
  }
}
```

If Cursor prompts for OAuth, complete the browser flow before using the tools.

## Windsurf / Devin Desktop

Install the skill into `~/.codeium/windsurf/skills`, `.windsurf/skills`, or `.agents/skills`. Then add this to `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "index-alpha": {
      "serverUrl": "https://api.indexalpha.com/mcp"
    }
  }
}
```

You can also add the server from Cascade: open `MCPs` in the Cascade panel, choose the remote/server option, enter the production MCP URL, and use Streamable HTTP.

## OpenCode

Install the skill into `~/.config/opencode/skills`, `.opencode/skills`, `.claude/skills`, or `.agents/skills`. Then add this to `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "index-alpha": {
      "type": "remote",
      "url": "https://api.indexalpha.com/mcp",
      "enabled": true
    }
  }
}
```

If authentication is not triggered automatically, run:

```bash
opencode mcp auth index-alpha
```

OpenCode also has an interactive setup wizard:

```bash
opencode mcp add
```

## Cline

Cline does not need a local skill to connect to Index Alpha tools. Add this remote MCP server through the Cline MCP Servers UI, or put this in the Cline MCP config:

```json
{
  "mcpServers": {
    "index-alpha": {
      "url": "https://api.indexalpha.com/mcp",
      "type": "streamableHttp",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

The Cline CLI wizard is:

```bash
cline mcp
```

## Gemini CLI

Gemini CLI can use the Index Alpha MCP server directly:

```bash
gemini mcp add --transport http index-alpha https://api.indexalpha.com/mcp
```

Equivalent `settings.json` entry:

```json
{
  "mcpServers": {
    "index-alpha": {
      "httpUrl": "https://api.indexalpha.com/mcp"
    }
  }
}
```

If OAuth is required, use `/mcp auth index-alpha` inside Gemini CLI.

## Sources and compatibility

Codex CLI commands were checked against the installed CLI help and [official MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). See also [official skill documentation](https://learn.chatgpt.com/docs/build-skills). Other client configuration examples were migrated from the official Index Alpha skill package; they have not been authenticated end to end in this repository setup. The website's connection guide and current client documentation should be consulted if a client changes its configuration format.
