import json

ce_path = r"Z:\.storage\core.config_entries"
with open(ce_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entries = data.get("data", {}).get("entries", [])
tts_entries = []
for e in entries:
    domain = e.get("domain", "")
    if "tts" in domain or "cloud" in domain or "google" in domain or "piper" in domain:
        tts_entries.append((domain, e.get("title"), e.get("data"), e.get("options")))

print("=== ALL TTS CONFIG ENTRIES ===")
for t in tts_entries:
    print(" -", t)
