import json

with open(r"C:\Karetnikov_Lineage\data\vault\lineage_graph.json", "r", encoding="utf-8") as f:
    g = json.load(f)

hypotheses = g.get("floating_hypotheses", [])
print(f"Total hypotheses: {len(hypotheses)}")
for h in hypotheses:
    print(f"- {h['id']}: gen={h.get('generation')} ({h.get('generation_label')}), clan={h.get('clan')}, probable_rel={h.get('probable_relative_ahnentafel')}")
    print(f"  name: {h.get('full_name')}")
    print(f"  village: {h.get('village')}")
