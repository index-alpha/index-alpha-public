# Release and publication checklist

This repository distributes skills, prompt examples and user documentation.
Publishing it does not publish the application implementation or grant access
to the hosted service. The repository owner decides when to change visibility.

## Before committing

- Review `git diff` and the exact proposed file list. Include new linked skill
  references and workflow documents, not just previously tracked files.
- Run `bash scripts/check.sh` from a clean checkout/export with the documented
  prerequisites. Public checks require no credentials or private application
  source. Request the separate maintainer MCP-schema contract check when tool
  guidance changes; record its actual result.
- Keep local client configuration, tokens, downloaded assets, run logs, runtime
  bindings and internal work records out of the commit. Ignore rules do not
  protect files already tracked or force-added; review the index as well.
- Confirm the MIT license and retained attribution in [NOTICE](../NOTICE) cover
  the material being contributed. Third-party source content and media retain
  their own rights; the repository license does not relicense those assets.

## Before changing visibility

- Review all reachable Git history, branches, tags and release assets for
  credentials, private content and personal information. Current-file checks
  alone do not establish clean history. If a credential was ever committed,
  revoke/rotate it and plan any history cleanup explicitly before publication.
- Inspect repository description, issues, discussions, PR attachments, Actions
  logs/artifacts and wiki content that could become public with the repository.
- Include closed PR diffs in that review: removing data from current files or
  rewriting reachable branches does not remove GitHub-held patches or cached
  views. If unacceptable private material remains, keep this repository private
  until an approved cleanup is verified, or publish a clean reviewed snapshot
  into a separate repository. Do not delete history or accept disclosure as an
  incidental documentation change.
- Finalize [SECURITY.md](../SECURITY.md) with a concrete, monitored private email
  address or reporting form and verify receipt through that route. Obtain the
  address from the owner; do not infer a working mailbox from the domain name.
  GitHub's repository-level private vulnerability reporting is available for
  public repositories, so enabling it is a post-switch step, not a prerequisite
  that can be verified on a private repository.
- Verify issue forms, maintainer ownership/access and branch protections.
  Require the public CI checks on the reviewed commit; keep write permissions
  and Actions secrets scoped to what the workflow needs.
- Confirm getting-started, client authentication and skill-install links work
  for an account without privileged access. Check at least one fresh client
  connection and a small authorized workflow; offline tests do not prove these.
- Review the resulting tracked snapshot, then obtain the owner's explicit
  publication decision. Do not upload a whole working directory containing
  ignored operational files as a source archive.

## Immediately after the approved visibility change

- Enable GitHub private vulnerability reporting and verify **Report a
  vulnerability** from a non-maintainer account before announcing the launch.
  Update `SECURITY.md` with the working reporting link, retaining the verified
  fallback contact. Follow [GitHub's reporting configuration guide](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/configure-vulnerability-reporting/configure-for-a-repository).
- Configure required CI and branch protection or rulesets as supported by the
  repository's plan and visibility. An unavailable private-repository setting is
  not proof that the public repository is protected.
- Verify anonymous clone, the reviewed release contents, installation links,
  and private reporting. Announce only after those checks pass. Retain private
  operational state and the original private repository if using a clean import.

## Release and deploy

Choose a reviewed commit/tag for reproducible installation and publish release
notes describing user-facing behavior and validation limits. Source publication
and [workflow deployment](../examples/deploy.md) are separate actions: scheduled
work uses verified Agent/common storage, and a repository release alone does not
update it. Deploy the selected source only when authorized, preserve private run
state, and record the source revision and readback result in its deployment.
