# MCP reference

Production endpoint: `https://api.indexalpha.com/mcp`.

Use a client supporting the server's current remote HTTP MCP contract and browser OAuth. The connected server's exposed schemas and `platform://mcp/usage-guide` are the runtime authority. The package's local contract checks do not establish deployed availability or a successful OAuth connection.

The official skill maintains the detailed references:

- [Tool inventory, fields, resources, response shapes, and pagination](../../skills/index-alpha/references/mcp-server-map.md)
- [Accounts, Agents, and access](../../skills/index-alpha/references/agents-and-access.md)
- [Known public Index reads](../../skills/index-alpha/references/public-index-reads.md)
- [Public card references and destination-local ranking](../../skills/index-alpha/references/card-references.md)
- [Stored Agent workflows and guarded workspace files](../../skills/index-alpha/references/agent-workflows.md)
- [Content workflows and recurring updates](../../skills/index-alpha/references/user-workflows.md)
- [Behavioral evaluation scenarios](../../skills/index-alpha/references/evaluation.md)

This guide links to those references instead of duplicating a second tool catalog. Account tools and actor tools differ. Content writes require the current versions and request keys specified by their actual schemas.
