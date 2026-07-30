import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
vacuum_entities = []
for e in entities:
    eid = e.get("entity_id", "")
    if eid.startswith("vacuum."):
        vacuum_entities.append((eid, e.get("original_name"), e.get("platform")))

print("=== ALL VACUUM DOMAIN ENTITIES IN HOME ASSISTANT ===")
for v in vacuum_entities:
    print(" -", v)
