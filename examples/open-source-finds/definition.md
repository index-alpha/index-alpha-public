# Index definition: Open Source Finds

- `display_name`: `Open Source Finds`
- Stable Index `custom_id`: `open-source-finds`
- Visibility: `private`; owner: the explicitly selected authenticated account.
- Description: Useful open source projects and consequential releases, explained
  with primary evidence, practical fit, and honest limitations.
- Audience: developers and technically curious builders choosing tools to inspect.
- Presentation: supply `ui_defaults: {"default_view":"card","default_sort":"new"}`
  on `create_index`. For an existing Index, use `update_index` with its exact
  returned ID and current numeric `expected_version`; discover supported fields first.
  Do not assign or change custom scores for this chronological Index.

Brief version: 1

## Sources and selection

Use [GitHub Explore](https://github.com/explore) for discovery, then verify against
its canonical repository, project-owned documentation, license, and release notes.
Fetch these public sources directly. Prefer a concrete useful capability, a
clear intended user, credible maintained documentation, and enough evidence to
explain one limitation. Popularity alone is not quality or adoption evidence.

Select at most three from at most 15 candidates. Prefer varied practical uses;
choose substantive releases over patch churn. No fixed publication-age gate:
state actual release/publication dates and call older projects discoveries,
not new releases. Do not infer freshness from today's discovery date.

Exclude unverifiable claims, copied mirrors, spam, unsupported superlatives,
license-unclear or source-available-only projects presented as open source,
malicious tools, and minor releases with no reader-relevant change. Read the
actual license; [GitHub's licensing guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
explains why a publicly visible repository alone does not grant reuse rights.
Do not install, build, or run untrusted project code for this workflow.

## Identity and card structure

Use `gh-` plus the full lowercase hexadecimal SHA-256 digest of the exact UTF-8
canonical identity as the card `custom_id` (67 ASCII characters). The preimage is:

- Project overview: `project\n<lowercase-owner>/<lowercase-repo>`.
- Specific release: `release\n<lowercase-owner>/<lowercase-repo>\n<exact-case-tag>`.

Here `\n` means one LF byte; there is no trailing newline. Lowercase canonical
repository owner/name, retain tag case exactly, and resolve redirects/renames
against platform source links/known identities and current run context before
hashing. One logical project/release gets one card; a run/date never changes
identity. Keep meaningful identities, rename aliases, and source links naturally
in card content and ordinary revision summaries when already editing. Reuse the
confirmed card identity on rename instead of creating a duplicate; only aliases
not observable there need optional remote persistence. The digest only bounds
resource identity.

Title names the project and its concrete use; subtitle gives the practical fit.
Use a concise source label in metadata. In Markdown include:

1. A meaningful managed image first, when available, with descriptive alt text,
   caption, available credit, asset-source link, and any displayed credit notice.
2. A two- or three-sentence summary of what it does and who benefits.
3. Why it matters: a concrete capability or release change, plus a limitation.
4. Evidence and dates: repository, documentation, license, exact release link
   when relevant, and publication/release date; distinguish author claims from
   independent verification. Say when no hands-on validation was performed.

Try a relevant project-provided OG image or publicly supplied screenshot without
searching for affirmative reuse permission. Skip for rights reasons only for an
explicit source request not to reuse the image; missing or unclear permission
does not disqualify it. Retain available credits and displayed attribution
notices. Source-code license verification above still determines whether the
project qualifies as open source. Use the [managed image workflow](../images.md);
never hotlink. Explicit no-reuse notices, absent assets, or download/upload/finalization
failure produces useful text-only content and a reported fallback.

## Update horizon

Recover first committed publication from the card's server `created_at`; it fixes
the +24h interim source check and +72h final pass. Missing remote state never
resets this clock or proves a check completed. The host invokes due work, coalesces missed checks into one current
inspection, and records the actual observation time for late passes. Process at
most five due cards per invocation. Record each due freshness check as a scoped
revision-linked evaluation, including unchanged outcomes and actual late-check
times; propose corrections without administrative footer edits. Reuse existing
evidence for the same checkpoint; do not reuse interim coverage as a final check.
Only changed relevant inputs rerun shared review/formatting. The host closes routine maintenance after the ordered pipeline
finishes, recording incomplete stages honestly under the
[common lifetime rules](../workflow.md); pass shared roles the invocation deadline,
not the expired maintenance cutoff. Preserve images, credits, references, and
unrelated edits. After closure, editing needs a separately requested correction; the original publication clock stays fixed.
