"""The One-Line Laugh — make.fun entry.

Writes a single original funny line to /output/entry.txt.
Deterministic, no network, no secrets.
"""

from pathlib import Path

LINE = (
    "I bought a standing desk to fix my posture, "
    "so now I slouch vertically instead of horizontally."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    # Gate self-check: one sentence, 1-200 UTF-8 characters, not blank.
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
