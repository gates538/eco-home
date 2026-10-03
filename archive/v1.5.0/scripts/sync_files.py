import subprocess
import os

files_to_sync = [
    ("eco-home-v1.5.0-core.yaml", "/config/automations/EcoHome.yaml"),
    ("eco-home-v1.5.0-cucina.yaml", "/config/automations/cucina.yaml"),
    ("eco-home-v1.5.0-frigo-meteo-asciugatrice.yaml", "/config/automations/frigo_meteo.yaml")
]

base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "automations")
ssh_target = os.environ.get("HA_SSH_TARGET", "root@homeassistant.local")

for src, dst in files_to_sync:
    src_path = os.path.join(base_dir, src)
    print(f"Syncing {src} -> {dst}...")
    cmd = f'scp -o StrictHostKeyChecking=no "{src_path}" {ssh_target}:"{dst}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"Exit code: {res.returncode}, stdout: {res.stdout}, stderr: {res.stderr}")
