# Nodal

Nodal is a personal design exploration of what a language could look like
if it were built from scratch around strict constraints: 2–5 letter
morphemes, zero homonymy, mandatory part-of-speech prefixes, and a
modular visual writing system called **Gliph**.

It is **not** intended to be spoken, adopted, or standardized. It is
presented as a finished artifact — a demonstration that such a language
can exist, and a foundation for anyone who wants to take it further.

## What is here

- **Specification** — phonetics, morphology, syntax, prosody.
  → `docs/Nodal_specification.md`
- **Vocabulary** — roots, prefixes, suffixes, JSON registry.
  → `docs/Nodal_vocabulary.md`
- **Gliph** — the slot-based modular writing system.
  → `docs/Nodal_glyph-specification.md`
- **Web renderer** — live demo of the Gliph cells.
  → https://tsar8.github.io/nodal/

## Background

The design constraints are deliberate and strict. Every morpheme is
2–5 letters, every content word starts with a grammatical prefix, no
two roots share a meaning, and opposites are always two independent
roots rather than a negative prefix. Gliph is a visual layer that fits
each morpheme into a 5-slot cell `[A]–[E]`.

Whether these constraints make the language *better* is an open
question. They make it *different*, and that is the point of the
exercise.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The dictionary can be validated
locally with:

    python validate.py

## License

- **Code** (HTML, JavaScript, Python) — MIT.
  See [`LICENSE-MIT`](LICENSE-MIT).
- **Specification, vocabulary, and dictionary** — CC-BY-4.0.
  See [`LICENSE-CC-BY-4.0`](LICENSE-CC-BY-4.0).