with open(r"C:\Karetnikov_Lineage\data\vault\karetnikov_lineage.ged", "r", encoding="utf-8", errors="ignore") as f:
    ged_lines = f.readlines()

print(f"GED lines: {len(ged_lines)}")
current_indi = None
indi_records = {}

for line in ged_lines:
    line_clean = line.strip()
    if line_clean.startswith("0 @I") and "INDI" in line_clean:
        current_indi = line_clean.split()[1]
        indi_records[current_indi] = []
    elif current_indi:
        if line_clean.startswith("0 "):
            current_indi = None
        else:
            indi_records[current_indi].append(line_clean)

print(f"Total individuals in GED: {len(indi_records)}")

for indi_id, lines in indi_records.items():
    text = " ".join(lines)
    if "Дмитрий" in text or "1913" in text or "Иван" in text or "Каретников" in text:
        # Check if Ivan or Dmitriy
        name_line = [l for l in lines if l.startswith("1 NAME")]
        birt_lines = [l for l in lines if "BIRT" in l or "DATE" in l]
        if any("Дмитрий" in l for l in lines) or any("1913" in l for l in lines) or any("Федор" in l or "Фёдор" in l for l in lines):
            print(f"=== {indi_id} ===")
            for l in lines:
                print(f"  {l}")
