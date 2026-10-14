# Adman

A standalone creative brain for purpose-driven offers. Membership organisations, conscious products, regenerative technology, and the transformations they sell.

It carries real campaign lessons alongside established creative frameworks: 240 knowledge pages, 16 skills, and operating rules learned from shipped work. Private operator and client identifiers are stripped.

Updated 2026-10-14: `/ad-loop` now runs **three tracks** every day. A is small swings on the control, B develops what already works in the account, C finds a new reason to act from outside news. The old "Track B" (pattern interrupt) is now Track C. The control is now picked by spend, results and cost per result together, not spend alone (`rules/control-is-strongest-performer.md`). Also new: an ad set naming convention, awareness-level tagging, a card verification loop, and more lessons in `knowledge/lessons/daily-creative-loop-lessons.md`.

Updated 2026-09-13: added `/ad-loop`, the daily paid-social testing loop, and the rules behind it.

## Install

```bash
git clone https://github.com/boryanmarkulis/adman.git
cd adman
claude        # or: codex
```

That is all. The skills load on their own. In Claude Code, type `/ad-loop`, `/copywriting`, `/last30days` and so on. In Codex, type `$ad-loop`, or `/skills` to see the list.

**Windows:** the skill folders are links, which Git on Windows turns into plain files unless links are on. Turn on Developer Mode, then clone with `git clone -c core.symlinks=true https://github.com/boryanmarkulis/adman.git`. Or skip the links: copy the `skills` folder into `.claude` and `.agents` by hand after cloning. To pull later updates, run `git pull` inside the folder. Your own `SUBJECT.md`, `VOICE.md`, `research/` and `work/` stay yours; commit them on your own branch or keep them out of git.

## Start here

```
CLAUDE.md              how the agent works. Read it first.
SUBJECT.md             who we serve and what we sell. FILL THIS IN.
VOICE.md               how our copy is allowed to sound. FILL THIS IN.
knowledge/INDEX.md     240 pages, grouped by job. Search this, do not load the folder.
knowledge/CODENAMES.md what the anonymised case-* campaigns actually were.
skills/                16 frameworks. Run with /name. Ads already running? Start with /ad-loop.
rules/                 the operating discipline, and the learning loop.
connections.md         what this is wired into and what it may do there.
KNOWN-GAPS.md          what is NOT wired yet. Read before promising anything.
.env.example           copy to .env and fill only what you need.
```

## First run

1. Fill `SUBJECT.md`. Nothing works well without it.
2. Fill `VOICE.md` from real copy that already performed. Not from an AI sample.
3. Copy `.env.example` to `.env` and fill only the connections you need today.
4. Run `/grill-me` against your SUBJECT to find what you have not written down yet.
5. Run `/last30days <your topic>` to hear what the market is actually saying.
6. Then follow the creative loop in `CLAUDE.md`.

## Retrofitting to a new client

Copy `SUBJECT.md` and `VOICE.md` into `clients/<name>/` and refill them. Nothing in `knowledge/`, `skills/`, or `rules/` changes. That separation is the whole design.
