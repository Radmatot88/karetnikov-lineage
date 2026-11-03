with open("scratch/scroll_rules_dump.txt", "r", encoding="utf-8") as f:
    text = f.read()

for block in text.split("\n---\n"):
    if any(k in block for k in ["background", "color:", "#", "rgb"]):
        first_line = block.split("\n")[0]
        print(first_line)
        for line in block.split("\n"):
            if any(k in line for k in ["background", "color:", "border"]):
                print("   ", line.strip())
