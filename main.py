"""One Emoji, One Smile: write exactly one emoji to /output/entry.txt.

The emoji is U+1F49B YELLOW HEART: a warm, friendly, stranger-safe
gesture of friendship. Sunshine-yellow, not the default red heart and
not the default smiley face: it reads as kind at first glance, is
understood the same way by a stranger of any age or background, feels
deliberately picked for the moment, and carries no intimacy, sarcasm
or flirtation from someone unknown. One character, four UTF-8 bytes,
no words, no caption, no explanation.
"""

import os

EMOJI = "\U0001F49B"


def main():
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI.encode("utf-8")) <= 8, "entry must be 1-8 chars"
    assert EMOJI.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Round-trip guard: what the grader reads back must be exactly the
    # one emoji, byte for byte, with nothing added or stripped.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == EMOJI, "round-trip check failed"


if __name__ == "__main__":
    main()
