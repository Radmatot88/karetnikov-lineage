with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("<article\n            class=\"${cardClasses}\"")
print(text[pos:pos+500])
