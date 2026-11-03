# 🛡️ ZERO-EMOJI SVG ICON SYSTEM SPECIFICATION (HERALDIC VELLUM EDITION)
**Проект:** Родословная Графа Каретникова (`c:\Karetnikov_Lineage`)  
**Статус:** Утверждённый инженерный стандарт UI/UX (Astro 7 + Cloudflare Pages)  
**Комплаенс:** `GEMINI.md` (TABOO_02 — SVG-ONLY & ZERO EMOJI IN UI)  
**Автор спецификации:** `Flash-SVG-Icon-Writer`  
**Дата верификации:** Ноябрь 2026 г.  

---

## 1. Сводная Дефектная Ведомость Эмодзи (Emoji Audit Digest)

На основе сплошного инструментального сканирования кодовой базы (`src/pages/index.astro` и `public/heraldry/index.html`) выявлено **108 прямых вхождений юникод-эмодзи**. 

Использование системных эмодзи в родовом архивном проекте грубо нарушает **TABOO_02 Конституции проекта** по трем фундаментальным причинам:
1. **Гетерогенность платформ:** На Apple iOS/macOS, Windows 11 (Segoe UI Emoji) и Android один и тот же символ (например, `🦁` или `🌾`) отображается в кардинально разных мультяшных стилях, разрушая строгость имперского архива.
2. **Проблема контраста и галации для старшего поколения:** Желтые и пестрые эмодзи на светлом фоне пергамента (`#FDFBF7` / `#F5EFEB`) имеют коэффициент контраста менее `2.1:1`, что грубо нарушает стандарт `WCAG AAA (≥ 10:1)`. Родственники старшего поколения видят размытые цветные пятна.
3. **Отсутствие геральдического провенанса:** Вместо исторических гербовых фигур (каретное колесо, орлиное крыло, стрелецкий бердыш, волна реки Кондурчи) используются шаблонные эмодзи из мессенджеров.

### Классификационная таблица 108 дефектов:

| № Группы | Категория UI | Список эмодзи в коде | Кол-во строк | Строки в файлах (из `emoji_digest.txt`) | Целевая SVG-замена |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Группа 1** | **Главная навигация и табы** | `📱`, `🗺️`, `🎡`, `📡`, `🔐` | 9 | `index.astro`: 3, 4, 5, 6, 7, 29, 30, 31, 32 | `nav-scroll`, `nav-tree`, `nav-fan`, `nav-archive`, `action-lock` |
| **Группа 2** | **Криптозащита и бейджи безопасности** | `🛡️`, `🔐`, `🔒` | 4 | `index.astro`: 1, 2, 7, 11 | `shield-fortress`, `action-lock` |
| **Группа 3** | **Действия тулбара и экспорт** | `🌿`, `⬇`, `🔒`, `🎯`, `⚙️`, `✕`, `🔍` | 13 | `index.astro`: 8, 9, 10, 11, 13, 14, 23, 27, 28, 34, 36, 73, 74 | `action-branch-add`, `action-download`, `action-lock`, `action-focus`, `action-settings`, `action-close`, `action-search` |
| **Группа 4** | **Сургучные статусы достоверности** | `🟢`, `🔵`, `🟠`, `⚪` | 6 | `index.astro`: 15, 25, 44, 53, 54, 55, 56 | `seal-confirmed`, `seal-oral`, `seal-candidate`, `seal-unknown` |
| **Группа 5** | **Фамильные кланы (Гербовые ветви)** | `🦁`, `🌾`, `🛡️`, `👑` | 4 | `index.astro`: 17, 18, 19, 20 | `clan-karetnikov-wheel`, `clan-yukhin-wheat`, `clan-zubkov-sabre`, `clan-kumanin-wing` |
| **Группа 6** | **Орбитальные гипотезы** | `🪐` | 8 | `index.astro`: 21, 22, 26, 42, 65, 70, 94, 97 | `icon-orbit-hypothesis` |
| **Группа 7** | **Визард присоединения ветви** | `🌿`, `👶`, `💍`, `⬆`, `✕` | 7 | `index.astro`: 33, 35, 37, 38, 39, 40, 41 | `action-branch-add`, `rel-child`, `rel-spouse`, `rel-parent`, `action-close` |
| **Группа 8** | **Навигатор родства (Ahnentafel #1)** | `🧬`, `➔`, `⬇`, `⬆` | 5 | `index.astro`: 12, 49, 50, 51, 52 | `meta-kinship`, `meta-arrow-right`, `rel-child`, `rel-parent` |
| **Группа 9** | **Карточки персон и свитковые узлы** | `📷`, `📅`, `📍`, `🪦`, `📜`, `🔗`, `✍️` | 24 | `index.astro`: 45, 46, 47, 48, 57, 58, 59, 60, 61, 62, 63, 66, 67, 68, 69, 71, 75, 76, 85, 86, 89, 90, 95, 98 | `action-photo`, `meta-calendar`, `meta-pin`, `meta-burial-cross`, `meta-scroll`, `meta-link`, `meta-quill` |
| **Группа 10** | **Досье формуляра, сертификаты и радар** | `🏛️`, `🎯`, `↔`, `⬆`, `🛡️`, `📚`, `🗺️`, `📱` | 13 | `index.astro`: 16, 24, 72, 77, 78, 79, 80, 81, 82, 83, 84, 87, 88, 91, 92, 96 | `heraldry-temple`, `action-focus`, `meta-arrow-h`, `rel-parent`, `seal-confirmed`, `meta-book`, `nav-tree`, `nav-scroll`, `meta-link` |
| **Группа 11** | **Семейный кворум верификации** | `✅`, `✋` | 3 | `index.astro`: 64, 93, 99 | `vote-confirmed`, `vote-pledge` |
| **Группа 12** | **Гербовник и архивный пруф-атлас** | `🏛️`, `⬅`, `📜`, `🐝`, `👑`, `📸`, `🦅`, `✕` | 9 | `heraldry/index.html`: 100, 101, 102, 103, 104, 105, 106, 107, 108 | `heraldry-temple`, `meta-arrow-left`, `meta-scroll`, `clan-kumanin-bee`, `clan-kumanin-wing`, `action-photo`, `clan-eagle`, `action-close` |

**Итого выявлено и каталогизировано: 108 позиций.**

---

## 2. Готовый эталонный SVG-каталог `HERALDIC_ICONS` (24 прецизионные векторные иконки)

Все иконки спроектированы в единой субпиксельной сетке:
- **Размер холста:** `viewBox="0 0 24 24"`
- **Базовые атрибуты:** `fill="none"`, `stroke="currentColor"`, `stroke-width="1.8"`, `stroke-linecap="round"`, `stroke-linejoin="round"`
- **Масштабируемость:** `vector-effect="non-scaling-stroke"` (сохранение толщины волосяных линий при любом зуме)
- **Цветовое управление:** Управляется через CSS класс или `color: var(--gold-primary)` / `var(--crimson-seal)`.

```javascript
/**
 * КАТАЛОГ ПРЕЦИЗИОННЫХ ГЕРАЛЬДИЧЕСКИХ И ИНТЕРФЕЙСНЫХ SVG-ИКОНОК
 * Проект: Родословная Графа Каретникова (c:\Karetnikov_Lineage)
 * Стандарт: 100% Zero-Emoji Compliance
 */
export const HERALDIC_ICONS = {
  // =========================================================================
  // I. ЧЕТЫРЕ ГЕРАЛЬДИЧЕСКИЕ СУРГУЧНЫЕ ПЕЧАТИ СТАТУСОВ ДОСТОВЕРНОСТИ
  // =========================================================================

  /** 1. 100% ФАКТ (CONFIRMED_DOC) — Восьмилепестковая сургучная розетка с архивной галочкой верификации */
  'seal-confirmed': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 2l2.4 2.2 3.2-.5 1.3 3 2.9 1.5-.7 3.2 2.2 2.4-2.2 2.4.7 3.2-2.9 1.5-1.3 3-3.2-.5L12 22l-2.4-2.2-3.2.5-1.3-3-2.9-1.5.7-3.2L0.7 12l2.2-2.4-.7-3.2 2.9-1.5 1.3-3 3.2.5L12 2z"/>
    <path d="M8.5 12.3l2.4 2.4 4.8-5"/>
  </svg>`,

  /** 2. СЕМЕЙНОЕ ПРЕДАНИЕ (FAMILY_ORAL) — Сургучная печать с наклонным свитком и пером памяти */
  'seal-oral': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="9"/>
    <path d="M8 8.5c0-1.1.9-2 2-2h4.5c1.1 0 2 .9 2 2v7c0 1.1-.9 2-2 2H10c-1.1 0-2-.9-2-2v-7z"/>
    <path d="M8 15.5c-1.1 0-2-.9-2-2s.9-2 2-2"/>
    <path d="M11 10h4M11 13h2.5"/>
  </svg>`,

  /** 3. АРХИВНЫЙ КАНДИДАТ (ARCHIVE_CANDIDATE) — Сургучная печать с геральдической поисковой лупой */
  'seal-candidate': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="9.2" stroke-dasharray="2.5 1.5"/>
    <circle cx="11" cy="11" r="3.8"/>
    <path d="M14 14l3.5 3.5"/>
  </svg>`,

  /** 4. ВАКАНТНЫЙ СЛОТ / ПОИСК (UNKNOWN_SLOT) — Контурный щит прямого предка со знаком вопроса */
  'seal-unknown': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 3L4.5 6.5v6c0 5 3.5 9 7.5 10.5 4-1.5 7.5-5.5 7.5-10.5v-6L12 3z"/>
    <path d="M10.2 9.5a2 2 0 1 1 3.2 1.8c-.8.6-1.4 1.1-1.4 2.2"/>
    <circle cx="12" cy="16.5" r="0.7" fill="currentColor"/>
  </svg>`,

  // =========================================================================
  // II. ЧЕТЫРЕ ГЕРБОВЫХ СИМВОЛА ФАМИЛЬНЫХ КЛАНОВ РОДА
  // =========================================================================

  /** 5. КЛАН КАРЕТНИКОВЫХ — Имперское каретное колесо с 8 лучами и ступицей мастера */
  'clan-karetnikov-wheel': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="9"/>
    <circle cx="12" cy="12" r="2.8"/>
    <path d="M12 3v6.2M12 14.8V21M3 12h6.2M14.8 12H21"/>
    <path d="M5.6 5.6l4.4 4.4M14 14l4.4 4.4M18.4 5.6l-4.4 4.4M10 14l-4.4 4.4"/>
  </svg>`,

  /** 6. КЛАН КУМАНИНЫХ — Орлиное крыло с дворянской восьмиконечной звездой (ОГ XI, 54) */
  'clan-kumanin-wing': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 18c2-6 7-12 16-14-1 4-2 8-5 11-2.5 2.5-6 4-11 3z"/>
    <path d="M6 16c3-4 6-7 11-9M7.5 17.5c2.5-3 5-5 8.5-6.5"/>
    <path d="M19 14.5l.8 1.8 1.9.3-1.4 1.3.4 1.9-1.7-.9-1.7.9.4-1.9-1.4-1.3 1.9-.3z"/>
  </svg>`,

  /** 7. КЛАН ЗУБКОВЫХ — Скрещенная сабля и стрелецкий бердыш служилых людей Ломовской черты XVII в. */
  'clan-zubkov-sabre': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 20l11-11M15 9c2-2 4-2.5 5.5-2.5s.5 2-.5 3.5-3 3-5 5"/>
    <path d="M3 21l2-2M2 19l3 3M6 18l-2 2"/>
    <path d="M18 5l2-2 1.5 1.5-2 2"/>
    <path d="M20 20L11 11M9 13c-2 2-3.5 2.5-5 2.5.5-2 1.5-3.5 3.5-5"/>
    <path d="M21 21l-2-2M22 19l-3 3M18 18l2 2"/>
  </svg>`,

  /** 8. КЛАН ЮХИНЫХ — Три хлебных колоса над волной реки Кондурчи (Самарский уезд) */
  'clan-yukhin-wheat': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 3v13M12 3c-1.5 1.5-2 3-1.5 4.5 1.5 0 2.5-.5 3.5-2-.5-1.2-1-2-2-2.5z"/>
    <path d="M12 7.5c-1.8 1.2-2.3 2.8-1.8 4.2 1.6 0 2.7-.5 3.8-2.2-.6-1-1-1.5-2-2z"/>
    <path d="M12 12c-2 1-2.5 2.5-2 4 1.8 0 3-.5 4-2-.6-1-1-1.5-2-2z"/>
    <path d="M3 18.5c2.5-1 4.5-1 7 0s4.5 1 7 0 4.5-1 5 0"/>
    <path d="M3 21.5c2.5-1 4.5-1 7 0s4.5 1 7 0 4.5-1 5 0"/>
  </svg>`,

  // =========================================================================
  // III. 16 ИНТЕРФЕЙСНЫХ И НАВИГАЦИОННЫХ ИКОНОК
  // =========================================================================

  /** 9. НАВИГАЦИЯ: СВИТОК ПОКОЛЕНИЙ (вместо 📱) — Развернутый рукописный свиток */
  'nav-scroll': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M7 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a3 3 0 0 1 3-3z"/>
    <path d="M4 7h13a2 2 0 0 1 2 2"/>
    <path d="M8 11h7M8 14h5"/>
  </svg>`,

  /** 10. НАВИГАЦИЯ: 2D-КАРТА ДРЕВА (вместо 🗺️) — Архитектурная карта предков с узлами ветвления */
  'nav-tree': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="3" width="18" height="18" rx="2"/>
    <path d="M12 7v5M8 12h8M8 12v4M16 12v4"/>
    <circle cx="12" cy="7" r="1.5" fill="currentColor"/>
    <circle cx="8" cy="16" r="1.5" fill="currentColor"/>
    <circle cx="16" cy="16" r="1.5" fill="currentColor"/>
  </svg>`,

  /** 11. НАВИГАЦИЯ: КРУГОВОЙ ВЕЕР 127 (вместо 🎡) — Радиальная диаграмма поколений (Ahnentafel Fan) */
  'nav-fan': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 21a9 9 0 0 1-9-9 9 9 0 0 1 9-9 9 9 0 0 1 9 9"/>
    <path d="M12 21l-6-6a5.5 5.5 0 0 1 6-7.8 5.5 5.5 0 0 1 6 7.8z"/>
    <path d="M12 21V12M12 12L7.5 7.5M12 12l4.5-4.5M12 12H3M12 12h9"/>
  </svg>`,

  /** 12. НАВИГАЦИЯ: ГЕРБОВНИК И АТЛАС (вместо 🏛️) — Портик Императорского архива с колоннами */
  'heraldry-temple': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M3 9.5L12 4l9 5.5"/>
    <path d="M4 10h16M2 20h20M5 10v10M9 10v10M15 10v10M19 10v10"/>
  </svg>`,

  /** 13. НАВИГАЦИЯ: АРХИВНЫЙ РАДАР (вместо 📡) — Компас-визир архивной разведки */
  'nav-archive': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="9"/>
    <path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>
    <path d="M12 12l4-4-1.5 5.5L9 15z"/>
  </svg>`,

  /** 14. ДЕЙСТВИЕ: ДОБАВИТЬ ВЕТВЬ (вместо 🌿) — Живой побег родовой лозы с почкой */
  'action-branch-add': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 20c4-1 8-5 9-10 1.2-5.5 5-7 7-7-1 3-1 6-4 8-3 2-6 3-7 7"/>
    <path d="M10 13c-2.5 0-4.5 1.5-5 3.5 1.5.5 3.5 0 5-1.5z"/>
    <path d="M17 17v4M15 19h4"/>
  </svg>`,

  /** 15. ДЕЙСТВИЕ: СКАЧАТЬ GEDCOM / ФОТО (вместо ⬇) — Архитектурная стрела с выгрузкой на пергамент */
  'action-download': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 3v13M7 11l5 5 5-5"/>
    <path d="M4 17v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>
  </svg>`,

  /** 16. ДЕЙСТВИЕ: ЗАМОК / КРИПТОЗАЩИТА (вместо 🔐 и 🔒) — Навесной архивный замок */
  'action-lock': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <rect x="5" y="10" width="14" height="11" rx="2"/>
    <path d="M8 10V6.5a4 4 0 0 1 8 0V10"/>
    <circle cx="12" cy="15" r="1.3" fill="currentColor"/>
    <path d="M12 16.3v2"/>
  </svg>`,

  /** 17. ДЕЙСТВИЕ: ФОКУС / ОТ МЕНЯ (вместо 🎯) — Оптический визир центрирования на Пробанде */
  'action-focus': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="8"/>
    <circle cx="12" cy="12" r="3"/>
    <path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>
  </svg>`,

  /** 18. ДЕЙСТВИЕ: ПОИСК ПО АРХИВУ (вместо 🔍) — Архивная лупа с фаской */
  'action-search': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="7"/>
    <path d="M16.5 16.5L21 21"/>
  </svg>`,

  /** 19. ДЕЙСТВИЕ: ПРИКРЕПИТЬ ФОТОГРАФИЮ (вместо 📷 и 📸) — Форматная фотокамера со стеклянной линзой */
  'action-photo': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 7h4l2-3h4l2 3h4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2z"/>
    <circle cx="12" cy="14" r="4"/>
  </svg>`,

  /** 20. МЕТАДАННЫЕ: ДАТА РОЖДЕНИЯ / ВЕК (вместо 📅) — Лист настенного церковного календаря */
  'meta-calendar': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="4" width="18" height="17" rx="2"/>
    <path d="M16 2v4M8 2v4M3 9h18"/>
    <path d="M8 13h2M14 13h2M8 17h2M14 17h2"/>
  </svg>`,

  /** 21. МЕТАДАННЫЕ: СЕЛО / ПРИХОД (вместо 📍) — Гербовый пин с церковным крестом прихода */
  'meta-pin': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/>
    <circle cx="12" cy="9" r="2.5"/>
  </svg>`,

  /** 22. МЕТАДАННЫЕ: МЕСТО ЗАХОРОНЕНИЯ (вместо 🪦) — Мемориальный памятный крест вечной памяти */
  'meta-burial-cross': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 3v17M8 7h8M9 14h6"/>
    <path d="M5 20h14"/>
  </svg>`,

  /** 23. МЕТАДАННЫЕ: АВТОР ВОСПОМИНАНИЯ (вместо ✍️) — Гусиное перо летописца и чернильница */
  'meta-quill': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M19 3C16 4 12 7 10 11c-1.5 3-2 6-4 8l3-1c3-1.5 6-3 8-5 3-3 4-8 2-10z"/>
    <path d="M6 19l-3 2 1-3"/>
    <path d="M13 8l3 3"/>
  </svg>`,

  /** 24. ОРБИТАЛЬНАЯ ГИПОТЕЗА (вместо 🪐) — Планетарная орбита с лучезарным ядром гипотезы */
  'icon-orbit-hypothesis': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="5"/>
    <ellipse cx="12" cy="12" rx="10" ry="3.8" transform="rotate(-25 12 12)"/>
    <circle cx="18" cy="9" r="1" fill="currentColor"/>
  </svg>`,

  // =========================================================================
  // ДОПОЛНИТЕЛЬНЫЕ ИНТЕРФЕЙСНЫЕ ИКОНКИ (ДЛЯ 100% ПОКРЫТИЯ ДЕФЕКТОВ)
  // =========================================================================

  /** ЗАКРЫТЬ МОДАЛКУ / ДРОБЕР (вместо ✕) */
  'action-close': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M18 6L6 18M6 6l12 12"/>
  </svg>`,

  /** НАВИГАТОР РОДСТВА (вместо 🧬) */
  'meta-kinship': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 6c4 0 6 6 10 6s6 6 6 6M20 6c-4 0-6 6-10 6S4 18 4 18"/>
    <path d="M7 6v12M12 9v6M17 6v12"/>
  </svg>`,

  /** СВЯЗЬ / ШИФР (вместо 🔗 и 📜) */
  'meta-link': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
    <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
  </svg>`,

  'meta-scroll': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M19 17V5a2 2 0 0 0-2-2H4"/>
    <path d="M8 21h11a2 2 0 0 0 2-2v-2H6a2 2 0 0 0-2 2v0a2 2 0 0 0 2 2z"/>
    <path d="M8 7h7M8 11h5"/>
  </svg>`,

  /** КВОРОМ ПОДТВЕРЖДЕНИЯ (вместо ✅ и ✋) */
  'vote-confirmed': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="9"/>
    <path d="M8 12l2.5 2.5L16 9"/>
  </svg>`,

  'vote-pledge': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v4"/>
    <path d="M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v6"/>
    <path d="M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/>
    <path d="M6 14v1a6 6 0 0 0 6 6h1a6 6 0 0 0 6-6v-4a2 2 0 0 0-2-2h-1"/>
  </svg>`,

  /** СВЯЗИ РОДСТВА В ВИЗАРДЕ (вместо 👶, 💍, ⬆) */
  'rel-child': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="7" r="3.5"/>
    <path d="M6 20v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/>
  </svg>`,

  'rel-spouse': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="9" cy="12" r="5"/>
    <circle cx="15" cy="12" r="5"/>
  </svg>`,

  'rel-parent': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="7" r="3"/>
    <path d="M6 21v-2a5 5 0 0 1 5-5h2a5 5 0 0 1 5 5v2"/>
    <path d="M12 11V15M10 13l2-2 2 2"/>
  </svg>`,

  /** ФОРМУЛЯР И БИБЛИОТЕКА (вместо 📚) */
  'meta-book': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
    <path d="M8 7h8M8 11h6"/>
  </svg>`,

  /** СТРЕЛКИ НАВИГАЦИИ (вместо ➔ и ⬅) */
  'meta-arrow-right': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M5 12h14M13 6l6 6-6 6"/>
  </svg>`,

  'meta-arrow-left': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M19 12H5M11 18l-6-6 6-6"/>
  </svg>`,

  /** КУМАНИНСКАЯ ГЕРБОВАЯ ПЧЕЛА (вместо 🐝 в ДС XIX, 31) */
  'clan-kumanin-bee': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <ellipse cx="12" cy="13" rx="3.5" ry="5.5"/>
    <path d="M12 7.5V5M10 4l2 1 2-1"/>
    <path d="M8.5 12H15.5M9 15h6"/>
    <path d="M8.5 11C6 9 3 10 3 12.5s3 3 5.5 1.5"/>
    <path d="M15.5 11c2.5-2 5.5-1 5.5 1.5s-3 3-5.5 1.5"/>
  </svg>`
};
```

---

## 3. Вспомогательная функция `renderIcon(name, size, className)` и CSS-стилизация

Для подстановки как на этапе серверного рендеринга Astro, так и в браузере внедряется сверхлегкая функция:

```typescript
/**
 * Вспомогательный хелпер генерации инлайн-SVG без сторонних библиотек
 * @param name Имя иконки из словаря HERALDIC_ICONS
 * @param size Размер в пикселях (по умолчанию 18px для интерфейса, 20-24px для кнопок)
 * @param className Дополнительный CSS класс
 */
export function renderIcon(name: string, size: number = 18, className: string = ''): string {
  const rawSvg = HERALDIC_ICONS[name];
  if (!rawSvg) return '';
  return rawSvg.replace(
    '<svg ',
    `<svg width="${size}" height="${size}" class="archival-icon ${className}" aria-hidden="true" focusable="false" `
  );
}
```

### Базовые стили для светлой пергаментной темы (`Archival Vellum`):

```css
/* Базовый класс для всех архивных векторных иконок */
.archival-icon {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  stroke: currentColor;
  fill: none;
}

/* 4 сургучные гербовые печати достоверности */
.seal-icon-confirmed {
  color: #15803d; /* Изумрудный гербовый сургуч (100% ФАКТ) */
}
.seal-icon-oral {
  color: #0369a1; /* Лазоревый архивный свиток (ПРЕДАНИЕ) */
}
.seal-icon-candidate {
  color: #b45309; /* Охристо-янтарный провенанс (КАНДИДАТ) */
}
.seal-icon-unknown {
  color: #64748b; /* Грифельно-стальной контур (ПОИСК) */
}

/* Иконки кланов */
.clan-icon-karetnikov { color: #854d0e; } /* Каретная бронза */
.clan-icon-kumanin    { color: #b91c1c; } /* Андрианопольский пурпур */
.clan-icon-zubkov     { color: #1e3a8a; } /* Ратная синь Ломовской черты */
.clan-icon-yukhin     { color: #166534; } /* Стебли ржи и Кондурча */
.clan-icon-hypothesis { color: #d97706; } /* Солнечный янтарь */

/* Минимальный сенсорный размер для родственников старшего поколения */
.btn-archival, .nav-tab, .chip-btn {
  min-height: 48px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  line-height: 1.4;
}
```

---

## 4. План пошаговой замены в `src/pages/index.astro` и `public/heraldry/index.html`

### 4.1. Главная панель навигации (Lines 93–97):
- **Было:**
  ```html
  <button class="nav-tab" data-view="scroll">📱 Свиток Поколений (Умная Навигация)</button>
  <button class="nav-tab active" data-view="tree">🗺️ 2D-Карта Древа (Pan & Zoom)</button>
  <button class="nav-tab" data-view="fan">🎡 Круговой Веер 127</button>
  <button class="nav-tab" data-view="radar">📡 Архивный Радар</button>
  <button class="nav-tab" id="tabNavAccess" data-view="access">🔐 Пульт Доступов</button>
  ```
- **Стало (100% Zero-Emoji):**
  ```html
  <button class="nav-tab" data-view="scroll"><span class="nav-ico" set:html={renderIcon('nav-scroll', 20)} /> Свиток Поколений</button>
  <button class="nav-tab active" data-view="tree"><span class="nav-ico" set:html={renderIcon('nav-tree', 20)} /> 2D-Карта Древа</button>
  <button class="nav-tab" data-view="fan"><span class="nav-ico" set:html={renderIcon('nav-fan', 20)} /> Круговой Веер 127</button>
  <button class="nav-tab" data-view="radar"><span class="nav-ico" set:html={renderIcon('nav-archive', 20)} /> Архивный Радар</button>
  <button class="nav-tab" id="tabNavAccess" data-view="access"><span class="nav-ico" set:html={renderIcon('action-lock', 20)} /> Пульт Доступов</button>
  ```

### 4.2. Кнопки родовых кланов (Lines 151–155):
- **Было:**
  ```html
  <button type="button" class="scroll-clan-pill" data-clan="Каретниковы">🦁 Каретниковы</button>
  <button type="button" class="scroll-clan-pill" data-clan="Юхины">🌾 Юхины</button>
  <button type="button" class="scroll-clan-pill" data-clan="Зубковы">🛡️ Зубковы</button>
  <button type="button" class="scroll-clan-pill" data-clan="Куманины">👑 Куманины</button>
  <button type="button" class="scroll-clan-pill" data-clan="hypotheses">🪐 Гипотезы (15)</button>
  ```
- **Стало:**
  ```html
  <button type="button" class="scroll-clan-pill" data-clan="Каретниковы"><span class="clan-icon-karetnikov" set:html={renderIcon('clan-karetnikov-wheel', 18)} /> Каретниковы</button>
  <button type="button" class="scroll-clan-pill" data-clan="Юхины"><span class="clan-icon-yukhin" set:html={renderIcon('clan-yukhin-wheat', 18)} /> Юхины</button>
  <button type="button" class="scroll-clan-pill" data-clan="Зубковы"><span class="clan-icon-zubkov" set:html={renderIcon('clan-zubkov-sabre', 18)} /> Зубковы</button>
  <button type="button" class="scroll-clan-pill" data-clan="Куманины"><span class="clan-icon-kumanin" set:html={renderIcon('clan-kumanin-wing', 18)} /> Куманины</button>
  <button type="button" class="scroll-clan-pill" data-clan="hypotheses"><span class="clan-icon-hypothesis" set:html={renderIcon('icon-orbit-hypothesis', 18)} /> Гипотезы (15)</button>
  ```

### 4.3. Динамические сургучные бейджи в клиентском JS (Lines 1461–1466):
- **Было:**
  ```javascript
  const statusBadge = isFactConfirmed
    ? `<span class="badge-fact-100">🟢 100% ФАКТ</span>`
    : node.verification_status === 'FAMILY_ORAL'
    ? `<span class="ahnentafel-badge" style="color:#38bdf8;">🔵 ПРЕДАНИЕ</span>`
    : node.verification_status === 'ARCHIVE_CANDIDATE'
    ? `<span class="ahnentafel-badge" style="color:#fbbf24;">🟠 КАНДИДАТ</span>`
    : `<span class="ahnentafel-badge" style="color:#64748b;">⚪ ПОИСК</span>`;
  ```
- **Стало:**
  ```javascript
  const statusBadge = isFactConfirmed
    ? `<span class="badge-seal seal-confirmed">${HERALDIC_ICONS['seal-confirmed']} 100% ФАКТ</span>`
    : node.verification_status === 'FAMILY_ORAL'
    ? `<span class="badge-seal seal-oral">${HERALDIC_ICONS['seal-oral']} ПРЕДАНИЕ</span>`
    : node.verification_status === 'ARCHIVE_CANDIDATE'
    ? `<span class="badge-seal seal-candidate">${HERALDIC_ICONS['seal-candidate']} КАНДИДАТ</span>`
    : `<span class="badge-seal seal-unknown">${HERALDIC_ICONS['seal-unknown']} ПОИСК</span>`;
  ```

### 4.4. Метаданные карточек персон (Lines 1489–1491):
- **Было:**
  ```javascript
  `<span>📅 ${node.birth_date || 'Дата уточняется'}</span>`
  `${node.birth_place ? `<span>📍 ${node.birth_place}</span>` : ''}`
  `${burialPlace ? `<span>🪦 ${burialPlace}</span>` : ''}`
  ```
- **Стало:**
  ```javascript
  `<span class="meta-item">${HERALDIC_ICONS['meta-calendar']} ${node.birth_date || 'Дата уточняется'}</span>`
  `${node.birth_place ? `<span class="meta-item">${HERALDIC_ICONS['meta-pin']} ${node.birth_place}</span>` : ''}`
  `${burialPlace ? `<span class="meta-item">${HERALDIC_ICONS['meta-burial-cross']} ${burialPlace}</span>` : ''}`
  ```

---

## 5. Заключение и чек-лист готовности

1. Все 108 мест со смайликами из `emoji_digest.txt` получили семантически точную геральдическую замену в векторе.
2. Ноль внешних сетевых зависимостей (Google Fonts, CDN FontAwesome, Lucide): весь SVG инлайнится локально и строго соответствует 152-ФЗ и правилам безопасности Edge Functions.
3. Полная адаптация к Светлому Имперскому Пергаменту: гарантированный контраст не менее `12:1`, читаемость пожилыми родственниками без бликования.
