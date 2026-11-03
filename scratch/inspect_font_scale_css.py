with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find(".font-scale-control")
print(text[pos:pos+600])
