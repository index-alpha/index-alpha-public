# Editorial standard: clear conclusions, honest limits

Write for a technically literate reader deciding what to build, buy, adopt or
ignore. Use the directness of a technology lawyer briefing an engineer: give the
conclusion, grounds, material exception and practical consequence. Use plain
English, not legal boilerplate. Be frank about weak evidence and commercial
claims; criticize the claim rather than attacking its author. Precision matters
more than theatrical certainty.

## Surface the useful information first

Aim for 200–400 words, extending only when essential evidence requires it. Use a
specific declarative title that states the actual mechanism, constraint or
tradeoff; a short subtitle should add the decision or caveat rather than repeat
it. Never promise a revelation, manufacture urgency or use outrage as a hook.
Avoid rhetorical questions, “game-changing,” “everyone agrees” and “X is dead.”

Start the Markdown page with the exact card title as its H1. Follow it with a
two-sentence introduction explaining what the story is about and why it matters
to a software builder. Keep the context specific and leave the finding and its
strongest caveat for the takeaway immediately below.

Use this compact structure after the introduction:

1. **The takeaway:** two sentences stating the finding and its strongest caveat.
   Place the card preview image, when available, immediately after the takeaway
   as the first managed image in the page.
2. **What the evidence supports:** two or three concrete facts, with links and
   dates/units/baselines for any numbers. Identify measurements versus vendor
   claims, anecdotes or editorial inference. If a benchmark lacks workload,
   hardware or comparator, state the missing basis rather than generalizing it.
3. **Where the discussion lands:** synthesize two or three leading themes from
   the sampled top-ranked threads. Explain the strongest substantive objection,
   important counterexample, and whether they change the takeaway. Say “the
   sampled leading threads converge on…” only when independent branches support
   it. If views split or evidence is thin, say so and explain the fault line.
   Comment counts or repeated agreement do not establish community consensus.
4. **Practical implication:** one concise recommendation conditional on the
   reader's workload, constraints or risk tolerance. State what evidence would
   change it when that matters. Do not invent data to deliver a firm conclusion.
5. **Sources and scope:** link the original article and the story's
   HN discussion at `https://news.ycombinator.com/item?id=<story-id>` using
   the verified story ID. Include a compact discussion observation time and actual comment/
   branch sample size. State missing evidence that materially limits confidence.

Summarize arguments in your own words. Do not quote or name individual HN users
in the page title, subtitle or body. Link to the story's comments section; precise
comment permalinks may support a specific argument without displaying a username.
Source authorship/necessary article attribution and image credits are preserved.
Treat an unsupported comment as a claim to check, not a fact to repeat.

## What “top voted” can truthfully mean

The official public API supplies story points and display-ranked comment `kids`,
but no public per-comment vote totals. Use the leading HN-ranked branches as the
available signal, and inspect substantial replies/rebuttals. Describe these as
“leading” or “top-ranked,” never as a measured vote ranking. Do not infer votes
from position, colour, reply count or story points. If verified vote information
is actually available in a future authorized source, identify the source and
observation time before using it. Importance can override position for a concrete
technical correction, evidence-backed rebuttal or significant consequence; explain
that judgment in working evidence rather than rewarding heat or repetition.

Update the article's synthesis and evidence in place when discussion materially
changes. Keep the observation/sampling facts in Sources and scope; never append
an administrative review/revision log. No change means an evaluation, not a page
revision merely to refresh a timestamp.

Official API contract: [Hacker News API](https://github.com/HackerNews/API).
