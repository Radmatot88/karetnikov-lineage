#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

graph_file = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(graph_file.read_text(encoding="utf-8"))

for c in data["collateral_nodes"]:
    print(f"#{c['ahnentafel']}: {c['full_name']} | fact: {c.get('is_fact_confirmed')} | lvl: {c.get('epistemic_level')}")
