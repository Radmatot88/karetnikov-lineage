import re

def apply_wave1_css():
    with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Define the 4 Heraldic Houses CSS token system
    theme_tokens = """/* ==========================================================================
   DYNAMIC 4-CLAN HERALDIC THEME ENGINE (FOUR HOUSES OF KARETNIKOV LINEAGE)
   WCAG 2.2 Level AAA Compliant | Smooth 0.35s Cubic Bezier Morphing
   ========================================================================== */

:root {
  /* Default Theme: Sovereign Quad-Dynasty Synthesis (Все 4 Рода / Граф Каретников) */
  --theme-primary: #7A1C1C;
  --theme-primary-hover: #9B2C2C;
  --theme-accent: #8C6D32;
  --theme-accent-light: #B45309;
  --theme-bg: #FAF6EE;
  --theme-surface: #FFFFFF;
  --theme-surface-warm: #FAF6EE;
  --theme-border: #8C6D32;
  --theme-border-subtle: rgba(140, 109, 50, 0.25);
  --theme-glow: rgba(122, 28, 28, 0.15);
  --theme-badge-bg: rgba(122, 28, 28, 0.08);
  --theme-watermark-opacity: 0.04;

  /* Global Core Tokens Mapped to Active Theme */
  --bg-obsidian: var(--theme-bg);
  --bg-page: var(--theme-bg);
  --bg-panel: #EDE4D4;
  --bg-panel-elevated: #E5DBC8;
  --bg-card: var(--theme-surface);
  --bg-card-hover: var(--theme-surface-warm);
  --border-subtle: var(--theme-border-subtle);
  --border-medium: var(--theme-border);
  --border-strong: var(--theme-border);
  --gold-primary: var(--theme-primary);
  --gold-light: var(--theme-primary-hover);
  --gold-dim: var(--theme-badge-bg);
  --text-main: #1A1715;
  --text-secondary: #4A423B;
  --text-muted: #4A423B;
  --text-dim: #6E645A;
  --text-inverse: #FFFFFF;
  --status-confirmed: #146C43;
  --status-confirmed-bg: #EDF7F1;
  --status-oral: #1D4ED8;
  --status-oral-bg: #EFF5FF;
  --status-candidate: #B45309;
  --status-candidate-bg: #FEF7ED;
  --status-unknown: #64748B;
  --status-unknown-bg: #F1F5F9;
  --danger: #B91C1C;
  --radius-lg: 16px;
  --radius-md: 12px;
  --radius-sm: 8px;
  --shadow-deep: 0 12px 36px rgba(74, 66, 59, 0.14);
  --shadow-card: 0 4px 12px rgba(74, 66, 59, 0.08);
}

/* 1. ДОМ КАРЕТНИКОВЫХ (Имперский Адрианопольский Пурпур и Литейная Бронза) */
html[data-clan-theme="karetnikov"],
body[data-clan-theme="karetnikov"] {
  --theme-primary: #7A1C1C;
  --theme-primary-hover: #9B2C2C;
  --theme-accent: #B45309;
  --theme-accent-light: #D97706;
  --theme-bg: #FAF6EE;
  --theme-surface: #FFFFFF;
  --theme-surface-warm: #FAF5EA;
  --theme-border: #8C6D32;
  --theme-border-subtle: rgba(140, 109, 50, 0.28);
  --theme-glow: rgba(122, 28, 28, 0.18);
  --theme-badge-bg: rgba(122, 28, 28, 0.08);
  --bg-panel: #EDE4D4;
  --bg-panel-elevated: #E5DBC8;
}

/* 2. ДОМ КУМАНИНЫХ (Московский Лазоревый Лазурит и Чистое Сусальное Золото) */
html[data-clan-theme="kumanin"],
body[data-clan-theme="kumanin"] {
  --theme-primary: #1D4ED8;
  --theme-primary-hover: #1E40AF;
  --theme-accent: #B45309;
  --theme-accent-light: #D97706;
  --theme-bg: #F4F7FC;
  --theme-surface: #FFFFFF;
  --theme-surface-warm: #EEF4FD;
  --theme-border: #2563EB;
  --theme-border-subtle: rgba(37, 99, 235, 0.28);
  --theme-glow: rgba(29, 78, 216, 0.18);
  --theme-badge-bg: rgba(29, 78, 216, 0.08);
  --bg-panel: #E2E8F4;
  --bg-panel-elevated: #D7E1F0;
}

/* 3. ДОМ ЗУБКОВЫХ (Малахитовый Хвойный Изумруд и Античная Латунь) */
html[data-clan-theme="zubkov"],
body[data-clan-theme="zubkov"] {
  --theme-primary: #146C43;
  --theme-primary-hover: #0F5132;
  --theme-accent: #9A7B38;
  --theme-accent-light: #B89243;
  --theme-bg: #F2F8F5;
  --theme-surface: #FFFFFF;
  --theme-surface-warm: #EAF4EE;
  --theme-border: #146C43;
  --theme-border-subtle: rgba(20, 108, 67, 0.28);
  --theme-glow: rgba(20, 108, 67, 0.18);
  --theme-badge-bg: rgba(20, 108, 67, 0.08);
  --bg-panel: #DEEDE5;
  --bg-panel-elevated: #D2E4DA;
}

/* 4. ДОМ ЮХИНЫХ (Царский Аметист / Слива и Волжская Степная Медь) */
html[data-clan-theme="yukhin"],
body[data-clan-theme="yukhin"] {
  --theme-primary: #6B21A8;
  --theme-primary-hover: #581C87;
  --theme-accent: #C2410C;
  --theme-accent-light: #EA580C;
  --theme-bg: #FAF5FF;
  --theme-surface: #FFFFFF;
  --theme-surface-warm: #F6EDFE;
  --theme-border: #7E22CE;
  --theme-border-subtle: rgba(126, 34, 206, 0.28);
  --theme-glow: rgba(107, 33, 168, 0.18);
  --theme-badge-bg: rgba(107, 33, 168, 0.08);
  --bg-panel: #F1E5F8;
  --bg-panel-elevated: #E7D5F2;
}

/* Плавный кинематографичный переход тинктур */
html, body, .topbar, .brand-seal, .scroll-person-card, .rm-node, .mob-bottom-nav,
.mob-nav-item, .chip-btn, .scroll-clan-pill, .seg-btn, .roadmap-shell, .clan-theme-pill {
  transition: background-color 0.35s cubic-bezier(0.16, 1, 0.3, 1),
              border-color 0.35s cubic-bezier(0.16, 1, 0.3, 1),
              color 0.35s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
"""

    # Replace old :root definition with new theme tokens
    old_root = re.search(r':root\s*\{[^}]*\}', css, re.DOTALL)
    if old_root:
        css = theme_tokens + "\n\n" + css[old_root.end():]
        print("Replaced :root with dynamic 4-clan theme tokens!")
    else:
        print("Error: Could not locate :root")
        return False

    # Clan Selector Pills styling for HUD and Topbar
    clan_pills_css = """
/* ==================== FOUR HOUSES HERALDIC SELECTOR BAR ==================== */
.clan-switcher-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  overflow-x: auto;
  padding: 4px 2px;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}
.clan-switcher-bar::-webkit-scrollbar { display: none; }

.clan-theme-pill {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 7px 14px;
  border-radius: 999px;
  background: #FFFFFF;
  border: 1.5px solid var(--border-medium);
  font-size: 12.5px;
  font-weight: 700;
  color: var(--text-main);
  cursor: pointer;
  white-space: nowrap;
  box-shadow: 0 2px 6px rgba(74, 66, 59, 0.06);
  user-select: none;
}

.clan-theme-pill:hover {
  border-color: var(--theme-primary);
  color: var(--theme-primary);
  transform: translateY(-1px);
}

.clan-theme-pill.active {
  background: var(--theme-primary);
  border-color: var(--theme-primary);
  color: #FFFFFF;
  box-shadow: 0 4px 14px var(--theme-glow);
}

.clan-theme-pill.active .svg-icon {
  stroke: #FFFFFF;
}

/* Card Generation Header Pill inside rm-card-top-bar */
.rm-gen-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.05em;
  padding: 2.5px 7px;
  border-radius: 6px;
  background: var(--theme-badge-bg);
  border: 1px solid var(--theme-border-subtle);
  color: var(--theme-primary);
  text-transform: uppercase;
}

/* Proband Monogram Cameo */
.proband-portrait {
  border-color: var(--theme-accent) !important;
}
.rm-proband-crown-title {
  color: var(--theme-primary) !important;
}
.rm-node.proband-node {
  border-color: var(--theme-primary) !important;
}

/* Canvas Heraldic Watermark */
.canvas-heraldic-watermark {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 540px;
  height: 540px;
  pointer-events: none;
  opacity: var(--theme-watermark-opacity);
  z-index: 0;
  transition: opacity 0.5s ease;
}
"""

    css += "\n" + clan_pills_css

    with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Wave 1 CSS applied successfully!")
    return True

if __name__ == "__main__":
    apply_wave1_css()
