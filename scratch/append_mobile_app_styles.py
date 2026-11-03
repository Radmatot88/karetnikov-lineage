#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Добавление стилей Нативного Мобильного Приложения («Мобильный Свиток Поколений»,
Bottom Tab Bar, Smart Kinship Path, Mobile Bottom Sheet и Touch 2D-Canvas) в src/styles/heritage.css.
"""

from pathlib import Path

css_file = Path(r"c:\Karetnikov_Lineage\src\styles\heritage.css")
content = css_file.read_text(encoding="utf-8")

mobile_css = '''

/* ==================== 11. НАТИВНОЕ МОБИЛЬНОЕ ПРИЛОЖЕНИЕ: СВИТОК ПОКОЛЕНИЙ (I -> VII) ==================== */

.scroll-app-container {
  max-width: 880px;
  margin: 0 auto;
  padding: 16px 16px 110px 16px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* Sticky Smart Header inside Scroll View */
.scroll-sticky-header {
  position: sticky;
  top: 0;
  z-index: 60;
  background: rgba(10, 14, 22, 0.94);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--border-strong);
  border-radius: 16px;
  padding: 12px 14px;
  box-shadow: 0 14px 36px rgba(0, 0, 0, 0.72);
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Smart Kinship Breadcrumb Path */
.kinship-path-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  overflow-x: auto;
  padding: 8px 10px;
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.14) 0%, rgba(16, 185, 129, 0.1) 100%);
  border: 1px solid rgba(212, 175, 55, 0.35);
  border-radius: 10px;
  font-size: 11.5px;
  scrollbar-width: none;
}
.kinship-path-bar::-webkit-scrollbar { display: none; }

.kinship-step-chip {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 9px;
  border-radius: 999px;
  background: rgba(7, 9, 14, 0.82);
  border: 1px solid rgba(212, 175, 55, 0.35);
  color: var(--text-main);
  font-weight: 700;
  font-size: 11px;
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.15s ease;
}
.kinship-step-chip:hover, .kinship-step-chip.active {
  background: var(--gold-primary);
  color: #07090e;
  border-color: var(--gold-light);
}
.kinship-arrow {
  color: var(--gold-primary);
  font-weight: 800;
  font-size: 12px;
  flex-shrink: 0;
}

/* Top Controls Row inside Scroll Sticky Header */
.scroll-controls-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
  justify-content: space-between;
}

.scroll-search-wrap {
  position: relative;
  flex: 1;
  min-width: 200px;
}

.scroll-search-input {
  width: 100%;
  padding: 9px 32px 9px 12px;
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

.scroll-search-clear {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 14px;
  padding: 4px;
}

/* Clan Filter Horizontal Scroll Pills */
.clan-pills-bar {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  padding-bottom: 2px;
  scrollbar-width: none;
}
.clan-pills-bar::-webkit-scrollbar { display: none; }

.clan-pill {
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 700;
  background: rgba(20, 26, 38, 0.85);
  border: 1px solid rgba(148, 163, 184, 0.2);
  color: var(--text-muted);
  white-space: nowrap;
  cursor: pointer;
  transition: all 0.15s ease;
}
.clan-pill.active {
  background: rgba(212, 175, 55, 0.2);
  border-color: var(--gold-primary);
  color: var(--gold-light);
  box-shadow: 0 0 12px rgba(212, 175, 55, 0.22);
}

/* Generation Quick Jump Bar (I - VII) */
.gen-jump-bar {
  display: flex;
  align-items: center;
  gap: 5px;
  overflow-x: auto;
  scrollbar-width: none;
}
.gen-jump-bar::-webkit-scrollbar { display: none; }

.gen-jump-btn {
  flex: 1;
  min-width: 38px;
  padding: 5px 8px;
  border-radius: 8px;
  background: rgba(7, 9, 14, 0.78);
  border: 1px solid rgba(148, 163, 184, 0.18);
  color: var(--text-muted);
  font-size: 11px;
  font-weight: 800;
  text-align: center;
  cursor: pointer;
  transition: all 0.15s ease;
}
.gen-jump-btn:hover, .gen-jump-btn.active {
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  color: #07090e;
  border-color: #d4af37;
}

/* Generation Section Block */
.scroll-gen-section {
  background: rgba(14, 18, 27, 0.78);
  border: 1px solid rgba(212, 175, 55, 0.22);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
}

.scroll-gen-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 16px;
  background: linear-gradient(90deg, rgba(28, 36, 52, 0.95) 0%, rgba(14, 18, 27, 0.95) 100%);
  border-bottom: 1px solid rgba(212, 175, 55, 0.18);
  cursor: pointer;
}

.scroll-gen-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 10px;
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  color: #07090e;
  font-weight: 900;
  font-size: 13px;
  margin-right: 10px;
  flex-shrink: 0;
}

.scroll-gen-title {
  font-size: 14.5px;
  font-weight: 800;
  color: var(--gold-light);
}

.scroll-gen-era {
  font-size: 11.5px;
  color: var(--text-muted);
}

.scroll-gen-cards {
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Individual Ancestor Native Card in Scroll */
.scroll-person-card {
  position: relative;
  background: var(--bg-card);
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-left: 4px solid var(--gold-primary);
  border-radius: 14px;
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  transition: all 0.25s ease;
}

.scroll-person-card.is-fact-card {
  border: 1.5px solid rgba(212, 175, 55, 0.65);
  border-left: 5px solid #10b981;
  background: linear-gradient(155deg, rgba(30, 26, 16, 0.96) 0%, rgba(16, 21, 32, 0.98) 100%);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.55), 0 0 18px rgba(212, 175, 55, 0.12);
}

.scroll-person-card.pulse-highlight {
  outline: 3px solid #f3dc8a;
  box-shadow: 0 0 35px rgba(243, 220, 138, 0.85) !important;
  transform: scale(1.01);
}

.spc-top {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}

.spc-avatar {
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
.spc-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.spc-avatar-initials {
  font-size: 18px;
  font-weight: 800;
  color: var(--gold-light);
}
.spc-cam-mini {
  position: absolute;
  bottom: 0;
  inset-inline: 0;
  background: rgba(0, 0, 0, 0.72);
  color: #f3dc8a;
  font-size: 9px;
  text-align: center;
  padding: 1px 0;
  font-weight: 700;
}

.spc-main {
  flex: 1;
  min-width: 0;
}

.spc-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 4px;
}

.spc-name {
  font-size: 15.5px;
  font-weight: 800;
  color: var(--text-main);
  line-height: 1.25;
}

.spc-role {
  font-size: 12px;
  color: var(--gold-light);
  font-weight: 600;
  margin-top: 2px;
}

.spc-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  font-size: 12px;
  color: var(--text-muted);
  margin-top: 4px;
}

.spc-notes {
  font-size: 12.5px;
  color: #cbd5e1;
  line-height: 1.48;
  background: rgba(7, 9, 14, 0.55);
  padding: 9px 11px;
  border-radius: 9px;
  border: 1px solid rgba(148, 163, 184, 0.1);
}

/* Smart Kinship Quick-Jump Pills inside each card */
.spc-kinship-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.kin-jump-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 5px 10px;
  border-radius: 8px;
  background: rgba(20, 28, 42, 0.9);
  border: 1px solid rgba(212, 175, 55, 0.28);
  color: var(--gold-light);
  font-size: 11px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
}
.kin-jump-pill:hover {
  background: rgba(212, 175, 55, 0.22);
  border-color: var(--gold-primary);
}

/* Card Action Buttons Footer */
.spc-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 8px;
  border-top: 1px solid rgba(148, 163, 184, 0.12);
}

.spc-btn {
  flex: 1;
  min-width: 110px;
  padding: 8px 10px;
  border-radius: 8px;
  font-size: 11.5px;
  font-weight: 700;
  text-align: center;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(148, 163, 184, 0.22);
  color: var(--text-main);
  transition: all 0.15s ease;
}
.spc-btn.primary {
  background: linear-gradient(135deg, rgba(212, 175, 55, 0.22) 0%, rgba(16, 185, 129, 0.18) 100%);
  border-color: var(--gold-primary);
  color: var(--gold-light);
}
.spc-btn:hover {
  background: rgba(212, 175, 55, 0.25);
  border-color: var(--gold-light);
}

/* ==================== 12. НАТИВНЫЙ MOBILE BOTTOM TAB BAR ==================== */
.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 180;
  background: rgba(8, 11, 18, 0.96);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-top: 1px solid var(--border-strong);
  padding: 6px 8px calc(6px + env(safe-area-inset-bottom, 0px)) 8px;
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.75);
  justify-content: space-around;
  align-items: center;
}

.mob-nav-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  padding: 6px 4px;
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 10.5px;
  font-weight: 700;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.mob-nav-item .mob-icon {
  font-size: 18px;
  line-height: 1;
}

.mob-nav-item.active {
  color: var(--gold-light);
  background: rgba(212, 175, 55, 0.14);
}

.mob-nav-item.accent-branch {
  color: #6ee7b7;
}

/* Mobile HUD Collapse Toggle on 2D Canvas */
.mobile-hud-toggle-btn {
  display: none;
  padding: 7px 12px;
  border-radius: 999px;
  background: rgba(14, 18, 27, 0.95);
  border: 1px solid var(--gold-primary);
  color: var(--gold-light);
  font-size: 11.5px;
  font-weight: 800;
  cursor: pointer;
  box-shadow: 0 6px 20px rgba(0,0,0,0.6);
}

/* Touch Action None for Smooth 2D Pan & Pinch Zoom */
.roadmap-shell {
  touch-action: none;
  user-select: none;
  -webkit-user-select: none;
}

/* 12 Rubrics Accordion inside Dossier Drawer */
.rubrics-12-details {
  margin: 14px 0;
  background: rgba(7, 9, 14, 0.65);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 12px;
  overflow: hidden;
}
.rubrics-12-summary {
  padding: 11px 14px;
  font-size: 12.5px;
  font-weight: 800;
  color: var(--gold-light);
  cursor: pointer;
  background: rgba(212, 175, 55, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.rubrics-12-grid {
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.rubric-mini-item {
  padding: 8px 10px;
  background: var(--bg-card);
  border-radius: 8px;
  border-left: 3px solid var(--gold-primary);
  font-size: 12px;
}
.rubric-mini-title {
  font-size: 10.5px;
  font-weight: 800;
  color: var(--gold-light);
  text-transform: uppercase;
  margin-bottom: 2px;
}

/* ==================== 13. МОБИЛЬНАЯ АДАПТАЦИЯ ЭКРАНОВ (<= 860px) ==================== */
@media (max-width: 860px) {
  .mobile-bottom-nav {
    display: flex;
  }

  .topbar {
    padding: 10px 14px;
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
  }

  .brand-title {
    font-size: 14.5px;
  }

  .brand-sub {
    font-size: 11px;
    display: none;
  }

  .nav-tabs {
    display: none; /* Заменено на нативный нижний Mobile Bottom Tab Bar */
  }

  .topbar-actions {
    display: flex;
    overflow-x: auto;
    gap: 6px;
    padding-bottom: 2px;
    scrollbar-width: none;
  }
  .topbar-actions::-webkit-scrollbar { display: none; }
  .topbar-actions .btn-outline {
    font-size: 11px;
    padding: 5px 9px;
    white-space: nowrap;
  }

  .roadmap-shell {
    height: calc(100vh - 125px);
  }

  .mobile-hud-toggle-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .roadmap-hud-top.hud-collapsed .hud-collapsible {
    display: none !important;
  }

  .roadmap-zoom-dock {
    bottom: 74px;
    left: 10px;
    right: 10px;
    justify-content: center;
    flex-wrap: wrap;
    padding: 6px 8px;
  }

  /* Нативная шторка Bottom Sheet для Досье на телефонах */
  .dossier-drawer {
    top: auto;
    bottom: 0;
    left: 0;
    right: 0;
    max-width: 100%;
    height: 88vh;
    border-left: none;
    border-top: 2px solid var(--gold-primary);
    border-radius: 22px 22px 0 0;
    padding: 16px 16px calc(80px + env(safe-area-inset-bottom, 0px)) 16px;
    transform: translateY(100%);
  }

  .dossier-drawer.open {
    transform: translateY(0);
  }

  .drawer-portrait-hero {
    flex-direction: row;
    padding: 12px;
  }

  .drawer-portrait-box {
    width: 72px;
    height: 72px;
    min-width: 72px;
  }

  .cards-grid {
    grid-template-columns: 1fr;
  }

  .padded-view {
    padding: 14px 14px 100px 14px;
  }
}
'''

if "НАТИВНОЕ МОБИЛЬНОЕ ПРИЛОЖЕНИЕ: СВИТОК ПОКОЛЕНИЙ" not in content:
    content += mobile_css
    css_file.write_text(content, encoding="utf-8")
    print("[OK] Appended Native Mobile App & Generation Scroll CSS to src/styles/heritage.css")
else:
    print("[INFO] Mobile CSS already present")
