import subprocess
import os

files_to_sync = [
    ("eco-home-v1.4.1-core.yaml", "/config/automations/EcoHome.yaml"),
    ("eco-home-v1.4.1-cucina.yaml", "/config/automations/cucina.yaml"),
    ("eco-home-v1.4.1-frigo-meteo-asciugatrice.yaml", "/config/automations/frigo_meteo.yaml")
]

base_dir = r"C:\Users\stefa\OneDrive\Cartella di Lavoro\Progetti\eco-home"

for src, dst in files_to_sync:
    src_path = os.path.join(base_dir, src)
    print(f"Syncing {src} -> {dst}...")
    cmd = f'scp -o StrictHostKeyChecking=no "{src_path}" gates538@192.168.179.145:"{dst}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(f"Exit code: {res.returncode}, stdout: {res.stdout}, stderr: {res.stderr}")
