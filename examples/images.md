# Images for card-view Indexes

Attempt one relevant leading image for every new card. For URL stories in
Signal to Noise, first try the original article's `og:image`. A missing,
unusable, or failed image must not prevent otherwise useful text content.
Do not select worse stories just because they have pictures.

Do not search for affirmative reuse permission or require a license grant for
image selection. Skip for rights reasons only when the source explicitly asks
that the image not be reused or prohibits that use. Missing or unclear permission
is not a reason to skip. Retain available credits and source links; do not infer
or claim that source silence establishes permission.

## Select and download

1. Reuse the original page HTML cached by the primary Agent in this run; fetch
   it with host HTTP/browser tools only if metadata is missing or stale. Inspect its
   original HTML metadata for `og:image` (prefer a usable HTTPS variant when
   provided). Resolve relative image URLs against the page's final URL/base.
   Read its caption, alt metadata, and credit when available. Open Graph is a
   source of representative image candidates, not a guarantee of suitability.
   See the [Open Graph specification](https://ogp.me/).
2. If the first image is a logo, tracker, unrelated thumbnail, or unusable
   asset, try at most one other relevant image from that same source page or
   its directly linked official media page. For science, prefer the credited
   original image accompanying the story. Honor an explicit no-reuse notice
   encountered on the source or asset page; do not conduct a separate permission
   search. Do not generate a
   substitute image or search indefinitely for decoration.
3. Download the binary to a temporary host asset directory, for example
   `examples/.state/<account-label>/<index-id>/assets/<source-id>.<extension>`.
   Use supported
   public HTTP URLs; do not follow source-supplied URLs to local/private network
   addresses or forward platform credentials. Limit attempts to two candidates
   and one bounded retry for a transient download/upload failure per card/run.
4. Verify that the result is a readable image rather than an HTML error page,
   that MIME type/extension match, and that its size is allowed by the current
   upload instructions. Inspect it with the host's image tools where available.
   Record source page, original image URL, available credit, any explicit
   no-reuse notice, intended alt text,
   local filename and failure reason in the run context; persist only useful
   asset/cache details with the host when needed. Remote workspace `state_dir` holds text only; do not upload image binaries as workspace files. Do not manufacture credits.

The article must still be read independently of its image. An OG image is not
evidence for the article's claims. NASA-hosted images can include third-party
credits; preserve the selected asset's full credited collaborators and any
explicit no-reuse notice encountered on its source page.

## Upload and finalize

In report mode keep the proposed image local. In edit mode:

1. Reserve one Index-owned image with `create_index_image_uploads`, using the
   exact actor/Index and a stable request key. Confirm the returned reservation
   state. Reuse an already-ready same-Index image when appropriate rather than
   uploading it again.
2. For an uploadable reservation, POST the downloaded file to the exact returned
   upload URL as multipart/form-data, field `file`, with filename and image MIME
   type. Never attach the Platform bearer token or persist upload tickets.
3. Before the original `expires_at`, create or version-edit the card page with
   the exact returned `markdown_destination` in `![Descriptive alt](media:...)`
   near the beginning of the body. Include a human-readable source credit/link
   where relevant. Initial Markdown save finalizes the image; byte upload alone
   does not complete it. Use the actual returned destination, not `media:...`.
4. Mark the image published only after the content save commits. Ready images
   may be reused within the same Index after original reservation expiry.
   External image URLs and HTML image loaders are not saved as card images.

## Failure and refresh

If an image is absent, unavailable, unsuitable, too large, disallowed, or fails
upload/finalization, remove the unpublished image reference from the proposed
Markdown and publish useful text after reconciling any uncertain write. Record
the failure in the run report and an optional receipt, not a warning in every card.
Do not replay a changed request under its old key or renew an expired reservation
by replaying its key. Expired/unusable reservations need a fresh logical request
only after reconciliation and within the run's retry budget.

On an uncertain content save, first determine whether a card and image already
committed before attempting fallback. Preserve ready images during later edits;
do not replace a working image because a later OG fetch fails. Do not reserve
more images automatically on every refresh. Retry a known failed image at most
once at a due maintenance checkpoint, within the card's fixed maintenance window.
