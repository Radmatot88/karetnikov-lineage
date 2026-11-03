import re

def update_css():
    with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
        css = f.read()

    # 1. .roadmap-shell background
    old_shell = """.roadmap-shell {
  position: relative;
  width: 100%;
  height: calc(100vh - 68px);
  overflow: hidden;
  background-color: #06080d;
  background-image:
    radial-gradient(rgba(212, 175, 55, 0.16) 1px, transparent 1px),
    radial-gradient(rgba(42, 157, 143, 0.08) 1px, transparent 1px);
  background-size: 28px 28px;
  background-position: 0 0, 14px 14px;
  cursor: grab;
  user-select: none;
}"""

    new_shell = """.roadmap-shell {
  position: relative;
  width: 100%;
  height: calc(100vh - 68px);
  overflow: hidden;
  background-color: #FAF6EE;
  background-image:
    radial-gradient(rgba(124, 94, 36, 0.25) 1.2px, transparent 1.2px),
    radial-gradient(rgba(122, 28, 28, 0.12) 1.2px, transparent 1.2px);
  background-size: 28px 28px;
  background-position: 0 0, 14px 14px;
  cursor: grab;
  user-select: none;
}"""
    if old_shell in css:
        css = css.replace(old_shell, new_shell)
        print("Replaced .roadmap-shell background")
    else:
        print("Warning: old_shell not matched exactly, trying regex")
        css = re.sub(
            r'\.roadmap-shell\s*\{[^}]*background-color:\s*#06080d;[^}]*\}',
            new_shell,
            css
        )

    # 2. .rm-node.collateral-node
    css = re.sub(
        r'\.rm-node\.collateral-node\s*\{[^}]*\}',
        """.rm-node.collateral-node {
  border-style: dashed;
  border-color: #7C5E24;
  background: #FFFFFF;
}""",
        css
    )

    # 3. .rm-node.floating-hypothesis-node
    css = re.sub(
        r'\.rm-node\.floating-hypothesis-node\s*\{[^}]*\}',
        """.rm-node.floating-hypothesis-node {
  border: 2px dashed #B45309 !important;
  background: #FFFDF9 !important;
  box-shadow: 0 4px 14px rgba(180, 83, 9, 0.12) !important;
}""",
        css
    )

    # 4. .canvas-hyp-banner
    css = re.sub(
        r'\.canvas-hyp-banner\s*\{[^}]*\}',
        """.canvas-hyp-banner {
  position: absolute;
  width: 310px;
  padding: 8px 14px;
  background: #FEF7ED;
  border: 1.5px dashed #B45309;
  border-radius: 8px;
  text-align: center;
  font-size: 11.5px;
  font-weight: 800;
  color: #9A3412;
  letter-spacing: 0.05em;
  pointer-events: none;
  box-shadow: 0 4px 12px rgba(180, 83, 9, 0.08);
}""",
        css
    )

    # 5. .kinship-pill
    css = re.sub(
        r'\.kinship-pill\s*\{[^}]*\}',
        """.kinship-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: #FFFFFF;
  border: 1.5px solid #7C5E24;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
  color: #1A1715;
  cursor: pointer;
  transition: all 0.15s ease;
}""",
        css
    )

    # 6. .rm-portrait background
    css = re.sub(
        r'\.rm-portrait\s*\{[^}]*\}',
        """.rm-portrait {
  position: relative;
  width: 62px;
  height: 62px;
  min-width: 62px;
  border-radius: 12px;
  background: #F5EFEB;
  border: 1.5px solid #7C5E24;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}""",
        css
    )

    # 7. .drawer-portrait-box
    css = re.sub(
        r'\.drawer-portrait-box\s*\{[^}]*\}',
        """.drawer-portrait-box {
  width: 96px;
  height: 96px;
  min-width: 96px;
  border-radius: 14px;
  border: 2px solid #7C5E24;
  overflow: hidden;
  background: #F5EFEB;
  display: flex;
  align-items: center;
  justify-content: center;
}""",
        css
    )

    # 8. .cipher-box
    css = re.sub(
        r'\.cipher-box\s*\{[^}]*\}',
        """.cipher-box {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  padding: 10px 12px;
  background: #FAF6EE;
  border: 1.5px solid #7C5E24;
  border-radius: var(--radius-sm);
  color: #7A1C1C;
}""",
        css
    )

    with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("heritage.css updated successfully.")

def update_index_astro():
    with open("src/pages/index.astro", "r", encoding="utf-8") as f:
        content = f.read()

    # Fix hypothesis name and era colors in roadmap
    content = content.replace('color:#fef3c7; font-size:12.5px;', 'color:#1A1715; font-size:13px; font-weight:800;')
    content = content.replace('color:#B45309; font-size:11px;', 'color:#7A1C1C; font-size:11.5px; font-weight:600;')
    content = content.replace('outline: 3px solid #f3dc8a; box-shadow: 0 0 28px rgba(243,220,138,0.65);', 'outline: 3px solid #7A1C1C; box-shadow: 0 0 24px rgba(122,28,28,0.3);')

    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.astro updated successfully.")

if __name__ == "__main__":
    update_css()
    update_index_astro()
