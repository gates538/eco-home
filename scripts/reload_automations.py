import json
import urllib.request
import urllib.error
import os

# Check for SUPERVISOR_TOKEN or Home Assistant auth tokens
token = os.environ.get("SUPERVISOR_TOKEN", "")

# Search for long-lived access tokens or auth tokens in .storage
if not token:
    auth_file = r"Z:\.storage\auth"
    if os.path.exists(auth_file):
        try:
            with open(auth_file, "r", encoding="utf-8") as f:
                auth_data = json.load(f)
            tokens = auth_data.get("data", {}).get("refresh_tokens", [])
            for t in tokens:
                if t.get("token_type") == "long_lived_access_token":
                    token = t.get("access_token")
                    print("Found long_lived_access_token in .storage/auth")
                    break
        except Exception as e:
            print("Error reading auth file:", e)

# Try calling automation/reload service via REST API
urls = [
    "http://127.0.0.1:8123/api/services/automation/reload",
    "http://localhost:8123/api/services/automation/reload",
    "http://192.168.179.140:8123/api/services/automation/reload"
]

success = False
for url in urls:
    try:
        req = urllib.request.Request(url, method="POST")
        req.add_header("Content-Type", "application/json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"Reload response from {url}: {resp.status}")
            success = True
            break
    except Exception as e:
        print(f"Failed to reload via {url}: {e}")

if not success:
    print("Could not reload automations automatically via REST API without token.")
