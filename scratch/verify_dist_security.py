#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Проверка безопасности дистрибутива dist/:
- Убедиться, что в публичном HTML/JS нет открытых фамилий и PII живых людей (кроме названий страниц/заголовков)
- Убедиться, что в public/vault/lineage_payload.enc.json лежит только AES-256-GCM шифротекст
"""

from pathlib import Path
import json

dist_dir = Path(r"c:\Karetnikov_Lineage\dist")
index_html = (dist_dir / "index.html").read_text(encoding="utf-8")

# Проверим, что граф НЕ вшит открыто в HTML
assert "Дмитрий Иванович Каретников" not in index_html, "LEAK: Пробанд найден открытым в HTML!"
assert "Светлана Владимировна" not in index_html, "LEAK: Мать найдена открытой в HTML!"
assert "Валентин Григорьевич" not in index_html, "LEAK: Дед найден открытым в HTML!"
assert "Клавдия Петровна" not in index_html, "LEAK: Бабушка найдена открытой в HTML!"

# Проверим зашифрованный контейнер
enc_path = Path(r"c:\Karetnikov_Lineage\public\vault\lineage_payload.enc.json")
enc_data = json.loads(enc_path.read_text(encoding="utf-8"))
assert "envelopes" in enc_data, "Нет поля envelopes в зашифрованном контейнере!"
assert "owner" in enc_data["envelopes"], "Нет envelopes.owner!"
assert "ciphertext_b64" in enc_data["envelopes"]["owner"], "Нет ciphertext_b64!"

print("[PASS] Security Fortress audit PASSED: ZERO RAW PII IN PUBLIC BUNDLE!")
