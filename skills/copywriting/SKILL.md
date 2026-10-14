---
name: copywriting
description: Copywriting session grounded in the operator's accumulated knowledge. Loads relevant wiki pages before writing so copy draws on real hooks, frameworks, and tests from past work.
allowed-tools: Read Write Edit Glob
---

Loads the knowledge base index, pulls the 3-5 most relevant copywriting pages, interviews you (thoroughly like the /grill-me skill), then writes and saves the copy. The wiki grounding is the point -- if the knowledge base is empty, say so and ask whether to run the compile first.

---

## Step 1: Search the knowledge base

Do NOT read `knowledge/INDEX.md`. It is 78 KB of table of contents, about 20,000 tokens, for what is only a list of page names. Query the knowledge base instead:

```
python3 scripts/knowledge_search.py --pages -k 8 "<the copy task in plain words>"
```

Run it two or three times with different angles (the offer, the channel, the audience) rather than once with a vague query. It returns section-level hits in about 3 seconds.

If it errors or returns nothing, tell the operator and ask whether to proceed without wiki context or search again with broader terms.

## Step 2: Select relevant pages

Pick the 3-5 highest-scoring pages that actually match the task -- hooks, persuasion, copy frameworks, ad structures, conversion, CTA patterns, or the specific channel. Announce your picks before reading:

> Pulling: [hook-frameworks], [ad-copy-structures], [cta-patterns]

Then read those pages. Check each page's `updated:` date: a `confidence: high` stamp is the extractor's confidence in the extraction, not a promise the strategy is still live.

## Step 3: Interview

Ask all of these in one message:

- **Goal:** What should this copy accomplish?
- **Audience:** Who's reading it?
- **Channel:** Where does it live? (WhatsApp, email, FB/IG ad, landing page, other)
- **Tone:** Any constraints on vibe or voice?
- **CTA:** What action do you want them to take?

## Step 4: Load client context if needed

If the interview reveals this is for a specific client, re-read `SUBJECT.md` and `VOICE.md` before writing.

## Step 5: Write

Write the copy grounded in the knowledge base pages -- hooks that worked, frameworks that convert, patterns from real tests. Write multiple variations if the task benefits from options (e.g., 3 different hooks to test).

## Step 5b: The read-aloud pass (mandatory, never skip)

If this copy is grounded in a corpus of real words (Reddit, transcripts, reviews, calls),
read `references/read-aloud-pass.md` **before drafting**, not after. It carries three things:

1. **The lifting rule.** 60 to 80% of the WORDS come from the corpus, not 70% of the
   sentences. You lift phrases and vocabulary and duct-tape them together with your own
   connective words into one narrator's voice. Stacking whole verbatim sentences is what
   makes copy choppy, and the operator rejects it every time.
2. **The reviewer.** After the draft exists, spawn a separate agent with the reviewer brief
   in that file. It reads the copy as if spoken out loud, lists every stumble, and returns
   a rewritten version. You then take the flow fixes and reject anything that softened a
   number or invented a claim.
3. **The target voice**, reverse-engineered from the operator's own hand-edits.

No draft goes to the operator without the read-aloud pass having run.

## Step 6: Save

Create `drafts/copywriting/` if it doesn't exist. Save to `drafts/copywriting/<kebab-slug>.md` where the slug describes the piece (e.g., `customer-welcome-sequence.md`). Display the full output in session too.

---

## Constraints

- State which wiki pages you pulled at the top of your response so the operator can see what knowledge is being used
- Keep your own voice out of it -- write the operator's copy, not AI copy
- No emojis, no em dashes, no filler
- Read it out loud in your head before you ship it. If the mouth stumbles, the line is wrong
