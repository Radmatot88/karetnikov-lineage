import re

def update_css():
    with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
        css = f.read()

    # Replace .rm-node and related classes with the aristocratic specification
    old_rm_block = re.search(r'/\* ================= ROADMAP NODE CARD WITH PHOTO PORTRAIT ================= \*/.*?/\* ================= FAN CHART & ARCHIVE RADAR ================= \*/', css, re.DOTALL)
    if not old_rm_block:
        print("Error: Could not locate rm-node block in CSS")
        return False

    new_rm_css = """/* ================= ROADMAP NODE CARD WITH PHOTO PORTRAIT (IMPERIAL ARCHITECTURAL) ================= */
.rm-node {
  position: absolute;
  width: 350px;
  border-radius: 14px;
  border: 1.5px solid #8C6D32;
  background: #FFFFFF;
  box-shadow: 0 4px 16px rgba(74, 66, 59, 0.08), 0 0 0 1px rgba(140, 109, 50, 0.12);
  display: flex;
  flex-direction: column;
  padding: 10px 14px 12px;
  gap: 8px;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.2, 0, 0, 1), box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), border-color 0.2s ease;
  user-select: none;
  box-sizing: border-box;
}

.rm-node:hover {
  transform: translateY(-3px) scale(1.01);
  border-color: #7A1C1C;
  box-shadow: 0 12px 30px rgba(122, 28, 28, 0.15), 0 0 0 1.5px rgba(122, 28, 28, 0.3);
}

/* Proband Imperial Sovereign Card (#1 - Граф Каретников) */
.rm-node.proband-node {
  width: 370px !important;
  background: linear-gradient(180deg, #FFFFFF 0%, #FDFBF7 100%) !important;
  border: 2px solid #7A1C1C !important;
  box-shadow: 0 8px 30px rgba(122, 28, 28, 0.18), 0 0 0 2px rgba(140, 109, 50, 0.28) !important;
  border-radius: 16px !important;
  padding: 12px 16px 14px !important;
}

.rm-node.proband-node:hover {
  transform: translateY(-3px) scale(1.015) !important;
  box-shadow: 0 16px 40px rgba(122, 28, 28, 0.28), 0 0 0 2.5px #7A1C1C !important;
}

.rm-proband-crown-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-bottom: 8px;
  border-bottom: 1.5px solid rgba(140, 109, 50, 0.25);
  margin-bottom: 4px;
}

.rm-proband-crown-title {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 800;
  color: #7A1C1C;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.rm-card-top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 6px;
  padding-bottom: 6px;
  border-bottom: 1px solid rgba(124, 94, 36, 0.18);
}

.rm-card-body {
  display: flex;
  align-items: center;
  gap: 12px;
}

.rm-node.collateral-node {
  border-style: dashed;
  border-color: #8C6D32;
  background: #FFFFFF;
}

.rm-node.status-CONFIRMED_DOC {
  border-top: 3px solid #146C43;
}
.rm-node.status-FAMILY_ORAL {
  border-top: 3px solid #1D4ED8;
}
.rm-node.status-ARCHIVE_CANDIDATE {
  border-top: 3px solid #B45309;
}
.rm-node.status-UNKNOWN_SLOT {
  border-top: 2px dashed #94A3B8;
  opacity: 0.88;
}

/* Portrait Cameo Medallion inside node */
.rm-portrait {
  position: relative;
  width: 58px;
  height: 58px;
  min-width: 58px;
  border-radius: 12px;
  background: #FAF6EE;
  border: 1.5px solid #8C6D32;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: inset 0 1px 4px rgba(74, 66, 59, 0.1);
}

.rm-portrait.proband-portrait {
  width: 66px;
  height: 66px;
  min-width: 66px;
  border-radius: 50%;
  border: 2px solid #8C6D32;
  background: #FAF6EE;
  box-shadow: 0 2px 8px rgba(140, 109, 50, 0.2), inset 0 1px 4px rgba(0,0,0,0.06);
}

.rm-portrait img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.rm-portrait-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: Georgia, serif;
  color: #7A1C1C;
  font-size: 19px;
  font-weight: 800;
}

.rm-photo-badge {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(26, 23, 21, 0.85);
  color: #FFFFFF;
  font-size: 8.5px;
  font-weight: 700;
  text-align: center;
  padding: 1.5px 0;
  opacity: 0.88;
  transition: opacity 0.15s, background 0.15s;
}

.rm-portrait:hover .rm-photo-badge {
  opacity: 1;
  background: #7A1C1C;
}

.rm-content {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.rm-proband-clan {
  font-size: 9.5px;
  font-weight: 800;
  color: #8C6D32;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}

.ahnentafel-badge {
  font-size: 10.5px;
  font-weight: 800;
  padding: 2.5px 7px;
  border-radius: 6px;
  background: #FAF6EE;
  border: 1px solid rgba(140, 109, 50, 0.35);
  color: #7A1C1C;
}

.badge-fact-100 {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2.5px 7px;
  border-radius: 6px;
  background: #EDF7F1;
  border: 1px solid #146C43;
  color: #146C43;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}

.branch-tag {
  font-size: 10px;
  padding: 2px 7px;
  border-radius: 6px;
  font-weight: 700;
}

.branch-tag.paternal {
  background: rgba(122, 28, 28, 0.08);
  color: #7A1C1C;
  border: 1px solid rgba(122, 28, 28, 0.22);
}

.branch-tag.maternal {
  background: #EDF7F1;
  color: #146C43;
  border: 1px solid rgba(20, 108, 67, 0.25);
}

.branch-tag.proband {
  background: rgba(140, 109, 50, 0.12);
  color: #7C5E24;
  border: 1px solid rgba(140, 109, 50, 0.3);
}

.rm-name {
  font-size: 15px;
  font-weight: 800;
  color: #1A1715;
  margin: 1px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.25;
}

.rm-name.proband-name {
  font-size: 16.5px;
  color: #1A1715;
  letter-spacing: 0.01em;
}

.rm-role-sub {
  font-size: 11px;
  font-weight: 700;
  color: #7A1C1C;
  line-height: 1.2;
}

.rm-meta-row, .rm-dates, .rm-place {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11.5px;
  color: #4A423B;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.rm-place {
  color: #5C5248;
}

/* Generation Column Header Plaque */
.canvas-gen-banner {
  position: absolute;
  width: 350px;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 16px;
  background: #FFFFFF;
  border: 1.5px solid #8C6D32;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(74, 66, 59, 0.08);
  pointer-events: none;
  z-index: 5;
  box-sizing: border-box;
  white-space: nowrap;
}

.gen-banner-badge {
  width: 32px;
  height: 32px;
  min-width: 32px;
  border-radius: 50%;
  background: #FAF6EE;
  border: 1.5px solid #8C6D32;
  color: #7A1C1C;
  font-weight: 800;
  font-size: 13px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.gen-banner-titles {
  flex: 1;
  min-width: 0;
  overflow: hidden;
}

.canvas-gen-banner .t1 {
  font-size: 11px;
  font-weight: 800;
  color: #7A1C1C;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.canvas-gen-banner .t2 {
  font-size: 12.5px;
  font-weight: 700;
  color: #1A1715;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Floating Zoom Dock Bottom-Center */
.roadmap-zoom-dock {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 30;
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(12px);
  border: 1.5px solid #8C6D32;
  border-radius: 999px;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 8px 24px rgba(74, 66, 59, 0.15);
}

"""

    css = css[:old_rm_block.start()] + new_rm_css + css[old_rm_block.end()-47:]
    with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated src/styles/heritage.css successfully!")
    return True

if __name__ == "__main__":
    update_css()
