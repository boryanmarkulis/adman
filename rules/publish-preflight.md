# Preflight anything that leaves the building

## Rule

Before any action that reaches a real person outside this repo, state in one block:

1. **What exactly goes out.** The literal payload. Not a description of it.
2. **Who receives it,** and how many.
3. **What it can trigger downstream.** Automations, sequences, notifications, spend.
4. **How to undo it,** or that it cannot be undone.

Then wait for a named go. Then release small before releasing wide.

## Why

Writes that look like data become marketing events. A tag added to fix attribution once fired a text-message sequence to weeks-old contacts, produced an 8% opt-out rate, and got an account restricted. Nothing in the request said "campaign". The system did not care.

## Apply

Applies to: posting, publishing, scheduling, ad launches, budget changes, email or SMS sends, bulk CRM writes, imports, tag sweeps, and any script that touches a live account.

A successful API response is not proof of correctness. Go look at the rendered, live surface and confirm what a real person now sees.
