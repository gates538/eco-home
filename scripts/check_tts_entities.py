import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
tts_entities = []
for e in entities:
    eid = e.get("entity_id", "")
    if "tts" in eid or "google" in eid or "hub" in eid:
        tts_entities.append((eid, e.get("original_name"), e.get("platform")))

print("=== TTS / GOOGLE ENTITIES ===")
for t in tts_entities:
    print(" -", t)
