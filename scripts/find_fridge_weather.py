import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])

fridge_entities = [e.get("entity_id") for e in entities if "frigo" in e.get("entity_id", "")]
weather_entities = [e.get("entity_id") for e in entities if any(k in e.get("entity_id", "") for k in ["anemometro", "pulviometro", "precipitazione", "vento", "netatmo"])]
dryer_entities = [e.get("entity_id") for e in entities if "asciugatrice" in e.get("entity_id", "") or "dryer" in e.get("entity_id", "")]

print("=== FRIDGE ENTITIES ===")
for f in fridge_entities:
    print(" -", f)

print("\n=== WEATHER / NETATMO ENTITIES ===")
for w in weather_entities:
    print(" -", w)

print("\n=== DRYER / ASCIUGATRICE ENTITIES ===")
for d in dryer_entities:
    print(" -", d)
