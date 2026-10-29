"""
Compile Master Catalog: Stitches together the master 83-car reference index
"""

import os
import re

REF_DIR = r"C:\Users\strider-desktop\.gemini\antigravity\scratch\car-livery-creator\references"
OUTPUT_FILE = os.path.join(REF_DIR, "master_catalog_83.md")

batch_files = [
    os.path.join(REF_DIR, "analysis_batch_1.md"),
    os.path.join(REF_DIR, "analysis_batch_2.md"),
    os.path.join(REF_DIR, "analysis_batch_3.md"),
    os.path.join(REF_DIR, "analysis_batch_4.md")
]

entries = []
seen_nums = set()

for bf in batch_files:
    if not os.path.exists(bf):
        continue
    with open(bf, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern matches any of:
    # ### Reference 01: ... \n - **Image Filename:** `IMG_6218.JPG`
    # IMAGE 22: IMG_6239.JPG
    # ### Image 43: IMG_6260.JPG
    # ## Image 64: `IMG_6281.JPG`
    pattern = re.compile(r'(?:### Reference|IMAGE|### Image|## Image)\s*(\d+)[:\s`]+([^\n\r]+)', re.IGNORECASE)
    matches = list(pattern.finditer(content))

    for idx, match in enumerate(matches):
        img_num = int(match.group(1))
        header_text = match.group(2)
        if img_num in seen_nums or img_num > 83 or img_num < 1:
            continue
        seen_nums.add(img_num)

        start_pos = match.start()
        end_pos = matches[idx + 1].start() if idx + 1 < len(matches) else len(content)
        block = content[start_pos:end_pos]

        # Extract filename:
        fn_match = re.search(r'(IMG_\d+\.JPG)', block, re.IGNORECASE)
        filename = fn_match.group(1) if fn_match else f"IMG_{6217+img_num}.JPG"

        # Extract subject car
        subject_match = re.search(r'(?:Subject Car|Platform|Vehicle Make|Make & Model|Vehicle Platform)[:\s*`]+([^\n\r]+)', block, re.IGNORECASE)
        if subject_match:
            subject = subject_match.group(1).strip("*# `")
        else:
            # Fallback to header text if it has a colon
            subject = header_text.split(":")[-1].strip("*# `") if ":" in header_text else header_text.strip("*# `")

        # Extract style
        style_match = re.search(r'(?:Livery Archetype|Cultural School|Discipline|Style)[:\s*`]+([^\n\r]+)', block, re.IGNORECASE)
        style = style_match.group(1).strip("*# `") if style_match else "JGTC / Street Style"

        # Extract dominant rule
        rule_match = re.search(r'(?:Core Actionable Design Rule|Design Rule|Core Rule)[:\s*`]+([^\n\r]+)', block, re.IGNORECASE)
        rule = rule_match.group(1).strip("*# `") if rule_match else "Harmonize graphics with chassis flow lines."

        entries.append({
            "num": img_num,
            "filename": filename,
            "subject": subject[:55].replace('|', '-'),
            "style": style[:45].replace('|', '-'),
            "rule": rule[:95].replace('|', '-')
        })

entries.sort(key=lambda x: x["num"])

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# Master Reference Catalog: 83 Iconic Automotive Liveries\n\n")
    f.write(f"Comprehensive forensic index of all {len(entries)} reference images from `H:\\Saját meghajtó\\Car Design Collection`.\n\n")
    f.write("| # | Image File | Vehicle Platform | Cultural Archetype | Core Architectural Rule |\n")
    f.write("|---|---|---|---|---|\n")
    for e in entries:
        f.write(f"| {e['num']:02d} | `{e['filename']}` | {e['subject']} | {e['style']} | {e['rule']} |\n")

    f.write("\n\n## Batch Detailed Analysis Navigation\n")
    f.write("- [Batch 1 (Images 01–21)](./analysis_batch_1.md): BMW E30 Touring, Lada Restomod, Porsche 911 GT1, Porsche 963 Le Mans, Hoonipigasus, RWB Porsches.\n")
    f.write("- [Batch 2 (Images 22–42)](./analysis_batch_2.md): Subaru 555 WRC, Calsonic R32 Group A, Ferrari F40 LM, Mazda 787B Renown, Ford GT40, DTM Alfa 155, Bosozoku, Itasha.\n")
    f.write("- [Batch 3 (Images 43–63)](./analysis_batch_3.md): Character Itasha (Goku, Buzz Lightyear, Patrick Star), Kanjo Civics, Pastrana GL Wagon, LTO E30, Datsun 240Z Zero Fighter.\n")
    f.write("- [Batch 4 (Images 64–83)](./analysis_batch_4.md): Silk Cut Jaguar Group C, Castrol Jaguar XJR-9, Apple Porsche/Lotus, JTCC Accord Trilogy, Takata Dome NSX, Mobil 1 NSX, Cusco GC8.\n")

print(f"Master catalog generated with {len(entries)} indexed entries: {OUTPUT_FILE}")
