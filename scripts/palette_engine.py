"""
Palette Engine: Color Harmony, High-Speed Velocity Contrast & Vinyl Finishes
Implements the 60-30-10 Rule, Optical Boundary Isolation, and Historical JDM / Motorsport Palettes.
"""

import sys
import math
import json
import argparse

PALETTES = {
    "calsonic": {
        "name": "Calsonic Impul GT",
        "description": "JGTC Nissan GT-R / Primera icon. Pure monochrome high-speed dominance.",
        "dominant_60": {"name": "Calsonic Cobalt", "hex": "#0055A5", "finish": "High Gloss"},
        "secondary_30": {"name": "Pure Arctic White", "hex": "#FFFFFF", "finish": "Gloss"},
        "accent_10": {"name": "Endurance Amber Yellow", "hex": "#FFD200", "finish": "Gloss"},
        "era": "90s-00s",
        "boundary_needed": False
    },
    "castrol_toms": {
        "name": "Castrol TOM'S Supra",
        "description": "Legendary Japanese GT500 ribbon swooshes. High kinetic flow.",
        "dominant_60": {"name": "Pearl Racing White", "hex": "#FFFFFF", "finish": "Gloss Pearl"},
        "secondary_30": {"name": "Castrol Emerald Green", "hex": "#008751", "finish": "Gloss"},
        "accent_10": {"name": "Castrol Crimson Red", "hex": "#DE0029", "finish": "Gloss"},
        "era": "90s",
        "boundary_needed": True,
        "boundary_color": "#FFFFFF",
        "boundary_reason": "Red and green touch causes chromatic vibration; separated by white spacer."
    },
    "takata_dome": {
        "name": "Takata Dome NSX",
        "description": "GT500 mid-engine purity. Takata racing harness green with pure white arrow.",
        "dominant_60": {"name": "Takata Harness Green", "hex": "#007F3E", "finish": "High Gloss"},
        "secondary_30": {"name": "Championship White", "hex": "#FFFFFF", "finish": "Gloss"},
        "accent_10": {"name": "Dome Racing Red", "hex": "#E60012", "finish": "Gloss"},
        "era": "00s",
        "boundary_needed": False
    },
    "pennzoil_nismo": {
        "name": "Pennzoil NISMO GT-R",
        "description": "JGTC GT500 champion. High-contrast yellow nose with black dropped rocker.",
        "dominant_60": {"name": "Pennzoil Solar Yellow", "hex": "#FFCE00", "finish": "Gloss"},
        "secondary_30": {"name": "Satin Carbon Black", "hex": "#161616", "finish": "Satin"},
        "accent_10": {"name": "Bell Oval Crimson", "hex": "#DE2910", "finish": "Gloss"},
        "era": "90s-00s",
        "boundary_needed": False
    },
    "raybrig_nsx": {
        "name": "Raybrig Nocturnal Lightning",
        "description": "High-voltage JGTC lighting team. Electric cyan discharge across metallic navy.",
        "dominant_60": {"name": "Midnight Metallic Blue", "hex": "#0B1B3D", "finish": "Metallic"},
        "secondary_30": {"name": "Electric Cyan Discharge", "hex": "#00D2FF", "finish": "Gloss"},
        "accent_10": {"name": "Raybrig Blaze Orange", "hex": "#FF3B30", "finish": "High Gloss"},
        "era": "90s-00s",
        "boundary_needed": False
    },
    "hks_oil_splash": {
        "name": "HKS Kinetic Oil Splash",
        "description": "Iconic D1GP and Group A Skyline splash graphics.",
        "dominant_60": {"name": "Stealth Obsidian Black", "hex": "#0A0A0A", "finish": "Satin"},
        "secondary_30": {"name": "HKS Racing Purple", "hex": "#8B1E8B", "finish": "Gloss"},
        "accent_10": {"name": "Aero Mint / Teal", "hex": "#00BFA5", "finish": "Gloss"},
        "era": "90s-00s",
        "boundary_needed": False
    },
    "advan_racing": {
        "name": "Yokohama Advan Red Slash",
        "description": "The purest racing aggression. Diagonal wedge cuts.",
        "dominant_60": {"name": "Matte Charcoal / Black", "hex": "#121212", "finish": "Matte / Satin"},
        "secondary_30": {"name": "Advan High-Gloss Red", "hex": "#DE0029", "finish": "High Gloss"},
        "accent_10": {"name": "Pure White Typographic", "hex": "#FFFFFF", "finish": "Gloss"},
        "era": "all",
        "boundary_needed": False
    },
    "falken_drift": {
        "name": "Falken Scallop Drift",
        "description": "Interlocking speed scallops peeling backward.",
        "dominant_60": {"name": "Falken Deep Teal", "hex": "#00A896", "finish": "Gloss"},
        "secondary_30": {"name": "Falken Sky Blue", "hex": "#028090", "finish": "Gloss"},
        "accent_10": {"name": "Matte Charcoal Smoke", "hex": "#212529", "finish": "Matte"},
        "era": "00s-modern",
        "boundary_needed": False
    },
    "renown_787b": {
        "name": "Renown Mazda 787B Le Mans",
        "description": "1991 Le Mans winner. Argyle diamond stitch pattern with dashed borders.",
        "dominant_60": {"name": "Fluorescent Dayglo Orange", "hex": "#FF5F00", "finish": "High Gloss"},
        "secondary_30": {"name": "Charge Racing Green", "hex": "#00783E", "finish": "High Gloss"},
        "accent_10": {"name": "Needle White Stitching", "hex": "#FFFFFF", "finish": "Gloss"},
        "era": "90s",
        "boundary_needed": True,
        "boundary_color": "#FFFFFF",
        "boundary_reason": "Dashed white stitch line prevents complementary orange/green clash."
    },
    "kanjo_yamato": {
        "name": "Kanjozoku Yamato Black Cat",
        "description": "Osaka loop line highway courier parody aesthetic.",
        "dominant_60": {"name": "Express Mint Green", "hex": "#80C29A", "finish": "Satin"},
        "secondary_30": {"name": "Delivery Sunburst Yellow", "hex": "#FFDF00", "finish": "Gloss"},
        "accent_10": {"name": "Kuro Neko Jet Black", "hex": "#1A1A1A", "finish": "Gloss"},
        "era": "90s-modern",
        "boundary_needed": False
    },
    "synthwave_cyberpunk": {
        "name": "Neo-Tokyo Cyberpunk",
        "description": "Nocturnal anime street racer with high-voltage neon pop.",
        "dominant_60": {"name": "Deep Space Obsidian", "hex": "#0F0F14", "finish": "Satin Black"},
        "secondary_30": {"name": "Electric Acid Magenta", "hex": "#FF007F", "finish": "Gloss Fluo"},
        "accent_10": {"name": "Neon Cyan Laser", "hex": "#00F0FF", "finish": "Gloss Fluo"},
        "era": "retro-future",
        "boundary_needed": False
    },
    "goku_saiyan": {
        "name": "Son Goku Super Saiyan Tribute",
        "description": "Anime character color translation onto widebody GT-R / coupe.",
        "dominant_60": {"name": "Turtle Hermit Dogi Orange", "hex": "#FF6200", "finish": "Gloss"},
        "secondary_30": {"name": "Royal Undershirt Blue", "hex": "#0D47A1", "finish": "Gloss"},
        "accent_10": {"name": "Super Saiyan Aura Gold", "hex": "#FFD700", "finish": "Metallic Gold"},
        "era": "pop-itasha",
        "boundary_needed": False
    },
    "buzz_lightyear": {
        "name": "Buzz Space Ranger Tribute",
        "description": "Toy Story character aesthetic applied to Le Mans / GT3 chassis.",
        "dominant_60": {"name": "Space Ranger Armor White", "hex": "#F4F5F7", "finish": "Gloss"},
        "secondary_30": {"name": "Laser Belt Green", "hex": "#43B02A", "finish": "Gloss"},
        "accent_10": {"name": "Star Command Purple", "hex": "#6C1D82", "finish": "Gloss"},
        "era": "pop-itasha",
        "boundary_needed": False
    },
    "stormtrooper_piaa": {
        "name": "PIAA Nakajima Monochrome",
        "description": "Pure black and white razor-sharp JTCC / JGTC aesthetic.",
        "dominant_60": {"name": "Glacier White", "hex": "#F8F9FA", "finish": "Ultra Gloss"},
        "secondary_30": {"name": "Deep Void Black", "hex": "#080808", "finish": "Satin"},
        "accent_10": {"name": "Titanium Grey Keyline", "hex": "#8A8D91", "finish": "Metallic"},
        "era": "90s",
        "boundary_needed": False
    }
}

def hex_to_rgb(hex_code):
    h = hex_code.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(hex_code):
    r, g, b = [x / 255.0 for x in hex_to_rgb(hex_code)]
    def adjust(c):
        return c / 12.92 if c <= 0.03928 else math.pow((c + 0.055) / 1.055, 2.4)
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def contrast_ratio(hex1, hex2):
    lum1 = relative_luminance(hex1)
    lum2 = relative_luminance(hex2)
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    return (lighter + 0.05) / (darker + 0.05)

def analyze_palette(palette_key):
    if palette_key not in PALETTES:
        print(f"Error: Palette '{palette_key}' not found.")
        print(f"Available palettes: {', '.join(PALETTES.keys())}")
        return

    p = PALETTES[palette_key]
    dom = p["dominant_60"]
    sec = p["secondary_30"]
    acc = p["accent_10"]

    cr_dom_sec = contrast_ratio(dom["hex"], sec["hex"])
    cr_dom_acc = contrast_ratio(dom["hex"], acc["hex"])
    cr_sec_acc = contrast_ratio(sec["hex"], acc["hex"])

    print(f"\n=======================================================")
    print(f"  PALETTE: {p['name']} ({p.get('era', 'all')})")
    print(f"  {p['description']}")
    print(f"=======================================================\n")
    print(f"  [60% BASE]    {dom['name']:25} {dom['hex']} ({dom['finish']})")
    print(f"  [30% GRAPHIC] {sec['name']:25} {sec['hex']} ({sec['finish']})")
    print(f"  [10% ACCENT]  {acc['name']:25} {acc['hex']} ({acc['finish']})\n")

    print(f"LUMINANCE CONTRAST RATIOS:")
    print(f"  • Base vs Graphic: {cr_dom_sec:.2f}:1  ({'EXCELLENT' if cr_dom_sec >= 4.5 else 'LOW - USE KEYLINE'})")
    print(f"  • Base vs Accent:  {cr_dom_acc:.2f}:1  ({'EXCELLENT' if cr_dom_acc >= 4.5 else 'MODERATE'})")
    print(f"  • Graphic vs Accent: {cr_sec_acc:.2f}:1\n")

    if p.get("boundary_needed"):
        print(f"OPTICAL BOUNDARY ISOLATION ALERT:")
        print(f"  [!] {p.get('boundary_reason')}")
        print(f"  Recommended Spacer Color: {p.get('boundary_color')} (stroke width: 2-4mm on 1:1 wrap)\n")
    else:
        print("Optical Boundary Isolation: Standard direct adjacency compliant.\n")

def main():
    parser = argparse.ArgumentParser(description="Palette Engine: Car Livery Color & Contrast Suite")
    parser.add_argument("--palette", "-p", help="Palette slug (e.g. calsonic, castrol_toms, takata_dome, falken_drift)")
    parser.add_argument("--list", "-l", action="store_true", help="List all curated palettes")
    parser.add_argument("--contrast", "-c", nargs=2, help="Compute contrast ratio between two HEX codes (e.g. -c #0055A5 #FFFFFF)")
    parser.add_argument("--json", action="store_true", help="Output JSON format")

    args = parser.parse_args()

    if args.list:
        if args.json:
            print(json.dumps(PALETTES, indent=2))
        else:
            print("\n=== CURATED HISTORICAL & RACING LIVERY PALETTES ===")
            for k, v in PALETTES.items():
                print(f" • {k:22} : {v['name']} [{v['dominant_60']['hex']}, {v['secondary_30']['hex']}, {v['accent_10']['hex']}]")
        return

    if args.contrast:
        hex1, hex2 = args.contrast
        cr = contrast_ratio(hex1, hex2)
        print(f"\nContrast Ratio between {hex1} and {hex2}: {cr:.2f}:1")
        print(f"Status: {'LEGIBLE AT SPEED (>=4.5:1)' if cr >= 4.5 else 'RISK OF BLUR (<4.5:1) - ADD OUTLINE'}")
        return

    if args.palette:
        analyze_palette(args.palette)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
