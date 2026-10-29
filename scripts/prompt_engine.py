"""
Prompt Engine: Dual-Style Automotive Design & Livery Generator
Implements locked STYLE BLOCK + CONTENT BLOCK architecture inspired by:
- songxiaopeng529/story-picture (Style DNA prompt blocks)
- FriedDev/handdrawn-presentation-skill (Structured presentation & sketching conventions)

Provides two distinct rendering engines:
1. hand_drawn (DEFAULT): Traditional industrial automotive design studio concept sketch (Copic markers, Prismacolor, Posca paint pen, 3/4 rotated dynamic perspective).
2. realistic: Commercial automotive 3D studio / motorsport photography with complex geometric liveries and ray-traced reflections.

Provides three chassis/body modification tiers:
1. oem_preserve (DEFAULT): Strict 100% preservation of all factory body panels, hood, bumpers, trunk, mirrors, spoilers, and wheels.
2. aftermarket_real: Creative use of verified, real-world aftermarket tuner components (Chargespeed, C-West, Prodrive, JUN, Volk, Enkei).
3. concept_radical: Extreme creative freedom with futuristic, prototype, or fictional aerodynamic parts that don't exist yet.
"""

import sys
import json
import argparse

STYLE_HAND_DRAWN = """[STYLE BLOCK - AUTOMOTIVE DESIGN CONCEPT SKETCH]
Style: Authentic industrial automotive design concept sketch, drawn by hand on bleedproof layout marker paper in the traditional style of professional car design studios.
- Medium: Layered Copic alcohol markers (cool grays C1-C9, black, and vibrant saturated markers). Smooth marker gradients with characteristic subtle marker brush stroke textures.
- Linework: Confident, expressive felt-tip technical pen and ballpoint linework with visible light construction perspective lines and dynamic lineweight (thick, heavy occlusion shadow underneath the car and in the wheel wells; razor-sharp thin lines on highlights).
- Highlights: Sharp opaque white Posca paint pen and white gouache streaks along the shoulder crease, hood power bulge, and a diagonal glare streak across the tinted windshield.
- Composition: Dynamic rotated 3/4 front view, low aggressive three-point perspective, wide stance, wheels turned slightly to showcase the rim architecture. Fast marker shadow wash on the floor grounding the vehicle.
- Studio Details: Design studio presentation board aesthetic with subtle technical callout annotations in the margin, marker color swatch test blocks, and authentic hand-lettered titling."""

STYLE_REALISTIC = """[STYLE BLOCK - PHOTOREALISTIC MOTORSPORT PHOTOGRAPHY]
Style: Commercial automotive studio photography with dynamic 3/4 front three-point perspective.
- Lighting: Professional cinematic overhead studio softbox strip lighting casting crisp, long specular reflections along the vehicle's shoulder crease and hood contours, with dark asphalt floor reflections.
- Camera: Low 3/4 front angle, 35mm lens perspective, shallow depth of field, wheels turned slightly outward showing the deep rim concave and brake hardware.
- Realism: Ultra-sharp 8K detail on carbon weave textures, metallic paint flake, tire rubber compound grain with white tire stencils, and realistic glass refractions."""

AERO_BLOCKS = {
    "oem_preserve": """- CHASSIS & BODY PRESERVATION (STRICT OEM INVARIANT - DEFAULT):
  Do NOT modify, swap, or alter any body panels, engine hood, front/rear bumpers, trunk, side mirrors, OEM spoiler/wing, or wheels.
  The vehicle's sheet metal, aero, and wheels MUST strictly remain 100% factory OEM / as photographed.
  Apply livery graphics purely as a vinyl wrap over the unmodified factory bodywork.""",
    "aftermarket_real": """- CHASSIS & BODY SPEC (AUTHENTIC REAL-WORLD AFTERMARKET / OEM+):
  Enhanced with period-correct, verified real-world tuner body components (e.g. Chargespeed, C-West, Prodrive, Bomex, JUN, STI S201 aero, authentic aftermarket forged wheels like TE37/RPF1).
  All aero additions must represent existing, real-world manufactured parts matching the chassis era.""",
    "concept_radical": """- CHASSIS & BODY SPEC (RADICAL PROTOTYPE & CONCEPT AERO):
  Hyper-creative custom bodywork. Can feature prototype or fictional aerodynamic components that do not exist yet (custom bespoke widebody blisters, 3D-printed time-attack splitters, aggressive multi-element diffusers, active aero wings, sculpted vortex generators)."""
}

def build_prompt(car_name,
                 style_mode="hand_drawn",
                 aero_mode="oem_preserve",
                 angle="3/4 front dynamic perspective",
                 base_color="Liquid Platinum Silver",
                 secondary_graphics="Matte Obsidian Black knife-blade speed slashes",
                 accent_color="Fluorescent Velocity Neon Yellow (#FFE600)",
                 wheels="6-spoke motorsport gold wheels with Brembo calipers",
                 sponsors="Prodrive, STI Performance, Motul, Bilstein, Enkei",
                 number="55",
                 plate="LJC-055"):
    """Assembles a high-precision prompt using locked Style DNA"""
    style_block = STYLE_HAND_DRAWN if style_mode == "hand_drawn" else STYLE_REALISTIC
    aero_block = AERO_BLOCKS.get(aero_mode, AERO_BLOCKS["oem_preserve"])

    content_block = f"""[CONTENT BLOCK - VEHICLE & LIVERY SPECIFICATION]
Subject: {car_name}
Camera & Stance: Rotated {angle}, low aggressive stance, wide track, front wheels turned slightly.
Hardware: {wheels}.

{aero_block}

Livery Graphics (Intricate Multi-Layered Motorsport Design):
- Base (60%): {base_color}
- Secondary Graphics (30%): {secondary_graphics} carving dynamically through the doors and wrapping around the rear haunches/quarter panels.
- Velocity Accent (10%): {accent_color} razor-edge pinstripes outlining graphics, front lip splitter, and wing endplates.
- Sponsors & Decals: Authentic {sponsors}, windshield sun visor banner, and competition number "#{number}" roundel.
- Vehicle Badging: Clean license plate "{plate}".
"""
    return f"{style_block}\n\n{content_block}"

def main():
    parser = argparse.ArgumentParser(description="Generate locked style prompts for car liveries")
    parser.add_argument("--car", default="Subaru Impreza GF8 Sportswagon", help="Vehicle name")
    parser.add_argument("--mode", default="hand_drawn", choices=["hand_drawn", "realistic"], help="Render mode")
    parser.add_argument("--aero", default="oem_preserve", choices=["oem_preserve", "aftermarket_real", "concept_radical"], help="Chassis aero/body mode")
    parser.add_argument("--base", default="Liquid Platinum Silver", help="Base paint color")
    parser.add_argument("--sec", default="Matte Obsidian Black speed blades", help="Secondary graphic mass")
    parser.add_argument("--acc", default="Fluorescent Neon Yellow (#FFE600)", help="Accent color")
    parser.add_argument("--output", "-o", help="Output prompt file")

    args = parser.parse_args()
    prompt = build_prompt(
        car_name=args.car,
        style_mode=args.mode,
        aero_mode=args.aero,
        base_color=args.base,
        secondary_graphics=args.sec,
        accent_color=args.acc
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(prompt)
        print(f"Wrote prompt to {args.output}")
    else:
        print(prompt)

if __name__ == "__main__":
    main()
