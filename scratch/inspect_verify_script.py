with open("scratch/verify_mobile_app_ui.py", "r", encoding="utf-8") as f:
    text = f.read()

for l in text.split("\n"):
    if "pw" in l.lower() or "password" in l.lower() or "vault" in l.lower():
        print(l.strip()[:90])
