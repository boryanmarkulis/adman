# Known gaps

Read this before promising output or connecting an account.

## Setup still required

- `SUBJECT.md` and `VOICE.md` are intentionally blank. Creative will remain generic until they contain real client context and shipped voice examples.
- `last30days` has a limited keyless mode. Additional providers improve coverage and require their own credentials.
- The Higgsfield skills require Higgsfield credentials.
- `post-inspo` requires working web access. Exa is optional.
- `brand-graphic` can produce HTML or SVG without extra services. PNG rendering requires a compatible local Chrome installation.
- `video-ad` produces the brief, hooks, script, shot list, and edit plan. It does not include a video-rendering toolchain.
- `ad-loop` is a manual procedure for three daily ad sets (Tracks A, B, C). It reads numbers from an Ads Manager export and the Dynamic Creative Element breakdown. It ships no API scripts for pulling data, rendering cards or publishing. The operator publishes each round after a named go.
- `ad-loop` expects `research/copy-corpus.md` and `research/fact-gate.md` to hold real material. With an empty corpus it has no words to build from.
- `ad-loop` Track C needs web access for current news and the Ads Library scan. Without it, Track C falls back to the corpus and recordings and says so.
- The `ad-loop` card check needs a second model or a person to look at each image. No checker script ships.
- Publishing and ad-account writes are intentionally not implemented. They must be connected separately and remain approval-gated.

## Local folders

Skills create `research/` and `work/` when they first need them. Neither folder contains private material in the starter repository.

## Verification

Run this before sharing:

```bash
python3 scripts/verify_export.py
python3 -m unittest discover -s tests -v
```

The verifier checks the standalone layout, known private identifiers, internal paths, malformed metadata, exposed contact details, and dead wiki links.
