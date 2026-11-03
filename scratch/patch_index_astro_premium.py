import re

def patch_index_astro():
    with open("src/pages/index.astro", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update dimensions in renderRoadmapCanvas
    content = content.replace("const COL_X_STEP = 450;\n      const CARD_W = 310;\n      const CARD_H = 108;", "const COL_X_STEP = 470;\n      const CARD_W = 350;\n      const CARD_H = 124;")
    content = content.replace("w: node.ahnentafel === 1 ? 330 : CARD_W,", "w: node.ahnentafel === 1 ? 370 : CARD_W,")

    # 2. Update Generation Banners loop (start from g = 2 so Gen 1 banner does not duplicate or collide with Proband card)
    old_banner_loop = """      for (let g = 1; g <= maxGen; g++) {
        const colX = 80 + (g - 1) * COL_X_STEP;
        const colH = getColHeight(g);
        const bannerTop = Math.max(18, (centerY - colH / 2) - 58);
        const [t1, t2] = genTitles[g];
        htmlParts.push(`
          <div class="canvas-gen-banner" style="left:${colX}px; top:${bannerTop}px;">
            <div class="t1">${t1}</div>
            <div class="t2">${t2}</div>
          </div>
        `);

        // Floating hypothesis banner if column has hypotheses
        const hypsInGen = visibleHypotheses.filter(h => h.generation === g);
        if (hypsInGen.length > 0) {
          const hypBannerTop = (centerY - colH / 2) + colH + 24;
          htmlParts.push(`
            <div class="canvas-hyp-banner" style="left:${colX}px; top:${hypBannerTop}px;">
              <svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> ПАРЯЩИЕ ГИПОТЕЗЫ КОЛЕНА (${hypsInGen.length})
            </div>
          `);
        }
      }"""

    new_banner_loop = """      const romanNumerals = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII'];
      // Generation Banners: start from g = 2 because Proband (#1) has its own sovereign royal crown header
      for (let g = 2; g <= maxGen; g++) {
        const colX = 80 + (g - 1) * COL_X_STEP;
        const colH = getColHeight(g);
        const startY = centerY - colH / 2;
        const bannerTop = Math.max(24, startY - 82);
        const [t1, t2] = genTitles[g];
        htmlParts.push(`
          <div class="canvas-gen-banner" style="left:${colX}px; top:${bannerTop}px; width:${CARD_W}px;">
            <div class="gen-banner-badge">${romanNumerals[g]}</div>
            <div class="gen-banner-titles">
              <div class="t1">${t1}</div>
              <div class="t2">${t2}</div>
            </div>
          </div>
        `);

        // Floating hypothesis banner if column has hypotheses
        const hypsInGen = visibleHypotheses.filter(h => h.generation === g);
        if (hypsInGen.length > 0) {
          const hypBannerTop = (centerY - colH / 2) + colH + 24;
          htmlParts.push(`
            <div class="canvas-hyp-banner" style="left:${colX}px; top:${hypBannerTop}px; width:${CARD_W}px;">
              <svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> ПАРЯЩИЕ ГИПОТЕЗЫ КОЛЕНА (${hypsInGen.length})
            </div>
          `);
        }
      }"""

    if old_banner_loop in content:
        content = content.replace(old_banner_loop, new_banner_loop)
        print("Replaced Generation Banner loop successfully!")
    else:
        print("Warning: old_banner_loop not found exactly, searching via regex...")
        content = re.sub(
            r'for\s*\(\s*let\s+g\s*=\s*1;\s*g\s*<=\s*maxGen;\s*g\+\+\s*\)\s*\{[^}]*canvas-gen-banner.*?\}\s*\}',
            new_banner_loop,
            content,
            flags=re.DOTALL
        )

    # 3. Update Node rendering loop to separate Proband (#1) and other cards
    old_node_render = re.search(r'// Render direct & collateral nodes\s*Object\.values\(coordsByAhn\)\.forEach\(box => \{.*?\}\);\s*// Render floating orbital hypotheses', content, re.DOTALL)
    if not old_node_render:
        print("Error: Could not locate node render block")
        return False

    new_node_render = """// Render direct & collateral nodes (Imperial Architectural Standard)
      Object.values(coordsByAhn).forEach(box => {
        const node = box.node;
        const photoSrc = getNodePhoto(node);
        const portraitInner = photoSrc
          ? `<img src="${photoSrc}" alt="${node.full_name}" />`
          : `<div class="rm-portrait-placeholder">${getInitials(node)}</div>`;

        const branchLabel = node.is_relative_proposal
          ? 'Ветвь родственников'
          : node.is_collateral
            ? 'Родной брат'
            : node.branch === 'paternal'
              ? 'Линия Отца'
              : node.branch === 'maternal'
                ? 'Линия Матери'
                : 'Пробанд (#1)';

        const deathStr = node.death_date ? ` — ${node.death_date}` : '';
        const extraClass = node.ahnentafel === 1 ? 'proband-node' : node.is_collateral ? 'collateral-node' : '';

        let searchHighlightStyle = '';
        if (q) {
          const hay = `${node.full_name} ${node.birth_place} ${node.sub_clan} ${node.notes} #${node.ahnentafel}`.toLowerCase();
          if (hay.includes(q)) {
            searchHighlightStyle = 'outline: 3px solid #7A1C1C; box-shadow: 0 0 24px rgba(122,28,28,0.3); z-index: 15;';
          } else {
            searchHighlightStyle = 'opacity: 0.25;';
          }
        }

        if (activeFilter === 'hypotheses') {
          searchHighlightStyle += ' opacity: 0.35;';
        }

        const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
        const isPendingSlot = (epistemicMode === 'facts_only' && !isFactConfirmed);

        let cardClasses = `rm-node status-${node.status} branch-${node.branch} ${extraClass}`;
        if (isFactConfirmed) cardClasses += ' is-fact-confirmed';
        if (isPendingSlot) cardClasses += ' is-pending-fact';

        const factBadge = isFactConfirmed ? `<span class="badge-fact-100"><svg class="svg-icon xs"><use href="#icon-seal-confirmed"/></svg> 100% ФАКТ</span>` : '';
        const displayName = isPendingSlot
          ? `Слот #${node.ahnentafel} • Ожидает выписки архива`
          : node.full_name;

        // PROBAND (#1): Sovereign Royal Master Card
        if (node.ahnentafel === 1) {
          htmlParts.push(`
            <article
              class="${cardClasses}"
              style="left:${box.x}px; top:${box.y}px; width:${box.w}px; ${searchHighlightStyle}"
              data-ahnentafel="1"
            >
              <div class="rm-proband-crown-bar">
                <div class="rm-proband-crown-title">
                  <svg class="svg-icon xs" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M5 16L3 5l5.5 5L12 4l3.5 6L21 5l-2 11H5zm14 3c0 .6-.4 1-1 1H6c-.6 0-1-.4-1-1v-1h14v1z"/>
                  </svg>
                  <span>I КОЛЕНО • ПРОБАНД (ОСНОВАТЕЛЬ)</span>
                </div>
                ${factBadge}
              </div>
              <div class="rm-card-body">
                <div class="rm-portrait proband-portrait" data-photo-trigger="${node.id}" title="Загрузить фотографию Пробанда">
                  ${portraitInner}
                  <span class="rm-photo-badge"><svg class="svg-icon sm"><use href="#icon-photo"/></svg> Фото</span>
                </div>
                <div class="rm-content">
                  <div class="rm-proband-clan">КАРЕТНИКОВЫ • ЗУБКОВЫ • КУМАНИНЫ • ЮХИНЫ</div>
                  <div class="rm-name proband-name">${displayName}</div>
                  <div class="rm-role-sub">Глава рода • Родовой архив 127 предков</div>
                  <div class="rm-meta-row">
                    <span class="rm-dates"><svg class="svg-icon xs"><use href="#icon-calendar"/></svg> 14.09.1994</span>
                    <span class="rm-place"><svg class="svg-icon xs"><use href="#icon-pin"/></svg> г. Самара</span>
                  </div>
                </div>
              </div>
            </article>
          `);
        } else {
          // GENERATIONS II-VII & COLLATERALS
          htmlParts.push(`
            <article
              class="${cardClasses}"
              style="left:${box.x}px; top:${box.y}px; width:${box.w}px; ${searchHighlightStyle}"
              data-ahnentafel="${node.ahnentafel}"
            >
              <div class="rm-card-top-bar">
                <span class="ahnentafel-badge">${node.is_collateral ? `Брат #${node.sibling_of_ahnentafel}` : `Слот #${node.ahnentafel}`}</span>
                ${factBadge}
                <span class="branch-tag ${node.branch}">${branchLabel}</span>
              </div>
              <div class="rm-card-body">
                <div class="rm-portrait" data-photo-trigger="${node.id}" title="Нажмите, чтобы загрузить или обновить фотографию">
                  ${portraitInner}
                  <span class="rm-photo-badge"><svg class="svg-icon sm"><use href="#icon-photo"/></svg> Фото</span>
                </div>
                <div class="rm-content">
                  <div class="rm-name">${displayName}</div>
                  <div class="rm-dates"><svg class="svg-icon xs"><use href="#icon-calendar"/></svg> ${node.birth_date || ''}${deathStr}</div>
                  <div class="rm-place" title="${node.birth_place || ''}"><svg class="svg-icon xs"><use href="#icon-pin"/></svg> ${node.birth_place || 'Село не указано'}</div>
                </div>
              </div>
            </article>
          `);
        }
      });

      // Render floating orbital hypotheses"""

    content = content[:old_node_render.start()] + new_node_render + content[old_node_render.end()-41:]
    print("Replaced Node Rendering template successfully!")

    # 4. Update SVG connector colors in renderRoadmapCanvas
    content = content.replace("const strokeColor = dstBox.node.branch === 'paternal'\n              ? 'rgba(224, 122, 95, 0.72)'\n              : 'rgba(42, 157, 143, 0.72)';", "const strokeColor = dstBox.node.branch === 'paternal'\n              ? '#8B261E'\n              : '#146C43';")
    content = content.replace("<circle cx=\"${x2}\" cy=\"${y2}\" r=\"4\" fill=\"${strokeColor}\" />", "<circle cx=\"${x1}\" cy=\"${y1}\" r=\"3.5\" fill=\"#8C6D32\" />\n              <circle cx=\"${x2}\" cy=\"${y2}\" r=\"3.5\" fill=\"${strokeColor}\" />")

    # 5. Update focusOnProband() for true symmetrical centering
    old_focus = """    function focusOnProband() {
      const shell = document.getElementById('roadmapShell');
      const probandCard = document.querySelector('.rm-node[data-ahnentafel="1"]');
      zoom = 0.65;
      if (probandCard && shell) {
        const cardTop = parseFloat(probandCard.style.top || '450');
        panX = 40;
        panY = (shell.clientHeight / 2) - ((cardTop + 54) * zoom);
      } else {
        panX = 40;
        panY = 80;
      }
      applyRoadmapTransform();
    }"""

    new_focus = """    function focusOnProband() {
      const shell = document.getElementById('roadmapShell');
      const probandCard = document.querySelector('.rm-node[data-ahnentafel="1"]');
      if (!shell || !probandCard) return;
      const isMobile = window.innerWidth <= 860;
      zoom = isMobile ? 0.82 : 0.95;
      const cardLeft = parseFloat(probandCard.style.left || '80');
      const cardTop = parseFloat(probandCard.style.top || '450');
      const cardW = parseFloat(probandCard.style.width || '370');
      const cardH = 152;
      panX = (shell.clientWidth / 2) - ((cardLeft + cardW / 2) * zoom);
      panY = (shell.clientHeight / 2) - ((cardTop + cardH / 2) * zoom);
      applyRoadmapTransform();
    }"""

    if old_focus in content:
        content = content.replace(old_focus, new_focus)
        print("Replaced focusOnProband() successfully!")
    else:
        print("Searching focusOnProband via regex...")
        content = re.sub(
            r'function\s+focusOnProband\s*\(\)\s*\{[^}]*applyRoadmapTransform\(\);\s*\}',
            new_focus.strip(),
            content
        )

    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("index.astro patched successfully!")
    return True

if __name__ == "__main__":
    patch_index_astro()
