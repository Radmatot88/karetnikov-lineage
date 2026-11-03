with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("function renderRoadmapCanvas")
print(text[pos+7500:pos+8500])
