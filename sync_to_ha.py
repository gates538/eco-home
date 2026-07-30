import shutil
import os

src_dir = r"C:\Users\stefa\OneDrive\Cartella di Lavoro\Progetti\eco-home"
dst_dir = r"Z:\automations"

mapping = {
    "eco-home-v1.4.1-core.yaml": "EcoHome.yaml",
    "eco-home-v1.4.1-cucina.yaml": "cucina.yaml",
    "eco-home-v1.4.2-dobby-and-frost.yaml": "dobby_frost.yaml",
    "eco-home-v1.4.2-cottura-dimenticata.yaml": "cottura_dimenticata.yaml",
    "eco-home-v1.4.2-zero-sprechi-luci.yaml": "zero_sprechi_luci.yaml",
    "eco-home-v1.4.2-emby-cinema-silenzioso.yaml": "emby_cinema.yaml",
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"Synced {src_name} -> {dst_path}")
    else:
        print(f"File not found: {src_path}")
