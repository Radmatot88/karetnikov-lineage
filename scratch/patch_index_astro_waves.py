import re

def patch_index_astro_waves():
    with open("src/pages/index.astro", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update topbar brand seal to allow dynamic SVG icon update
    old_seal = """<div class="brand-seal">
            <svg class="svg-icon seal-icon"><use href="#icon-shield-fortress"/></svg>
          </div>
          <div class="brand-text">
            <div class="brand-title">
              Каретников
              <span class="badge-role">Владелец архива</span>
            </div>"""

    new_seal = """<div class="brand-seal" id="topbarBrandSeal">
            <svg class="svg-icon seal-icon" id="topbarBrandIcon"><use href="#icon-shield-fortress"/></svg>
          </div>
          <div class="brand-text">
            <div class="brand-title">
              Каретников
              <span class="badge-role" id="topbarBrandBadge">Свод 4 Родов</span>
            </div>"""

    if old_seal in content:
        content = content.replace(old_seal, new_seal)
        print("Updated topbar brand seal!")

    # 2. Add Clan Switcher panel to roadmapHudTop
    hud_clan_panel = """          <!-- Гербовый Селектор 4 Домов (Four Houses Heraldic Selector) -->
          <div class="hud-panel clan-switcher-panel" style="pointer-events:auto;">
            <span style="font-size:11.5px; color:var(--text-muted); font-weight:700;">Гербовый Дом:</span>
            <div class="clan-switcher-bar" id="treeClanSwitcher">
              <button type="button" class="clan-theme-pill active" data-clan-theme="all" title="Свод всех четырех родов">
                <svg class="svg-icon sm"><use href="#icon-shield-fortress"/></svg> Все 4 рода
              </button>
              <button type="button" class="clan-theme-pill" data-clan-theme="karetnikov" title="Гербовый пурпур и золото Каретниковых">
                <svg class="svg-icon sm"><use href="#icon-clan-karetnikov"/></svg> Каретниковы
              </button>
              <button type="button" class="clan-theme-pill" data-clan-theme="kumanin" title="Лазурит и золото именитых граждан Куманиных">
                <svg class="svg-icon sm"><use href="#icon-clan-kumanin"/></svg> Куманины
              </button>
              <button type="button" class="clan-theme-pill" data-clan-theme="zubkov" title="Малахитовый изумруд фабрикантов Зубковых">
                <svg class="svg-icon sm"><use href="#icon-clan-zubkov"/></svg> Зубковы
              </button>
              <button type="button" class="clan-theme-pill" data-clan-theme="yukhin" title="Аметист и волжская медь старшин Юхиных">
                <svg class="svg-icon sm"><use href="#icon-clan-yukhin"/></svg> Юхины
              </button>
            </div>
          </div>
"""

    if '<!-- Эпистемический переключатель:' in content:
        content = content.replace('<!-- Эпистемический переключатель:', hud_clan_panel + '\n          <!-- Эпистемический переключатель:')
        print("Added Clan Switcher panel to 2D tree HUD!")

    # 3. Update scroll-clan-pills to include data-clan-theme attributes
    old_pills = """          <div class="scroll-clan-pills" id="scrollClanPills">
            <button type="button" class="scroll-clan-pill active" data-clan="all">Все 4 рода</button>
            <button type="button" class="scroll-clan-pill" data-clan="Каретниковы"><svg class="svg-icon sm"><use href="#icon-clan-karetnikov"/></svg> Каретниковы</button>
            <button type="button" class="scroll-clan-pill" data-clan="Юхины"><svg class="svg-icon sm"><use href="#icon-clan-yukhin"/></svg> Юхины</button>
            <button type="button" class="scroll-clan-pill" data-clan="Зубковы"><svg class="svg-icon sm"><use href="#icon-clan-zubkov"/></svg> Зубковы</button>
            <button type="button" class="scroll-clan-pill" data-clan="Куманины"><svg class="svg-icon sm"><use href="#icon-clan-kumanin"/></svg> Куманины</button>
            <button type="button" class="scroll-clan-pill" data-clan="hypotheses"><svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> Гипотезы (15)</button>
          </div>"""

    new_pills = """          <div class="scroll-clan-pills clan-switcher-bar" id="scrollClanPills">
            <button type="button" class="scroll-clan-pill clan-theme-pill active" data-clan="all" data-clan-theme="all">
              <svg class="svg-icon sm"><use href="#icon-shield-fortress"/></svg> Все 4 рода
            </button>
            <button type="button" class="scroll-clan-pill clan-theme-pill" data-clan="Каретниковы" data-clan-theme="karetnikov">
              <svg class="svg-icon sm"><use href="#icon-clan-karetnikov"/></svg> Каретниковы
            </button>
            <button type="button" class="scroll-clan-pill clan-theme-pill" data-clan="Куманины" data-clan-theme="kumanin">
              <svg class="svg-icon sm"><use href="#icon-clan-kumanin"/></svg> Куманины
            </button>
            <button type="button" class="scroll-clan-pill clan-theme-pill" data-clan="Зубковы" data-clan-theme="zubkov">
              <svg class="svg-icon sm"><use href="#icon-clan-zubkov"/></svg> Зубковы
            </button>
            <button type="button" class="scroll-clan-pill clan-theme-pill" data-clan="Юхины" data-clan-theme="yukhin">
              <svg class="svg-icon sm"><use href="#icon-clan-yukhin"/></svg> Юхины
            </button>
            <button type="button" class="scroll-clan-pill clan-theme-pill" data-clan="hypotheses" data-clan-theme="hypotheses">
              <svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> Гипотезы (15)
            </button>
          </div>"""

    if old_pills in content:
        content = content.replace(old_pills, new_pills)
        print("Updated scroll-clan-pills with heraldic theme attributes!")

    # 4. In renderRoadmapCanvas: Add generation pill to card top bar for Generations II-VII
    old_card_top = """            <article
              class="${cardClasses}"
              style="left:${box.x}px; top:${box.y}px; width:${box.w}px; ${searchHighlightStyle}"
              data-ahnentafel="${node.ahnentafel}"
            >
              <div class="rm-card-top-bar">
                <span class="ahnentafel-badge">${node.is_collateral ? `Брат #${node.sibling_of_ahnentafel}` : `Слот #${node.ahnentafel}`}</span>
                ${factBadge}
                <span class="branch-tag ${node.branch}">${branchLabel}</span>
              </div>"""

    new_card_top = """            <article
              class="${cardClasses}"
              style="left:${box.x}px; top:${box.y}px; width:${box.w}px; ${searchHighlightStyle}"
              data-ahnentafel="${node.ahnentafel}"
              data-node-clan="${node.sub_clan || node.clan || ''}"
            >
              <div class="rm-card-top-bar">
                <div style="display:flex; align-items:center; gap:5px;">
                  <span class="rm-gen-pill">${romanNumerals[node.generation]} КОЛЕНО</span>
                  <span class="ahnentafel-badge">${node.is_collateral ? `Брат #${node.sibling_of_ahnentafel}` : `Слот #${node.ahnentafel}`}</span>
                </div>
                <div style="display:flex; align-items:center; gap:5px;">
                  ${factBadge}
                  <span class="branch-tag ${node.branch}">${branchLabel}</span>
                </div>
              </div>"""

    if old_card_top in content:
        content = content.replace(old_card_top, new_card_top)
        print("Updated card top bar with explicit Generation Pill!")

    # 5. Add setHeraldicClanTheme and highlightClanOnTree JS functions
    js_heraldic_engine = """
    // ================= DYNAMIC 4-CLAN HERALDIC THEME ENGINE =================
    let currentHeraldicTheme = 'all';

    function setHeraldicClanTheme(themeName) {
      if (!themeName) themeName = 'all';
      currentHeraldicTheme = themeName;
      document.documentElement.setAttribute('data-clan-theme', themeName);
      document.body.setAttribute('data-clan-theme', themeName);
      try { localStorage.setItem('karetnikov_clan_theme', themeName); } catch(e){}

      // Sync active pills across both Scroll and Tree views
      document.querySelectorAll('.clan-theme-pill').forEach(pill => {
        const pTheme = pill.getAttribute('data-clan-theme');
        pill.classList.toggle('active', pTheme === themeName);
      });

      // Update Topbar Brand Seal
      const iconMap = {
        all: '#icon-shield-fortress',
        karetnikov: '#icon-clan-karetnikov',
        kumanin: '#icon-clan-kumanin',
        zubkov: '#icon-clan-zubkov',
        yukhin: '#icon-clan-yukhin',
        hypotheses: '#icon-orbit-hypothesis'
      };
      const titleMap = {
        all: 'Свод 4 Родов',
        karetnikov: 'Род Каретниковых',
        kumanin: 'Род Куманиных',
        zubkov: 'Род Зубковых',
        yukhin: 'Род Юхиных',
        hypotheses: 'Парящие Гипотезы'
      };

      const iconUse = document.querySelector('#topbarBrandIcon use');
      if (iconUse && iconMap[themeName]) {
        iconUse.setAttribute('href', iconMap[themeName]);
      }
      const badgeEl = document.getElementById('topbarBrandBadge');
      if (badgeEl && titleMap[themeName]) {
        badgeEl.textContent = titleMap[themeName];
      }

      // Highlight matching nodes on 2D Tree Roadmap
      highlightClanOnTree(themeName);
    }

    function highlightClanOnTree(themeName) {
      const clanMap = {
        karetnikov: 'Каретниковы',
        kumanin: 'Куманины',
        zubkov: 'Зубковы',
        yukhin: 'Юхины'
      };
      const targetClan = clanMap[themeName];

      document.querySelectorAll('#roadmapNodesLayer .rm-node:not(.floating-hypothesis-node)').forEach(card => {
        const ahn = parseInt(card.getAttribute('data-ahnentafel') || '0', 10);
        if (ahn === 1 || !targetClan) {
          // Proband is always visible at 100%
          card.style.opacity = '1';
          card.style.filter = '';
          return;
        }
        const cardClan = card.getAttribute('data-node-clan') || '';
        if (cardClan.includes(targetClan)) {
          card.style.opacity = '1';
          card.style.filter = 'drop-shadow(0 0 12px var(--theme-glow))';
        } else {
          card.style.opacity = '0.42';
          card.style.filter = 'grayscale(35%)';
        }
      });
    }

    function initHeraldicThemeEngine() {
      let savedTheme = 'all';
      try {
        savedTheme = localStorage.getItem('karetnikov_clan_theme') || 'all';
      } catch(e){}

      // Attach event listeners to all clan switcher pills in Scroll and Tree HUD
      document.querySelectorAll('.clan-theme-pill').forEach(pill => {
        pill.addEventListener('click', (ev) => {
          const theme = pill.getAttribute('data-clan-theme') || 'all';
          setHeraldicClanTheme(theme);

          // If in scroll view, also sync scroll filter
          const clanFilterVal = pill.getAttribute('data-clan');
          if (clanFilterVal && typeof scrollClanFilter !== 'undefined') {
            scrollClanFilter = clanFilterVal;
            if (lineageData) renderMobileScroll(lineageData);
          }
        });
      });

      setHeraldicClanTheme(savedTheme);
    }
"""

    if 'function initFontScaling()' in content:
        content = content.replace('function initFontScaling()', js_heraldic_engine + '\n    function initFontScaling()')
        print("Injected Heraldic Theme Engine JavaScript!")

    # In window load / DOMContentLoaded: call initHeraldicThemeEngine
    if 'initFontScaling();' in content:
        content = content.replace('initFontScaling();', 'initFontScaling(); initHeraldicThemeEngine();')
        print("Attached initHeraldicThemeEngine to lifecycle!")

    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.astro patched with Waves 2 & 3 successfully!")
    return True

if __name__ == "__main__":
    patch_index_astro_waves()
