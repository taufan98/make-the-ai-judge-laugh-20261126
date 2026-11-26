#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one line to /output/entry.txt: a single joke about office life,
under 200 characters. The judge picks the funniest head to head.
"""

import os

ENTRY = (
    "Our team-building exercise was a meeting about why nobody "
    "likes team-building exercises."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
