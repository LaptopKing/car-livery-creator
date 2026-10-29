import os
import glob

dir_path = r"H:\Saját meghajtó\Car Design Collection"
files = sorted(glob.glob(os.path.join(dir_path, "*.[jJ][pP][gG]")) + 
               glob.glob(os.path.join(dir_path, "*.[pP][nN][gG]")))
with open(r"C:\Users\strider-desktop\.gemini\antigravity\scratch\car-livery-creator\image_index.txt", "w", encoding="utf-8") as out:
    for i, f in enumerate(files):
        line = f"{i+1:02d}: {os.path.basename(f)}\n"
        print(line, end="")
        out.write(line)
