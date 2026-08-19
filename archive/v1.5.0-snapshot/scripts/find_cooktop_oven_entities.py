import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
cucina_entities = []
for e in entities:
    eid = e.get("entity_id", "")
    if "cucina" in eid or "forno" in eid or "induzione" in eid or "piano_cottura" in eid:
        cucina_entities.append((eid, e.get("original_name"), e.get("platform")))

print("=== ALL CUCINA / FORNO / INDUZIONE ENTITIES IN ER ===")
for ce in cucina_entities:
    print(" -", ce)
