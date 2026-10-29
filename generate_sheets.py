import os
import glob
from PIL import Image

COLLECTION_DIR = r"H:\Saját meghajtó\Car Design Collection"
OUTPUT_DIR = r"C:\Users\strider-desktop\.gemini\antigravity\scratch\car-livery-creator"
THUMBS_DIR = os.path.join(OUTPUT_DIR, "thumbs")
SHEETS_DIR = os.path.join(OUTPUT_DIR, "contact_sheets")

os.makedirs(THUMBS_DIR, exist_ok=True)
os.makedirs(SHEETS_DIR, exist_ok=True)

image_files = sorted(glob.glob(os.path.join(COLLECTION_DIR, "*.[jJ][pP][gG]")) + 
                     glob.glob(os.path.join(COLLECTION_DIR, "*.[pP][nN][gG]")))

print(f"Found {len(image_files)} images.")

manifest = []
for idx, img_path in enumerate(image_files):
    filename = os.path.basename(img_path)
    try:
        with Image.open(img_path) as img:
            w, h = img.size
            manifest.append({
                "index": idx + 1,
                "filename": filename,
                "path": img_path,
                "width": w,
                "height": h,
                "aspect": round(w / h, 2)
            })
            
            # Create a uniform thumbnail for contact sheets
            thumb = img.copy()
            thumb.thumbnail((400, 400))
            thumb.save(os.path.join(THUMBS_DIR, f"{idx+1:02d}_{filename}"))
    except Exception as e:
        print(f"Error reading {filename}: {e}")

print(f"Created {len(manifest)} thumbnails.")

# Create contact sheets in groups of 9 (3x3 grid)
BATCH_SIZE = 9
for batch_idx in range(0, len(manifest), BATCH_SIZE):
    batch = manifest[batch_idx:batch_idx + BATCH_SIZE]
    sheet_num = (batch_idx // BATCH_SIZE) + 1
    
    cell_w, cell_h = 420, 420
    grid_cols = 3
    grid_rows = (len(batch) + grid_cols - 1) // grid_cols
    
    sheet = Image.new("RGB", (grid_cols * cell_w, grid_rows * cell_h), (25, 25, 28))
    
    for i, item in enumerate(batch):
        r = i // grid_cols
        c = i % grid_cols
        thumb_path = os.path.join(THUMBS_DIR, f"{item['index']:02d}_{item['filename']}")
        with Image.open(thumb_path) as t:
            # Center thumbnail in cell
            tw, th = t.size
            x_offset = c * cell_w + (cell_w - tw) // 2
            y_offset = r * cell_h + (cell_h - th) // 2
            sheet.paste(t, (x_offset, y_offset))
            
    sheet_path = os.path.join(SHEETS_DIR, f"contact_sheet_{sheet_num:02d}.jpg")
    sheet.save(sheet_path, quality=85)
    print(f"Saved {sheet_path} with {len(batch)} images.")

print("All contact sheets generated successfully!")
