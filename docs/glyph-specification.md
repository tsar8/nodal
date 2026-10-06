# Specification Version 1.4 

**Specification Version:** 1.4  
**Status:** Graphics specification for the Gliph writing system.
**Purpose:** Description of graphic atoms, slot-based modular cells, spatial composition rules, digital module integration, font engine specifications (FontForge), and machine processing formats (JSON).  
**Update Date:** 2026-10-04  

---

## 1. General Principles

The **Gliph** graphic system is a minimalist, geometrically rigorous writing system specifically designed for the **Nodal** language. Unlike the linear script of natural languages, Gliph utilizes slot-based **5-position modular cells ([A]–[E])**, combining letters of a single morpheme (up to 5 characters) into a unified visual block.

### 1.1. Modular Cell [A]–[E]

Every single Nodal morpheme without exception (root, prefix, suffix, conjunction) strictly contains between **2 and 5 letters** (0% 1-letter morphemes) and fits into a fixed 5-position structure:

```text
[A] (Top Left) ─────►         [E] (Top Right)
      │                             ▲
      ▼                             │
[B] (Bottom Left) ──► [C] ──► [D] (Bottom Right)
                    (Center)
```

The cell is a positional container. Letters are placed into predefined slots; no connecting stroke between letters is required or mandatory. The cell may be rendered with or without a visible frame.

### 1.2. Reading Order

Elements inside a modular cell are read in a strict slot order:

1. **Position [A]** — Top Left corner *(Start)*
2. **Position [B]** — Bottom Left corner
3. **Position [C]** — Center Bottom element
4. **Position [D]** — Bottom Right corner
5. **Position [E]** — Top Right corner *(Finish)*

The reading order is a property of the slot index, not of a visual path. The reader (human or machine) reads slot [A] first, then [B], then [C], then [D], then [E], skipping empty slots.

### 1.3. Morpheme Boundaries and Spacing

* **Inside a morpheme:** letters occupy slots [A]–[E] according to the slot matrix (Section 4.1). No hyphen is written inside the cell.
* **Between morphemes inside a word:** morpheme boundaries are expressed by an **inter-modular micro-gap** (spatial pause). In linear input, the hyphen `-` is used as the morpheme separator; it is rendered as a micro-gap.
* **Between words:** standard spaces are used.

### 1.4. Optional Decorative Layer

A wave thread (a continuous stroke linking letters inside a cell) may be offered as an optional decorative feature in select fonts or renderers. It carries no grammatical, phonetic, or semantic information. Its presence or absence must not affect parsing, machine reading, or the canonical JSON representation.

**Rule:** if a conflict arises between a decorative rendering and the slot-based specification, the slot-based specification always wins.

### 1.5. Single-Character Notation

For consistency between input, JSON, and glyph rendering, the following single-character notations are canonical:

| Form | Replaces digraph | Unicode |
| :--- | :--- | :--- |
| **á** | ja | U+00E1 |
| **é** | je | U+00E9 |
| **í** | ji | U+00ED |
| **ó** | jo | U+00F3 |
| **ú** | ju | U+00FA |
| **ǆ** | dž | U+01C6 |

All tables, JSON keys, and OpenType classes must use these single characters. The digraph notation (ja, je, dž) is descriptive only and is not part of the input format; the letter j does not exist in Nodal. Input must already contain the single-character forms (á, é, ǆ). The ccmp feature is therefore not used for digraph normalization. The mandatory text preprocessing is described in Section 6.0.

---

## 2. Atoms (Base Graphic Elements)

Gliph graphics are built entirely from **11 fundamental geometric atoms**, forming all 32 letters of the alphabet. Every letter is assembled by combining these atoms according to strict positional rules.

| Atom | Unicode / Symbol | Name | Function and Application |
| :--- | :--- | :--- | :--- |
| **Atom-1** | ○ (U+25CB) | Circle | Base form for simple vowel `a` and structural frame |
| **Atom-2** | • (U+2022) | Dot | Nasal/labial marker; vocalic node for vowel `i` |
| **Atom-3** | │ (U+2502) | Vertical Bar | Base for sonorants (`l`, `n`, `r`); structural frame |
| **Atom-4** | ─ (U+2500) | Horizontal Bar | Main bar for alveolar plosives (`t`, `d`) |
| **Atom-5** | ⊓ (U+2293) | Square Cap | Base frame for labial, velar, and palatal consonants |
| **Atom-6** | ◜ (U+25DC) | Iotation Horn | Iotation marker (`á`, `é`, `í`, `ó`, `ú`); affricate/trill marker |
| **Atom-7** | ╱ (U+2571) | Forward Slash | Base for alveolar fricatives (`s`, `z`, `f`, `v`, `c`) |
| **Atom-8** | ╲ (U+2572) | Backslash | Base for postalveolar sibilants (`š`, `ž`, `č`, `ǆ`) |
| **Atom-9** | ╳ (U+2573) | Cross | Base for velar fricative (`h`) |
| **Atom-10** | ◠ (U+25E0) | Upper Half Circle | Base form for vowel `e` |
| **Atom-11** | ⎸ (U+23B8) | Voicing Marker | Right/left voicing indicator |

### Voicing Marker (⎸)

For all paired consonants, voiceless and voiced forms use identical base frames. Voicing is conveyed by the **position of the thin vertical stroke ⎸** relative to the base:

* **Voiceless sound:** the stroke ⎸ is located on the **right** side of the base (`t` = ─⎸, `p` = ⊓⎸, `k` = ⊓⎸╱).
* **Voiced sound:** the stroke ⎸ shifts to the **left** side of the base (`d` = ⎸─, `b` = ⎸⊓, `g` = ⎸⊓╱).

### Diacritic Rules

* **• (Dot)** — marks labial or nasal articulation (`m` = ⊓•, `n` = │•, `f` = ╱⎸•, `v` = ⎸╱•).
* **◜ (Iotation Horn)** — marks affrication or trill (`r` = │◜, `c` = ╱⎸◜, `č` = ╲⎸◜, `ǆ` = ⎸╲◜, `ĉ` = ⊓⎸◜, `ĝ` = ⎸⊓◜).

The stroke ⎸ appears in all consonants except the sonorants l, n, r, m. In paired consonants it marks voicing: right position = voiceless, left position = voiced. In the unpaired consonants c and h, ⎸ is a structural component retained from their original paired forms; it does not mark a voicing distinction because no voiced counterpart exists in the modern alphabet.

---

## 3. Complete "Letter → Glyph" Table (32 Letters)

The Gliph alphabet comprises **10 vowels** (5 simple + 5 iotated) and **22 consonants** (8 voiced/voiceless pairs + 6 unpaired sounds).

### 3.1. Vowels (10)

| Letter | Sound (IPA) | Gliph Glyph | Atomic Composition | Key | Graphic Structure Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **a** | [a] | ○ | Atom-1 | `a` | Base circle |
| **e** | [e] | ◠ | Atom-10 | `e` | Upper half circle |
| **i** | [i] | ⊙ | Atom-1 + Atom-2 | `i` | Circle with centered dot |
| **o** | [o] | ⦶ | Atom-1 + Atom-3 | `o` | Circle with inner vertical bar |
| **u** | [u] | ⊖ | Atom-1 + Atom-4 | `u` | Circle with inner horizontal bar |
| **á** | [ja] | ◜○ | Atom-6 + Atom-1 | `á` / `Shift+A` | Iotation horn + circle |
| **é** | [je] | ◜◠ | Atom-6 + Atom-10 | `é` / `Shift+E` | Iotation horn + upper half circle |
| **í** | [ji] | ◜⊙ | Atom-6 + Atom-1 + Atom-2 | `í` / `Shift+I`| Iotation horn + circle with dot |
| **ó** | [jo] | ◜⦶ | Atom-6 + Atom-1 + Atom-3 | `ó` / `Shift+O`| Iotation horn + circle with inner vertical |
| **ú** | [ju] | ◜⊖ | Atom-6 + Atom-1 + Atom-4 | `ú` / `Shift+U`| Iotation horn + circle with inner horizontal |

### 3.2. Paired Consonants (16 sounds / 8 pairs)

| Class | Voiceless | Voiced | Voiceless Glyph | Voiced Glyph | Base Atom | Key | Graphic Distinction Description |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **C1** (─) | **t** | **d** | ─⎸ | ⎸─ | Atom-4 (─) | `t` / `Shift+T` | Right stroke (`t`) vs Left stroke (`d`) |
| **C3** (╱) | **s** | **z** | ╱⎸ | ⎸╱ | Atom-7 (╱) | `s` / `Shift+S` | Right stroke (`s`) vs Left stroke (`z`) |
| **C3** (╱) | **f** | **v** | ╱⎸• | ⎸╱• | Atom-7 + Atom-2 | `f` / `Shift+F` | Forward slash with dot, stroke right / left |
| **C4** (╲) | **š** | **ž** | ╲⎸ | ⎸╲ | Atom-8 (╲) | `š` / `Shift+Š` | Backslash with right stroke / left stroke |
| **C4** (╲) | **č** | **ǆ** | ╲⎸◜ | ⎸╲◜ | Atom-8 + Atom-6 | `č` / `Shift+Č` | Backslash with horn, stroke right / left |
| **C5** (⊓) | **p** | **b** | ⊓⎸ | ⎸⊓ | Atom-5 (⊓) | `p` / `Shift+P` | Cap with right stroke (`p`) vs left stroke (`b`) |
| **C5** (⊓) | **k** | **g** | ⊓⎸╱ | ⎸⊓╱ | Atom-5 + Atom-7 | `k` / `Shift+K` | Cap with half-slash, stroke right / left |
| **C5** (⊓) | **ĉ** | **ĝ** | ⊓⎸◜ | ⎸⊓◜ | Atom-5 + Atom-6 | `ĉ` / `Shift+Ĉ` | Cap with horn, stroke right / left |

### 3.3. Unpaired Consonants (6)

| Letter | Sound (IPA) | Gliph Glyph | Atomic Composition | Key | Graphic Structure Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **l** | [l] | │ | Atom-3 | `l` | Lateral vertical bar |
| **n** | [n] | │• | Atom-3 + Atom-2 | `n` | Vertical bar with dot (nasal) |
| **r** | [r] | │◜ | Atom-3 + Atom-6 | `r` | Vertical bar with horn (trill) |
| **m** | [m] | ⊓• | Atom-5 + Atom-2 | `m` | Square cap with dot (labial nasal) |
| **c** | [ts] | ╱⎸◜ | Atom-7 + Atom-6 | `c` | Forward slash with stroke and horn (affricate) |
| **h** | [x] | ╳⎸ | Atom-9 | `h` | Cross with right stroke (velar fricative) |

---

## 4. Slot Distribution Rules

Depending on morpheme length (2 to 5 letters), characters occupy strictly defined slots in the cell [A]–[E]. Entry is always at [A]; exit is always at [E].

### 4.1. Slot Filling Matrix

| Letter Count | Position A | Position B | Position C | Position D | Position E |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **2 letters** | Letter 1 | — | — | — | Letter 2 |
| **3 letters** | Letter 1 | — | Letter 2 | — | Letter 3 |
| **4 letters** | Letter 1 | Letter 2 | — | Letter 3 | Letter 4 |
| **5 letters** | Letter 1 | Letter 2 | Letter 3 | Letter 4 | Letter 5 |

**Notes:**
* Empty slots are not rendered.
* The slot index is determined solely by the position of the letter inside the morpheme, not by its visual shape.
* No letter may occupy more than one slot; no slot may contain more than one letter.

### 4.2. Digital Graphics (3-Digit Cell Rule)

Numbers utilize the same 5-position modular cells [A]–[E], but only positions [A], [C], and [E] are used — one digit per position.

* **Grouping:** Numbers are written in blocks of strictly **3 digits per cell**.
* **Padding Rule:**
  * **Whole Part (Numbers > 1):** if the leftmost group has fewer than 3 digits, **1–2 zeros** are prepended (`1` ➔ `001`, `12` ➔ `012`).
  * **Fractional Part (Numbers < 1):** if the rightmost group has fewer than 3 digits, **1–2 zeros** are appended (`.1` ➔ `.100`).

#### Example: Writing 1000.1

1. **Split:** `1000` = `1` + `000`. Fractional tail = `.1`.
2. **Apply padding:** `1` ➔ **001**, `000` ➔ **000**, `.1` ➔ **.100**.
3. **Result:** `| 0 0 1 | 0 0 0 | . | 1 0 0 |`

Each 3-digit group occupies one cell: digit 1 → [A], digit 2 → [C], digit 3 → [E]. 

---

## 5. Slot-Based Rendering Examples (SVG)

Below are vector SVG diagrams demonstrating the slot-based rendering of morpheme modules. No wave thread is required. Letters are placed into slots [A]–[E] according to the slot matrix (Section 4.1).

### 5.1. Morpheme `hom` (3 letters: h [A] ➔ o [C] ➔ m [E])

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="180">
  <rect width="100%" height="100%" fill="#1a1c23" rx="10"/>
  <!-- Cell container -->
  <rect x="40" y="30" width="220" height="120" rx="15" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4 4"/>
  <!-- Slot [A] - h -->
  <circle cx="70" cy="65" r="14" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="70" y="70" fill="#f87171" font-family="monospace" font-size="14" text-anchor="middle">h</text>
  <text x="70" y="95" fill="#f87171" font-family="monospace" font-size="9" text-anchor="middle">[A]</text>
  <!-- Slot [C] - o -->
  <circle cx="150" cy="115" r="14" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="150" y="120" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">o</text>
  <text x="150" y="145" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[C]</text>
  <!-- Slot [E] - m -->
  <circle cx="230" cy="65" r="14" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="230" y="70" fill="#4ade80" font-family="monospace" font-size="14" text-anchor="middle">m</text>
  <text x="230" y="95" fill="#4ade80" font-family="monospace" font-size="9" text-anchor="middle">[E]</text>
  <!-- Title -->
  <text x="150" y="22" fill="#ffffff" font-family="sans-serif" font-weight="bold" font-size="14" text-anchor="middle">Module "hom" (3 letters: A → C → E)</text>
  <!-- Legend -->
  <text x="150" y="168" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">Slots [B] and [D] are empty and not rendered.</text>
</svg>
```

### 5.2. Two morphemes `am` + `as` (micro-gap between cells)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 180" width="100%" height="180">
  <rect width="100%" height="100%" fill="#1a1c23" rx="10"/>
  <!-- Cell 1: am -->
  <rect x="30" y="30" width="160" height="120" rx="12" fill="none" stroke="#3b82f6" stroke-width="2"/>
  <text x="110" y="22" fill="#93c5fd" font-family="sans-serif" font-weight="bold" font-size="12" text-anchor="middle">Morpheme "am"</text>
  <circle cx="60" cy="65" r="14" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="60" y="70" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">a</text>
  <text x="60" y="95" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[A]</text>
  <circle cx="160" cy="65" r="14" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="160" y="70" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">m</text>
  <text x="160" y="95" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[E]</text>
  <!-- Micro-gap -->
  <line x1="200" y1="40" x2="200" y2="140" stroke="#475569" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="200" y="158" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">micro-gap</text>
  <!-- Cell 2: as -->
  <rect x="210" y="30" width="180" height="120" rx="12" fill="none" stroke="#a855f7" stroke-width="2"/>
  <text x="300" y="22" fill="#c084fc" font-family="sans-serif" font-weight="bold" font-size="12" text-anchor="middle">Morpheme "as"</text>
  <circle cx="240" cy="65" r="14" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="240" y="70" fill="#c084fc" font-family="monospace" font-size="14" text-anchor="middle">a</text>
  <text x="240" y="95" fill="#c084fc" font-family="monospace" font-size="9" text-anchor="middle">[A]</text>
  <circle cx="360" cy="65" r="14" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="360" y="70" fill="#c084fc" font-family="monospace" font-size="14" text-anchor="middle">s</text>
  <text x="360" y="95" fill="#c084fc" font-family="monospace" font-size="9" text-anchor="middle">[E]</text>
  <text x="210" y="172" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">No hyphen is drawn between cells — only the micro-gap.</text>
</svg>
```
*Note: The dashed vertical line and the label `micro-gap` in the diagram above are annotations for this document only. In actual Gliph rendering the boundary between two morpheme cells is empty whitespace — no visible stroke, line, or glyph is drawn. The micro-gap is a spatial pause, not a graphic element.*

### 5.3. Five-letter morpheme `grand` (5 letters: A → B → C → D → E)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" width="100%" height="200">
  <rect width="100%" height="100%" fill="#1a1c23" rx="10"/>
  <rect x="40" y="35" width="240" height="140" rx="15" fill="none" stroke="#3b82f6" stroke-width="2" stroke-dasharray="4 4"/>
  <circle cx="70" cy="65" r="13" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="70" y="70" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">g</text>
  <text x="70" y="90" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[A]</text>
  <circle cx="70" cy="150" r="13" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="70" y="155" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">r</text>
  <text x="70" y="175" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[B]</text>
  <circle cx="160" cy="150" r="13" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="160" y="155" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">a</text>
  <text x="160" y="175" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[C]</text>
  <circle cx="250" cy="150" r="13" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="250" y="155" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">n</text>
  <text x="250" y="175" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[D]</text>
  <circle cx="250" cy="65" r="13" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="250" y="70" fill="#60a5fa" font-family="monospace" font-size="14" text-anchor="middle">d</text>
  <text x="250" y="90" fill="#60a5fa" font-family="monospace" font-size="9" text-anchor="middle">[E]</text>
  <text x="160" y="22" fill="#ffffff" font-family="sans-serif" font-weight="bold" font-size="14" text-anchor="middle">Module "grand" (5 letters: A → B → C → D → E)</text>
</svg>
```

### 5.4. Number cell example: `001` (as in 1000.1)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 180" width="100%" height="180">
  <rect width="100%" height="100%" fill="#1a1c23" rx="10"/>
  <rect x="30" y="30" width="200" height="120" rx="15" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 4"/>
  <circle cx="60" cy="65" r="14" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="60" y="71" fill="#fbbf24" font-family="monospace" font-size="16" text-anchor="middle">0</text>
  <text x="60" y="95" fill="#fbbf24" font-family="monospace" font-size="9" text-anchor="middle">[A]</text>
  <circle cx="130" cy="115" r="14" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="130" y="121" fill="#fbbf24" font-family="monospace" font-size="16" text-anchor="middle">0</text>
  <text x="130" y="145" fill="#fbbf24" font-family="monospace" font-size="9" text-anchor="middle">[C]</text>
  <circle cx="200" cy="65" r="14" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="200" y="71" fill="#fbbf24" font-family="monospace" font-size="16" text-anchor="middle">1</text>
  <text x="200" y="95" fill="#fbbf24" font-family="monospace" font-size="9" text-anchor="middle">[E]</text>
  <text x="130" y="22" fill="#ffffff" font-family="sans-serif" font-weight="bold" font-size="14" text-anchor="middle">Number cell "001" (A → C → E)</text>
  <text x="130" y="168" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">Only slots A, C, E are used for digits.</text>
</svg>
```

### 5.5. Optional decorative wave (disabled by default)

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 180" width="100%" height="180">
  <rect width="100%" height="100%" fill="#1a1c23" rx="10"/>
  <rect x="40" y="30" width="220" height="120" rx="15" fill="none" stroke="#475569" stroke-width="2"/>
  <path d="M 70 65 L 150 115 L 230 65" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.35"/>
  <text x="150" y="70" fill="#94a3b8" font-family="monospace" font-size="14" text-anchor="middle">h · o · m</text>
  <text x="150" y="22" fill="#ffffff" font-family="sans-serif" font-weight="bold" font-size="13" text-anchor="middle">Optional decorative wave (disabled by default)</text>
  <text x="150" y="168" fill="#64748b" font-family="sans-serif" font-size="10" text-anchor="middle">Carries no grammatical or phonetic information.</text>
</svg>
```

---

## 6. Font Specification (FontForge & OpenType)

### 6.0. Input Preprocessor (Mandatory)

The canonical OpenType `.fea` rules use `@DELIM` (hyphen or space) as the left and right boundary of every morpheme. Since the start and end of a text stream are not delimiters by themselves, a mandatory preprocessing step is required before the text reaches the shaper.

The preprocessor performs three operations:
1. Insert a space after every punctuation mark (`.`, `,`, `!`, `?`, `;`, `:`) if the next character is not already a space. A `.` or `,` placed between two digits is treated as a decimal separator and is left untouched.
2. Strip each line and wrap it with a single leading and trailing space.
3. *(Mandatory)* Validate morpheme lengths. Every sequence of letters between two delimiters must be 2–5 characters long. A length of 1 or ≥6 is a canonical error and must be reported.

#### Reference Implementation (Python)

```python
import re

# All 32 Nodal letters (must be kept in sync with the alphabet)
LETTERS = set("aeiouáéíóútdpbszkgfvšžčǆĉĝlnrmch")
PUNCT       = set(".!?;:")
SOFT_PUNCT  = set(",.")   # may be decimal separators

def add_space_after_punct(text: str) -> str:
    out = []
    for i, ch in enumerate(text):
        out.append(ch)
        if ch in PUNCT or ch in SOFT_PUNCT:
            if i + 1 >= len(text):
                continue
            nxt = text[i + 1]
            if nxt.isspace():
                continue
            # decimal separator: do not insert space between digits
            if ch in SOFT_PUNCT and i > 0 and text[i - 1].isdigit() and nxt.isdigit():
                continue
            out.append(" ")
    return "".join(out)

def validate_morphemes(text: str) -> list[str]:
    """Return a list of error messages (empty if all morphemes are 2-5 letters)."""
    errors = []
    # Split on whitespace and punctuation EXCEPT hyphen (morpheme separator)
    for token in re.split(r"[\s.,!?;:]+", text.strip()):
        if not token:
            continue
        # Skip pure-digit tokens (numbers are handled separately)
        if re.fullmatch(r"[\d,\.]+", token):
            continue
        for morpheme in token.split("-"):
            if not morpheme:
                continue
            # Reject non-letter characters inside a morpheme
            if not all(ch in LETTERS for ch in morpheme):
                bad = "".join(ch for ch in morpheme if ch not in LETTERS)
                errors.append(
                    f"morpheme '{morpheme}' contains non-letter characters: {bad!r}"
                )
                continue
            if not (2 <= len(morpheme) <= 5):
                errors.append(
                    f"morpheme '{morpheme}' has invalid length {len(morpheme)}"
                )
    return errors

def preprocess(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = add_space_after_punct(text)
    lines = [ln.strip() for ln in text.split("\n")]
    lines = [" " + ln + " " for ln in lines]
    return "\n".join(lines)
```

**Rule:** No text may be passed to the Gliph shaper without preprocessing. Renderers that skip the preprocessor will silently fail to position the first and last morpheme of a line.

### 6.1. OpenType Feature Definitions (`Gliph.fea`)

The reference font uses no mandatory wave thread. The `.fea` file defines positional variants and a length-based contextual substitution.

```fea
languagesystem latn dflt;

# 1. Alphabet: all 32 letters as single characters.
# Order MUST match each @POS_X class below, position by position.
@L = [a e i o u á é í ó ú t d p b s z k g f v š ž č ǆ ĉ ĝ l n r m c h];

# Delimiters: hyphen = morpheme boundary, space = word boundary.
@DELIM = [hyphen space];

# 2. Positional variant classes.
@POS_A = [a.A e.A i.A o.A u.A á.A é.A í.A ó.A ú.A t.A d.A p.A b.A s.A z.A k.A g.A f.A v.A š.A ž.A č.A ǆ.A ĉ.A ĝ.A l.A n.A r.A m.A c.A h.A];
@POS_B = [a.B e.B i.B o.B u.B á.B é.B í.B ó.B ú.B t.B d.B p.B b.B s.B z.B k.B g.B f.B v.B š.B ž.B č.B ǆ.B ĉ.B ĝ.B l.B n.B r.B m.B c.B h.B];
@POS_C = [a.C e.C i.C o.C u.C á.C é.C í.C ó.C ú.C t.C d.C p.C b.C s.C z.C k.C g.C f.C v.C š.C ž.C č.C ǆ.C ĉ.C ĝ.C l.C n.C r.C m.C c.C h.C];
@POS_D = [a.D e.D i.D o.D u.D á.D é.D í.D ó.D ú.D t.D d.D p.D b.D s.D z.D k.D g.D f.D v.D š.D ž.D č.D ǆ.D ĉ.D ĝ.D l.D n.D r.D m.D c.D h.D];
@POS_E = [a.E e.E i.E o.E u.E á.E é.E í.E ó.E ú.E t.E d.E p.E b.E s.E z.E k.E g.E f.E v.E š.E ž.E č.E ǆ.E ĉ.E ĝ.E l.E n.E r.E m.E c.E h.E];


# ccmp is not used: the letter 'j' does not exist in Nodal,
# and input must already contain single-character forms (á, é, ǆ).

# 3. Numbers: 3-digit cells use slots A, C, E.
@DIGIT = [zero one two three four five six seven eight nine];
@DIG_A = [zero.A one.A two.A three.A four.A five.A six.A seven.A eight.A nine.A];
@DIG_C = [zero.C one.C two.C three.C four.C five.C six.C seven.C eight.C nine.C];
@DIG_E = [zero.E one.E two.E three.E four.E five.E six.E seven.E eight.E nine.E];

feature calt {
    # 2-letter morphemes: A -> E
    lookup Pos2 {
        sub @DELIM @L' @L' @DELIM by @POS_A @POS_E;
    } Pos2;

    # 3-letter morphemes: A -> C -> E
    lookup Pos3 {
        sub @DELIM @L' @L' @L' @DELIM by @POS_A @POS_C @POS_E;
    } Pos3;

    # 4-letter morphemes: A -> B -> D -> E
    lookup Pos4 {
        sub @DELIM @L' @L' @L' @L' @DELIM by @POS_A @POS_B @POS_D @POS_E;
    } Pos4;

    # 5-letter morphemes: A -> B -> C -> D -> E
    lookup Pos5 {
        sub @DELIM @L' @L' @L' @L' @L' @DELIM by @POS_A @POS_B @POS_C @POS_D @POS_E;
    } Pos5;

    # Render the hyphen as a micro-gap
    lookup DelimToGap {
        sub hyphen by micro_gap;
    } DelimToGap;

    sub @DELIM @DIGIT' @DIGIT' @DIGIT' @DELIM by @DIG_A @DIG_C @DIG_E;
} calt;
```

### 6.2. Font Metrics (FontForge Metrics)

* **EM Square:** 1000 units
* **Ascender:** 800 units (Positions [A] and [E])
* **Descender:** -200 units (Positions [B], [C], [D])
* **Modular Cell Width:** 600 units
* **Inter-Modular Gap (Letter spacing):** 150 units
* **Positional variant count:** 32 letters × 5 slots = 160 glyphs, plus 10 digits × 3 slots = 30 digit variants, plus delimiters.

### 6.3. Fallback Rendering

If a font lacks positional variants (e.g., a system fallback font), the linear form is rendered as plain text: `no-hom`, `ve-vid-as`, etc. The canonical JSON representation remains unchanged.

---

## 7. Machine-Readable JSON Description

```json
{
  "system": "Gliph",
  "version": "1.4",
  "cell_structure": {
    "max_symbols": 5,
    "positions": ["A", "B", "C", "D", "E"],
    "slot_matrix": {
      "2_letters": ["A", "E"],
      "3_letters": ["A", "C", "E"],
      "4_letters": ["A", "B", "D", "E"],
      "5_letters": ["A", "B", "C", "D", "E"]
    }
  },
  "atoms": {
    "circle": {"unicode": "U+25CB", "symbol": "○"},
    "dot": {"unicode": "U+2022", "symbol": "•"},
    "vertical_bar": {"unicode": "U+2502", "symbol": "│"},
    "horizontal_bar": {"unicode": "U+2500", "symbol": "─"},
    "square_cap": {"unicode": "U+2293", "symbol": "⊓"},
    "iotation_horn": {"unicode": "U+25DC", "symbol": "◜"},
    "forward_slash": {"unicode": "U+2571", "symbol": "╱"},
    "backslash": {"unicode": "U+2572", "symbol": "╲"},
    "cross": {"unicode": "U+2573", "symbol": "╳"},
    "upper_arc": {"unicode": "U+25E0", "symbol": "◠"},
    "voicing_marker": {"unicode": "U+23B8", "symbol": "⎸"}
  },
  "alphabet": [
    {"letter": "a", "type": "vowel", "glyph": "○", "key": "a", "atoms": ["circle"]},
    {"letter": "e", "type": "vowel", "glyph": "◠", "key": "e", "atoms": ["upper_arc"]},
    {"letter": "i", "type": "vowel", "glyph": "⊙", "key": "i", "atoms": ["circle", "dot"]},
    {"letter": "o", "type": "vowel", "glyph": "⦶", "key": "o", "atoms": ["circle", "vertical_bar"]},
    {"letter": "u", "type": "vowel", "glyph": "⊖", "key": "u", "atoms": ["circle", "horizontal_bar"]},
    {"letter": "á", "type": "iotated_vowel", "glyph": "◜○", "key": "Shift+A", "atoms": ["iotation_horn", "circle"]},
    {"letter": "é", "type": "iotated_vowel", "glyph": "◜◠", "key": "Shift+E", "atoms": ["iotation_horn", "upper_arc"]},
    {"letter": "í", "type": "iotated_vowel", "glyph": "◜⊙", "key": "Shift+I", "atoms": ["iotation_horn", "circle", "dot"]},
    {"letter": "ó", "type": "iotated_vowel", "glyph": "◜⦶", "key": "Shift+O", "atoms": ["iotation_horn", "circle", "vertical_bar"]},
    {"letter": "ú", "type": "iotated_vowel", "glyph": "◜⊖", "key": "Shift+U", "atoms": ["iotation_horn", "circle", "horizontal_bar"]},
    {"letter": "t", "type": "voiceless_consonant", "pair": "d", "glyph": "─⎸", "key": "t", "class": "C1", "voicing": "right"},
    {"letter": "d", "type": "voiced_consonant", "pair": "t", "glyph": "⎸─", "key": "Shift+T", "class": "C1", "voicing": "left"},
    {"letter": "s", "type": "voiceless_consonant", "pair": "z", "glyph": "╱⎸", "key": "s", "class": "C3", "voicing": "right"},
    {"letter": "z", "type": "voiced_consonant", "pair": "s", "glyph": "⎸╱", "key": "Shift+S", "class": "C3", "voicing": "left"},
    {"letter": "f", "type": "voiceless_consonant", "pair": "v", "glyph": "╱⎸•", "key": "f", "class": "C3", "voicing": "right"},
    {"letter": "v", "type": "voiced_consonant", "pair": "f", "glyph": "⎸╱•", "key": "Shift+F", "class": "C3", "voicing": "left"},
    {"letter": "š", "type": "voiceless_consonant", "pair": "ž", "glyph": "╲⎸", "key": "š", "class": "C4", "voicing": "right"},
    {"letter": "ž", "type": "voiced_consonant", "pair": "š", "glyph": "⎸╲", "key": "Shift+Š", "class": "C4", "voicing": "left"},
    {"letter": "č", "type": "voiceless_consonant", "pair": "ǆ", "glyph": "╲⎸◜", "key": "č", "class": "C4", "voicing": "right"},
    {"letter": "ǆ", "type": "voiced_consonant", "pair": "č", "glyph": "⎸╲◜", "key": "Shift+Č", "class": "C4", "voicing": "left"},
    {"letter": "p", "type": "voiceless_consonant", "pair": "b", "glyph": "⊓⎸", "key": "p", "class": "C5", "voicing": "right"},
    {"letter": "b", "type": "voiced_consonant", "pair": "p", "glyph": "⎸⊓", "key": "Shift+P", "class": "C5", "voicing": "left"},
    {"letter": "k", "type": "voiceless_consonant", "pair": "g", "glyph": "⊓⎸╱", "key": "k", "class": "C5", "voicing": "right"},
    {"letter": "g", "type": "voiced_consonant", "pair": "k", "glyph": "⎸⊓╱", "key": "Shift+K", "class": "C5", "voicing": "left"},
    {"letter": "ĉ", "type": "voiceless_consonant", "pair": "ĝ", "glyph": "⊓⎸◜", "key": "ĉ", "class": "C5", "voicing": "right"},
    {"letter": "ĝ", "type": "voiced_consonant", "pair": "ĉ", "glyph": "⎸⊓◜", "key": "Shift+Ĉ", "class": "C5", "voicing": "left"},
    {"letter": "l", "type": "unpaired_consonant", "glyph": "│", "key": "l", "class": "C2"},
    {"letter": "n", "type": "unpaired_consonant", "glyph": "│•", "key": "n", "class": "C2"},
    {"letter": "r", "type": "unpaired_consonant", "glyph": "│◜", "key": "r", "class": "C2"},
    {"letter": "m", "type": "unpaired_consonant", "glyph": "⊓•", "key": "m", "class": "C5"},
    {"letter": "c", "type": "unpaired_consonant", "glyph": "╱⎸◜", "key": "c", "class": "C3"},
    {"letter": "h", "type": "unpaired_consonant", "glyph": "╳⎸", "key": "h", "class": "C6"}
  ],
  "number_padding_rules": {
    "integer_part": "pad_left_with_zeros_to_3",
    "fractional_part": "pad_right_with_zeros_to_3",
    "example_1000_1": {
      "raw": "1000.1",
      "modules": ["001", "000", ".", "100"]
    }
  },
  "input_normalization": {
    "boundary_markers": {
      "start_of_line": "space",
      "end_of_line": "space",
      "after_punctuation": [".", ",", "!", "?", ";", ":"],
      "decimal_separator_exception": true
    }
  },
  "rendering": {
    "wave_thread": "optional_decorative",
    "cell_frame": "canonical_visual_container",
    "micro_gap_replaces_hyphen": true,
    "empty_slots_rendered": false
  }
}
```
