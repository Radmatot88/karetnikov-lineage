with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
    css = f.read()

target = """.mobile-bottom-nav {
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
  color: #FFFFFF;
  background: linear-gradient(135deg, #8B261E 0%, #7A1C1C 100%);
  box-shadow: 0 2px 10px rgba(212, 175, 55, 0.35);
}"""

replacement = """.mobile-bottom-nav {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 120;
  background: #FAF6EE;
  border-top: 1.5px solid var(--border-medium);
  padding: 6px 4px calc(6px + env(safe-area-inset-bottom, 0px)) 4px;
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
  font-size: 11px;
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

# Normalize CRLF
target_norm = target.replace("\r\n", "\n")
css_norm = css.replace("\r\n", "\n")

if target_norm in css_norm:
    css_norm = css_norm.replace(target_norm, replacement)
    with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
        f.write(css_norm)
    print("Replaced .mobile-bottom-nav successfully!")
else:
    print("Target not found even with norm")
