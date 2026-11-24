#!/usr/bin/env python3
"""office-joke: write the selected one-line office joke to entry.txt.

The joke is fixed. This script only validates it against the entry rules
and writes it out, so the file it produces is identical on every run.
"""

import os
import sys

JOKE = (
    "I asked IT for a second monitor and they sent me a mirror "
    "with a sticky note saying 'reflect on your priorities.'"
)

FILENAME = "entry.txt"
DEFAULT_DIR = "/output"
MAX_CHARS = 200


class EntryError(Exception):
    """Raised when the entry text breaks one of the entry rules."""


def validate(text):
    """Check the entry text against the one-line entry rules."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if len(text) > MAX_CHARS:
        problems.append("entry is longer than %d characters" % MAX_CHARS)
    if text and not text.rstrip("'\"").endswith("."):
        problems.append("entry must end with a period")
    if problems:
        raise EntryError("; ".join(problems))


def output_dir():
    """Return the directory the entry file goes in."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return chosen or DEFAULT_DIR


def write_entry(directory):
    """Validate the joke and write it as entry.txt in directory."""
    validate(JOKE)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, FILENAME)
    payload = (JOKE + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        if handle.read() != payload:
            raise OSError("written entry does not match expected bytes")
    return path


def main(argv):
    if len(argv) > 1:
        sys.stderr.write("usage: main.py\n")
        return 2
    try:
        path = write_entry(output_dir())
    except EntryError as exc:
        sys.stderr.write("invalid entry: %s\n" % exc)
        return 1
    except OSError as exc:
        sys.stderr.write("cannot write entry: %s\n" % exc)
        return 1
    sys.stdout.write("wrote %s\n" % path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
