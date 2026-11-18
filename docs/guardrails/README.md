# Repository guardrails

## Scope

All public skills, examples, documentation, and contribution tooling.

## Rules

- Keep the repository private until its owner explicitly authorizes publication.
- Publish only skills, examples, user guides and contribution tooling. Do not commit internal work records, private source references, application implementation, architecture, credentials or operational evidence.
- Preserve `skills/index-alpha` as the portable skill package; host-specific metadata supplements it.
- Examples MUST NOT store Index Alpha credentials. Prompt workflows read public sources directly; platform mutations require an authorized MCP Agent and an in-scope write request. No custom ingestion runtime is required.
- Current MCP schemas and authorization rules govern examples; installation alone grants no access.
- Public checks MUST run without a private backend checkout or production credentials. Backend contract checks are an additional maintainer lane.
- Changes MUST preserve unrelated local work and use no new dependency without owner authorization.

## Verification

Run `bash scripts/check.sh` for public checks, including private-reference and work-record checks. For MCP guidance or operation-plan changes, request a maintainer contract validation. See [contributing](../../CONTRIBUTING.md) for prerequisites. Fixture checks do not establish deployed MCP readiness.
