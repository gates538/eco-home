import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
for e in entities:
    eid = e.get("entity_id", "")
    if eid.startswith("tts."):
        print("Entity:", eid, "| Platform:", e.get("platform"), "| Options:", e.get("options"))
