import re

with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Update :root variables
root_old = """  --bg-obsidian: #07090e;
  --bg-panel: #0e121b;
  --bg-card: #141a26;
  --bg-card-hover: #1c2536;
  --border-subtle: rgba(212, 175, 55, 0.18);
  --border-strong: rgba(212, 175, 55, 0.48);
  --gold-primary: #d4af37;
  --gold-light: #f3dc8a;
  --gold-dim: rgba(212, 175, 55, 0.12);
  --paternal-copper: #e07a5f;
  --maternal-emerald: #2a9d8f;
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --text-dim: #64748b;
  --status-confirmed: #10b981;
  --status-oral: #38bdf8;
  --status-candidate: #f59e0b;
  --status-unknown: #475569;
  --danger: #ef4444;
  --radius-lg: 16px;
  --radius-md: 12px;
  --radius-sm: 8px;
  --shadow-deep: 0 24px 60px rgba(0, 0, 0, 0.65);"""

root_new = """  /* Light Imperial Senate Vellum & Adrianople Crimson (TABOO_02 & WCAG AAA 15.2:1) */
  --bg-obsidian: #FAF6EE;
  --bg-page: #FAF6EE;
  --bg-panel: #EDE4D4;
  --bg-panel-elevated: #E5DBC8;
  --bg-card: #FFFFFF;
  --bg-card-hover: #F7F1E6;
  --border-subtle: rgba(124, 94, 36, 0.25);
  --border-medium: rgba(124, 94, 36, 0.45);
  --border-strong: #7C5E24;
  --gold-primary: #7A1C1C;
  --gold-light: #9B2C2C;
  --gold-dim: rgba(122, 28, 28, 0.08);
  --paternal-copper: #8B261E;
  --paternal-bg: #FBECEB;
  --maternal-emerald: #1B4D3E;
  --maternal-bg: #EAF3EF;
  --text-main: #1A1715;
  --text-secondary: #4A423B;
  --text-muted: #4A423B;
  --text-dim: #6E645A;
  --text-inverse: #FAF6EE;
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
  --shadow-card: 0 4px 12px rgba(74, 66, 59, 0.08);"""

if root_old in css:
    css = css.replace(root_old, root_new)
    print("Replaced :root tokens successfully")
else:
    print("WARNING: root_old not found exactly")

# 2. Update html, body typography and scaling
body_old = """html, body {
  width: 100%;
  min-height: 100vh;
  background-color: var(--bg-obsidian);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, sans-serif;
  line-height: 1.45;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}"""

body_new = """html {
  font-size: 18px; /* Senior Readability standard 60+ */
  -webkit-text-size-adjust: 100%;
}

html[data-font-scale="lg"] {
  font-size: 21.6px; /* +20% */
}

html[data-font-scale="xl"] {
  font-size: 25.2px; /* +40% */
}

html, body {
  width: 100%;
  min-height: 100vh;
  background-color: var(--bg-obsidian);
  color: var(--text-main);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.5;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* --- SVG ICON STANDARD (TABOO_02) --- */
.svg-icon {
  width: 18px;
  height: 18px;
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  stroke: currentColor;
}
.svg-icon.seal-icon {
  width: 20px;
  height: 20px;
}
.svg-icon.sm {
  width: 15px;
  height: 15px;
}
.svg-icon.lg {
  width: 22px;
  height: 22px;
}

/* --- SENIOR FONT SCALER CONTROLS --- */
.font-scale-control {
  display: inline-flex;
  align-items: center;
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 2px;
  gap: 2px;
}
.font-scale-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 13px;
  line-height: 1;
  transition: all 0.15s ease;
}
.font-scale-btn.active, .font-scale-btn:hover {
  background: var(--gold-primary);
  color: #FFFFFF;
}"""

if body_old in css:
    css = css.replace(body_old, body_new)
    print("Replaced body & added font-scale / svg rules successfully")
else:
    print("WARNING: body_old not found")

with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved base heritage.css updates")
