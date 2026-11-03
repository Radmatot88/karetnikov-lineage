with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

target = "<script is:inline>"
font_scaler_code = """<script is:inline>
    // --- SENIOR FONT SCALER ENGINE (WCAG AAA 15.2:1 & SENIOR READABILITY 60+) ---
    function initFontScaling() {
      const saved = localStorage.getItem('karetnikov_font_scale') || 'normal';
      applyFontScale(saved);
      document.querySelectorAll('.font-scale-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          applyFontScale(btn.getAttribute('data-scale'));
        });
      });
    }

    function applyFontScale(scale) {
      if (scale === 'lg') {
        document.documentElement.setAttribute('data-font-scale', 'lg');
      } else if (scale === 'xl') {
        document.documentElement.setAttribute('data-font-scale', 'xl');
      } else {
        document.documentElement.removeAttribute('data-font-scale');
      }
      try { localStorage.setItem('karetnikov_font_scale', scale); } catch (e) {}
      document.querySelectorAll('.font-scale-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-scale') === scale);
      });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initFontScaling);
    } else {
      initFontScaling();
    }
"""

if target in text:
    text = text.replace(target, font_scaler_code, 1)
    with open("src/pages/index.astro", "w", encoding="utf-8") as f:
        f.write(text)
    print("Inserted font scaler engine successfully!")
else:
    print("Target <script is:inline> not found")
