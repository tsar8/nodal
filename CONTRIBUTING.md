# Contributing to Nodal

Thank you for your interest in Nodal. This document describes how to propose a new root, an antonym, or a correction to the language dictionary.

---

### What You Can Propose

* **New root** — adding a meaning that does not yet exist in the language.
* **Antonym** — a paired root for an existing adjective.
* **Correction** — typo, incorrect translation, or inaccurate category.
* **New category** — only via discussion in GitHub Issues, not through a PR.

---

### Rules for a New Root

All rules derive from the Nodal v1.4 specification and are automatically verified by the `validate.py` script.

#### 1. Length: 2–5 Letters
Law of Wave Cell: every morpheme — root, prefix, suffix, conjunction — is strictly between 2 and 5 letters long. There are zero single-letter morphemes in Nodal.

| Example | Result |
| :--- | :--- |
| `a` | ❌ 1 letter |
| `vidim` | ❌ 6 letters |
| `vid`, `hom`, `grand` | ✓ |

#### 2. Only Nodal Alphabet Letters
32 letters: `a e i o u á é í ó ú t d p b s z k g f v š ž č ǆ ĉ ĝ l n r m c h`

Latin letters outside this list, Cyrillic, numbers, and punctuation marks are not allowed.

| Example | Result |
| :--- | :--- |
| `video` | ❌ letter `o` exists, but `e` is not iotated; 5 letters long ✓, but this is an English loanword (see §7) |
| `xyz` | ❌ `x` and `y` are not in the alphabet |
| `vok` | ✓ |

#### 3. Zero Homonymy
Every root corresponds to exactly one unique meaning. If a root is already taken, it cannot be proposed with a different meaning.
Check the existing dictionary: `dictionary.json`.

| Example | Result |
| :--- | :--- |
| `hom` for "earth" | ❌ already taken by "human" |
| `sol` for "soul" | ❌ already taken by "sun" |

#### 4. No Overlap with Prefixes or Suffixes
A root must not conflict with:
* **Part-of-speech prefix:** `no`, `ve`, `pa`, `po`, `ka`, `ko`, `na`, `to`, `pro`
* **Derivational prefix:** `dis`, `ek`, `for`, `ge`, `re`
* **Suffix:** `um`, `aĉ`, `ec`, `ig`, `iĝ`, `in`, `on`, `ul`, `an`, `ist`, `estr`, `et`, `eg`, `er`, `ar`, `eá`, `ué`, `mó`, `as`, `is`, `os`, `us`, `ut`, `im`, `om`

| Example | Result |
| :--- | :--- |
| `čaj` | X letter `j` is not in the alphabet |
| `vqo` | X `q` is not in the alphabet |

#### 5. Category from Fixed List

| `cat` | Meaning |
| :--- | :--- |
| **human** | people, relatives, social roles |
| **body** | body parts |
| **nature** | nature, cosmos, elements |
| **animals** | animals |
| **food** | food and drinks |
| **home** | home, household items |
| **settlement** | settlements |
| **verbs** | actions and states |
| **adj** | qualities (must include an antonym) |
| **numeral** | numbers |
| **pronoun** | pronouns |
| **prep** | prepositions |
| **particle** | particles |
| **conj** | conjunctions |
| **referential_root** | roots for `ka-` / `to-` |

#### 6. Antonyms for Adjectives
If `cat: "adj"`, the root **must** have an `antonym` — another root denoting the opposite quality.
Nodal does not use negative prefixes like `mal-`. Antonym pairs are two independent roots.

| Example | Result |
| :--- | :--- |
| `bon` / `dol` | ✓ good / bad |
| `grand` / `mikr` | ✓ large / small |
| `bon` without antonym | ❌ |

Antonyms must be **symmetric**: if `bon` → `dol`, then `dol` → `bon`. The validator checks this automatically.

#### 7. Phonotactics and Loanwords
A root should not be a direct loanword from a natural language if it violates the phonetic character of Nodal. Preference is given to short, "dense" forms characteristic of the language.

**Discouraged:**
* Clusters of 3+ consecutive consonants at the beginning of a word;
* Rare combinations like `x`, `q`, `w` (which are not in the alphabet);
* Long loanwords like `telefon`, `kompjutr`.

**Encouraged:**
* Short forms (2–4 letters);
* Open syllables (consonant + vowel);
* Recognizability through root associations (`vid` — see, `aud` — hear, `manĝ` — eat).

---

### How to Propose a Change

1. **Fork** the repository.
2. **Open** `dictionary.json`.
3. **Add** a new entry to the `roots` array.

**Format:**

*Noun / verb / preposition / conjunction:*
```json
{ "root": "vok", "cat": "verbs", "en": "sound / to sound" }
```

*Adjective (with antonym):*
```json
{ "root": "klam", "cat": "adj", "en": "quiet", "antonym": "laŭt" },
{ "root": "laŭt", "cat": "adj", "en": "loud", "antonym": "klam" }
```

4. **Run the validator locally:**
```bash
python validate.py
```
If there are errors, fix them and run again.

5. **Open a Pull Request.** In the description, specify:
* Which root (or roots) you are adding;
* Why it is needed in the language;
* Examples of usage with different prefixes: `no-vok` (sound), `ve-vok-as` (sounds), `pa-vok` (acoustic);
* For adjectives — the antonym pair.

---

### What Happens to a PR

* GitHub Actions automatically runs `validate.py`.
* If all checks pass — a maintainer will review and merge (or ask for revisions).
* If checks fail — please correct them and update the pull request. A maintainer will re-review once checks are green.
* Controversial cases (new categories, large blocks of words) are discussed in GitHub Discussions → Root proposals.

---

### What Will Not Be Accepted

* Words duplicating existing meanings.
* Roots with homonymy.
* Violations of the 2–5 letter length rule.
* Adjectives without an antonym pair.
* Direct loanwords violating Nodal phonotactics.

---

### Style Guidelines

* In `en`, provide a brief English gloss, not a full definition.
* Category — strictly from the list above.
* Antonyms — exact, not "opposite in meaning".
* Order of roots in the file — by category, as currently structured.

---

Thank you for helping Nodal develop.
