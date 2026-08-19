import json

er_path = r"Z:\.storage\core.entity_registry"
with open(er_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entities = data.get("data", {}).get("entities", [])
print("=== TTS ENTITIES IN CORE.ENTITY_REGISTRY ===")
for e in entities:
    eid = e.get("entity_id", "")
    if "tts" in eid:
        print(f" - Entity ID: {eid} | Platform: {e.get('platform')} | Unique ID: {e.get('unique_id')}")

ce_path = r"Z:\.storage\core.config_entries"
with open(ce_path, "r", encoding="utf-8") as f:
    cdata = json.load(f)

entries = cdata.get("data", {}).get("entries", [])
print("\n=== GOOGLE TRANSLATE CONFIG ENTRIES ===")
for entry in entries:
    if entry.get("domain") == "google_translate":
        print(f" - Entry ID: {entry.get('entry_id')} | Data: {entry.get('data')} | Options: {entry.get('options')}")
