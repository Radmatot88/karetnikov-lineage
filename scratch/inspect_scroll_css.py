with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    lines = f.readlines()

scroll_rules = []
capturing = False
current_rule = []

for i, l in enumerate(lines):
    if any(k in l for k in [".scroll-", "#view-scroll", ".generation-scroll", ".person-card", ".badge-"]):
        capturing = True
    if capturing:
        current_rule.append(f"{i+1}: {l}")
        if "}" in l and not "{" in l:
            scroll_rules.append("".join(current_rule))
            current_rule = []
            capturing = False

print(f"Found {len(scroll_rules)} scroll rules blocks.")
with open("scratch/scroll_rules_dump.txt", "w", encoding="utf-8") as out:
    out.write("\n---\n".join(scroll_rules))

print("Dumped to scratch/scroll_rules_dump.txt")
