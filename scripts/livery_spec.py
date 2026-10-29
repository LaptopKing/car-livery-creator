"""
Livery Spec: Structured Project Specification & Validation Engine
Creates, validates, and exports standardized automotive livery project specifications.
"""

import sys
import os
import json
import argparse

SCHEMA = {
    "title": "str",
    "author": "str",
    "platform": ["GT7", "FH5", "AssettoCorsa", "iRacing", "PhysicalWrap"],
    "chassis": {
        "make": "str",
        "model": "str",
        "year": "int",
        "class": ["GT500", "GT300", "JTCC", "GroupA", "D1GP", "Kanjo", "KaidoRacer", "LeMans", "Street"]
    },
    "palette": {
        "dominant_60": {"name": "str", "hex": "str", "finish": "str"},
        "secondary_30": {"name": "str", "hex": "str", "finish": "str"},
        "accent_10": {"name": "str", "hex": "str", "finish": "str"}
    },
    "graphic_style": "str",
    "sponsors": {
        "title": "str",
        "secondary": "list",
        "vertical_stack": "list"
    },
    "hardware": {
        "wheels": "str",
        "wheel_color": "str",
        "tires": "str",
        "race_number": "str"
    },
    "aero_modification": ["oem_preserve", "aftermarket_real", "concept_radical"]
}

def create_default_spec(title, make, model, style="JGTC"):
    return {
        "title": title,
        "author": "Livery Architect",
        "platform": "GT7",
        "aero_modification": "oem_preserve",
        "chassis": {
            "make": make,
            "model": model,
            "year": 1999,
            "class": "GT500" if "GT-R" in model or "NSX" in model or "Supra" in model else "Street"
        },
        "palette": {
            "dominant_60": {"name": "Cobalt Blue", "hex": "#0055A5", "finish": "High Gloss"},
            "secondary_30": {"name": "Arctic White", "hex": "#FFFFFF", "finish": "Gloss"},
            "accent_10": {"name": "Amber Yellow", "hex": "#FFD200", "finish": "Gloss"}
        },
        "graphic_style": "wedge_split",
        "sponsors": {
            "title": "CALSONIC",
            "secondary": ["IMPUL", "BRIDGESTONE", "NISMO"],
            "vertical_stack": ["NISMO", "TEIN", "ENDLESS", "RAYS", "MOTUL"]
        },
        "hardware": {
            "wheels": "Impul Aerodisc",
            "wheel_color": "#FFFFFF",
            "tires": "Bridgestone Potenza",
            "race_number": "12"
        },
        "scrutineering": {
            "driver_name": "K. Hoshino",
            "country_flag": "JP",
            "blood_type": "A+",
            "tow_arrows": True,
            "kill_switch": True
        }
    }

def validate_spec(spec_data):
    errors = []
    if "title" not in spec_data:
        errors.append("Missing required field: 'title'")
    if "palette" not in spec_data or "dominant_60" not in spec_data["palette"]:
        errors.append("Missing required field: 'palette.dominant_60'")
    if "chassis" not in spec_data or "model" not in spec_data["chassis"]:
        errors.append("Missing required field: 'chassis.model'")
    return len(errors) == 0, errors

def export_markdown_summary(spec_data):
    c = spec_data.get("chassis", {})
    p = spec_data.get("palette", {})
    s = spec_data.get("sponsors", {})
    h = spec_data.get("hardware", {})
    sc = spec_data.get("scrutineering", {})

    md = f"""# Livery Specification: {spec_data.get('title', 'Untitled')}

**Author:** {spec_data.get('author', 'Unknown')} | **Target Platform:** {spec_data.get('platform', 'Universal')} | **Discipline:** {c.get('class', 'Custom')}

---

## 1. Vehicle Platform
- **Make & Model:** {c.get('make', '')} {c.get('model', '')} ({c.get('year', '')})
- **Class:** {c.get('class', 'Street')}
- **Aero Configuration:** GT Wing, Front Splitter, Canards, Vented Hood

---

## 2. Color Distribution (The 60-30-10 Velocity Rule)
- **60% Dominant Base:** `{p.get('dominant_60', {}).get('hex', '')}` — {p.get('dominant_60', {}).get('name', '')} ({p.get('dominant_60', {}).get('finish', '')})
- **30% Graphic Mass:** `{p.get('secondary_30', {}).get('hex', '')}` — {p.get('secondary_30', {}).get('name', '')} ({p.get('secondary_30', {}).get('finish', '')})
- **10% Accent Keyline:** `{p.get('accent_10', {}).get('hex', '')}` — {p.get('accent_10', {}).get('name', '')} ({p.get('accent_10', {}).get('finish', '')})
- **Graphic Shape Archetype:** `{spec_data.get('graphic_style', 'wedge_split')}`

---

## 3. Sponsor Hierarchy & Layout
- **Tier 1 (Title Billboard):** **{s.get('title', 'None')}** (Mid-door, Hood center, Wing blade)
- **Tier 2 (Co-Sponsors):** {', '.join(s.get('secondary', []))}
- **Tier 3 (Vertical Stack):**
{chr(10).join(['  ' + str(i) + '. ' + item for i, item in enumerate(s.get('vertical_stack', []), 1)])}

---

## 4. Hardware & Scrutineering
- **Race Number:** #{h.get('race_number', '00')}
- **Wheels:** {h.get('wheels', 'Racing Alloy')} ({h.get('wheel_color', '#FFFFFF')})
- **Tire Stencils:** {h.get('tires', 'Slick')}
- **Driver Tag:** {sc.get('driver_name', 'Driver')} ({sc.get('country_flag', '')}) [{sc.get('blood_type', '')}]
"""
    return md

def main():
    parser = argparse.ArgumentParser(description="Livery Project Spec Engine")
    parser.add_argument("--create", "-c", action="store_true", help="Create a new default spec")
    parser.add_argument("--title", default="JGTC Skyline Tribute", help="Livery project title")
    parser.add_argument("--make", default="Nissan", help="Vehicle manufacturer")
    parser.add_argument("--model", default="Skyline GT-R R34", help="Vehicle model")
    parser.add_argument("--validate", "-v", help="Validate an existing spec JSON file")
    parser.add_argument("--summary", "-s", help="Output a clean markdown summary from a JSON spec")
    parser.add_argument("--output", "-o", help="Output filepath")

    args = parser.parse_args()

    if args.create:
        spec = create_default_spec(args.title, args.make, args.model)
        out_path = args.output or "livery_spec.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(spec, f, indent=2)
        print(f"Created new livery spec: {out_path}")
        return

    if args.validate:
        with open(args.validate, "r", encoding="utf-8") as f:
            data = json.load(f)
        valid, errors = validate_spec(data)
        if valid:
            print(f"Spec '{args.validate}' is VALID.")
        else:
            print(f"Spec '{args.validate}' has ERRORS:")
            for e in errors:
                print(f"  • {e}")
        return

    if args.summary:
        with open(args.summary, "r", encoding="utf-8") as f:
            data = json.load(f)
        md = export_markdown_summary(data)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(md)
            print(f"Saved summary to {args.output}")
        else:
            print(md)
        return

    parser.print_help()

if __name__ == "__main__":
    main()
