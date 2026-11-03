#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

GRAPH_PATH = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
nodes = {n["ahnentafel"]: n for n in data["nodes"]}

for a in [14, 16, 17, 18, 28]:
    n = nodes[a]
    print(f"=== AHNEN #{a} ===")
    print(f"Name: {n.get('full_name')}")
    print(f"Status: {n.get('status')}")
    print(f"Epistemic Level: {n.get('epistemic_level')}")
    print(f"Confidence: {n.get('confidence_score')}")
    print(f"Sources: {n.get('sources')}")
    print(f"Notes: {n.get('notes')}")
    print(f"Fact Cert: {n.get('fact_certificate')}")
