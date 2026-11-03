#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Fixes CSS class names in src/styles/heritage.css so every button, pill, avatar,
   kinship bar, and mobile HUD collapse in src/pages/index.astro is styled as a native dark-gold app.
2. Formats node.fact_certificate and node.dossier_12_rubrics in src/pages/index.astro
   into human-readable Russian rubrics (eliminating [object Object]).
"""

from pathlib import Path

css_path = Path(r"c:\Karetnikov_Lineage\src\styles\heritage.css")
css_text = css_path.read_text(encoding="utf-8")

marker = "/* ==================== 11. НАТИВНОЕ МОБИЛЬНОЕ ПРИЛОЖЕНИЕ: СВИТОК ПОКОЛЕНИЙ (I -> VII) ==================== */"
assert marker in css_text, "Could not find Section 11 marker in heritage.css"
base_css = css_text.split(marker)[0]

aligned_mobile_css = """/* ==================== 11. НАТИВНОЕ МОБИЛЬНОЕ ПРИЛОЖЕНИЕ: СВИТОК ПОКОЛЕНИЙ (I -> VII) ==================== */

.scroll-app-container {
  max-width: 860px;
  margin: 0 auto;
  padding: 14px 14px 110px 14px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.scroll-sticky-header {
  position: sticky;
  top: 0;
  z-index: 60;
  background: rgba(10, 14, 22, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-strong);
  border-radius: 16px;
  padding: 12px 14px;
  box-shadow: 0 14px 34px rgba(0, 0, 0, 0.72);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Smart Kinship Path Breadcrumb */
.kinship-path-bar {
  display: none;
  flex-direction: column;
  gap: 6px;
  padding: 10px 12px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.14) 0%, rgba(212, 175, 55, 0.12) 100%);
  border: 1px solid rgba(16, 185, 129, 0.42);
}

.kinship-path-bar.visible {
  display: flex;
}

.kinship-path-title {
  font-size: 10.5px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #6ee7b7;
}

.kinship-path-steps {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  font-size: 12px;
}

.kinship-step {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(7, 9, 14, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.35);
  color: var(--text-main);
  font-weight: 700;
  font-size: 11.5px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.kinship-step.active-target {
  border-color: #10b981;
  background: rgba(16, 185, 129, 0.22);
  color: #6ee7b7;
}

.kinship-arrow {
  color: var(--gold-primary);
  font-weight: 800;
  font-size: 12px;
}

/* Search + Mode Row */
.scroll-search-row {
  display: flex;
  gap: 8px;
  align-items: center;
}

.scroll-search-wrap {
  position: relative;
  flex: 1;
}

.scroll-search-icon {
  position: absolute;
  left: 11px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 13px;
  pointer-events: none;
}

.scroll-search-input {
  width: 100%;
  padding: 9px 12px 9px 34px;
  border-radius: 10px;
  background: rgba(7, 9, 14, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.25);
  color: var(--text-main);
  font-size: 13px;
}

.scroll-search-input:focus {
  outline: none;
  border-color: var(--gold-primary);
  box-shadow: 0 0 0 2px rgba(212, 175, 55, 0.2);
}

/* Mode Toggle inside Scroll View */
.scroll-mode-switch {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
  background: rgba(7, 9, 14, 0.88);
  padding: 4px;
  border-radius: 11px;
  border: 1px solid rgba(148, 163, 184, 0.18);
}

.scroll-mode-btn {
  padding: 8px 10px;
  border-radius: 8px;
  border: 1px solid transparent;
  background: transparent;
  color: var(--text-muted);
  font-size: 12px;
  font-weight: 800;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: all 0.18s ease;
}

.scroll-mode-btn.active-facts {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.26) 0%, rgba(16, 185, 129, 0.14) 100%);
  border-color: #10b981;
  color: #6ee7b7;
  box-shadow: 0 2px 12px rgba(16, 185, 129, 0.22);
}

.scroll-mode-btn.active-all {
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  border-color: #d4af37;
  color: #07090e;
  box-shadow: 0 2px 12px rgba(212, 175, 55, 0.3);
}

.badge-count {
  padding: 1px 6px;
  border-radius: 999px;
  background: rgba(0, 0, 0, 0.35);
  font-size: 10.5px;
  font-weight: 900;
}

/* Clan Filter Chips */
.scroll-clan-pills {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding-bottom: 2px;
  scrollbar-width: none;
}
.scroll-clan-pills::-webkit-scrollbar { display: none; }

.scroll-clan-pill {
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(18, 24, 36, 0.88);
  color: var(--text-muted);
  font-size: 11.5px;
  font-weight: 700;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.15s ease;
}

.scroll-clan-pill.active {
  background: rgba(212, 175, 55, 0.22);
  border-color: var(--gold-primary);
  color: var(--gold-light);
  box-shadow: 0 0 12px rgba(212, 175, 55, 0.2);
}

/* Generation Quick-Jump Bar (I - VII) */
.scroll-gen-jumpbar {
  display: flex;
  align-items: center;
  gap: 5px;
  overflow-x: auto;
  scrollbar-width: none;
}
.scroll-gen-jumpbar::-webkit-scrollbar { display: none; }

.jumpbar-label {
  font-size: 10.5px;
  color: var(--text-dim);
  font-weight: 800;
  text-transform: uppercase;
  margin-right: 2px;
  white-space: nowrap;
}

.gen-jump-btn {
  padding: 5px 10px;
  border-radius: 8px;
  background: rgba(7, 9, 14, 0.85);
  border: 1px solid rgba(212, 175, 55, 0.25);
  color: var(--gold-light);
  font-size: 11.5px;
  font-weight: 800;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s ease;
}

.gen-jump-btn:hover, .gen-jump-btn.active {
  background: var(--gold-primary);
  color: #07090e;
  border-color: var(--gold-light);
}

/* Generation Section Block */
.scroll-gen-section {
  display: flex;
  flex-direction: column;
  gap: 10px;
  scroll-margin-top: 230px;
  margin-bottom: 14px;
}

.scroll-gen-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 14px;
  border-radius: 12px;
  background: linear-gradient(90deg, rgba(212, 175, 55, 0.16) 0%, rgba(14, 18, 27, 0.92) 100%);
  border: 1px solid rgba(212, 175, 55, 0.35);
}

.scroll-gen-title {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  font-weight: 800;
  color: var(--gold-light);
}

.gen-roman-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 32px;
  height: 28px;
  padding: 0 8px;
  border-radius: 7px;
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  color: #07090e;
  font-size: 12.5px;
  font-weight: 900;
}

.scroll-gen-stats {
  font-size: 11.5px;
  color: var(--text-muted);
  font-weight: 700;
}

/* Native Ancestor Card in Scroll */
.scroll-person-card {
  background: linear-gradient(155deg, rgba(20, 26, 38, 0.96) 0%, rgba(11, 15, 23, 0.98) 100%);
  border: 1px solid rgba(148, 163, 184, 0.22);
  border-left: 5px solid var(--gold-primary);
  border-radius: 16px;
  padding: 14px;
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.55);
  display: flex;
  flex-direction: column;
  gap: 11px;
  transition: all 0.2s ease;
  scroll-margin-top: 240px;
}

.scroll-person-card.branch-paternal {
  border-left-color: #e07a5f;
}

.scroll-person-card.branch-maternal {
  border-left-color: #2a9d8f;
}

.scroll-person-card.is-fact-card {
  border-color: rgba(212, 175, 55, 0.55);
  border-left: 5px solid #10b981;
  background: linear-gradient(155deg, rgba(28, 25, 16, 0.97) 0%, rgba(13, 18, 27, 0.99) 100%);
}

.scroll-person-card.is-hyp-card {
  border: 1.5px dashed #f59e0b;
  border-left: 5px solid #f59e0b;
  background: linear-gradient(155deg, rgba(36, 26, 12, 0.96) 0%, rgba(15, 13, 10, 0.98) 100%);
}

.scroll-person-card.highlight-target {
  outline: 3px solid #f3dc8a;
  box-shadow: 0 0 32px rgba(243, 220, 138, 0.75);
}

.scroll-card-top {
  display: flex;
  gap: 13px;
  align-items: flex-start;
}

.scroll-avatar {
  width: 62px;
  height: 62px;
  min-width: 62px;
  border-radius: 14px;
  background: #090d14;
  border: 2px solid var(--gold-primary);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  cursor: pointer;
}

.scroll-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.scroll-avatar-cam {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.75);
  color: var(--gold-light);
  font-size: 9px;
  text-align: center;
  padding: 2px 0;
  font-weight: 700;
}

.scroll-person-main {
  flex: 1;
  min-width: 0;
}

.scroll-badges-row {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  margin-bottom: 5px;
}

.scroll-person-name {
  font-size: 16px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.25;
  margin-bottom: 3px;
}

.scroll-person-role {
  font-size: 12px;
  color: var(--gold-light);
  font-weight: 600;
  margin-bottom: 4px;
}

.scroll-person-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 12px;
  color: var(--text-muted);
}

.scroll-person-bio {
  font-size: 12.5px;
  color: #cbd5e1;
  line-height: 1.5;
  padding: 9px 11px;
  border-radius: 10px;
  background: rgba(7, 9, 14, 0.65);
  border-left: 3px solid rgba(212, 175, 55, 0.45);
}

/* Smart Kinship Quick-Jump Pills inside each card */
.scroll-kinship-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.kinship-pill {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 10px;
  border-radius: 8px;
  background: rgba(15, 22, 34, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.25);
  color: var(--text-main);
  font-size: 11.5px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

.kinship-pill:hover {
  border-color: var(--gold-primary);
  background: rgba(212, 175, 55, 0.15);
  color: var(--gold-light);
}

.kinship-pill .kp-name {
  color: var(--gold-light);
  font-weight: 700;
}

/* Card Action Bar */
.scroll-card-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  padding-top: 6px;
  border-top: 1px solid rgba(148, 163, 184, 0.14);
}

.scroll-act-btn {
  padding: 7px 12px;
  border-radius: 8px;
  border: 1px solid rgba(148, 163, 184, 0.25);
  background: rgba(14, 18, 27, 0.85);
  color: var(--text-main);
  font-size: 11.5px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  transition: all 0.15s ease;
}

.scroll-act-btn:hover {
  border-color: var(--gold-primary);
  color: var(--gold-light);
}

.scroll-act-btn.primary-act {
  background: rgba(212, 175, 55, 0.16);
  border-color: rgba(212, 175, 55, 0.5);
  color: var(--gold-light);
}

/* 12 Rubrics Accordion inside Dossier Drawer */
.rubrics-12-details {
  margin: 12px 0;
  background: rgba(7, 9, 14, 0.72);
  border: 1px solid rgba(212, 175, 55, 0.35);
  border-radius: 10px;
  overflow: hidden;
}

.rubrics-12-details summary {
  padding: 10px 14px;
  font-size: 12.5px;
  font-weight: 800;
  color: var(--gold-light);
  cursor: pointer;
  user-select: none;
  background: rgba(212, 175, 55, 0.1);
}

.rubrics-12-grid {
  padding: 12px 14px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 12px;
}

.rubric-row {
  padding-bottom: 7px;
  border-bottom: 1px dashed rgba(148, 163, 184, 0.16);
}
.rubric-row:last-child { border-bottom: none; padding-bottom: 0; }
.rubric-key {
  font-size: 10.5px;
  font-weight: 800;
  color: var(--gold-primary);
  text-transform: uppercase;
  margin-bottom: 2px;
}
.rubric-val {
  color: var(--text-main);
  line-height: 1.45;
}

/* ==================== 12. FIXED MOBILE BOTTOM TAB BAR ==================== */
.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 95;
  background: rgba(8, 11, 18, 0.96);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-top: 1px solid rgba(212, 175, 55, 0.35);
  padding: 6px 8px calc(6px + env(safe-area-inset-bottom, 0px)) 8px;
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.75);
  justify-content: space-around;
  align-items: center;
}

.mob-nav-item {
  flex: 1;
  background: none;
  border: none;
  color: var(--text-muted);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  padding: 6px 4px;
  border-radius: 10px;
  font-size: 10.5px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}

.mob-nav-item .mob-nav-icon {
  font-size: 17px;
  line-height: 1;
}

.mob-nav-item.active {
  color: #07090e;
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  box-shadow: 0 2px 10px rgba(212, 175, 55, 0.35);
}

.mobile-hud-toggle-btn {
  display: none;
  position: absolute;
  top: 12px;
  left: 12px;
  z-index: 45;
  padding: 8px 14px;
  border-radius: 999px;
  background: rgba(14, 18, 27, 0.95);
  border: 1px solid var(--gold-primary);
  color: var(--gold-light);
  font-size: 12px;
  font-weight: 800;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.65);
  cursor: pointer;
}

.roadmap-shell {
  touch-action: none;
  user-select: none;
  -webkit-user-select: none;
}

/* ==================== 13. RESPONSIVE MOBILE RULES (<= 860px) ==================== */
@media (max-width: 860px) {
  .mobile-bottom-nav {
    display: flex;
  }

  .topbar {
    padding: 10px 12px;
    gap: 8px;
  }

  .brand-title {
    font-size: 14px;
  }

  .brand-sub {
    display: none;
  }

  .nav-tabs {
    display: none;
  }

  .topbar-actions {
    width: 100%;
    justify-content: space-between;
    overflow-x: auto;
    padding-bottom: 2px;
  }

  .topbar-actions .btn-outline {
    padding: 6px 9px;
    font-size: 11px;
    white-space: nowrap;
  }

  /* Bottom Sheet Dossier Drawer on Mobile */
  .dossier-drawer {
    width: 100% !important;
    max-width: 100% !important;
    top: auto !important;
    bottom: 0 !important;
    height: 88vh !important;
    border-left: none !important;
    border-top: 2px solid var(--gold-primary) !important;
    border-radius: 22px 22px 0 0 !important;
    transform: translateY(105%) !important;
    padding: 18px 16px 90px 16px !important;
  }

  .dossier-drawer.open {
    transform: translateY(0) !important;
  }

  /* Collapsible HUD on 2D Canvas for Mobile */
  .mobile-hud-toggle-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .roadmap-hud-top {
    top: 52px;
    left: 10px;
    right: 10px;
    display: none;
    max-height: 60vh;
    overflow-y: auto;
  }

  .roadmap-hud-top.hud-expanded {
    display: flex;
  }

  .roadmap-zoom-dock {
    bottom: 74px;
    left: 10px;
    right: 10px;
    justify-content: space-between;
    overflow-x: auto;
  }

  .roadmap-shell {
    height: calc(100vh - 115px);
  }
}
"""

css_path.write_text(base_css + aligned_mobile_css, encoding="utf-8")
print("[OK] Aligned all Mobile App CSS classes in src/styles/heritage.css")

# Now update src/pages/index.astro to format node.fact_certificate and node.dossier_12_rubrics cleanly
astro_path = Path(r"c:\Karetnikov_Lineage\src\pages\index.astro")
astro_text = astro_path.read_text(encoding="utf-8")

old_cert_and_rubrics = """      const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
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
      }"""

new_cert_and_rubrics = """      const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
      const fc = node.fact_certificate;
      const fcText = (fc && typeof fc === 'object')
        ? `${fc.archive_code ? fc.archive_code + ' • ' : ''}${fc.doc_basis || ''}`
        : (fc || 'Верифицировано прямыми документами ЗАГС, военными фондами и свидетельствами семьи.');

      const factCertHtml = isFactConfirmed ? `
        <div style="padding:10px 12px; border-radius:10px; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.45); margin-bottom:12px; font-size:12px; color:#6ee7b7;">
          <strong>🛡️ АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ</strong><br/>
          <span style="color:#cbd5e1; font-size:11.5px;">${fcText}</span>
        </div>
      ` : '';

      const RUBRIC_TITLES_RU = {
        rubric_01_naming: '1. Имянаречение и родовая фамилия',
        rubric_02_worldview: '2. Вероисповедание и приходская традиция',
        rubric_03_life_milestones: '3. Вехи жизни и брачный союз',
        rubric_04_ancestral_cradle: '4. Родовое гнездо и пути переселения',
        rubric_05_life_work: '5. Дело жизни, сословие и ремесло',
        rubric_06_military_service: '6. Воинское служение и награды',
        rubric_07_crafts_and_skills: '7. Мастерство и хозяйственные таланты',
        rubric_08_personality_and_lore: '8. Характер и живая память рода',
        rubric_09_family_and_children: '9. Семья, супружество и дети',
        rubric_10_historical_trials: '10. Исторические испытания эпохи',
        rubric_11_relics_and_photos: '11. Семейные реликвии и фотоархив',
        rubric_12_citations_and_archives: '12. Архивные шифры и первоисточники'
      };

      function formatRubricVal(val) {
        if (!val) return 'Уточняется в архивах';
        if (typeof val === 'string') return val;
        if (Array.isArray(val)) return val.filter(Boolean).join('; ') || 'Уточняется';
        if (typeof val === 'object') {
          const parts = [];
          Object.entries(val).forEach(([subK, subV]) => {
            if (!subV || subK === 'is_alive' || subK === 'primary_tradition' || subK === 'photo_url') return;
            if (Array.isArray(subV)) {
              if (subV.length > 0) parts.push(subV.join(', '));
            } else if (typeof subV === 'string' && subV.trim()) {
              parts.push(subV.trim());
            }
          });
          return parts.join(' • ') || 'Уточняется в архивах';
        }
        return String(val);
      }

      let rubrics12Html = '';
      if (node.dossier_12_rubrics && typeof node.dossier_12_rubrics === 'object') {
        const rubricEntries = Object.entries(node.dossier_12_rubrics).map(([k, v]) => `
          <div class="rubric-row">
            <div class="rubric-key">${RUBRIC_TITLES_RU[k] || k}</div>
            <div class="rubric-val">${formatRubricVal(v)}</div>
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
      }"""

assert old_cert_and_rubrics in astro_text, "Could not find old_cert_and_rubrics in index.astro"
astro_text = astro_text.replace(old_cert_and_rubrics, new_cert_and_rubrics, 1)
astro_path.write_text(astro_text, encoding="utf-8")
print("[OK] Updated openDossier 12 Rubrics & Fact Certificate formatting in src/pages/index.astro")
