import os
files = [f'IMG_{i}.JPG' for i in range(6281, 6301)]
base_dir = r'H:\Saját meghajtó\Car Design Collection'
thumb_dir = r'C:\Users\strider-desktop\.gemini\antigravity\scratch\car-livery-creator\thumbs'
print('Base exists:', os.path.exists(base_dir))
for f in files:
    p = os.path.join(base_dir, f)
    t = os.path.join(thumb_dir, f)
    print(f, 'orig:', os.path.exists(p), 'thumb:', os.path.exists(t))
