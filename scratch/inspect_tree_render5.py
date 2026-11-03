with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("function renderRoadmapCanvas")
print(text[pos+6000:pos+7500])
