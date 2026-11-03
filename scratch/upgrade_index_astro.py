import re

with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    content = f.read()

# Normalize CRLF to LF for reliable string matching
content = content.replace("\r\n", "\n")

# SVG definitions to inject into HTML and JS
SVG_DEFS = """
  <!-- SVG ICON HELPER TEMPLATES (ZERO EMOJI CANON) -->
  <svg style="display:none;" xmlns="http://www.w3.org/2000/svg">
    <symbol id="icon-shield-fortress" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 2L4 5v6.09c0 5.05 3.41 9.76 8 10.91 4.59-1.15 8-5.86 8-10.91V5l-8-3z"/><path d="M12 8v4m0 4h.01"/>
    </symbol>
    <symbol id="icon-lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V6.5a4 4 0 0 1 8 0V10"/><circle cx="12" cy="15" r="1.3" fill="currentColor"/><path d="M12 16.3v2"/>
    </symbol>
    <symbol id="icon-eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
    </symbol>
    <symbol id="icon-eye-off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/>
    </symbol>
    <symbol id="icon-scroll" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M7 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a3 3 0 0 1 3-3z"/><path d="M4 7h13a2 2 0 0 1 2 2"/><path d="M8 11h7M8 14h5"/>
    </symbol>
    <symbol id="icon-tree" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 7v5M8 12h8M8 12v4M16 12v4"/><circle cx="12" cy="7" r="1.5" fill="currentColor"/><circle cx="8" cy="16" r="1.5" fill="currentColor"/><circle cx="16" cy="16" r="1.5" fill="currentColor"/>
    </symbol>
    <symbol id="icon-fan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 21a9 9 0 0 1-9-9 9 9 0 0 1 9-9 9 9 0 0 1 9 9"/><path d="M12 21l-6-6a5.5 5.5 0 0 1 6-7.8 5.5 5.5 0 0 1 6 7.8z"/><path d="M12 21V12M12 12L7.5 7.5M12 12l4.5-4.5M12 12H3M12 12h9"/>
    </symbol>
    <symbol id="icon-temple" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3 9.5L12 4l9 5.5"/><path d="M4 10h16M2 20h20M5 10v10M9 10v10M15 10v10M19 10v10"/>
    </symbol>
    <symbol id="icon-radar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/><path d="M12 12l4-4-1.5 5.5L9 15z"/>
    </symbol>
    <symbol id="icon-branch" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 20c4-1 8-5 9-10 1.2-5.5 5-7 7-7-1 3-1 6-4 8-3 2-6 3-7 7"/><path d="M10 13c-2.5 0-4.5 1.5-5 3.5 1.5.5 3.5 0 5-1.5z"/><path d="M17 17v4M15 19h4"/>
    </symbol>
    <symbol id="icon-download" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 3v13M7 11l5 5 5-5"/><path d="M4 17v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>
    </symbol>
    <symbol id="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M18 6L6 18M6 6l12 12"/>
    </symbol>
    <symbol id="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/>
    </symbol>
    <symbol id="icon-focus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>
    </symbol>
    <symbol id="icon-settings" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>
    </symbol>
    <symbol id="icon-photo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 7h4l2-3h4l2 3h4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2z"/><circle cx="12" cy="14" r="4"/>
    </symbol>
    <symbol id="icon-calendar" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 9h18"/><path d="M8 13h2M14 13h2M8 17h2M14 17h2"/>
    </symbol>
    <symbol id="icon-pin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>
    </symbol>
    <symbol id="icon-burial" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 3v17M8 7h8M9 14h6"/><path d="M5 20h14"/>
    </symbol>
    <symbol id="icon-quill" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M19 3C16 4 12 7 10 11c-1.5 3-2 6-4 8l3-1c3-1.5 6-3 8-5 3-3 4-8 2-10z"/><path d="M6 19l-3 2 1-3"/><path d="M13 8l3 3"/>
    </symbol>
    <symbol id="icon-kinship" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 6c4 0 6 6 10 6s6 6 6 6M20 6c-4 0-6 6-10 6S4 18 4 18"/><path d="M7 6v12M12 9v6M17 6v12"/>
    </symbol>
    <symbol id="icon-link" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
    </symbol>
    <symbol id="icon-book" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="14" y2="11"/>
    </symbol>
    <symbol id="icon-seal-confirmed" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 2l2.4 2.2 3.2-.5 1.3 3 2.9 1.5-.7 3.2 2.2 2.4-2.2 2.4.7 3.2-2.9 1.5-1.3 3-3.2-.5L12 22l-2.4-2.2-3.2.5-1.3-3-2.9-1.5.7-3.2L0.7 12l2.2-2.4-.7-3.2 2.9-1.5 1.3-3 3.2.5L12 2z"/><path d="M8.5 12.3l2.4 2.4 4.8-5"/>
    </symbol>
    <symbol id="icon-seal-oral" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9"/><path d="M8 8.5c0-1.1.9-2 2-2h4.5c1.1 0 2 .9 2 2v7c0 1.1-.9 2-2 2H10c-1.1 0-2-.9-2-2v-7z"/><path d="M8 15.5c-1.1 0-2-.9-2-2s.9-2 2-2"/><path d="M11 10h4M11 13h2.5"/>
    </symbol>
    <symbol id="icon-seal-candidate" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9.2" stroke-dasharray="2.5 1.5"/><circle cx="11" cy="11" r="3.8"/><path d="M14 14l3.5 3.5"/>
    </symbol>
    <symbol id="icon-seal-unknown" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 3L4.5 6.5v6c0 5 3.5 9 7.5 10.5 4-1.5 7.5-5.5 7.5-10.5v-6L12 3z"/><path d="M10.2 9.5a2 2 0 1 1 3.2 1.8c-.8.6-1.4 1.1-1.4 2.2"/><circle cx="12" cy="16.5" r="0.7" fill="currentColor"/>
    </symbol>
    <symbol id="icon-clan-karetnikov" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.8"/><path d="M12 3v6.2M12 14.8V21M3 12h6.2M14.8 12H21"/><path d="M5.6 5.6l4.4 4.4M14 14l4.4 4.4M18.4 5.6l-4.4 4.4M10 14l-4.4 4.4"/>
    </symbol>
    <symbol id="icon-clan-kumanin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 18c2-6 7-12 16-14-1 4-2 8-5 11-2.5 2.5-6 4-11 3z"/><path d="M6 16c3-4 6-7 11-9M7.5 17.5c2.5-3 5-5 8.5-6.5"/><path d="M19 14.5l.8 1.8 1.9.3-1.4 1.3.4 1.9-1.7-.9-1.7.9.4-1.9-1.4-1.3 1.9-.3z"/>
    </symbol>
    <symbol id="icon-clan-zubkov" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M4 20l11-11M15 9c2-2 4-2.5 5.5-2.5s.5 2-.5 3.5-3 3-5 5"/><path d="M3 21l2-2M2 19l3 3M6 18l-2 2"/><path d="M18 5l2-2 1.5 1.5-2 2"/><path d="M20 20L11 11M9 13c-2 2-3.5 2.5-5 2.5.5-2 1.5-3.5 3.5-5"/><path d="M21 21l-2-2M22 19l-3 3M18 18l2 2"/>
    </symbol>
    <symbol id="icon-clan-yukhin" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 3v13M12 3c-1.5 1.5-2 3-1.5 4.5 1.5 0 2.5-.5 3.5-2-.5-1.2-1-2-2-2.5z"/><path d="M12 7.5c-1.8 1.2-2.3 2.8-1.8 4.2 1.6 0 2.7-.5 3.8-2.2-.6-1-1-1.5-2-2z"/><path d="M12 12c-2 1-2.5 2.5-2 4 1.8 0 3-.5 4-2-.6-1-1-1.5-2-2z"/><path d="M3 18.5c2.5-1 4.5-1 7 0s4.5 1 7 0 4.5-1 5 0"/><path d="M3 21.5c2.5-1 4.5-1 7 0s4.5 1 7 0 4.5-1 5 0"/>
    </symbol>
    <symbol id="icon-orbit-hypothesis" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="12" cy="12" r="5"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(-25 12 12)"/>
    </symbol>
    <symbol id="icon-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="20 6 9 17 4 12"/>
    </symbol>
    <symbol id="icon-hand" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
      <path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v7M10 10.5V6a2 2 0 0 0-4 0v8M18 8a2 2 0 1 1 4 0v7a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.9-6.3-2.7L2 17.5l1.5-1.5c.8-.8 1.9-1 2.9-.6L8 16.5"/>
    </symbol>
  </svg>
"""

# Insert SVG symbols right after <body>
if '<!-- SVG ICON HELPER TEMPLATES' not in content:
    content = content.replace("<body>", "<body>\n" + SVG_DEFS)

# 1. Update Fortress Gate
old_gate = """      <div class="gate-badge-row">
        <span class="crypto-pill">AES-256-GCM Dual-Vault</span>
        <span class="crypto-pill">PBKDF2-SHA256 (100k)</span>
        <span class="crypto-pill">Zero-Hardcode</span>
      </div>"""

new_gate = """      <div class="gate-badge-row">
        <span class="crypto-pill">Государственный стандарт архива</span>
        <span class="crypto-pill">Защита данных 152-ФЗ</span>
        <span class="crypto-pill">Edge Zero-Knowledge Vault</span>
      </div>"""
content = content.replace(old_gate, new_gate)

old_pw_btn = """          <button type="button" id="togglePwBtn" class="gate-toggle-pw" title="Показать/скрыть ключ">
            ГЛАЗ
          </button>"""

new_pw_btn = """          <button type="button" id="togglePwBtn" class="gate-eye-btn" title="Показать/скрыть ключ">
            <svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><use href="#icon-eye"/></svg>
          </button>"""
content = content.replace(old_pw_btn, new_pw_btn)

# Input font size >= 16px to prevent iOS auto-zoom
content = content.replace(
    'class="gate-input"\n            placeholder="Введите ключ доступа к родовому архиву..."',
    'class="gate-input"\n            style="font-size:16px;"\n            placeholder="Введите ключ доступа к родовому архиву..."'
)

old_gate_foot = """      <div class="gate-security-footnote">
        <div>🛡️ <strong>Astro Fortress:</strong> X-Robots noindex, AI-Scraper Block</div>
        <div>🔐 <strong>Zero-PII Leak:</strong> Без пароля данные физически нечитаемы</div>
      </div>"""

new_gate_foot = """      <div class="gate-security-footnote">
        <div><svg class="svg-icon sm" style="margin-right:4px;"><use href="#icon-shield-fortress"/></svg> <strong>Astro Fortress:</strong> X-Robots noindex, AI-Scraper Block</div>
        <div><svg class="svg-icon sm" style="margin-right:4px;"><use href="#icon-lock"/></svg> <strong>Zero-PII Vault:</strong> Без пароля данные физически нечитаемы</div>
      </div>"""
content = content.replace(old_gate_foot, new_gate_foot)

# 2. Update Topbar
old_tabs = """      <nav class="nav-tabs" aria-label="Режимы отображения">
        <button class="nav-tab" data-view="scroll">📱 Свиток Поколений (Умная Навигация)</button>
        <button class="nav-tab active" data-view="tree">🗺️ 2D-Карта Древа (Pan & Zoom)</button>
        <button class="nav-tab" data-view="fan">🎡 Круговой Веер 127</button>
        <button class="nav-tab" data-view="radar">📡 Архивный Радар</button>
        <button class="nav-tab" id="tabNavAccess" data-view="access">🔐 Пульт Доступов</button>
      </nav>"""

new_tabs = """      <nav class="nav-tabs" aria-label="Режимы отображения">
        <button class="nav-tab" data-view="scroll"><svg class="svg-icon sm"><use href="#icon-scroll"/></svg> Свиток Поколений</button>
        <button class="nav-tab active" data-view="tree"><svg class="svg-icon sm"><use href="#icon-tree"/></svg> 2D-Карта Древа</button>
        <button class="nav-tab" data-view="fan"><svg class="svg-icon sm"><use href="#icon-fan"/></svg> Круговой Веер 127</button>
        <a href="/heraldry/" class="nav-tab" target="_blank" rel="noopener"><svg class="svg-icon sm"><use href="#icon-temple"/></svg> Гербовник</a>
        <button class="nav-tab" data-view="radar"><svg class="svg-icon sm"><use href="#icon-radar"/></svg> Архивный Радар</button>
        <button class="nav-tab" id="tabNavAccess" data-view="access"><svg class="svg-icon sm"><use href="#icon-lock"/></svg> Доступы</button>
      </nav>"""
content = content.replace(old_tabs, new_tabs)

old_actions = """      <div class="topbar-actions">
        <button id="openBranchWizardBtn" class="btn-outline" style="border-color:#10b981; color:#6ee7b7;" title="Присоединить свою семейную ветку в Большой Род">🌿 Присоединить ветку</button>
        <button id="exportGedBtn" class="btn-outline" title="Скачать стандарт GEDCOM 5.5.1">⬇ GEDCOM (.ged)</button>
        <button id="exportJsonBtn" class="btn-outline" title="Скачать JSON со всеми загруженными фото">⬇ JSON + Фото</button>
        <button id="lockVaultBtn" class="btn-outline" title="Очистить память и закрыть архив">🔒 Закрыть</button>
      </div>"""

new_actions = """      <div class="topbar-actions">
        <div class="font-scale-control" aria-label="Размер шрифта для чтения">
          <button type="button" class="font-scale-btn active" data-scale="normal" title="Стандартный кегль">А</button>
          <button type="button" class="font-scale-btn" data-scale="lg" title="Крупный кегль (+20%)">А+</button>
          <button type="button" class="font-scale-btn" data-scale="xl" title="Максимальный кегль (+40%)">А++</button>
        </div>
        <button id="openBranchWizardBtn" class="btn-outline" style="border-color:var(--status-confirmed); color:var(--status-confirmed);" title="Присоединить свою семейную ветку в Большой Род"><svg class="svg-icon sm"><use href="#icon-branch"/></svg> +Ветвь</button>
        <button id="exportGedBtn" class="btn-outline" title="Скачать стандарт GEDCOM 5.5.1"><svg class="svg-icon sm"><use href="#icon-download"/></svg> GEDCOM</button>
        <button id="exportJsonBtn" class="btn-outline" title="Скачать JSON со всеми загруженными фото"><svg class="svg-icon sm"><use href="#icon-download"/></svg> JSON</button>
        <button id="lockVaultBtn" class="btn-outline" title="Очистить память и закрыть архив"><svg class="svg-icon sm"><use href="#icon-lock"/></svg> Закрыть</button>
      </div>"""
content = content.replace(old_actions, new_actions)

# 3. Update Mobile Bottom Nav (5 items)
old_mob_nav = """    <nav id="mobileBottomNav" class="mobile-bottom-nav" aria-label="Мобильная навигация">
      <button type="button" class="mob-nav-item" data-mob-view="scroll">
        <span class="mob-nav-icon">📱</span>
        <span>Свиток</span>
      </button>
      <button type="button" class="mob-nav-item active" data-mob-view="tree">
        <span class="mob-nav-icon">🗺️</span>
        <span>2D-Карта</span>
      </button>
      <button type="button" class="mob-nav-item" data-mob-view="fan">
        <span class="mob-nav-icon">🎡</span>
        <span>Веер 127</span>
      </button>
      <button type="button" class="mob-nav-item" data-mob-view="radar">
        <span class="mob-nav-icon">📡</span>
        <span>Архивы</span>
      </button>
      <button type="button" class="mob-nav-item" id="mobOpenBranchWizardBtn">
        <span class="mob-nav-icon">🌿</span>
        <span>+ Ветвь</span>
      </button>
    </nav>"""

new_mob_nav = """    <nav id="mobileBottomNav" class="mobile-bottom-nav" aria-label="Мобильная навигация">
      <button type="button" class="mob-nav-item" data-mob-view="scroll">
        <span class="mob-nav-icon"><svg class="svg-icon"><use href="#icon-scroll"/></svg></span>
        <span>Свиток</span>
      </button>
      <button type="button" class="mob-nav-item active" data-mob-view="tree">
        <span class="mob-nav-icon"><svg class="svg-icon"><use href="#icon-tree"/></svg></span>
        <span>2D-Карта</span>
      </button>
      <button type="button" class="mob-nav-item" data-mob-view="fan">
        <span class="mob-nav-icon"><svg class="svg-icon"><use href="#icon-fan"/></svg></span>
        <span>Веер 127</span>
      </button>
      <a href="/heraldry/" class="mob-nav-item" target="_blank" rel="noopener">
        <span class="mob-nav-icon"><svg class="svg-icon"><use href="#icon-temple"/></svg></span>
        <span>Гербовник</span>
      </a>
      <button type="button" class="mob-nav-item" data-mob-view="radar">
        <span class="mob-nav-icon"><svg class="svg-icon"><use href="#icon-radar"/></svg></span>
        <span>Архивы</span>
      </button>
    </nav>"""
content = content.replace(old_mob_nav, new_mob_nav)

# 4. Update Dossier Drawer Close Button
content = content.replace(
    '<button id="closeDrawerBtn" class="drawer-close">✕ Закрыть (Esc)</button>',
    '<button id="closeDrawerBtn" class="drawer-close"><svg class="svg-icon sm"><use href="#icon-close"/></svg> Закрыть</button>'
)

# 5. Add Fan Mobile Touch Card container
old_fan_cont = """    <section id="view-fan" class="view-section padded-view">
      <h2 style="font-size:22px; color:var(--gold-primary); margin-bottom:6px;">Круговой Веер Предков (127 персон, VII Колен)</h2>
      <p style="color:var(--text-muted); font-size:13px; margin-bottom:18px;">
        Канонический веер Соса-Страдоница от Пробанда (#1) до 64 предков VII колена.<br/>
        Наведите на сектор для просмотра имени, кликните для открытия персонального досье.
      </p>

      <div style="display:grid; grid-template-columns: 1fr 300px; gap:24px; align-items:start;" class="fan-grid-layout">
        <div id="fanChartContainer" style="display:flex; justify-content:center; align-items:center; min-height:500px;"></div>"""

new_fan_cont = """    <section id="view-fan" class="view-section padded-view">
      <h2 style="font-size:22px; color:var(--gold-primary); margin-bottom:6px;">Круговой Веер Предков (127 персон, VII Колен)</h2>
      <p style="color:var(--text-muted); font-size:14px; margin-bottom:18px;">
        Канонический веер Соса-Страдоница от Пробанда (#1) до 64 предков VII колена.<br/>
        Нажмите на сектор для просмотра персоны и открытия архивного досье.
      </p>

      <div style="display:grid; grid-template-columns: 1fr 300px; gap:24px; align-items:start;" class="fan-grid-layout">
        <div>
          <div id="fanChartContainer" style="display:flex; justify-content:center; align-items:center; min-height:480px;"></div>
          <div id="fanMobileInspector" class="fan-mobile-card" style="display:none;"></div>
        </div>"""
content = content.replace(old_fan_cont, new_fan_cont)

# 6. Replace remaining emojis in HTML markup
content = content.replace('🧬 Умный навигатор прямого родства (от #1)', '<svg class="svg-icon sm"><use href="#icon-kinship"/></svg> Умный навигатор прямого родства (от #1)')
content = content.replace('<span class="scroll-search-icon">🔍</span>', '<span class="scroll-search-icon"><svg class="svg-icon sm"><use href="#icon-search"/></svg></span>')
content = content.replace('🟢 Только 100% факты', '<svg class="svg-icon sm"><use href="#icon-seal-confirmed"/></svg> Только 100% факты')
content = content.replace('🏛️ Все 7 колен + Гипотезы', '<svg class="svg-icon sm"><use href="#icon-temple"/></svg> Все 7 колен + Гипотезы')
content = content.replace('🦁 Каретниковы', '<svg class="svg-icon sm"><use href="#icon-clan-karetnikov"/></svg> Каретниковы')
content = content.replace('🌾 Юхины', '<svg class="svg-icon sm"><use href="#icon-clan-yukhin"/></svg> Юхины')
content = content.replace('🛡️ Зубковы', '<svg class="svg-icon sm"><use href="#icon-clan-zubkov"/></svg> Зубковы')
content = content.replace('👑 Куманины', '<svg class="svg-icon sm"><use href="#icon-clan-kumanin"/></svg> Куманины')
content = content.replace('🪐 Гипотезы (15)', '<svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> Гипотезы (15)')
content = content.replace('title="Парящие гипотезы">🪐<', 'title="Парящие гипотезы"><svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg><')
content = content.replace('⚙️ Фильтры и поиск 2D-карты', '<svg class="svg-icon sm"><use href="#icon-settings"/></svg> Фильтры и поиск 2D-карты')
content = content.replace('🏛️ Полное Древо 7 Колен (130 ячеек)', '<svg class="svg-icon sm"><use href="#icon-temple"/></svg> Полное Древо 7 Колен (130 ячеек)')
content = content.replace('🟢 Подсветка 100% фактов', '<svg class="svg-icon sm"><use href="#icon-seal-confirmed"/></svg> Подсветка 100% фактов')
content = content.replace('title="Сфокусировать на мне (#1)">🎯 От меня (#1)', 'title="Сфокусировать на мне (#1)"><svg class="svg-icon sm"><use href="#icon-focus"/></svg> От меня (#1)')
content = content.replace('title="Показать всю карту целиком">🗺️ Весь масштаб', 'title="Показать всю карту целиком"><svg class="svg-icon sm"><use href="#icon-tree"/></svg> Весь масштаб')
content = content.replace('🌿 Присоединить свою семейную ветку в Большой Род', '<svg class="svg-icon sm"><use href="#icon-branch"/></svg> Присоединить свою семейную ветку в Большой Род')
content = content.replace('<span>👶 Сын / Дочь</span>', '<span><svg class="svg-icon sm"><use href="#icon-branch"/></svg> Сын / Дочь</span>')
content = content.replace('<span>💍 Супруг / Супруга</span>', '<span><svg class="svg-icon sm"><use href="#icon-kinship"/></svg> Супруг / Супруга</span>')

with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.write(content)

print("HTML part of index.astro upgraded successfully!")
