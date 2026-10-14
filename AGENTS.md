# Adman: Creative Intelligence for Purpose-Driven Offers

Turn purpose-driven offers into creative that spreads. This repo is a distilled creative brain: real campaign lessons plus the frameworks behind them. Every performance claim must trace to evidence stated on the page.

## Read first
- `SUBJECT.md`: who we serve, what we sell. **Nothing here works until this is filled.**
- `VOICE.md`: how our copy is allowed to sound. Empty until filled.
- `knowledge/INDEX.md`: 240 pages, grouped by job.
- `KNOWN-GAPS.md`: what is not wired, and which skills need a key.

## Invariants
- Never invent performance data. A hook rate, a CPA, a win: it comes from a real report or it goes unsaid.
- Never publish, launch or spend without explicit approval. Drafting is free. Shipping is a separate, named decision.
- Never touch a live ad, ad set or campaign. New creative ships as a new ad set inside the live campaign. See `rules/never-modify-live-ads.md`.
- Never turn an ad off, and never suggest it. Ship new creative daily instead. See `rules/ship-daily-never-turn-off.md`.
- Every money number in an ad comes from a dated fact gate. See `rules/money-numbers-need-a-fact-gate.md`.
- `knowledge/` is distilled truth. Correct it only when something is proven wrong, and say so when you do.
- `rules/` is append-only. A superseded rule stays, marked SUPERSEDED at the top with a pointer to the rule that replaced it. `CLAUDE.md` and `AGENTS.md` stay byte-identical.

## The creative loop
In order. Do not jump straight to the hook.

1. **Listen**: mine real market language (`/last30days`, reviews, comments). Real words beat invented ones.
2. **Locate**: find the awareness stage. The angle changes completely per stage.
3. **Angle**: pick the emotional job, not the feature.
4. **Hook**: volume before judgement. Ten buckets, four each, forty ideas.
5. **Build**: script, shot list or static.
6. **Test**: once ads are live, run `/ad-loop` daily, three tracks: A small swings on the control (five emotional angles), B new ways to say what already works in the account, C a fresh reason to act from outside news.
7. **Read**: spend, results and cost per result together pick the control. Then break it down to image, headline and primary.
8. **Feed back**: see the learning loop.

Search for the page covering each step. Do not guess filenames.

## Using the knowledge
- Never load the folder. Search it: `python3 scripts/knowledge_search.py "<the real question>"`.
- Then `knowledge/INDEX.md` for one-line summaries, or `grep -ril "<term>" knowledge/`.
- Read three pages, not thirty. Follow a `[[link]]` only when the page you have is not enough.
- `playbooks/` = a repeatable system. `lessons/` = what one campaign taught. `concepts/` = one idea.
- When two pages disagree, prefer recent and high `confidence:`, and say that they disagree. `lessons/daily-creative-loop-lessons.md` is the most recent word on paid-social testing.
- `case-*` pages are anonymised real campaigns. Legend: `knowledge/CODENAMES.md`.

## Skills
Frameworks, not filled-in templates. They expect `SUBJECT.md` and `VOICE.md` to be real. Each skill file carries its own detail.

- **Direction**: `/last30days` real market language, `/grill-me` extract the brief, `/roast` kill or reshape an idea
- **Writing**: `/copywriting` grounded draft, `/copy-mentor` critique not rewrite, `/voice` enforce `VOICE.md`
- **Making**: `/video-ad`, `/post-inspo`, `/brand-graphic`, `/weekly-posts`, `/higgsfield-generate`, `/higgsfield-soul-id`, `/higgsfield-product-photoshoot`
- **Iterating**: `/ad-loop` the daily three-track loop for paid social
- **Discipline**: `/fable-mode` verify before handoff, `/level-up` turn a repeat into a skill

## Voice
`VOICE.md` governs. Always: no emojis, no em dashes, no jargon, no filler openers. Specific beats clever. One idea per line in ad copy. Read it aloud; if you would not say it, cut it. `skills/copywriting/references/read-aloud-pass.md` is mandatory on anything that ships.

## The learning loop
This is what makes the repo compound instead of plateau.

- **Corrected?** Fix it, write `rules/feedback_<slug>.md` (the rule, why it matters, how to apply it), then show the rule in one line. The test: a fresh agent gets it right next time without being told.
- **A hunch from the operator?** Check it against past rounds, customer words and results before it changes an ad. See `rules/verify-hunches-before-acting.md`.
- **A campaign taught you something?** New page in `knowledge/lessons/` with `updated:`, `confidence:`, and the evidence. No evidence means it is an opinion.
- **A workflow repeated three times?** Run `/level-up`.

## Working rules
Read on demand; this file is the index, not the payload. One write beats many sequential edits. Batch independent tool calls into one turn. No preamble, no recap of what just happened.
