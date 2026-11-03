#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

GRAPH_PATH = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))

target_ahnen = [8, 9, 10, 12, 14, 16, 17, 18, 28, 32, 33, 64, 65]
nodes = {n["ahnentafel"]: n for n in data["nodes"]}

for a in target_ahnen:
    if a in nodes:
        n = nodes[a]
        print(f"=== AHNEN #{a} ===")
        print(f"Name: {n.get('full_name')}")
        print(f"Status: {n.get('status')}")
        print(f"Epistemic Level: {n.get('epistemic_level')}")
        print(f"Confidence: {n.get('confidence_score')}")
        print(f"Sources: {n.get('sources')}")
        print(f"Notes: {n.get('notes')}")
        print(f"Fact Cert: {n.get('fact_certificate')}")
        print()

print("=== COLLATERAL NODES COUNT ===")
collat = data.get("collateral_nodes", [])
print(f"Count: {len(collat)}")
for c in collat:
    print(f"- ID: {c.get('id')} | Name: {c.get('full_name')} | Status: {c.get('status')} | Rel: {c.get('relation_to_proband')}")

print("\n=== TOP LEVEL KEYS ===")
print(list(data.keys()))
