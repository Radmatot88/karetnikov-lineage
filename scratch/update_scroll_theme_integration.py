import re

def update_scroll_theme_integration():
    # 1. Update heritage.css
    with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Replace hardcoded #7A1C1C in .scroll-clan-pill.active
    css = re.sub(
        r'\.scroll-clan-pill\.active\s*\{[^}]*\}',
        """.scroll-clan-pill.active {
  background: var(--theme-primary) !important;
  border-color: var(--theme-primary) !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px var(--theme-glow) !important;
}""",
        css
    )

    # Update scroll-gen-header and scroll-gen-num to use var(--theme-primary)
    css = re.sub(
        r'\.scroll-gen-header\s*\{[^}]*\}',
        """.scroll-gen-header {
  background: #FFFFFF;
  border: 1.5px solid var(--theme-border-subtle);
  border-left: 5px solid var(--theme-primary) !important;
  border-radius: 12px;
  padding: 12px 14px;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  box-shadow: 0 2px 8px rgba(74, 66, 59, 0.05);
}""",
        css
    )

    css = re.sub(
        r'\.scroll-gen-num\s*\{[^}]*\}',
        """.scroll-gen-num {
  width: 32px;
  height: 32px;
  min-width: 32px;
  border-radius: 8px;
  background: var(--theme-primary) !important;
  color: #FFFFFF !important;
  font-weight: 800;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
}""",
        css
    )

    css = re.sub(
        r'\.scroll-gen-title\s*\{[^}]*\}',
        """.scroll-gen-title {
  font-size: 15px;
  font-weight: 800;
  color: var(--theme-primary) !important;
}""",
        css
    )

    with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("heritage.css updated with theme variable inheritance!")

    # 2. Update index.astro event listener for scroll clan pills
    with open("src/pages/index.astro", "r", encoding="utf-8") as f:
        content = f.read()

    old_listener = """    document.querySelectorAll('#scrollClanPills .scroll-clan-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        document.querySelectorAll('#scrollClanPills .scroll-clan-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        scrollClanFilter = pill.getAttribute('data-clan') || 'all';
        if (scrollClanFilter === 'hypotheses' && scrollEpistemicMode === 'facts_only') {
          scrollEpistemicMode = 'all_levels';
          syncScrollModeButtons();
        }
        if (lineageData) renderMobileScroll(lineageData);
      });
    });"""

    new_listener = """    document.querySelectorAll('#scrollClanPills .scroll-clan-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        document.querySelectorAll('#scrollClanPills .scroll-clan-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        scrollClanFilter = pill.getAttribute('data-clan') || 'all';
        const theme = pill.getAttribute('data-clan-theme') || 'all';
        setHeraldicClanTheme(theme);
        if (scrollClanFilter === 'hypotheses' && scrollEpistemicMode === 'facts_only') {
          scrollEpistemicMode = 'all_levels';
          syncScrollModeButtons();
        }
        if (lineageData) renderMobileScroll(lineageData);
      });
    });"""

    if old_listener in content:
        content = content.replace(old_listener, new_listener)
        print("index.astro updated with setHeraldicClanTheme trigger on clan pills!")
    else:
        print("Warning: old_listener not found exactly, searching via regex...")
        content = re.sub(
            r'document\.querySelectorAll\(\'#scrollClanPills \.scroll-clan-pill\'\)\.forEach\(pill => \{[^}]*renderMobileScroll\(lineageData\);\s*\}\);',
            new_listener.strip(),
            content
        )

    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.astro saved!")

if __name__ == "__main__":
    update_scroll_theme_integration()
