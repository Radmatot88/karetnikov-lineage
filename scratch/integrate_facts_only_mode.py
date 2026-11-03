#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Интеграция режима «ТОЛЬКО ФАКТЫ (100% ФАКТ)» в src/pages/index.astro.
"""

from pathlib import Path

target_file = Path(r"c:\Karetnikov_Lineage\src\pages\index.astro")
content = target_file.read_text(encoding="utf-8")

# 1. Вставка HUD переключателя режимов
old_hud_top = '''        <!-- Floating Top HUD -->
        <div class="roadmap-hud-top">
          <div class="hud-panel">'''

new_hud_top = '''        <!-- Floating Top HUD -->
        <div class="roadmap-hud-top">
          <!-- Режим 100% ФАКТЫ vs Все уровни -->
          <div class="hud-panel mode-toggle-panel">
            <div class="epistemic-segmented-control" role="radiogroup" aria-label="Эпистемический режим отображения">
              <button
                id="modeFactsBtn"
                type="button"
                class="seg-btn active"
                data-mode="facts_only"
                role="radio"
                aria-checked="true"
                title="Показать только 100% верифицированные архивные факты (19 персон) [Горячая клавиша: F]"
              >
                <span class="seg-gem gold-gem"></span>
                <span class="seg-label">🟢 Только факты (100%)</span>
                <span class="seg-counter" id="factsCounterReadout">19</span>
              </button>
              
              <button
                id="modeAllBtn"
                type="button"
                class="seg-btn"
                data-mode="all_levels"
                role="radio"
                aria-checked="false"
                title="Открыть полный исследовательский контур со всеми гипотезами I–V (137 слотов) [Горячая клавиша: A]"
              >
                <span class="seg-gem cyan-gem"></span>
                <span class="seg-label">🏛️ Все уровни (гипотезы I–V)</span>
                <span class="seg-counter" id="allNodesCounterReadout">137</span>
              </button>
            </div>

            <div class="mode-live-pill" id="modeLivePill">
              <span class="pill-dot pulse"></span>
              <span class="pill-text" id="modeLivePillText">ЯДРО ВЕРИФИКАЦИИ: 19 ПЕРСОН</span>
            </div>
          </div>

          <div class="hud-panel">'''

content = content.replace(old_hud_top, new_hud_top, 1)

# 2. Инициализация состояния и констант в <script is:inline>
old_script_start = '''  <!-- ================= CLIENT-SIDE WEB CRYPTO, PHOTO VAULT & ROADMAP ENGINE ================= -->
  <script is:inline>
    let encryptedBundle = null;
    let lineageData = null;
    let activeFilter = 'all7';
    let searchQuery = '';
    let failedAttempts = 0;'''

new_script_start = '''  <!-- ================= CLIENT-SIDE WEB CRYPTO, PHOTO VAULT & ROADMAP ENGINE ================= -->
  <script is:inline>
    let encryptedBundle = null;
    let lineageData = null;
    let activeFilter = 'all7';
    let searchQuery = '';
    let failedAttempts = 0;

    // Режим отображения: 'facts_only' (100% золотое ядро) или 'all_levels' (I–V уровни)
    let epistemicMode = 'facts_only';

    // Золотой реестр 19 верифицированных архивных персон (100% ФАКТ)
    const CONFIRMED_FACT_AHNENTAFELS = new Set([
      1,     // #1 Пробанд Каретников Дмитрий Иванович
      2,     // #2 Отец Каретников Иван Валентинович
      3,     // #3 Мать Каретникова Светлана Владимировна (Зубкова)
      4,     // #4 Дед Каретников Валентин Григорьевич (1936)
      5,     // #5 Бабушка Каретникова Клавдия Петровна (Юхина, 1936)
      6,     // #6 Дед Зубков Владимир Владимирович
      7,     // #7 Бабушка Зубкова Валентина Сергеевна (Куманина)
      8,     // #8 Прадед Каретников Григорий Иванович
      9,     // #9 Прабабушка Каретникова Агриппина Анисимовна
      10,    // #10 Прадед Юхин Пётр (с. Четыровка)
      14,    // #14 Прадед Куманин Сергей (с. Новый Шуструй)
      301,   // #301 Дядя Зубков Владимир Владимирович-мл.
      401,   // #401 Старший брат деда Каретников Николай Григорьевич
      402,   // #402 Средний брат деда Каретников Пётр Григорьевич
      4011,  // #4011 Двоюродный дядя Каретников Василий Николаевич (с. Плешаново)
      4012,  // #4012 Двоюродный дядя Каретников Валерий Николаевич (г. Тольятти)
      701,   // #701 Двоюродная бабушка Зинаида Сергеевна (с. Новый Шуструй, жива)
      702,   // #702 Двоюродная бабушка Антонина Сергеевна (с. Новый Шуструй, жива)
      801    // #801 Брат прадеда Каретников Фёдор Иванович (1923, сталинградец, председатель)
    ]);'''

content = content.replace(old_script_start, new_script_start, 1)

# 3. Добавление функции setEpistemicMode перед renderRoadmapCanvas
mode_switch_func = '''
    function setEpistemicMode(mode) {
      epistemicMode = mode;
      const factsBtn = document.getElementById('modeFactsBtn');
      const allBtn = document.getElementById('modeAllBtn');
      const livePill = document.getElementById('modeLivePill');
      const pillText = document.getElementById('modeLivePillText');

      if (mode === 'facts_only') {
        if (factsBtn) {
          factsBtn.classList.add('active');
          factsBtn.setAttribute('aria-checked', 'true');
        }
        if (allBtn) {
          allBtn.classList.remove('active');
          allBtn.setAttribute('aria-checked', 'false');
        }
        if (livePill) {
          livePill.style.borderColor = 'rgba(16, 185, 129, 0.3)';
          livePill.style.background = 'rgba(16, 185, 129, 0.1)';
        }
        if (pillText) {
          pillText.textContent = 'ЯДРО ВЕРИФИКАЦИИ: 19 ПЕРСОН';
          pillText.style.color = '#34d399';
        }
      } else {
        if (factsBtn) {
          factsBtn.classList.remove('active');
          factsBtn.setAttribute('aria-checked', 'false');
        }
        if (allBtn) {
          allBtn.classList.add('active');
          allBtn.setAttribute('aria-checked', 'true');
        }
        if (livePill) {
          livePill.style.borderColor = 'rgba(56, 189, 248, 0.3)';
          livePill.style.background = 'rgba(56, 189, 248, 0.1)';
        }
        if (pillText) {
          pillText.textContent = 'ИССЛЕДОВАТЕЛЬСКИЙ КОНТУР: I–V УРОВНИ (137)';
          pillText.style.color = '#38bdf8';
        }
      }

      if (lineageData) {
        renderRoadmapCanvas(lineageData);
        renderFanChart(lineageData);
        if (mode === 'facts_only') focusOnProband();
      }
    }
'''

content = content.replace(
    '    // ================= INFINITE EXPANDING BINARY TREE RENDERER (1->2->4->8->16->32->64) =================',
    mode_switch_func + '\n    // ================= INFINITE EXPANDING BINARY TREE RENDERER (1->2->4->8->16->32->64) =================',
    1
)

# 4. Обновление renderRoadmapCanvas: maxGen
content = content.replace(
    "const maxGen = activeFilter === 'gen5' ? 5 : 7;",
    "const maxGen = epistemicMode === 'facts_only' ? 4 : (activeFilter === 'gen5' ? 5 : 7);",
    1
)

# 5. Обновление карточек узлов в renderRoadmapCanvas
old_card_gen = '''        htmlParts.push(`
          <article
            class="rm-node status-${node.status} branch-${node.branch} ${extraClass}"
            style="left:${box.x}px; top:${box.y}px; ${searchHighlightStyle}"
            data-ahnentafel="${node.ahnentafel}"
          >
            <div class="rm-portrait" data-photo-trigger="${node.id}" title="Нажмите, чтобы загрузить или обновить фотографию">
              ${portraitInner}
              <span class="rm-photo-badge">📷 Фото</span>
            </div>
            <div class="rm-content">
              <div class="rm-top-badges">
                <span class="ahnentafel-badge">${node.is_collateral ? `Брат #${node.sibling_of_ahnentafel}` : `Слот #${node.ahnentafel}`}</span>
                <span class="branch-tag ${node.branch}">${branchLabel}</span>
              </div>
              <div class="rm-name">${node.full_name}</div>
              <div class="rm-dates">${node.birth_date || ''}${deathStr}</div>
              <div class="rm-place" title="${node.birth_place || ''}">📍 ${node.birth_place || ''}</div>
            </div>
          </article>
        `);'''

new_card_gen = '''        const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
        const isPendingSlot = (epistemicMode === 'facts_only' && !isFactConfirmed);

        let cardClasses = `rm-node status-${node.status} branch-${node.branch} ${extraClass}`;
        if (isFactConfirmed) cardClasses += ' is-fact-confirmed';
        if (isPendingSlot) cardClasses += ' is-pending-fact';

        const factBadge = isFactConfirmed ? `<span class="badge-fact-100">🟢 100% ФАКТ</span>` : '';
        const displayName = isPendingSlot
          ? `Слот #${node.ahnentafel} • Ожидает выписки архива`
          : node.full_name;

        htmlParts.push(`
          <article
            class="${cardClasses}"
            style="left:${box.x}px; top:${box.y}px; ${searchHighlightStyle}"
            data-ahnentafel="${node.ahnentafel}"
          >
            <div class="rm-portrait" data-photo-trigger="${node.id}" title="Нажмите, чтобы загрузить или обновить фотографию">
              ${portraitInner}
              <span class="rm-photo-badge">📷 Фото</span>
            </div>
            <div class="rm-content">
              <div class="rm-top-badges">
                <span class="ahnentafel-badge">${node.is_collateral ? `Брат #${node.sibling_of_ahnentafel}` : `Слот #${node.ahnentafel}`}</span>
                ${factBadge}
                <span class="branch-tag ${node.branch}">${branchLabel}</span>
              </div>
              <div class="rm-name">${displayName}</div>
              <div class="rm-dates">${node.birth_date || ''}${deathStr}</div>
              <div class="rm-place" title="${node.birth_place || ''}">📍 ${node.birth_place || ''}</div>
            </div>
          </article>
        `);'''

content = content.replace(old_card_gen, new_card_gen, 1)

# 6. Вставка facts-horizon-column после отрисовки узлов
horizon_block = '''
      // Монолитная колонка «Архивный фронт V–VII колен» в режиме «Только факты»
      if (epistemicMode === 'facts_only') {
        const horizonX = 80 + 4 * COL_X_STEP;
        const horizonY = centerY - 240;
        htmlParts.push(`
          <div class="facts-horizon-column" style="left:${horizonX}px; top:${horizonY}px;">
            <div class="facts-horizon-title">
              <span>🏛️ Архивный фронт V–VII колен</span>
            </div>
            <p style="font-size:12px; color:var(--text-muted); line-height:1.45;">
              Глубокие корни династии XVII–XIX вв. исследуются в целевых фондах РГАДА, ГАОО, ЦГАСО и ГАПО:
            </p>
            <div class="facts-horizon-card">
              <strong>Каретниковы:</strong> Бузулукский уезд, слободы Мценска (РГАДА Ф. 350) и фабричная ветвь Тейково.
            </div>
            <div class="facts-horizon-card">
              <strong>Юхины:</strong> с. Четыровка на р. Кондурче (ЦГАСО Ф. 678 рекруты 1863 г. и метрики Ф. 32).
            </div>
            <div class="facts-horizon-card">
              <strong>Зубковы:</strong> с. Новый Шуструй (19 дворов переписи 1917 г. ГАПО Ф. 158 и X ревизия Ф. 60).
            </div>
            <div class="facts-horizon-card">
              <strong>Куманины:</strong> с. Новый Шуструй, служилые стрельцы Ломовской черты с 1670-х гг. (РГАДА Ф. 210).
            </div>
            <button id="openAllLevelsFromHorizonBtn" class="btn-outline" style="width:100%; font-size:12px; font-weight:700; color:var(--gold-light); border-color:var(--gold-primary); margin-top:4px;">
              Раскрыть все 137 слотов и гипотез ↗
            </button>
          </div>
        `);
      }
'''

content = content.replace("nodesLayer.innerHTML = htmlParts.join('');", horizon_block + "\n      nodesLayer.innerHTML = htmlParts.join('');", 1)

# 7. Обновление SVG связей: золотые линии для фактов
old_svg_curve = '''            const d = `M ${x1} ${y1} C ${cpx1} ${y1}, ${cpx2} ${y2}, ${x2} ${y2}`;
            const isDash = targetNode && targetNode.status === 'UNKNOWN_SLOT';
            pathsSvg += `
              <path
                d="${d}"
                fill="none"
                stroke="${strokeColor}"
                stroke-width="${strokeWidth}"
                stroke-dasharray="${isDash ? '6,5' : 'none'}"
                opacity="${isDash ? 0.45 : 0.85}"
              />
            `;'''

new_svg_curve = '''            const d = `M ${x1} ${y1} C ${cpx1} ${y1}, ${cpx2} ${y2}, ${x2} ${y2}`;
            const isConfirmedEdge = CONFIRMED_FACT_AHNENTAFELS.has(n.ahnentafel) && CONFIRMED_FACT_AHNENTAFELS.has(targetAhn);
            const edgeStroke = isConfirmedEdge ? '#d4af37' : (strokeColor || '#475569');
            const edgeWidth = isConfirmedEdge ? 3.5 : (targetNode && targetNode.status === 'UNKNOWN_SLOT' ? 1.5 : strokeWidth);
            const isDash = (!isConfirmedEdge && epistemicMode === 'facts_only') || (targetNode && targetNode.status === 'UNKNOWN_SLOT');
            const edgeOpacity = isConfirmedEdge ? 0.95 : (isDash ? 0.4 : 0.8);
            pathsSvg += `
              <path
                d="${d}"
                fill="none"
                stroke="${edgeStroke}"
                stroke-width="${edgeWidth}"
                stroke-dasharray="${isDash ? '4,4' : 'none'}"
                opacity="${edgeOpacity}"
              />
            `;'''

content = content.replace(old_svg_curve, new_svg_curve, 1)

# 8. Обновление renderFanChart: подсветка 19 секторов
old_fan_fill = '''          const d = createAnnularSectorPath(cx, cy, rInner, rOuter, a0, a1 - 0.4);
          const fill = statusColors[node.status] || '#1e293b';
          const stroke = node.branch === 'paternal' ? 'rgba(224,122,95,0.45)' : 'rgba(42,157,143,0.45)';'''

new_fan_fill = '''          const d = createAnnularSectorPath(cx, cy, rInner, rOuter, a0, a1 - 0.4);
          let fill = statusColors[node.status] || '#1e293b';
          let stroke = node.branch === 'paternal' ? 'rgba(224,122,95,0.45)' : 'rgba(42,157,143,0.45)';
          let strokeWidth = '1';

          if (epistemicMode === 'facts_only') {
            if (CONFIRMED_FACT_AHNENTAFELS.has(ahn)) {
              fill = '#10b981';
              stroke = '#d4af37';
              strokeWidth = '2.5';
            } else {
              fill = 'rgba(20, 26, 38, 0.45)';
              stroke = 'rgba(148, 163, 184, 0.12)';
              strokeWidth = '0.8';
            }
          }'''

content = content.replace(old_fan_fill, new_fan_fill, 1)
content = content.replace("stroke-width=\"1\"", "stroke-width=\"${strokeWidth}\"", 1)

# 9. Обновление openDossier: гербовый сертификат достоверности
cert_banner_code = '''
      const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
      let certHtml = '';
      if (isFactConfirmed) {
        const basis = (node.fact_certificate && node.fact_certificate.doc_basis) || 'Запись верифицирована государственными архивами РФ и прямым свидетельством семьи.';
        certHtml = `
          <div class="fact-guarantee-banner">
            <div class="fact-guarantee-badge">
              <span class="cert-shield">🛡️</span>
              <div>
                <div class="cert-title">АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ</div>
                <div class="cert-desc">${basis}</div>
              </div>
            </div>
          </div>
        `;
      }
'''

content = content.replace(
    '      const drawerBody = document.getElementById(\'drawerBody\');\n      drawerBody.innerHTML = `',
    cert_banner_code + '\n      const drawerBody = document.getElementById(\'drawerBody\');\n      drawerBody.innerHTML = `\n        ${certHtml}',
    1
)

# 10. Добавление обработчиков клика по кнопкам переключения и кнопке в горизонте
event_bindings = '''
    // Переключение режимов: Только факты vs Все уровни
    document.getElementById('modeFactsBtn').addEventListener('click', () => setEpistemicMode('facts_only'));
    document.getElementById('modeAllBtn').addEventListener('click', () => setEpistemicMode('all_levels'));

    document.addEventListener('click', (e) => {
      if (e.target && e.target.id === 'openAllLevelsFromHorizonBtn') {
        setEpistemicMode('all_levels');
      }
    });

    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'f' || e.key === 'F' || e.key === 'а' || e.key === 'А') {
        setEpistemicMode('facts_only');
      } else if (e.key === 'a' || e.key === 'A' || e.key === 'ф' || e.key === 'Ф') {
        setEpistemicMode('all_levels');
      }
    });
'''

content = content.replace(
    "    document.getElementById('togglePwBtn').addEventListener('click', () => {",
    event_bindings + "\n    document.getElementById('togglePwBtn').addEventListener('click', () => {",
    1
)

target_file.write_text(content, encoding="utf-8")
print("[OK] Successfully integrated facts-only mode into src/pages/index.astro")
