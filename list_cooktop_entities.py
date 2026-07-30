import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
cooktop = []
for e in entities:
    eid = e.get("entity_id", "")
    if "piano_cottura" in eid:
        cooktop.append(eid)

print("=== ALL COOKTOP ENTITIES ===")
for c in cooktop:
    print(" -", c)
