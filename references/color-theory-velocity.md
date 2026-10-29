# Color Theory of Velocity & Vinyl Materials Guide

In automotive livery design, color is not merely an aesthetic choice—it is a **functional aerodynamic signal**. At 250 km/h, the human eye and trackside broadcast cameras do not have time to process complex nuance; they perceive silhouette blocks, luminous contrast, and chromatic boundaries.

---

## 1. The 60-30-10 Velocity Distribution Rule

Every master livery adheres to a strict hierarchical color distribution:

| Layer | Percentage | Visual Function | Typical Placement | Exemplar |
|---|---|---|---|---|
| **Dominant (Base)** | ~60% | Vehicle identification & silhouette foundation | Full body shell, roof, quarter panels | Calsonic Cobalt (`#0055A5`), Advan Black (`#111111`) |
| **Secondary (Graphic)** | ~30% | Direction of motion, forward rake & attitude | Sweeping wedges, scallops, diagonal slashes | Castrol Green (`#008751`), Falken Sky Blue (`#028090`) |
| **Accent (Tension)** | ~10% | Eye anchor, boundary isolation & focal details | Tow arrows, mirrors, wing endplates, pin-stripes | Castrol Crimson (`#DE0029`), Neon Yellow (`#FFD200`) |

### Why This Ratio Works:
- If a livery is **50/50**, neither color leads; the car's body shape appears fractured and visually unstable at speed.
- If a livery has **too many colors (e.g. 5 colors in equal share)**, the design becomes visual noise and sponsor logos become completely illegible.
- The 60-30-10 ratio creates an immediate visual hierarchy: **Identify chassis -> Follow vector of motion -> Read sponsor details.**

---

## 2. Optical Boundary Isolation (The Anti-Vibration Law)

When two highly saturated, contrasting colors (especially complementary or near-complementary pairs) touch directly without an outline, an optical phenomenon known as **chromatic aberration / simultaneous contrast vibration** occurs. The boundary appears to flicker or blur to the human eye, destroying sharpness.

### Dangerous Color Pairings:
1. **Red + Green (e.g. Castrol):** Without isolation, the border vibrates aggressively.
   - *Master Fix:* A 2mm–5mm pure white (`#FFFFFF`) spacer boundary separates the red chevron from the green sweep.
2. **Orange + Green (e.g. Renown 787B):**
   - *Master Fix:* White dashed needle-and-thread stitch lines isolate the fluorescent orange from the racing green argyle diamonds.
3. **Navy Blue + Crimson Red (e.g. Mobil 1 / Rothmans):**
   - *Master Fix:* A crisp white keyline or golden ribbon buffers the two deep tones.
4. **Yellow + White:**
   - *Master Fix:* Low luminance contrast makes yellow illegible on white. A black (`#000000`) keyline or drop shadow is mandatory.

---

## 3. Luminance Contrast & Speed Readability

To guarantee readability from the grandstands or on TV cameras, logos and essential race numbers must meet strict luminance contrast ratios:

$$\text{Contrast Ratio} = \frac{L_1 + 0.05}{L_2 + 0.05}$$

- **Title Sponsors & Race Numbers:** Minimum **4.5:1** contrast ratio against the background paint.
- **Secondary Decals:** Minimum **3.0:1** contrast ratio.
- If a dark logo (e.g., black NISMO text) must sit over a dark section of paint (e.g., carbon fiber hood), place the logo inside a **White Sticker Backer (Pill)** or apply a **2pt white contour outline**.

---

## 4. Real-World Wrap Finishes & Material Science

Digital liveries often treat all colors as flat hex codes, but physical race wraps and high-end sim rendering rely on material finish interactions:

### Finish Types & Strategic Application:
- **High-Gloss Vinyl (e.g., 3M 2080-G12 Gloss Deep Black):**
  - Maximizes light reflection, highlights body curve highlights. Best for primary sponsor zones.
- **Satin / Matte Vinyl (e.g., Avery SW900-190-O Matte Black):**
  - Absorbs harsh reflections, creating a menacing, stealth mechanical presence. Perfect for lower rocker panels, splitters, and diffusers to "slam" the car visually.
- **Metallic / Pearl Flake (e.g., 3M 2080-GP278 Gloss Flip Deep Space):**
  - Shifts hue depending on camera angle and sunlight. Used extensively in JGTC (Raybrig metallic blue) and modern drift builds.
- **Fluorescent / Dayglo (e.g., Oracal 7510 Fluorescent Orange):**
  - Reflects ultraviolet light, appearing to "glow" in daylight. Mandatory for safety accents (TOW arrows), Le Mans night racing visibility, and iconic retro racers (Renown 787B, Marlboro Chevron).
- **Brushed Titanium / Chrome Foil:**
  - Used for retro-futuristic Cyberpunk accents, heat shield emulation around side-exit exhausts, and premium sponsor highlights.
- **Dry Carbon Weave (1x1 or 2x2 Twill):**
  - Used on hood vents, canards, GT wings, and rear diffusers to denote lightweight racing components.

---

## 5. Sim-Racing vs. Physical Print Color Space Conversion

| Scheme | Hex Code | RGB (0-255) | 3M Wrap Code Equivalent | Avery Dennison Code |
|---|---|---|---|---|
| **Calsonic Blue** | `#0055A5` | `(0, 85, 165)` | 3M 2080-G378 Gloss Blue Raspberry | SW900-671-O Gloss Intense Blue |
| **Castrol Green** | `#008751` | `(0, 135, 81)` | 3M 2080-G46 Gloss Kelly Green | SW900-758-O Gloss Dark Green |
| **Castrol Red** | `#DE0029` | `(222, 0, 41)` | 3M 2080-G13 Gloss Hot Rod Red | SW900-472-O Gloss Dragon Red |
| **Takata Green** | `#007F3E` | `(0, 127, 62)` | 3M 2080-G336 Gloss Green Envy | SW900-771-O Gloss Apple Green |
| **Pennzoil Yellow** | `#FFCE00` | `(255, 206, 0)` | 3M 2080-G25 Gloss Sunflower Yellow | SW900-236-O Gloss Bright Yellow |
| **Advan Red** | `#DE0029` | `(222, 0, 41)` | 3M 2080-G13 Gloss Hot Rod Red | SW900-436-O Gloss Carmine Red |
| **Gulf Powder Blue** | `#7BA4D5` | `(123, 164, 213)` | 3M 2080-G147 Gloss Sky Blue | SW900-643-O Gloss Powder Blue |
| **Gulf Tangerine** | `#FF6B00` | `(255, 107, 0)` | 3M 2080-G14 Gloss Burnt Orange | SW900-362-O Gloss Bright Orange |
| **Championship White** | `#F8F9FA` | `(248, 249, 250)` | 3M 2080-G10 Gloss White | SW900-101-O Gloss White |
| **Stealth Satin Black** | `#141416` | `(20, 20, 22)` | 3M 2080-S12 Satin Black | SW900-197-O Satin Black |
