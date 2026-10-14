# The read-aloud pass

Canonical. `copywriting` and `copy-mentor` both point here. Do not copy this
file into another skill. Link to it.

This runs **after** a draft exists and **before** it is shown to the operator. It is not optional
and it is not a proofread. It is the flow gate.

---

## Part 1: how to lift from a corpus without going choppy

The old rule said 70% of **sentences** must be lifted verbatim. That rule is what makes the
copy choppy. It ships three stranded Reddit sentences in a row, from three different people,
and it reads like a clip show. Repeated review showed the word-level rule produces cleaner copy.

The rule now:

**60 to 80% of the WORDS come from the corpus. Not 70% of the sentences.**

You are lifting vocabulary and phrases, then duct-taping them together with your own
connective tissue so the whole thing sounds like one person talking.

What that means in practice:

1. **Phrases, not sentences, are the unit.** Take `dealer fee`, `white glove service`,
   `they ended up leaving with a signature`, `apples to apples`, `the guy was a clown`,
   `marketing home`. Those are the gold. Take the phrase, drop the sentence around it.
2. **One narrator, always.** Every lifted phrase gets rewritten into the mouth of a single
   composite first-person homeowner. Different real people said these things. The reader
   must never be able to tell.
3. **Connective words are yours.** `so`, `because`, `and then`, `here's the thing`,
   `that's when`, `what I didn't know is`. Use them freely. They are the duct tape and they
   do not count against the corpus ratio.
4. **Never announce the source inside the copy.** No "here's what neighbors said", no
   "one homeowner wrote", no quoting other people mid-story. Nobody talks like that. The
   narrator lived it.
5. **Never stack three lifted lines in a row without narrating between them.** If three
   consecutive lines are all lifted, at least one of them has to be rewritten into the
   narrator's own telling.
6. **Provenance still ships**, in the round doc, as source material. The doc records which
   phrases came from where. It never records a claim that the shipped sentence is verbatim.

The verbatim percentage table stays in the doc as information. It is not a target and it is
never a reason to make a sentence worse.

---

## Part 2: the read-aloud reviewer

Spawn this as a **separate agent** on a fresh context so it cannot see the drafting
reasoning and cannot fall in love with the draft.

```
Agent(
  subagent_type: "general-purpose",
  description: "Read-aloud copy review",
  prompt: <the reviewer brief below, with the draft pasted in>
)
```

### The reviewer brief

> You are reviewing one piece of long-form Facebook ad copy. Assume it is being READ OUT
> LOUD by one person telling a friend what happened to them, across a kitchen table.
>
> You have two jobs.
>
> **Job 1: mark every place the mouth stumbles.** For each one, say what is wrong. Look for:
>
> - a sentence a real person would not say out loud
> - two lines in a row that make the same point
> - a line that changes subject with no bridge into it
> - a stack of instructions or a list dropped into the middle of a story
> - hedging, throat-clearing, or the narrator explaining that they are being fair
> - a formal construction where a contraction belongs (`it is` / `that is` / `I did not`
>   / `they are` where the mouth would say `it's` / `that's` / `I didn't` / `they're`)
> - a compound sentence carrying two separate beats that should be two lines
> - a line that reads like it was pasted in from somewhere else
> - repeated sentence rhythm, three or more lines in a row with the same shape
> - a number or fact that contradicts another line in the same piece
>
> **Job 2: return the full rewritten copy.** Same story, same facts, same numbers, same
> angle, same closing lines. Fix the flow only.
>
> Hard rules you must not break:
>
> - One sentence per line. Never a paragraph.
> - Do not add a claim, a number, a statistic, or a benefit that is not already there.
> - Do not remove a number or an attribution that is already there.
> - Do not add emojis, em dashes or double hyphens.
> - Do not make it shorter by cutting the story. Cut the lecture, keep the story.
> - Keep the last two lines of the copy exactly as they are. That is the tested close.
>
> Return: (1) the numbered list of stumbles, (2) the full rewritten copy in a code block.

### After it comes back

Read both. You are still the author. Take the flow fixes, reject anything that softened a
number, weakened the hook, or invented a claim. Then run the honesty checks again on the
rewritten copy, because the reviewer does not know the round's claim rules.

Log in the round doc that the read-aloud pass ran, and note anything you rejected.

---

## Part 3: the target voice, written down

This pattern comes from a real operator hand-edit of long-form paid-social copy. The repeated changes were:

| He cut | He kept or added |
| --- | --- |
| `It is what the lender charges` | `It's what the lender charges` |
| One line carrying two beats | Two lines, one beat each |
| `Nobody sells you a price anymore. They sell you a payment.` on one line | Split onto two lines |
| A three-line block of instructions (`Ask for the cash price. Then ask for the financed price. Write both down.`) | Deleted whole. It stopped the story. |
| `I want to be fair here, because I am not anti-solar` | Deleted. No hedging, no self-defence. |
| `Because here is the thing nobody had said out loud to me.` | Deleted. No throat-clearing. |
| `Nobody is going to hand you the number.` | Deleted where it repeated a point already made |
| `Dealer fee. 29.74%. On a $55,345 contract.` | `29.74%. Out of $55,345.` Tighter. |
| `The panels were never the problem. Panels are cheap now.` | `The panels are never the problem. They're pretty much dirt cheap now.` |
| `I called them back and I asked one question. If I paid cash instead, what is the price?` | `So I called them back and asked a simple question:` then the question on its own line |

The five rules that fall out of it:

1. Contract everything the mouth contracts.
2. One beat per line.
3. No lecture blocks. If it turns into a how-to list, cut it to one line or cut it.
4. No hedging and no throat-clearing. The narrator is not defending themselves.
5. Say the number the shortest way that is still true.
