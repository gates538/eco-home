import yaml, os

dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "automations")
files = [
    os.path.join(dir_path, "eco-home-v1.5.0-core.yaml"),
    os.path.join(dir_path, "eco-home-v1.5.0-cucina.yaml"),
    os.path.join(dir_path, "eco-home-v1.5.0-climate.yaml"),
    os.path.join(dir_path, "eco-home-v1.5.0-actions.yaml"),
    os.path.join(dir_path, "eco-home-v1.5.0-security.yaml"),
    os.path.join(dir_path, "luci.yaml"),
    os.path.join(dir_path, "notifiche.yaml")
]

all_autos = []
for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if isinstance(data, list):
                all_autos.extend(data)
            elif isinstance(data, dict):
                all_autos.append(data)

target_auto_file = r"Z:\automations.yaml"
with open(target_auto_file, "w", encoding="utf-8") as f:
    yaml.dump(all_autos, f, allow_unicode=True, sort_keys=False)

print(f"Combined {len(all_autos)} automations into {target_auto_file} successfully!")
