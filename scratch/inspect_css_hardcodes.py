with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ["#07090e", "#0e121b", "#141a26", "#1c2536", "#d4af37", "#f3dc8a", "rgba(7, 9, 14", "rgba(8, 11, 18", "rgba(14, 18, 27", "rgba(20, 26, 38", "rgba(212, 175, 55"]):
        print(f"L{i+1}: {line.strip()[:80]}")
