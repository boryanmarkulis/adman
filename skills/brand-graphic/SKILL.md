---
name: brand-graphic
description: Create a branded static-ad or social graphic from the active subject, voice, proof, and brand assets.
allowed-tools: Bash Read Write Edit
---

# Brand Graphic

Build a static creative that communicates one idea at feed speed.

## Process

1. Read `SUBJECT.md`, `VOICE.md`, and any supplied brand guide or reference assets.
2. Define the audience, placement, desired action, single message, and proof source.
3. Draft the accompanying copy first. Run the `voice` check.
4. Choose the simplest useful format: proof card, comparison, diagram, quote, product demonstration, or offer card.
5. Create a self-contained HTML or SVG file. Use only supplied brand tokens. If none exist, use a neutral black, white, and one-accent system and label it as a placeholder.
6. Render with `python3 scripts/render_graphic.py <file> --out <preview.png> --size <WxH>` when Chrome is available. Otherwise deliver the source file and state that rendering remains.
7. Inspect the rendered image before handoff. Check hierarchy, contrast, spelling, crop, safe zones, and factual accuracy.

Save the source, copy, and preview under `work/creative/<YYYY-MM-DD>-<slug>/`. Never publish or overwrite an existing asset without explicit approval.
