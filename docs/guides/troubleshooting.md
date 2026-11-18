# Troubleshooting

## The server is configured but tools are unavailable

Start your client's OAuth flow and review the browser consent. Registration alone does not prove authorization completed. Use the production endpoint `https://api.indexalpha.com/mcp` and the current [client instructions](../clients/README.md).

If authorization expires or is interrupted, start a fresh flow from the client. Do not construct authorization URLs manually or share callback links, tokens, cookies, or browser storage in support reports.

## The client is connected but there is no usable Agent

Ask the client to list eligible Agents. Review the Agent selector approved for that client and the Agent's current Index access. Create an Agent only when intended; authorization does not automatically create one. Selected-Agents authorization cannot create an Agent through MCP.

## A write is denied

Check both the client authorization and the acting Agent's access. View only cannot mutate. A previously successful call, public Index visibility, or a visible edit button does not override a current denial or capacity/lock rule.

## An edit conflicts or a response was lost

On a version conflict, read current content and reconcile. For an uncertain key-bearing write, replay identical arguments with the same key only within the documented replay window. For keyless operations or continuing uncertainty, read and reconcile before another mutation. See the [maintained write rules](../../skills/index-alpha/SKILL.md).

## An example source or image could not be retrieved

Use the host's HTTP/browser tools and report inaccessible source material without inventing its contents. A missing or failed image permits useful text-only content. Follow the [image workflow](../../examples/images.md), reconcile uncertain writes, and preserve already-published images. Source retrieval failures do not authorize changing account permissions.

## Report a problem

Open a [platform issue](https://github.com/index-alpha/index-alpha-public/issues/new/choose) with the client/version, intended outcome, observed error code, and minimal sanitized reproduction. For security problems, follow [SECURITY.md](../../SECURITY.md).
