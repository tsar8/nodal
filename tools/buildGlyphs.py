import json
import os
import re

BASE = r"D:\Documents\Nodal_text"
SVG_FOLDER = os.path.join(BASE, "svgs")
OUTPUT = os.path.join(BASE, "glyphs.js")

NODAL_LETTERS = set("aeiouáéíóútdpbszkgfvšžčǆĉĝlnrmch")

glyphs = {}
skipped = []

for filename in sorted(os.listdir(SVG_FOLDER)):
    if not filename.endswith(".svg"):
        continue

    m = re.match(r"([0-9A-Fa-f]{4,6})\s+(.+)\.svg$", filename)
    if not m:
        skipped.append(filename)
        continue

    code = int(m.group(1), 16)
    char = chr(code)

    if char not in NODAL_LETTERS:
        skipped.append(f"{filename} → U+{code:04X} '{char}'")
        continue

    with open(os.path.join(SVG_FOLDER, filename), "r", encoding="utf-8") as f:
        content = f.read()

    ds = re.findall(r'<path[^>]*\sd="([^"]+)"', content, re.DOTALL)
    if not ds:
        skipped.append(f"{filename} (no <path d=...>)")
        continue

    # Склеиваем все path одного глифа; убираем переводы строк внутри d.
    combined = " ".join(d.replace("\n", " ") for d in ds)
    glyphs[char] = combined

with open(os.path.join(BASE, "font.json"), "r", encoding="utf-8") as f:
    font_info = json.load(f)

payload = {
    "em": font_info["em"],
    "ascent": font_info["ascent"],
    "descent": font_info["descent"],
    "viewBox": f"0 0 {font_info['em']} {font_info['em']}",
    "glyphs": glyphs,
}

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("// Auto-generated. Do not edit.\n")
    f.write("export const NODAL_GLYPHS = ")
    json.dump(payload, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Wrote {len(glyphs)} glyphs → {OUTPUT}")
print("Found letters:", " ".join(sorted(glyphs)))
print()
print("Skipped:")
for s in skipped:
    print("  -", s)