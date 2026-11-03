with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

import re

for i, l in enumerate(lines):
    # Check for dark background colors
    if any(k in l for k in [
        "#07090e", "#090d14", "#0a0e16", "#0b0d13", "#0d1017", "#0e121b", "#121824", "#131822",
        "#141a26", "#161d2b", "#182030", "#1a2332", "#1c2536", "#1e293b", "#0f172a",
        "rgba(0, 0, 0", "rgba(7, 9, 14", "rgba(8, 11, 18", "rgba(10, 14, 22", "rgba(13, 18, 27",
        "rgba(14, 18, 27", "rgba(15, 13, 10", "rgba(18, 24, 36", "rgba(20, 26, 38",
        "rgba(22, 29, 43", "rgba(28, 25, 16", "rgba(32, 27, 16", "rgba(36, 26, 12"
    ]):
        print(f"L{i+1}: {l.strip()[:90]}")
