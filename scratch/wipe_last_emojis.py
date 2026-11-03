with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if "scrollClearSearchBtn" in l:
        lines[i] = '            <button type="button" id="scrollClearSearchBtn" class="scroll-act-btn" style="display:none;"><svg class="svg-icon sm"><use href="#icon-close"/></svg> Сброс</button>\n'
    if "filterHypothesesBtn" in l:
        lines[i] = '          <button class="chip-btn" id="filterHypothesesBtn" data-filter="hypotheses" style="border-color:var(--status-candidate); color:var(--status-candidate);"><svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> Гипотезы (15)</button>\n'
    if "CONFIRMED_DOC</span>" in l:
        lines[i] = '          <div><span style="color:var(--status-confirmed); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-confirmed"/></svg> 100% ФАКТ</span> — Подтверждено архивной метрикой/ревизией</div>\n'
    if "FAMILY_ORAL</span>" in l:
        lines[i] = '          <div><span style="color:var(--status-oral); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-oral"/></svg> ПРЕДАНИЕ</span> — Семейные воспоминания</div>\n'
    if "ARCHIVE_CANDIDATE</span>" in l:
        lines[i] = '          <div><span style="color:var(--status-candidate); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-candidate"/></svg> КАНДИДАТ</span> — Архивные зацепки (ЦГАСО, ГАОО, ГАПО)</div>\n'
    if "UNKNOWN_SLOT</span>" in l:
        lines[i] = '          <div><span style="color:var(--status-unknown); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-unknown"/></svg> ПОИСК</span> — Вакантные слоты древа</div>\n'
    if "Присоединить ветку к архиву" in l:
        lines[i] = '          <button type="submit" class="gate-btn" style="width:auto; padding:10px 24px;"><svg class="svg-icon sm"><use href="#icon-branch"/></svg> Присоединить ветку к архиву</button>\n'
    if "🔵 ПРЕДАНИЕ" in l:
        lines[i] = lines[i].replace("🔵 ПРЕДАНИЕ", '<svg class="svg-icon sm"><use href="#icon-seal-oral"/></svg> ПРЕДАНИЕ')
    if "🟠 КАНДИДАТ" in l:
        lines[i] = lines[i].replace("🟠 КАНДИДАТ", '<svg class="svg-icon sm"><use href="#icon-seal-candidate"/></svg> КАНДИДАТ')
    if "⚪ ПОИСК" in l:
        lines[i] = lines[i].replace("⚪ ПОИСК", '<svg class="svg-icon sm"><use href="#icon-seal-unknown"/></svg> ПОИСК')
    if "⬆ Отец" in l:
        lines[i] = lines[i].replace("⬆ Отец", "&uarr; Отец")
    if "⬆ Мать" in l:
        lines[i] = lines[i].replace("⬆ Мать", "&uarr; Мать")

with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Wiped last 12 lines successfully!")
