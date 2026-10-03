import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])

pet_entities = [e.get("entity_id") for e in entities if any(k in e.get("entity_id", "") for k in ["petkit", "puramax", "dispenser", "crocchette", "lettiera"])]
car_entities = [e.get("entity_id") for e in entities if any(k in e.get("entity_id", "") for k in ["drivvo", "discovery", "refuelling", "vehicle", "odometer"])]

print("=== PET ENTITIES ===")
for p in pet_entities:
    print(" -", p)

print("\n=== CAR / DRIVVO ENTITIES ===")
for c in car_entities:
    print(" -", c)
