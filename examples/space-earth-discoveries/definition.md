# Index definition: Space & Earth Discoveries

- `display_name`: `Space & Earth Discoveries`
- Stable Index `custom_id`: `space-earth-discoveries`
- Visibility: `private`; owner: the explicitly selected authenticated account.
- Description: Space and Earth observations explained with primary evidence,
  honest uncertainty, meaningful images, and complete image credits.
- Audience: curious general readers seeking clear explanations of science.
- Presentation: supply `ui_defaults: {"default_view":"card","default_sort":"new"}`
  on `create_index`. For an existing Index, use `update_index` with its exact
  returned ID and current numeric `expected_version`; discover supported fields first.
  This chronological Index does not need custom scores or a ranking Agent.

Brief version: 1

## Sources and selection

Discover via [NASA Webb](https://science.nasa.gov/mission/webb/) and
[NASA Earth Observatory](https://science.nasa.gov/earth/earth-observatory/).
Read the original official article and asset page directly over HTTP/browser.
Follow its linked research when needed for a material claim; identify a paper
as unread or inaccessible rather than implying it was checked.

Inspect at most 15 candidates and select at most three with a clear observation,
reader-relevant explanation, primary evidence, and explicit limits. Prefer a
mix of space and Earth when equally supported. Novelty is not a requirement:
an older discovery can be useful when its dates and context are clear.

Exclude sensational extrapolation, unsupported causal claims, speculative
life/health predictions, duplicates, and stories whose only evidence is a
headline or inaccessible page. Distinguish an observation, an interpretation,
and a hypothesis; one image or paper does not establish scientific consensus.

Publication date, observation/acquisition date, and discovery date are distinct.
State the first two when available; label unknown dates. A newly published
image of an old observation is not a new observation. Describe composites,
processed/false-color views, illustrations, and artist concepts accurately.

## Identity and card structure

Use `nasa-` plus the full lowercase hexadecimal SHA-256 digest of the exact UTF-8
canonical official article URL as the card `custom_id` (69 ASCII characters).
Resolve redirects, lowercase scheme and host, remove the fragment and known
tracking parameters (`utm_*`, `fbclid`, `gclid`), and retain identity-bearing URL
components, including path case and nontracking query parameters. The preimage
is that canonical URL alone, with no trailing newline.

Resolve redirects and cross-posts against platform source links/known identities
and current run context before creating; one discovery does not become a new
card on another official page or later run. Keep the canonical URL, meaningful
aliases, and source links naturally in card content and ordinary revision
summaries when already editing. Reuse the confirmed card identity for a known
alias; only aliases not observable there need optional remote persistence. The
digest only bounds resource identity; it does not establish equivalence between
different stories.

Title states the observation without hype; subtitle explains why it matters.
Use a short official-source label in metadata. Markdown includes:

1. A meaningful managed image first when successful, with descriptive alt text,
   accurate caption, available full asset credit, original asset link, and any
   displayed credit notice.
2. A two- or three-sentence explanation of what was observed and why it matters.
3. Evidence and limits, separating source interpretation from direct observation.
4. Article publication and observation/acquisition dates, plus links to the
   official article, asset page, and research actually consulted.

Do not label the page as AI-written or append generic authorship/accuracy
disclaimers. Attribute NASA source material through the links and image credits
above; state scientific limits in the relevant explanation.

## Images and attribution

Prefer the official article's relevant Webb/Earth image. Retain available full
credited collaborators and displayed attribution wording/links, not just “NASA.”
Do not search for affirmative reuse permission. Skip for rights reasons only
when the source explicitly requests no reuse or prohibits that use; missing or
unclear permission is not a reason to skip.

Use the [managed image procedure](../images.md): direct public download into
optional ignored `examples/.state/` assets, managed upload and committed Markdown finalization, no hotlinks.
Preserve scientific context when cropping is prohibited or would mislead; choose
another suitable asset or text-only. Explicit no-reuse notices, absent assets, or
download/upload/finalization failure does not block useful text publication;
report the exact fallback. Do not invent a visual to represent measured data.

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
