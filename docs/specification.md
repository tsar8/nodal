# Specification Version 1.5

**Standard Version:** 1.5   
**Status:** Personal design artifact. Not a proposal for adoption.
**Purpose:** Reference guide to the philosophy, phonetics, morphology,
syntax, prosody, and digital interfaces of the Nodal language, as
designed by its author. 
**Update Date:**2026-10-07 

---

## 1. Philosophy and Principles

**Nodal** is a personal design exploration — a constructed language built from scratch around strict morphological constraints. The design goal was not to be optimal for humans or for machines, but to see what a language looks like when those constraints are applied consistently and without exception.

The result is documented here as a finished artifact. It is not presented as a solution to a problem, nor as a research finding, nor as a standard. It is a demonstration that such a language can exist.

* **Zero Redundancy:** Every grammatical element carries exactly one meaning ("one sign = one meaning"). There are no redundant agreements in gender or number.
* **Maximum Clarity (0% Homonymy):** Complete absence of homonyms. Every root possesses a unique meaning, eliminating contextual ambiguity.
* **Compositionality:** The meaning of a complex word strictly equals the sum of its constituent meanings (prefix + root + suffixes).
* **Digital Design:** All roots are strictly constrained to **2 to 5 letters**, fitting into the 5-position modular cell [A]–[E] of the Gliph writing system and the 3-digit numerical modules.
* **Algorithmicity:** 100% absence of grammatical exceptions. Any word or sentence is unambiguously parsed by a linear parser in a single pass.

---

## 2. Phonetics and Prosody

### 2.1. Alphabet and the "Fixed Pronunciation Rule" Rule

The Nodal alphabet consists of **32 letters** (10 vowels + 22 consonants). Every letter is pronounced strictly identically, regardless of its position in a word.

*Note*: The Fixed Pronunciation Rule guarantees that every letter has exactly one stable pronunciation regardless of position. Iotated vowels (á = [ja]) and affricates (ǆ = [dʒ]) map to two IPA symbols each, but their pronunciation is still invariant.

* **Simple Vowels (5):** `a` [a], `e` [e], `i` [i], `o` [o], `u` [u].
* **Iotated Vowels (5):** `á` [ja], `é` [je], `í` [ji], `ó` [jo], `ú` [ju].
* **Paired Consonants (16 sounds / 8 pairs):**
  * `t` [t] / `d` [d]
  * `p` [p] / `b` [b]
  * `s` [s] / `z` [z]
  * `k` [k] / `g` [g]
  * `f` [f] / `v` [v]
  * `š` [ʃ] / `ž` [ʒ]
  * `č` [tʃ] / `ǆ` [dʒ]
  * `ĉ` [tɕ] / `ĝ` [dʑ]
* **Unpaired & Sonorant Consonants (6):** `l` [l], `n` [n], `r` [r], `m` [m], `c` [ts], `h` [x].

*Note:* Letters `ŭ`, `ɣ`, and `x` are excluded from the alphabet. Diphthongs are written using standard `u` (e.g. `au`, `nau`, `ko-au`). There is no separate letter **j**. Iotation is expressed exclusively by the single characters **á**, **é**, **í**, **ó**, **ú**.

### 2.2. Stress Rule

* **Part-of-speech Prefix** (`no-`, `ve-`, `pa-`...) is always **unstressed** and pronounced as a rapid pickup (anacrusis).
* **Stress ALWAYS falls on the FIRST syllable of the root** (e.g. `no-HOM-in`, `ve-AM-as`, `pa-DEKir-as`). This creates a 3-phase acoustic wave: *unstressed pickup ➔ stressed semantic peak ➔ unstressed fall on suffixes*.

### 2.3. Hierarchy of Syntactic Pauses

To prevent slurring in spoken discourse, 4 levels of pauses are defined:

* **Pause 0:** Inside a word and a wave morpheme cell.
* **Micro-pause `|`:** Separates the head word with primary focus from secondary modifiers and background details.
* **Medium Pause `||`:** Separates major syntactic blocks in SOV structure (Subject || Object || Verb).
* **Inter-clause Pause `|||`:** Mandatory before conjunctions (`ko-`) and relative nodes (`to-`) at clause boundaries inside a single sentence.
* **Sentence-final Pause `||||`:** Terminates a sentence. Never occurs inside a sentence; always closes it. In speech it is realized as the longest pause and a falling terminal contour.

The pause level is encoded by the number of vertical bars: one, two, three, or three bars plus a terminal modifier (Section 2.4).

### 2.4. Punctuation as Pause Modifier

Punctuation marks are not written literally. They are **rendered as a pause of the appropriate level**, with the fourth element replacing the final bar:

| Input | Rendered as | Bars | Modifier | Function |
| :--- | :--- | :--- | :--- | :--- |
| `,` | `\|` | 1 | — | micro-pause |
| `;` | `\|\|` | 2 | — | medium pause |
| `:` | `\|\|:` | 2 | two dots (bottom dot on slot [C]) | explanatory pause |
| `.` | `\|\|\|\|` | 3 | horizontal bar | declarative sentence end |
| `!` | `\|\|\|/` | 3 | rising slash | exclamative sentence end |
| `?` | `\|\|\|\\` | 3 | falling backslash | interrogative sentence end |

The literal forms `|`, `||`, `|||`, `||||` may also be typed directly; they render identically to `.`, `;`, `:`, `.` respectively where the bar count matches. This allows explicit prosodic transcription without punctuation.

**Rule:** the bar count determines the pause **level**; the modifier determines the pause **type**. A modifier never appears without bars.

### 2.5. Whitespace Around Punctuation

Whitespace immediately preceding or following a punctuation mark or pause marker is not significant. Renderers suppress it: the punctuation mark or pause is rendered flush against the neighbouring morpheme or cell. Whitespace between words without intervening punctuation is preserved as a word separator.

---

## 3. Morphology

### 3.1. Mandatory Part-of-Speech Prefixes

Every content word begins with a mandatory prefix that defines its grammatical category:

| Prefix | Category / Function | Example | Meaning |
| :--- | :--- | :--- | :--- |
| **no-** | Noun (Entity / Object) | `no-dom` | house |
| **ve-** | Verb (Action / State) | `ve-vid-as` | sees |
| **pa-** | Adjective (Quality / Property) | `pa-grand-as` | large |
| **po-** | Adverb / Circumstance / Preposition | `po-bon` | well |
| **ka-** | Interrogative word | `ka-ku` | who |
| **ko-** | Conjunction | `ko-sed` | but |
| **na-** | Numeral | `na-tri` | three |
| **to-** | Relative / Demonstrative word | `to-ku` | which / who |
| **pro-** | Pronoun (Personal / Demonstrative) | `pro-mi` | I / me |

### 3.2. Derivational Prefixes

Inserted strictly between the part-of-speech prefix and the root:

* **dis-** — separation / dismantling (`ve-dis-lig-as` — unties)
* **ek-** — inchoative / start of action (`ve-ek-ir-as` — sets off / starts walking)
* **for-** — removal / departure (`ve-for-ir-as` — goes away)
* **ge-** — joint gender (`no-ge-frat-mó` — brothers and sisters / siblings)
* **re-** — repetition / return (`ve-re-far-as` — redoes / remakes)

### 3.3. Suffixes (Strict Order: 1 ➔ 2 ➔ 3 ➔ 4 ➔ 5 ➔ 6)

1. **Internal Properties and Modifications:**
   * `-um-` — special operator / idiomatic (`ve-han-um-as` — handle / operate)
   * `-aĉ-` — pejorative / low quality (`no-dom-aĉ` — hovel)
   * `-ec-` — abstract property (`pa-bon-ec` — goodness)
   * `-ig-` — causative / to make into (`ve-bon-ig-as` — improve)
   * `-iĝ-` — passive / to become (`ve-bon-iĝ-as` — become good)
2. **Classification, Subject, and Gender:**
   * `-in-` — feminine gender (`no-hom-in` — woman, `no-kat-in` — female cat)
   * `-on-` — masculine gender (`no-hom-on` — man, `no-kat-on` — male cat)
   * `-ul-` — person characterized by trait (`no-rich-ul` — rich person)
   * `-an-` — member / inhabitant (`no-mord-an` — northerner)
   * `-ist-` — professional / specialist (`no-art-ist` — artist)
   * `-estr-` — leader / chief / responsible (`no-urb-estr` — village head, `no-gor-estr` — city mayor)
3. **Size, Location, and Fraction:**
   * `-et-` — diminutive (`no-dom-et` — cottage)
   * `-eg-` — augmentative (`no-dom-eg` — mansion / palace)
   * `-er-` — fragment / fraction / portion (`no-pan-er` — crumb, `na-dek-er` — 1/10)
   * `-ar-` — collective / set (`no-arb-ar` — forest)
   * `-eá` — place / venue (`no-lern-eá` — school)
   * `-ué-` — container / receptacle (`no-penn-ué` — pencil case)
4. **Plural:**
   * `-mó` — plural marker (`no-dom-mó` — houses)
5. **Tense and Mood:**
   * `-as` — present tense (`ve-vid-as`)
   * `-is` — past tense (`ve-vid-is`)
   * `-os` — future tense (`ve-vid-os`)
   * `-us` — conditional mood (`ve-vid-us`)
   * `-ut` — imperative mood (`ve-vid-ut`)
   * `-im` — infinitive (`ve-vid-im`)
6. **Direct Object Case (Accusative):**
   * `-om` — accusative case marker for inversion (`no-dom-om`)

### 3.4. Negation `po-ne`

The negative particle **po-ne** is placed **directly after** the negated constituent (postposition) in strict accordance with the Law of Gradient (Law 6):

* **Verb Negation (S-O-V-Neg):** `pro-mi pro-ti ve-am-as po-ne` *(I do not love you)*
* **Adverbial/Location Negation:** `pro-ti ve-viv-as | po-ci po-ne` *(You live | not here)*
* **Noun/Entity Negation:** `no-dom po-ne` *(Not a house)*

### 3.5. Antonyms via Paired Unique Roots

Nodal does not use a negative prefix like `mal-`. All opposite concepts are represented by unique paired roots:

* `bon` (good) / `dol` (bad)
* `grand` (large) / `mikr` (small)
* `leger` (light) / `pez` (heavy)
* `sinir` (left) / `dekir` (right)

---

## 4. Syntax

### 4.1. Base Word Order: SOV

Standard word order in a clause: **Subject ➔ Object ➔ Verb**.

* `no-hom` *(S)* `no-dom` *(O)* `ve-vid-as` *(V)* — The human sees the house.

### 4.2. Distance Gradient for Modifiers (Law 6)

All modifiers (adjectives, adverbs, adverbials, negative particles) are placed **after the head word**.

* **Principle:** The closer a modifier stands to the head word, the stronger its semantic accent.
  * `no-dom pa-grand-as | po-en no-foret` — The house [which?] *large* | in the forest.
  * `no-dom po-en no-foret | pa-grand-as` — The house [where?] *in the forest* | large.

### 4.3. Basic Clause Types

1. **State Clause:** `no-dom pa-grand-as` *(The house is large)*
2. **Action Clause:** `no-hom no-dom ve-vid-as` *(The human sees the house)*
3. **Identification Clause (Verbless):** `to-ci no-dom pa-mi` *(This is my house)*

### 4.4. Flexibility via Accusative `-om`

To alter word order for poetic emphasis or focus, the direct object is marked with suffix **-om**:

* `no-dom-om no-hom ve-vid-as` *(The house [specifically it!] the human sees)*

---

## 5. Interrogatives and Relatives

| Root | Interrogative (`ka-`) | Relative (`to-`) | Meaning |
| :--- | :--- | :--- | :--- |
| **ku** | `ka-ku` | `to-ku` | who / who (anim.) |
| **ĉo** | `ka-ĉo` | `to-ĉo` | what / which (inanim.) |
| **lo** | `ka-lo` | `to-lo` | where / place where |
| **tem** | `ka-tem` | `to-tem` | when / time when |
| **man** | `ka-man` | `to-man` | how / manner in which |
| **kial** | `ka-kial` | `to-kial` | why / reason for which |

---

## 6. Prepositions (`po-`)

All prepositions carry the grammatical prefix **po-**:

* `po-pog` — for (purpose / target)
* `po-en` — in / inside
* `po-sur` — on / upon surface
* `po-sub` — under / beneath
* `po-apud` — near / beside
* `po-inter` — between / among
* `po-de` — of / from / about
* `po-al` — to / towards
* `po-tra` — through / across
* `po-kun` — with (together)
* `po-sen` — without
* `po-ĝis` — until / up to
* `po-ci` — here / at this place
* `po-ne` — not (negation particle)

---

## 7. Conjunctions (`ko-`)

All conjunctions and clause linkers carry the prefix **ko-**:

* `ko-tor` — because (cause)
* `ko-sed` — but / however (contrast)
* `ko-ef` — and (conjunction)
* `ko-au` — or (disjunction)
* `ko-se` — if (condition)
* `ko-do` — therefore / so
* `ko-ke` — that (subordinating)
* `ko-por` — in order to / so that

---

## 8. Numerals (`na-`) and Mathematical Graphics

### 8.1. Base Numbers and Fractions

* **0–10:** `na-nul` (0), `na-un` (1), `na-du` (2), `na-tri` (3), `na-kvar` (4), `na-kvin` (5), `na-ses` (6), `na-sep` (7), `na-ok` (8), `na-nau` (9), `na-dek` (10), `na-du-dek`(20), `na-du-dek na-tri` (23), `na-tri-dek` (30), `na-kvar-dek` (40), `na-kvin-dek` (50), `na-ses-dek` (60), `na-sep-dek` (70), `na-ok-dek` (80), `na-nau-dek` (90).

Tens are formed as ‘na-{digit}-dek’ for 2–9.

* **Hundreds, Thousands, Millions:** `na-cent` (100), `na-ton` (1000), `na-mil` (1,000,000).
* **Fractions and Percentages (via suffix `-er-`):**
  * `na-dek-er` — 1/10 (one tenth)
  * `na-du na-tri-er` — 2/3 (two thirds)
  * `na-kvin-dek na-cent-er` — 50% (fifty hundredths)

### 8.2. Digital Graphics in Gliph Cells (3-Digit Rule)

In Gliph graphics, numbers are split into cells strictly by **3 digits in the [A]–[E] module**:

* **For whole numbers (> 1):** if the leftmost group has fewer than 3 digits, **1–2 zeros** are prepended (`1` ➔ `001`, `12` ➔ `012`).
* **For fractional tails (< 1):** if the rightmost group has fewer than 3 digits, **1–2 zeros** are appended (`,1` ➔ `,100`).

```text
| 0 0 1 | 0 0 0 | . | 1 0 0 |
```

---

## 9. Pronouns

### 9.1. Personal Pronouns (`pro-`)

* `pro-mi` (I / me)
* `pro-ti` (you [sg])
* `pro-li` (he / him)
* `pro-si` (she / her)
* `pro-ĝi` (it)
* `pro-ni` (we / us)
* `pro-vi` (you [pl])
* `pro-ili` (they / them)

### 9.2. Possessive Pronouns (`pa-`)

Formed as adjectival modifiers:

* `pa-mi` (my / mine), `pa-ti` (your / yours), `pa-li` (his), `pa-si` (her / hers), `pa-ĝi` (its), `pa-ni` (our / ours), `pa-vi` (your / yours [pl]), `pa-ili` (their / theirs).

---

## 10. Core Rules of Nodal (10 Laws)

1. **Law of Fixed Prefix:** Every content word begins with a mandatory part-of-speech prefix.
2. **Law of Wave Cell:** Every single morpheme (roots, prefixes, suffixes, conjunctions) strictly has a length of 2 to 5 letters (0% 1-letter morphemes).
3. **Law of Zero Homonymy:** 1 root = 1 unique meaning.
4. **Law of Single Stress:** Prefixes are always unstressed; stress falls on the 1st syllable of the root.
5. **Law of SOV:** Standard word order is Subject ➔ Object ➔ Verb.
6. **Law of Gradient:** All modifiers follow the head word (including postposed `po-ne`).
7. **Law of Suffix Ordering:** Suffixes attach strictly by rank (1➔2➔3➔4➔5➔6).
8. **Law of Fractional Share:** All fractions and percentages are formed using suffix `-er-`.
9. **Law of 3-Digit Module:** Numbers in Gliph cells group into 3-digit padded units.
10. **Law of Acoustic Pauses:** Syntactic boundaries are delineated by 4 pause levels `|`, `||`, `|||`, `||||`. The last is reserved for sentence termination; the other three operate inside a sentence. Punctuation marks are rendered as pauses, not as literal glyphs (Section 2.4).

---

## 11. Sentence Examples and Analysis

### Analysis of Sample Sentence

* **Text:** `pro-mi pro-ti ve-am-as po-ne|||ko-sed|pro-ti ve-viv-as po-ci||||`
* **Meaning:** "I do not love you, but you live here."
* **Acoustic Score:** `pro-MI pro-TI ve-AM-as po-ne ||| ko-SED | pro-TI ve-VIV-as po-CI ||||`

#### Structural Breakdown

* `pro-MI` — subject (I), stress on root `MI`
* `pro-TI` — direct object (you)
* `ve-AM-as` — verb in present tense (love)
* `po-ne` — negative particle following verb (not loving)
* `|||` — inter-clause pause before conjunction
* `ko-SED` — adversative conjunction (but)
* `|` — micro-pause for emphasis
* `pro-TI` — subject of second clause (you)
* `po-CI` — adverbial of place (here)
* `po-ne` — negative particle modifying location or verb
* `ve-VIV-as` — verb in present tense (live), concluding clause in SOV order
* `||||` — sentence-final pause, closes the whole utterance

---

## 12. Keyboard Input Interface

For maximum typing speed, a chordal-modular layout is designed. The keyboard layout follows the principle "no Shift = voiceless, Shift = voiced" for paired consonants. Iotated vowels are typed with Shift on the corresponding simple vowel keys.

### 12.1. Layout Without Shift

```text
l a s e t o k i r u , +
p f ĉ n š č c m h . ?
po to pro ve no pa ko na ka -
```

### 12.2. Layout With Shift

```text
· á z é d ó g í · ú ; *
b v ĝ · ž ǆ · · · : !
· · · · · · · · · _
```

### 12.3. Input Rules

* **Macro-row of Prefixes (Bottom Row):** The nine grammatical prefixes — `po`, `to`, `pro`, `ve`, `no`, `pa`, `ko`, `na`, `ka` — are typed in 1 click on the bottom row.
* **Paired Consonants (Shift):** Voiceless sounds are typed normally; voiced pairs via Shift:
  * `t` / `Shift+T` = `d`
  * `p` / `Shift+P` = `b`
  * `s` / `Shift+S` = `z`
  * `f` / `Shift+F` = `v`
  * `k` / `Shift+K` = `g`
  * `š` / `Shift+Š` = `ž`
  * `č` / `Shift+Č` = `ǆ` (single glyph)
  * `ĉ` / `Shift+Ĉ` = `ĝ`
* **Iotated Vowels (Shift on Vowels):** Dedicated keys `á`, `é`, `í`, `ó`, `ú` generate the iotated hook `◜` and produce `ja`, `je`, `ji`, `jo`, `ju`.
* Letter `h` is typed without Shift; `x` is not a letter of the alphabet.
* Punctuation and Symbols occupy the upper and right-hand rows as shown in the layout tables above.

