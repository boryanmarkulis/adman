# Image models never type long or exact words

## Rule

Never ask an image model to render long text, exact numbers, prices, chat or forum mock-ups, or any words over a real person's face. Generate the picture with no lettering, then set those words in HTML, SVG or a design tool and composite them on top.

Short words are the one exception: a headline, two labels or a button, on an image with no real person's face. Then spell every word out in the prompt, and proofread the result with a second eye before it ships (the card check in `/ad-loop`).

Do not over-correct: faces and legible numbers belong in ad images. Never write a prompt that bans them.

## Why

Image models invent letters. A typo in a live ad burns real budget and looks like a scam. Later tests showed current image models can lay out a short headline and two arrow labels cleanly, and the result looked better than the hand-coded version, so short words are allowed when they are checked. Separately, one round banned faces, legible text and numbers from the image prompt to be safe, and it removed the only two things that reliably stop a scroll: a real face, or a number you can read. Seven of twelve renders in another round were killed for having neither.

## Apply

- Long or exact text, numbers, faces with words: add "no text, no letters, no logos" to the prompt, type the words afterwards and render to PNG.
- Short words on a faceless image: spell every word in the prompt, then run the card check.
- Proofread the rendered image, not the source text.
- Keep the words big, bold and readable at thumbnail size.
