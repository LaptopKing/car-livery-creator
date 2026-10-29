"""
SVG Car Generator: Modular Vector Blueprint & Livery Staging Engine
Generates clean, scalable SVG car profiles (GT-R, RX-7, Civic EG, Silvia S15, Porsche 911)
with customizable base paint, graphic wrap styles, wheels, sponsors, and aero kits.
"""

import sys
import os
import argparse
import json

CHASSIS_CONFIGS = {
    "gtr_r34": {
        "name": "Nissan Skyline GT-R (BNR34)",
        "viewBox": "0 0 1000 400",
        "body_path": "M 120 280 L 140 250 L 190 235 L 280 230 L 390 170 L 620 170 L 740 220 L 890 230 L 910 260 L 900 295 L 860 300 L 840 290 C 800 230 710 230 670 290 L 350 290 C 310 230 220 230 180 290 L 120 290 Z",
        "cabin_path": "M 395 175 L 615 175 L 725 220 L 290 230 Z",
        "wheel_front": (265, 290, 52),
        "wheel_rear": (755, 290, 52),
        "door_line": "M 420 180 L 410 285 M 630 180 L 620 285",
        "headlight": "M 130 255 L 180 245 L 175 260 Z",
        "taillight": "M 895 240 L 905 255 L 885 260 Z",
        "gt_wing": "M 840 210 L 870 145 L 940 145 L 920 215 M 865 145 L 850 210",
        "spoiler_y": 145
    },
    "rx7_fd": {
        "name": "Mazda RX-7 (FD3S)",
        "viewBox": "0 0 1000 400",
        "body_path": "M 110 285 L 130 260 L 210 240 L 320 235 L 420 175 C 520 160 620 170 710 205 L 860 225 L 895 255 L 890 295 L 850 295 C 820 235 730 235 695 295 L 345 295 C 315 235 225 235 190 295 L 110 295 Z",
        "cabin_path": "M 425 180 C 515 168 610 175 695 208 L 330 235 Z",
        "wheel_front": (270, 295, 50),
        "wheel_rear": (770, 295, 50),
        "door_line": "M 430 185 L 425 290 M 650 200 L 640 290",
        "headlight": "M 170 245 L 210 240 L 205 252 Z",
        "taillight": "M 875 235 L 890 248 L 870 255 Z",
        "gt_wing": "M 820 205 L 845 155 L 925 155 L 905 210 M 850 155 L 840 205",
        "spoiler_y": 155
    },
    "civic_eg": {
        "name": "Honda Civic (EG6 Hatchback)",
        "viewBox": "0 0 1000 400",
        "body_path": "M 120 290 L 135 265 L 210 245 L 320 240 L 400 170 L 680 170 L 730 200 L 790 265 L 785 295 L 745 295 C 715 235 625 235 595 295 L 345 295 C 315 235 225 235 190 295 L 120 295 Z",
        "cabin_path": "M 405 175 L 675 175 L 725 205 L 760 255 L 330 240 Z",
        "wheel_front": (270, 295, 48),
        "wheel_rear": (670, 295, 48),
        "door_line": "M 410 180 L 400 290 M 620 180 L 610 290",
        "headlight": "M 140 260 L 195 250 L 185 265 Z",
        "taillight": "M 770 255 L 785 268 L 768 275 Z",
        "gt_wing": "M 675 168 L 735 150 L 755 155 L 685 172",
        "spoiler_y": 150
    },
    "silvia_s15": {
        "name": "Nissan Silvia (S15 Spec-R)",
        "viewBox": "0 0 1000 400",
        "body_path": "M 115 285 L 135 255 L 200 238 L 305 232 L 405 172 L 635 172 L 735 215 L 875 228 L 900 260 L 890 295 L 850 295 C 815 235 725 235 690 295 L 345 295 C 315 235 225 235 190 295 L 115 295 Z",
        "cabin_path": "M 410 178 L 630 178 L 725 218 L 315 232 Z",
        "wheel_front": (270, 295, 50),
        "wheel_rear": (770, 295, 50),
        "door_line": "M 415 180 L 410 290 M 640 185 L 630 290",
        "headlight": "M 140 250 L 195 240 L 185 255 Z",
        "taillight": "M 880 238 L 895 250 L 878 258 Z",
        "gt_wing": "M 830 215 L 860 150 L 935 150 L 910 220 M 855 150 L 845 215",
        "spoiler_y": 150
    },
    "porsche_911": {
        "name": "Porsche 911 (964 / 993 Silhouette)",
        "viewBox": "0 0 1000 400",
        "body_path": "M 110 290 L 130 260 L 220 235 L 340 230 L 440 165 C 540 155 640 170 760 215 L 880 250 L 900 275 L 890 295 L 845 295 C 815 230 725 230 690 295 L 345 295 C 315 230 225 230 190 295 L 110 295 Z",
        "cabin_path": "M 445 170 C 540 160 630 175 745 218 L 350 230 Z",
        "wheel_front": (270, 295, 52),
        "wheel_rear": (770, 295, 52),
        "door_line": "M 450 175 L 440 290 M 650 195 L 640 290",
        "headlight": "M 180 235 A 15 15 0 1 1 200 255 Z",
        "taillight": "M 885 255 L 898 268 L 875 272 Z",
        "gt_wing": "M 770 210 L 800 135 L 905 135 L 880 245 M 810 135 L 795 210",
        "spoiler_y": 135
    },
    "impreza_gf8": {
        "name": "Subaru Impreza GF8 Sportswagon",
        "viewBox": "0 0 1000 400",
        "body_path": "M 105 288 L 115 262 L 142 248 L 190 242 L 250 238 L 275 229 L 305 233 L 380 233 L 452 172 L 722 172 L 750 165 L 762 169 L 742 178 L 798 228 L 826 235 L 838 252 L 846 285 L 836 295 L 795 295 C 765 232 675 232 645 295 L 345 295 C 315 232 225 232 195 295 L 105 295 Z",
        "cabin_path": "M 385 228 L 454 176 L 718 176 L 782 228 Z",
        "wheel_front": (270, 295, 50),
        "wheel_rear": (720, 295, 50),
        "door_line": "M 454 176 L 445 290 M 535 176 L 530 290 M 625 176 L 620 290 M 715 176 L 710 230 M 195 262 L 835 262",
        "headlight": "M 135 248 L 185 243 L 180 258 L 138 258 Z",
        "taillight": "M 822 238 L 836 248 L 826 260 Z",
        "gt_wing": "M 708 174 L 755 163 L 762 168 L 720 178 Z",
        "spoiler_y": 163
    }
}

def generate_wheel_svg(cx, cy, r, style="te37", wheel_color="#D4AF37", tire_brand="POTENZA"):
    """Generates an authentic motorsport wheel assembly (Tire + Rim + Hardware)"""
    tire_r = r + 16
    svg = f"""
    <!-- Wheel Assembly at ({cx}, {cy}) -->
    <g class="wheel">
        <!-- Rubber Tire -->
        <circle cx="{cx}" cy="{cy}" r="{tire_r}" fill="#18181A" stroke="#0D0D0F" stroke-width="4"/>
        <circle cx="{cx}" cy="{cy}" r="{r + 6}" fill="none" stroke="#252528" stroke-width="1.5" stroke-dasharray="8 4"/>
        <!-- Tire Lettering Stencil -->
        <path id="tire_curve_{cx}" d="M {cx - r - 8} {cy} A {r + 8} {r + 8} 0 0 1 {cx + r + 8} {cy}" fill="none"/>
        <text font-family="'Impact', 'Arial Black', sans-serif" font-size="9" font-weight="bold" fill="#F0F0F0" letter-spacing="2">
            <textPath href="#tire_curve_{cx}" startOffset="50%" text-anchor="middle">
                {tire_brand}
            </textPath>
        </text>
        <!-- Rim Outer Lip -->
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="#111111" stroke="#444444" stroke-width="2.5"/>
        <circle cx="{cx}" cy="{cy}" r="{r - 4}" fill="{wheel_color}" stroke="#000000" stroke-width="1.5"/>
        <circle cx="{cx}" cy="{cy}" r="{r - 12}" fill="#0A0A0A"/>
    """

    if style == "turbofan":
        # White / Colored Aerodisc with central locking nut
        svg += f"""
        <circle cx="{cx}" cy="{cy}" r="{r - 5}" fill="{wheel_color}" stroke="#222" stroke-width="1"/>
        <circle cx="{cx}" cy="{cy}" r="{r - 14}" fill="none" stroke="#DE0029" stroke-width="2"/>
        <text x="{cx}" y="{cy - 16}" font-family="Arial, sans-serif" font-size="8" font-weight="900" fill="#111" text-anchor="middle">IMPUL</text>
        <circle cx="{cx}" cy="{cy}" r="10" fill="#DE0029" stroke="#880010" stroke-width="1.5"/>
        <circle cx="{cx}" cy="{cy}" r="4" fill="#FFD700"/>
        """
    elif style == "mesh":
        # Classic BBS Multi-spoke Mesh
        svg += f"""
        <circle cx="{cx}" cy="{cy}" r="{r - 6}" fill="none" stroke="{wheel_color}" stroke-width="3" stroke-dasharray="4 2"/>
        <circle cx="{cx}" cy="{cy}" r="{r - 16}" fill="none" stroke="{wheel_color}" stroke-width="2" stroke-dasharray="3 3"/>
        <circle cx="{cx}" cy="{cy}" r="9" fill="#000" stroke="#FFD700" stroke-width="1.5"/>
        <text x="{cx}" y="{cy + 3}" font-family="Arial, sans-serif" font-size="7" font-weight="bold" fill="#FFD700" text-anchor="middle">BBS</text>
        """
    else:
        # Iconic 6-Spoke TE37 Style
        svg += f"""
        <!-- 6 Spokes -->
        <g stroke="{wheel_color}" stroke-width="7" stroke-linecap="round">
            <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - r + 8}"/>
            <line x1="{cx}" y1="{cy}" x2="{cx + int(r*0.86)}" y2="{cy - int(r*0.5) + 4}"/>
            <line x1="{cx}" y1="{cy}" x2="{cx + int(r*0.86)}" y2="{cy + int(r*0.5) - 4}"/>
            <line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy + r - 8}"/>
            <line x1="{cx}" y1="{cy}" x2="{cx - int(r*0.86)}" y2="{cy + int(r*0.5) - 4}"/>
            <line x1="{cx}" y1="{cy}" x2="{cx - int(r*0.86)}" y2="{cy - int(r*0.5) + 4}"/>
        </g>
        <!-- Center Hub & 5 Lugs -->
        <circle cx="{cx}" cy="{cy}" r="12" fill="#111111" stroke="#333" stroke-width="1.5"/>
        <circle cx="{cx}" cy="{cy}" r="5" fill="#0055A5"/>
        <circle cx="{cx}" cy="{cy - 7}" r="1.8" fill="#FFF"/>
        <circle cx="{cx + 7}" cy="{cy - 2}" r="1.8" fill="#FFF"/>
        <circle cx="{cx + 4}" cy="{cy + 6}" r="1.8" fill="#FFF"/>
        <circle cx="{cx - 4}" cy="{cy + 6}" r="1.8" fill="#FFF"/>
        <circle cx="{cx - 7}" cy="{cy - 2}" r="1.8" fill="#FFF"/>
        """
    svg += "</g>\n"
    return svg

def generate_graphic_overlay(style, chassis, sec_color="#008751", acc_color="#DE0029", num="36"):
    """Builds specific livery shape grammar over the chassis"""
    overlay = ""
    if style == "wedge_split":
        # Aggressive JGTC forward wedge rising from front bumper up through C-pillar
        overlay += f"""
        <g id="livery_wedge">
            <path d="M 120 280 L 350 280 L 890 230 L 910 260 L 900 295 L 670 295 L 350 295 L 120 295 Z" fill="{sec_color}" opacity="0.95"/>
            <polygon points="280,230 910,180 910,230 600,230" fill="{acc_color}" opacity="0.9"/>
            <line x1="280" y1="230" x2="910" y2="180" stroke="#FFFFFF" stroke-width="4"/>
        </g>
        """
    elif style == "scallop_drift":
        # Falken style interlocking scallops
        overlay += f"""
        <g id="livery_scallops">
            <path d="M 270 230 C 450 180 500 300 700 220 L 910 220 L 910 295 L 670 295 C 600 250 450 290 270 230 Z" fill="{sec_color}"/>
            <path d="M 380 240 C 520 200 580 300 780 230 L 910 230 L 910 295 L 750 295 C 680 260 550 290 380 240 Z" fill="{acc_color}"/>
        </g>
        """
    elif style == "advan_slash":
        # Yokohama Advan aggressive diagonal red slashes
        overlay += f"""
        <g id="livery_advan">
            <polygon points="520,170 590,170 470,295 400,295" fill="{sec_color}"/>
            <polygon points="620,170 690,170 570,295 500,295" fill="{sec_color}"/>
            <polygon points="720,180 790,200 670,295 600,295" fill="{sec_color}"/>
            <polygon points="810,210 880,225 770,295 700,295" fill="{sec_color}"/>
        </g>
        """
    elif style == "kanjo_meatball":
        # Osaka Loop Line Clubman style
        overlay += f"""
        <g id="livery_kanjo">
            <!-- White Door Meatball -->
            <circle cx="520" cy="235" r="45" fill="#FFFFFF" stroke="#111111" stroke-width="3"/>
            <text x="520" y="252" font-family="'Impact', 'Arial Black', sans-serif" font-size="48" font-weight="bold" fill="#111111" text-anchor="middle">{num}</text>
            <!-- Rocker Decal Strip -->
            <rect x="350" y="275" width="280" height="15" fill="{sec_color}"/>
            <text x="490" y="286" font-family="sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">TEMPLE RACING 浪花環状</text>
        </g>
        """
    elif style == "two_tone_horizontal":
        # Classic 80s/90s S13 two-tone or touring car horizontal split
        overlay += f"""
        <g id="livery_twotone">
            <path d="M 120 255 L 905 255 L 890 295 L 120 295 Z" fill="{sec_color}"/>
            <line x1="120" y1="255" x2="905" y2="255" stroke="{acc_color}" stroke-width="3"/>
        </g>
        """
    return overlay

def generate_car_svg(chassis_key="gtr_r34",
                     base_color="#FFFFFF",
                     sec_color="#008751",
                     acc_color="#DE0029",
                     style="wedge_split",
                     title_sponsor="CASTROL",
                     sub_sponsor="TOM'S",
                     wheel_style="te37",
                     wheel_color="#D4AF37",
                     tire_brand="POTENZA",
                     number="36",
                     has_wing=True):
    """Assembles the complete master SVG file"""
    chassis = CHASSIS_CONFIGS.get(chassis_key, CHASSIS_CONFIGS["gtr_r34"])
    fw_x, fw_y, fw_r = chassis["wheel_front"]
    rw_x, rw_y, rw_r = chassis["wheel_rear"]

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{chassis['viewBox']}" width="1000" height="400">
    <defs>
        <!-- Gradients & Shadows -->
        <linearGradient id="groundShadow" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#000000" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
        </linearGradient>
        <linearGradient id="glassGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1A2530"/>
            <stop offset="70%" stop-color="#2D3E50"/>
            <stop offset="100%" stop-color="#141E28"/>
        </linearGradient>
        <clipPath id="bodyClip">
            <path d="{chassis['body_path']}"/>
        </clipPath>
    </defs>

    <!-- Studio / Track Backdrop -->
    <rect width="100%" height="100%" fill="#141417"/>
    <line x1="0" y1="345" x2="1000" y2="345" stroke="#252528" stroke-width="2"/>

    <!-- Ground Contact Shadow -->
    <ellipse cx="500" cy="350" rx="440" ry="18" fill="url(#groundShadow)"/>

    <!-- GT Wing (Rear) -->
    {"<path d='" + chassis['gt_wing'] + "' fill='#0A0A0A' stroke='#222' stroke-width='2'/>" if has_wing else ""}

    <!-- BASE CAR BODY (Clipped for liveries) -->
    <g id="car_assembly">
        <!-- Main Painted Shell -->
        <path d="{chassis['body_path']}" fill="{base_color}" stroke="#1A1A1A" stroke-width="3"/>

        <!-- Livery Graphics (Clipped to body) -->
        <g clip-path="url(#bodyClip)">
            {generate_graphic_overlay(style, chassis, sec_color, acc_color, number)}

            <!-- Mid-Door Title Sponsor Billboard -->
            <g transform="translate(510, 248)">
                <text x="0" y="0" font-family="'Impact', 'Arial Black', sans-serif" font-size="34" font-weight="900" 
                      fill="#FFFFFF" stroke="#000000" stroke-width="2" text-anchor="middle" letter-spacing="1">
                    {title_sponsor}
                </text>
                <text x="0" y="18" font-family="sans-serif" font-size="12" font-weight="bold" 
                      fill="{acc_color}" text-anchor="middle" letter-spacing="3">
                    {sub_sponsor}
                </text>
            </g>

            <!-- Tier 3 Vertical Sponsor Stack (Front Fender) -->
            <g transform="translate(345, 235)" font-family="sans-serif" font-size="7" font-weight="900" fill="#FFFFFF">
                <text x="0" y="0">NISMO</text>
                <text x="0" y="9">TEIN</text>
                <text x="0" y="18">ENDLESS</text>
                <text x="0" y="27">RAYS</text>
                <text x="0" y="36">MOTUL</text>
            </g>

            <!-- Competition Number Box (If not kanjo meatball) -->
            {f'''<g transform="translate(425, 220)">
                <rect width="36" height="42" fill="#FFFFFF" stroke="#000" stroke-width="2" rx="3"/>
                <rect x="0" y="0" width="36" height="10" fill="{acc_color}" rx="2"/>
                <text x="18" y="34" font-family="'Impact', sans-serif" font-size="24" font-weight="bold" fill="#111" text-anchor="middle">{number}</text>
            </g>''' if style != "kanjo_meatball" else ''}

            <!-- Scrutineering Details: Tow Hook Arrow -->
            <g transform="translate(130, 280)">
                <polygon points="0,0 8,4 0,8" fill="#FF1744"/>
                <text x="11" y="6" font-family="monospace" font-size="6" font-weight="bold" fill="#FF1744">TOW</text>
            </g>
        </g>

        <!-- Cabin Greenhouse / Windows -->
        <path d="{chassis['cabin_path']}" fill="url(#glassGradient)" stroke="#111111" stroke-width="2.5"/>

        <!-- A/B/C Pillars & Door Cutlines -->
        <path d="{chassis['door_line']}" fill="none" stroke="#1A1A1A" stroke-width="2.5"/>

        <!-- Aerodynamic Lower Rocker Splitter -->
        <path d="M 110 295 L 900 295 L 890 302 L 115 302 Z" fill="#080808"/>

        <!-- Headlight & Taillight Units -->
        <path d="{chassis['headlight']}" fill="#FFFDE7" stroke="#333" stroke-width="1"/>
        <path d="{chassis['taillight']}" fill="#D50000" stroke="#333" stroke-width="1"/>
    </g>

    <!-- Wheels (Drawn above body) -->
    {generate_wheel_svg(fw_x, fw_y, fw_r, style=wheel_style, wheel_color=wheel_color, tire_brand=tire_brand)}
    {generate_wheel_svg(rw_x, rw_y, rw_r, style=wheel_style, wheel_color=wheel_color, tire_brand=tire_brand)}

    <!-- Spec Banner Header -->
    <text x="30" y="40" font-family="'Impact', sans-serif" font-size="20" fill="#E0E0E0" letter-spacing="1">
        CAR LIVERY CREATOR // {chassis['name'].upper()}
    </text>
    <text x="30" y="60" font-family="monospace" font-size="11" fill="#888888">
        STYLE: {style.upper()} | BASE: {base_color} | ACCENT: {acc_color} | SPONSOR: {title_sponsor} #{number}
    </text>
</svg>"""
    return svg

def main():
    parser = argparse.ArgumentParser(description="SVG Car Profile & Livery Generator")
    parser.add_argument("--chassis", "-c", default="gtr_r34", choices=list(CHASSIS_CONFIGS.keys()), help="Target chassis model")
    parser.add_argument("--style", "-s", default="wedge_split", choices=["wedge_split", "scallop_drift", "advan_slash", "kanjo_meatball", "two_tone_horizontal"], help="Graphic style")
    parser.add_argument("--base", default="#FFFFFF", help="Base paint HEX color")
    parser.add_argument("--secondary", default="#008751", help="Secondary graphic HEX color")
    parser.add_argument("--accent", default="#DE0029", help="Accent HEX color")
    parser.add_argument("--sponsor", default="CASTROL", help="Primary title sponsor text")
    parser.add_argument("--sub-sponsor", default="TOM'S", help="Secondary subtitle sponsor text")
    parser.add_argument("--number", default="36", help="Competition race number")
    parser.add_argument("--wheel", default="te37", choices=["te37", "turbofan", "mesh"], help="Wheel style")
    parser.add_argument("--wheel-color", default="#D4AF37", help="Wheel color HEX")
    parser.add_argument("--tire", default="POTENZA", help="Tire brand lettering")
    parser.add_argument("--output", "-o", default="car_livery.svg", help="Output SVG filepath")

    args = parser.parse_args()

    svg_content = generate_car_svg(
        chassis_key=args.chassis,
        base_color=args.base,
        sec_color=args.secondary,
        acc_color=args.accent,
        style=args.style,
        title_sponsor=args.sponsor,
        sub_sponsor=args.sub_sponsor,
        wheel_style=args.wheel,
        wheel_color=args.wheel_color,
        tire_brand=args.tire,
        number=args.number
    )

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Generated car livery SVG: {args.output}")

if __name__ == "__main__":
    main()
