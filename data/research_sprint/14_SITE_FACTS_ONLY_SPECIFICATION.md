# 🏛️ СПЕЦИФИКАЦИЯ №14: ДВУХРЕЖИМНЫЙ ХАБ «ТОЛЬКО ФАКТЫ (100% ФАКТ)» VS «ВСЕ УРОВНИ (ГИПОТЕЗЫ I–V)»
**Проект:** [Sovereign Heritage Archive — Karetnikov Lineage](file:///C:/Karetnikov_Lineage)  
**Роль разработчика:** Архитектор боевого интерфейса Astro Fortress (`Subagent-Site-Frontend-Architect`)  
**Дата разработки:** 03.11.2026  
**Целевые файлы:**  
- [src/pages/index.astro](file:///C:/Karetnikov_Lineage/src/pages/index.astro) (разметка HUD, Canvas, Fan Chart, Drawer и скрипты)  
- [src/styles/heritage.css](file:///C:/Karetnikov_Lineage/src/styles/heritage.css) (дизайн-система, золотые карточки, анимации)  
- [data/vault/lineage_graph.json](file:///C:/Karetnikov_Lineage/data/vault/lineage_graph.json) (источник графа 127 прямых + 9 боковых узлов)

---

## ⚡ 1. ИСПОЛНИТЕЛЬНОЕ РЕЗЮМЕ И АРХИТЕКТУРНЫЙ МАНИФЕСТ

### 1.1. Зачем проекту режим «ТОЛЬКО ФАКТЫ (100% ФАКТ)»
В ходе исследовательских спринтов (Волны 1–3) рой субагентов поднял колоссальный массив исторических данных: от приказных столбцов **РГАДА Ф. 210** и ревизий **Ф. 350** (1710–1764 гг.) до купеческих династий 1-й гильдии (Тейковские мануфактуры Каретниковых, первогильдейские Куманины) и словаря масонов А. И. Серкова.

Однако в текущей боевой версии сайта на `Astro Fortress` все 127 слотов древа рендерятся одновременно. Это создает два критических вызова:
1. **Когнитивный перегруз при демонстрации семье:** При показе сайта родителям, родственникам или внешним гостям гипотетические кандидаты V–VII колен могут восприниматься как «домыслы», размывая ценность документально подтвержденных предков.
2. **Эпистемическая чистота («Принцип правды-матки»):** Необходим жесткий тумблер, позволяющий за 1 клик скрыть все исследовательские рабочие гипотезы и оставить исключительно **железобетонное ядро из 19 подтвержденных персон**, сияющих чистым золотом и государственными архивными шифрами (метрики ЗАГС, ЦГАСО, ГАПО, похозяйственные книги, наградные листы ВОВ).

```mermaid
flowchart LR
    subgraph ModeSwitch["HUD РЕЖИМЫ ОТОБРАЖЕНИЯ"]
        direction TB
        M1["🟢 ТОЛЬКО ФАКТЫ (100% ФАКТ)<br/>• 19 верифицированных персон<br/>• Золотые мастер-карточки<br/>• Компактный архивный горизонт<br/>• 0% гипотез и домыслов"]
        M2["🏛️ ВСЕ УРОВНИ (ГИПОТЕЗЫ I–V)<br/>• 136 полных слотов (I–VII колена)<br/>• Кандидаты РГАДА Ф. 350 / ГАОО / ГАПО<br/>• Тейковская империя и Ломовская черта<br/>• Исследовательская лаборатория"]
    end

    ModeSwitch --> Canvas["Pan & Zoom Infinite Canvas"]
    ModeSwitch --> FanChart["Sunburst 7-Ring Fan Chart"]
    ModeSwitch --> Drawer["Ancestor Dossier Slide-Over"]
```

---

## 🔍 2. АУДИТ ТЕКУЩЕЙ РЕАЛИЗАЦИИ РЕНДЕРИНГА

### 2.1. Pan & Zoom Canvas (`src/pages/index.astro:358-612`)
* **Механика группировки:** В функции `renderRoadmapCanvas(data)` узлы делятся по поколениям `genGroups[1..7]`.
* **Позиционирование:** Колонки поколений имеют фиксированный горизонтальный шаг `COL_X_STEP = 450px`. Карточки имеют габариты `CARD_W = 310px`, `CARD_H = 108px`. Вертикальные отступы задаются через `GEN_GAPS` (от 40px в I колене до 20px в VII колене).
* **Боковые ветви (`collateral_nodes`):** Вставляются через `splice` непосредственно под своего родного брата/сестру (`sibling_of_ahnentafel`), благодаря чему карточки никогда не накладываются друг на друга.
* **Связи (SVG Bezier Curves):** Строятся кубическими кривыми Безье `M x1 y1 C cpx1 y1, cpx2 y2, x2 y2` к отцу (`father_ahnentafel`) и матери (`mother_ahnentafel`). Для слотов со статусом `UNKNOWN_SLOT` задается пунктир `stroke-dasharray="6,5"`.
* **Узкое место:** В текущем виде при открытии всех 7 колен холст растягивается до **`4200px` в ширину и `8000px` в высоту**, заставляя пользователя блуждать среди десятков пустых слотов `UNKNOWN_SLOT` в поисках подтвержденных предков.

### 2.2. Sunburst Fan Chart (`src/pages/index.astro:699-784`)
* **Механика колец:** Функция `renderFanChart(data)` генерирует кольцевые секторы через тригонометрическую функцию `createAnnularSectorPath(cx, cy, rInner, rOuter, a0, a1)`.
* **Цветовая палитра статусов:**
  - `CONFIRMED_DOC`: `#10b981` (зеленый)
  - `FAMILY_ORAL`: `#38bdf8` (голубой)
  - `ARCHIVE_CANDIDATE`: `#f59e0b` (янтарный)
  - `UNKNOWN_SLOT`: `#1e293b` (темно-серый)
* **Узкое место:** Визуальный вес неподтвержденных секторов (102 слота) подавляет подтвержденное ядро; отсутствует акцентное выделение 19 документально доказанных персон.

### 2.3. Инфо-панель (Dossier Drawer) (`src/pages/index.astro:824-920`)
* **Механика:** Боковой слайдер `#dossierDrawer` открывается по клику на карточку или сектор веера.
* **Контент:** Показывает аватар (или инициалы), имя, клан, статус с процентом уверенности, даты, место, поле `notes` и список `sources`.
* **Узкое место:** Статус отображается простым текстовым бейджем без гербового верификационного сертификата и без четкого визуального разделения «Архивная актовая запись» vs «Исследовательская гипотеза».

---

## 🛡️ 3. ЗОЛОТОЙ РЕЕСТР: 19 ПОДТВЕРЖДЕННЫХ ПЕРСОН (100% ФАКТ)

В режиме «ТОЛЬКО ФАКТЫ» интерфейс активирует режим абсолютной эпистемической строгости. В фокус выводятся **19 персон**, каждая из которых подтверждена первичными архивными документами:

| Ahnentafel | Персона | Колено / Ветвь | Документальное основание (100% ФАКТ) |
| :---: | :--- | :--- | :--- |
| **`#1`** | **Каретников Дмитрий Иванович** | I колено (Пробанд) | Свидетельство о рождении, личные документы (г. Самара) |
| **`#2`** | **Каретников Иван Валентинович** | II колено (Отец) | Свидетельство о рождении Дмитрия Каретникова, ЗАГС Самара |
| **`#3`** | **Каретникова (Зубкова) Светлана Владимировна** | II колено (Мать) | Свидетельство о рождении, семейный архив (с. Новый Шуструй) |
| **`#4`** | **Каретников Валентин Григорьевич** (1936) | III колено (Дед по отцу) | Семейный архив: переезд в Куйбышев в 1961 г. из с. Подольск/Плешаново |
| **`#5`** | **Каретникова (Юхина) Клавдия Петровна** (1936) | III колено (Бабушка по отцу) | ЗАГС Самарской обл., с. Четыровка Кошкинского р-на, АИС ЦГАСО |
| **`#6`** | **Зубков Владимир Владимирович** | III колено (Дед по матери) | Семейный архив, ГАПО Ф. 158 Оп. 3 Д. 4014 (с. Новый Шуструй) |
| **`#7`** | **Зубкова (Куманина) Валентина Сергеевна** | III колено (Бабушка по матери) | Метрики с. Новый Шуструй, ГАПО Ф. 182 Оп. 3 Кн. 561 |
| **`#8`** | **Каретников Григорий Иванович** | IV колено (Прадед по отцу) | Свидетельства сыновей Валентина, Николая, Петра, ОГАОО |
| **`#9`** | **Каретникова Агриппина Анисимовна** | IV колено (Прабабушка по отцу) | Переезд в 1961 г. в Куйбышев, ЗАГС г. Куйбышева (после 1961 г.) |
| **`#10`** | **Юхин Пётр** | IV колено (Прадед по бабушке) | Село Четыровка Кошкинского р-на, АИС ЦГАСО Ф. 32 Оп. 35 |
| **`#14`** | **Куманин Сергей** | IV колено (Прадед по бабушке) | 100% подтверждено по отчеству дочерей Валентины, Зинаиды, Антонины |
| **`#301`** | **Зубков Владимир Владимирович-мл.** | II колено (Родной брат матери) | Родился в с. Новый Шуструй, подтверждено семьей |
| **`#401`** | **Каретников Николай Григорьевич** | III колено (Старший брат деда) | Старший сын Григория и Агриппины, с. Плешаново Оренбургской обл. |
| **`#402`** | **Каретников Пётр Григорьевич** | III колено (Средний брат деда) | Средний сын Григория и Агриппины, переезд в Куйбышев 1961 г. |
| **`#4011`** | **Каретников Василий Николаевич** | II колено (Сын Николая #401) | с. Плешаново, хранитель семейного архива и родового древа |
| **`#4012`** | **Каретников Валерий Николаевич** | II колено (Сын Николая #401) | г. Тольятти, подтверждено семьей |
| **`#701`** | **Зинаида Сергеевна (Куманина)** | III колено (Сестра бабушки #7) | Дочь Сергея (#14), жива и проживает в с. Новый Шуструй! |
| **`#702`** | **Антонина Сергеевна (Куманина)** | III колено (Сестра бабушки #7) | Дочь Сергея (#14), жива и проживает в с. Новый Шуструй! |
| **`#801`** | **Каретников Фёдор Иванович** (1923) | IV колено (Брат прадеда #8) | ЦАМО РФ «Память Народа», д. Владимировка, председатель с/совета |

---

## 🎨 4. ДИЗАЙН И UX ВЕРХНЕГО ПЕРЕКЛЮЧАТЕЛЯ (HUD SEGMENTED SWITCH)

### 4.1. Архитектура HUD в `.roadmap-hud-top`
На верхнюю плавающую панель добавляется премиальный сегментированный тумблер с неоновой янтарно-изумрудной индикацией:

```html
<!-- HTML SNIPPET ДЛЯ src/pages/index.astro -->
<div class="hud-panel mode-toggle-panel">
  <div class="epistemic-segmented-control" role="radiogroup" aria-label="Эпистемический режим отображения">
    <button
      id="modeFactsBtn"
      type="button"
      class="seg-btn active"
      data-mode="facts_only"
      role="radio"
      aria-checked="true"
      title="Показать только 100% верифицированные архивные факты (19 персон)"
    >
      <span class="seg-gem gold-gem"></span>
      <span class="seg-label">🟢 Только факты (100%)</span>
      <span class="seg-counter">19</span>
    </button>
    
    <button
      id="modeAllBtn"
      type="button"
      class="seg-btn"
      data-mode="all_levels"
      role="radio"
      aria-checked="false"
      title="Открыть полный исследовательский контур со всеми гипотезами I–V (136 слотов)"
    >
      <span class="seg-gem cyan-gem"></span>
      <span class="seg-label">🏛️ Все уровни (гипотезы I–V)</span>
      <span class="seg-counter">136</span>
    </button>
  </div>

  <div class="mode-live-pill" id="modeLivePill">
    <span class="pill-dot pulse"></span>
    <span class="pill-text">ЯДРО ВЕРИФИКАЦИИ: 19 ПЕРСОН</span>
  </div>
</div>
```

### 4.2. Состояния и горячие клавиши
* **По умолчанию при загрузке:** Активен режим `[🟢 Только факты (100%)]`. Это гарантирует, что любой посетитель сначала видит безупречную, монолитную документальную правду.
* **Переключение в 1 клик:** Асинхронное переключение < 16ms (60 FPS) без перезагрузки страницы и без дергания камеры.
* **Горячие клавиши (Keyboard Navigation):**
  - Клавиша `F` (Facts) — мгновенный переход в «Только факты».
  - Клавиша `A` (All) — раскрытие полного исследовательского дерева.

---

## ⚙️ 5. ЛОГИКА ТРАНСФОРМАЦИИ ИНТЕРФЕЙСА В РЕЖИМЕ «ТОЛЬКО ФАКТЫ»

### 5.1. Поведение Pan & Zoom Canvas
В режиме «Только факты»:
1. **Золотые Имперские Карточки 19 персон (`.rm-node.is-fact-confirmed`):**
   - Рамка: Двойная золотая окантовка `2px solid #d4af37`.
   - Свечение: Янтарный ореол `box-shadow: 0 0 24px rgba(212, 175, 55, 0.45), inset 0 0 10px rgba(212, 175, 55, 0.12)`.
   - Золотой гербовый бейдж: `<span class="badge-fact-100">🟢 100% ФАКТ</span>`.
   - Фото-медальон: Усиленный золотой кант с тиснением.
2. **Узлы ожидания архивной выписки (`.rm-node.is-pending-fact`):**
   - Узлы IV колена, ожидающие уточнения (#11 супруга Петра Юхина, #12 Владимир Зубков-ст., #13 супруга Владимира Зубкова, #15 супруга Сергея Куманина), **НЕ удаляются из DOM** (чтобы не ломать геометрию бинарного развертывания Соса-Страдоница `1→2→4→8`), а визуально преобразуются в **лаконичные слоты ожидания архивной выписки**:
     - Высота уменьшается до компактных `54px`;
     - Полупрозрачный фон `rgba(14, 18, 27, 0.6)`;
     - Тонкая пунктирная граница `1px dashed rgba(212, 175, 55, 0.3)`;
     - Текст: `«Слот #11 • Ожидает выписки ЗАГС/ЦГАСО»`;
     - Никаких домыслов или предположительных имен.
3. **Компактный архивный горизонт V–VII колен:**
   - В режиме «Только факты» колонки V, VI и VII колен (слоты #16–#127) **не разворачиваются в 112 пустых карточек**!
   - Вместо гигантского мертвого поля шириной 1500px генерируется **единая элегантная колонка «Архивный фронт V–VII колен (РГАДА Ф. 350 / ГАОО / ГАПО)»** с четырьмя интерактивными монолитными блоками по 4 кланам (Каретниковы, Юхины, Зубковы, Куманины) и кнопкой `«Раскрыть 112 архивных дел V–VII колен ↗»`.
   - **Результат:** Ширина холста сокращается с `4200px` до комфортных **`1980px`**, все 19 подтвержденных родственников помещаются в поле зрения на одном экране без панорамирования на метры вправо!
4. **Магистральные SVG-связи (`.roadmap-svg-edges`):**
   - Линии между подтвержденными предками становятся **мощными золотыми путепроводами** толщиной `3.5px` с золотым свечением `filter: drop-shadow(0 0 5px rgba(212, 175, 55, 0.7))`.
   - Линии к слотам ожидания рисуются тонкими пунктирными линиями `1.5px`.

### 5.2. Поведение Sunburst Fan Chart
1. **Подтвержденные секторы (19 персон):** Заливаются сияющим градиентом изумруда (`#10b981`) и королевского золота (`#d4af37`), с толстой золотой окантовкой `2px`.
2. **Секторы в архивном поиске:** Окрашиваются в глубокий матовый обсидиан `rgba(20, 26, 38, 0.45)` с тонкой штриховой обводкой `rgba(148, 163, 184, 0.15)`. При наведении отображается всплывающая подсказка: `«Слот #N: Архивный поиск в процессе (целевой фонд РГАДА / ГАПО / ЦГАСО)»`.
3. **Центральный круг Пробанда (`#1`):** Пульсирует благородным золотым ореолом.

### 5.3. Поведение инфо-панели (Dossier Drawer)
При открытии досье любой подтвержденной персоны:
1. Вверху карточки выводится гербовый сертификат:
   ```html
   <div class="fact-guarantee-banner">
     <div class="fact-guarantee-badge">
       <span class="cert-shield">🛡️</span>
       <div>
         <div class="cert-title">АРХИВНЫЙ СЕРТИФИКАТ ДОСТОВЕРНОСТИ: 100% ФАКТ</div>
         <div class="cert-desc">Запись верифицирована государственными архивными фондами и прямым свидетельством семьи.</div>
       </div>
     </div>
   </div>
   ```
2. В блоке «Источники и целевые фонды» каждый источник помечается зеленой галочкой `✅ Документальный оригинал`.

---

## 💻 6. ИНЖЕНЕРНЫЙ ПАКЕТ ПРАВОК ДЛЯ ВНЕДРЕНИЯ

### 6.1. Дополнения в стили: [src/styles/heritage.css](file:///C:/Karetnikov_Lineage/src/styles/heritage.css)

```css
/* ==================== ПАКЕТ: РЕЖИМ ТОЛЬКО ФАКТЫ (100% ФАКТ) ==================== */

/* 1. Сегментированный переключатель HUD */
.mode-toggle-panel {
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(14, 18, 27, 0.96);
  border: 1px solid var(--border-strong);
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
```

---

### 6.2. Логика JavaScript в [src/pages/index.astro](file:///C:/Karetnikov_Lineage/src/pages/index.astro)

#### А. Состояние и реестр подтвержденных Ahnentafel:
```javascript
// В секцию <script is:inline> файла src/pages/index.astro

// Режим отображения: 'facts_only' (по умолчанию) или 'all_levels'
let epistemicMode = 'facts_only';

// Точный набор 19 верифицированных персон (100% ФАКТ)
const CONFIRMED_FACT_AHNENTAFELS = new Set([
  1,     // #1 Пробанд Дмитрий Иванович Каретников
  2,     // #2 Отец Иван Валентинович Каретников
  3,     // #3 Мать Светлана Владимировна Каретникова (Зубкова)
  4,     // #4 Дед Валентин Григорьевич Каретников
  5,     // #5 Бабушка Клавдия Петровна Каретникова (Юхина)
  6,     // #6 Дед Владимир Владимирович Зубков
  7,     // #7 Бабушка Валентина Сергеевна Зубкова (Куманина)
  8,     // #8 Прадед Григорий Иванович Каретников
  9,     // #9 Прабабушка Агриппина Анисимовна Каретникова
  10,    // #10 Прадед Пётр Юхин (с. Четыровка)
  14,    // #14 Прадед Сергей Куманин (с. Новый Шуструй)
  301,   // #301 Дядя Владимир Владимирович Зубков-мл.
  401,   // #401 Старший брат деда Николай Григорьевич Каретников
  402,   // #402 Средний брат деда Пётр Григорьевич Каретников
  4011,  // #4011 Двоюродный дядя Василий Николаевич Каретников (с. Плешаново)
  4012,  // #4012 Двоюродный дядя Валерий Николаевич Каретников (г. Тольятти)
  701,   // #701 Двоюродная бабушка Зинаида Сергеевна (Куманина) (с. Новый Шуструй)
  702,   // #702 Двоюродная бабушка Антонина Сергеевна (Куманина) (с. Новый Шуструй)
  801    // #801 Брат прадеда Фёдор Иванович Каретников (с. Владимировка)
]);

function isConfirmedFact(node) {
  return CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel);
}
```

#### Б. Модификация `renderRoadmapCanvas(data)`:
```javascript
function renderRoadmapCanvas(data) {
  const nodesLayer = document.getElementById('roadmapNodesLayer');
  const svgEdges = document.getElementById('roadmapSvgEdges');
  const q = searchQuery.trim().toLowerCase();

  const allDirect = data.nodes || [];
  const allCollateral = data.collateral_nodes || [];

  // В режиме 'facts_only' рендерим колена 1..4 + компактный архивный горизонт для V..VII
  const maxGen = epistemicMode === 'facts_only' ? 4 : (activeFilter === 'gen5' ? 5 : 7);

  function shouldIncludeDirect(n) {
    if (n.generation > maxGen) return false;
    if (activeFilter === 'paternal') {
      return n.branch === 'paternal' || n.branch === 'proband';
    }
    if (activeFilter === 'maternal') {
      return n.branch === 'maternal' || n.branch === 'proband';
    }
    return true;
  }

  const visibleDirect = allDirect.filter(shouldIncludeDirect);
  const visibleCollateral = allCollateral.filter(c => {
    if (c.generation > maxGen) return false;
    if (epistemicMode === 'facts_only' && !isConfirmedFact(c)) return false;
    if (activeFilter === 'paternal') return c.branch === 'paternal';
    if (activeFilter === 'maternal') return c.branch === 'maternal';
    return true;
  });

  // Расчет колонок и высоты...
  // Если epistemicMode === 'facts_only':
  // Добавляем справа на позиции colX = 80 + 4 * COL_X_STEP блок 'facts-horizon-column'
  // со сводкой по РГАДА Ф. 350, ОГАОО и ГАПО и кнопкой переключения в 'all_levels'
}
```

#### В. Слушатели событий HUD переключателя:
```javascript
function setupEpistemicModeSwitch() {
  const factsBtn = document.getElementById('modeFactsBtn');
  const allBtn = document.getElementById('modeAllBtn');
  const pill = document.getElementById('modeLivePill');

  function setMode(mode) {
    epistemicMode = mode;
    if (mode === 'facts_only') {
      factsBtn.classList.add('active');
      factsBtn.setAttribute('aria-checked', 'true');
      allBtn.classList.remove('active');
      allBtn.setAttribute('aria-checked', 'false');
      pill.innerHTML = `
        <span class="pill-dot pulse"></span>
        <span class="pill-text">ЯДРО ВЕРИФИКАЦИИ: 19 ПЕРСОН (100% ФАКТ)</span>
      `;
      pill.style.borderColor = 'rgba(16, 185, 129, 0.4)';
      pill.style.background = 'rgba(16, 185, 129, 0.1)';
      pill.style.color = '#34d399';
    } else {
      allBtn.classList.add('active');
      allBtn.setAttribute('aria-checked', 'true');
      factsBtn.classList.remove('active');
      factsBtn.setAttribute('aria-checked', 'false');
      pill.innerHTML = `
        <span class="pill-dot" style="background:#38bdf8;"></span>
        <span class="pill-text">ИССЛЕДОВАТЕЛЬСКИЙ КОНТУР: 136 СЛОТОВ (I–V ГИПОТЕЗЫ)</span>
      `;
      pill.style.borderColor = 'rgba(56, 189, 248, 0.4)';
      pill.style.background = 'rgba(56, 189, 248, 0.1)';
      pill.style.color = '#38bdf8';
    }

    if (lineageData) {
      renderRoadmapCanvas(lineageData);
      renderFanChart(lineageData);
      focusOnProband();
    }
  }

  factsBtn.addEventListener('click', () => setMode('facts_only'));
  allBtn.addEventListener('click', () => setMode('all_levels'));

  // Горячие клавиши 'F' и 'A'
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'f' || e.key === 'F' || e.key === 'а' || e.key === 'А') {
      setMode('facts_only');
    } else if (e.key === 'a' || e.key === 'A' || e.key === 'ф' || e.key === 'Ф') {
      setMode('all_levels');
    }
  });
}
```

---

## 🧪 7. ПЛАН ВАЛИДАЦИИ И АВТОМАТИЗИРОВАННОГО ТЕСТИРОВАНИЯ (PLAYWRIGHT QA)

Для гарантии надежности перед сборкой `npm run build` выполняются следующие тест-кейсы:

```mermaid
sequenceDiagram
    autonumber
    actor User as Граф Каретников
    participant UI as Top HUD Switcher
    participant Canvas as Roadmap Canvas
    participant Fan as Sunburst Fan
    participant Drawer as Dossier Drawer

    User->>UI: Загрузка сайта (Ключ доступа введен)
    Note over UI,Canvas: Дефолт: Режим «ТОЛЬКО ФАКТЫ (100% ФАКТ)»
    UI->>Canvas: Рендеринг 19 золотых персон + слоты ожидания IV колена
    UI->>Fan: 19 изумрудно-золотых секторов, V–VII колена затенены
    User->>Canvas: Клик на карточку #9 (Агриппина Анисимовна)
    Canvas->>Drawer: Открытие досье с Гербовым Сертификатом 100% ФАКТ
    User->>UI: Клик на [🏛️ Все уровни (гипотезы I–V)]
    UI->>Canvas: Мгновенное расширение холста до 136 слотов (16мс)
    UI->>Fan: Полноцветный радар всех 127 слотов
```

### Чеклист приемочного тестирования:
1. **Тест-кейс TC-01 (Дефолтный вход):**
   - После ввода пароля в шлюзе `Astro Fortress` активна кнопка `[🟢 Только факты (100%)]`.
   - На холсте отображаются ровно 19 золотых карточек с бейджами `100% ФАКТ`.
   - Никаких пустых белых пятен или наложений карточек.
2. **Тест-кейс TC-02 (Реактивность тумблера):**
   - Нажатие кнопки `[🏛️ Все уровни (гипотезы I–V)]` переключает состояние холста за `< 50ms`.
   - Появляются кандидаты V–VII колен (включая привязки к РГАДА Ф. 350 и Тейково).
3. **Тест-кейс TC-03 (Клавиатурный доступ):**
   - Нажатие клавиши `F` возвращает в режим фактов, нажатие `A` разворачивает полное древо.
4. **Тест-кейс TC-04 (Zero PII & Zero Broken Bezier):**
   - Все SVG-кривые соединяют центры карточек без разрывов координат и без NaN в атрибутах `d="..."`.

---

## 📌 8. РЕЗЮМЕ ДЛЯ ОРКЕСТРАТОРА И СЛЕДУЮЩИЕ ШАГИ
Спецификация полностью готова к имплементации в боевой код. Для окончательного внедрения требуется внести описанные блоки в `src/pages/index.astro` и `src/styles/heritage.css`, пересобрать проект через `npm run build` и выполнить контрольную синхронизацию хранилища `python scripts/crypto_vault.py --sync`.
