# Sim Racing & Physical Wrap Export Guide

Professional liveries must translate seamlessly from conceptual vector designs into gaming engines (Gran Turismo 7, Forza Horizon 5, Assetto Corsa, iRacing) and physical vinyl wrap print shops.

---

## 1. Gran Turismo 7 (GT7 Decal Uploader Protocol)

Polyphony Digital enforces strict technical constraints on custom SVG decals uploaded through `gran-turismo.com/user/decal-uploader`.

### Hard Technical Limits:
- **Maximum File Size:** **15.0 KB (15,360 bytes)** per SVG. Files exceeding this by even 1 byte will trigger an immediate upload error.
- **SVG Spec:** SVG 1.1 Standard.
- **Embedded Rasters:** **100% PROHIBITED.** No PNG/JPG base64 data strings allowed.
- **Text Elements:** Must be converted to paths (`<path>` or `<polygon>`). Live `<text>` tags will render with fallback fonts or fail.

### Optimization Workflow:
1. Run `python scripts/gt7_svg_optimizer.py <your_decal.svg>`:
   - Strips all editor metadata (`inkscape:`, `sodipodi:`, `<metadata>`).
   - Removes XML comments and excessive whitespace.
   - Truncates decimal precision to 2 digits (e.g. `124.58291` -> `124.58`).
2. If the file is still >15 KB:
   - Combine separate path elements into compound paths (`d="M... Z M... Z"`).
   - In Illustrator/Inkscape, run Path -> Simplify (reduce anchor count by 20–30% without optical distortion).
   - Split complex multi-layer designs into 2 or 3 separate modular SVG layers and align them on the car in the GT7 livery editor.

---

## 2. Forza Horizon 5 & Forza Motorsport (Vinyl Group System)

Forza uses an internal procedural vinyl shape engine rather than direct vector file imports.

### Layer Budgeting & Best Practices:
- **Layer Limit:** Up to 3,000 layers per car side/hood/roof, and 1,000 layers per sub-assembly.
- **Vinyl Groups:** Build complex sponsor logos (e.g. NISMO, Castrol, Advan) as standalone Vinyl Groups first, then apply the group to the vehicle body.
- **Mirroring Symmetry:**
  - "Insert All from Right Side" mirrors coordinates automatically, but typographic sponsor letters will appear backwards!
  - **Rule:** Mirror the graphic shapes, then delete the reversed sponsor text and re-apply correctly oriented sponsor vinyl groups onto the opposite side.
- **Compound Curved Panels:** Forza projects vinyls straight along standard orthogonal axes (Top, Left, Right, Front, Rear). On rounded fender flares, shapes stretch. Use the "Angle Projection / Mask" tool to prevent roof stripes from bleeding into door jambs.

---

## 3. Assetto Corsa & iRacing (DDS Skin Texturing)

Assetto Corsa (with Custom Shaders Patch / Pure) and iRacing rely on 2D texture mapping over 3D UV unwrapped meshes.

### Assetto Corsa Skin Structure:
A car skin folder lives in `content/cars/<car_model>/skins/<skin_name>/`:
- `skin.dds` (or `skin.png`): Primary diffuse color map (Standard resolution: 4096 x 4096, BC7 or DXT1 compression with mipmaps).
- `skin_map.dds`: Specular / Roughness / Metallic map (Red = Redness/Ao, Green = Roughness/Gloss, Blue = Metallic).
- `livery.png`: UI preview thumbnail (200 x 90 px).
- `preview.jpg`: High-res garage showcase render (1024 x 576 px).
- `ui_skin.json`: Metadata containing car number, team name, driver name, country flag.
- `ext_config.ini`: Custom Shaders Patch shader overrides (e.g. adding chrome foil effects, glow-in-the-dark fluorescent decals, or custom glass tinting).

### CSP Shader Material Trick for Chrome / Gold Foils:
```ini
[INCLUDE: common/materials_carpaint.ini]
[Material_CarPaint_Metallic]
Materials = ext_body
ClearCoatThickness = 0.4
FlakesK = 0.8
```

---

## 4. Real-World Physical Vehicle Wrapping (1:1 Wrap Print)

When sending liveries to commercial wide-format vinyl printing and cutting shops:

### Vector Guidelines for Vinyl Cutters (Roland, Graphtec, Mimaki):
- **Cut Lines (Plotter Cutters):** Decal contours must be styled with a 0.25pt stroke set to a dedicated Spot Color named exactly `CutContour` (100% Magenta).
- **Print Bleed:** Full-vehicle printed wraps require **50mm (2 inches) of external bleed** past all body panel edges to allow installers to tuck vinyl cleanly behind door seals, wheel wells, and headlights.
- **Panel Seams & Relinquishments:**
  - Keep critical logos and typographic sponsor names at least 75mm away from door gaps, fuel filler doors, and bumper separation seams.
  - Never place a sponsor's letter directly across a panel gap where the knife cut will divide a character.
