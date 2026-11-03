with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("function focusOnProband")
print(text[pos:pos+700])
