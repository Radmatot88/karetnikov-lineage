import os

code = """---
import '../styles/heritage.css';
---

<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, nofollow, noarchive, nosnippet" />
  <title>Sovereign Heritage Archive — Дорожная карта 7 колен</title>
</head>
<body>

  <!-- Hidden file input for attaching ancestor photos & scans (including iPhone HEIC/HEIF) -->
  <input
    id="photoFileInput"
    type="file"
    accept="image/*,.heic,.heif,.HEIC,.HEIF,image/heic,image/heif,image/webp,image/jpeg,image/png,image/tiff"
    style="display:none;"
  />

  <!-- ================= 1. FORTRESS ZERO-HARDCODE DUAL-ROLE AUTH GATE ================= -->
  <section id="fortressGate" class="fortress-gate" aria-label="Криптографический шлюз родового архива">
    <div class="gate-card">
      <div class="gate-crest" aria-hidden="true">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <path d="M12 2L4 5v6.09c0 5.05 3.41 9.76 8 10.91 4.59-1.15 8-5.86 8-10.91V5l-8-3z"/>
          <path d="M12 8v4m0 4h.01"/>
        </svg>
      </div>

      <div class="gate-badge-row">
        <span class="crypto-pill">AES-256-GCM Dual-Vault</span>
        <span class="crypto-pill">PBKDF2-SHA256 (100k)</span>
        <span class="crypto-pill">Zero-Hardcode</span>
      </div>

      <h1 class="gate-title">Родовой Архив VII Колен</h1>
      <p class="gate-subtitle">
        Закрытый фамильный контур (Интерактивная Дорожная Карта 127+ предков с фотоархивом).<br/>
        Двухролевой доступ: Ключ Владельца (Администратор) или Пароль Родственников (Append-Only).<br/>
        Расшифровка графа выполняется локально в памяти браузера через Web Crypto API.
      </p>

      <form id="authForm" class="gate-form" autocomplete="off">
        <div class="gate-input-wrap">
          <input
            id="passwordInput"
            type="password"
            class="gate-input"
            placeholder="Введите ключ доступа к родовому архиву..."
            required
            autofocus
          />
          <button type="button" id="togglePwBtn" class="gate-toggle-pw" title="Показать/скрыть ключ">
            ГЛАЗ
          </button>
        </div>
        <button type="submit" id="unlockBtn" class="gate-btn">
          Расшифровать и открыть Дорожную Карту Рода
        </button>
        <div id="authStatus" class="gate-status" role="status" aria-live="polite">
          Контейнер AES-256-GCM готов к проверке ключа
        </div>
      </form>

      <div class="gate-security-footnote">
        <div>🛡️ <strong>Astro Fortress:</strong> X-Robots noindex, AI-Scraper Block</div>
        <div>🔐 <strong>Zero-PII Leak:</strong> Без пароля данные физически нечитаемы</div>
      </div>
    </div>
  </section>

  <!-- ================= 2. MAIN WORKSPACE ================= -->
  <div id="workspace" class="workspace">
    <header class="topbar">
      <div class="brand-block">
        <div class="brand-emblem">VII</div>
        <div>
          <div style="display:flex; align-items:center; gap:8px;">
            <div class="brand-title">Sovereign Heritage Archive — Дорожная Карта Рода</div>
            <span id="userRoleBadge" class="user-role-badge role-owner">Администратор архива</span>
          </div>
          <div class="brand-sub">От меня (#1) вглубь до VII колена • Каретниковы • Юхины • Зубковы • Куманины</div>
        </div>
      </div>

      <nav class="nav-tabs" aria-label="Режимы отображения">
        <button class="nav-tab active" data-view="tree">1. Дорожная Карта Древа (Pan & Zoom)</button>
        <button class="nav-tab" data-view="fan">2. Круговой Веер 127 Предков</button>
        <button class="nav-tab" data-view="radar">3. Архивный Радар (Шуструй • Плешаново • Кошки)</button>
        <button class="nav-tab" id="tabNavAccess" data-view="access">4. Пульт Доступов & Playwright</button>
      </nav>

      <div class="topbar-actions">
        <button id="openBranchWizardBtn" class="btn-outline" style="border-color:#10b981; color:#6ee7b7;" title="Присоединить свою семейную ветку в Большой Род">🌿 Присоединить ветку</button>
        <button id="exportGedBtn" class="btn-outline" title="Скачать стандарт GEDCOM 5.5.1">⬇ GEDCOM (.ged)</button>
        <button id="exportJsonBtn" class="btn-outline" title="Скачать JSON со всеми загруженными фото">⬇ JSON + Фото</button>
        <button id="lockVaultBtn" class="btn-outline" title="Очистить память и закрыть архив">🔒 Закрыть</button>
      </div>
    </header>

    <!-- VIEW 1: INFINITE PAN & ZOOM ROADMAP TREE CANVAS -->
    <main id="view-tree" class="view-section active">
      <div id="roadmapShell" class="roadmap-shell">
        <!-- Floating Top HUD -->
        <div class="roadmap-hud-top">
          <!-- Эпистемический переключатель: 100% ФАКТ vs Полное Древо 7 Колен -->
          <div class="hud-panel mode-toggle-panel">
            <div class="epistemic-segmented-control" role="radiogroup" aria-label="Эпистемический режим отображения">
              <button
                id="modeAllBtn"
                type="button"
                class="seg-btn active"
                data-mode="all_levels"
                role="radio"
                aria-checked="true"
                title="Полномасштабное древо 7 колен (127 прямых слотов + боковые ветви + 15 парящих гипотез) [Горячая клавиша: A]"
              >
                <span class="seg-gem gold-gem"></span>
                <span class="seg-label">🏛️ Полное Древо 7 Колен (130 ячеек)</span>
                <span class="seg-counter" id="allNodesCounterReadout">137</span>
              </button>

              <button
                id="modeFactsBtn"
                type="button"
                class="seg-btn"
                data-mode="facts_only"
                role="radio"
                aria-checked="false"
                title="Подсветить 100% верифицированные архивные факты (19 персон) с мягким затенением слотов ожидания [Горячая клавиша: F]"
              >
                <span class="seg-gem cyan-gem"></span>
                <span class="seg-label">🟢 Подсветка 100% фактов</span>
                <span class="seg-counter" id="factsCounterReadout">19</span>
              </button>
            </div>

            <div class="mode-live-pill" id="modeLivePill">
              <span class="pill-dot pulse"></span>
              <span class="pill-text" id="modeLivePillText">ПОЛНОЕ ДРЕВО 7 КОЛЕН (1→2→4→8→16→32→64)</span>
            </div>
          </div>

          <div class="hud-panel">
            <span style="font-size:11.5px; color:var(--text-muted); font-weight:700;">Масштаб расширения:</span>
            <button class="chip-btn active" data-filter="all7" title="Полное расширение всех 7 поколений">Все 7 Колен (1→2→4→8→16→32→64 • 130 узлов)</button>
            <button class="chip-btn" data-filter="gen5" title="Ограничить 5 поколениями">5 Колен (1→2→4→8→16 • 34 узла)</button>
            <button class="chip-btn" data-filter="paternal" title="Только отцовская ветвь">Ветвь Отца (1→1→2→4→8→16→32)</button>
            <button class="chip-btn" data-filter="maternal" title="Только материнская ветвь">Ветвь Матери (1→1→2→4→8→16→32)</button>
            <button class="chip-btn" id="filterHypothesesBtn" data-filter="hypotheses" style="border-color:rgba(245,158,11,0.5); color:#fbbf24;" title="Подсветить и сфокусироваться на 15 парящих гипотезах">🪐 Парящие гипотезы (15)</button>
          </div>

          <div class="hud-panel">
            <input
              id="searchNodesInput"
              type="search"
              class="search-input"
              placeholder="Подсветить предка или село (напр. Шуструй)..."
            />
          </div>
        </div>

        <!-- Floating Bottom-Left Zoom Controls -->
        <div class="roadmap-zoom-dock">
          <button id="zoomOutBtn" class="zoom-btn" title="Отдалить (Колесико вниз)">−</button>
          <span id="zoomReadout" class="zoom-readout">85%</span>
          <button id="zoomInBtn" class="zoom-btn" title="Приблизить (Колесико вверх)">+</button>
          <button id="zoomResetBtn" class="chip-btn" title="Сфокусировать на мне (#1)">🎯 От меня (#1)</button>
          <button id="zoomFitBtn" class="chip-btn" title="Показать всю карту целиком">🗺️ Весь масштаб</button>
        </div>

        <!-- Transformable World -->
        <div id="roadmapWorld" class="roadmap-world">
          <svg id="roadmapSvgEdges" class="roadmap-svg-edges" width="4200" height="9000"></svg>
          <div id="roadmapNodesLayer" class="roadmap-nodes-layer"></div>
        </div>
      </div>
    </main>

    <!-- VIEW 2: 7-RING SUNBURST FAN CHART -->
    <section id="view-fan" class="view-section padded-view">
      <div class="fan-layout">
        <div class="fan-svg-box">
          <h2 style="font-size:18px; color:var(--gold-light); margin-bottom:6px;">
            Концентрический круговой радар 7 поколений (127 прямых слотов)
          </h2>
          <p style="font-size:12.5px; color:var(--text-muted); margin-bottom:14px;">
            Нажмите на любой сектор кольца (от I колена в центре до VII колена на внешнем ободе), чтобы открыть досье предка и загрузить фото.
          </p>
          <div id="fanChartContainer" style="width:100%; max-width:740px; display:flex; justify-content:center;"></div>
        </div>

        <aside class="legend-box">
          <h3 style="font-size:16px; color:var(--gold-light);">Эпистемическая шкала достоверности</h3>
          <div style="font-size:13px; display:flex; flex-direction:column; gap:10px;">
            <div><span style="color:var(--status-confirmed); font-weight:700;">● CONFIRMED_DOC</span> — Подтвержденные предки и братья (Самара, Плешаново/Подольск, Кошкинский р-н, с. Новый Шуструй)</div>
            <div><span style="color:var(--status-oral); font-weight:700;">● FAMILY_ORAL</span> — Прадеды IV колена (Григорий Каретников, Пётр Юхин, Владимир Зубков)</div>
            <div><span style="color:var(--status-candidate); font-weight:700;">● ARCHIVE_CANDIDATE</span> — Архивные пересечения в ГАПО, ЦГАСО и ГАОО (V–VII колена)</div>
            <div><span style="color:var(--status-unknown); font-weight:700;">● UNKNOWN_SLOT</span> — Вакантный слот матрицы Соса-Страдоница</div>
          </div>

          <hr style="border:none; border-top:1px solid rgba(148,163,184,0.15); margin:10px 0;" />
          <h3 style="font-size:15px; color:var(--gold-light); margin-bottom:8px;">4 родовых кластера</h3>
          <div id="clansLegendList" style="display:flex; flex-direction:column; gap:10px; font-size:12.5px;"></div>
        </aside>
      </div>
    </section>

    <!-- VIEW 3: ARCHIVE RADAR -->
    <section id="view-radar" class="view-section padded-view">
      <div style="margin-bottom:18px;">
        <h2 style="font-size:20px; color:var(--gold-light);">Архивный Радар: Новые находки по Плешаново/Подольску, Кошкинскому р-ну и Новому Шуструю</h2>
        <p style="font-size:13.5px; color:var(--text-muted);">
          Актуализированные архивные шифры и найденные ветви родственников по вашим точным географическим координатам.
        </p>
      </div>
      <div id="archiveLeadsGrid" class="cards-grid"></div>
    </section>

    <!-- VIEW 4: ACCESS GUIDE (ADMIN ONLY) -->
    <section id="view-access" class="view-section padded-view">
      <div style="margin-bottom:18px;">
        <h2 style="font-size:20px; color:var(--gold-light);">Автономный Playwright-доступ для агента и входы в архивы</h2>
        <p style="font-size:13.5px; color:var(--text-muted);">
          Как дать агенту постоянную сессию в АИС ЦГАСО (Самара), Familio и ВГД без передачи паролей.
        </p>
      </div>
      <div id="accessGuideGrid" class="cards-grid"></div>
    </section>
  </div>

  <!-- ================= 3. SLIDE-OVER ANCESTOR DOSSIER DRAWER ================= -->
  <div id="drawerBackdrop" class="drawer-backdrop"></div>
  <aside id="dossierDrawer" class="dossier-drawer" aria-label="Досье предка">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
      <span id="drawerAhnentafel" class="ahnentafel-badge" style="font-size:12px;">Слот #1</span>
      <button id="closeDrawerBtn" class="drawer-close">✕ Закрыть (Esc)</button>
    </div>
    <div id="drawerBody"></div>
  </aside>

  <!-- ================= 4. STEP-BY-STEP MODAL WIZARD: JOIN FAMILY BRANCH ================= -->
  <div id="branchWizardModal" class="wizard-modal-backdrop" aria-label="Присоединить семейную ветку">
    <div class="wizard-modal">
      <div class="wizard-header">
        <div class="wizard-title">🌿 Присоединить свою семейную ветку в Большой Род</div>
        <button type="button" class="wizard-close" id="closeBranchWizardBtn" title="Закрыть">✕</button>
      </div>

      <div class="wizard-steps-indicator">
        <div class="step-pill active" id="wizPill1">1. К кому присоединить</div>
        <div class="step-pill" id="wizPill2">2. Кем приходится</div>
        <div class="step-pill" id="wizPill3">3. Данные персоны</div>
        <div class="step-pill" id="wizPill4">4. Ваша подпись</div>
      </div>

      <form id="branchWizardForm">
        <!-- Step 1 -->
        <div class="wizard-step-pane active" id="wizPane1">
          <label class="wizard-label">Выберите известного предка или родственника, к которому присоединяется ветвь:</label>
          <select id="wizardTargetPerson" class="gate-input" style="padding:10px; font-size:13px; margin-bottom:10px;"></select>
          <p class="wizard-hint">
            Вы можете прикрепить потомка, супруга, родного брата или сестру к любой известной ячейке древа. Никаких .ged файлов загружать не требуется.
          </p>
          <div class="wizard-footer">
            <div></div>
            <button type="button" class="wizard-next-btn" id="toWizStep2">Далее: Родство →</button>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="wizard-step-pane" id="wizPane2">
          <label class="wizard-label">Кем новая персона приходится выбранному предку?</label>
          <div class="rel-choice-grid">
            <label class="rel-choice">
              <input type="radio" name="wiz_relation" value="Сын / Дочь" checked />
              <span>👶 Сын / Дочь</span>
            </label>
            <label class="rel-choice">
              <input type="radio" name="wiz_relation" value="Супруг / Супруга" />
              <span>💍 Супруг / Супруга</span>
            </label>
            <label class="rel-choice">
              <input type="radio" name="wiz_relation" value="Брат / Сестра" />
              <span>↔ Брат / Сестра</span>
            </label>
            <label class="rel-choice">
              <input type="radio" name="wiz_relation" value="Отец / Мать" />
              <span>⬆ Отец / Мать</span>
            </label>
          </div>
          <div class="wizard-footer">
            <button type="button" class="wizard-prev-btn" id="backToWizStep1">← Назад</button>
            <button type="button" class="wizard-next-btn" id="toWizStep3">Далее: Данные →</button>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="wizard-step-pane" id="wizPane3">
          <label class="wizard-label">Сведения о присоединяемом родственнике:</label>
          <input type="text" id="wizFullName" class="gate-input" placeholder="ФИО (напр. Каретников Андрей Валентинович) *" required style="margin-bottom:10px;" />
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:10px;">
            <input type="text" id="wizBirthDate" class="gate-input" placeholder="Год / Дата рождения (напр. 1968)" />
            <input type="text" id="wizDeathDate" class="gate-input" placeholder="Дата ухода (или ныне жив)" />
          </div>
          <input type="text" id="wizBirthPlace" class="gate-input" placeholder="Место рождения / село / город (напр. г. Самара)" style="margin-bottom:10px;" />
          <textarea id="wizBio" class="gate-input" style="min-height:75px; resize:vertical; margin-bottom:10px;" placeholder="Краткие биографические сведения, профессия, дети, памятные истории..."></textarea>
          <div class="wizard-footer">
            <button type="button" class="wizard-prev-btn" id="backToWizStep2">← Назад</button>
            <button type="button" class="wizard-next-btn" id="toWizStep4">Далее: Подпись →</button>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="wizard-step-pane" id="wizPane4">
          <label class="wizard-label">Ваша авторская подпись (для сохранения в реестре рода):</label>
          <input type="text" id="wizAuthorName" class="gate-input" placeholder="Ваше имя и родство (напр. Елена Каретникова, внучка) *" required style="margin-bottom:10px;" />
          <input type="text" id="wizAuthorContact" class="gate-input" placeholder="Телефон или Telegram для связи *" required style="margin-bottom:12px;" />
          <div id="wizSummaryPreview" class="wizard-summary-box"></div>
          <div class="wizard-footer">
            <button type="button" class="wizard-prev-btn" id="backToWizStep3">← Назад</button>
            <button type="submit" class="gate-btn" style="width:auto; padding:10px 24px;">🌿 Присоединить ветку в Большой Род</button>
          </div>
        </div>
      </form>

      <div id="wizSuccessBox" class="wizard-success-box" style="display:none;">
        <div style="font-size:38px; margin-bottom:8px;">🌿</div>
        <div style="font-size:18px; font-weight:700; color:#6ee7b7; margin-bottom:6px;">Семейная ветвь успешно присоединена!</div>
        <p style="font-size:13px; color:var(--text-muted); margin-bottom:14px; line-height:1.5;">
          Ваше дополнение добавлено в родовой архив и отображается на Дорожной Карте с отметкой «Добавлено родственниками».
        </p>
        <button type="button" id="closeWizSuccessBtn" class="gate-btn">Вернуться к Дорожной Карте</button>
      </div>
    </div>
  </div>

  <!-- ================= CLIENT-SIDE WEB CRYPTO, PHOTO VAULT & ROADMAP ENGINE ================= -->
  <script is:inline>
    let encryptedBundle = null;
    let lineageData = null;
    let currentRole = 'owner'; // 'owner' | 'relative_append_only'
    let activeFilter = 'all7';
    let epistemicMode = 'all_levels'; // 'all_levels' by default to ensure 7-gen expansion!
    let searchQuery = '';
    let failedAttempts = 0;

    // Storage keys
    const PHOTO_STORAGE_KEY = 'kh_heritage_photos_v1';
    const BURIAL_STORAGE_KEY = 'kh_ancestor_burials_v1';
    const MEMORIES_STORAGE_KEY = 'kh_ancestor_memories_v1';
    const QUORUM_STORAGE_KEY = 'kh_quorum_confirmations_v1';
    const PENDING_BRANCHES_KEY = 'kh_pending_branches_v1';

    let photoMap = {};
    let burialMap = {};
    let memoriesMap = {};
    let quorumMap = {};
    let currentPhotoTargetId = null;

    try {
      const sp = localStorage.getItem(PHOTO_STORAGE_KEY);
      if (sp) photoMap = JSON.parse(sp);
      const sb = localStorage.getItem(BURIAL_STORAGE_KEY);
      if (sb) burialMap = JSON.parse(sb);
      const sm = localStorage.getItem(MEMORIES_STORAGE_KEY);
      if (sm) memoriesMap = JSON.parse(sm);
      const sq = localStorage.getItem(QUORUM_STORAGE_KEY);
      if (sq) quorumMap = JSON.parse(sq);
    } catch {}

    function savePhotoMap() {
      try {
        localStorage.setItem(PHOTO_STORAGE_KEY, JSON.stringify(photoMap));
      } catch (e) {
        alert('Хранилище браузера заполнено, экспортируйте JSON + Фото.');
      }
    }

    function saveBurialMap() {
      try {
        localStorage.setItem(BURIAL_STORAGE_KEY, JSON.stringify(burialMap));
      } catch {}
    }

    function saveMemoriesMap() {
      try {
        localStorage.setItem(MEMORIES_STORAGE_KEY, JSON.stringify(memoriesMap));
      } catch {}
    }

    function saveQuorumMap() {
      try {
        localStorage.setItem(QUORUM_STORAGE_KEY, JSON.stringify(quorumMap));
      } catch {}
    }

    // List of 100% verified fact Ahnentafels
    const CONFIRMED_FACT_AHNENTAFELS = new Set([
      1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 24, 28
    ]);

    // Pan & Zoom State for Roadmap Canvas
    let panX = 60;
    let panY = 80;
    let zoom = 0.85;
    let isDragging = false;
    let dragStartX = 0;
    let dragStartY = 0;

    function applyRoadmapTransform() {
      const world = document.getElementById('roadmapWorld');
      const readout = document.getElementById('zoomReadout');
      if (world) {
        world.style.transform = `translate3d(${panX}px, ${panY}px, 0) scale(${zoom})`;
      }
      if (readout) {
        readout.textContent = `${Math.round(zoom * 100)}%`;
      }
    }

    function b64ToBytes(b64) {
      const bin = atob(b64);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      return bytes;
    }

    async function loadEncryptedBundle() {
      const res = await fetch('/vault/lineage_payload.enc.json', { cache: 'no-store' });
      if (!res.ok) throw new Error('Не удалось загрузить зашифрованный контейнер родословной');
      encryptedBundle = await res.json();
    }

    async function decryptEnvelope(env, password) {
      const enc = new TextEncoder();
      const keyMaterial = await window.crypto.subtle.importKey(
        'raw',
        enc.encode(password),
        { name: 'PBKDF2' },
        false,
        ['deriveBits', 'deriveKey']
      );

      const saltBytes = b64ToBytes(env.salt_b64 || env.salt);
      const ivBytes = b64ToBytes(env.iv_b64 || env.iv);
      const ciphertextBytes = b64ToBytes(env.ciphertext_b64 || env.ciphertext);

      const aesKey = await window.crypto.subtle.deriveKey(
        {
          name: 'PBKDF2',
          salt: saltBytes,
          iterations: env.iterations || 100000,
          hash: 'SHA-256'
        },
        keyMaterial,
        { name: 'AES-GCM', length: 256 },
        false,
        ['decrypt']
      );

      const decryptedBuffer = await window.crypto.subtle.decrypt(
        { name: 'AES-GCM', iv: ivBytes },
        aesKey,
        ciphertextBytes
      );

      const dec = new TextDecoder('utf-8');
      return JSON.parse(dec.decode(decryptedBuffer));
    }

    async function unlockVaultWithPassword(password) {
      if (!encryptedBundle) await loadEncryptedBundle();

      // Check if dual-envelope is present
      const envelopes = encryptedBundle.envelopes;
      if (envelopes && envelopes.owner) {
        // Attempt 1: Try decrypting envelopes.owner (Owner password)
        try {
          const ownerData = await decryptEnvelope(envelopes.owner, password);
          currentRole = 'owner';
          return ownerData;
        } catch (ownerErr) {
          // Attempt 2: If owner fails, try envelopes.relative (Relative password e.g. RodKaretnikov-1917!)
          if (envelopes.relative) {
            try {
              const relData = await decryptEnvelope(envelopes.relative, password);
              currentRole = 'relative_append_only';
              return relData;
            } catch (relErr) {
              throw new Error('Неверный ключ доступа к родовому архиву');
            }
          }
          throw ownerErr;
        }
      }

      // Legacy fallback
      const data = await decryptEnvelope(encryptedBundle, password);
      currentRole = 'owner';
      return data;
    }

    function applyRolePermissions() {
      const badge = document.getElementById('userRoleBadge');
      const tabAccess = document.getElementById('tabNavAccess');
      if (currentRole === 'relative_append_only') {
        if (badge) {
          badge.className = 'user-role-badge role-relative';
          badge.textContent = 'Гостевой режим родственников';
          badge.title = 'Режим дополнения родословной и воспоминаний (Append-Only)';
        }
        if (tabAccess) {
          tabAccess.style.display = 'none';
        }
      } else {
        if (badge) {
          badge.className = 'user-role-badge role-owner';
          badge.textContent = 'Администратор архива';
          badge.title = 'Полный доступ к архиву и исследовательским протоколам';
        }
        if (tabAccess) {
          tabAccess.style.display = '';
        }
      }
    }

    function getInitials(node) {
      const s = (node.surname || '').trim();
      const f = (node.first_name || '').trim();
      const c1 = s ? s[0].toUpperCase() : 'Р';
      const c2 = (f && !f.startsWith('Слот') && !f.startsWith('Ожидает')) ? f[0].toUpperCase() : String(node.generation || 'I');
      return `${c1}${c2}`;
    }

    function getNodePhoto(node) {
      return photoMap[node.id] || node.photo_url || null;
    }

    function triggerPhotoUpload(nodeId, event) {
      if (event) event.stopPropagation();
      currentPhotoTargetId = nodeId;
      const inp = document.getElementById('photoFileInput');
      inp.value = '';
      inp.click();
    }

    // Photo & Document Scan Upload Handler with WebP / Canvas scaling & iPhone HEIC support
    document.getElementById('photoFileInput').addEventListener('change', (e) => {
      const file = e.target.files && e.target.files[0];
      if (!file || !currentPhotoTargetId) return;

      const reader = new FileReader();
      reader.onload = (ev) => {
        const img = new Image();
        img.onload = () => {
          const canvas = document.createElement('canvas');
          const maxDim = 640;
          let w = img.width;
          let h = img.height;
          if (w > maxDim || h > maxDim) {
            if (w > h) {
              h = Math.round((h * maxDim) / w);
              w = maxDim;
            } else {
              w = Math.round((w * maxDim) / h);
              h = maxDim;
            }
          }
          canvas.width = w;
          canvas.height = h;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);

          let dataUrl = '';
          try {
            dataUrl = canvas.toDataURL('image/webp', 0.88);
            if (!dataUrl || !dataUrl.startsWith('data:image/webp')) {
              dataUrl = canvas.toDataURL('image/jpeg', 0.85);
            }
          } catch {
            dataUrl = canvas.toDataURL('image/jpeg', 0.85);
          }

          photoMap[currentPhotoTargetId] = dataUrl;
          savePhotoMap();
          if (lineageData) {
            renderRoadmapCanvas(lineageData);
            const allNodes = [...lineageData.nodes, ...(lineageData.collateral_nodes || [])];
            const found = allNodes.find(x => x.id === currentPhotoTargetId);
            if (found && document.getElementById('dossierDrawer').classList.contains('open')) {
              openDossier(found.ahnentafel);
            }
          }
        };
        img.onerror = () => {
          alert('Не удалось декодировать изображение. Если это файл iPhone HEIC, сохраните его в JPEG/PNG или загрузите с устройства Apple.');
        };
        img.src = ev.target.result;
      };
      reader.readAsDataURL(file);
    });

    function setEpistemicMode(mode) {
      epistemicMode = mode;
      const factsBtn = document.getElementById('modeFactsBtn');
      const allBtn = document.getElementById('modeAllBtn');
      const livePill = document.getElementById('modeLivePill');
      const pillText = document.getElementById('modeLivePillText');

      if (mode === 'facts_only') {
        if (factsBtn) {
          factsBtn.classList.add('active');
          factsBtn.setAttribute('aria-checked', 'true');
        }
        if (allBtn) {
          allBtn.classList.remove('active');
          allBtn.setAttribute('aria-checked', 'false');
        }
        if (livePill) {
          livePill.style.borderColor = 'rgba(16, 185, 129, 0.3)';
          livePill.style.background = 'rgba(16, 185, 129, 0.1)';
        }
        if (pillText) {
          pillText.textContent = 'ПОДСВЕТКА 100% ФАКТОВ (19 ПЕРСОН)';
          pillText.style.color = '#34d399';
        }
      } else {
        if (factsBtn) {
          factsBtn.classList.remove('active');
          factsBtn.setAttribute('aria-checked', 'false');
        }
        if (allBtn) {
          allBtn.classList.add('active');
          allBtn.setAttribute('aria-checked', 'true');
        }
        if (livePill) {
          livePill.style.borderColor = 'rgba(212, 175, 55, 0.3)';
          livePill.style.background = 'rgba(212, 175, 55, 0.1)';
        }
        if (pillText) {
          pillText.textContent = 'ПОЛНОЕ ДРЕВО 7 КОЛЕН (1→2→4→8→16→32→64)';
          pillText.style.color = '#f3dc8a';
        }
      }

      if (lineageData) {
        renderRoadmapCanvas(lineageData);
        renderFanChart(lineageData);
      }
    }

    // ================= INFINITE EXPANDING BINARY TREE RENDERER (1->2->4->8->16->32->64) =================
    function renderRoadmapCanvas(data) {
      const nodesLayer = document.getElementById('roadmapNodesLayer');
      const svgEdges = document.getElementById('roadmapSvgEdges');
      const q = searchQuery.trim().toLowerCase();

      const allDirect = data.nodes || [];
      const allCollateral = data.collateral_nodes || [];
      const allHypotheses = data.floating_hypotheses || [];

      // Max generation is always 7 (or 5 for gen5 filter) so the binary tree strictly expands!
      const maxGen = activeFilter === 'gen5' ? 5 : 7;

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
        if (activeFilter === 'paternal') return c.branch === 'paternal';
        if (activeFilter === 'maternal') return c.branch === 'maternal';
        return true;
      });

      const visibleHypotheses = allHypotheses.filter(h => {
        if (h.generation > maxGen) return false;
        if (activeFilter === 'paternal') return h.branch === 'paternal';
        if (activeFilter === 'maternal') return h.branch === 'maternal';
        return true;
      });

      const genGroups = {};
      for (let g = 1; g <= maxGen; g++) genGroups[g] = [];
      visibleDirect.forEach(n => {
        genGroups[n.generation].push(n);
      });

      // Sort each generation by Ahnentafel number so binary pairs (2n, 2n+1) are strictly adjacent
      for (let g = 1; g <= maxGen; g++) {
        genGroups[g].sort((a, b) => a.ahnentafel - b.ahnentafel);
      }

      const COL_X_STEP = 450;
      const CARD_W = 310;
      const CARD_H = 108;

      // Insert collateral siblings right next to their sibling in the same generation column so cards never overlap
      visibleCollateral.forEach(c => {
        const col = genGroups[c.generation];
        if (!col) return;
        const sibIdx = col.findIndex(x => x.ahnentafel === c.sibling_of_ahnentafel);
        if (sibIdx !== -1) {
          col.splice(sibIdx + 1, 0, c);
        } else {
          col.push(c);
        }
      });

      // Progressive vertical gap per generation so every column strictly expands outward
      const GEN_GAPS = {
        1: 40,
        2: 60,
        3: 54,
        4: 64,
        5: 52,
        6: 36,
        7: 20
      };

      function getColHeight(g) {
        const count = genGroups[g].length;
        if (count === 0) return 0;
        const gap = GEN_GAPS[g] || 24;
        return count * CARD_H + (count - 1) * gap;
      }

      function getTotalColHeight(g) {
        const baseH = getColHeight(g);
        const hyps = visibleHypotheses.filter(h => h.generation === g);
        const hypH = hyps.length > 0 ? (60 + hyps.length * (CARD_H + 20)) : 0;
        return baseH + hypH;
      }

      const maxColH = Math.max(...Object.keys(genGroups).map(g => getTotalColHeight(Number(g))), 900);
      const TOP_PAD = 110;
      const totalCanvasH = maxColH + TOP_PAD * 2;
      const totalCanvasW = maxGen * COL_X_STEP + 360;
      const centerY = totalCanvasH / 2;

      svgEdges.setAttribute('width', String(totalCanvasW));
      svgEdges.setAttribute('height', String(totalCanvasH));

      const coordsByAhn = {};
      const coordsByHyp = {};

      // Calculate coordinates for direct nodes
      for (let g = 1; g <= maxGen; g++) {
        const list = genGroups[g];
        const colX = 80 + (g - 1) * COL_X_STEP;
        const gap = GEN_GAPS[g] || 24;
        const colH = getColHeight(g);
        const startY = centerY - colH / 2;

        list.forEach((node, idx) => {
          const y = startY + idx * (CARD_H + gap);
          coordsByAhn[node.ahnentafel] = {
            x: colX,
            y,
            w: node.ahnentafel === 1 ? 330 : CARD_W,
            h: CARD_H,
            node
          };
        });

        // Place floating hypotheses below the column
        const hypsInGen = visibleHypotheses.filter(h => h.generation === g);
        if (hypsInGen.length > 0) {
          const hypStartY = startY + colH + 60;
          hypsInGen.forEach((hyp, hIdx) => {
            const hypY = hypStartY + hIdx * (CARD_H + 22);
            coordsByHyp[hyp.id] = {
              x: colX,
              y: hypY,
              w: CARD_W,
              h: CARD_H,
              hyp
            };
          });
        }
      }

      let htmlParts = [];
      const genTitles = {
        1: ['I КОЛЕНО — 1 СЛОТ', 'Пробанд (#1)'],
        2: ['II КОЛЕНО — 2 СЛОТА (+1 БРАТ)', 'Родители (#2–#3)'],
        3: ['III КОЛЕНО — 4 СЛОТА (+2 БРАТА)', 'Дедушки и бабушки (#4–#7)'],
        4: ['IV КОЛЕНО — 8 СЛОТОВ', 'Прадеды и прабабушки (#8–#15)'],
        5: ['V КОЛЕНО — 16 СЛОТОВ', 'Прапрадеды • Перепись 1917 г. (#16–#31)'],
        6: ['VI КОЛЕНО — 32 СЛОТА', 'Прапрапрадеды • Ревизия 1858 г. (#32–#63)'],
        7: ['VII КОЛЕНО — 64 СЛОТА', 'Прапрапрапрадеды • 1815–1834 гг. (#64–#127)']
      };

      for (let g = 1; g <= maxGen; g++) {
        const colX = 80 + (g - 1) * COL_X_STEP;
        const colH = getColHeight(g);
        const bannerTop = Math.max(18, (centerY - colH / 2) - 58);
        const [t1, t2] = genTitles[g];
        htmlParts.push(`
          <div class="canvas-gen-banner" style="left:${colX}px; top:${bannerTop}px;">
            <div class="t1">${t1}</div>
            <div class="t2">${t2}</div>
          </div>
        `);

        // Floating hypothesis banner if column has hypotheses
        const hypsInGen = visibleHypotheses.filter(h => h.generation === g);
        if (hypsInGen.length > 0) {
          const hypBannerTop = (centerY - colH / 2) + colH + 24;
          htmlParts.push(`
            <div class="canvas-hyp-banner" style="left:${colX}px; top:${hypBannerTop}px;">
              🪐 ПАРЯЩИЕ ГИПОТЕЗЫ КОЛЕНА (${hypsInGen.length})
            </div>
          `);
        }
      }

      // Render direct & collateral nodes
      Object.values(coordsByAhn).forEach(box => {
        const node = box.node;
        const photoSrc = getNodePhoto(node);
        const portraitInner = photoSrc
          ? `<img src="${photoSrc}" alt="${node.full_name}" />`
          : `<div class="rm-portrait-placeholder">${getInitials(node)}</div>`;

        const branchLabel = node.is_relative_proposal
          ? '🌿 Ветвь родственников'
          : node.is_collateral
            ? 'Родной брат'
            : node.branch === 'paternal'
              ? 'Линия Отца'
              : node.branch === 'maternal'
                ? 'Линия Матери'
                : 'Пробанд (#1)';

        const deathStr = node.death_date ? ` — ${node.death_date}` : '';
        const extraClass = node.ahnentafel === 1 ? 'proband-node' : node.is_collateral ? 'collateral-node' : '';

        let searchHighlightStyle = '';
        if (q) {
          const hay = `${node.full_name} ${node.birth_place} ${node.sub_clan} ${node.notes} #${node.ahnentafel}`.toLowerCase();
          if (hay.includes(q)) {
            searchHighlightStyle = 'outline: 3px solid #f3dc8a; box-shadow: 0 0 28px rgba(243,220,138,0.65); z-index: 15;';
          } else {
            searchHighlightStyle = 'opacity: 0.25;';
          }
        }

        if (activeFilter === 'hypotheses') {
          searchHighlightStyle += ' opacity: 0.35;';
        }

        const isFactConfirmed = CONFIRMED_FACT_AHNENTAFELS.has(node.ahnentafel) || node.is_fact_confirmed;
        const isPendingSlot = (epistemicMode === 'facts_only' && !isFactConfirmed);

        let cardClasses = `rm-node status-${node.status} branch-${node.branch} ${extraClass}`;
        if (isFactConfirmed) cardClasses += ' is-fact-confirmed';
        if (isPendingSlot) cardClasses += ' is-pending-fact';

        const factBadge = isFactConfirmed ? `<span class="badge-fact-100">🟢 100% ФАКТ</span>` : '';
        const displayName = isPendingSlot
          ? `Слот #${node.ahnentafel} • Ожидает выписки архива`
          : node.full_name;

        htmlParts.push(`
          <article
            class="${cardClasses}"
            style="left:${box.x}px; top:${box.y}px; ${searchHighlightStyle}"
            data-ahnentafel="${node.ahnentafel}"
          >
            <div class="rm-portrait" data-photo-trigger="${node.id}" title="Нажмите, чтобы загрузить или обновить фотографию">
              ${portraitInner}
              <span class="rm-photo-badge">📷 Фото</span>
            </div>
            <div class="rm-content">
              <div class="rm-top-badges">
                <span class="ahnentafel-badge">${node.is_collateral ? `Брат #${node.sibling_of_ahnentafel}` : `Слот #${node.ahnentafel}`}</span>
                ${factBadge}
                <span class="branch-tag ${node.branch}">${branchLabel}</span>
              </div>
              <div class="rm-name">${displayName}</div>
              <div class="rm-dates">${node.birth_date || ''}${deathStr}</div>
              <div class="rm-place" title="${node.birth_place || ''}">📍 ${node.birth_place || ''}</div>
            </div>
          </article>
        `);
      });

      // Render floating orbital hypotheses
      Object.values(coordsByHyp).forEach(box => {
        const hyp = box.hyp;
        let hypHighlightStyle = '';
        if (q) {
          const hay = `${hyp.full_name} ${hyp.village} ${hyp.role_badge} ${hyp.relationship_hypothesis}`.toLowerCase();
          if (hay.includes(q)) {
            hypHighlightStyle = 'outline: 3px solid #f59e0b; box-shadow: 0 0 32px rgba(245,158,11,0.8); z-index: 15;';
          } else {
            hypHighlightStyle = 'opacity: 0.3;';
          }
        }
        if (activeFilter === 'hypotheses') {
          hypHighlightStyle = 'outline: 3px solid #fbbf24; box-shadow: 0 0 36px rgba(251,191,36,0.85); z-index: 20;';
        }

        htmlParts.push(`
          <article
            class="rm-node floating-hypothesis-node"
            style="left:${box.x}px; top:${box.y}px; ${hypHighlightStyle}"
            data-hypothesis-id="${hyp.id}"
            title="Орбитальная гипотеза: нажмите для просмотра архивного обоснования"
          >
            <div class="rm-content" style="width:100%;">
              <div class="rm-top-badges" style="margin-bottom:5px;">
                <span class="badge-floating-hyp">ГИПОТЕЗА / КАНДИДАТ В РОД</span>
                <span class="ahnentafel-badge" style="background:rgba(245,158,11,0.25); color:#fbbf24;">${hyp.confidence}%</span>
              </div>
              <div class="rm-name" style="color:#fef3c7; font-size:12.5px;">${hyp.full_name}</div>
              <div class="rm-dates" style="color:#fbbf24; font-size:11px;">${hyp.era}</div>
              <div class="rm-place" style="color:#cbd5e1;" title="${hyp.village}">📍 ${hyp.village}</div>
              <div style="font-size:10px; color:#f59e0b; margin-top:4px; font-weight:700;">
                🔗 Связь: Слот #${hyp.probable_relative_ahnentafel} (${hyp.clan})
              </div>
            </div>
          </article>
        `);
      });

      nodesLayer.innerHTML = htmlParts.join('');

      // Draw SVG Bezier Connectors strictly expanding 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64
      let pathsSvg = '';
      Object.values(coordsByAhn).forEach(srcBox => {
        const n = srcBox.node;
        if (!n.is_collateral) {
          const targets = [n.father_ahnentafel, n.mother_ahnentafel].filter(Boolean);
          targets.forEach(targetAhn => {
            const dstBox = coordsByAhn[targetAhn];
            if (!dstBox) return;
            const x1 = srcBox.x + srcBox.w;
            const y1 = srcBox.y + srcBox.h / 2;
            const x2 = dstBox.x;
            const y2 = dstBox.y + dstBox.h / 2;
            const cpx1 = x1 + (x2 - x1) * 0.45;
            const cpx2 = x1 + (x2 - x1) * 0.55;
            const strokeColor = dstBox.node.branch === 'paternal'
              ? 'rgba(224, 122, 95, 0.72)'
              : 'rgba(42, 157, 143, 0.72)';
            const strokeWidth = dstBox.node.status === 'UNKNOWN_SLOT' ? '1.5' : '2.8';
            const dash = dstBox.node.status === 'UNKNOWN_SLOT' ? 'stroke-dasharray="6,5"' : '';

            pathsSvg += `
              <path
                d="M ${x1} ${y1} C ${cpx1} ${y1}, ${cpx2} ${y2}, ${x2} ${y2}"
                fill="none"
                stroke="${strokeColor}"
                stroke-width="${strokeWidth}"
                ${dash}
              />
              <circle cx="${x2}" cy="${y2}" r="4" fill="${strokeColor}" />
            `;
          });
        } else {
          const sibBox = coordsByAhn[n.sibling_of_ahnentafel];
          if (sibBox) {
            const x1 = sibBox.x + 32;
            const y1 = sibBox.y + sibBox.h;
            const x2 = srcBox.x + 32;
            const y2 = srcBox.y;
            pathsSvg += `
              <line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"
                stroke="#d4af37" stroke-width="2.2" stroke-dasharray="4,4" />
            `;
          }
          const parentBox = coordsByAhn[n.parent_ahnentafel];
          if (parentBox) {
            const x1 = srcBox.x + srcBox.w;
            const y1 = srcBox.y + srcBox.h / 2;
            const x2 = parentBox.x;
            const y2 = parentBox.y + parentBox.h / 2;
            const cpx = x1 + (x2 - x1) * 0.5;
            pathsSvg += `
              <path d="M ${x1} ${y1} C ${cpx} ${y1}, ${cpx} ${y2}, ${x2} ${y2}"
                fill="none" stroke="rgba(212, 175, 55, 0.5)" stroke-width="1.8" stroke-dasharray="6,4" />
            `;
          }
        }
      });

      // Draw SVG connectors for floating hypotheses
      Object.values(coordsByHyp).forEach(hypBox => {
        const hyp = hypBox.hyp;
        if (hyp.probable_relative_ahnentafel) {
          const relBox = coordsByAhn[hyp.probable_relative_ahnentafel];
          if (relBox) {
            const x1 = relBox.x + relBox.w / 2;
            const y1 = relBox.y + relBox.h;
            const x2 = hypBox.x + hypBox.w / 2;
            const y2 = hypBox.y;
            const cpy1 = y1 + (y2 - y1) * 0.5;
            const cpy2 = y1 + (y2 - y1) * 0.5;

            pathsSvg += `
              <path
                d="M ${x1} ${y1} C ${x1} ${cpy1}, ${x2} ${cpy2}, ${x2} ${y2}"
                fill="none"
                stroke="rgba(245, 158, 11, 0.65)"
                stroke-width="2"
                stroke-dasharray="5,5"
              />
              <circle cx="${x2}" cy="${y2}" r="3.5" fill="#f59e0b" />
            `;
          }
        }
      });

      svgEdges.innerHTML = pathsSvg;

      // Event listeners for photo upload triggers
      nodesLayer.querySelectorAll('[data-photo-trigger]').forEach(el => {
        el.addEventListener('click', (ev) => {
          triggerPhotoUpload(el.getAttribute('data-photo-trigger'), ev);
        });
      });

      // Event listeners for direct cards
      nodesLayer.querySelectorAll('.rm-node:not(.floating-hypothesis-node)').forEach(card => {
        card.addEventListener('click', () => {
          const ahn = parseInt(card.getAttribute('data-ahnentafel'), 10);
          openDossier(ahn);
        });
      });

      // Event listeners for hypothesis cards
      nodesLayer.querySelectorAll('.floating-hypothesis-node').forEach(card => {
        card.addEventListener('click', () => {
          const hypId = card.getAttribute('data-hypothesis-id');
          openHypothesisDossier(hypId);
        });
      });
    }

    function focusOnProband() {
      const shell = document.getElementById('roadmapShell');
      const probandCard = document.querySelector('.rm-node[data-ahnentafel="1"]');
      zoom = 0.65;
      if (probandCard && shell) {
        const cardTop = parseFloat(probandCard.style.top || '450');
        panX = 40;
        panY = (shell.clientHeight / 2) - ((cardTop + 54) * zoom);
      } else {
        panX = 40;
        panY = 80;
      }
      applyRoadmapTransform();
    }

    function fitEntireRoadmap() {
      const shell = document.getElementById('roadmapShell');
      const svgEdges = document.getElementById('roadmapSvgEdges');
      if (!shell || !svgEdges) return;
      const w = parseFloat(svgEdges.getAttribute('width') || '3600');
      const h = parseFloat(svgEdges.getAttribute('height') || '8500');
      const scaleX = (shell.clientWidth - 60) / w;
      const scaleY = (shell.clientHeight - 80) / h;
      zoom = Math.max(0.12, Math.min(scaleX, scaleY, 0.95));
      panX = 30;
      panY = Math.max(20, (shell.clientHeight - h * zoom) / 2);
      applyRoadmapTransform();
    }

    // Setup Mouse Drag & Wheel Zoom on #roadmapShell
    (function initCanvasPanZoom() {
      const shell = document.getElementById('roadmapShell');
      if (!shell) return;

      shell.addEventListener('mousedown', (e) => {
        if (e.target.closest('.hud-panel') || e.target.closest('.roadmap-zoom-dock') || e.target.closest('.rm-node')) {
          return;
        }
        isDragging = true;
        dragStartX = e.clientX - panX;
        dragStartY = e.clientY - panY;
        shell.classList.add('dragging');
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        panX = e.clientX - dragStartX;
        panY = e.clientY - dragStartY;
        applyRoadmapTransform();
      });

      window.addEventListener('mouseup', () => {
        isDragging = false;
        shell.classList.remove('dragging');
      });

      shell.addEventListener('wheel', (e) => {
        e.preventDefault();
        const rect = shell.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        const prevZoom = zoom;
        const delta = e.deltaY < 0 ? 1.12 : 0.89;
        zoom = Math.min(2.2, Math.max(0.12, zoom * delta));

        panX = mouseX - ((mouseX - panX) * (zoom / prevZoom));
        panY = mouseY - ((mouseY - panY) * (zoom / prevZoom));
        applyRoadmapTransform();
      }, { passive: false });

      document.getElementById('zoomInBtn').addEventListener('click', () => {
        zoom = Math.min(2.2, zoom * 1.2);
        applyRoadmapTransform();
      });
      document.getElementById('zoomOutBtn').addEventListener('click', () => {
        zoom = Math.max(0.12, zoom * 0.82);
        applyRoadmapTransform();
      });
      document.getElementById('zoomResetBtn').addEventListener('click', focusOnProband);
      document.getElementById('zoomFitBtn').addEventListener('click', fitEntireRoadmap);
    })();

    // ================= FAN CHART (SUNBURST) =================
    function polarToCartesian(cx, cy, r, angleInDegrees) {
      const rad = (angleInDegrees - 90) * Math.PI / 180.0;
      return { x: cx + (r * Math.cos(rad)), y: cy + (r * Math.sin(rad)) };
    }

    function createAnnularSectorPath(cx, cy, rInner, rOuter, startAngle, endAngle) {
      const startOuter = polarToCartesian(cx, cy, rOuter, endAngle);
      const endOuter = polarToCartesian(cx, cy, rOuter, startAngle);
      const startInner = polarToCartesian(cx, cy, rInner, endAngle);
      const endInner = polarToCartesian(cx, cy, rInner, startAngle);
      const largeArc = (endAngle - startAngle) <= 180 ? '0' : '1';
      return [
        'M', startOuter.x, startOuter.y,
        'A', rOuter, rOuter, 0, largeArc, 0, endOuter.x, endOuter.y,
        'L', endInner.x, endInner.y,
        'A', rInner, rInner, 0, largeArc, 1, startInner.x, startInner.y,
        'Z'
      ].join(' ');
    }

    function renderFanChart(data) {
      const container = document.getElementById('fanChartContainer');
      const size = 680;
      const cx = size / 2;
      const cy = size / 2;
      const nodeMap = {};
      data.nodes.forEach(n => { nodeMap[n.ahnentafel] = n; });

      const statusColors = {
        CONFIRMED_DOC: '#10b981',
        FAMILY_ORAL: '#38bdf8',
        ARCHIVE_CANDIDATE: '#f59e0b',
        UNKNOWN_SLOT: '#1e293b'
      };

      let pathsHtml = '';
      const probandNode = nodeMap[1];
      pathsHtml += `
        <circle cx="${cx}" cy="${cy}" r="36" fill="#d4af37" stroke="#07090e" stroke-width="2"
          style="cursor:pointer;" data-ahnentafel="1">
          <title>#1 ${probandNode ? probandNode.full_name : ''} (${probandNode ? probandNode.birth_date : ''})</title>
        </circle>
        <text x="${cx}" y="${cy + 4}" text-anchor="middle" fill="#07090e" font-size="11" font-weight="800" pointer-events="none">#1 Я</text>
      `;

      const ringThickness = 42;
      for (let gen = 2; gen <= 7; gen++) {
        const count = Math.pow(2, gen - 1);
        const startId = count;
        const rInner = 38 + (gen - 2) * ringThickness;
        const rOuter = rInner + ringThickness - 2;
        const angleStep = 360 / count;

        for (let i = 0; i < count; i++) {
          const ahn = startId + i;
          const node = nodeMap[ahn];
          const a0 = i * angleStep;
          const a1 = (i + 1) * angleStep;
          const d = createAnnularSectorPath(cx, cy, rInner, rOuter, a0, a1 - 0.4);
          const fill = (node && statusColors[node.status]) || '#1e293b';
          const stroke = (node && node.branch === 'paternal') ? 'rgba(224,122,95,0.45)' : 'rgba(42,157,143,0.45)';

          pathsHtml += `
            <path d="${d}" fill="${fill}" stroke="${stroke}" stroke-width="1"
              style="cursor:pointer;" data-ahnentafel="${ahn}">
              <title>#${ahn} (${gen} колено): ${node ? node.full_name : ''} — ${node ? node.birth_place : ''}</title>
            </path>
          `;
        }
      }

      container.innerHTML = `<svg viewBox="0 0 ${size} ${size}" width="100%" height="100%" style="max-width:660px;">${pathsHtml}</svg>`;
      container.querySelectorAll('[data-ahnentafel]').forEach(el => {
        el.addEventListener('click', () => openDossier(parseInt(el.getAttribute('data-ahnentafel'), 10)));
      });

      const legendList = document.getElementById('clansLegendList');
      if (data.meta && data.meta.clans) {
        legendList.innerHTML = data.meta.clans.map(c => `
          <div style="padding:10px; background:var(--bg-panel); border-radius:8px; border-left:3px solid ${c.color};">
            <div style="font-weight:700; color:var(--text-main);">${c.name} (${c.branch})</div>
            <div style="color:var(--text-muted); font-size:11.5px;">📍 ${c.region}</div>
            <div style="color:var(--gold-light); font-size:11.5px; margin-top:3px;">🔗 ${c.key_ancestor}</div>
          </div>
        `).join('');
      }
    }

    function renderArchiveRadar(data) {
      const grid = document.getElementById('archiveLeadsGrid');
      grid.innerHTML = (data.archive_leads || []).map(lead => `
        <article class="archive-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="ahnentafel-badge">${lead.priority} • ${lead.lead_id}</span>
            <span style="font-size:12px; color:var(--gold-light); font-weight:600;">${lead.clan}</span>
          </div>
          <h3>${lead.title}</h3>
          <div style="font-size:12.5px; color:var(--text-muted);">📍 <strong>Историческая привязка:</strong> ${lead.region}</div>
          <div style="font-size:12.5px; color:var(--text-muted);">🏛️ <strong>Архив:</strong> ${lead.archive_name}</div>
          <div class="cipher-box">📜 Шифр фонда: ${lead.fond_cipher}</div>
          <p style="font-size:13.5px; color:var(--text-main);">${lead.summary}</p>
          <div style="margin-top:auto; padding-top:10px; border-top:1px solid rgba(148,163,184,0.14); font-size:12.5px; color:#52b788;">
            <strong>🎯 Следующий шаг:</strong> ${lead.next_action}
          </div>
        </article>
      `).join('');
    }

    function renderAccessGuide(data) {
      const grid = document.getElementById('accessGuideGrid');
      grid.innerHTML = (data.access_guide || []).map(item => `
        <article class="archive-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="ahnentafel-badge">ШАГ ${item.step}</span>
            <span style="font-size:12px; color:#52b788; font-weight:600;">${item.cost}</span>
          </div>
          <h3>${item.service}</h3>
          <p style="font-size:13px; color:var(--text-muted);">${item.purpose}</p>
          <div class="cipher-box">🎯 Команда / Действие: ${item.action_for_owner}</div>
          <a href="${item.url}" target="_blank" rel="noopener noreferrer" class="gate-btn" style="text-align:center; text-decoration:none; margin-top:auto; display:block;">
            Открыть ${item.service.split('(')[0].trim()} ↗
          </a>
        </article>
      `).join('');
    }

    // ================= 5. ANCESTOR DOSSIER DRAWER WITH BURIAL & MEMORIES =================
    function openDossier(ahnentafelNum) {
      if (!lineageData) return;
      const allNodes = [...lineageData.nodes, ...(lineageData.collateral_nodes || [])];
      const node = allNodes.find(n => n.ahnentafel === ahnentafelNum);
      if (!node) return;

      document.getElementById('drawerAhnentafel').textContent = node.is_relative_proposal
        ? `Ветвь родственников • ${node.generation || 'II'} колено`
        : node.is_collateral
          ? `Боковая ветвь • ${node.generation_label}`
          : `Ahnentafel #${node.ahnentafel} • ${node.generation_label}`;

      const father = allNodes.find(n => n.ahnentafel === (node.father_ahnentafel || node.parent_ahnentafel));
      const mother = allNodes.find(n => n.ahnentafel === node.mother_ahnentafel);
      const child = allNodes.find(n => n.ahnentafel === (node.child_ahnentafel || node.sibling_of_ahnentafel));

      const relButtons = [];
      if (child) {
        const label = node.is_collateral ? '↔ Родной брат/сестра' : '⬇ Потомок';
        relButtons.push(`<button class="btn-outline" data-jump="${child.ahnentafel}">${label} (#${child.ahnentafel}: ${child.full_name})</button>`);
      }
      if (father) {
        relButtons.push(`<button class="btn-outline" data-jump="${father.ahnentafel}">⬆ Отец (#${father.ahnentafel}: ${father.full_name})</button>`);
      }
      if (mother) {
        relButtons.push(`<button class="btn-outline" data-jump="${mother.ahnentafel}">⬆ Мать (#${mother.ahnentafel}: ${mother.full_name})</button>`);
      }

      const photoSrc = getNodePhoto(node);
      const portraitHeroHtml = photoSrc
        ? `<img src="${photoSrc}" alt="${node.full_name}" />`
        : `<div class="rm-portrait-placeholder" style="font-size:26px;">${getInitials(node)}</div>`;

      // Smart Burial Rule 1920:
      const burialPlace = burialMap[node.id] || node.burial_place || null;
      let burialBlockHtml = '';
      if (burialPlace) {
        burialBlockHtml = `
          <div class="field-row burial-row">
            <div class="field-label">Место захоронения (Некрополь)</div>
            <div class="field-val" style="display:flex; justify-content:space-between; align-items:center;">
              <span>🪦 ${burialPlace}</span>
              <button type="button" id="editBurialBtn" class="btn-outline" style="padding:2px 8px; font-size:11px;">Изменить</button>
            </div>
            <div id="burialInlineForm" class="burial-inline-form" style="display:none; margin-top:8px;">
              <input type="text" id="burialInputVal" class="gate-input" value="${burialPlace}" placeholder="Кладбище, населенный пункт, сектор/могила..." style="padding:7px 10px; font-size:12px; margin-bottom:8px;" />
              <div style="display:flex; gap:8px;">
                <button type="button" id="saveBurialBtn" class="btn-outline" style="border-color:#10b981; color:#6ee7b7; font-size:11.5px;">Сохранить</button>
                <button type="button" id="cancelBurialBtn" class="btn-outline" style="font-size:11.5px;">Отмена</button>
              </div>
            </div>
          </div>
        `;
      } else {
        burialBlockHtml = `
          <div class="field-row burial-row">
            <div id="burialAddPrompt">
              <button type="button" id="showAddBurialBtn" class="btn-outline add-burial-btn">
                + Указать место захоронения
              </button>
            </div>
            <div id="burialInlineForm" class="burial-inline-form" style="display:none; margin-top:8px;">
              <input type="text" id="burialInputVal" class="gate-input" placeholder="Кладбище, населенный пункт, сектор/могила..." style="padding:7px 10px; font-size:12px; margin-bottom:8px;" />
              <div style="display:flex; gap:8px;">
                <button type="button" id="saveBurialBtn" class="btn-outline" style="border-color:#10b981; color:#6ee7b7; font-size:11.5px;">Сохранить место</button>
                <button type="button" id="cancelBurialBtn" class="btn-outline" style="font-size:11.5px;">Отмена</button>
              </div>
            </div>
          </div>
        `;
      }

      // Quorum confirmations
      const baseQuorum = node.status === 'CONFIRMED_DOC' ? 2 : 1;
      const userVotes = quorumMap[node.id] || 0;
      const totalQuorum = baseQuorum + userVotes;
      const userHasConfirmed = Boolean(quorumMap[node.id + '_user']);

      // Family memories
      const memories = memoriesMap[node.id] || [];
      const memoriesHtml = memories.map(m => `
        <div class="memory-card">
          <div class="memory-card-header">
            <span>✍️ ${m.author}</span>
            <span class="memory-card-date">${m.timestamp}</span>
          </div>
          <div class="memory-card-text">${m.text}</div>
        </div>
      `).join('');

      const drawerBody = document.getElementById('drawerBody');
      drawerBody.innerHTML = `
        <div class="drawer-portrait-hero">
          <div class="drawer-portrait-box">${portraitHeroHtml}</div>
          <div style="flex:1;">
            <h2 style="font-size:19px; color:var(--gold-light); margin-bottom:4px;">${node.full_name}</h2>
            <div style="font-size:12.5px; color:var(--text-muted); margin-bottom:10px;">${node.role_label || ''}</div>
            <button id="drawerUploadPhotoBtn" class="btn-outline" style="width:100%;">
              📷 ${photoSrc ? 'Сменить фотографию' : 'Прикрепить фотографию / скан'}
            </button>
          </div>
        </div>

        <div class="field-row">
          <div class="field-label">Родовой клан и статус</div>
          <div class="field-val">${node.sub_clan || ''} • <strong>${node.status}</strong> (${node.confidence || 95}%)</div>
        </div>

        <div class="field-row">
          <div class="field-label">Даты жизни и эпоха</div>
          <div class="field-val">Рождение: ${node.birth_date || 'Уточняется'}${node.death_date ? ` | Уход: ${node.death_date}` : ''}<br/><span style="font-size:12px; color:var(--text-muted);">Эпоха: ${node.era || ''}</span></div>
        </div>

        <div class="field-row">
          <div class="field-label">Географическая привязка</div>
          <div class="field-val">📍 ${node.birth_place || 'Уточняется'}</div>
        </div>

        ${burialBlockHtml}

        <div class="field-row">
          <div class="field-label">Аналитика и архивные сведения</div>
          <div class="field-val" style="line-height:1.55;">${node.notes || 'Ведется сбор архивных источников.'}</div>
        </div>

        <div class="field-row">
          <div class="field-label">Источники и целевые фонды</div>
          <div class="field-val">
            <ul style="padding-left:18px; font-size:13px;">
              ${(node.sources || []).map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>
        </div>

        ${relButtons.length > 0 ? `
          <div class="field-row">
            <div class="field-label">Переход по связям на карте</div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              ${relButtons.join('')}
            </div>
          </div>
        ` : ''}

        <!-- Кворум подтверждения согласия рода -->
        <div class="quorum-box">
          <button type="button" id="quorumBtn" class="btn-quorum ${userHasConfirmed ? 'confirmed' : ''}">
            ${userHasConfirmed ? '✅ Вы подтвердили данные' : '✋ Подтверждаю, так и было'} (+${totalQuorum})
          </button>
          <span class="quorum-hint">Кворум согласия рода (${totalQuorum} подтв.)</span>
        </div>

        <!-- Раздел фамильных воспоминаний и свидетельств -->
        <div class="memories-section">
          <div class="field-label" style="display:flex; justify-content:space-between;">
            <span>Фамильные воспоминания и предания</span>
            <span style="color:#10b981; font-weight:700;">${memories.length} записей</span>
          </div>

          <div id="memoriesContainer" class="memories-list">
            ${memoriesHtml || '<div style="font-size:12px; color:var(--text-dim); padding:6px 0;">Воспоминаний пока нет. Будьте первыми, кто дополнит архив!</div>'}
          </div>

          <div class="add-memory-box">
            <div style="font-weight:700; font-size:12px; margin-bottom:8px; color:var(--gold-light);">
              Дополнить воспоминание / факт
            </div>
            <input
              type="text"
              id="newMemoryAuthor"
              class="gate-input"
              placeholder="Ваше имя и родство (Подпись) *"
              style="padding:8px 12px; font-size:12px; margin-bottom:8px;"
              required
            />
            <textarea
              id="newMemoryText"
              class="gate-input"
              placeholder="Напишите памятный факт, предание или уточнение..."
              style="min-height:60px; padding:8px 12px; font-size:12px; resize:vertical; margin-bottom:8px;"
              required
            ></textarea>
            <button type="button" id="submitMemoryBtn" class="btn-outline" style="width:100%; border-color:#10b981; color:#6ee7b7; font-weight:700;">
              + Добавить свидетельство в архив
            </button>
          </div>
        </div>
      `;

      // Event handlers inside drawer
      document.getElementById('drawerUploadPhotoBtn').addEventListener('click', (ev) => {
        triggerPhotoUpload(node.id, ev);
      });

      drawerBody.querySelectorAll('[data-jump]').forEach(btn => {
        btn.addEventListener('click', () => openDossier(parseInt(btn.getAttribute('data-jump'), 10)));
      });

      // Burial edit/add handlers
      const showAddBurialBtn = document.getElementById('showAddBurialBtn');
      const editBurialBtn = document.getElementById('editBurialBtn');
      const burialInlineForm = document.getElementById('burialInlineForm');
      const cancelBurialBtn = document.getElementById('cancelBurialBtn');
      const saveBurialBtn = document.getElementById('saveBurialBtn');
      const burialInputVal = document.getElementById('burialInputVal');

      if (showAddBurialBtn) {
        showAddBurialBtn.addEventListener('click', () => {
          showAddBurialBtn.style.display = 'none';
          burialInlineForm.style.display = 'block';
          burialInputVal.focus();
        });
      }
      if (editBurialBtn) {
        editBurialBtn.addEventListener('click', () => {
          burialInlineForm.style.display = 'block';
          burialInputVal.focus();
        });
      }
      if (cancelBurialBtn) {
        cancelBurialBtn.addEventListener('click', () => {
          burialInlineForm.style.display = 'none';
          if (showAddBurialBtn) showAddBurialBtn.style.display = '';
        });
      }
      if (saveBurialBtn) {
        saveBurialBtn.addEventListener('click', () => {
          const val = (burialInputVal.value || '').trim();
          if (val) {
            burialMap[node.id] = val;
            saveBurialMap();
            openDossier(node.ahnentafel);
          }
        });
      }

      // Quorum handler
      document.getElementById('quorumBtn').addEventListener('click', () => {
        if (!quorumMap[node.id + '_user']) {
          quorumMap[node.id] = (quorumMap[node.id] || 0) + 1;
          quorumMap[node.id + '_user'] = true;
          saveQuorumMap();
          openDossier(node.ahnentafel);
        }
      });

      // Add memory handler
      document.getElementById('submitMemoryBtn').addEventListener('click', () => {
        const authorInput = document.getElementById('newMemoryAuthor');
        const textInput = document.getElementById('newMemoryText');
        const author = (authorInput.value || '').trim();
        const text = (textInput.value || '').trim();
        if (!author) {
          alert('Пожалуйста, укажите Ваше имя и родство (Подпись)');
          authorInput.focus();
          return;
        }
        if (!text) {
          alert('Пожалуйста, напишите воспоминание или факт');
          textInput.focus();
          return;
        }
        if (!memoriesMap[node.id]) memoriesMap[node.id] = [];
        memoriesMap[node.id].push({
          author,
          text,
          timestamp: new Date().toLocaleDateString('ru-RU')
        });
        saveMemoriesMap();
        openDossier(node.ahnentafel);
      });

      document.getElementById('drawerBackdrop').classList.add('open');
      document.getElementById('dossierDrawer').classList.add('open');
    }

    // ================= 6. FLOATING HYPOTHESIS DOSSIER =================
    function openHypothesisDossier(hypId) {
      if (!lineageData || !lineageData.floating_hypotheses) return;
      const hyp = lineageData.floating_hypotheses.find(h => h.id === hypId);
      if (!hyp) return;

      document.getElementById('drawerAhnentafel').textContent = `🪐 ОРБИТАЛЬНАЯ ГИПОТЕЗА • ${hyp.id}`;

      // Quorum for hypothesis
      const baseQuorum = 1;
      const userVotes = quorumMap[hyp.id] || 0;
      const totalQuorum = baseQuorum + userVotes;
      const userHasConfirmed = Boolean(quorumMap[hyp.id + '_user']);

      // Memories for hypothesis
      const memories = memoriesMap[hyp.id] || [];
      const memoriesHtml = memories.map(m => `
        <div class="memory-card">
          <div class="memory-card-header">
            <span>✍️ ${m.author}</span>
            <span class="memory-card-date">${m.timestamp}</span>
          </div>
          <div class="memory-card-text">${m.text}</div>
        </div>
      `).join('');

      const relAncestorBtn = hyp.probable_relative_ahnentafel
        ? `<button class="btn-outline" id="jumpToProbableAncestorBtn" style="border-color:#f59e0b; color:#fbbf24; font-weight:700;">
             🔗 Перейти к вероятному родственнику в древе (Слот #${hyp.probable_relative_ahnentafel})
           </button>`
        : '';

      const citationsHtml = (hyp.citation_links || []).map(link => `
        <li><a href="${link}" target="_blank" rel="noopener noreferrer" style="color:#6ee7b7; text-decoration:none;">${link} ↗</a></li>
      `).join('');

      const drawerBody = document.getElementById('drawerBody');
      drawerBody.innerHTML = `
        <div class="drawer-portrait-hero" style="border-color:rgba(245,158,11,0.5); background:linear-gradient(145deg, rgba(38,28,12,0.96) 0%, rgba(14,18,27,0.98) 100%);">
          <div class="drawer-portrait-box" style="border-color:#f59e0b; color:#f59e0b; font-size:28px;">🪐</div>
          <div style="flex:1;">
            <div class="badge-floating-hyp" style="margin-bottom:6px;">ГИПОТЕЗА / КАНДИДАТ В РОД • ${hyp.confidence}%</div>
            <h2 style="font-size:18px; color:#fef3c7; margin-bottom:4px;">${hyp.full_name}</h2>
            <div style="font-size:12px; color:var(--text-muted);">${hyp.role_badge}</div>
          </div>
        </div>

        <div class="field-row">
          <div class="field-label">Родовой кластер и поколение</div>
          <div class="field-val" style="color:#fbbf24; font-weight:700;">
            ${(hyp.clan || '').toUpperCase()} • ${hyp.generation_label}
          </div>
        </div>

        <div class="field-row">
          <div class="field-label">Эпоха и временной диапазон</div>
          <div class="field-val">
            ${hyp.era} (Рождение: ${hyp.birth_date || '—'} / Уход: ${hyp.death_date || '—'})
          </div>
        </div>

        <div class="field-row">
          <div class="field-label">Историческая география</div>
          <div class="field-val">📍 ${hyp.village}</div>
        </div>

        <div class="field-row">
          <div class="field-label">Обоснование архивной гипотезы</div>
          <div class="field-val" style="line-height:1.55;">${hyp.relationship_hypothesis}</div>
        </div>

        ${relAncestorBtn ? `
          <div class="field-row">
            <div class="field-label">Точка привязки к древу</div>
            <div>${relAncestorBtn}</div>
          </div>
        ` : ''}

        <div class="field-row">
          <div class="field-label">Архивные фонды и метрики</div>
          <div class="field-val">
            <ul style="padding-left:18px; font-size:13px;">
              ${(hyp.sources || []).map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>
        </div>

        ${citationsHtml ? `
          <div class="field-row">
            <div class="field-label">Прямые ссылки на первоисточники</div>
            <div class="field-val">
              <ul style="padding-left:18px; font-size:12.5px;">
                ${citationsHtml}
              </ul>
            </div>
          </div>
        ` : ''}

        <!-- Quorum for hypothesis -->
        <div class="quorum-box">
          <button type="button" id="hypQuorumBtn" class="btn-quorum ${userHasConfirmed ? 'confirmed' : ''}">
            ${userHasConfirmed ? '✅ Вы подтвердили гипотезу' : '✋ Подтверждаю, семейное предание помнит'} (+${totalQuorum})
          </button>
          <span class="quorum-hint">Кворум подтверждения родственниками</span>
        </div>

        <!-- Memories / additions for hypothesis -->
        <div class="memories-section">
          <div class="field-label" style="display:flex; justify-content:space-between;">
            <span>Свидетельства и предания по гипотезе</span>
            <span style="color:#fbbf24; font-weight:700;">${memories.length} записей</span>
          </div>

          <div id="hypMemoriesContainer" class="memories-list">
            ${memoriesHtml || '<div style="font-size:12px; color:var(--text-dim); padding:6px 0;">Добавьте воспоминание или документ по этой гипотезе!</div>'}
          </div>

          <div class="add-memory-box" style="border-color:rgba(245,158,11,0.4);">
            <div style="font-weight:700; font-size:12px; margin-bottom:8px; color:#fbbf24;">
              Дополнить свидетельство к гипотезе
            </div>
            <input
              type="text"
              id="newHypMemoryAuthor"
              class="gate-input"
              placeholder="Ваше имя и родство (Подпись) *"
              style="padding:8px 12px; font-size:12px; margin-bottom:8px;"
              required
            />
            <textarea
              id="newHypMemoryText"
              class="gate-input"
              placeholder="Известные вам факты, документы, рассказы старших родственников..."
              style="min-height:60px; padding:8px 12px; font-size:12px; resize:vertical; margin-bottom:8px;"
              required
            ></textarea>
            <button type="button" id="submitHypMemoryBtn" class="btn-outline" style="width:100%; border-color:#f59e0b; color:#fbbf24; font-weight:700;">
              + Сохранить свидетельство по гипотезе
            </button>
          </div>
        </div>
      `;

      if (hyp.probable_relative_ahnentafel) {
        const jumpBtn = document.getElementById('jumpToProbableAncestorBtn');
        if (jumpBtn) {
          jumpBtn.addEventListener('click', () => openDossier(hyp.probable_relative_ahnentafel));
        }
      }

      document.getElementById('hypQuorumBtn').addEventListener('click', () => {
        if (!quorumMap[hyp.id + '_user']) {
          quorumMap[hyp.id] = (quorumMap[hyp.id] || 0) + 1;
          quorumMap[hyp.id + '_user'] = true;
          saveQuorumMap();
          openHypothesisDossier(hyp.id);
        }
      });

      document.getElementById('submitHypMemoryBtn').addEventListener('click', () => {
        const authorInput = document.getElementById('newHypMemoryAuthor');
        const textInput = document.getElementById('newHypMemoryText');
        const author = (authorInput.value || '').trim();
        const text = (textInput.value || '').trim();
        if (!author) {
          alert('Пожалуйста, укажите Ваше имя и родство (Подпись)');
          authorInput.focus();
          return;
        }
        if (!text) {
          alert('Пожалуйста, напишите свидетельство');
          textInput.focus();
          return;
        }
        if (!memoriesMap[hyp.id]) memoriesMap[hyp.id] = [];
        memoriesMap[hyp.id].push({
          author,
          text,
          timestamp: new Date().toLocaleDateString('ru-RU')
        });
        saveMemoriesMap();
        openHypothesisDossier(hyp.id);
      });

      document.getElementById('drawerBackdrop').classList.add('open');
      document.getElementById('dossierDrawer').classList.add('open');
    }

    function closeDossier() {
      document.getElementById('drawerBackdrop').classList.remove('open');
      document.getElementById('dossierDrawer').classList.remove('open');
    }

    // ================= 7. STEP-BY-STEP MODAL WIZARD: JOIN FAMILY BRANCH =================
    function initBranchWizard() {
      const modal = document.getElementById('branchWizardModal');
      const openBtn = document.getElementById('openBranchWizardBtn');
      const closeBtn = document.getElementById('closeBranchWizardBtn');
      const targetSelect = document.getElementById('wizardTargetPerson');
      const form = document.getElementById('branchWizardForm');
      const successBox = document.getElementById('wizSuccessBox');
      const closeSuccessBtn = document.getElementById('closeWizSuccessBtn');

      function populateTargetPersons() {
        if (!lineageData) return;
        const all = [...lineageData.nodes, ...(lineageData.collateral_nodes || [])];
        targetSelect.innerHTML = all.map(n => `
          <option value="${n.ahnentafel || n.id}">
            ${n.ahnentafel ? `#${n.ahnentafel}` : 'Боковая ветвь'} ${n.full_name} (${n.role_label || n.sub_clan || ''})
          </option>
        `).join('');
      }

      function showStep(stepNum) {
        for (let i = 1; i <= 4; i++) {
          const pill = document.getElementById(`wizPill${i}`);
          const pane = document.getElementById(`wizPane${i}`);
          if (pill) {
            pill.className = i === stepNum ? 'step-pill active' : (i < stepNum ? 'step-pill completed' : 'step-pill');
          }
          if (pane) {
            pane.className = i === stepNum ? 'wizard-step-pane active' : 'wizard-step-pane';
          }
        }
        if (stepNum === 4) {
          updateSummary();
        }
      }

      function updateSummary() {
        const targetOption = targetSelect.options[targetSelect.selectedIndex];
        const targetText = targetOption ? targetOption.text : 'Выбранный предок';
        const rel = document.querySelector('input[name="wiz_relation"]:checked')?.value || 'Сын / Дочь';
        const fullName = (document.getElementById('wizFullName').value || '').trim() || 'Новый родственник';
        const bDate = (document.getElementById('wizBirthDate').value || '').trim();
        const bPlace = (document.getElementById('wizBirthPlace').value || '').trim();

        document.getElementById('wizSummaryPreview').innerHTML = `
          <strong style="color:#6ee7b7;">Сводка присоединяемой ветви:</strong><br/>
          К кому: ${targetText}<br/>
          Отношение: <strong>${rel}</strong><br/>
          ФИО персоны: <strong>${fullName}</strong> ${bDate ? `(${bDate} г.р.)` : ''}<br/>
          Место: ${bPlace || 'Не указано'}
        `;
      }

      openBtn.addEventListener('click', () => {
        populateTargetPersons();
        showStep(1);
        form.reset();
        form.style.display = 'block';
        successBox.style.display = 'none';
        modal.classList.add('open');
      });

      closeBtn.addEventListener('click', () => modal.classList.remove('open'));
      closeSuccessBtn.addEventListener('click', () => modal.classList.remove('open'));

      document.getElementById('toWizStep2').addEventListener('click', () => showStep(2));
      document.getElementById('backToWizStep1').addEventListener('click', () => showStep(1));

      document.getElementById('toWizStep3').addEventListener('click', () => showStep(3));
      document.getElementById('backToWizStep2').addEventListener('click', () => showStep(2));

      document.getElementById('toWizStep4').addEventListener('click', () => {
        const fn = (document.getElementById('wizFullName').value || '').trim();
        if (!fn) {
          alert('Пожалуйста, введите ФИО новой персоны');
          document.getElementById('wizFullName').focus();
          return;
        }
        showStep(4);
      });
      document.getElementById('backToWizStep3').addEventListener('click', () => showStep(3));

      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const author = (document.getElementById('wizAuthorName').value || '').trim();
        const contact = (document.getElementById('wizAuthorContact').value || '').trim();
        const fullName = (document.getElementById('wizFullName').value || '').trim();
        const bDate = (document.getElementById('wizBirthDate').value || '').trim();
        const dDate = (document.getElementById('wizDeathDate').value || '').trim();
        const bPlace = (document.getElementById('wizBirthPlace').value || '').trim();
        const bio = (document.getElementById('wizBio').value || '').trim();
        const rel = document.querySelector('input[name="wiz_relation"]:checked')?.value || 'Сын / Дочь';
        const targetVal = targetSelect.value;

        if (!author || !contact || !fullName) {
          alert('Пожалуйста, заполните все обязательные поля');
          return;
        }

        const newId = `REL-BRANCH-${Date.now()}`;
        const newBranchNode = {
          id: newId,
          ahnentafel: 900 + Math.floor(Math.random() * 99),
          full_name: fullName,
          role_label: `${rel} (ветвь от #${targetVal})`,
          sub_clan: 'Каретниковы',
          branch: 'paternal',
          generation: 2,
          generation_label: 'Семейная ветвь',
          birth_date: bDate,
          death_date: dDate,
          birth_place: bPlace,
          notes: `${bio ? bio + ' • ' : ''}Внесено родственником: ${author} (контакт: ${contact}). Отношение: ${rel} к слоту #${targetVal}.`,
          status: 'FAMILY_ORAL',
          confidence: 85,
          is_collateral: true,
          is_relative_proposal: true,
          sibling_of_ahnentafel: parseInt(targetVal, 10) || 1,
          sources: [`Свидетельство родственника: ${author}`]
        };

        // Append to collateral_nodes
        if (!lineageData.collateral_nodes) lineageData.collateral_nodes = [];
        lineageData.collateral_nodes.push(newBranchNode);

        // Save to pending branches in localStorage
        try {
          const pb = JSON.parse(localStorage.getItem(PENDING_BRANCHES_KEY) || '[]');
          pb.push(newBranchNode);
          localStorage.setItem(PENDING_BRANCHES_KEY, JSON.stringify(pb));
        } catch {}

        renderRoadmapCanvas(lineageData);

        form.style.display = 'none';
        successBox.style.display = 'block';
      });
    }

    function generateGedcomClientString(data) {
      const lines = [
        '0 HEAD',
        '1 SOUR KARETNIKOV_HERITAGE_ARCHIVE',
        '2 VERS 2.0',
        '1 GEDC',
        '2 VERS 5.5.1',
        '2 FORM LINEAGE-LINKED',
        '1 CHAR UTF-8'
      ];
      for (const n of (data.nodes || [])) {
        const id = `@I${String(n.ahnentafel).padStart(3, '0')}@`;
        const given = `${n.first_name || ''} ${n.patronymic || ''}`.trim();
        lines.push(`0 ${id} INDI`);
        lines.push(`1 NAME ${given} /${n.surname || ''}/`);
        lines.push(`1 SEX ${n.gender || 'M'}`);
        lines.push('1 BIRT');
        if (n.birth_date) lines.push(`2 DATE ${n.birth_date}`);
        if (n.birth_place) lines.push(`2 PLAC ${n.birth_place}`);
        if (n.death_date) {
          lines.push('1 DEAT');
          lines.push(`2 DATE ${n.death_date}`);
        }
        if (n.generation < 7) lines.push(`1 FAMC @F${String(n.ahnentafel).padStart(3, '0')}@`);
        if (n.ahnentafel > 1) lines.push(`1 FAMS @F${String(Math.floor(n.ahnentafel / 2)).padStart(3, '0')}@`);
      }
      for (let c = 1; c <= 63; c++) {
        lines.push(`0 @F${String(c).padStart(3, '0')}@ FAM`);
        lines.push(`1 HUSB @I${String(2 * c).padStart(3, '0')}@`);
        lines.push(`1 WIFE @I${String(2 * c + 1).padStart(3, '0')}@`);
        lines.push(`1 CHIL @I${String(c).padStart(3, '0')}@`);
      }
      lines.push('0 TRLR');
      return lines.join('\\n');
    }

    function downloadBlob(filename, content, mime) {
      const blob = new Blob([content], { type: mime });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    }

    // ================= 8. AUTH & UI EVENTS =================
    document.getElementById('togglePwBtn').addEventListener('click', () => {
      const inp = document.getElementById('passwordInput');
      inp.type = inp.type === 'password' ? 'text' : 'password';
    });

    document.getElementById('authForm').addEventListener('submit', async (e) => {
      e.preventDefault();
      const pwInput = document.getElementById('passwordInput');
      const btn = document.getElementById('unlockBtn');
      const statusEl = document.getElementById('authStatus');
      const pw = pwInput.value;

      btn.disabled = true;
      statusEl.className = 'gate-status';
      statusEl.textContent = 'Вычисление PBKDF2-HMAC-SHA256 (100 000 итераций) и проверка ключа...';

      try {
        lineageData = await unlockVaultWithPassword(pw);
        applyRolePermissions();

        // Inject saved pending branches from localStorage if any
        try {
          const pb = JSON.parse(localStorage.getItem(PENDING_BRANCHES_KEY) || '[]');
          if (pb.length > 0) {
            if (!lineageData.collateral_nodes) lineageData.collateral_nodes = [];
            pb.forEach(p => {
              if (!lineageData.collateral_nodes.some(x => x.id === p.id)) {
                lineageData.collateral_nodes.push(p);
              }
            });
          }
        } catch {}

        statusEl.className = 'gate-status success';
        statusEl.textContent = currentRole === 'owner'
          ? 'Ключ владельца подтвержден! Режим: Администратор архива.'
          : 'Ключ родственников подтвержден! Режим: Гостевой режим родственников (Append-Only).';
        pwInput.value = '';

        renderRoadmapCanvas(lineageData);
        renderFanChart(lineageData);
        renderArchiveRadar(lineageData);
        renderAccessGuide(lineageData);
        initBranchWizard();

        setTimeout(() => {
          document.getElementById('fortressGate').classList.add('unlocked');
          document.getElementById('workspace').classList.add('active');
          focusOnProband();
        }, 180);
      } catch (err) {
        failedAttempts += 1;
        const delaySec = Math.min(failedAttempts * 2, 10);
        statusEl.className = 'gate-status error';
        statusEl.textContent = `Ошибка расшифровки AES-256-GCM: неверный ключ доступа (задержка ${delaySec} сек.)`;
        setTimeout(() => { btn.disabled = false; }, delaySec * 1000);
        return;
      }
      btn.disabled = false;
    });

    document.querySelectorAll('.nav-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
        tab.classList.add('active');
        const target = tab.getAttribute('data-view');
        document.getElementById(`view-${target}`).classList.add('active');
      });
    });

    // Epistemic Mode Toggle Buttons
    document.getElementById('modeFactsBtn').addEventListener('click', () => {
      setEpistemicMode('facts_only');
    });
    document.getElementById('modeAllBtn').addEventListener('click', () => {
      setEpistemicMode('all_levels');
    });

    // Keyboard Shortcuts: 'F' for facts_only, 'A' for all_levels
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'f' || e.key === 'F' || e.key === 'а' || e.key === 'А') {
        setEpistemicMode('facts_only');
      } else if (e.key === 'a' || e.key === 'A' || e.key === 'ф' || e.key === 'Ф') {
        setEpistemicMode('all_levels');
      }
    });

    document.querySelectorAll('.hud-panel .chip-btn[data-filter]').forEach(chip => {
      chip.addEventListener('click', () => {
        document.querySelectorAll('.hud-panel .chip-btn[data-filter]').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        activeFilter = chip.getAttribute('data-filter');
        if (lineageData) {
          renderRoadmapCanvas(lineageData);
          if (activeFilter === 'all7') fitEntireRoadmap();
          else if (activeFilter === 'hypotheses') {
            // Focus on hypotheses area (Col 3-4, lower half)
            zoom = 0.55;
            panX = -200;
            panY = -1200;
            applyRoadmapTransform();
          } else {
            focusOnProband();
          }
        }
      });
    });

    document.getElementById('searchNodesInput').addEventListener('input', (e) => {
      searchQuery = e.target.value || '';
      if (lineageData) renderRoadmapCanvas(lineageData);
    });

    document.getElementById('closeDrawerBtn').addEventListener('click', closeDossier);
    document.getElementById('drawerBackdrop').addEventListener('click', closeDossier);
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeDossier();
    });

    document.getElementById('exportGedBtn').addEventListener('click', () => {
      if (!lineageData) return;
      downloadBlob('karetnikov_lineage_7gen.ged', generateGedcomClientString(lineageData), 'text/plain;charset=utf-8');
    });

    document.getElementById('exportJsonBtn').addEventListener('click', () => {
      if (!lineageData) return;
      const exportCopy = JSON.parse(JSON.stringify(lineageData));
      exportCopy.attached_photos = photoMap;
      exportCopy.ancestor_burials = burialMap;
      exportCopy.family_memories = memoriesMap;
      exportCopy.quorum_confirmations = quorumMap;
      try {
        exportCopy.pending_branches = JSON.parse(localStorage.getItem(PENDING_BRANCHES_KEY) || '[]');
      } catch {}
      downloadBlob('karetnikov_lineage_with_photos.json', JSON.stringify(exportCopy, null, 2), 'application/json');
    });

    document.getElementById('lockVaultBtn').addEventListener('click', () => {
      lineageData = null;
      document.getElementById('roadmapNodesLayer').innerHTML = '';
      document.getElementById('roadmapSvgEdges').innerHTML = '';
      document.getElementById('workspace').classList.remove('active');
      document.getElementById('fortressGate').classList.remove('unlocked');
    });
  </script>
</body>
</html>
"""

with open(r"C:\Karetnikov_Lineage\src\pages\index.astro", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated src/pages/index.astro successfully!")
