import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
print("=== FRIDGE / FRIGORIFERO ENTITIES ===")
for e in entities:
    eid = e.get("entity_id", "")
    if "frig" in eid.lower() or "refrig" in eid.lower() or "frost" in eid.lower():
        print(f" - {eid} (name: {e.get('original_name') or e.get('name')})")
