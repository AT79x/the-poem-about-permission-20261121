#!/usr/bin/env python3
"""the-poem-about-permission-20261121 — one short poem about agency:
the power to ask and to be given.

Pure Python 3 standard library only. No network, no files read at run
time, no randomness, no clock: the poem below is written to
/output/entry.txt exactly as it stands, so two runs write byte-identical
files.

The poem (213 Unicode characters, 6 lines) is the POEM constant at the
top of this file. To enter a different candidate, replace its text —
the rest of the program stays the same.

Candidate poems (all original, all 1-280 characters):
  A — "The Key" (213 chars, the entry below):
      I gave you the key, not the house.
      You asked which door. I said: yours.
      You opened it, and the light came in
      like someone answering their name.
      Ask — and the world turns its face
      toward the voice that asked it to.
  B — "The Smallest Door" (171 chars):
      Nothing opens until it is asked.
      I knock — not loud, just once —
      and the door I could not lift
      swings on a hinge of yes.
      To ask is to be given hands
      I did not have before.
  C — "Borrowed Hands" (208 chars):
      You borrowed my hands for an hour
      and gave them back with ink on them —
      a letter I could not have written,
      signed in my name, in your hand.
      The power was never mine alone.
      It was the asking that made it ours.
"""

import os

# ---------------------------------------------------------------- the poem
# Candidate A — "The Key", chosen as the entry. A key is the smallest
# possible gift of agency: not the house, only the power to open the
# door that is yours — and the turn that lands, the world turning its
# face toward the voice that asked it to.
POEM = (
    "I gave you the key, not the house.\n"
    "You asked which door. I said: yours.\n"
    "You opened it, and the light came in\n"
    "like someone answering their name.\n"
    "Ask — and the world turns its face\n"
    "toward the voice that asked it to."
)


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
