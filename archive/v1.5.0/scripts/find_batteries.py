import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
battery_entities = [e.get("entity_id") for e in entities if "battery" in e.get("entity_id", "") or "batteria" in e.get("entity_id", "")]

print("=== BATTERY ENTITIES IN HA ===")
for b in battery_entities:
    print(" -", b)
