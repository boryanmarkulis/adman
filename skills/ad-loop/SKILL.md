---
name: ad-loop
description: The daily paid-social iteration loop. Three tracks, all built every day. Track A picks the strongest lead performer from the last 3 days (spend, results and cost per result read together), breaks it down to the winning image, headline and primary text, and builds a 5:2:2 challenger that moves one creative variable across five emotional angles. Track B develops an angle that worked or almost worked in the account, in a new headline, visual world, messenger or emotion. Track C finds a fresh reason to act from current news and outside market attention. Use for "/ad-loop", "run the ad loop", "beat the control", "iterate on the winner", "daily ads", or reviewing today's ads.
---

# ad-loop

One run = **three new ad sets**, one per track, every day, on any account. Three is the default. Ship fewer only when a track has nothing honest to build that day, and say which track and why in the round doc.

- **Track A, small swings at the control.** A 5:2:2 dynamic-creative ad set built against the current winner. It holds the winner's proven copy and moves **one** creative variable across five different emotional angles.
- **Track B, develop the account's signals.** A 3:2:2 ad set that takes an angle the account's own results say works or almost works, and says it in a new way: new headline, new visual world, new messenger, new emotion.
- **Track C, external discovery.** A 3:2:2 ad set with a fresh **reason to act**, found in current news, headlines and outside market attention. It loses most days. It ships anyway, because the step changes come from here.

Track A compounds a proven performer. Track B develops promising results. Track C finds new hooks outside the account. All three run. None replaces the others.

**Track names changed.** Earlier versions of this skill had two tracks, and "Track B" meant the pattern-interrupt swing that is now Track C. In older round docs, read "Track B" as Track C. The old `research/track-b-seed-bank.md` is now `research/track-c-seed-bank.md`.

**The rule that makes this work: understand why the control wins, then improve the parts that matter.** Moving one tiny variable on a winner rarely beats it. Moving several unrelated things with no reason teaches nothing. Every change needs a line of evidence behind it.

Needs `SUBJECT.md` and `VOICE.md` filled in. Without them this produces generic ads.

Written for Meta dynamic-creative ads (up to 5 images, 5 primary texts, 5 headlines per ad, and Meta concentrates spend on one of each). The logic transfers to any platform that lets the algorithm pick between assets.

## Doctrine, non-negotiable

1. **Ship every day.** Three new ad sets per account per day, one per track, is the default. Extra same-day rounds are welcome. Never zero. Not one round when the data looks clean. If in doubt, ship more. See `rules/ship-daily-never-turn-off.md`.
2. **Never turn an ad off, and never suggest it.** No pause lists, no "thin the field", no consolidating ad sets to free budget. Low-cost ads depend on higher-cost ads feeding the funnel. Kill the top and the bottom starves. See [[facebook-cbo-creative-volume]].
3. **Never correct the platform's allocation.** Never suggest a dedicated budget, a spend floor, a separate campaign or a guaranteed test for any ad or track. If it is good, it will win spend.
4. **Never withhold a round waiting for "learnings".** Low spend on a new ad set is not a defect and not a blocker. Report spend as an observation only. Do not write that new ads are "starving".
5. **Creative volume is the strategy.** More shots on goal beats fewer, better reasoned shots. "Consistency beats intensity." See [[ad-creative-testing-loop]].
6. **Track A is 5:2:2.** Five images, two primary texts, two headlines. See [[ad-variation-framework]].
7. **Tracks B and C are 3:2:2.** Three images, two primaries, two headlines. **Never three primaries.** If a new body is strong enough to need a slot, it replaces one of the two or waits for tomorrow.
8. **Look back 3 days, not 7.** You ship daily, so the read has to be as fresh as the shipping. A 7-day window keeps counting ads that were already replaced. On one real account the same winner held 72% of spend on the 3-day window and 34% on the 7-day window. Widen to 7 or 30 only to answer a specific question, and say so in the round doc.
9. **New ad sets go into the live campaign.** Never invent a new campaign. Adding a new ad set to a live campaign is not modifying a live ad. See `rules/never-modify-live-ads.md`.
10. **Tracks are never blended inside one ad set.** Track A inherits the winner's look. Track B develops an evidenced account angle. Track C discovers an angle from outside.

Older pages in `knowledge/` that say "avoid constant creation" or "wait three days before judging" came from an account where creative was expensive to produce. They do not apply to this loop. When creative is cheap to make, volume wins.

**Corpus refresh is not this loop's job.** If `research/copy-corpus.md` is stale, say so in the round doc and ship anyway. Feed the corpus with a separate research pass (`/last30days`).

---

## Folder layout

The skill creates these the first time it runs:

```
research/copy-corpus.md            real customer words, verbatim, with source and date
research/fact-gate.md              every number an ad may cite, with a verified date
research/track-c-angles.md         every reason to act the account has tested, with its awareness level
research/track-c-seed-bank.md      look ideas used to dress a Track C angle, open or BUILT
research/round-image-inventory.md  every look the account has already run
research/reviews/<date>.md         the operator's review of the live ads, newest first
work/ads/<date>-<slug>/            Track A round: ad-set.md, round.json, images/, bodies/
work/ads/<date>b-<slug>/           Track B round
work/ads/<date>c-<slug>/           Track C round
```

Templates: `references/round-doc.md`, `references/track-c-angles.md` and `references/seed-bank.md`.

**Naming.** Build the tracks in order A, B, C, so the folders read `<date>-<slug>`, `<date>b-<slug>` and `<date>c-<slug>`. Name each ad set `<Short Name> | <maker> | <format> | <date><letter>`, for example `Street Interviews | CLD | IMG | 2026-10-12b`. `<maker>` is a short code for whoever built it (`CLD` for Claude, `GRK` for Grok, initials for a person). `<format>` is `IMG` or `VID`. The letter is empty for Track A, `b` for Track B, `c` for Track C. An extra same-day round keeps its track letter and adds a number: `2026-10-12a2` for a second Track A, `2026-10-12b2` for a second Track B. One look at Ads Manager then tells you the track, the maker and the day.

---

## Phase 1. Find the control

Export the last 3 days from Ads Manager at the **ad** level: spend, results, cost per result, CTR, frequency. The window ends **yesterday**, never today. Today is a partial day and drags every number down.

**The control is the strongest result performer with real delivery. Read spend, result volume and cost per result together.** See `rules/control-is-strongest-performer.md`.

- Compare the leading ads side by side, inside the same campaign, result definition, attribution window and funnel.
- A simple shortlist that works: drop ads with zero results. Drop any ad that another ad beats on both result count and cost per result (at least as many results, no higher cost, one strictly better). From what is left, take the one with the most spend. This is a decision aid, not statistical proof. Look hard at small samples and close cost differences before you accept it.
- **Spend alone does not choose it.** An ad the platform funded more can still be the weaker one. Real example: ad X spent 34 with 5 results; ad Y spent 44 with 1 result. X is the control.
- **The cheapest single result on tiny spend does not choose it either.** That ad is a Track B signal, not the control.
- No minimum age or tenure. Re-select from current results every run. Never hard-code yesterday's control, or its format, as today's Track A.
- If nothing spent anything, stop and say so. If spend produced no results, there is no proven control in the window: keep the last verified control, or label the choice provisional. Keep doing Track B and C research.

Explain the choice in the round doc with the numbers. CTR and frequency go in the doc too. This selects which creative to iterate. It never changes budgets.

**A funnel change breaks the series.** If the lead form, landing page or checkout changed, draw a hard line at that date. A tougher qualifying form can cut click-to-lead rate from 18% to 6% and double cost per lead on purpose. That is the system working, not a creative failure. Compare creative across the line on click-to-result rate instead.

## Phase 2. Break the control down

The ad-level number is not the answer. Meta concentrates the budget inside a dynamic-creative ad on one image, one headline and one primary. Stop at the ad level and you iterate on an asset that barely ran.

In Ads Manager, select the control, then **Breakdown > By Dynamic Creative Element**: image, then headline, then primary text. Take the top-spend row of each. Those three are what you hold.

Real concentrations seen: 91 to 99% of an ad's spend on one image; 82% on one primary text.

- **The platform only gives one element breakdown at a time.** It will show the best image and the best headline separately, never which combination ran together. The only place a served combination is visible is the post itself: select the ad, **Preview**, share menu, **Facebook Post with Comments**. That post is also where the comments live.
- **The winning headline is often not the one you see on the post.** One real post showed headline A while 96% of spend sat on headline B. Take the words from the breakdown, take the look from the post, and write both down if they disagree.

Then:

1. **Who does it convert?** Age and gender breakdown on the ad: spend and results per segment. On one real account, men 55+ produced 8 of 13 leads while women 65+ took real spend for zero. That segment decides whose words you mine next.
2. **Frequency.** Above roughly 2.5 the winner is wearing out. Move the image rather than the words.
3. **What does it share with the last two rounds' winners?** A pattern across rounds beats any single week.
4. **Why does it win?** Reason by reason, each tied to evidence: the entry, the narrator, the villain, what the reader gets, what the click resolves. Check what past challengers changed and how they did. If a challenger swapped the opening and lost, the opening is proven.

Write the verdict as one sentence: *"It wins because X."* X is what you hold.

## Phase 3. Read the comments

Comments are the only free focus group in the whole system. People say exactly what they object to, and objections are hooks.

Sort them into **objections**, **questions** and **hostility**. Each is a candidate opening line. Objections that repeat across two rounds go into `research/copy-corpus.md`.

Comments may simply not be there, deleted or hidden. Then say the round ran without comments. Never imply they were checked.

## Phase 4. Mine the corpus

Read `skills/copywriting/references/read-aloud-pass.md` and `research/copy-corpus.md` before drafting a word.

- **60 to 80% of the WORDS come from the corpus, not 60 to 80% of the sentences.** Lift phrases, drop the sentence around them, rewrite into one composite first-person narrator. Pasting whole sentences from different people reads like a clip show.
- Mine for **the segment Phase 2 found**, in their words. A retired engineer says "ran the numbers" and "my wife and I". A first-time buyer says something else.
- Signal ranked best to worst: direct customer calls; comments, reviews and ad metrics; competitor reviews and forums; AI synthesis, for sorting only, never for inventing. See [[control-killer-cohort]].
- **A quote supplies words, never money numbers.** Any price, saving, payback or ROI figure comes from `research/fact-gate.md` or it does not ship. See `rules/money-numbers-need-a-fact-gate.md`.
- **Operator hunches are hypotheses.** "This angle feels niche" gets checked against past rounds, customer words and campaign results before it changes the ad. See `rules/verify-hunches-before-acting.md`.

Ten to fifteen candidate phrases is plenty.

## Read the newest review first

The operator reviews the live ads, ideally daily, and sends notes back. Save each one as `research/reviews/<date>.md` with three parts: what the operator saw (their words), what the numbers say, what the loop does next. Check each claim against the 3-day numbers and the asset breakdown. Report where they agree and where they do not.

**Every round reads the newest review before Phase 5**, and the round doc says which review it followed and how.

- **Review notes are seeds, not a script.** Build some of the named ideas, because they carry market knowledge the loop does not have. Also bring your own from the knowledge base, the corpus and outside research. Say in the round doc which ideas came from the review and which are new.
- **Hard rules go into this skill only rarely.** Promote a review line to a rule only when the operator states it as a must (facts, brand, readable text) or it repeats across reviews. Rules pile up and never expire. Ideas in the review file stay flexible.
- **Creative approval is direction, not conversion proof.** "I like this one" does not make an ad the control. Results do.
- Never modify a live ad to act on a review. Write the fix down and leave it for the operator to approve per object.

---

## Phase 5. Build the Track A copy

Measured against the Phase 2 winning assets, never the ad as a whole:

- **Primary 1 = the winning primary text, verbatim.** The exact body Meta put the spend behind.
- **Primary 2 = one new entry into the same close.** Only the opening four or five sentences change. The back half and the call to action stay word for word. Nothing else in either body moves at random.
- **Check the held body against the copy bans before you hold it.** Verbatim copies the control's mistakes too. On one real account the control carried a tiny monthly dollar figure ("two dollars and fifty cents a month") for weeks against a standing ban, and every round copied it. A banned line gets the review fix, in every body, Primary 1 included. Log it as a known fix, not a new variable.
- **Payoff before mechanism.** Within the first five or six lines, say what they get (the result, in the fact gate's words). Then how. A body that opens on the mechanism misses its strongest line.
- **Big stacked numbers, never small steps.** "Rates already went up 45% in five years, with more increases approved" beats "$2.50 more a month". A small number kills the story. Every number still comes from the fact gate.
- **Headline 1 = the winning headline, verbatim.**
- **Headline 2 = one new headline**, same length and shape.
- **Every new headline, every track: 40 characters or fewer, hook in the first 25.** Meta cuts the headline under the image on phones. A 53-character headline did not show. Count the characters before publishing.
- **The first line of each primary must hook on its own.** The feed shows about one line before "See more".

A current, real news headline is a legitimate source for a new headline or first line. Record outlet, date and URL in the provenance table, next to the corpus phrase that shows the buyer cares.

Run the read-aloud pass on every new line. Ship a **provenance table** in the round doc: new line on the left, the corpus phrase it came from on the right. The verbatim percentage is information, never a target. Flow beats the ratio.

## Phase 6. Build the Track A images

**Five images, five emotional angles, one creative variable.**

### Pick the one variable

Small steps inside the winner's format. Pick one from the evidence:

- the **actor**, same headline and scene type;
- the **whole scene**, same headline (a new picture world around the winning words);
- the **headline itself**, same format;
- the **subheading or supporting line**, only together with a bigger move (a new scene, actor or look). A text-only Track A round moves the headline; a subhead alone does not change enough;
- the **colors or look** of the card (palette, type, layout), same words and picture.

One variable per round, across the five images. Everything else in the images stays exactly as the winner's, including the claim. The copy follows Phase 5: slot 1 of each is the winner's verbatim, slot 2 is the one new primary entry and the one new headline. That is the standing shape of every Track A round, not a second variable.

**What is held comes from the winner, not from a neighbour round.** A photo, face or background from another round enters Track A only if its own breakdown shows it carried spend and results. "It has a face" is not evidence. On one real account a round held a man's photo from a zero-result card while the control's own image carried 96% of the spend.

### The five images are five emotional angles, not five rewordings

Five wordings of one idea teach you wording. Five angles teach you **which need this buyer actually has**, and that answer carries into every future round. The precedent is a 13-headline split test grouped into three emotional clusters: speed and ease, confidence, identity. "The winning headline reveals which psychological need is most urgent for this audience right now." See [[headline-split-test]].

- Name five distinct angles before drafting. When you need a menu, use the six lead types: offer, promise, problem-solution, story, proclamation, secret. See [[lead-types-and-awareness]].
- If two images share an angle, one of them is wasted. Replace it.
- Each angle's words still come from the corpus. The angle picks *which* phrases; it never licenses inventing a line.

### Look and craft

- **Inherit the winning image's look.** Copy the renderer or design file that made the winning image and start from it. Same layout system, palette, type family and claim, unless the look itself is the variable. On one real account the loop kept inventing new poster styles against a winner that was pure typography, and three rounds taught nothing.
- **The image must carry the message on its own.** Many people never read the primary text.
- **A real face or a legible number stops the scroll.** Seven of twelve renders in one round were killed because they had neither. Never write an image prompt that bans faces or numbers.
- **Never let an image model type long or exact text.** It invents letters, and a typo burns real budget. See `rules/image-models-never-type-words.md` and "Build and verify the card" below.
- **Words on the image are big, bold, high contrast**, readable by an older reader on a phone. The headline is the first thing the eye finds.
- **Real and a little imperfect beats polished.** Make ads that look like content the buyer already consumes, not like a brand deck.

### When the isolated tests have done their job: consolidate, then visualize

Once recent rounds have a useful read on image treatment, on-image claim, headline and primary, stop re-testing them one at a time. Build a **best-of consolidation round**: the strongest evidenced element from each, with the source round and evidence for every choice. Call it consolidation, not a one-variable test. Then hold that package steady and move the visualization: the same winning message in genuinely different containers.

**The bar is a big win.** New ads not taking spend is not a problem to fix. It means they have not beaten the control yet. Keep shipping.

---

## Track B. Develop what worked or almost worked

One ad set, every day, 3:2:2, next to Tracks A and C. Its job is a better way to sell a reason the account's own results say works or has promise.

The line against Track A: Track A moves one thing and holds the rest. Track B moves several things at once (a new headline in a new world with a new messenger or emotion) around an evidenced angle.

### Start with the account's signals

Read the 3-day results first. Widen to 7 days for sparse or older tests and state both windows. Find ads and assets with results at an attractive cost, **including ones with little spend**. Click rate and click cost can support an "almost worked" hypothesis but do not prove result performance. Record spend, impressions, clicks, results and cost per result for each candidate, then the angle and execution that may explain it. Tiny samples stay hypotheses. Do not turn low spend into a budget request.

On one real account a chat-style ad with no big numbers (a message thread, an old forum post, a handwritten note) got the cheapest leads in the account, at one seventh of the control's cost, on almost no spend. That is the kind of signal Track B develops.

### What stays and what moves

- **Stays: the evidenced source angle.** Name the source ad or asset and its result before building. It can be the control or another promising test. Keep its reason to act.
- **Moves: everything else, several things at once if needed.** A new headline (40 characters or fewer, hook in the first 25). A new visual world. A new messenger. A new emotion. A new explanation of why.
- **Primary 1 = the source ad's primary, verbatim** (with any review fixes, as in Phase 5). Primary 2 is a new entry written for the new way of saying it. Both headlines may be new.

### The test before building

1. Put the three images next to the source ad and the last three Track B rounds. A stranger should call them a different kind of ad. If they look like the same poster with new words, it is Track A.
2. Read the angle line again. Does it develop the named account signal? Then it is Track B. A fresh reason found outside belongs in Track C.
3. Not every round has to be dramatic. Keep it believable and on the source's message.

### Seeds, not a menu

New ways to say a proven angle that have worked: an interview with a real buyer; the cause of the pain shown plainly; the emotion in one line ("AC set to 80. The bill still went up."); a new visual world for the same headline (a plane pulling a banner, a big yellow block with black text, a reporter on site); a before and after of the source's own angle, used lightly.

### Judging Track B

It enters the field and the platform allocates delivery. If its spend, results and cost per result make it the strongest performer, it becomes the control and Track A develops it from the next morning. A new visual world that wins in Track B becomes the format Track A iterates inside.

---

## Track C. External discovery, the big angle swing

One ad set, every day, 3:2:2, next to Tracks A and B. Its job is a new **reason to act** that beats the control's reason. Expect it to lose most days. Ship it anyway.

### What an angle is

The angle is the reason the buyer should act. It is not the picture.

"Rates keep rising, and here is the named cause" is **one** angle. On one real account it shipped seven times as the big swing: a reporter, a thermostat note, front-door signs, a morning paper, a neighbour text, a cardboard sign and a living-room TV. The operator's verdict on the TV: "it's kind of out of the box, but it's the same shit." A new look on the same reason is not Track C. It is Track B.

Real swings look like: the whole street is dark and one house has its lights on (backup power); a plain "get a quote" ad that just says what it is; this month's bill next to the new payment; the deal will not last; a home with the upgrade sells better.

### Step 1. Find external news and attention first

Search current market news, headlines and public conversation for a fresh reason to act that could catch the buyer's eye. Prefer recent developments. Record outlet, publication date, event date and URL, and check the underlying source before using the claim. Explain why it matters to this buyer and how it differs from active angles. State research gaps rather than inventing a timely event. `/last30days <topic>` is a good start.

Use account results to judge relevance and to avoid repeating failed beliefs. Developing efficient low-spend account signals is Track B's job, not this one.

### Step 2. Pick something the account has not tested

Write the angle as **"Act now because ___"** and name the belief underneath it in a few words ("the bill looks wrong", "money paid to the utility", "people like you did it", "it looks right on the house"). Read `research/track-c-angles.md` and the active ads. Has the account already tested this belief, recently? Then pick something else, or say in the round doc why this is a real extension. Running the same belief three days in a row on the same kind of image is the rut to avoid.

Log every Track C round in `research/track-c-angles.md` (template: `references/track-c-angles.md`).

### Step 2b. Pick the awareness level on purpose

Eugene Schwartz's five levels are a second axis next to the angle. See [[lead-types-and-awareness]] and [[eugene-schwartz-frameworks]]. The same belief can be sold at any level; the level decides how the ad opens.

| level | the buyer thinks | how the ad opens |
| --- | --- | --- |
| Unaware | nothing is wrong | call the group, a story, a surprise; the product comes late |
| Problem aware | this cost or risk bothers me | name the pain, then show there is a way out |
| Solution aware | the category exists, not sure it fits me | why this way of doing it is different |
| Product aware | I have seen offers like this, I do not trust them | proof: a real person, a real result, the risk removed |
| Most aware | I want it, show me the deal | the offer and the button, nothing else |

- Tag every round, all tracks, with one level in its round doc. Track C rounds also go in the `level` column of `research/track-c-angles.md`.
- If the last three Track C rounds sat on one or two levels, pick one the account has not tried lately. Unaware and Most aware are the usual gaps, because pain-driven accounts drift to Problem aware.
- Image, headline and the first two lines of the primary all speak at the chosen level.
- When the platform funds a Track C, write its level next to the result. Over a few weeks that shows where the audience sits, which is worth more than any one angle.

Also name the **problem**, the **emotion** and the **buyer type**. See [[breakthrough-advertising-principles]] and [[buyer-persona-strategy]]. A Track C round that repeats the last round's problem and emotion is not a big swing, even with a new picture.

### Step 3. Design an image that stops the scroll and sends them to the next step

The funnel sells one step at a time. The image stops the scroll. The headline sells the read. The primary sells the click. The next step (the form, the calculator, the booking page) sells itself. Every image does its own job **and** points to the next step.

- **Try a comparison first.** Before and after, or this versus that, is the strongest visual these accounts have. Split frame, two rooms, two bills, two years. Show the difference in the picture, not in a sentence. A hair-brand ad that spent over $100k was one clear before/after. A suggestion, not a rule: use another shape when the angle needs it. Both sides must be true, labeled examples inside the fact gate.
- **The account's own photos with big bold words on top** work: real install or product photos designed like a strong graphic, a big headline, a label or arrow on the thing that matters.
- **Real-life surfaces that tell a small story.** A chat, a note, a forum post. But each needs the turn ("a lot has changed since then") and the next step ("check yours in a minute"). A line the viewer has to decode fails.
- **Numbers rarely stop a thumb.** A face, a conversation, a real place or a feeling does. Use a number when it is the story, not as the whole image.
- **Default for a new Track C image: one full scene from one prompt.** A real-looking moment with a person in it and tension in the frame, big bold words low on the image, no bars, no boxes, no arrows. Write the prompt as a scene: who, where, doing what, what feels wrong, light, camera. A stock-looking photo with bars and labels on top did not stand out.

Before shipping, look at the three images as a stranger scrolling past, next to the last three Track C rounds, and answer in the round doc:

1. What would make someone stop on this?
2. In three seconds, what do they understand?
3. Why would they tap, and do they know where it goes?
4. Has this account run anything that looks or argues like it?

If an answer is weak, fix the image before shipping.

### Where the angles come from

1. **External news and public attention** (Step 1).
2. **The operator's spark.** Inspiration to investigate, not proof.
3. **The outside scan, worldwide** (below). It has to shape the ad, not just check it.
4. **Recordings.** Sales calls, coaching calls, partner calls. Search by date and topic, not file title.
5. **The corpus.** Reasons people give for buying, or for fearing it, that no active ad uses. A corpus built from complaints mostly gives complaint angles; when the belief is something else, take the words from the scan or the recordings and add them to the corpus.

Say in the round doc which source the angle came from and, for the scan, which outside ad you borrowed from and what you took (the angle, the kind of picture, the hook shape). `research/track-c-seed-bank.md` holds look ideas; use it only to dress a new angle, never as the reason for a round.

### The outside scan

Search the Facebook Ads Library across the whole world's market for your category, one country at a time. Your own market is one check among many.

- Use searches that return sellers, not gadgets. Use the exact-phrase search: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22<phrase>%22&search_type=keyword_exact_phrase&media_type=all`
- Favour ads that have run for weeks. Long-running usually means it is paying. Several versions of one ad from one advertiser is a second sign.
- Save three inspirations in the round's `research/` folder: the image, the advertiser, the start date and the first lines of copy.
- Take the angle and the kind of picture. **Never a competitor's claim or number.**
- Read only. Never log in, post, comment, like or message through the browser.

If browsing is not available, say so in the round doc and continue with the other sources.

### Copy in Tracks B and C

Corpus-locked, same as Track A. The picture goes wild. The words do not.

- The format may force shorter copy. Lift the phrases, cut the length, keep the provenance table.
- **Primary texts target 12 to 15 nonblank lines.** Seventeen is already long.
- **Chat formats have to sound like chat.** Draft the exchange as two real people talking: contractions, short replies, ordinary words, believable turn-taking. Corpus provenance does not rescue a text thread that reads like ad copy cut into bubbles.
- **No invented testimonial.** A chat or post may dramatise a question or a doubt, never a customer result that did not happen.
- The same lead form and funnel as the control. New angles go into the same form, so the winning angle shows itself.

### Judging Track C

Do not judge it against the control on its first partial day, and do not kill it. It enters the field like every other ad and the platform decides. Each morning's Phase 1 re-selects the control from the 3-day numbers, with no minimum age. When a Track C ad's spend, results and cost per result make it the strongest performer, it becomes the control and Track A starts iterating on it. That is the whole payoff.

---

## Build and verify the card (every track)

Two real misses in one day: an arrow tip landing on a face, and a circle drawn under a label instead of around it. Both times the cause was the same: marks placed on guessed coordinates, and the same agent judging its own render.

### Pick the design route

Track A keeps the winner's renderer. This choice is for Tracks B and C.

| route | use when | how |
| --- | --- | --- |
| **Image-model design** | no real person's face in the photo, and the words are short (a headline, two labels, a button) | give the model every word spelled out, what each arrow points at, and the brand colors |
| **Code render** (HTML, headless Chrome or a design tool) | a real person's face is in frame (never let a model redraw it), long text, exact numbers, a chat or forum mock-up, or exact brand fonts | `/brand-graphic`, or a template copied from an earlier round |

Design principles (judgement, not rules):

- An arrow points at a thing, never at a face, and its tip stops just short of it. One or two per image.
- A circle goes around its target with room to spare. In HTML, attach it to the target element so it moves with it.
- Name a person with a tag beside them, not an arrow.
- Hide readable other-company names on clothes, vans and signs.
- Pick the best frame, not the first.

### The verification loop

1. Write what each mark is meant to point at, one line per arrow, circle or label, in `images/<card>.intent.txt`.
2. Show each finished card to a **second eye with no stake in it**: a different model, or a person. Ask what each mark lands on and whether every word is spelled right.
3. On a miss, fix the card, render again, re-check. Stop at a pass, or after three tries; ship the best version only if the problem is small, and name it in the round doc.
4. Then look at every image yourself at full size. The checker is a second eye, not the only one.
5. Paste the checker's verdict in the round doc.

---

## Phase 7. Hand it over

1. **Present the case, then stop.** Show the Phase 2 verdict, the Track A variable and five angles, the Track B source signal, the Track C angle and its awareness level, and the rendered images. **Show both primaries and both headlines right next to each preview,** so the operator reads the whole ad in one pass. If the operator wants to talk first, stay in the conversation and build nothing until they say build.
2. **Publish only after a named go.** See `rules/publish-preflight.md`.
3. Each track is its **own ad set**, inside the **live campaign**. Copy every setting off the control ad set on the day you publish: targeting, optimisation goal, conversion event and data set, attribution, placements, page, lead form, call to action, creative enhancement opt-outs. Typing those in from memory is how a round ends up testing something it did not mean to.
4. **Start at 00:00 tomorrow in the ad account's own time zone.** Read the time zone off the account, never from notes. A mid-day start makes the platform read a partial first day as a bad day.
5. **A paused ad set that nobody turns on is not shipped.** Only pause a round that genuinely should not run, and say so.
6. **Check asset counts before publishing:** Track A is 5 images, 2 primaries, 2 headlines. Tracks B and C are 3 images, 2 primaries, 2 headlines.
7. **Re-read after publishing.** Open the new ad sets and confirm every field, and confirm the control was not touched. A successful click is not proof. See `rules/verify-published-not-described.md`.
8. Some per-ad settings do not copy (for example Messenger follow-up on lead ads). Say so in the round doc: until it is switched on, the comparison is confounded.

**Same-day extra rounds** are cheap. Copy a round folder into the next number for its track (`a2`, `b2`, `c2`), change one asset slot, write a `variable.md` saying what moved and what held. Change only one of image, primary or headline, so the round can be read.

## Phase 8. Log it

- Write each round's `ad-set.md` from `references/round-doc.md`.
- Add the Track C angle and its level to `research/track-c-angles.md`. Add every new look to `research/round-image-inventory.md`.
- Append the new verbatim phrases to `research/copy-corpus.md`. Each round starts from a bigger pile. That is the compounding part.
- Append this round's result to the previous round's doc once the numbers land.
- A campaign lesson with evidence becomes a page in `knowledge/lessons/`.

## Never

- Pick the control by spend alone, or by the cheapest isolated result. Read spend, results and cost per result together and show the numbers.
- Argue that the budget should have gone somewhere else, or ask for a dedicated budget, spend floor or separate campaign for any ad or track.
- Stop at the ad level. Always break down to image, headline and primary.
- Invent a look in Track A. Tracks B and C may use any look.
- Call a new picture on the same reason a Track C. That is Track B.
- Change anything between control and challenger without a line of evidence.
- Invent copy. A line that cannot be traced to a corpus phrase or a dated news source does not ship.
- Put a money number in an ad that is not in the fact gate with a verified date.
- Let an image model type long or exact text, or redraw a real person's face.
- Ship three primary texts in any track.
- Edit, pause, duplicate or reactivate a live ad, ad set or campaign.
- **Propose** pausing, thinning the field, consolidating ad sets, or freeing budget.
- Skip a day because yesterday's round took little spend or the numbers are not "significant".
