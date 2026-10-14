# Rules

Two kinds of file live here.

**Standing rules** (`*.md` without a prefix) are the operating discipline. They were paid for with real incidents. Read them; do not rewrite them.

**Feedback rules** (`feedback_*.md`) are what the agent has learned since. They are written by the agent, at the moment of correction, and they are how this repo gets smarter than the day it shipped. See `learn-from-corrections.md`.

Every rule file has the same shape:

```markdown
# <the rule in one line>

## Rule
What to do, stated so a fresh agent can follow it without context.

## Why
The real incident or reasoning. Without this the rule gets argued away later.

## Apply
The concrete steps, next time.
```
