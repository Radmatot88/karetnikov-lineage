with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("async function unlockVaultWithPassword")
print(text[pos:pos+1500])
