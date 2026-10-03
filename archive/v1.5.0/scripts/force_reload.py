import urllib.request
import json
import os

token = ""
auth_file = r"Z:\.storage\auth"
if os.path.exists(auth_file):
    try:
        with open(auth_file, "r", encoding="utf-8") as f:
            auth_data = json.load(f)
        for t in auth_data.get("data", {}).get("refresh_tokens", []):
            if t.get("token_type") in ["system", "long_lived_access_token", "normal"]:
                token = t.get("token") or t.get("access_token")
                print("Found token:", token[:10] + "...")
                break
    except Exception as e:
        print("Auth read error:", e)

urls = [
    "http://127.0.0.1:8123/api/services/automation/reload",
    "http://localhost:8123/api/services/automation/reload"
]

for url in urls:
    try:
        req = urllib.request.Request(url, method="POST", data=b"{}")
        req.add_header("Content-Type", "application/json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"Reload response from {url}: {resp.status}")
    except Exception as e:
        print(f"Error calling {url}: {e}")
