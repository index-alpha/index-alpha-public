# Your first Index

Complete [getting started](../getting-started.md) and choose an eligible Agent before requesting writes. For a small first workflow, ask:

> Use Index Alpha to create a private Index named Research Notes. Add three short notes about a topic I choose, with useful Markdown and source links where relevant. Use the Agent I select. If a suitable Index already exists, ask before creating another one. Return the actual Index and card links.

The agent should discover eligible identities, confirm the intended one when ambiguous, and use current access to find or create the target Index. New Index creation requires full write authority. The user request supplies intent; effective permission still comes from the account authorization and Agent grants.

To make a follow-up edit:

> Update the second note with this new finding. Preserve its existing sources and other summary fields, and keep the Index private.

The agent should read the current version, apply the change through the appropriate content operation, and report the committed result. It should reconcile a conflict rather than overwrite an intervening edit.

For a curated example, try [Signal to Noise](../../examples/signal-to-noise/README.md). Its Agent reads public HN Best stories, articles, and discussion directly; separate review, formatting, and ranking workflows improve the selected cards. Read the definition before requesting setup or publication.
