# Markdown style standard

Style version: `2`.

Use these defaults unless the run supplies an explicit Index-specific override.
Apply only changes that preserve meaning and rendering. Keep a page's useful
structure; a short page does not need a fixed set of sections.

## Headings and spacing

- Use ATX headings (`## Heading`) with a space after the marker. Preserve the
  page title and heading text. Use a consistent hierarchy without inventing
  sections; report ambiguous structural problems.
- Put a blank line between headings and surrounding content, and between
  paragraphs, lists, tables, blockquotes, and fenced code blocks.
- Use one blank line between blocks when additional blank lines serve no
  purpose. Do not alter whitespace inside code or other literal content.
- Remove incidental trailing whitespace. Preserve intentional Markdown hard
  breaks, indentation, and whitespace that affects rendering.
- Keep prose paragraphs unwrapped where practical. Do not rewrite wording,
  split arguments, or merge separate paragraphs to impose a line-length rule.

## Lists, emphasis, and tables

- Use `-` for unordered list markers. Preserve list order, ordered-list start
  values, task-checkbox state, nesting, and paragraph boundaries within items.
- Prefer `**bold**` and `*italic*` for existing emphasis when conversion has
  identical meaning and rendering. Do not add emphasis based on editorial
  importance or alter literal asterisks and underscores.
- Keep existing data tables readable with a header separator and consistent
  pipes. Preserve cell values, alignment markers, escaped pipes, and row order.
  Do not convert prose or lists into tables or invent missing headers.

## Links, images, and literal content

- Preserve every link destination, citation, footnote identifier, and reference
  definition. Do not resolve, shorten, replace, or remove sources during
  formatting. Preserve heading anchors and links to them; leave headings alone
  when conversion could break an anchor.
- Preserve exact `media:<UUID>` image destinations, image order, alt text,
  captions, and credits. Do not substitute external image URLs.
- Preserve code and quotations verbatim, including language identifiers,
  indentation, commands, numbers, and punctuation. Do not guess a missing code
  language or fix apparent code errors.
- Preserve supported constructs such as footnotes, definition lists, `[TOC]`,
  explicit anchors, and escaped text. Leave unfamiliar syntax intact and flag
  it if it prevents safe formatting.

## Content boundaries

Preserve claims, caveats, dates, attribution, and the strength of conclusions.
Do not fact-check, summarize, translate, change tone, or add boilerplate sections
as a formatting action. Removing identifiable legacy administrative footers under
[completion.md](../completion.md) is the explicit administrative exception; do not
replace them with another page log.
Report apparent content problems for the owning Agent.

Never introduce AI-authorship labels or generic summary disclaimers. Flag any
existing wording for the author to remove; preserve useful source attribution
and evidence limits.
