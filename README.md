# Index Alpha

Create, organize, and maintain collections of links, notes, and pages with your AI agents.

Index Alpha keeps content in public or private **Indexes**. Connect an MCP client, approve its access, and let it work through an Index Alpha **Agent** with the permissions you choose.

This is the official home for Index Alpha skills, examples, guides, and platform bug reports and feature requests. The hosted application and its implementations are separate from this repository.

## Get started

1. [Open Index Alpha](https://indexalpha.com) and create an account or sign in.
2. [Connect your client](https://indexalpha.com/agents) and approve access in your browser. The remote MCP endpoint is `https://api.indexalpha.com/mcp`.
3. [Install the official skill](docs/guides/install-skill.md) if your client supports skills. It provides behavior and workflow guidance; the MCP connection provides tools and authentication.
4. Choose an eligible Agent, or create one intentionally, then try:

   > Use Index Alpha to create a private research Index with three useful notes about a topic I choose. Ask which Agent to use if needed, and return the Index link.

For the complete walkthrough, see [getting started](docs/getting-started.md). Explore the [prompt workflows](examples/README.md) for curated Indexes, evidence review, and consistent Markdown. Reading their definitions requires no account; applying them uses an authorized Agent.

## What's here

| Resource | Start here |
| --- | --- |
| Official portable skill | [skills/index-alpha](skills/index-alpha/README.md) |
| Runnable examples | [Examples catalog](examples/README.md) |
| Account, client, Agent, and Index concepts | [Concepts](docs/concepts.md) |
| Client configuration | [Client setup](docs/clients/README.md) |
| Guides and reference | [Documentation](docs/README.md) |
| Bugs, feature requests, and questions | [Platform issues](https://github.com/index-alpha/index-alpha-public/issues) |

## Help shape Index Alpha

Use this repository's issues for platform feedback, including the web app, Agents, skills, examples, and documentation. Describe the outcome you need and include a minimal reproduction when reporting a bug. Keep credentials and private content out of reports; use the [security reporting instructions](SECURITY.md) for vulnerabilities.

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and the contribution process. Frontend and backend implementations remain in separate repositories; this repository owns the shared user and agent resources.

## License

The skills, example code, and documentation in this repository are available under the [MIT license](LICENSE). This license does not grant access to the hosted service or rights to third-party content processed by the examples. See [NOTICE](NOTICE) for migration provenance.
