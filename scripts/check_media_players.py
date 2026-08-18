import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
mp_entities = []
for e in entities:
    eid = e.get("entity_id", "")
    if eid.startswith("media_player.") or eid.startswith("tts."):
        mp_entities.append((eid, e.get("original_name"), e.get("platform")))

print("=== ALL MEDIA PLAYER & TTS ENTITIES ===")
for mp in mp_entities:
    print(" -", mp)
