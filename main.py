# SPDX-License-Identifier: MIT
"""Write one persuasive sentence to /output/entry.txt.

The sentence is a single fixed pitch: describe the app you have always
wanted, the agent builds it while you watch, and by dinner you are showing
it to your friends. It is written to /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR) as UTF-8, 1 to 240 characters (the sentence
is 131 characters), never only whitespace. No network, no randomness, no arguments.
The output directory is created if missing and never deleted.
"""

import os
import sys

TEXT = (
    "You describe the app you have always wanted, the agent builds it "
    "while you watch, and by dinner you are showing it to your friends."
)

# A short, known-valid sentence used only if TEXT ever failed the gate.
FALLBACK = (
    "Tell the agent your idea in plain words, and it writes the whole "
    "app while you have coffee."
)


def valid(text: str) -> bool:
    """Competition gate: 1-240 characters, not only whitespace."""
    return 1 <= len(text) <= 240 and bool(text.strip())


def choose_text() -> str:
    if valid(TEXT):
        return TEXT
    if valid(FALLBACK):
        return FALLBACK
    print("error: no valid entry text available", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    text = choose_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
