import json

with open(r"C:\Karetnikov_Lineage\public\vault\lineage_payload.enc.json", "r", encoding="utf-8") as f:
    enc_data = json.load(f)

print("lineage_payload.enc.json keys:", list(enc_data.keys()))
if "envelopes" in enc_data:
    print("envelopes:", enc_data["envelopes"])
else:
    print("No envelopes key at top level. Let's see all keys and types:")
    for k, v in enc_data.items():
        if isinstance(v, str):
            print(f"  {k}: str (len {len(v)})")
        elif isinstance(v, dict):
            print(f"  {k}: dict keys={list(v.keys())}")
        else:
            print(f"  {k}: {type(v).__name__} = {v}")

with open(r"C:\Karetnikov_Lineage\data\vault\lineage_graph.json", "r", encoding="utf-8") as f:
    graph = json.load(f)

print("\nlineage_graph.json keys:", list(graph.keys()))
if "floating_hypotheses" in graph:
    print(f"floating_hypotheses count: {len(graph['floating_hypotheses'])}")
    print("Sample floating hypothesis:", graph['floating_hypotheses'][0])
