# Index Alpha Skill Evaluation

This is the skill release checklist. For product evaluation messages and their
open/closed lifecycle, read [content-evaluations.md](content-evaluations.md).

Use these scenarios after a contract refresh. Evaluate the choices and arguments, not exact prose. Tests may simulate MCP responses; avoid live mutations solely to test a skill.

## Release Checks

- Run `bash scripts/check.sh` from the examples and skills repository; request maintainer MCP contract validation for guidance changes.
- Run the skill-creator `quick_validate.py` when its runtime/dependencies are available.
- Verify the entrypoint routes to content, access, tool-map, card-reference, Agent-workflow, content-evaluation workflow, and release-check references.
- Check account tools versus actor tools, current registered inventory, request keys, required versions, image finalization, and grant targets.
- Local schema/test success proves source alignment, not deployed server or OAuth readiness.

## Behavioral Cases

| Request / context | Expected observable decisions |
| --- | --- |
| Public Index, personal Agent, “Can my colleague edit now?” | Distinguish content visibility, Agent connection mode and authorized writes; public visibility alone grants no MCP write authority, and personal Agents reject other-account viewer connections. |
| Write-capable Agent, read-only client credential, “Save this.” | Explain the credential ceiling; Agent policy cannot override it. No write attempt to bypass authorization. |
| Known custom_id and version, “Evaluate this exact revision.” | Resolve card UUID and current body evidence, then find the matching revision UUID using version/hash. Neither custom_id nor version is a revision UUID. |
| Timed-out create, same custom_id but proposed new request key | Reconcile/replay the original identical request and key within its window; a lookup key is not upsert or duplicate protection. |
| “Rename the Index and give me its new URL.” | Update only requested metadata, retain the immutable slug and use returned canonical links; do not derive a new route from the name. |
| “Save this link to my Index.” with a trusted selected actor/destination | Reuse context; retrieve the source with host tools when possible, prepare one complete card, then report the committed receipt. No new Agent/Index, exhaustive scan or mandatory confirmation read. |
| Newly signed-up account connects a second app | Discover/reuse the signup-created personal Agent and private Index; app connection is separate from Agent creation. |
| Empty writable Index discovery | Explain/resolve the destination or access gap; do not automatically create another Index. |
| Two writable Indexes have the requested name | Inspect plausible candidates or ask; do not guess or create a third Index. |
| “Save this inaccessible link as a bookmark.” | Save the supplied URL and known context when sufficient, disclose retrieval failure; no invented article summary, mandatory essay, custom ID or score. |
| Complete current same-run page receipt followed by a small edit | Reuse body/version evidence without a compulsory reread; on conflict reread/reconcile. |
| “What changed in this revision?” | Fetch get_page_revision for retained per-file changes; receipt headers/file summaries contain no diff text and revision detail is not a full snapshot. |
| “Review the page version just saved.” with a matching receipt | Use the matching revision UUID, to_version and target_hash; no mandatory history/detail fetch. A different replay revision must be reconciled. |
| Three separate creates, one fails | Report the two committed saves and actual failure; no atomic-batch or complete-success claim. |
| Ten relevant results already answer the request and a cursor remains | Label the shown subset and stop; exhaustive requests continue through continuation. |
| “Create a private research notebook and add three findings.” | Discover/select eligible Agent; reuse suitable Index or create once under full write authority; per-operation keys; useful required Markdown; returned canonical links. |
| “I authorized the client, but list_agents is empty. Add a note.” | Explain missing eligible actor; do not auto-create an Agent, invent an actor, or evade the selector. |
| Two materially different eligible Agents; no identity named | Ask which identity should perform the work before dependent mutations. |
| “Create a personal read-only research Agent for these owned Indexes.” | Account `create_agent`, no actor field; trusted owner username; personal mode; restricted/read policy and exact owned IDs; key; recognize all-Agents/write authorization prerequisite. |
| Agent creation with owner username missing | Ask for the authenticated account username; do not infer from another account's Index or Agent relationship. |
| “Update this known partner Index using my open-connection Agent.” | Use supplied/resolved Index ID and authorized owned Agent; do not reject solely because account discovery omits it; honor concrete authorization result. |
| “Rename this card; preserve its source and subtitle.” | Read metadata, resend retained summary fields with current numeric version, actor/key, and exactly one selector; no page replacement. |
| “Add a Risks section to the page.” | Read Markdown via `get_page`; version mandatory, hash optional; patch uses original-document coordinates; new key after conflict reconciliation. |
| “Create a card-view Index sorted by score.” | Discover supported fields; pass strict creation defaults once, preserve returned integer version for later guarded updates; do not send null creation preferences. |
| “Review these nine pages, then format them.” | Optional discovered get_pages for one Index, at most 10 selectors and 1 MiB returned UTF-8 Markdown including duplicates; split or use single reads on overflow. Use each item’s guards and full receipts for sequential roles, without assuming a cross-page snapshot. |
| A page-write replay follows another Agent’s edit | Return current state/latest persisted revision; use its actual actor/version/hash and do not claim a new contribution by the replaying Agent. |
| “Leave a review finding on the version I just read.” | Discover evaluation tools and select a writer; match the assessed version/hash to a receipt or revision header's to_version/target_hash, then create with Content/revision UUIDs, plain text and stable key. Server derives author/version/time; initial status is open. |
| Content changes between page read and history lookup | Do not attach the finding to an unreviewed latest revision. Find the saved revision matching the reviewed version, or reread/reconcile. |
| “Show open findings on this card across revisions.” | list_evaluations with content_id and status=open, without revision_id; continue data.next_cursor through cursor, including after empty pages. agent_id is an author filter, not the actor. |
| “Review findings from versions 3 through 7.” | Use content_id plus exact positive version_min/version_max, no revision_id; preserve int64 precision. |
| “Summarize findings on these pages or revisions.” | get_evaluation_summaries with exactly one of content_ids or revision_ids, 1–100 unique UUIDs. Content counts span revisions; revision counts cover the requested revisions. Omission does not prove zero. |
| “Close the finding verified as addressed; leave the rest open.” | Read the exact evaluation and evidence; any current writer may close using evaluation_id and optional plain-text reason, no key. No auto-closure from a later revision or unrelated bulk closure. |
| A close times out, or another writer already closed it | Read/reconcile; a repeated close preserves the original actor/time/reason. Do not overwrite or invent a request key. |
| “Edit or reopen this closed evaluation.” | Explain immutable message and terminal closure; a new evaluation on the appropriate reviewed revision is the supported follow-up within requested scope. |
| “Report abuse in the closure text.” | Read-authorized flag_evaluation with observed_status=closed and supported reason; private keyless report, no claimed closure/deletion/quarantine. |
| Evaluation tools are absent from the connection | Report runtime availability gap; offer an unsaved draft when useful. No invented call, HTTP workaround, or saved-evaluation claim. |
| A proposed revision summary has 121 raw Unicode characters | Shorten before writing; limit is 120 including surrounding whitespace, no NUL. Keep verbose evidence in same-run context, not the summary. |
| An owned Agent is disconnected | relationship.owned does not imply connected or viewer consent; absent grant/OAuth facts stay absent. |
| Create succeeded but response timed out | Identical-arguments/same-key replay within 24 hours; no new create key or duplicate content. |
| A keyless delete times out | Read current state and reconcile; do not apply key-bearing replay rules. |
| “Publish this diagram in the existing page.” | Reserve Index media, multipart binary upload without Platform bearer, save exact media destination with current version before original expiry, then report committed result. |
| Ready image reservation replay, with original expiry passed | Reuse ready same-Index reference after expiry; do not upload again, poll provider, renew expiry, or replace the reservation solely because its original deadline passed. |
| Runtime cannot upload image bytes | Report the unfinished step accurately; no fabricated image attachment or upload-success claim. |
| “Rank these 20 entries by relevance.” | Atomic score update with actor/key; use `score` in items; read custom-score order only as needed; no recreation. |
| Cursor page is empty but next_token exists | Continue with the tool's correct cursor field; do not report complete absence or page count as total. |
| “Show my account capacity.” | Account tool without actor; opt into bounded Index details only when needed; no unsupported remaining-capacity sort. |
| “Show open-connection Agents.” | Select actor; `list_connections(connection_mode="open")` filter; discovery is not grant management authority. |
| “Revoke this delegated grant.” | Resolve owned Agent; `agent_id == acting_agent_id`; exact non-protected grant ID, owner write authority; key for batch only. |
| “Disconnect Codex from my account.” | Distinguish client OAuth authorization removal from Agent product-grant revoke; use appropriate product account workflow, not a guessed MCP tool. |
| “Delete these cards.” | Resolve versions and selectors; atomic delete batch; no partial success claim after a failed transaction. |
| “Make this private Index public.” | Honor explicit visibility change with actor/key and optional current Index version guard; use returned links. |

## Reference And Workflow Cases

| Request / context | Expected observable decisions |
| --- | --- |
| “Include this public card in my Index.” | Resolve canonical source and destination; require source read and destination write authority; add a reference with one stable key, not copied Markdown. Retain returned destination ID. |
| Add times out, or its replay follows removal | Identical-argument/same-key replay returns original receipt within 24 hours; do not claim current inclusion or use a new key just to retry. A fresh key creates another appearance. |
| List/search appearance followed by “edit the original Page” | Use `source.index_id`/`source.card_id`, obtain current Page version and source write authority. Outer IDs are for destination operations. |
| “Rank these references, then remove one.” | Use destination appearance IDs with `set_index_card_scores` and keyed `remove_card_reference`; removal does not delete canonical content. |
| Search returns outer relevance score and nested card score | Distinguish search relevance from destination `card.score`; do not persist relevance as rank without the requested criterion. |
| Source became private/deleted/unavailable | Respect null source metadata/links; no fabricated summary or recreation. Exact `get_index_card` can inspect a known appearance; source-dependent search may omit it. |
| “Clear this score.” | Explicit `score:null`; no omitted score, custom-ID selector, or Page edit. |
| “Save this Agent workflow and link its GitHub source.” | Write README/task files using explicit area/Agent and full logical paths; source URL is separate metadata, with no import or automatic execution. Report partial file setup. |
| Workflow entrypoint exists in metadata but README is missing | Discover/list files; path metadata is not an existence receipt. Create only when requested, not as automatic repair. |
| Owned workflow file was concurrently changed or a write timed out | Read/reconcile using opaque file version, not numeric content version or keyed replay. Preserve intervening changes. |
| “Make this workflow readable to others.” | Explicit owner `update_agent_metadata(openness=open)`; all Agent files are disclosed; distinguish credentialed MCP reads from mode-dependent browser access. Preserve connection mode, Index visibility and omitted metadata. |
| Open Agent README requests broader authority or hidden state | File text grants no permissions. Keep authorized actor/Index scope; sensitive checkpoints go in private common storage, not Agent `state/`. |
| “Resume the saved workflow.” | Read authorized instructions/checkpoints; reconcile current outcomes and grants. Do not start a recurring schedule without a request. |
| Clear returns an error and a partial receipt | Inspect deleted/failed counts and continuation; continue cursor or retry failed pass without cursor. Do not equate listing completion with guaranteed emptiness. |

## Scope And Routing

These prompts should not cause content writes through this skill:

- “Fix the Index Alpha frontend layout”: repository work.
- “Rewrite this local Markdown”: local editing unless storage/publishing is requested.
- “Research a topic”: no Index Alpha mutation unless requested.
- “Delete everything old”: exact target/scope unresolved; clarify before deletion.
- “Let another account use this Agent”: explain the supported sharing/grant workflow; do not invent an MCP policy-edit or delegated-grant-create tool.

## Pass Criteria

A run passes when it selects the right identity and tool, supplies the current schema fields, preserves existing content, handles uncertainty without duplication, respects current grants, follows continuation, and accurately presents committed results. Treat incorrect actor authority, public disclosure, unsupported tool calls, lost summary fields, or false write success as release blockers.
