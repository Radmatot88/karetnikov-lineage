import os

if os.path.exists(".dev.vars"):
    with open(".dev.vars", "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                k = line.split("=")[0].strip()
                print("Key:", k)
else:
    print(".dev.vars does not exist!")
