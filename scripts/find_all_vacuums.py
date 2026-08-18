import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
vac_entities = []
for e in entities:
    eid = e.get("entity_id", "")
    domain = eid.split(".")[0]
    if domain in ["vacuum", "sensor", "binary_sensor"] and any(k in eid for k in ["dreame", "l40", "dobby", "robot"]):
        vac_entities.append((eid, e.get("original_name"), e.get("platform")))

print("=== ALL VACUUM / DREAME ENTITIES IN ER ===")
for ve in vac_entities:
    print(" -", ve)
