#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

GRAPH_PATH = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))

print(f"Total floating hypotheses: {len(data.get('floating_hypotheses', []))}")
for fh in data.get("floating_hypotheses", []):
    print(f"- {fh.get('id')}: {fh.get('full_name')} ({fh.get('clan')}) [Score: {fh.get('confidence')}]")
