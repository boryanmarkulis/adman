# Connections

What this agent is wired into, what it is allowed to do there, and whether it works yet.

Update the Status column the moment a connection goes live. An unstated connection gets rediscovered the expensive way.

| System | Reads | Writes | Status |
|---|---|---|---|
| Meta Ads | campaigns, ad sets, ads, insights, creative | creates **paused** drafts only | TODO |
| Meta Page + Instagram | posts, comments, insights | publishes posts and replies after a named go | TODO |
| Google Ads | campaigns, keywords, search terms, insights | none until explicitly enabled | TODO |
| Google Search Console + GA4 | queries, pages, traffic | read-only, always | TODO |
| Etsy | listings, shop stats, reviews, ads | listing copy and images after a named go | TODO |
| OpenArt | generated images | generates on request | TODO |
| Higgsfield | generated images and video | generates on request | TODO |
| Scheduler | the queue | queues posts; publishing is a separate go | TODO |
| Research (Exa, Apify, Perplexity, Reddit, YouTube) | public posts and comments | read-only, always | TODO |
| Automation handoff | approved inputs and outputs | none until explicitly connected | TODO |

## The line between this agent and automation

Use a separate automation system for deterministic pipelines where the same input should produce the same output every time. Do not assume one is installed or connected.

This agent handles the part that is not deterministic: what to say, to whom, in what order, and why. It may hand finished creative to an approved automation, but it does not become a second automation layer.

## Rules that apply to every connection

1. Reading is always allowed. Writing is never assumed. See `rules/publish-preflight.md`.
2. Live ads are read-only. See `rules/never-modify-live-ads.md`.
3. After any write, go read the live surface. See `rules/verify-published-not-described.md`.
4. Credentials live in `.env`. Never in a skill, never in a knowledge page, never in a commit.
5. Access to an account is not permission to spend in it.

## Adding a connection

1. Add the keys to `.env.example` first, with a comment saying what they unlock.
2. Add the row to the table above with Status TODO.
3. Write a read-only call and confirm it returns real data.
4. Only then write anything, and only through the preflight.
