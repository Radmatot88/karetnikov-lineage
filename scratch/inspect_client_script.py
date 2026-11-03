with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

funcs = [
    "togglePwBtn",
    "switchView",
    "focusOnProband",
    "renderMobileScroll",
    "renderFanChart",
    "renderArchiveRadar",
    "openDossier",
    "mobOpenBranchWizardBtn",
    "mobileBottomNav"
]

for fn in funcs:
    matches = [(i+1, l.strip()[:70]) for i, l in enumerate(lines) if fn in l]
    print(f"Function/Keyword '{fn}': {len(matches)} occurrences")
    for m in matches[:5]:
        print(f"   L{m[0]}: {m[1]}")
