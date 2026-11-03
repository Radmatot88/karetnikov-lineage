import json

with open(r"C:\Karetnikov_Lineage\data\vault\lineage_graph.json", "r", encoding="utf-8") as f:
    data = json.load(f)

nodes = data.get("nodes", [])
edges = data.get("edges", [])

print(f"Total nodes: {len(nodes)}, Total edges: {len(edges)}")

dmitriy_nodes = []
for node in nodes:
    label = str(node.get("label", ""))
    name = str(node.get("name", ""))
    data_dict = node.get("data", {})
    if "Дмитрий" in label or "Дмитрий" in name or "1913" in str(node):
        print("FOUND NODE:", json.dumps(node, ensure_ascii=False, indent=2))
        dmitriy_nodes.append(node)

# Also let's check Ivan Dmitrievich
for node in nodes:
    label = str(node.get("label", ""))
    if "Иван" in label and "Дмитри" in label:
        print("FOUND IVAN DMITRIEVICH:", json.dumps(node, ensure_ascii=False, indent=2))

