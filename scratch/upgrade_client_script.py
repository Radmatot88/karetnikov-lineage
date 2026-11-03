import re

with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("\r\n", "\n")

# 1. Update togglePwBtn to toggle SVG eye / eye-off
old_pw_toggle_js = """    document.getElementById('togglePwBtn').addEventListener('click', () => {
      const inp = document.getElementById('passwordInput');
      inp.type = inp.type === 'password' ? 'text' : 'password';
    });"""

new_pw_toggle_js = """    document.getElementById('togglePwBtn').addEventListener('click', () => {
      const inp = document.getElementById('passwordInput');
      const btn = document.getElementById('togglePwBtn');
      if (inp.type === 'password') {
        inp.type = 'text';
        btn.innerHTML = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><use href="#icon-eye-off"/></svg>';
      } else {
        inp.type = 'password';
        btn.innerHTML = '<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><use href="#icon-eye"/></svg>';
      }
    });"""

text = text.replace(old_pw_toggle_js, new_pw_toggle_js)

# 2. Update switchView to fix 2D tree mobile centering
old_switch_view = """    function switchView(targetView) {
      document.querySelectorAll('.nav-tab').forEach(t => {
        t.classList.toggle('active', t.getAttribute('data-view') === targetView);
      });
      document.querySelectorAll('.mob-nav-item[data-mob-view]').forEach(m => {
        m.classList.toggle('active', m.getAttribute('data-mob-view') === targetView);
      });
      document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
      const sec = document.getElementById(`view-${targetView}`);
      if (sec) sec.classList.add('active');
    }"""

new_switch_view = """    function switchView(targetView) {
      document.querySelectorAll('.nav-tab').forEach(t => {
        t.classList.toggle('active', t.getAttribute('data-view') === targetView);
      });
      document.querySelectorAll('.mob-nav-item[data-mob-view]').forEach(m => {
        m.classList.toggle('active', m.getAttribute('data-mob-view') === targetView);
      });
      document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
      const sec = document.getElementById(`view-${targetView}`);
      if (sec) sec.classList.add('active');

      // SENIOR MOBILE FIX: Auto-center 2D Map on Proband (#1) when tab is opened
      if (targetView === 'tree') {
        setTimeout(() => {
          if (typeof focusOnProband === 'function') focusOnProband();
        }, 80);
      }
    }"""

text = text.replace(old_switch_view, new_switch_view)

# 3. Add font scale init & handler at the start of DOMContentLoaded or script
font_scale_engine = """
    // --- SENIOR FONT SCALER (WCAG AAA & 60+ SENIOR READABILITY) ---
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
      localStorage.setItem('karetnikov_font_scale', scale);
      document.querySelectorAll('.font-scale-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-scale') === scale);
      });
    }
"""

if 'initFontScaling();' not in text:
    text = text.replace(
        "document.addEventListener('DOMContentLoaded', async () => {",
        font_scale_engine + "\n    document.addEventListener('DOMContentLoaded', async () => {\n      initFontScaling();"
    )

# 4. Add showFanInspector and upgrade renderFanChart
fan_inspector_fn = """
    function showFanInspector(ahn, node) {
      const insp = document.getElementById('fanMobileInspector');
      if (!insp) return;
      if (!node) {
        insp.style.display = 'block';
        insp.innerHTML = `
          <div class="fan-mobile-card-title"><svg class="svg-icon"><use href="#icon-seal-unknown"/></svg> Вакантный Слот #${ahn}</div>
          <div class="fan-mobile-card-meta">Прямой предок в матрице 7 колен. Данные в процессе архивного поиска.</div>
        `;
        return;
      }

      const statusIcon = node.status === 'CONFIRMED_DOC' ? 'seal-confirmed' :
                         node.status === 'FAMILY_ORAL' ? 'seal-oral' :
                         node.status === 'ARCHIVE_CANDIDATE' ? 'seal-candidate' : 'seal-unknown';
      const statusLabel = node.status === 'CONFIRMED_DOC' ? '100% ФАКТ (Архивный документ)' :
                          node.status === 'FAMILY_ORAL' ? 'Семейное предание' :
                          node.status === 'ARCHIVE_CANDIDATE' ? 'Архивный кандидат' : 'Поиск';
      const clanIcon = node.clan === 'Каретниковы' ? 'clan-karetnikov' :
                       node.clan === 'Юхины' ? 'clan-yukhin' :
                       node.clan === 'Зубковы' ? 'clan-zubkov' : 'clan-kumanin';

      insp.style.display = 'block';
      insp.innerHTML = `
        <div class="fan-mobile-card-title">
          <svg class="svg-icon lg"><use href="#icon-${clanIcon}"/></svg>
          <span>#${node.ahnentafel} ${node.full_name}</span>
        </div>
        <div class="fan-mobile-card-meta">
          <div><strong>Годы жизни:</strong> ${node.birth_date || 'Уточняется'} – ${node.death_date || ''}</div>
          <div><strong>Место:</strong> ${node.birth_place || 'Уточняется'}</div>
          <div style="margin-top:4px;"><svg class="svg-icon sm"><use href="#icon-${statusIcon}"/></svg> <strong>Статус:</strong> ${statusLabel}</div>
        </div>
        <div class="fan-mobile-card-act">
          <button type="button" class="btn-primary" onclick="openDossier(${node.ahnentafel})" style="padding:9px 16px; font-size:13.5px; font-weight:700; border-radius:8px; background:var(--gold-primary); color:#FFF; border:none; cursor:pointer;">
            Открыть досье предка
          </button>
        </div>
      `;
    }
"""

old_fan_event = """      container.querySelectorAll('[data-ahnentafel]').forEach(el => {
        el.addEventListener('click', () => openDossier(parseInt(el.getAttribute('data-ahnentafel'), 10)));
      });"""

new_fan_event = """      container.querySelectorAll('[data-ahnentafel]').forEach(el => {
        el.addEventListener('click', () => {
          const ahn = parseInt(el.getAttribute('data-ahnentafel'), 10);
          showFanInspector(ahn, nodeMap[ahn]);
        });
      });"""

text = text.replace(old_fan_event, fan_inspector_fn + "\n" + new_fan_event)

# 5. Clean emojis in JS rendering routines
# Scroll card badges:
text = text.replace("`🟢 100% ФАКТ`", "`<svg class=\"svg-icon sm\"><use href=\"#icon-seal-confirmed\"/></svg> 100% ФАКТ`")
text = text.replace("`🔵 ПРЕДАНИЕ`", "`<svg class=\"svg-icon sm\"><use href=\"#icon-seal-oral\"/></svg> ПРЕДАНИЕ`")
text = text.replace("`🟠 КАНДИДАТ`", "`<svg class=\"svg-icon sm\"><use href=\"#icon-seal-candidate\"/></svg> КАНДИДАТ`")
text = text.replace("`⚪ ПОИСК`", "`<svg class=\"svg-icon sm\"><use href=\"#icon-seal-unknown\"/></svg> ПОИСК`")

text = text.replace('<span class="rm-photo-badge">📷 Фото</span>', '<span class="rm-photo-badge"><svg class="svg-icon sm"><use href="#icon-photo"/></svg> Фото</span>')
text = text.replace('<span class="scroll-avatar-cam">📷 Фото</span>', '<span class="scroll-avatar-cam"><svg class="svg-icon sm"><use href="#icon-photo"/></svg> Фото</span>')
text = text.replace("📍 ${node.birth_place || ''}", "<svg class=\"svg-icon sm\"><use href=\"#icon-pin\"/></svg> ${node.birth_place || ''}")
text = text.replace("📍 ${hyp.village}", "<svg class=\"svg-icon sm\"><use href=\"#icon-pin\"/></svg> ${hyp.village}")
text = text.replace("<span>📅 ${node.birth_date || 'Дата уточняется'}${deathStr}</span>", "<span><svg class=\"svg-icon sm\"><use href=\"#icon-calendar\"/></svg> ${node.birth_date || 'Дата уточняется'}${deathStr}</span>")
text = text.replace("<span>📍 ${node.birth_place}</span>", "<span><svg class=\"svg-icon sm\"><use href=\"#icon-pin\"/></svg> ${node.birth_place}</span>")
text = text.replace("<span>🪦 ${burialPlace}</span>", "<span><svg class=\"svg-icon sm\"><use href=\"#icon-burial\"/></svg> ${burialPlace}</span>")
text = text.replace("📜 Досье и 12 рубрик", "<svg class=\"svg-icon sm\"><use href=\"#icon-book\"/></svg> Досье")
text = text.replace("🧬 Линия родства", "<svg class=\"svg-icon sm\"><use href=\"#icon-kinship\"/></svg> Линия родства")
text = text.replace("🗺️ На 2D-карте", "<svg class=\"svg-icon sm\"><use href=\"#icon-tree\"/></svg> 2D-Карта")
text = text.replace("🗺️ Показать на 2D-карте", "<svg class=\"svg-icon sm\"><use href=\"#icon-tree\"/></svg> Показать на 2D-карте")
text = text.replace("📱 Показать в Свитке", "<svg class=\"svg-icon sm\"><use href=\"#icon-scroll\"/></svg> Показать в Свитке")
text = text.replace("${userConfirmed ? '✅ Подтв.' : '✋ Подтвердить'}", "${userConfirmed ? '<svg class=\"svg-icon sm\"><use href=\"#icon-check\"/></svg> Подтв.' : '<svg class=\"svg-icon sm\"><use href=\"#icon-hand\"/></svg> Подтвердить'}")
text = text.replace("${userHasConfirmed ? '✅ Вы подтвердили данные' : '✋ Подтверждаю, так и было'}", "${userHasConfirmed ? '<svg class=\"svg-icon sm\"><use href=\"#icon-check\"/></svg> Данные подтверждены' : '<svg class=\"svg-icon sm\"><use href=\"#icon-hand\"/></svg> Подтверждаю'}")
text = text.replace("${userHasConfirmed ? '✅ Вы подтвердили гипотезу' : '✋ Подтверждаю, семейное предание'}", "${userHasConfirmed ? '<svg class=\"svg-icon sm\"><use href=\"#icon-check\"/></svg> Гипотеза подтверждена' : '<svg class=\"svg-icon sm\"><use href=\"#icon-hand\"/></svg> Подтверждаю'}")
text = text.replace("🔗 Связь:", "<svg class=\"svg-icon sm\"><use href=\"#icon-link\"/></svg> Связь:")
text = text.replace("🔗 К предку #", "<svg class=\"svg-icon sm\"><use href=\"#icon-link\"/></svg> К предку #")
text = text.replace("🔗 Перейти к вероятному родственнику", "<svg class=\"svg-icon sm\"><use href=\"#icon-link\"/></svg> Перейти к родственнику")
text = text.replace("<span>✍️ ${m.author}</span>", "<span><svg class=\"svg-icon sm\"><use href=\"#icon-quill\"/></svg> ${m.author}</span>")
text = text.replace("<strong>🛡️ АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ</strong>", "<strong><svg class=\"svg-icon sm\"><use href=\"#icon-seal-confirmed\"/></svg> АРХИВНЫЙ СЕРТИФИКАТ: 100% ФАКТ</strong>")
text = text.replace("<summary>📚 Полный формуляр досье (12 историко-архивных рубрик)</summary>", "<summary><svg class=\"svg-icon sm\"><use href=\"#icon-book\"/></svg> Полный формуляр досье (12 рубрик)</summary>")
text = text.replace("📷 ${photoSrc ? 'Сменить фотографию' : 'Прикрепить фотографию / скан'}", "<svg class=\"svg-icon sm\"><use href=\"#icon-photo\"/></svg> ${photoSrc ? 'Сменить фотографию' : 'Прикрепить фото / скан'}")
text = text.replace("<div class=\"field-val\">📍 ${node.birth_place || 'Уточняется'}</div>", "<div class=\"field-val\"><svg class=\"svg-icon sm\"><use href=\"#icon-pin\"/></svg> ${node.birth_place || 'Уточняется'}</div>")
text = text.replace("<div class=\"field-val\">📍 ${hyp.village}</div>", "<div class=\"field-val\"><svg class=\"svg-icon sm\"><use href=\"#icon-pin\"/></svg> ${hyp.village}</div>")
text = text.replace("🪐 ПАРЯЩИЕ ГИПОТЕЗЫ КОЛЕНА", "<svg class=\"svg-icon sm\"><use href=\"#icon-orbit-hypothesis\"/></svg> ПАРЯЩИЕ ГИПОТЕЗЫ КОЛЕНА")
text = text.replace("? '🌿 Ветвь родственников'", "? 'Ветвь родственников'")
text = text.replace("<span>📅 ${hyp.era || ''}</span>", "<span><svg class=\"svg-icon sm\"><use href=\"#icon-calendar\"/></svg> ${hyp.era || ''}</span>")
text = text.replace("<span>📍 ${hyp.village || ''}</span>", "<span><svg class=\"svg-icon sm\"><use href=\"#icon-pin\"/></svg> ${hyp.village || ''}</span>")
text = text.replace("📜 Архивное досье гипотезы", "<svg class=\"svg-icon sm\"><use href=\"#icon-book\"/></svg> Архивное досье гипотезы")
text = text.replace("<div style=\"font-size:32px; margin-bottom:8px;\">🔍</div>", "<div style=\"margin-bottom:8px;\"><svg class=\"svg-icon\" style=\"width:32px;height:32px;\"><use href=\"#icon-search\"/></svg></div>")
text = text.replace("? '✕ Скрыть панель фильтров'", "? 'Скрыть панель фильтров'")
text = text.replace(": '⚙️ Фильтры и поиск 2D-карты'", ": 'Фильтры и поиск 2D-карты'")
text = text.replace("<div class=\"cipher-box\">📜 Шифр фонда: ${lead.fond_cipher}</div>", "<div class=\"cipher-box\"><svg class=\"svg-icon sm\"><use href=\"#icon-book\"/></svg> Шифр фонда: ${lead.fond_cipher}</div>")
text = text.replace("<strong>🎯 Следующий шаг:</strong>", "<strong><svg class=\"svg-icon sm\"><use href=\"#icon-focus\"/></svg> Следующий шаг:</strong>")
text = text.replace("<div class=\"cipher-box\">🎯 Команда / Действие: ${item.action_for_owner}</div>", "<div class=\"cipher-box\"><svg class=\"svg-icon sm\"><use href=\"#icon-focus\"/></svg> Команда / Действие: ${item.action_for_owner}</div>")
text = text.replace("document.getElementById('drawerAhnentafel').textContent = `🪐 ОРБИТАЛЬНАЯ ГИПОТЕЗА", "document.getElementById('drawerAhnentafel').textContent = `ОРБИТАЛЬНАЯ ГИПОТЕЗА")

# Format drawer Ahnentafel text without raw code
text = text.replace(
    ": `Ahnentafel #${node.ahnentafel} • ${node.generation_label}`;",
    ": `Позиция в родословной: №${node.ahnentafel} • ${node.generation_label}`;",
)

with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.write(text)

print("Client-side script in index.astro upgraded successfully!")
