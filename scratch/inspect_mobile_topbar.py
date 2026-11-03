with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("@media (max-width: 860px)")
print(text[pos:pos+1000])
