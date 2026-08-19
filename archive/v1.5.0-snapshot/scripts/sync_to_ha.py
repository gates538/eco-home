import shutil
import os

src_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "automations")
dst_dir = r"Z:\automations"

mapping = {
    "eco-home-v1.5.0-core.yaml": "EcoHome.yaml",
    "eco-home-v1.5.0-cucina.yaml": "cucina.yaml",
    "eco-home-v1.5.0-dobby-and-frost.yaml": "dobby_frost.yaml",
    "eco-home-v1.5.0-cottura-dimenticata.yaml": "cottura_dimenticata.yaml",
    "eco-home-v1.5.0-zero-sprechi-luci.yaml": "zero_sprechi_luci.yaml",
    "eco-home-v1.5.0-emby-cinema-silenzioso.yaml": "emby_cinema.yaml",
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Synced {src_name} -> {dst_path}")
    else:
        print(f"File not found: {src_path}")
