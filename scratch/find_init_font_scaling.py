with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("initFontScaling")
print(text[pos-100:pos+800])
