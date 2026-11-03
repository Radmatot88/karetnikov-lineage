#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrades src/pages/index.astro with:
1. Native Mobile Generation Scroll View (#view-scroll) with Smart Kinship Path Breadcrumb,
   1-Tap Kinship Jump Chips, Epistemic Mode Switch (19 Facts vs All 7 Generations),
   Clan Filter Pills, Quick Generation Jump Bar (I..VII), and 2D Map Focus bridge.
2. Fixed Mobile Bottom Tab Bar (.mobile-bottom-nav) for iOS/Android ergonomics.
3. Multi-Touch 1-finger Pan & 2-finger Pinch-to-Zoom on the 2D Roadmap Canvas.
4. Mobile Bottom Sheet Dossier enhancements (Fact Certificate + 12 Rubrics Accordion).
5. Relative fetch path './vault/lineage_payload.enc.json' for GitHub Pages compatibility.
"""

from pathlib import Path

astro_path = Path(r"c:\Karetnikov_Lineage\src\pages\index.astro")
html = astro_path.read_text(encoding="utf-8")

# 1. Upgrade viewport & PWA meta tags
old_meta = '<meta name="viewport" content="width=device-width, initial-scale=1.0" />'
new_meta = (
    '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />\n'
    '  <meta name="theme-color" content="#07090e" />\n'
    '  <meta name="apple-mobile-web-app-capable" content="yes" />\n'
    '  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />'
)
assert old_meta in html, "Could not find viewport meta tag"
html = html.replace(old_meta, new_meta, 1)

# 2. Add Mobile Scroll Tab in .nav-tabs
old_nav_tabs = """      <nav class="nav-tabs" aria-label="Режимы отображения">
        <button class="nav-tab active" data-view="tree">1. Дорожная Карта Древа (Pan & Zoom)</button>
        <button class="nav-tab" data-view="fan">2. Круговой Веер 127 Предков</button>
        <button class="nav-tab" data-view="radar">3. Архивный Радар (Шуструй • Плешаново • Кошки)</button>
        <button class="nav-tab" id="tabNavAccess" data-view="access">4. Пульт Доступов & Playwright</button>
      </nav>"""

new_nav_tabs = """      <nav class="nav-tabs" aria-label="Режимы отображения">
        <button class="nav-tab" data-view="scroll">📱 Свиток Поколений (Умная Навигация)</button>
        <button class="nav-tab active" data-view="tree">🗺️ 2D-Карта Древа (Pan & Zoom)</button>
        <button class="nav-tab" data-view="fan">🎡 Круговой Веер 127</button>
        <button class="nav-tab" data-view="radar">📡 Архивный Радар</button>
        <button class="nav-tab" id="tabNavAccess" data-view="access">🔐 Пульт Доступов</button>
      </nav>"""
assert old_nav_tabs in html, "Could not find .nav-tabs block"
html = html.replace(old_nav_tabs, new_nav_tabs, 1)

# 3. Insert VIEW 0 (#view-scroll) and Mobile HUD Toggle inside #view-tree
old_view1_start = """    <!-- VIEW 1: INFINITE PAN & ZOOM ROADMAP TREE CANVAS -->
    <main id="view-tree" class="view-section active">
      <div id="roadmapShell" class="roadmap-shell">
        <!-- Floating Top HUD -->
        <div class="roadmap-hud-top">"""

new_view0_and_view1_start = """    <!-- VIEW 0: NATIVE MOBILE GENERATION SCROLL APP (I -> VII) -->
    <section id="view-scroll" class="view-section">
      <div class="scroll-app-container">
        <!-- Sticky Native App Header -->
        <div class="scroll-sticky-header">
          <!-- Smart Kinship Bloodline Breadcrumb -->
          <div id="kinshipPathBar" class="kinship-path-bar">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span class="kinship-path-title">🧬 Умный навигатор прямого родства (от #1)</span>
              <button type="button" id="resetKinshipPathBtn" class="scroll-act-btn" style="padding:2px 8px; font-size:10.5px;">Сброс</button>
            </div>
            <div id="kinshipPathSteps" class="kinship-path-steps"></div>
          </div>

          <!-- Search Input + Counter -->
          <div class="scroll-search-row">
            <div class="scroll-search-wrap">
              <span class="scroll-search-icon">🔍</span>
              <input
                id="scrollSearchInput"
                type="search"
                class="scroll-search-input"
                placeholder="ФИО, девичья фамилия, село (Шуструй, Плешаново)..."
              />
            </div>
            <button type="button" id="scrollClearSearchBtn" class="scroll-act-btn" style="display:none; padding:8px 12px;">✕</button>
          </div>

          <!-- Epistemic Mode Segmented Control (100% Facts vs Full 7 Gen) -->
          <div class="scroll-mode-switch" role="radiogroup" aria-label="Режим достоверности свитка">
            <button type="button" id="scrollModeFactsBtn" class="scroll-mode-btn active-facts" data-scroll-mode="facts_only">
              <span>🟢 Только 100% факты</span>
              <span class="badge-count" id="scrollFactsCountBadge">19</span>
            </button>
            <button type="button" id="scrollModeAllBtn" class="scroll-mode-btn" data-scroll-mode="all_levels">
              <span>🏛️ Все 7 колен + Гипотезы</span>
              <span class="badge-count" id="scrollAllCountBadge">152</span>
            </button>
          </div>

          <!-- 4 Clans Filter Bar -->
          <div class="scroll-clan-pills" id="scrollClanPills">
            <button type="button" class="scroll-clan-pill active" data-clan="all">Все 4 рода</button>
            <button type="button" class="scroll-clan-pill" data-clan="Каретниковы">🦁 Каретниковы</button>
            <button type="button" class="scroll-clan-pill" data-clan="Юхины">🌾 Юхины</button>
            <button type="button" class="scroll-clan-pill" data-clan="Зубковы">🛡️ Зубковы</button>
            <button type="button" class="scroll-clan-pill" data-clan="Куманины">👑 Куманины</button>
            <button type="button" class="scroll-clan-pill" data-clan="hypotheses">🪐 Гипотезы (15)</button>
          </div>

          <!-- Quick Generation Jump Bar (I -> VII) -->
          <div class="scroll-gen-jumpbar" id="scrollGenJumpbar">
            <span class="jumpbar-label">Колено:</span>
            <button type="button" class="gen-jump-btn active" data-gen-jump="1">I</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="2">II</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="3">III</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="4">IV</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="5">V</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="6">VI</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="7">VII</button>
            <button type="button" class="gen-jump-btn" data-gen-jump="hyp" title="Парящие гипотезы">🪐</button>
          </div>
        </div>

        <!-- Dynamic Generations & Ancestor Cards List -->
        <div id="scrollGenerationsList"></div>
      </div>
    </section>

    <!-- VIEW 1: INFINITE PAN & ZOOM ROADMAP TREE CANVAS -->
    <main id="view-tree" class="view-section active">
      <div id="roadmapShell" class="roadmap-shell">
        <button type="button" id="mobileHudToggleBtn" class="mobile-hud-toggle-btn">
          ⚙️ Фильтры и поиск 2D-карты
        </button>
        <!-- Floating Top HUD -->
        <div id="roadmapHudTop" class="roadmap-hud-top">"""

assert old_view1_start in html, "Could not find VIEW 1 start"
html = html.replace(old_view1_start, new_view0_and_view1_start, 1)

# 4. Insert Fixed Mobile Bottom Navigation Bar right before closing #workspace
old_workspace_end = """      <div id="accessGuideGrid" class="cards-grid"></div>
    </section>
  </div>"""

new_workspace_end = """      <div id="accessGuideGrid" class="cards-grid"></div>
    </section>

    <!-- NATIVE MOBILE BOTTOM NAVIGATION BAR (iOS / Android Ergonomics) -->
    <nav id="mobileBottomNav" class="mobile-bottom-nav" aria-label="Мобильная навигация">
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
    </nav>
  </div>"""

assert old_workspace_end in html, "Could not find #workspace end"
html = html.replace(old_workspace_end, new_workspace_end, 1)

# 5. Update CONFIRMED_FACT_AHNENTAFELS and loadEncryptedBundle()
old_facts_and_fetch = """    // List of 100% verified fact Ahnentafels
    const CONFIRMED_FACT_AHNENTAFELS = new Set([
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24, 28
    ]);

    // Pan & Zoom State for Roadmap Canvas
    let panX = 60;
    let panY = 80;
    let zoom = 0.85;
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;

    function applyRoadmapTransform() {
      const world = document.getElementById('roadmapWorld');
      const readout = document.getElementById('zoomReadout');
      if (world) {
        world.style.transform = `translate3d(${panX}px, ${panY}px, 0) scale(${zoom})`;
      }
      if (readout) {
        readout.textContent = `${Math.round(zoom * 100)}%`;
      }
    }

    function b64ToBytes(b64) {
      const bin = atob(b64);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      return bytes;
    }

    async function loadEncryptedBundle() {
      const res = await fetch('/vault/lineage_payload.enc.json', { cache: 'no-store' });
      if (!res.ok) throw new Error('Не удалось загрузить зашифрованный контейнер родословной');
      encryptedBundle = await res.json();
    }"""

new_facts_and_fetch = """    // Exact 19 verified fact Ahnentafels (11 direct + 8 collateral)
    const CONFIRMED_FACT_AHNENTAFELS = new Set([
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14,
      301, 401, 402, 4011, 4012, 701, 702, 801
    ]);

    // Mobile Scroll State
    let scrollEpistemicMode = 'facts_only'; // 'facts_only' | 'all_levels'
    let scrollClanFilter = 'all';
    let scrollSearchQuery = '';
    let selectedKinshipAhn = null;

    // Pan & Zoom State for Roadmap Canvas
    let panX = 60;
    let panY = 80;
    let zoom = 0.85;
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;

    function applyRoadmapTransform() {
      const world = document.getElementById('roadmapWorld');
      const readout = document.getElementById('zoomReadout');
      if (world) {
        world.style.transform = `translate3d(${panX}px, ${panY}px, 0) scale(${zoom})`;
      }
      if (readout) {
        readout.textContent = `${Math.round(zoom * 100)}%`;
      }
    }

    function b64ToBytes(b64) {
      const bin = atob(b64);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      return bytes;
    }

    async function loadEncryptedBundle() {
      const candidateUrls = [
        './vault/lineage_payload.enc.json',
        '/vault/lineage_payload.enc.json'
      ];
      for (const url of candidateUrls) {
        try {
          const res = await fetch(url, { cache: 'no-store' });
          if (res.ok) {
            encryptedBundle = await res.json();
            return;
          }
        } catch {}
      }
      throw new Error('Не удалось загрузить зашифрованный контейнер родословной');
    }"""

assert old_facts_and_fetch in html, "Could not find CONFIRMED_FACT_AHNENTAFELS and loadEncryptedBundle"
html = html.replace(old_facts_and_fetch, new_facts_and_fetch, 1)

# 6. Update photo upload callback to also re-render Mobile Scroll
old_photo_cb = """          if (lineageData) {
            renderRoadmapCanvas(lineageData);
            const allNodes = [...lineageData.nodes, ...(lineageData.collateral_nodes || [])];"""

new_photo_cb = """          if (lineageData) {
            renderRoadmapCanvas(lineageData);
            renderMobileScroll(lineageData);
            const allNodes = [...lineageData.nodes, ...(lineageData.collateral_nodes || [])];"""

assert old_photo_cb in html, "Could not find photo upload callback"
html = html.replace(old_photo_cb, new_photo_cb, 1)

# 7. Update setEpistemicMode to also sync with Mobile Scroll
old_set_epistemic = """      if (lineageData) {
        renderRoadmapCanvas(lineageData);
        renderFanChart(lineageData);
      }
    }"""

new_set_epistemic = """      scrollEpistemicMode = mode;
      syncScrollModeButtons();
      if (lineageData) {
        renderRoadmapCanvas(lineageData);
        renderFanChart(lineageData);
        renderMobileScroll(lineageData);
      }
    }

    function syncScrollModeButtons() {
      const fBtn = document.getElementById('scrollModeFactsBtn');
      const aBtn = document.getElementById('scrollModeAllBtn');
      if (!fBtn || !aBtn) return;
      fBtn.className = scrollEpistemicMode === 'facts_only' ? 'scroll-mode-btn active-facts' : 'scroll-mode-btn';
      aBtn.className = scrollEpistemicMode === 'all_levels' ? 'scroll-mode-btn active-all' : 'scroll-mode-btn';
    }"""

assert old_set_epistemic in html, "Could not find setEpistemicMode end"
html = html.replace(old_set_epistemic, new_set_epistemic, 1)

# 8. Upgrade initCanvasPanZoom() with Multi-Touch (1-finger pan + 2-finger pinch-to-zoom) and focusNodeOn2DCanvas + renderMobileScroll
old_panzoom_block = """    // Setup Mouse Drag & Wheel Zoom on #roadmapShell
    (function initCanvasPanZoom() {
      const shell = document.getElementById('roadmapShell');
      if (!shell) return;

      shell.addEventListener('mousedown', (e) => {
        if (e.target.closest('.hud-panel') || e.target.closest('.roadmap-zoom-dock') || e.target.closest('.rm-node')) {
          return;
        }
        isDragging = true;
        dragStartX = e.clientX - panX;
        dragStartY = e.clientY - panY;
        shell.classList.add('dragging');
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        panX = e.clientX - dragStartX;
        panY = e.clientY - dragStartY;
        applyRoadmapTransform();
      });

      window.addEventListener('mouseup', () => {
        isDragging = false;
        shell.classList.remove('dragging');
      });

      shell.addEventListener('wheel', (e) => {
        e.preventDefault();
        const rect = shell.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const prevZoom = zoom;
        const delta = e.deltaY < 0 ? 1.12 : 0.89;
        zoom = Math.min(2.2, Math.max(0.12, zoom * delta));

        panX = mouseX - ((mouseX - panX) * (zoom / prevZoom));
        panY = mouseY - ((mouseY - panY) * (zoom / prevZoom));
        applyRoadmapTransform();
      }, { passive: false });

      document.getElementById('zoomInBtn').addEventListener('click', () => {
        zoom = Math.min(2.2, zoom * 1.2);
        applyRoadmapTransform();
      });
      document.getElementById('zoomOutBtn').addEventListener('click', () => {
        zoom = Math.max(0.12, zoom * 0.82);
        applyRoadmapTransform();
      });
      document.getElementById('zoomResetBtn').addEventListener('click', focusOnProband);
      document.getElementById('zoomFitBtn').addEventListener('click', fitEntireRoadmap);
    })();"""

new_panzoom_and_mobile_scroll_block = """    // Focus camera on any specific node on the 2D Roadmap Canvas
    function focusNodeOn2DCanvas(ahnentafelNum) {
      switchView('tree');
      setTimeout(() => {
        const shell = document.getElementById('roadmapShell');
        const targetCard = document.querySelector(`.rm-node[data-ahnentafel="${ahnentafelNum}"]`);
        if (!shell || !targetCard) {
          focusOnProband();
          return;
        }
        const cardX = parseFloat(targetCard.style.left || '80');
        const cardY = parseFloat(targetCard.style.top || '450');
        zoom = window.innerWidth <= 860 ? 0.72 : 0.92;
        panX = (shell.clientWidth / 2) - ((cardX + 155) * zoom);
        panY = (shell.clientHeight / 2) - ((cardY + 54) * zoom);
        applyRoadmapTransform();
        targetCard.style.outline = '3px solid #10b981';
        targetCard.style.boxShadow = '0 0 35px rgba(16, 185, 129, 0.85)';
        setTimeout(() => {
          targetCard.style.outline = '';
          targetCard.style.boxShadow = '';
        }, 2600);
      }, 80);
    }

    // ================= NATIVE MOBILE GENERATION SCROLL ENGINE =================
    function buildKinshipChain(targetAhn, allNodes) {
      const nodeMap = {};
      allNodes.forEach(n => { nodeMap[n.ahnentafel] = n; });
      const target = nodeMap[targetAhn];
      if (!target) return [];

      // If collateral, start from its sibling or parent in direct tree
      const chain = [];
      if (target.is_collateral) {
        chain.unshift(target);
        let currAhn = target.sibling_of_ahnentafel || target.parent_ahnentafel || 1;
        while (currAhn >= 1) {
          const n = nodeMap[currAhn];
          if (n) chain.unshift(n);
          if (currAhn === 1) break;
          currAhn = Math.floor(currAhn / 2);
        }
        return chain;
      }

      let curr = targetAhn;
      while (curr >= 1) {
        const n = nodeMap[curr];
        if (n) chain.unshift(n);
        if (curr === 1) break;
        curr = Math.floor(curr / 2);
      }
      return chain;
    }

    function updateKinshipBreadcrumb(targetAhn) {
      const bar = document.getElementById('kinshipPathBar');
      const stepsEl = document.getElementById('kinshipPathSteps');
      if (!bar || !stepsEl || !lineageData) return;

      if (!targetAhn || targetAhn === 1) {
        selectedKinshipAhn = null;
        bar.classList.remove('visible');
        return;
      }

      selectedKinshipAhn = targetAhn;
      const allNodes = [...(lineageData.nodes || []), ...(lineageData.collateral_nodes || [])];
      const chain = buildKinshipChain(targetAhn, allNodes);
      if (chain.length <= 1) {
        bar.classList.remove('visible');
        return;
      }

      bar.classList.add('visible');
      stepsEl.innerHTML = chain.map((n, idx) => {
        const shortName = `${n.surname || ''} ${n.first_name || ''}`.trim() || `Слот #${n.ahnentafel}`;
        const isLast = idx === chain.length - 1;
        const stepHtml = `
          <span class="kinship-step ${isLast ? 'active-target' : ''}" data-kinship-jump="${n.ahnentafel}" style="cursor:pointer;">
            #${n.ahnentafel} ${shortName}
          </span>
        `;
        return idx < chain.length - 1
          ? `${stepHtml}<span class="kinship-arrow">➔</span>`
          : stepHtml;
      }).join('');

      stepsEl.querySelectorAll('[data-kinship-jump]').forEach(el => {
        el.addEventListener('click', () => {
          const jumpAhn = parseInt(el.getAttribute('data-kinship-jump'), 10);
          scrollToPersonInScroll(jumpAhn);
        });
      });
    }

    function scrollToPersonInScroll(ahnentafelNum) {
      if (!lineageData) return;
      const isFact = CONFIRMED_FACT_AHNENTAFELS.has(ahnentafelNum);
      if (!isFact && scrollEpistemicMode === 'facts_only') {
        scrollEpistemicMode = 'all_levels';
        syncScrollModeButtons();
        renderMobileScroll(lineageData);
      }
      if (scrollClanFilter !== 'all') {
        scrollClanFilter = 'all';
        document.querySelectorAll('#scrollClanPills .scroll-clan-pill').forEach(p => {
          p.classList.toggle('active', p.getAttribute('data-clan') === 'all');
        });
        renderMobileScroll(lineageData);
      }

      updateKinshipBreadcrumb(ahnentafelNum);

      setTimeout(() => {
        const card = document.querySelector(`#scrollGenerationsList .scroll-person-card[data-scroll-ahn="${ahnentafelNum}"]`);
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
          card.classList.remove('highlight-target');
          void card.offsetWidth;
          card.classList.add('highlight-target');
        }
      }, 60);
    }

    function renderMobileScroll(data) {
      const container = document.getElementById('scrollGenerationsList');
      if (!container || !data) return;

      const allDirect = data.nodes || [];
      const allCollateral = data.collateral_nodes || [];
      const allHypotheses = data.floating_hypotheses || [];
      const allCombined = [...allDirect, ...allCollateral];

      const nodeByAhn = {};
      allCombined.forEach(n => { nodeByAhn[n.ahnentafel] = n; });

      // Update counters
      const factsCountEl = document.getElementById('scrollFactsCountBadge');
      const allCountEl = document.getElementById('scrollAllCountBadge');
      const totalFactsCount = allCombined.filter(n => CONFIRMED_FACT_AHNENTAFELS.has(n.ahnentafel) || n.is_fact_confirmed || n.is_relative_proposal).length;
      if (factsCountEl) factsCountEl.textContent = String(totalFactsCount);
      if (allCountEl) allCountEl.textContent = String(allCombined.length + allHypotheses.length);

      const q = scrollSearchQuery.trim().toLowerCase();

      function matchesScrollFilters(node) {
        const isFact = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed || node.is_relative_proposal;
        if (scrollEpistemicMode === 'facts_only' && !isFact) return false;
        if (scrollClanFilter === 'hypotheses') return false;
        if (scrollClanFilter !== 'all') {
          const clanStr = (node.sub_clan || '').toLowerCase();
          if (!clanStr.includes(scrollClanFilter.toLowerCase())) return false;
        }
        if (q) {
          const hay = `${node.full_name || ''} ${node.birth_place || ''} ${node.sub_clan || ''} ${node.role_label || ''} ${node.notes || ''} #${node.ahnentafel}`.toLowerCase();
          if (!hay.includes(q)) return false;
        }
        return true;
      }

      const genMeta = {
        1: { roman: 'I', title: 'I Колено • Пробанд (Я)', era: '1994 г.р. — Наше время' },
        2: { roman: 'II', title: 'II Колено • Родители и родной брат', era: '1960–1991 гг.' },
        3: { roman: 'III', title: 'III Колено • Дедушки, бабушки и их братья/сёстры', era: '1925–1946 гг.' },
        4: { roman: 'IV', title: 'IV Колено • Прадеды и прабабушки', era: '1895–1918 гг. • Мост через 1917 год' },
        5: { roman: 'V', title: 'V Колено • Прапрадеды (Перепись 1917 г.)', era: '1865–1895 гг.' },
        6: { roman: 'VI', title: 'VI Колено • Прапрапрадеды (X Ревизия 1858 г.)', era: '1830–1865 гг.' },
        7: { roman: 'VII', title: 'VII Колено • Корни рода (Ревизии 1795–1834 гг.)', era: '1795–1835 гг.' }
      };

      let htmlSections = [];

      if (scrollClanFilter !== 'hypotheses') {
        for (let g = 1; g <= 7; g++) {
          const directInGen = allDirect.filter(n => n.generation === g && matchesScrollFilters(n));
          const collatInGen = allCollateral.filter(c => c.generation === g && matchesScrollFilters(c));
          const list = [...directInGen, ...collatInGen];
          if (list.length === 0) continue;

          const meta = genMeta[g];
          const cardsHtml = list.map(node => {
            const isFact = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
            const photoSrc = getNodePhoto(node);
            const portraitHtml = photoSrc
              ? `<img src="${photoSrc}" alt="${node.full_name}" />`
              : `<div class="rm-portrait-placeholder" style="font-size:18px;">${getInitials(node)}</div>`;

            const burialPlace = burialMap[node.id] || node.burial_place || '';
            const deathStr = node.death_date ? ` — ${node.death_date}` : '';

            // Build 1-Tap Kinship Navigation Pills
            const navPills = [];
            const fatherAhn = node.father_ahnentafel || node.parent_ahnentafel;
            const motherAhn = node.mother_ahnentafel;
            const childAhn = node.child_ahnentafel || (!node.is_collateral && node.ahnentafel > 1 ? Math.floor(node.ahnentafel / 2) : null);

            if (childAhn && nodeByAhn[childAhn]) {
              const ch = nodeByAhn[childAhn];
              navPills.push(`
                <button type="button" class="kinship-pill" data-scroll-jump="${ch.ahnentafel}">
                  ⬇ Потомок: <span class="kp-name">${ch.first_name || '#' + ch.ahnentafel}</span>
                </button>
              `);
            }
            if (node.is_collateral && node.sibling_of_ahnentafel && nodeByAhn[node.sibling_of_ahnentafel]) {
              const sib = nodeByAhn[node.sibling_of_ahnentafel];
              navPills.push(`
                <button type="button" class="kinship-pill" data-scroll-jump="${sib.ahnentafel}">
                  ↔ Брат/Сестра: <span class="kp-name">${sib.first_name || '#' + sib.ahnentafel}</span>
                </button>
              `);
            }
            // Also find collateral siblings attached to this direct node
            if (!node.is_collateral) {
              const mySibs = allCollateral.filter(c => c.sibling_of_ahnentafel === node.ahnentafel);
              mySibs.forEach(s => {
                navPills.push(`
                  <button type="button" class="kinship-pill" data-scroll-jump="${s.ahnentafel}">
                    ↔ ${s.gender === 'F' ? 'Сестра' : 'Брат'}: <span class="kp-name">${s.first_name || s.full_name}</span>
                  </button>
                `);
              });
            }
            if (fatherAhn && nodeByAhn[fatherAhn] && nodeByAhn[fatherAhn].status !== 'UNKNOWN_SLOT') {
              const fa = nodeByAhn[fatherAhn];
              navPills.push(`
                <button type="button" class="kinship-pill" data-scroll-jump="${fa.ahnentafel}">
                  ⬆ Отец: <span class="kp-name">${fa.first_name || '#' + fa.ahnentafel}</span>
                </button>
              `);
            }
            if (motherAhn && nodeByAhn[motherAhn] && nodeByAhn[motherAhn].status !== 'UNKNOWN_SLOT') {
              const mo = nodeByAhn[motherAhn];
              navPills.push(`
                <button type="button" class="kinship-pill" data-scroll-jump="${mo.ahnentafel}">
                  ⬆ Мать: <span class="kp-name">${mo.first_name || '#' + mo.ahnentafel}</span>
                </button>
              `);
            }

            const baseQuorum = node.status === 'CONFIRMED_DOC' ? 2 : 1;
            const totalQuorum = baseQuorum + (quorumMap[node.id] || 0);
            const userConfirmed = Boolean(quorumMap[node.id + '_user']);
            const memCount = (memoriesMap[node.id] || []).length;

            const statusBadgeHtml = isFact
              ? `<span class="badge-fact-100">🟢 100% ФАКТ</span>`
              : node.status === 'FAMILY_ORAL'
                ? `<span class="ahnentafel-badge" style="color:#38bdf8;">🔵 ПРЕДАНИЕ</span>`
                : node.status === 'ARCHIVE_CANDIDATE'
                  ? `<span class="ahnentafel-badge" style="color:#fbbf24;">🟠 КАНДИДАТ</span>`
                  : `<span class="ahnentafel-badge" style="color:#64748b;">⚪ ПОИСК</span>`;

            return `
              <article
                class="scroll-person-card branch-${node.branch || 'paternal'} ${isFact ? 'is-fact-card' : ''}"
                data-scroll-ahn="${node.ahnentafel}"
              >
                <div class="scroll-card-top">
                  <div class="scroll-avatar" data-scroll-photo="${node.id}" title="Нажмите, чтобы загрузить фотографию">
                    ${portraitHtml}
                    <span class="scroll-avatar-cam">📷 Фото</span>
                  </div>
                  <div class="scroll-person-main">
                    <div class="scroll-badges-row">
                      <span class="ahnentafel-badge">${node.is_collateral ? 'Боковая ветвь' : 'Слот #' + node.ahnentafel}</span>
                      ${statusBadgeHtml}
                      <span class="branch-tag ${node.branch}">${node.sub_clan || ''}</span>
                    </div>
                    <div class="scroll-person-name" data-open-dossier="${node.ahnentafel}" style="cursor:pointer;">
                      ${node.full_name}
                    </div>
                    <div class="scroll-person-role">${node.role_label || ''}</div>
                    <div class="scroll-person-meta">
                      <span>📅 ${node.birth_date || 'Дата уточняется'}${deathStr}</span>
                      ${node.birth_place ? `<span>📍 ${node.birth_place}</span>` : ''}
                      ${burialPlace ? `<span>🪦 ${burialPlace}</span>` : ''}
                    </div>
                  </div>
                </div>

                ${node.notes && node.status !== 'UNKNOWN_SLOT' ? `
                  <div class="scroll-person-bio">${node.notes}</div>
                ` : ''}

                ${navPills.length > 0 ? `
                  <div class="scroll-kinship-pills">
                    ${navPills.join('')}
                  </div>
                ` : ''}

                <div class="scroll-card-actions">
                  <button type="button" class="scroll-act-btn primary-act" data-open-dossier="${node.ahnentafel}">
                    📜 Досье и 12 рубрик ${memCount > 0 ? `(${memCount})` : ''}
                  </button>
                  <button type="button" class="scroll-act-btn" data-show-kinship="${node.ahnentafel}" title="Показать прямую цепь родства от #1">
                    🧬 Линия родства
                  </button>
                  <button type="button" class="scroll-act-btn" data-focus-2d="${node.ahnentafel}" title="Показать эту ячейку на 2D-карте">
                    🗺️ На 2D-карте
                  </button>
                  <button type="button" class="scroll-act-btn ${userConfirmed ? 'primary-act' : ''}" data-quick-quorum="${node.id}" data-quorum-ahn="${node.ahnentafel}">
                    ${userConfirmed ? '✅ Подтв.' : '✋ Подтвердить'} (+${totalQuorum})
                  </button>
                </div>
              </article>
            `;
          }).join('');

          htmlSections.push(`
            <div class="scroll-gen-section" id="scroll-gen-${g}">
              <div class="scroll-gen-header">
                <div class="scroll-gen-title">
                  <span class="gen-roman-badge">${meta.roman}</span>
                  <div>
                    <div>${meta.title}</div>
                    <div style="font-size:11px; color:var(--text-muted); font-weight:500;">${meta.era}</div>
                  </div>
                </div>
                <span class="scroll-gen-stats">${list.length} перс.</span>
              </div>
              ${cardsHtml}
            </div>
          `);
        }
      }

      // Render Floating Hypotheses Section if in all_levels or hypotheses filter
      if (scrollEpistemicMode === 'all_levels' || scrollClanFilter === 'hypotheses') {
        const filteredHyps = allHypotheses.filter(h => {
          if (scrollClanFilter !== 'all' && scrollClanFilter !== 'hypotheses') {
            if (!(h.clan || '').toLowerCase().includes(scrollClanFilter.toLowerCase())) return false;
          }
          if (q) {
            const hay = `${h.full_name} ${h.village} ${h.role_badge} ${h.relationship_hypothesis}`.toLowerCase();
            if (!hay.includes(q)) return false;
          }
          return true;
        });

        if (filteredHyps.length > 0) {
          const hypCardsHtml = filteredHyps.map(hyp => `
            <article class="scroll-person-card is-hyp-card" data-scroll-hyp="${hyp.id}">
              <div class="scroll-card-top">
                <div class="scroll-avatar" style="border-color:#f59e0b; color:#fbbf24; font-size:22px;">🪐</div>
                <div class="scroll-person-main">
                  <div class="scroll-badges-row">
                    <span class="badge-floating-hyp">ГИПОТЕЗА • ${hyp.confidence}%</span>
                    <span class="ahnentafel-badge">${hyp.generation_label || ''}</span>
                  </div>
                  <div class="scroll-person-name" style="color:#fef3c7;">${hyp.full_name}</div>
                  <div class="scroll-person-role" style="color:#fbbf24;">${hyp.role_badge || ''}</div>
                  <div class="scroll-person-meta">
                    <span>📅 ${hyp.era || ''}</span>
                    <span>📍 ${hyp.village || ''}</span>
                  </div>
                </div>
              </div>
              <div class="scroll-person-bio" style="border-left-color:#f59e0b;">
                ${hyp.relationship_hypothesis}
              </div>
              <div class="scroll-card-actions">
                <button type="button" class="scroll-act-btn" style="border-color:rgba(245,158,11,0.5); color:#fbbf24;" data-open-hyp="${hyp.id}">
                  📜 Архивное досье гипотезы
                </button>
                ${hyp.probable_relative_ahnentafel ? `
                  <button type="button" class="scroll-act-btn" data-scroll-jump="${hyp.probable_relative_ahnentafel}">
                    🔗 К предку #${hyp.probable_relative_ahnentafel}
                  </button>
                ` : ''}
              </div>
            </article>
          `).join('');

          htmlSections.push(`
            <div class="scroll-gen-section" id="scroll-gen-hyp">
              <div class="scroll-gen-header" style="border-color:rgba(245,158,11,0.4);">
                <div class="scroll-gen-title">
                  <span class="gen-roman-badge" style="background:rgba(245,158,11,0.2); color:#fbbf24;">🪐</span>
                  <div>
                    <div style="color:#fef3c7;">Орбитальные архивные гипотезы и кандидаты в род</div>
                    <div style="font-size:11px; color:#fbbf24;">Кандидаты из ревизских сказок и метрик (требуют архивной склейки)</div>
                  </div>
                </div>
                <span class="scroll-gen-stats">${filteredHyps.length} канд.</span>
              </div>
              ${hypCardsHtml}
            </div>
          `);
        }
      }

      if (htmlSections.length === 0) {
        container.innerHTML = `
          <div style="text-align:center; padding:40px 20px; background:rgba(15,20,30,0.8); border-radius:16px; border:1px solid rgba(212,175,55,0.2);">
            <div style="font-size:32px; margin-bottom:8px;">🔍</div>
            <div style="font-size:15px; font-weight:700; color:var(--gold-light); margin-bottom:6px;">Ничего не найдено в текущем режиме</div>
            <p style="font-size:12.5px; color:var(--text-muted); margin-bottom:14px;">
              Попробуйте переключить тумблер в режим «🏛️ Все 7 колен + Гипотезы (152)» или сбросить фильтр клана.
            </p>
            <button type="button" id="scrollEmptyShowAllBtn" class="gate-btn" style="width:auto; padding:9px 20px; font-size:12.5px;">
              Показать все 7 колен и гипотезы
            </button>
          </div>
        `;
        const showAllBtn = document.getElementById('scrollEmptyShowAllBtn');
        if (showAllBtn) {
          showAllBtn.addEventListener('click', () => {
            scrollEpistemicMode = 'all_levels';
            scrollClanFilter = 'all';
            scrollSearchQuery = '';
            const sInp = document.getElementById('scrollSearchInput');
            if (sInp) sInp.value = '';
            syncScrollModeButtons();
            renderMobileScroll(lineageData);
          });
        }
        return;
      }

      container.innerHTML = htmlSections.join('');

      // Bind interactive events inside #scrollGenerationsList
      container.querySelectorAll('[data-scroll-photo]').forEach(el => {
        el.addEventListener('click', (ev) => {
          triggerPhotoUpload(el.getAttribute('data-scroll-photo'), ev);
        });
      });

      container.querySelectorAll('[data-open-dossier]').forEach(el => {
        el.addEventListener('click', () => {
          const ahn = parseInt(el.getAttribute('data-open-dossier'), 10);
          updateKinshipBreadcrumb(ahn);
          openDossier(ahn);
        });
      });

      container.querySelectorAll('[data-open-hyp]').forEach(el => {
        el.addEventListener('click', () => {
          openHypothesisDossier(el.getAttribute('data-open-hyp'));
        });
      });

      container.querySelectorAll('[data-scroll-jump]').forEach(el => {
        el.addEventListener('click', () => {
          const targetAhn = parseInt(el.getAttribute('data-scroll-jump'), 10);
          scrollToPersonInScroll(targetAhn);
        });
      });

      container.querySelectorAll('[data-show-kinship]').forEach(el => {
        el.addEventListener('click', () => {
          const ahn = parseInt(el.getAttribute('data-show-kinship'), 10);
          updateKinshipBreadcrumb(ahn);
          const bar = document.getElementById('kinshipPathBar');
          if (bar) bar.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });
      });

      container.querySelectorAll('[data-focus-2d]').forEach(el => {
        el.addEventListener('click', () => {
          const ahn = parseInt(el.getAttribute('data-focus-2d'), 10);
          focusNodeOn2DCanvas(ahn);
        });
      });

      container.querySelectorAll('[data-quick-quorum]').forEach(el => {
        el.addEventListener('click', () => {
          const nodeId = el.getAttribute('data-quick-quorum');
          if (!quorumMap[nodeId + '_user']) {
            quorumMap[nodeId] = (quorumMap[nodeId] || 0) + 1;
            quorumMap[nodeId + '_user'] = true;
            saveQuorumMap();
            renderMobileScroll(lineageData);
          }
        });
      });
    }

    // Setup Mouse Drag, Wheel Zoom & Multi-Touch (1-Finger Pan + 2-Finger Pinch-to-Zoom) on #roadmapShell
    (function initCanvasPanZoom() {
      const shell = document.getElementById('roadmapShell');
      if (!shell) return;

      // Mobile HUD Toggle button
      const hudToggleBtn = document.getElementById('mobileHudToggleBtn');
      const hudTop = document.getElementById('roadmapHudTop');
      if (hudToggleBtn && hudTop) {
        hudToggleBtn.addEventListener('click', () => {
          hudTop.classList.toggle('hud-expanded');
          hudToggleBtn.textContent = hudTop.classList.contains('hud-expanded')
            ? '✕ Скрыть панель фильтров'
            : '⚙️ Фильтры и поиск 2D-карты';
        });
      }

      shell.addEventListener('mousedown', (e) => {
        if (e.target.closest('.hud-panel') || e.target.closest('.roadmap-zoom-dock') || e.target.closest('.rm-node') || e.target.closest('.mobile-hud-toggle-btn')) {
          return;
        }
        isDragging = true;
        dragStartX = e.clientX - panX;
        dragStartY = e.clientY - panY;
        shell.classList.add('dragging');
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        panX = e.clientX - dragStartX;
        panY = e.clientY - dragStartY;
        applyRoadmapTransform();
      });

      window.addEventListener('mouseup', () => {
        isDragging = false;
        shell.classList.remove('dragging');
      });

      // Multi-Touch Support (1-finger pan + 2-finger pinch-to-zoom)
      let touchDragging = false;
      let pinchStartDist = 0;
      let pinchStartZoom = 1;

      function getTouchDist(t1, t2) {
        const dx = t1.clientX - t2.clientX;
        const dy = t1.clientY - t2.clientY;
        return Math.hypot(dx, dy);
      }

      shell.addEventListener('touchstart', (e) => {
        if (e.target.closest('.hud-panel') || e.target.closest('.roadmap-zoom-dock') || e.target.closest('.mobile-hud-toggle-btn')) {
          return;
        }
        if (e.touches.length === 1) {
          if (e.target.closest('.rm-node')) return;
          touchDragging = true;
          dragStartX = e.touches[0].clientX - panX;
          dragStartY = e.touches[0].clientY - panY;
        } else if (e.touches.length === 2) {
          touchDragging = false;
          pinchStartDist = getTouchDist(e.touches[0], e.touches[1]);
          pinchStartZoom = zoom;
        }
      }, { passive: true });

      shell.addEventListener('touchmove', (e) => {
        if (e.touches.length === 1 && touchDragging) {
          e.preventDefault();
          panX = e.touches[0].clientX - dragStartX;
          panY = e.touches[0].clientY - dragStartY;
          applyRoadmapTransform();
        } else if (e.touches.length === 2 && pinchStartDist > 0) {
          e.preventDefault();
          const rect = shell.getBoundingClientRect();
          const midX = ((e.touches[0].clientX + e.touches[1].clientX) / 2) - rect.left;
          const midY = ((e.touches[0].clientY + e.touches[1].clientY) / 2) - rect.top;
          const newDist = getTouchDist(e.touches[0], e.touches[1]);
          const scaleRatio = newDist / pinchStartDist;
          const prevZoom = zoom;
          zoom = Math.min(2.2, Math.max(0.14, pinchStartZoom * scaleRatio));
          panX = midX - ((midX - panX) * (zoom / prevZoom));
          panY = midY - ((midY - panY) * (zoom / prevZoom));
          applyRoadmapTransform();
        }
      }, { passive: false });

      shell.addEventListener('touchend', () => {
        touchDragging = false;
        pinchStartDist = 0;
      });

      shell.addEventListener('wheel', (e) => {
        e.preventDefault();
        const rect = shell.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const prevZoom = zoom;
        const delta = e.deltaY < 0 ? 1.12 : 0.89;
        zoom = Math.min(2.2, Math.max(0.12, zoom * delta));

        panX = mouseX - ((mouseX - panX) * (zoom / prevZoom));
        panY = mouseY - ((mouseY - panY) * (zoom / prevZoom));
        applyRoadmapTransform();
      }, { passive: false });

      document.getElementById('zoomInBtn').addEventListener('click', () => {
        zoom = Math.min(2.2, zoom * 1.2);
        applyRoadmapTransform();
      });
      document.getElementById('zoomOutBtn').addEventListener('click', () => {
        zoom = Math.max(0.12, zoom * 0.82);
        applyRoadmapTransform();
      });
      document.getElementById('zoomResetBtn').addEventListener('click', focusOnProband);
      document.getElementById('zoomFitBtn').addEventListener('click', fitEntireRoadmap);
    })();"""

assert old_panzoom_block in html, "Could not find initCanvasPanZoom block"
html = html.replace(old_panzoom_block, new_panzoom_and_mobile_scroll_block, 1)

# 9. Enhance openDossier with Fact Certificate & 12 Rubrics Accordion + Button to Focus on 2D Map
old_dossier_render = """      const drawerBody = document.getElementById('drawerBody');
      drawerBody.innerHTML = `
        <div class="drawer-portrait-hero">"""

new_dossier_render = """      const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
      const factCertHtml = isFactConfirmed ? `
        <div style="padding:10px 12px; border-radius:10px; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.45); margin-bottom:12px; font-size:12px; color:#6ee7b7;">
          <strong>🛡️ АРХИВНЫЙ СЕРТИФИКАТ: 100% ФАКТ</strong><br/>
          <span style="color:#cbd5e1; font-size:11.5px;">${node.fact_certificate || 'Верифицировано прямыми документами ЗАГС, военными фондами и свидетельствами семьи.'}</span>
        </div>
      ` : '';

      let rubrics12Html = '';
      if (node.dossier_12_rubrics && typeof node.dossier_12_rubrics === 'object') {
        const rubricEntries = Object.entries(node.dossier_12_rubrics).map(([k, v]) => `
          <div class="rubric-row">
            <div class="rubric-key">${k.replace(/_/g, ' ')}</div>
            <div class="rubric-val">${v}</div>
          </div>
        `).join('');
        rubrics12Html = `
          <details class="rubrics-12-details">
            <summary>📚 Полный формуляр досье (12 историко-архивных рубрик)</summary>
            <div class="rubrics-12-grid">
              ${rubricEntries}
            </div>
          </details>
        `;
      }

      const drawerBody = document.getElementById('drawerBody');
      drawerBody.innerHTML = `
        ${factCertHtml}
        <div class="drawer-portrait-hero">"""

assert old_dossier_render in html, "Could not find drawerBody.innerHTML start"
html = html.replace(old_dossier_render, new_dossier_render, 1)

# Insert rubrics12Html and 2D focus button inside openDossier
old_dossier_sources = """        <div class="field-row">
          <div class="field-label">Источники и целевые фонды</div>
          <div class="field-val">
            <ul style="padding-left:18px; font-size:13px;">
              ${(node.sources || []).map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>
        </div>"""

new_dossier_sources = """        <div class="field-row">
          <div class="field-label">Источники и целевые фонды</div>
          <div class="field-val">
            <ul style="padding-left:18px; font-size:13px;">
              ${(node.sources || []).map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>
        </div>

        ${rubrics12Html}

        <div style="display:flex; gap:8px; margin:10px 0;">
          <button type="button" id="drawerFocus2dBtn" class="btn-outline" style="flex:1; font-size:12px;">
            🗺️ Показать на 2D-карте
          </button>
          <button type="button" id="drawerFocusScrollBtn" class="btn-outline" style="flex:1; font-size:12px;">
            📱 Показать в Свитке
          </button>
        </div>"""

assert old_dossier_sources in html, "Could not find dossier sources block"
html = html.replace(old_dossier_sources, new_dossier_sources, 1)

old_dossier_listeners = """      // Event handlers inside drawer
      document.getElementById('drawerUploadPhotoBtn').addEventListener('click', (ev) => {
        triggerPhotoUpload(node.id, ev);
      });"""

new_dossier_listeners = """      // Event handlers inside drawer
      document.getElementById('drawerUploadPhotoBtn').addEventListener('click', (ev) => {
        triggerPhotoUpload(node.id, ev);
      });
      const focus2dBtn = document.getElementById('drawerFocus2dBtn');
      if (focus2dBtn) {
        focus2dBtn.addEventListener('click', () => {
          closeDossier();
          focusNodeOn2DCanvas(node.ahnentafel);
        });
      }
      const focusScrollBtn = document.getElementById('drawerFocusScrollBtn');
      if (focusScrollBtn) {
        focusScrollBtn.addEventListener('click', () => {
          closeDossier();
          switchView('scroll');
          scrollToPersonInScroll(node.ahnentafel);
        });
      }"""

assert old_dossier_listeners in html, "Could not find drawerUploadPhotoBtn listener"
html = html.replace(old_dossier_listeners, new_dossier_listeners, 1)

# 10. Update Wizard submit to also re-render Mobile Scroll
old_wiz_submit_render = """        renderRoadmapCanvas(lineageData);

        form.style.display = 'none';"""

new_wiz_submit_render = """        renderRoadmapCanvas(lineageData);
        renderMobileScroll(lineageData);

        form.style.display = 'none';"""

assert old_wiz_submit_render in html, "Could not find wizard submit renderRoadmapCanvas"
html = html.replace(old_wiz_submit_render, new_wiz_submit_render, 1)

# 11. Update Auth unlock & View Switching to support Mobile Scroll & Bottom Nav
old_auth_unlock_and_tabs = """        renderRoadmapCanvas(lineageData);
        renderFanChart(lineageData);
        renderArchiveRadar(lineageData);
        renderAccessGuide(lineageData);
        initBranchWizard();

        setTimeout(() => {
          document.getElementById('fortressGate').classList.add('unlocked');
          document.getElementById('workspace').classList.add('active');
          focusOnProband();
        }, 180);
      } catch (err) {
        failedAttempts += 1;
        const delaySec = Math.min(failedAttempts * 2, 10);
        statusEl.className = 'gate-status error';
        statusEl.textContent = `Ошибка расшифровки AES-256-GCM: неверный ключ доступа (задержка ${delaySec} сек.)`;
        setTimeout(() => { btn.disabled = false; }, delaySec * 1000);
        return;
      }
      btn.disabled = false;
    });

    document.querySelectorAll('.nav-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
        tab.classList.add('active');
        const target = tab.getAttribute('data-view');
        document.getElementById(`view-${target}`).classList.add('active');
      });
    });"""

new_auth_unlock_and_tabs = """        renderRoadmapCanvas(lineageData);
        renderMobileScroll(lineageData);
        renderFanChart(lineageData);
        renderArchiveRadar(lineageData);
        renderAccessGuide(lineageData);
        initBranchWizard();

        setTimeout(() => {
          document.getElementById('fortressGate').classList.add('unlocked');
          document.getElementById('workspace').classList.add('active');
          if (window.innerWidth <= 860) {
            switchView('scroll');
          } else {
            focusOnProband();
          }
        }, 180);
      } catch (err) {
        failedAttempts += 1;
        const delaySec = Math.min(failedAttempts * 2, 10);
        statusEl.className = 'gate-status error';
        statusEl.textContent = `Ошибка расшифровки AES-256-GCM: неверный ключ доступа (задержка ${delaySec} сек.)`;
        setTimeout(() => { btn.disabled = false; }, delaySec * 1000);
        return;
      }
      btn.disabled = false;
    });

    function switchView(targetView) {
      document.querySelectorAll('.nav-tab').forEach(t => {
        t.classList.toggle('active', t.getAttribute('data-view') === targetView);
      });
      document.querySelectorAll('.mob-nav-item[data-mob-view]').forEach(m => {
        m.classList.toggle('active', m.getAttribute('data-mob-view') === targetView);
      });
      document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
      const sec = document.getElementById(`view-${targetView}`);
      if (sec) sec.classList.add('active');
    }

    document.querySelectorAll('.nav-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-view');
        switchView(target);
      });
    });

    document.querySelectorAll('.mob-nav-item[data-mob-view]').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-mob-view');
        switchView(target);
      });
    });

    const mobWizBtn = document.getElementById('mobOpenBranchWizardBtn');
    if (mobWizBtn) {
      mobWizBtn.addEventListener('click', () => {
        const openBtn = document.getElementById('openBranchWizardBtn');
        if (openBtn) openBtn.click();
      });
    }

    // Mobile Scroll Header Controls
    document.getElementById('scrollModeFactsBtn').addEventListener('click', () => {
      scrollEpistemicMode = 'facts_only';
      syncScrollModeButtons();
      if (lineageData) renderMobileScroll(lineageData);
    });

    document.getElementById('scrollModeAllBtn').addEventListener('click', () => {
      scrollEpistemicMode = 'all_levels';
      syncScrollModeButtons();
      if (lineageData) renderMobileScroll(lineageData);
    });

    document.querySelectorAll('#scrollClanPills .scroll-clan-pill').forEach(pill => {
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
    });

    document.querySelectorAll('#scrollGenJumpbar .gen-jump-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('#scrollGenJumpbar .gen-jump-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const g = btn.getAttribute('data-gen-jump');
        if ((g === '5' || g === '6' || g === '7' || g === 'hyp') && scrollEpistemicMode === 'facts_only') {
          scrollEpistemicMode = 'all_levels';
          syncScrollModeButtons();
          if (lineageData) renderMobileScroll(lineageData);
        }
        setTimeout(() => {
          const sec = document.getElementById(`scroll-gen-${g}`);
          if (sec) sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 40);
      });
    });

    const scrollSearchInp = document.getElementById('scrollSearchInput');
    const scrollClearBtn = document.getElementById('scrollClearSearchBtn');
    scrollSearchInp.addEventListener('input', (e) => {
      scrollSearchQuery = e.target.value || '';
      scrollClearBtn.style.display = scrollSearchQuery ? 'inline-flex' : 'none';
      if (lineageData) renderMobileScroll(lineageData);
    });
    scrollClearBtn.addEventListener('click', () => {
      scrollSearchInp.value = '';
      scrollSearchQuery = '';
      scrollClearBtn.style.display = 'none';
      if (lineageData) renderMobileScroll(lineageData);
    });

    document.getElementById('resetKinshipPathBtn').addEventListener('click', () => {
      updateKinshipBreadcrumb(null);
    });"""

assert old_auth_unlock_and_tabs in html, "Could not find auth unlock and tabs block"
html = html.replace(old_auth_unlock_and_tabs, new_auth_unlock_and_tabs, 1)

astro_path.write_text(html, encoding="utf-8")
print("[OK] Successfully upgraded src/pages/index.astro with Native Mobile App & Generation Scroll!")
