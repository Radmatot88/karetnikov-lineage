import re

def refine_styles():
    with open("src/styles/heritage.css", "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Update proband name wrapping and styling
    css = re.sub(
        r'\.rm-name\.proband-name\s*\{[^}]*\}',
        """.rm-name.proband-name {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 15.5px;
  font-weight: 800;
  color: #1A1715;
  letter-spacing: 0.01em;
  white-space: normal;
  line-height: 1.25;
}""",
        css
    )

    # 2. Refine mobile-hud-toggle-btn shadow and appearance
    css = re.sub(
        r'\.mobile-hud-toggle-btn\s*\{[^}]*\}',
        """.mobile-hud-toggle-btn {
  display: none;
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 45;
  padding: 8px 14px;
  border-radius: 999px;
  background: #FFFFFF;
  border: 1.5px solid #8C6D32;
  color: #7A1C1C;
  font-size: 12px;
  font-weight: 800;
  box-shadow: 0 4px 14px rgba(74, 66, 59, 0.12);
  cursor: pointer;
  align-items: center;
  gap: 6px;
}""",
        css
    )

    # 3. Refine roadmap-zoom-dock styling for perfect responsive mobile centering
    css = re.sub(
        r'/\* Floating Zoom Dock Bottom-Center \*/\s*\.roadmap-zoom-dock\s*\{[^}]*\}',
        """/* Floating Zoom Dock Bottom-Center */
.roadmap-zoom-dock {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 30;
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(12px);
  border: 1.5px solid #8C6D32;
  border-radius: 999px;
  padding: 4px 8px;
  display: flex;
  align-items: center;
  gap: 6px;
  box-shadow: 0 6px 20px rgba(74, 66, 59, 0.14);
  max-width: calc(100vw - 24px);
  box-sizing: border-box;
}

@media (max-width: 640px) {
  .roadmap-zoom-dock {
    gap: 4px;
    padding: 3px 6px;
  }
  .zoom-btn {
    width: 28px;
    height: 28px;
    font-size: 14px;
    border-radius: 6px;
    background: #FAF6EE;
    border: 1px solid rgba(140, 109, 50, 0.3);
    color: #7A1C1C;
  }
  .zoom-readout {
    width: 36px;
    font-size: 11px;
    font-weight: 800;
    color: #1A1715;
  }
  .roadmap-zoom-dock .chip-btn {
    padding: 5px 9px;
    font-size: 11px;
    font-weight: 700;
    background: #FAF6EE;
    border: 1px solid rgba(140, 109, 50, 0.35);
    color: #1A1715;
    border-radius: 6px;
  }
}""",
        css
    )

    with open("src/styles/heritage.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Refined heritage.css successfully!")

def refine_index_astro():
    with open("src/pages/index.astro", "r", encoding="utf-8") as f:
        content = f.read()

    # Refine zoom dock button labels
    content = content.replace(
        '<button id="zoomResetBtn" class="chip-btn" title="Сфокусировать на мне (#1)"><svg class="svg-icon sm"><use href="#icon-focus"/></svg> От меня (#1)</button>',
        '<button id="zoomResetBtn" class="chip-btn" title="Сфокусировать на мне (#1)"><svg class="svg-icon sm"><use href="#icon-focus"/></svg> Я (#1)</button>'
    )
    content = content.replace(
        '<button id="zoomFitBtn" class="chip-btn" title="Показать всю карту целиком"><svg class="svg-icon sm"><use href="#icon-tree"/></svg> Весь масштаб</button>',
        '<button id="zoomFitBtn" class="chip-btn" title="Показать всю карту целиком"><svg class="svg-icon sm"><use href="#icon-tree"/></svg> Вся карта</button>'
    )

    # In proband card rendering, ensure cardH is properly measured
    content = content.replace("const cardH = 152;", "const cardH = probandCard.offsetHeight || 152;")

    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(content)
    print("Refined index.astro successfully!")

if __name__ == "__main__":
    refine_styles()
    refine_index_astro()
