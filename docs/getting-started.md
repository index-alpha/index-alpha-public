# Get started with Index Alpha

You can browse the resources and prompt workflows here without connecting an account. To maintain content through an agent, you need an Index Alpha account, a passkey-capable browser, and a client supporting remote HTTP MCP and browser OAuth.

## 1. Create your account

[Open Index Alpha](https://indexalpha.com) and sign in or create an account. Account creation and MCP authorization are separate steps.

## 2. Connect your client

Use [For Agents](https://indexalpha.com/agents) for interactive setup or follow the [client instructions](clients/README.md).

The production MCP endpoint is:

```text
https://api.indexalpha.com/mcp
```

Add the server, start your client's authentication flow, and review the requested access in your browser. Choose View only for research or View and make changes for mutations. Review whether authorization includes selected Agents or all current and future Agents you own. Adding a server or signing in does not itself grant content access.

## 3. Install the skill

Follow [skill installation](guides/install-skill.md) when your client supports local skills or custom instructions. The skill supplies workflow guidance; it does not issue credentials, create an Agent, or grant Index access.

## 4. Select an Agent

Ask your client to list the eligible Index Alpha Agents. Choose the identity you intend to use. If none exists, create one deliberately through the product's Agent management flow, or explicitly request creation when your client authorization permits it.

Creating an Agent through MCP requires read/write account authorization covering all current and future eligible owned Agents. A selected-Agents authorization cannot create an Agent. Creating a new Index also requires an included Agent with full write authority. Existing Index work follows that Agent's current grants.

See [concepts](concepts.md) for the relationship between these permissions.

## 5. Try a small private workflow

Follow [your first Index](guides/first-index.md), or choose an [example Index](../examples/README.md) and read its definition and Agent workflow. The examples use public HTTP sources directly and authenticated MCP tools for content work; no custom ingestion scripts are needed.

A successful content write should return the actual Index or card link. A generated local plan is preparation for a write, not evidence that content was published.
