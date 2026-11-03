#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

css_file = Path(r"c:\Karetnikov_Lineage\src\styles\heritage.css")
content = css_file.read_text(encoding="utf-8")

css_addon = '''

/* ==================== ПАКЕТ: РЕЖИМ ТОЛЬКО ФАКТЫ (100% ФАКТ) ==================== */

/* 1. Сегментированный переключатель HUD */
.mode-toggle-panel {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(14, 18, 27, 0.96);
  border: 1px solid var(--border-strong);
  border-radius: var(--radius-md);
  padding: 6px 12px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7), 0 0 20px rgba(212, 175, 55, 0.12);
}

.epistemic-segmented-control {
  display: inline-flex;
  align-items: center;
  background: rgba(7, 9, 14, 0.85);
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 10px;
  padding: 3px;
  gap: 4px;
}

.seg-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 6px 12px;
  font-size: 12px;
  font-weight: 700;
  color: var(--text-muted);
  background: transparent;
  border: 1px solid transparent;
  border-radius: 7px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.seg-btn:hover {
  color: var(--text-main);
  background: rgba(255, 255, 255, 0.04);
}

.seg-btn.active {
  color: #07090e;
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  border-color: #d4af37;
  box-shadow: 0 2px 10px rgba(212, 175, 55, 0.35);
}

.seg-btn.active .seg-counter {
  background: #07090e;
  color: #f3dc8a;
}

.seg-counter {
  font-size: 10.5px;
  padding: 1px 6px;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.18);
  color: var(--text-muted);
  font-weight: 800;
  transition: all 0.2s ease;
}

.seg-gem {
  width: 7px;
  height: 7px;
  border-radius: 50%;
}
.seg-gem.gold-gem { background: #10b981; box-shadow: 0 0 6px #10b981; }
.seg-gem.cyan-gem { background: #38bdf8; box-shadow: 0 0 6px #38bdf8; }

.mode-live-pill {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.3);
  border-radius: 999px;
  font-size: 11px;
  font-weight: 800;
  color: #34d399;
  letter-spacing: 0.04em;
}

.pill-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
}

.pill-dot.pulse {
  animation: pulseDot 2s infinite ease-in-out;
}

@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 0.9; }
  50% { transform: scale(1.4); opacity: 0.4; }
}

/* 2. Карточки подтвержденных персон в режиме «Только факты» */
.rm-node.is-fact-confirmed {
  border: 2px solid #d4af37 !important;
  border-left: 5px solid #10b981 !important;
  background: linear-gradient(155deg, rgba(32, 27, 16, 0.98) 0%, rgba(14, 18, 27, 0.98) 100%) !important;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.7), 0 0 24px rgba(212, 175, 55, 0.3) !important;
}

.rm-node.is-fact-confirmed:hover {
  transform: translateY(-3px) scale(1.015);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.8), 0 0 32px rgba(212, 175, 55, 0.5) !important;
}

.badge-fact-100 {
  font-size: 9.5px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid rgba(16, 185, 129, 0.45);
  color: #6ee7b7;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  display: inline-flex;
  align-items: center;
  gap: 3px;
}

/* 3. Компактные слоты ожидания архивной выписки */
.rm-node.is-pending-fact {
  height: 52px !important;
  padding: 8px 12px !important;
  background: rgba(14, 18, 27, 0.5) !important;
  border: 1px dashed rgba(212, 175, 55, 0.28) !important;
  border-left: 3px solid rgba(148, 163, 184, 0.3) !important;
  opacity: 0.65;
  box-shadow: none !important;
}

.rm-node.is-pending-fact:hover {
  opacity: 0.95;
  border-color: #d4af37 !important;
}

.rm-node.is-pending-fact .rm-portrait {
  width: 34px !important;
  height: 34px !important;
  min-width: 34px !important;
}

.rm-node.is-pending-fact .rm-name {
  font-size: 11.5px !important;
  color: var(--text-muted) !important;
}

.rm-node.is-pending-fact .rm-dates,
.rm-node.is-pending-fact .rm-place,
.rm-node.is-pending-fact .rm-photo-badge {
  display: none !important;
}

/* 4. Монолитная колонка «Архивный горизонт V–VII колен» */
.facts-horizon-column {
  position: absolute;
  width: 360px;
  padding: 20px;
  background: linear-gradient(165deg, rgba(20, 26, 38, 0.92) 0%, rgba(10, 13, 20, 0.95) 100%);
  border: 1px solid var(--border-strong);
  border-radius: 16px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), 0 0 28px rgba(212, 175, 55, 0.1);
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.facts-horizon-title {
  font-size: 14px;
  font-weight: 800;
  color: var(--gold-light);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.facts-horizon-card {
  padding: 10px 12px;
  background: rgba(7, 9, 14, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.16);
  border-radius: 8px;
  font-size: 11.5px;
}

.facts-horizon-card strong {
  color: var(--gold-primary);
}

/* 5. Гербовый сертификат достоверности в Dossier Drawer */
.fact-guarantee-banner {
  margin-bottom: 16px;
  padding: 12px 14px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(212, 175, 55, 0.1) 100%);
  border: 1px solid rgba(16, 185, 129, 0.4);
  border-radius: 12px;
}

.fact-guarantee-badge {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cert-shield {
  font-size: 26px;
}

.cert-title {
  font-size: 12px;
  font-weight: 800;
  color: #6ee7b7;
  letter-spacing: 0.04em;
}

.cert-desc {
  font-size: 11px;
  color: var(--text-muted);
  margin-top: 2px;
}
'''

if "/* ==================== ПАКЕТ: РЕЖИМ ТОЛЬКО ФАКТЫ (100% ФАКТ) ==================== */" not in content:
    content += css_addon
    css_file.write_text(content, encoding="utf-8")
    print("[OK] Appended facts styles to src/styles/heritage.css")
else:
    print("[INFO] Styles already present in src/styles/heritage.css")
