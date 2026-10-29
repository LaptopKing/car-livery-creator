"""
Sponsor Vault: Curated Authentic JDM & Motorsport Racing Sponsor Registry
Provides era-accurate, tiered sponsor lookups, vertical stack generators,
and color pairings for car livery creation.
"""

import sys
import json
import argparse

SPONSORS = [
    # Engine / ECU / Tuning
    {"name": "NISMO", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#E60012", "#000000", "#FFFFFF"], "compat": ["Nissan", "Datsun"]},
    {"name": "Mugen Power", "category": "tuning", "origin": "JDM", "era": "all", "kanji": "無限", "colors": ["#E60012", "#FFD700", "#000000"], "compat": ["Honda"]},
    {"name": "TRD", "category": "tuning", "origin": "JDM", "era": "90s", "colors": ["#ED1C24", "#FFFFFF", "#000000"], "compat": ["Toyota"]},
    {"name": "TOM'S", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#008751", "#FFFFFF"], "compat": ["Toyota"]},
    {"name": "STI", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#E6007E", "#000000", "#FFFFFF"], "compat": ["Subaru"]},
    {"name": "Mazdaspeed", "category": "tuning", "origin": "JDM", "era": "90s", "colors": ["#0055A5", "#FF6600", "#FFFFFF"], "compat": ["Mazda"]},
    {"name": "Ralliart", "category": "tuning", "origin": "JDM", "era": "90s", "colors": ["#ED1C24", "#FF7F00", "#000000"], "compat": ["Mitsubishi"]},
    {"name": "Spoon Sports", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#005BAC", "#FFDE00"], "compat": ["Honda"]},
    {"name": "HKS", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#E60012", "#8B1E8B", "#00BFA5"], "compat": ["universal"]},
    {"name": "GReddy / Trust", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Apexi", "category": "tuning", "origin": "JDM", "era": "90s", "colors": ["#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Blitz", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#DE0029"], "compat": ["universal"]},
    {"name": "Tomei", "category": "tuning", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},
    {"name": "RE Amemiya", "category": "tuning", "origin": "JDM", "era": "all", "kanji": "雨宮", "colors": ["#0055A5", "#FFD700"], "compat": ["Mazda"]},
    {"name": "Mine's", "category": "tuning", "origin": "JDM", "era": "90s", "colors": ["#000000", "#DE0029"], "compat": ["Nissan"]},
    {"name": "Top Secret", "category": "tuning", "origin": "JDM", "era": "00s", "colors": ["#D4AF37", "#000000"], "compat": ["universal"]},

    # Suspension
    {"name": "Tein", "category": "suspension", "origin": "JDM", "era": "all", "colors": ["#009639", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Cusco", "category": "suspension", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Bilstein", "category": "suspension", "origin": "Euro", "era": "all", "colors": ["#00509B", "#FED100"], "compat": ["universal"]},
    {"name": "Öhlins", "category": "suspension", "origin": "Euro", "era": "all", "colors": ["#FDB813", "#004B87"], "compat": ["universal"]},
    {"name": "KW Suspensions", "category": "suspension", "origin": "Euro", "era": "all", "colors": ["#6D2077", "#FFF200"], "compat": ["universal"]},
    {"name": "Tanabe", "category": "suspension", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Eibach", "category": "suspension", "origin": "Euro", "era": "all", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},

    # Brakes
    {"name": "Endless", "category": "brakes", "origin": "JDM", "era": "all", "colors": ["#003399", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Project Mu", "category": "brakes", "origin": "JDM", "era": "all", "colors": ["#00A896", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Brembo", "category": "brakes", "origin": "Euro", "era": "all", "colors": ["#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "AP Racing", "category": "brakes", "origin": "Euro", "era": "all", "colors": ["#FFCC00", "#000000"], "compat": ["universal"]},
    {"name": "Winmax", "category": "brakes", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},

    # Wheels
    {"name": "Rays / Volk Racing", "category": "wheels", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Work Wheels", "category": "wheels", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#DE0029"], "compat": ["universal"]},
    {"name": "SSR (Speed Star)", "category": "wheels", "origin": "JDM", "era": "vintage", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},
    {"name": "Enkei", "category": "wheels", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#FFFFFF"], "compat": ["universal"]},
    {"name": "BBS", "category": "wheels", "origin": "Euro", "era": "all", "colors": ["#D4AF37", "#000000", "#DE0029"], "compat": ["universal"]},
    {"name": "WedsSport", "category": "wheels", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#FFD700"], "compat": ["universal"]},
    {"name": "Desmond Regamaster", "category": "wheels", "origin": "JDM", "era": "90s", "colors": ["#FFFFFF", "#DE0029"], "compat": ["universal"]},
    {"name": "RS Watanabe", "category": "wheels", "origin": "JDM", "era": "vintage", "kanji": "渡辺", "colors": ["#1A1A1A", "#DE0029"], "compat": ["universal"]},
    {"name": "Rotiform", "category": "wheels", "origin": "US", "era": "modern", "colors": ["#000000", "#FFFFFF"], "compat": ["universal"]},

    # Tires
    {"name": "Bridgestone Potenza", "category": "tires", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Yokohama Advan", "category": "tires", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},
    {"name": "Toyo Tires Proxes", "category": "tires", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Dunlop Direzza", "category": "tires", "origin": "JDM", "era": "all", "colors": ["#FFCC00", "#000000"], "compat": ["universal"]},
    {"name": "Falken Azenis", "category": "tires", "origin": "JDM", "era": "all", "colors": ["#00A896", "#028090", "#000000"], "compat": ["universal"]},

    # Lubricants & Fuel
    {"name": "Motul", "category": "lubricants", "origin": "Euro", "era": "all", "colors": ["#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Castrol", "category": "lubricants", "origin": "Euro", "era": "all", "colors": ["#008751", "#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Mobil 1", "category": "lubricants", "origin": "US", "era": "all", "colors": ["#003399", "#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Idemitsu", "category": "lubricants", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},
    {"name": "Pennzoil", "category": "lubricants", "origin": "US", "era": "90s", "colors": ["#FFCE00", "#DE0029", "#000000"], "compat": ["universal"]},
    {"name": "Wako's", "category": "lubricants", "origin": "JDM", "era": "all", "colors": ["#0055A5", "#FF007F", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Agip / Eni", "category": "lubricants", "origin": "Euro", "era": "vintage", "colors": ["#FED100", "#000000", "#DE0029"], "compat": ["universal"]},

    # Safety & Interior
    {"name": "Takata", "category": "safety", "origin": "JDM", "era": "all", "colors": ["#007F3E", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Bride", "category": "safety", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Recaro", "category": "safety", "origin": "Euro", "era": "all", "colors": ["#003399", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Sparco", "category": "safety", "origin": "Euro", "era": "all", "colors": ["#003399", "#FFFFFF"], "compat": ["universal"]},
    {"name": "OMP", "category": "safety", "origin": "Euro", "era": "all", "colors": ["#FFCE00", "#000000"], "compat": ["universal"]},
    {"name": "Sabelt", "category": "safety", "origin": "Euro", "era": "all", "colors": ["#FED100", "#003399"], "compat": ["universal"]},

    # Electronics & Lighting
    {"name": "PIAA", "category": "electronics", "origin": "JDM", "era": "all", "colors": ["#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Raybrig", "category": "electronics", "origin": "JDM", "era": "90s-00s", "colors": ["#00D2FF", "#0B1B3D", "#FF3B30"], "compat": ["universal"]},
    {"name": "NGK Spark Plugs", "category": "electronics", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Denso", "category": "electronics", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Defi", "category": "electronics", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#000000"], "compat": ["universal"]},

    # Legendary Title Sponsors
    {"name": "Calsonic", "category": "title", "origin": "JDM", "era": "90s-00s", "colors": ["#0055A5", "#FFFFFF"], "compat": ["Nissan"]},
    {"name": "Xanavi", "category": "title", "origin": "JDM", "era": "00s", "colors": ["#0055A5", "#DE0029", "#FFFFFF"], "compat": ["Nissan"]},
    {"name": "ZENT", "category": "title", "origin": "JDM", "era": "all", "colors": ["#DE0029", "#FFFFFF", "#C0C0C0"], "compat": ["Toyota"]},
    {"name": "Autobacs", "category": "title", "origin": "JDM", "era": "all", "colors": ["#FF6600", "#000000", "#FFFFFF"], "compat": ["universal"]},
    {"name": "JACCS", "category": "title", "origin": "JDM", "era": "90s", "colors": ["#009E49", "#FF6600", "#0072CE", "#ED1C24"], "compat": ["Honda"]},
    {"name": "Renown", "category": "title", "origin": "JDM", "era": "90s", "colors": ["#FF5F00", "#00783E", "#FFFFFF"], "compat": ["Mazda"]},
    {"name": "Marlboro", "category": "title", "origin": "Global", "era": "vintage", "colors": ["#DE0029", "#FFFFFF", "#000000"], "compat": ["universal"]},
    {"name": "Rothmans", "category": "title", "origin": "Global", "era": "vintage", "colors": ["#0C2340", "#FFFFFF", "#C5A059", "#DE0029"], "compat": ["universal"]},
    {"name": "Martini Racing", "category": "title", "origin": "Global", "era": "vintage", "colors": ["#00A3E0", "#00205B", "#DE0029", "#FFFFFF"], "compat": ["universal"]},
    {"name": "Gulf Oil", "category": "title", "origin": "Global", "era": "vintage", "colors": ["#7BA4D5", "#FF6B00", "#00205B"], "compat": ["universal"]}
]

def search_sponsors(query=None, category=None, origin=None, make=None):
    results = []
    q = query.lower() if query else None
    for s in SPONSORS:
        if q and q not in s["name"].lower() and q not in s.get("kanji", "").lower() and q not in s["category"]:
            continue
        if category and category.lower() != s["category"].lower():
            continue
        if origin and origin.lower() != s["origin"].lower():
            continue
        if make:
            compat = [c.lower() for c in s.get("compat", [])]
            if "universal" not in compat and make.lower() not in compat:
                continue
        results.append(s)
    return results

def generate_vertical_stack(make="universal", count=6):
    """
    Builds an authentic Tier 3 Vertical Sponsor Stack
    Ordered: Tuning -> Suspension -> Brakes -> Wheels -> Tires -> Fluid/Safety
    """
    categories = ["tuning", "suspension", "brakes", "wheels", "tires", "lubricants", "safety", "electronics"]
    stack = []
    for cat in categories:
        candidates = search_sponsors(category=cat, make=make)
        if candidates:
            stack.append(candidates[0])
        if len(stack) >= count:
            break
    return stack

def main():
    parser = argparse.ArgumentParser(description="Sponsor Vault: JDM & Motorsport Sponsor Database")
    parser.add_argument("--query", "-q", help="Search string")
    parser.add_argument("--category", "-c", help="Filter by category (tuning, suspension, brakes, wheels, tires, lubricants, safety, title)")
    parser.add_argument("--origin", "-o", help="Filter by origin (JDM, Euro, US, Global)")
    parser.add_argument("--make", "-m", help="Target vehicle make (Nissan, Toyota, Honda, Subaru, Mazda, universal)")
    parser.add_argument("--stack", action="store_true", help="Generate an authentic vertical door/fender sponsor stack")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if args.stack:
        stack = generate_vertical_stack(make=args.make or "universal")
        if args.json:
            print(json.dumps(stack, indent=2))
        else:
            print("\n=== AUTHENTIC TIER 3 VERTICAL SPONSOR STACK ===")
            print(f"Vehicle Make: {args.make or 'Universal'}\n")
            for i, item in enumerate(stack, 1):
                kanji_tag = f" ({item['kanji']})" if "kanji" in item else ""
                print(f"  {i}. [{item['category'].upper():12}] {item['name']}{kanji_tag}")
            print("\nRecommended Decal Color: Pure White (#FFFFFF) or High-Gloss Black (#000000)")
            print("Alignment: Left-aligned or Center-locked on front fender behind wheel arch.")
        return

    results = search_sponsors(query=args.query, category=args.category, origin=args.origin, make=args.make)
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"\nFound {len(results)} sponsors matching query:\n")
        for s in results:
            kanji_str = f" [{s['kanji']}]" if "kanji" in s else ""
            print(f" • {s['name']}{kanji_str} | Cat: {s['category']} | Origin: {s['origin']} | Colors: {', '.join(s['colors'])}")

if __name__ == "__main__":
    main()
