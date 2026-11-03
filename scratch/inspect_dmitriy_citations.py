import json

with open(r"C:\Karetnikov_Lineage\data\vault\osint_wave2_findings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find all citations and persons mentioned
for cand in data.get("branch_findings", {}).get("1_orenburg_karetnikovs", {}).get("direct_candidates_for_slot_16_ivan_karetnikov", []):
    print("Candidate:", cand.get("full_name"))
    print("Spouse:", cand.get("spouse"))
    print("Children:", cand.get("known_children_up_to_1915"))
    print("Citation links:", cand.get("citation_links"))

for fh in data.get("floating_hypotheses", []):
    if "FH-KAR-010" in fh.get("id", "") or "Дмитрий" in fh.get("full_name", ""):
        print("\nFH:", json.dumps(fh, ensure_ascii=False, indent=2))
