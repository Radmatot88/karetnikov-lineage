/**
 * HERALDIC_ICONS — Полный каталог 100% SVG-иконок для Родового Архива Графа Каретникова
 * Стандарт: TABOO_02 (ZERO EMOJI IN UI), WCAG AAA 15.2:1
 */

export const HERALDIC_ICONS: Record<string, string> = {
  // --- ЧЕТЫРЕ СУРГУЧНЫЕ ПЕЧАТИ СТАТУСОВ ДОСТОВЕРНОСТИ ---
  'seal-confirmed': `<svg class="svg-icon seal-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2l2.4 2.2 3.2-.5 1.3 3 2.9 1.5-.7 3.2 2.2 2.4-2.2 2.4.7 3.2-2.9 1.5-1.3 3-3.2-.5L12 22l-2.4-2.2-3.2.5-1.3-3-2.9-1.5.7-3.2L0.7 12l2.2-2.4-.7-3.2 2.9-1.5 1.3-3 3.2.5L12 2z"/><path d="M8.5 12.3l2.4 2.4 4.8-5"/></svg>`,
  'seal-oral': `<svg class="svg-icon seal-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 8.5c0-1.1.9-2 2-2h4.5c1.1 0 2 .9 2 2v7c0 1.1-.9 2-2 2H10c-1.1 0-2-.9-2-2v-7z"/><path d="M8 15.5c-1.1 0-2-.9-2-2s.9-2 2-2"/><path d="M11 10h4M11 13h2.5"/></svg>`,
  'seal-candidate': `<svg class="svg-icon seal-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9.2" stroke-dasharray="2.5 1.5"/><circle cx="11" cy="11" r="3.8"/><path d="M14 14l3.5 3.5"/></svg>`,
  'seal-unknown': `<svg class="svg-icon seal-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3L4.5 6.5v6c0 5 3.5 9 7.5 10.5 4-1.5 7.5-5.5 7.5-10.5v-6L12 3z"/><path d="M10.2 9.5a2 2 0 1 1 3.2 1.8c-.8.6-1.4 1.1-1.4 2.2"/><circle cx="12" cy="16.5" r="0.7" fill="currentColor"/></svg>`,

  // --- ЧЕТЫРЕ ГЕРБОВЫХ ЗНАКА ФАМИЛЬНЫХ КЛАНОВ ---
  'clan-karetnikov-wheel': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.8"/><path d="M12 3v6.2M12 14.8V21M3 12h6.2M14.8 12H21"/><path d="M5.6 5.6l4.4 4.4M14 14l4.4 4.4M18.4 5.6l-4.4 4.4M10 14l-4.4 4.4"/></svg>`,
  'clan-kumanin-wing': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 18c2-6 7-12 16-14-1 4-2 8-5 11-2.5 2.5-6 4-11 3z"/><path d="M6 16c3-4 6-7 11-9M7.5 17.5c2.5-3 5-5 8.5-6.5"/><path d="M19 14.5l.8 1.8 1.9.3-1.4 1.3.4 1.9-1.7-.9-1.7.9.4-1.9-1.4-1.3 1.9-.3z"/></svg>`,
  'clan-zubkov-sabre': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20l11-11M15 9c2-2 4-2.5 5.5-2.5s.5 2-.5 3.5-3 3-5 5"/><path d="M3 21l2-2M2 19l3 3M6 18l-2 2"/><path d="M18 5l2-2 1.5 1.5-2 2"/><path d="M20 20L11 11M9 13c-2 2-3.5 2.5-5 2.5.5-2 1.5-3.5 3.5-5"/><path d="M21 21l-2-2M22 19l-3 3M18 18l2 2"/></svg>`,
  'clan-yukhin-wheat': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v13M12 3c-1.5 1.5-2 3-1.5 4.5 1.5 0 2.5-.5 3.5-2-.5-1.2-1-2-2-2.5z"/><path d="M12 7.5c-1.8 1.2-2.3 2.8-1.8 4.2 1.6 0 2.7-.5 3.8-2.2-.6-1-1-1.5-2-2z"/><path d="M12 12c-2 1-2.5 2.5-2 4 1.8 0 3-.5 4-2-.6-1-1-1.5-2-2z"/><path d="M3 18.5c2.5-1 4.5-1 7 0s4.5 1 7 0 4.5-1 5 0"/><path d="M3 21.5c2.5-1 4.5-1 7 0s4.5 1 7 0 4.5-1 5 0"/></svg>`,

  // --- ИНТЕРФЕЙСНЫЕ И НАВИГАЦИОННЫЕ ИКОНКИ ---
  'nav-scroll': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 4h11a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a3 3 0 0 1 3-3z"/><path d="M4 7h13a2 2 0 0 1 2 2"/><path d="M8 11h7M8 14h5"/></svg>`,
  'nav-tree': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 7v5M8 12h8M8 12v4M16 12v4"/><circle cx="12" cy="7" r="1.5" fill="currentColor"/><circle cx="8" cy="16" r="1.5" fill="currentColor"/><circle cx="16" cy="16" r="1.5" fill="currentColor"/></svg>`,
  'nav-fan': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21a9 9 0 0 1-9-9 9 9 0 0 1 9-9 9 9 0 0 1 9 9"/><path d="M12 21l-6-6a5.5 5.5 0 0 1 6-7.8 5.5 5.5 0 0 1 6 7.8z"/><path d="M12 21V12M12 12L7.5 7.5M12 12l4.5-4.5M12 12H3M12 12h9"/></svg>`,
  'heraldry-temple': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9.5L12 4l9 5.5"/><path d="M4 10h16M2 20h20M5 10v10M9 10v10M15 10v10M19 10v10"/></svg>`,
  'nav-archive': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/><path d="M12 12l4-4-1.5 5.5L9 15z"/></svg>`,

  // --- ДЕЙСТВИЯ ---
  'action-branch-add': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20c4-1 8-5 9-10 1.2-5.5 5-7 7-7-1 3-1 6-4 8-3 2-6 3-7 7"/><path d="M10 13c-2.5 0-4.5 1.5-5 3.5 1.5.5 3.5 0 5-1.5z"/><path d="M17 17v4M15 19h4"/></svg>`,
  'action-download': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v13M7 11l5 5 5-5"/><path d="M4 17v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg>`,
  'action-lock': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V6.5a4 4 0 0 1 8 0V10"/><circle cx="12" cy="15" r="1.3" fill="currentColor"/><path d="M12 16.3v2"/></svg>`,
  'action-focus': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></svg>`,
  'action-search': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M16.5 16.5L21 21"/></svg>`,
  'action-photo': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h4l2-3h4l2 3h4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2z"/><circle cx="12" cy="14" r="4"/></svg>`,
  'action-close': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>`,
  'action-eye': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>`,
  'action-settings': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`,

  // --- МЕТАДАННЫЕ ---
  'meta-calendar': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M16 2v4M8 2v4M3 9h18"/><path d="M8 13h2M14 13h2M8 17h2M14 17h2"/></svg>`,
  'meta-pin': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>`,
  'meta-burial-cross': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v17M8 7h8M9 14h6"/><path d="M5 20h14"/></svg>`,
  'meta-quill': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 3C16 4 12 7 10 11c-1.5 3-2 6-4 8l3-1c3-1.5 6-3 8-5 3-3 4-8 2-10z"/><path d="M6 19l-3 2 1-3"/><path d="M13 8l3 3"/></svg>`,
  'meta-scroll': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>`,
  'meta-kinship': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6c4 0 6 6 10 6s6 6 6 6M20 6c-4 0-6 6-10 6S4 18 4 18"/><path d="M7 6v12M12 9v6M17 6v12"/></svg>`,
  'meta-link': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>`,
  'meta-book': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="14" y2="11"/></svg>`,

  // --- РОДСТВО И ВИЗАРД ---
  'rel-child': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="7" r="4"/><path d="M6 21v-2a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v2"/></svg>`,
  'rel-spouse': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="12" r="5"/><circle cx="15" cy="12" r="5"/></svg>`,
  'rel-parent': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>`,
  'rel-descendant': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>`,
  'rel-sibling': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M8 7l-5 5 5 5M16 7l5 5-5 5"/></svg>`,

  // --- ОРБИТАЛЬНЫЕ ГИПОТЕЗЫ ---
  'icon-orbit-hypothesis': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="5"/><ellipse cx="12" cy="12" rx="10" ry="3.8" transform="rotate(-25 12 12)"/><circle cx="18" cy="9" r="1" fill="currentColor"/></svg>`,

  // --- СЕМЕЙНЫЙ КВОРИУМ ---
  'vote-confirmed': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>`,
  'vote-pledge': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 11V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v0M14 10V4a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v2M10 10.5V6a2 2 0 0 0-2-2v0a2 2 0 0 0-2 2v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15"/></svg>`,

  // --- ГЕРБОВНИК И ДОПОЛНИТЕЛЬНЫЕ ЗНАКИ ---
  'shield-fortress': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2L4 5v6.09c0 5.05 3.41 9.76 8 10.91 4.59-1.15 8-5.86 8-10.91V5l-8-3z"/></svg>`,
  'clan-kumanin-bee': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 4v4M12 16v4M4 12h4M16 12h4"/><path d="M7 7l3 3M14 14l3 3M17 7l-3 3M10 14l-3 3"/></svg>`,
  'clan-eagle': `<svg class="svg-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l3 4 5 1-4 4 1 5-5-2-5 2 1-5-4-4 5-1z"/></svg>`,
};

/**
 * Вспомогательная функция для генерации HTML SVG-иконки
 */
export function renderIcon(name: string, extraClass: string = ''): string {
  const svg = HERALDIC_ICONS[name] || '';
  if (!svg) return '';
  if (!extraClass) return svg;
  return svg.replace('class="svg-icon', `class="svg-icon ${extraClass}`);
}
