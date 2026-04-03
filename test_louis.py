import louis

# Grade 2 English Unified Braille table
table = "en-ueb-g2.ctb"
text = "Hello World"
translated = louis.translateString([table], text)
print(f"Text: {text}")
print(f"Braille: {translated}")