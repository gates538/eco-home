import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
tts_list = []
for e in entities:
    eid = e.get("entity_id", "")
    if eid.startswith("tts."):
        tts_list.append((eid, e.get("original_name"), e.get("platform")))

print("=== ALL REGISTERED TTS ENTITIES IN HA ===")
for t in tts_list:
    print(" -", t)
