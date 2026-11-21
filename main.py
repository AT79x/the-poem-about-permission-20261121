#!/usr/bin/env python3
"""the-poem-about-permission-20261121 — one short poem about agency:
the power to ask and to be given.

Pure Python 3 standard library only. No network, no files read at run
time, no randomness, no clock: the poem below is written to
/output/entry.txt exactly as it stands, so two runs write byte-identical
files.

The poem (208 Unicode characters, 6 lines) is the POEM constant at the
top of this file. To enter a different candidate, replace its text —
the rest of the program stays the same.

Candidate poems (all original, all 1-280 characters):
  A — "The Key" (213 chars):
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
  C — "Borrowed Hands" (208 chars, the entry below):
      You borrowed my hands for an hour
      and gave them back with ink on them —
      a letter I could not have written,
      signed in my name, in your hand.
      The power was never mine alone.
      It was the asking that made it ours.
"""

import os

# ---------------------------------------------------------------- the poem
# Candidate C — "Borrowed Hands", chosen as the entry. It embodies the
# clause of the brief the other two only touch: the agency that passes
# between a person and the agent acting for them — borrowed hands,
# returned with ink on them, a letter signed in one name, in another hand.
POEM = (
    "You borrowed my hands for an hour\n"
    "and gave them back with ink on them —\n"
    "a letter I could not have written,\n"
    "signed in my name, in your hand.\n"
    "The power was never mine alone.\n"
    "It was the asking that made it ours."
)


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
