#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

GRAPH_PATH = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))

nodes = data["nodes"]
by_status = {}
for n in nodes:
    st = n.get("status")
    by_status.setdefault(st, []).append(n["ahnentafel"])

for st, ahn_list in by_status.items():
    print(f"Status '{st}': count {len(ahn_list)} -> {ahn_list}")
