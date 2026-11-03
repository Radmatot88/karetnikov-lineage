with open("src/pages/index.astro", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("\r\n", "\n")

# 1. Wizard and Search Close Buttons
text = text.replace(
    '<button type="button" id="scrollClearSearchBtn" class="scroll-act-btn" style="display:none;">✕ Сброс</button>',
    '<button type="button" id="scrollClearSearchBtn" class="scroll-act-btn" style="display:none;"><svg class="svg-icon sm"><use href="#icon-close"/></svg> Сброс</button>'
)
text = text.replace(
    '<button type="button" class="wizard-close" id="closeBranchWizardBtn" title="Закрыть">✕</button>',
    '<button type="button" class="wizard-close" id="closeBranchWizardBtn" title="Закрыть"><svg class="svg-icon sm"><use href="#icon-close"/></svg></button>'
)

# 2. 2D Filter hypotheses button
text = text.replace(
    '🪐 Гипотезы (15)</button>',
    '<svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg> Гипотезы (15)</button>'
)

# 3. Legend Dots on 2D map
text = text.replace(
    '<div><span style="color:var(--status-confirmed); font-weight:700;">● CONFIRMED_DOC</span> — Подтверждено архивной метрикой/ревизией (100% факт)</div>',
    '<div><span style="color:var(--status-confirmed); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-confirmed"/></svg> 100% ФАКТ</span> — Подтверждено архивной метрикой или ревизией</div>'
)
text = text.replace(
    '<div><span style="color:var(--status-oral); font-weight:700;">● FAMILY_ORAL</span> — Прадеды по семейным воспоминаниям (требует шифра)</div>',
    '<div><span style="color:var(--status-oral); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-oral"/></svg> ПРЕДАНИЕ</span> — Семейные воспоминания (требует архивного шифра)</div>'
)
text = text.replace(
    '<div><span style="color:var(--status-candidate); font-weight:700;">● ARCHIVE_CANDIDATE</span> — Архивные зацепки (ЦГАСО / ГАОО / ГАПО)</div>',
    '<div><span style="color:var(--status-candidate); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-candidate"/></svg> КАНДИДАТ</span> — Архивные зацепки (ЦГАСО, ГАОО, ГАПО)</div>'
)
text = text.replace(
    '<div><span style="color:var(--status-unknown); font-weight:700;">● UNKNOWN_SLOT</span> — Вакантные слоты (цель архивного поиска)</div>',
    '<div><span style="color:var(--status-unknown); font-weight:700;"><svg class="svg-icon sm"><use href="#icon-seal-unknown"/></svg> ПОИСК</span> — Вакантные позиции прямого восходящего древа</div>'
)

# 4. Wizard options
text = text.replace('<span>⬆ Отец / Мать</span>', '<span><svg class="svg-icon sm"><use href="#icon-branch"/></svg> Отец / Мать</span>')
text = text.replace('🌿 Присоединить ветку к архиву', '<svg class="svg-icon sm"><use href="#icon-branch"/></svg> Присоединить ветку к архиву')
text = text.replace('<div style="font-size:38px; margin-bottom:8px;">🌿</div>', '<div style="margin-bottom:8px;"><svg class="svg-icon" style="width:38px;height:38px;"><use href="#icon-branch"/></svg></div>')

# 5. Roadmap canvas badges
text = text.replace('`<span class="badge-fact-100">🟢 100% ФАКТ</span>`', '`<span class="badge-fact-100"><svg class="svg-icon sm"><use href="#icon-seal-confirmed"/></svg> 100% ФАКТ</span>`')
text = text.replace('<span class="kinship-arrow">➔</span>', '<span class="kinship-arrow">&rarr;</span>')

# 6. Kinship banner items
text = text.replace('⬇ Потомок:', '&darr; Потомок:')
text = text.replace('⬆ Отец:', '&uarr; Отец:')
text = text.replace('⬆ Мать:', '&uarr; Мать:')

# 7. Collateral relative buttons in dossier
text = text.replace("'↔ Родной брат/сестра'", "'&harr; Брат/Сестра'")
text = text.replace("'⬇ Потомок'", "'&darr; Потомок'")
text = text.replace("`⬆ Отец (#${father.ahnentafel}", "`&uarr; Отец (#${father.ahnentafel}")
text = text.replace("`⬆ Мать (#${mother.ahnentafel}", "`&uarr; Мать (#${mother.ahnentafel}")

# 8. Remaining hypothesis avatar in scroll & drawer
text = text.replace('color:#fbbf24; font-size:22px;">🪐<', 'color:#fbbf24;"><svg class="svg-icon" style="width:24px;height:24px;"><use href="#icon-orbit-hypothesis"/></svg><')
text = text.replace('color:#fbbf24;">🪐</s', 'color:#fbbf24;"><svg class="svg-icon sm"><use href="#icon-orbit-hypothesis"/></svg></s')
text = text.replace('color:#f59e0b; font-size:28px;">🪐<', 'color:#f59e0b;"><svg class="svg-icon" style="width:32px;height:32px;"><use href="#icon-orbit-hypothesis"/></svg><')

# 9. Radar template literals
text = text.replace('<div style="color:var(--text-muted); font-size:11.5px;">📍 ${c.region}</div>', '<div style="color:var(--text-muted); font-size:12px;"><svg class="svg-icon sm"><use href="#icon-pin"/></svg> ${c.region}</div>')
text = text.replace('<div style="color:var(--gold-light); font-size:11.5px; margin-top:3px;">🔗 ${c.key_ancestor', '<div style="color:var(--gold-light); font-size:12px; margin-top:3px;"><svg class="svg-icon sm"><use href="#icon-link"/></svg> ${c.key_ancestor')
text = text.replace('<div style="font-size:12.5px; color:var(--text-muted);">📍 <strong>Историческая привязка:', '<div style="font-size:13px; color:var(--text-muted);"><svg class="svg-icon sm"><use href="#icon-pin"/></svg> <strong>Историческая привязка:')
text = text.replace('<div style="font-size:12.5px; color:var(--text-muted);">🏛️ <strong>Архив:</strong>', '<div style="font-size:13px; color:var(--text-muted);"><svg class="svg-icon sm"><use href="#icon-temple"/></svg> <strong>Архив:</strong>')

# 10. Hypotheses quorum vote text
text = text.replace("${userHasConfirmed ? '✅ Вы подтвердили гипотезу' : '✋ Подтверждаю, семейное предание", "${userHasConfirmed ? '<svg class=\"svg-icon sm\"><use href=\"#icon-check\"/></svg> Гипотеза подтверждена' : '<svg class=\"svg-icon sm\"><use href=\"#icon-hand\"/></svg> Подтверждаю, предание")

with open("src/pages/index.astro", "w", encoding="utf-8") as f:
    f.write(text)

print("Remaining emojis cleaned successfully!")
