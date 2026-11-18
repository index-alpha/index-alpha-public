# Contributing

Use this repository for improvements to official skills, examples, guides, and platform feedback. For product bugs or feature requests, [open an issue](https://github.com/index-alpha/index-alpha-public/issues/new/choose) describing the outcome you need. Maintainers route frontend/backend implementation while the central issue tracks the user-facing result.

## Local setup and checks

Repository-check prerequisites: Git, Bash, Ruby with standard-library JSON/YAML, and Python 3.11 or newer. Checks use standard libraries only. The prompt examples need no Python application or custom scripts; their host supplies public HTTP retrieval and authenticated MCP tools.

From the repository root:

```bash
bash scripts/check.sh
```

Public checks validate repository documents, workflow links, JSON/YAML examples, and skill metadata, and run focused validator regression tests. No virtual environment or package installation is needed. They require no private backend checkout, service credentials, or network access. They do not execute Agent prompts or write to Index Alpha.

For MCP guidance or operation-plan changes, request a maintainer contract run in
your PR. Maintainers compare documented tools and invocation arguments against
current MCP schemas. Public contributors need no application source checkout.
Local checks do not establish deployed transport, OAuth, or live mutation readiness.

## Make a contribution

1. Read [AGENTS.md](AGENTS.md) and the linked guardrails/work workflow.
2. Use a focused branch and keep the diff small. Do not add a dependency without prior agreement.
3. Keep the portable skill in `skills/index-alpha/`. Use relative links inside the package so installation stays self-contained.
4. Give prompt examples clear inputs, bounded tasks, outputs, source/image failure behaviour, and stop conditions. Document live-read/write requirements and distinguish document checks from actual execution. Never commit tokens, local configuration, generated output, or private content.
5. Run the relevant checks and include commands, results, and any gaps in the PR. Keep private work records out of commits; include public validation results in the PR.

Repository visibility changes and releases require an explicit owner decision. See the [release checklist](docs/releasing.md) before publishing.

## Issue organization

Use one type label (`type:bug`, `type:feature`, or `type:question`) and relevant areas such as `area:web`, `area:agents`, `area:skills`, `area:examples`, or `area:docs`. Do not copy private implementation details into a future public issue. Use [SECURITY.md](SECURITY.md) for vulnerabilities.

## Ownership and releases

CODEOWNERS identifies the current maintainer. Review required behavior and example definitions before release. Use reviewed commits for reproducible installs; release tags and a public launch follow owner review. Adding packages, SDKs, or plugins should meet an actual user need rather than create empty directories.
