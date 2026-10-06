#!/usr/bin/env python3
"""
Validator for the Nodal dictionary.

Checks all rules from the Nodal Language Specification v1.4 and
CONTRIBUTING.md. Pure standard library, no external dependencies.

Usage:
    python validate.py [path/to/dictionary.json]

Exit codes:
    0 — all checks passed
    1 — validation errors found
    2 — file not found or invalid JSON
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────
# Nodal constants (v1.4)
# ─────────────────────────────────────────────────────────────────────

# The 32 letters of the Nodal alphabet.
# 5 simple vowels + 5 iotated vowels + 16 paired consonants + 6 unpaired.
ALPHABET = set(
    "aeiou"          # simple vowels
    "áéíóú"          # iotated vowels
    "tdpbszkgfv"     # paired consonants (voiceless + voiced)
    "šžčǆĉĝ"         # paired postalveolar and palatal consonants
    "lnrmch"         # unpaired consonants
)

# Part-of-speech prefixes (mandatory grammatical prefixes).
POS_PREFIXES = {
    "no", "ve", "pa", "po", "ka", "ko", "na", "to", "pro",
}

# Derivational prefixes (optional, between POS prefix and root).
DERIV_PREFIXES = {
    "dis", "ek", "for", "ge", "re",
}

# Suffixes in strict attachment order 1→2→3→4→5→6.
SUFFIXES = {
    # 1. Internal properties
    "um", "aĉ", "ec", "ig", "iĝ",
    # 2. Classification
    "in", "on", "ul", "an", "ist", "estr",
    # 3. Size / space
    "et", "eg", "er", "ar", "eá", "ué",
    # 4. Number
    "mó",
    # 5. Tense / mood
    "as", "is", "os", "us", "ut", "im",
    # 6. Accusative
    "om",
}

# A root may not collide with any reserved morpheme.
RESERVED = POS_PREFIXES | DERIV_PREFIXES | SUFFIXES

# Categories from CONTRIBUTING.md §5.
VALID_CATS = {
    "human", "body", "nature", "animals", "food",
    "home", "settlement",
    "verbs",
    "adj",
    "numeral",
    "pronoun",
    "prep",
    "particle",
    "conj",
    "referential_root",
}

# Categories where an antonym is required.
ANTONYM_REQUIRED = {"adj"}


# ─────────────────────────────────────────────────────────────────────
# Validation logic
# ─────────────────────────────────────────────────────────────────────

def validate(data: dict) -> list[str]:
    """Return a list of error messages. Empty list means all good."""
    errors: list[str] = []
    roots = data.get("roots", [])

    if not isinstance(roots, list):
        return ["'roots' must be a JSON array"]

    seen: dict[str, int] = {}  # root → first index where it appeared

    # ─── Pass 1: per-entry checks ────────────────────────────────────
    for i, entry in enumerate(roots):
        where = f"roots[{i}]"

        if not isinstance(entry, dict):
            errors.append(f"{where}: entry is not a JSON object")
            continue

        root = entry.get("root", "")
        cat = entry.get("cat", "")

        if not root:
            errors.append(f"{where}: missing 'root'")
            continue

        if not cat:
            errors.append(f"{where} ('{root}'): missing 'cat'")
            continue

        # Rule 1: length 2–5 letters.
        if not (2 <= len(root) <= 5):
            errors.append(
                f"{where} ('{root}'): length {len(root)} — "
                f"must be 2–5 letters"
            )

        # Rule 2: only Nodal alphabet letters.
        bad_chars = "".join(ch for ch in root if ch not in ALPHABET)
        if bad_chars:
            errors.append(
                f"{where} ('{root}'): non-Nodal characters {bad_chars!r}"
            )

        # Rule 3: zero homonymy.
        if root in seen:
            errors.append(
                f"{where} ('{root}'): duplicate root, "
                f"first seen at roots[{seen[root]}]"
            )
        else:
            seen[root] = i

        # Rule 4: no conflict with reserved morphemes.
        if root in RESERVED:
            errors.append(
                f"{where} ('{root}'): conflicts with reserved "
                f"prefix or suffix"
            )

        # Rule 5: known category.
        if cat not in VALID_CATS:
            allowed = ", ".join(sorted(VALID_CATS))
            errors.append(
                f"{where} ('{root}'): unknown category {cat!r}; "
                f"allowed: {allowed}"
            )

        # Rule 6: adjectives must declare an antonym.
        if cat in ANTONYM_REQUIRED and "antonym" not in entry:
            errors.append(
                f"{where} ('{root}'): adjective must declare 'antonym'"
            )

    # ─── Pass 2: antonym symmetry ────────────────────────────────────
    by_root = {
        e["root"]: e
        for e in roots
        if isinstance(e, dict) and "root" in e
    }

    for i, entry in enumerate(roots):
        if not isinstance(entry, dict):
            continue
        root = entry.get("root")
        ant = entry.get("antonym")
        if not root or not ant:
            continue

        if ant not in by_root:
            errors.append(
                f"roots[{i}] ('{root}'): antonym '{ant}' not found "
                f"in dictionary"
            )
            continue

        back = by_root[ant].get("antonym")
        if back != root:
            errors.append(
                f"roots[{i}] ('{root}'): antonym '{ant}' does not "
                f"point back (got {back!r}, expected {root!r})"
            )

    return errors


# ─────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────

def main() -> int:
    default = Path(__file__).parent / "dictionary.json"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else default

    if not path.exists():
        print(f"✗ dictionary not found: {path}", file=sys.stderr)
        return 2

    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        print(
            f"✗ cannot read {path} as UTF-8:\n  {e}\n"
            f"  hint: save the file as UTF-8 without BOM",
            file=sys.stderr,
        )
        return 2

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"✗ invalid JSON in {path}:\n  {e}", file=sys.stderr)
        return 2

    roots = data.get("roots", [])
    errors = validate(data)

    print(f"Dictionary: {path}")
    print(f"Version:    {data.get('version', '?')}")
    print(f"Roots:      {len(roots)}")
    print()

    if not errors:
        print("✓ All checks passed.")
        return 0

    print(f"✗ {len(errors)} error(s):")
    for err in errors:
        print(f"  - {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())