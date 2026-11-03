with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("function renderFanChart")
print(text[pos+4200:pos+4800])
