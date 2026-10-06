# Nodal Vocabulary Specification

**Vocabulary Version:** 1.4
**Update Date:** 2026-10-03  

---

## 1. Morphological Architecture and Lexical System

### 1.1. General Information

The vocabulary of the **Nodal** language is documented in two forms: human-readable tables in this document, and a machine-readable JSON registry in the appendix. The JSON form is provided because the constraints of Nodal (2–5 letter morphemes, zero homonymy, fixed prefix set) make an automated check straightforward — not because the language is intended for machine use.

#### Key Principles of the Lexical System:

1. **100% Strict Morpheme Length (2–5 letters):** ALL morphemes (roots, prefixes, suffixes, conjunctions) are strictly constrained to **2 to 5 letters**. There are ZERO 1-letter morphemes in Nodal, ensuring 100% uniform integration into the 5-position modular cell [A]–[E] of Gliph.
2. **0% Homonymy:** Every root corresponds to exactly one unique meaning. There are zero homonyms or grammatical exceptions.
3. **Paired Antonyms:** The language avoids artificial negative prefixes like `mal-`. Antonyms are expressed via independent unique roots (`bon` — good / `dol` — bad).
4. **Mandatory Marker System:** Every content word begins with a grammatical prefix defining its part of speech.
5. **Compositionality:** Complex concepts and numbers are formed strictly by sequential attachment of morphemes.

#### Conventions:

* `[root]` — word root (2–5 letters)
* `[pref]` — part-of-speech grammatical prefix (`no-`, `ve-`, `pa-`, `po-`, `ka-`, `ko-`, `na-`, `to-`, `pro-`)
* `[affix]` — derivational prefix or grammatical suffix
* `(M)` — machine-processing variant in JSON blocks

---

### 1.2. Part-of-Speech Prefixes

Mandatory unstressed initial morphemes that determine the word's grammatical class:

| Prefix | Part of Speech / Function | Example Word | Meaning of Example |
| :--- | :--- | :--- | :--- |
| **no-** | Noun (Entity / Object) | `no-dom` | house |
| **ve-** | Verb (Action / State) | `ve-vid` | see / to see |
| **pa-** | Adjective / Quality | `pa-grand` | large / big |
| **po-** | Adverb / Circumstance / Preposition | `po-pog` | for (purpose preposition) |
| **ka-** | Interrogative word | `ka-ku` | who? |
| **ko-** | Conjunction (Clause linker) | `ko-tor` | because |
| **na-** | Numeral | `na-tri` | three |
| **to-** | Relative / Demonstrative word | `to-ku` | which / who |
| **pro-** | Pronoun (Personal / Demonstrative) | `pro-mi` | I / me |

---

### 1.3. Derivational Prefixes

Optional prefixes that modify root meaning (placed between the part-of-speech prefix and the root):

| Prefix | Meaning | Example with Prefix | Translation |
| :--- | :--- | :--- | :--- |
| **dis-** | Separation / Disassembly | `ve-dis-lig` | untie / disconnect |
| **ek-** | Inchoative / Instantaneous action | `ve-ek-ir` | set off / start going |
| **for-** | Removal / Departure away | `ve-for-ir` | go away / depart |
| **ge-** | Joint gender (both sexes together) | `no-ge-frat` | brother and sister / siblings |
| **re-** | Repetition / Return of action | `ve-re-far` | redo / make again |

---

### 1.4. Suffixes (Strict Sequential Order)

Suffixes in Nodal attach to the root in a strictly fixed order **1 ➔ 2 ➔ 3 ➔ 4 ➔ 5 ➔ 6**:

```text
[Prefix] + [Root] + [1. Internal Prop.] + [2. Classification] + [3. Size/Space] + [4. Number] + [5. Tense/Mood] + [6. Accusative]
```

#### 1. Internal Properties and Nuances
* `-um-` — special / idiomatic suffix (semantic operator)
* `-aĉ-` — low quality / pejorative (`no-dom-aĉ` = hovel)
* `-ec-` — abstract quality (`pa-bon-ec` = goodness)
* `-ig-` — causative / to make into (`ve-bon-ig` = improve)
* `-iĝ-` — passive / to become (`ve-bon-iĝ` = become better)

#### 2. Classification and Gender
* `-in-` — feminine gender (`no-hom-in` = woman, `no-kat-in` = female cat)
* `-on-` — masculine gender (`no-hom-on` = man, `no-kat-on` = male cat)
* `-ul-` — person characterized by trait (`no-bon-ul` = good person, `no-rich-ul` = rich person)
* `-an-` — member / inhabitant (`no-gor-an` = townsman, `no-mord-an` = northerner)
* `-ist-` — professional / specialist (`no-art-ist` = artist)
* `-estr-` — leader / chief / responsible (`no-urb-estr` = village head, `no-gor-estr` = city mayor)

#### 3. Size, Fragment, and Place
* `-et-` — diminutive (`no-dom-et` = small house / cottage)
* `-eg-` — augmentative (`no-dom-eg` = mansion / palace)
* `-er-` — part / fragment / share (`no-pan-er` = bread crumb, `na-dek-er` = 1/10)
* `-ar-` — collection / set (`no-arb-ar` = forest / collection of trees)
* `-eá` — place / venue (`no-lern-eá` = school / venue of learning)
* `-ué-` — container / receptacle (`no-akv-ué` = water pitcher)

#### 4. Number
* `-mó` — plural (`no-hom-mó` = humans / people, `no-dom-mó` = houses)

#### 5. Tense and Mood
* `-as` — present tense / predicative (`ve-vid-as` = sees, `pa-grand-as` = is large)
* `-is` — past tense (`ve-vid-is` = saw)
* `-os` — future tense (`ve-vid-os` = will see)
* `-us` — conditional mood (`ve-vid-us` = would see)
* `-ut` — imperative mood (`ve-vid-ut` = look!)
* `-im` — infinitive (`ve-vid-im` = to see)

#### 6. Accusative (Direct Object Case)
* `-om` — direct object marker for flexible word order (`no-dom-om ve-vid-as pro-mi` = The house [obj], sees I)

---

### 1.5. Roots by Categories

In all tables, roots strictly obey the 2–5 letter rule.

#### 1. Human & Body

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **hom** | `no-hom` | human / person |
| **inf** | `no-inf` | child |
| **vir** | `no-vir` | man (base) |
| **fem** | `no-fem` | woman (base) |
| **patr** | `no-patr` | father |
| **matr** | `no-matr` | mother |
| **frat** | `no-frat` | sibling |
| **amik** | `no-amik` | friend |
| **enem** | `no-enem` | enemy |
| **kap** | `no-kap` | head |
| **har** | `no-har` | hair |
| **oka** | `no-oka` | eye (distinguished from ok=8) |
| **naz** | `no-naz` | nose |
| **buk** | `no-buk` | mouth |
| **den** | `no-den` | tooth |
| **kord** | `no-kord` | heart |
| **hem** | `no-hem` | blood |
| **han** | `no-han` | hand |
| **ped** | `no-ped` | foot / leg |

#### 2. Nature & Cosmos

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **sol** | `no-sol` | sun |
| **lun** | `no-lun` | moon |
| **stel** | `no-stel` | star |
| **akv** | `no-akv` | water |
| **faé** | `no-faé` | fire |
| **ter** | `no-ter` | earth / land |
| **aer** | `no-aer` | air |
| **foret** | `no-foret` | forest |
| **dezet** | `no-dezet` | desert |
| **mar** | `no-mar` | sea |
| **mon** | `no-mon` | mountain |
| **flor** | `no-flor` | flower |
| **arb** | `no-arb` | tree |
| **mord** | `no-mord` | north |

#### 3. Animals

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **best** | `no-best` | animal |
| **fiš** | `no-fiš` | fish |
| **kaval** | `no-kaval` | horse |
| **kat** | `no-kat` | cat |
| **donk** | `no-donk` | dog |
| **av** | `no-av` | bird |
| **insek** | `no-insek` | insect |

#### 4. Food & Drinks

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **pan** | `no-pan` | bread |
| **karn** | `no-karn` | meat |
| **from** | `no-from` | cheese |
| **lakt** | `no-lakt` | milk |
| **frukt** | `no-frukt` | fruit |
| **legum** | `no-legum` | vegetable |
| **vin** | `no-vin` | wine |

#### 5. Home, Objects, and Settlements

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **dom** | `no-dom` | house |
| **fen** | `no-fen` | window |
| **tegm** | `no-tegm` | roof |
| **tabl** | `no-tabl` | table |
| **sedl** | `no-sedl` | chair / seat |
| **tond** | `no-tond` | scissors |
| **livr** | `no-livr` | book |
| **penn** | `no-penn` | writing pen |
| **aut** | `no-aut` | car / automobile |
| **urb** | `no-urb` | village |
| **gor** | `no-gor` | town / city |

#### 6. Verbs of Action and State

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **vid** | `ve-vid` | see / to see |
| **aud** | `ve-aud` | hear / to hear |
| **dir** | `ve-dir` | say / speak |
| **skib** | `ve-skib` | write |
| **dema** | `ve-dema` | ask |
| **resp** | `ve-resp` | answer |
| **lev** | `ve-lev` | lift / raise |
| **ir** | `ve-ir` | go / walk |
| **ven** | `ve-ven` | come |
| **far** | `ve-far` | do / make |
| **lern** | `ve-lern` | learn / study |
| **manĝ** | `ve-manĝ` | eat |
| **trink** | `ve-trink` | drink |
| **viv** | `ve-viv` | live |
| **am** | `ve-am` | love |
| **lig** | `ve-lig` | bind / tie |

#### 7. Adjectives and Qualities

| Root | With Prefix | Meaning | Antonym Root |
| :--- | :--- | :--- | :--- |
| **grand** | `pa-grand` | big / large | `mikr` |
| **mikr** | `pa-mikr` | small / little | `grand` |
| **bon** | `pa-bon` | good | `dol` |
| **dol** | `pa-dol` | bad | `bon` |
| **leger** | `pa-leger` | light (weight) | `pez` |
| **pez** | `pa-pez` | heavy | `leger` |
| **sinir** | `pa-sinir` | left | `dekir` |
| **dekir** | `pa-dekir` | right (side) | `sinir` |
| **nov** | `pa-nov` | new | `vié` |
| **vié** | `pa-vié` | old | `nov` |
| **alt** | `pa-alt` | high / tall | `bas` |
| **bas** | `pa-bas` | low / short | `alt` |
| **varm** | `pa-varm` | warm / hot | `frod` |
| **frod** | `pa-frod` | cold | `varm` |
| **fast** | `pa-fast` | fast / quick | `lent` |
| **lent** | `pa-lent` | slow | `fast` |
| **rich** | `pa-rich` | rich / wealthy | `povr` |
| **povr** | `pa-povr` | poor | `rich` |
| **pur** | `pa-pur` | clean | `sord` |
| **sord** | `pa-sord` | dirty | `pur` |
| **san** | `pa-san` | healthy | `morb` |
| **morb** | `pa-morb` | sick / ill | `san` |

#### 8. Numbers & Fractions

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **nul** | `na-nul` | zero (0) |
| **un** | `na-un` | one (1) |
| **du** | `na-du` | two (2) |
| **tri** | `na-tri` | three (3) |
| **kvar** | `na-kvar` | four (4) |
| **kvin** | `na-kvin` | five (5) |
| **ses** | `na-ses` | six (6) |
| **sep** | `na-sep` | seven (7) |
| **ok** | `na-ok` | eight (8) |
| **nau** | `na-nau` | nine (9) |
| **dek** | `na-dek` | ten (10) |
| **cent** | `na-cent` | hundred (100) |
| **ton** | `na-ton` | thousand (1000) |
| **mil** | `na-mil` | million (1,000,000) |

> **Fractions:** any numeral root + suffix `-er-` yields the fraction
> (`na-dek-er` = 1/10, `na-cent-er` = 1/100, `na-tri-er` = 1/3).

#### 9. Pronouns

| Root | Personal (`pro-`) | Possessive (`pa-`) | Person / Gender |
| :--- | :--- | :--- | :--- |
| **mi** | `pro-mi` (I / me) | `pa-mi` (my / mine) | 1st person sg |
| **ti** | `pro-ti` (you) | `pa-ti` (your / yours) | 2nd person sg |
| **li** | `pro-li` (he / him) | `pa-li` (his) | 3rd person masc |
| **si** | `pro-si` (she / her) | `pa-si` (her / hers) | 3rd person fem |
| **ĝi** | `pro-ĝi` (it) | `pa-ĝi` (its) | 3rd person neut |
| **ni** | `pro-ni` (we / us) | `pa-ni` (our / ours) | 1st person pl |
| **vi** | `pro-vi` (you pl) | `pa-vi` (your pl) | 2nd person pl |
| **ili** | `pro-ili` (they / them) | `pa-ili` (their / theirs) | 3rd person pl |

#### 10. Prepositions (`po-`)

| Root | With Prefix | Meaning |
| :--- | :--- | :--- |
| **pog** | `po-pog` | for (purpose preposition) |
| **en** | `po-en` | in / inside |
| **sur** | `po-sur` | on / upon |
| **sub** | `po-sub` | under / below |
| **apud** | `po-apud` | near / beside |
| **inter** | `po-inter` | between / among |
| **de** | `po-de` | from / of |
| **al** | `po-al` | to / towards |
| **tra** | `po-tra` | through |
| **kun** | `po-kun` | with (together) |
| **sen** | `po-sen` | without |
| **ĝis** | `po-ĝis` | until / till |
| **ci** | `po-ci` | here / this place |
| **ne** | `po-ne` | not (negation particle) |

#### 11. Interrogative / Relative / Demonstrative Roots

| Root | `ka-` (interrogative) | `to-` (relative) | `po-` (adverbial) | `no-` (nominal) | Meaning |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ku** | `ka-ku` — who? | `to-ku` — who / which (anim.) | — | — | animate referent |
| **ĉo** | `ka-ĉo` — what? | `to-ĉo` — which (inanim.) | — | — | inanimate referent |
| **lo** | `ka-lo` — where? | `to-lo` — where / place where | — | — | place / location |
| **tem** | `ka-tem` — when? | `to-tem` — when / time when | — | — | time / moment |
| **man** | `ka-man` — how? | `to-man` — how / manner in which | — | — | manner / mode |
| **kial** | `ka-kial` — why? | `to-kial` — reason for which | — | — | cause / reason |
| **ci** | — | `to-ci` — this / that (near) | `po-ci` — here / at this place | `no-ci` — this place | deictic place |

**Notes:**
* `ka-` forms are **interrogative**: they introduce a question.
* `to-` forms are **relative / demonstrative**: they introduce a subordinate clause or point to a referent.
* `po-` forms are **adverbial**: they modify a verb or clause.
* `no-` forms are **nominal**: they name the referent as an entity (used when a noun is required syntactically).
* A dash (`—`) indicates that the given prefix is not used with that root.


---

### 1.6. Antonym Pairs

Nodal uses a system of unique paired roots, ensuring aesthetic and expressive speech without artificial prefixes:

| Positive Quality | Negative Quality | Pair Translation |
| :--- | :--- | :--- |
| **bon** (`pa-bon`) | **dol** (`pa-dol`) | good — bad |
| **grand** (`pa-grand`) | **mikr** (`pa-mikr`) | large / big — small / little |
| **leger** (`pa-leger`) | **pez** (`pa-pez`) | light — heavy |
| **sinir** (`pa-sinir`) | **dekir** (`pa-dekir`) | left — right |
| **nov** (`pa-nov`) | **vije** (`pa-vije`) | new — old |
| **alt** (`pa-alt`) | **bas** (`pa-bas`) | high / tall — low / short |
| **varm** (`pa-varm`) | **frod** (`pa-frod`) | warm / hot — cold |
| **fast** (`pa-fast`) | **lent** (`pa-lent`) | fast / quick — slow |
| **pur** (`pa-pur`) | **sord** (`pa-sord`) | clean — dirty |
| **san** (`pa-san`) | **morb** (`pa-morb`) | healthy — sick / ill |
| **rich** (`pa-rich`) | **povr** (`pa-povr`) | rich / wealthy — poor |

---

### 1.7. Word Formation Examples

* `no-hom-in-mó-om`
  * **Breakdown:** `no-` (noun) + `hom` (human) + `-in-` (feminine) + `-mó` (plural) + `-om` (accusative / direct object)
  * **Translation:** (see) women (as a direct object)
* `ve-dis-lig-as`
  * **Breakdown:** `ve-` (verb) + `dis-` (separation) + `lig` (bind) + `-as` (present tense)
  * **Translation:** unties / disconnects
* `pa-grand-eg-as`
  * **Breakdown:** `pa-` (adjective) + `grand` (large) + `-eg-` (augmentative) + `-as` (present tense)
  * **Translation:** is gigantic / enormous
* `no-pan-er`
  * **Breakdown:** `no-` (noun) + `pan` (bread) + `-er` (part / fragment)
  * **Translation:** bread crumb
* `na-du na-tri-er`
  * **Breakdown:** `na-du` (two) + `na-tri-er` (third portion)
  * **Translation:** two thirds (2/3)
* `no-lern-eá`
  * **Breakdown:** `no-` (noun) + `lern` (learn) + `-eá` (place / venue)
  * **Translation:** school / learning venue
* `po-pog`
  * **Breakdown:** `po-` (preposition) + `pog` (purpose / target)
  * **Translation:** for
* `ko-tor`
  * **Breakdown:** `ko-` (conjunction) + `tor` (cause / reason)
  * **Translation:** because

---

## Machine-Readable JSON Database 

The dictionary lives in [`dictionary.json`](../dictionary.json).
All contributions to the lexicon go through that file. Rules for adding
new roots are in [`CONTRIBUTING.md`](../CONTRIBUTING.md).


