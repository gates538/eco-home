import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
dobby_entities = [e.get("entity_id") for e in entities if any(k in e.get("entity_id", "") for k in ["dobby", "dreame", "vacuum", "robot"])]

print("=== DOBBY / VACUUM ENTITIES ===")
for d in dobby_entities:
    print(" -", d)
