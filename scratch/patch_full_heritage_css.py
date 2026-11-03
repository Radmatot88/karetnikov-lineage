import re

with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace gate backgrounds
css = re.sub(
    r'\.fortress-gate\s*\{[^}]*background:\s*radial-gradient\([^}]*\);\s*transition:',
    '''.fortress-gate {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
  background:
    radial-gradient(circle at 20% 20%, rgba(122, 28, 28, 0.06) 0%, transparent 45%),
    radial-gradient(circle at 80% 80%, rgba(27, 77, 62, 0.05) 0%, transparent 45%),
    var(--bg-obsidian);
  transition:''',
    css
)

css = re.sub(
    r'\.gate-card\s*\{[^}]*background:\s*linear-gradient\([^;]*\);[^}]*\}',
    '''.gate-card {
  width: 100%;
  max-width: 480px;
  background: #FFFFFF;
  border: 1.5px solid var(--border-strong);
  border-radius: 20px;
  padding: 36px 32px;
  box-shadow: 0 16px 40px rgba(74, 66, 59, 0.16);
}''',
    css
)

# Password eye toggle button in gate
css = re.sub(
    r'\.gate-eye-btn\s*\{[^}]*\}',
    '''.gate-eye-btn {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 8px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  transition: color 0.15s ease;
}
.gate-eye-btn:hover {
  color: var(--gold-primary);
}''',
    css
)

# Replace dark input backgrounds
css = css.replace("background: rgba(7, 9, 14, 0.85);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.7);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.72);", "background: #FDFBF7;")
css = css.replace("background: rgba(7, 9, 14, 0.75);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.78);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.82);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.88);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.9);", "background: #FFFFFF;")
css = css.replace("background: rgba(7, 9, 14, 0.65);", "background: #FAF6EE;")

# Replace dark panels
css = css.replace("background: rgba(14, 18, 27, 0.94);", "background: rgba(237, 228, 212, 0.96);")
css = css.replace("background: rgba(14, 18, 27, 0.92);", "background: rgba(237, 228, 212, 0.95);")
css = css.replace("background: rgba(14, 18, 27, 0.96);", "background: rgba(237, 228, 212, 0.98);")
css = css.replace("background: rgba(14, 18, 27, 0.95);", "background: rgba(237, 228, 212, 0.97);")
css = css.replace("background: rgba(14, 18, 27, 0.9);", "background: #EDE4D4;")
css = css.replace("background: rgba(14, 18, 27, 0.85);", "background: #FAF6EE;")

# Replace gold gradients with Crimson buttons
css = css.replace(
    "background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 50%, #b8860b 100%);",
    "background: linear-gradient(135deg, #8B261E 0%, #7A1C1C 100%);"
)
css = css.replace(
    "background: linear-gradient(135deg, #f3dc8a 0%, #d4af37 100%);",
    "background: linear-gradient(135deg, #8B261E 0%, #7A1C1C 100%);"
)
css = css.replace(
    "color: #07090e;\n  background: linear-gradient(135deg, #8B261E 0%, #7A1C1C 100%);",
    "color: #FFFFFF;\n  background: linear-gradient(135deg, #8B261E 0%, #7A1C1C 100%);"
)

# Card linear gradients
css = re.sub(
    r'background:\s*linear-gradient\(165deg,\s*rgba\(20,\s*26,\s*38,\s*0\.9[268]\)[^;]*\);',
    'background: #FFFFFF;',
    css
)
css = re.sub(
    r'background:\s*linear-gradient\(160deg,\s*rgba\(22,\s*29,\s*43,\s*0\.9[268]\)[^;]*\);',
    'background: #FFFFFF;',
    css
)
css = re.sub(
    r'background:\s*linear-gradient\(155deg,\s*rgba\(20,\s*26,\s*38,\s*0\.9[268]\)[^;]*\);',
    'background: #FFFFFF;',
    css
)

# Update Mobile Bottom Nav
mob_nav_old = """.mobile-bottom-nav {
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
}"""

mob_nav_new = """.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 120;
  background: #FAF6EE;
  border-top: 1.5px solid var(--border-medium);
  padding: 6px 6px calc(6px + env(safe-area-inset-bottom, 0px)) 6px;
  box-shadow: 0 -4px 20px rgba(74, 66, 59, 0.12);
  justify-content: space-around;
  align-items: center;
}

.mob-nav-item {
  flex: 1;
  min-height: 48px;
  background: none;
  border: none;
  color: var(--text-secondary);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  padding: 6px 2px;
  border-radius: 10px;
  font-size: 11.5px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
  text-decoration: none;
}

.mob-nav-item .mob-nav-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
}

.mob-nav-item.active {
  color: #FFFFFF !important;
  background: var(--gold-primary);
  box-shadow: 0 2px 10px rgba(122, 28, 28, 0.35);
}

.mob-nav-item.active .svg-icon {
  stroke: #FFFFFF;
}

/* --- FAN CHART TOUCH INSPECTOR CARD --- */
.fan-mobile-card {
  margin: 16px auto 0 auto;
  max-width: 520px;
  padding: 16px;
  background: #FFFFFF;
  border: 1.5px solid var(--border-strong);
  border-radius: 14px;
  box-shadow: 0 4px 16px rgba(74, 66, 59, 0.08);
  display: flex;
  flex-direction: column;
  gap: 8px;
  text-align: left;
}

.fan-mobile-card-title {
  font-size: 17px;
  font-weight: 800;
  color: var(--gold-primary);
  display: flex;
  align-items: center;
  gap: 8px;
}

.fan-mobile-card-meta {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.45;
}

.fan-mobile-card-act {
  display: flex;
  gap: 10px;
  margin-top: 6px;
}"""

if mob_nav_old in css:
    css = css.replace(mob_nav_old, mob_nav_new)
    print("Replaced mobile-bottom-nav successfully")
else:
    print("WARNING: mob_nav_old not found")

# Update media query for <= 860px to fix topbar and drawer
mq_old = """@media (max-width: 860px) {
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
  }"""

mq_new = """@media (max-width: 860px) {
  .mobile-bottom-nav {
    display: flex;
  }

  .topbar {
    padding: 8px 12px;
    gap: 8px;
    overflow-x: hidden;
    height: 58px;
  }

  .brand-title {
    font-size: 15px;
    white-space: nowrap;
  }

  .brand-sub {
    display: none;
  }

  .nav-tabs {
    display: none;
  }

  .topbar-actions {
    width: auto;
    display: flex;
    align-items: center;
    gap: 6px;
    overflow: hidden;
    padding-bottom: 0;
  }

  /* Hide secondary desktop buttons on mobile topbar to prevent overflow */
  .topbar-actions #exportGedBtn,
  .topbar-actions #exportJsonBtn,
  .topbar-actions #openBranchWizardBtn {
    display: none !important;
  }

  .topbar-actions .btn-outline {
    padding: 6px 10px;
    font-size: 13px;
    white-space: nowrap;
    min-height: 38px;
  }

  /* Bottom Sheet Dossier Drawer on Mobile (Single Scrollbar) */
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
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: thin !important;
    background: #FAF6EE !important;
  }

  .dossier-drawer .dossier-body {
    overflow-y: visible !important;
    max-height: none !important;
  }

  .dossier-drawer.open {
    transform: translateY(0) !important;
  }"""

if mq_old in css:
    css = css.replace(mq_old, mq_new)
    print("Replaced responsive mobile media query successfully")
else:
    print("WARNING: mq_old not found")

with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Finished heritage.css modifications")
