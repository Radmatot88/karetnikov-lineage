#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path

css_file = Path(r"C:\Karetnikov_Lineage\src\styles\heritage.css")
content = css_file.read_text(encoding="utf-8")

new_css = """

/* ==================== 6. ДВУХРОЛЕВОЙ РЕЖИМ & НЕЙТРАЛЬНЫЕ БЕЙДЖИ ==================== */
.user-role-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.03em;
  transition: all 0.2s ease;
}

.user-role-badge.role-owner {
  background: rgba(212, 175, 55, 0.15);
  border: 1px solid var(--gold-primary);
  color: var(--gold-light);
  box-shadow: 0 0 12px rgba(212, 175, 55, 0.2);
}

.user-role-badge.role-relative {
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid #10b981;
  color: #6ee7b7;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.2);
}

/* ==================== 7. ПАРЯЩИЕ ОРБИТАЛЬНЫЕ ГИПОТЕЗЫ (FLOATING_HYPOTHESIS) ==================== */
.rm-node.floating-hypothesis-node {
  border: 2px dashed #f59e0b !important;
  background: linear-gradient(160deg, rgba(38, 28, 12, 0.96) 0%, rgba(18, 14, 10, 0.98) 100%) !important;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.65), 0 0 22px rgba(245, 158, 11, 0.18) !important;
}

.rm-node.floating-hypothesis-node:hover {
  transform: translateY(-3px) scale(1.015);
  border-color: #fbbf24 !important;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.8), 0 0 32px rgba(245, 158, 11, 0.45) !important;
}

.badge-floating-hyp {
  font-size: 9px;
  font-weight: 800;
  padding: 2px 7px;
  border-radius: 4px;
  background: rgba(245, 158, 11, 0.22);
  border: 1px solid rgba(245, 158, 11, 0.55);
  color: #fbbf24;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.canvas-hyp-banner {
  position: absolute;
  width: 310px;
  padding: 6px 12px;
  background: rgba(30, 22, 10, 0.92);
  border: 1px dashed rgba(245, 158, 11, 0.45);
  border-radius: 8px;
  text-align: center;
  font-size: 11px;
  font-weight: 800;
  color: #fbbf24;
  letter-spacing: 0.05em;
  pointer-events: none;
  box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}

/* ==================== 8. УМНОЕ ПРАВИЛО ЗАХОРОНЕНИЙ (НЕКРОПОЛЬ) ==================== */
.burial-row {
  margin-bottom: 14px;
}

.burial-inline-form {
  background: var(--bg-card);
  border: 1px solid rgba(212, 175, 55, 0.35);
  border-radius: var(--radius-sm);
  padding: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.4);
}

.add-burial-btn {
  width: 100%;
  text-align: center;
  color: var(--text-muted);
  border-style: dashed !important;
  border-color: rgba(212, 175, 55, 0.4) !important;
  padding: 8px 12px;
  transition: all 0.2s ease;
}

.add-burial-btn:hover {
  color: var(--gold-light);
  border-color: var(--gold-primary) !important;
  background: rgba(212, 175, 55, 0.12);
}

/* ==================== 9. КВОУМ ПОДТВЕРЖДЕНИЙ & ВОСПОМИНАНИЯ РОДСТВЕННИКОВ ==================== */
.quorum-box {
  margin: 14px 0;
  padding: 12px 14px;
  background: rgba(16, 185, 129, 0.09);
  border: 1px solid rgba(16, 185, 129, 0.28);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.btn-quorum {
  padding: 8px 16px;
  font-size: 12.5px;
  font-weight: 700;
  color: #6ee7b7;
  background: rgba(16, 185, 129, 0.18);
  border: 1px solid rgba(16, 185, 129, 0.45);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.btn-quorum:hover {
  background: rgba(16, 185, 129, 0.32);
  border-color: #34d399;
  transform: translateY(-1px);
}

.btn-quorum.confirmed {
  background: #10b981;
  color: #07090e;
  border-color: #10b981;
  box-shadow: 0 0 16px rgba(16, 185, 129, 0.4);
}

.quorum-hint {
  font-size: 11px;
  color: var(--text-muted);
}

.memories-section {
  margin-top: 18px;
  padding-top: 14px;
  border-top: 1px solid rgba(148, 163, 184, 0.15);
}

.memories-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 12px;
}

.memory-card {
  padding: 10px 12px;
  background: rgba(7, 9, 14, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-left: 3px solid #10b981;
  border-radius: 8px;
  font-size: 12.5px;
}

.memory-card-header {
  display: flex;
  justify-content: space-between;
  font-size: 11.5px;
  color: var(--gold-light);
  font-weight: 700;
  margin-bottom: 4px;
}

.memory-card-date {
  color: var(--text-dim);
  font-weight: normal;
  font-size: 10.5px;
}

.memory-card-text {
  color: var(--text-main);
  line-height: 1.45;
}

.add-memory-box {
  margin-top: 12px;
  padding: 14px;
  background: var(--bg-card);
  border: 1px dashed rgba(212, 175, 55, 0.35);
  border-radius: 12px;
}

/* ==================== 10. МОДАЛЬНЫЙ ВИЗАРД: ПРИСОЕДИНЕНИЕ ВЕТКИ ==================== */
.wizard-modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 9000;
  background: rgba(0, 0, 0, 0.78);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.wizard-modal-backdrop.open {
  display: flex;
}

.wizard-modal {
  width: 100%;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
  background: linear-gradient(165deg, rgba(20, 26, 38, 0.98) 0%, rgba(10, 13, 20, 0.99) 100%);
  border: 1px solid var(--border-strong);
  border-radius: 20px;
  padding: 28px 24px;
  box-shadow: var(--shadow-deep), 0 0 50px rgba(16, 185, 129, 0.1);
}

.wizard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}

.wizard-title {
  font-size: 17px;
  font-weight: 700;
  color: var(--gold-light);
}

.wizard-close {
  background: none;
  border: none;
  font-size: 18px;
  color: var(--text-muted);
  cursor: pointer;
  padding: 4px;
}

.wizard-close:hover {
  color: var(--text-main);
}

.wizard-steps-indicator {
  display: flex;
  gap: 6px;
  margin-bottom: 20px;
}

.step-pill {
  flex: 1;
  padding: 6px;
  border-radius: 8px;
  font-size: 11px;
  font-weight: 700;
  text-align: center;
  background: rgba(148, 163, 184, 0.1);
  color: var(--text-dim);
  border: 1px solid transparent;
  transition: all 0.2s;
}

.step-pill.active {
  background: rgba(16, 185, 129, 0.18);
  color: #6ee7b7;
  border-color: rgba(16, 185, 129, 0.45);
}

.step-pill.completed {
  background: rgba(212, 175, 55, 0.12);
  color: var(--gold-light);
  border-color: rgba(212, 175, 55, 0.3);
}

.wizard-step-pane {
  display: none;
}

.wizard-step-pane.active {
  display: block;
}

.wizard-label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  color: var(--text-main);
  margin-bottom: 8px;
}

.wizard-hint {
  font-size: 11.5px;
  color: var(--text-muted);
  margin-bottom: 16px;
  line-height: 1.45;
}

.rel-choice-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-bottom: 20px;
}

.rel-choice {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  background: var(--bg-card);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 10px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.15s;
}

.rel-choice:hover {
  border-color: var(--gold-primary);
  background: var(--bg-card-hover);
}

.rel-choice input[type="radio"]:checked + span {
  color: var(--gold-light);
}

.wizard-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 20px;
  padding-top: 14px;
  border-top: 1px solid rgba(148, 163, 184, 0.15);
}

.wizard-next-btn, .wizard-prev-btn {
  padding: 9px 18px;
  font-size: 13px;
  font-weight: 700;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.15s;
}

.wizard-next-btn {
  background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);
  color: #07090e;
  border: none;
}

.wizard-next-btn:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.wizard-prev-btn {
  background: var(--bg-card);
  color: var(--text-muted);
  border: 1px solid rgba(148, 163, 184, 0.25);
}

.wizard-prev-btn:hover {
  color: var(--text-main);
  border-color: var(--text-muted);
}

.wizard-summary-box {
  padding: 12px 14px;
  background: rgba(7, 9, 14, 0.75);
  border: 1px solid rgba(212, 175, 55, 0.25);
  border-radius: 8px;
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 12px;
  line-height: 1.5;
}

.wizard-success-box {
  text-align: center;
  padding: 24px 12px;
}
"""

if "user-role-badge" not in content:
    content += new_css
    css_file.write_text(content, encoding="utf-8")
    print("Successfully appended new styles to heritage.css!")
else:
    print("Styles already present.")
