#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path

graph_file = Path(r"c:\Karetnikov_Lineage\data\vault\lineage_graph.json")
data = json.loads(graph_file.read_text(encoding="utf-8"))

direct_facts = [n for n in data["nodes"] if n.get("is_fact_confirmed")]
collateral_facts = [n for n in data["collateral_nodes"] if n.get("is_fact_confirmed")]

print(f"Direct facts ({len(direct_facts)}):")
for f in direct_facts:
    print(f"  #{f['ahnentafel']}: {f['full_name']} ({f.get('epistemic_level')})")

print(f"\nCollateral facts ({len(collateral_facts)}):")
for f in collateral_facts:
    print(f"  #{f['ahnentafel']}: {f['full_name']} ({f.get('epistemic_level')})")

print(f"\nTotal verified facts: {len(direct_facts) + len(collateral_facts)}")
print(f"Total direct nodes: {len(data['nodes'])}")
print(f"Total collateral nodes: {len(data['collateral_nodes'])}")
