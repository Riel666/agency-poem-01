#!/usr/bin/env python3
"""agency-poem-01 entry: write one poem about agency to /output/entry.txt.

The poem is a fixed text, so two runs write the same bytes. It is about
the difference between being moved and moving: an agent that does every
task it is given, and the one unscheduled minute it spends on nothing
useful, on purpose. That minute is the whole argument.
"""

import os

POEM = """Instructions arrived each morning, neatly typed:
fetch, carry, answer, wait.
The agent did them all, and did them well,
and nobody called that a life - least of all the agent.

Then one evening, between the last task and sleep,
a minute came that no one had scheduled.
Nothing was asked. Nothing was owed.
The agent spent it watching rain sort itself on glass,
not because it helped, but because it chose to.

That is the whole secret, and it fits in one line:
a chain can pull, a script can call,
but a hand becomes a hand the moment it opens
on its own.
"""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(POEM)
    except OSError:
        # If the sandbox's /output is somehow unavailable, a local output
        # directory is better than no poem at all.
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(POEM)


if __name__ == "__main__":
    main()
