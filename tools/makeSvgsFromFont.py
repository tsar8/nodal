# type: ignore[import]
import fontforge
import json
import os
import sys
import fileinput

# Ensure the svgs folder exists.
svgFolder = "./svgs/"
try:
    os.makedirs(svgFolder)
except OSError:
    if os.path.exists(svgFolder):
        pass
    else:
        raise

# Open the font file.
font = fontforge.open("font.ttf")
print (font.fontname)

# Export font glyphs to svgs.
print ("\nExporting svgs:")
for g in font.glyphs():
  if g.unicode != -1:
    svgPath = "%s%04X %s.svg" % (svgFolder, g.unicode, g.glyphname)
    print ("\t%s" % (svgPath))
    g.export(svgPath)
    for line in fileinput.input(svgPath, inplace=1):
        print (line.replace("<svg viewBox", '<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="2048" viewBox')),

# Export font settings to json.
fontInfo = {
    "fontname": font.fontname,
    "fullname": font.fullname,
    "familyname": font.familyname,
    "weight": font.weight,
    "version": font.version,
    "encoding": font.encoding,
    "copyright": font.copyright,
    "em": font.em,
    "ascent": font.ascent,
    "descent": font.descent
}

# Write json data.
file = open("./font.json", "w")
file.write(json.dumps(fontInfo, indent=4, sort_keys=True))

# Done!
font.close()
print ("Finished exporting.\n")