import json

with open(r"C:\Karetnikov_Lineage\public\vault\lineage_payload.enc.json", "r", encoding="utf-8") as f:
    enc_data = json.load(f)

print("Envelopes keys:", list(enc_data["envelopes"].keys()))
for env_name, env in enc_data["envelopes"].items():
    print(f"\nEnvelope: {env_name}")
    print(f"  access_role: {env.get('access_role')}")
    print(f"  iterations: {env.get('iterations')}")
    print(f"  salt_b64: {env.get('salt_b64')}")
    print(f"  iv_b64: {env.get('iv_b64')}")
    print(f"  ciphertext_b64 len: {len(env.get('ciphertext_b64', ''))}")
