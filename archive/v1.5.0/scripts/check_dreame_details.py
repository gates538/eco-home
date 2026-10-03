import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
dreame_entities = []
for e in entities:
    eid = e.get("entity_id", "")
    if "dreame" in eid or "dobby" in eid or "vacuum" in eid:
        dreame_entities.append((eid, e.get("original_name"), e.get("platform")))

print("=== ALL DREAME / VACUUM ENTITIES ===")
for de in dreame_entities:
    print(" -", de)
