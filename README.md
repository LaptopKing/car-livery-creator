# 🏎️ Car Livery Creator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests: Passing](https://img.shields.io/badge/tests-passing-brightgreen.svg)]()
[![GT7 SVG Compliant](https://img.shields.io/badge/Gran%20Turismo%207-%3C15KB%20SVG-orange.svg)]()
[![Antigravity Skill](https://img.shields.io/badge/Antigravity-Native%20Skill-purple.svg)]()

> **The definitive automotive livery design skill, aerodynamic graphic styling suite, and motorsport identity engine.**

Rooted in a forensic visual and architectural analysis of **83 iconic motorsport and underground street machines**—from **JGTC / Super GT Golden Era GT500/GT300** legends, **Osaka Kanjozoku** highway runners, and **Kaido Racer / Bosozoku** silhouettes, to **D1GP drift icons**, **Le Mans prototypes**, and **character-infused Itasha**.

---

## ⚡ Key Capabilities

- **Chassis Flow-Line Synchronization:** Harmonize graphics with real automotive anatomy—beltlines, swage creases, blister wheel arches, diffusers, and GT wings.
- **The 60-30-10 Velocity Color Rule:** Compositional balance designed for readability at 250+ km/h (60% Dominant Base, 30% Dynamic Graphic Mass, 10% High-Energy Accent).
- **Optical Boundary Isolation:** Automatic detection of chromatic vibration clashes (e.g., Red/Green, Orange/Green) and injection of protective 2–5mm white or black spacer keylines.
- **4-Tier Sponsor Hierarchy:** Strict architectural real estate zoning (Tier 1 Title Billboard, Tier 2 Co-Sponsors, Tier 3 Mechanical Vertical Stack, Tier 4 Scrutineering Safety Tags).
- **Sponsor Vault Database:** 100+ curated JDM and motorsport sponsors categorized by functional systems (Tuning, Suspension, Brakes, Wheels, Tires, Fluids, Safety, Electronics).
- **Modular SVG Blueprint Generator:** Generates crisp, layered side-profile car elevations (`gtr_r34`, `rx7_fd`, `civic_eg`, `silvia_s15`, `porsche_911`) with customizable liveries, wheels, and aero wings.
- **Gran Turismo 7 SVG Optimizer:** Automatically strips metadata, rounds coordinates, and compresses SVG decals to guarantee strict compliance with GT7's **15.0 KB** upload limit.
- **Master 83-Car Reference Catalog:** An exhaustive, 260KB+ forensic breakdown of all 83 reference cars with color ratios, HEX palettes, sponsor layouts, and design rules.

---

## 🏛️ System Architecture

```
car-livery-creator/
├── SKILL.md                          # Antigravity skill specification & 6-phase workflow
├── README.md                         # Project documentation & GitHub guide
├── LICENSE                           # MIT License
│
├── references/                       # Deep domain knowledge & forensic analyses
│   ├── master_catalog_83.md          # 83-car master lookup matrix & architectural rules
│   ├── analysis_batch_1.md           # Images 01–21 (BMW E30 Touring, Lada, Le Mans, RWB)
│   ├── analysis_batch_2.md           # Images 22–42 (Subaru 555, Calsonic R32, 787B, DTM)
│   ├── analysis_batch_3.md           # Images 43–63 (Character Itasha, Kanjo, Pastrana GL)
│   ├── analysis_batch_4.md           # Images 64–83 (Silk Cut Jaguar, JTCC Accords, Dome NSX)
│   ├── principles.md                 # 12 Core Principles of Automotive Velocity Design
│   ├── jgtc-golden-era.md            # JGTC GT500/GT300 history, palettes & skunkworks
│   ├── japanese-street-culture.md    # Kanjozoku, Kaido Racer, D1GP & Wangan underground
│   ├── color-theory-velocity.md      # Contrast ratios, boundary isolation & vinyl materials
│   ├── chassis-flow-geometry.md      # Body panel mapping, hardpoints & aero integration
│   ├── sponsor-curation-hierarchy.md # 4-Tier sponsor zoning & vertical stack anatomy
│   ├── visual-motifs-and-shapes.md   # Wedge cuts, scallops, camo shards, kanji typography
│   └── sim-racing-game-export.md     # GT7, Forza Horizon 5, Assetto Corsa & 1:1 wrap guide
│
├── scripts/                          # Dependency-free Python 3 CLI tools
│   ├── svg_car_generator.py          # Modular SVG side-profile car blueprint generator
│   ├── palette_engine.py             # Velocity contrast calculator & curated palettes
│   ├── sponsor_vault.py              # Searchable JDM sponsor database & stack generator
│   ├── gt7_svg_optimizer.py          # Strict GT7 SVG decal optimizer (<15KB)
│   ├── livery_spec.py                # Livery JSON specification validator & exporter
│   └── preview_sheet.py              # Standalone interactive HTML studio showcase
│
├── templates/                        # Ready-to-use project templates
│   ├── livery-brief-template.md      # Comprehensive design brief questionnaire
│   ├── livery-spec.example.json      # Sample JSON specification (Castrol TOM'S Supra)
│   └── gt7-decal-template.svg        # 512x512 clean SVG decal canvas
│
└── tests/                            # Automated test suite
    └── test_tools.py                 # Comprehensive unit tests for all CLI tools
```

---

## 🚀 Quickstart & CLI Usage

All scripts run on standard Python 3.10+ with zero external dependencies (uses standard library `json`, `math`, `re`, `argparse`, `xml.etree`).

### 1. Generate a Modular SVG Car Blueprint
```bash
# Generate a Calsonic GT-R R34 with white Impul turbofans
python scripts/svg_car_generator.py \
  --chassis gtr_r34 \
  --style wedge_split \
  --base "#0055A5" \
  --secondary "#FFFFFF" \
  --accent "#FFD200" \
  --sponsor "CALSONIC" \
  --wheel turbofan \
  --wheel-color "#FFFFFF" \
  --number 12 \
  -o calsonic_r34.svg
```

### 2. Inspect a Historical Livery Palette & Contrast
```bash
# Analyze Castrol TOM'S Supra palette and check optical boundary isolation
python scripts/palette_engine.py --palette castrol_toms
```

### 3. Generate an Authentic Tier 3 Vertical Sponsor Stack
```bash
# Generate Nissan-accurate vertical fender stack:
# (NISMO -> Tein -> Endless -> Rays -> Potenza -> Motul)
python scripts/sponsor_vault.py --make Nissan --stack
```

### 4. Optimize an SVG Decal for Gran Turismo 7 (<15KB)
```bash
# Strips editor metadata, rounds coordinates, and compresses SVG
python scripts/gt7_svg_optimizer.py decal.svg -o decal_gt7.svg
```

### 5. Launch the Standalone Interactive Showcase Sheet
```bash
# Generates a standalone interactive HTML studio with real-time palette toggles
python scripts/preview_sheet.py -o studio.html
# Open studio.html in any modern web browser!
```

---

## 🎨 Historical & Cultural Palettes Included

| Slug | Livery Inspiration | Dominant 60% | Secondary 30% | Accent 10% | Boundary Rule |
|---|---|---|---|---|---|
| `calsonic` | JGTC Calsonic GT-R R32/R34 | `#0055A5` | `#FFFFFF` | `#FFD200` | Clean Adjacency |
| `castrol_toms` | GT500 Castrol TOM'S Supra | `#FFFFFF` | `#008751` | `#DE0029` | **White Spacer Line** |
| `takata_dome` | GT500 Takata Dome NSX | `#007F3E` | `#FFFFFF` | `#E60012` | Clean Adjacency |
| `pennzoil_nismo`| JGTC Pennzoil GT-R | `#FFCE00` | `#161616` | `#DE2910` | Clean Adjacency |
| `raybrig_nsx` | GT500 Raybrig Electric NSX | `#0B1B3D` | `#00D2FF` | `#FF3B30` | Clean Adjacency |
| `advan_racing` | Yokohama Advan Slashes | `#121212` | `#DE0029` | `#FFFFFF` | Clean Adjacency |
| `falken_drift` | Falken Scallops | `#00A896` | `#028090` | `#212529` | Clean Adjacency |
| `renown_787b` | Mazda 787B Le Mans | `#FF5F00` | `#00783E` | `#FFFFFF` | **Dashed White Stitch** |
| `kanjo_yamato` | Osaka Loop Yamato Parody | `#80C29A` | `#FFDF00` | `#1A1A1A` | Clean Adjacency |
| `synthwave_neon`| Neo-Tokyo Cyberpunk | `#0F0F14` | `#FF007F` | `#00F0FF` | Neon Boundary Glow |

---

## 🧪 Testing

Run the automated test suite directly:
```bash
python tests/test_tools.py
```

---

## 📄 License

Distributed under the **MIT License**. Free for personal and commercial automotive livery design projects.
