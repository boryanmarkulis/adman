---
name: video-ad
description: Build a vertical video-ad brief, script, hook set, shot list, and edit plan from verified client context.
allowed-tools: Read Write Edit
---

# Video Ad

Create the creative package for a vertical paid-social video. This skill does not assume a particular editor, local toolchain, campaign, or client.

## Inputs

Read `SUBJECT.md`, `VOICE.md`, the brief, available proof, and any supplied footage notes. If the offer, audience, desired action, or proof is missing, ask for it. Never invent performance data or customer claims.

## Process

1. Search the knowledge base with `python3 scripts/knowledge_search.py -k 6 "<offer audience video ad>"`.
2. State the audience awareness level and the one belief the ad must change.
3. Produce at least five distinct hooks before choosing one. Label the variable each hook tests.
4. Write one shared body: problem, mechanism, proof, offer, action.
5. Build a shot list with timing, visual, spoken line, on-screen text, and asset source.
6. Add an edit plan covering pace, captions, cutaways, sound, aspect ratio, and safe zones.
7. Run the `voice` and read-aloud checks.

Save requested deliverables under `work/ads/<YYYY-MM-DD>-<slug>/`. Create the folder when needed. Rendering or publishing requires a separately installed media workflow and explicit authorization.
