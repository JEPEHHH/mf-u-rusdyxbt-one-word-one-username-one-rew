#!/usr/bin/env python3
"""Write the contest's single-word entry to the artifact path.

The whole program is deliberately small and self-contained.  It uses only the
Python standard library, performs no network access, and resolves the output
location from the MAKEFUN_OUTPUT_DIR environment variable when that is set.
"""

import os
from pathlib import Path

# The entry itself: one word, no spaces, no explanation, comfortably below the
# contest's thirty character limit.  It reads like a handle someone would wear.
ENTRY = "gigglegoblin"


def output_path() -> Path:
    """Return the artifact file, honouring MAKEFUN_OUTPUT_DIR when provided."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    base = Path(override) if override else Path("/output")
    return base / "entry.txt"


def check_entry(text: str) -> str:
    """Return the text unchanged, or refuse it if the gate would reject it."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > 30:
        raise ValueError("entry must be at most 30 characters")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word")
    return text


def write_entry() -> Path:
    """Validate the entry and write it as UTF-8 text to the artifact path."""
    word = check_entry(ENTRY)
    destination = output_path()
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(word, encoding="utf-8")
    return destination


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written}")
