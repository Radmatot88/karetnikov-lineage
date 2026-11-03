#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

GRAPH_PATH = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))

print("=== SAMPLE COLLATERAL NODE ===")
if data.get("collateral_nodes"):
    print(json.dumps(data["collateral_nodes"][0], ensure_ascii=False, indent=2))
    print("\n=== COLLATERAL C007 and C008 ===")
    for c in data["collateral_nodes"]:
        if c.get("id") in ["C007", "C008", "C009"]:
            print(json.dumps(c, ensure_ascii=False, indent=2))

print("\n=== SAMPLE FLOATING HYPOTHESIS ===")
if data.get("floating_hypotheses"):
    print(json.dumps(data["floating_hypotheses"][0], ensure_ascii=False, indent=2))
