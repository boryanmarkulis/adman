---
type: playbook
updated: 2026-05-04
provenance: gdocs
confidence: medium
---

# Lyric to Scene Prompting

Use this when turning a song, chant, or short script into image prompts or a scene-by-scene video prompt sequence.

## Core Pattern

- Break the lyrics into fixed visual beats, usually 5-second sections.
- Write one image prompt per beat so continuity stays manageable.
- Keep a single core style prompt that anchors the whole sequence.
- Carry the same character design through every scene.
- Ask the model whether it can generate everything at once or should work one section at a time.

## Useful Prompt Structure

- Start with the intended medium: image generation or video generation.
- State the visual style in one compact block.
- Define the main character with stable identifying details.
- List each lyric segment as a separate scene.
- Describe camera motion, lighting, and setting only when they help the shot.

## What Worked in the Source

- the studio theme-song prompt was split into 10 numbered visual moments.
- The system prompt anchored the sequence with a reusable style sentence, the same reuse logic in [[viral-content-sourcing-and-repackaging]].
- Each scene mapped directly to a lyric line or chorus beat.
- The final result was easy to adapt into Sora-style video prompts.

## Evidence

Derived from a completed ten-scene theme-song sequence and retained as a reusable method.
