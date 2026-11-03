with open("src/utils/heraldic_icons.ts", "r", encoding="utf-8") as f:
    ts = f.read()

# Let's inspect the export in heraldic_icons.ts
print(f"Length of heraldic_icons.ts: {len(ts)}")
# Clean export const HERALDIC_ICONS = { ... } for client script
