import os

for fname in os.listdir("scratch"):
    if "deploy" in fname.lower() or "cf" in fname.lower() or "wrangler" in fname.lower():
        print("Checking", fname)
        with open(os.path.join("scratch", fname), "r", encoding="utf-8") as f:
            t = f.read()
            if "token" in t.lower() or "api" in t.lower():
                print("   Found token/api references in", fname)
