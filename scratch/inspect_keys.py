with open(r"C:\Karetnikov_Lineage\.dev.vars", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#"):
            k, _ = line.split("=", 1)
            print("Dev var key:", k)
