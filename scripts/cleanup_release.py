import os

dir_path = r"C:\Users\stefa\OneDrive\Cartella di Lavoro\Progetti\eco-home"
temp_files = [
    "combine.py",
    "find_batteries.py",
    "find_dobby.py",
    "find_fridge_weather.py",
    "find_frigo_exact.py",
    "find_pet_drivvo.py"
]

for f in temp_files:
    fp = os.path.join(dir_path, f)
    if os.path.exists(fp):
        try:
            os.remove(fp)
            print("Removed:", f)
        except Exception as e:
            print("Error removing:", f, e)
