# Install the official skill

The portable package is [`skills/index-alpha`](../../skills/index-alpha/README.md). Its name remains `index-alpha` across clients; client-specific metadata supplements the same package.

Connect the MCP server separately using the [client setup guide](../clients/README.md). Repository access is required while a copy is private. Public releases can be cloned without authentication.

## Install from a checkout

Clone this repository (use an authenticated Git credential helper if access is restricted):

```bash
git clone https://github.com/index-alpha/index-alpha-public.git
cd index-alpha-public
```

Choose a destination supported by your client. For a personal Codex installation, use its current shared skill location:

```bash
DEST="$HOME/.agents/skills"
mkdir -p "$DEST"
if [ -e "$DEST/index-alpha" ]; then
  echo "An index-alpha skill already exists. Review it before updating."
else
  cp -R skills/index-alpha "$DEST/index-alpha"
fi
```

Older Codex installations may use `${CODEX_HOME:-$HOME/.codex}/skills`; follow the skill discovery rules for your installed client and use one deliberate installation. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

| Client | Example skill destination |
| --- | --- |
| Claude Code | `~/.claude/skills/index-alpha` or `.claude/skills/index-alpha` |
| Cursor | `.cursor/skills/index-alpha` where supported |
| GitHub Copilot | `.github/skills/index-alpha` where supported |
| Windsurf | `.windsurf/skills/index-alpha` where supported |
| OpenCode | `.opencode/skills/index-alpha` where supported |

Use your client's current documentation to confirm discovery locations. For a client without native skills, provide `SKILL.md` and the `references/` directory as supporting custom instructions. Reload the client if it does not discover the new skill automatically.

## Update intentionally

Fetch and review changes in this checkout, then replace or merge your installed copy deliberately. Preserve local customizations and avoid leaving multiple competing copies of the same skill. Use a reviewed commit or release tag when a reproducible installation is needed; the first release tag will be chosen after initial review.

Installing a skill does not authorize an account, select an acting Agent, or grant Index access.
