import re

with open("public/heraldry/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update :root to Light Imperial Vellum
root_old = """:root {
    --bg: #0b0d13;
    --card: #131722;
    --border: #2a3042;
    --gold: #d4af37;
    --gold-light: #f3e5ab;
    --crimson: #8b0000;
    --emerald: #10b981;
    --text: #e8ecf2;
    --muted: #94a3b8;
  }"""

root_new = """:root {
    --bg: #FAF6EE;
    --card: #FFFFFF;
    --border: rgba(124, 94, 36, 0.28);
    --gold: #7A1C1C;
    --gold-light: #8B261E;
    --crimson: #7A1C1C;
    --emerald: #146C43;
    --text: #1A1715;
    --muted: #4A423B;
  }
  .svg-icon {
    width: 18px;
    height: 18px;
    display: inline-block;
    vertical-align: middle;
    margin-right: 6px;
    stroke: currentColor;
  }"""

html = html.replace(root_old, root_new)

# 2. Update styles for header, grid, cards
html = html.replace(
    "background: radial-gradient(circle at top, #1e1b18 0%, #0d1017 100%);",
    "background: #FFFFFF; border: 1.5px solid #7C5E24;"
)
html = html.replace("box-shadow: 0 10px 30px rgba(0,0,0,0.6);", "box-shadow: 0 4px 20px rgba(74,66,59,0.1);")
html = html.replace("box-shadow: 0 8px 24px rgba(0,0,0,0.45);", "box-shadow: 0 4px 16px rgba(74,66,59,0.08);")
html = html.replace("background: #07090e;", "background: #FDFBF7;")
html = html.replace("color: #cbd5e1;", "color: var(--muted);")
html = html.replace("background: rgba(212, 175, 55, 0.1);", "background: rgba(122, 28, 28, 0.08);")
html = html.replace("background: rgba(212, 175, 55, 0.2);", "background: rgba(122, 28, 28, 0.1);")
html = html.replace("background: rgba(212, 175, 55, 0.08);", "background: rgba(122, 28, 28, 0.06);")
html = html.replace("color: #6ee7b7;", "color: #146C43;")
html = html.replace("color: #fcd34d;", "color: #B45309;")
html = html.replace("grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));", "grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));")
html = html.replace("grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));", "grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));")
html = html.replace("color: #000;", "color: #FFF;")

# Add mobile responsive styling
media_style = """
  @media (max-width: 600px) {
    body { padding: 12px; }
    .header { padding: 18px 12px; }
    .header h1 { font-size: 20px; }
    .img-box { height: 280px; }
    .hero-compare { grid-template-columns: 1fr; }
    .grid-3 { grid-template-columns: 1fr; }
  }
</style>"""
html = html.replace("</style>", media_style)

# 3. Replace all Emojis with inline SVG
svg_temple = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5L12 4l9 5.5"/><path d="M4 10h16M2 20h20M5 10v10M9 10v10M15 10v10M19 10v10"/></svg>'
svg_back = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>'
svg_scroll = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a3 3 0 0 1 3-3z"/><path d="M4 7h13a2 2 0 0 1 2 2"/><path d="M8 11h7M8 14h5"/></svg>'
svg_bee = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="6"/><path d="M12 6V2M12 22v-4M4 12H2M22 12h-2M7.5 7.5L5 5M19 19l-2.5-2.5M16.5 7.5L19 5M5 19l2.5-2.5"/></svg>'
svg_crown = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4l3 12h14l3-12-6 7-4-7-4 7-6-7zm3 16h14v2H5z"/></svg>'
svg_photo = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h4l2-3h4l2 3h4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2z"/><circle cx="12" cy="14" r="4"/></svg>'
svg_eagle = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l3 4 5-1-2 6 4 3-5 3-1 4-4-2-4 2-1-4-5-3 4-3-2-6 5 1z"/></svg>'
svg_close = '<svg class="svg-icon" style="margin-right:4px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'

html = html.replace("<h1>🏛️ Гербовник", f"<h1>{svg_temple}Гербовник")
html = html.replace("⬅ На главную", f"{svg_back}На главную")
html = html.replace("📜 ОГ XI, 54", f"{svg_scroll}ОГ XI, 54")
html = html.replace("🏛️ ДС XIX, 30", f"{svg_temple}ДС XIX, 30")
html = html.replace("🐝 ДС XIX, 31", f"{svg_bee}ДС XIX, 31")
html = html.replace("👑 I. Эталонный Большой Герб", f"{svg_crown}I. Эталонный Большой Герб")
html = html.replace("📸 II. Документальные скриншоты", f"{svg_photo}II. Документальные скриншоты")
html = html.replace("🦅 III. Полная Галерея Фамильной Атрибутики", f"{svg_eagle}III. Полная Галерея Фамильной Атрибутики")
html = html.replace("✕ Закрыть", f"{svg_close}Закрыть")

with open("public/heraldry/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated public/heraldry/index.html to Light Imperial Vellum + SVG icons successfully!")
