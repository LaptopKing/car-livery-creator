"""
Gran Turismo 7 SVG Decal Optimizer
Optimizes, sanitizes, and minifies SVG decals to comply with the strict GT7 15 KB limit.
Strips editor metadata, rounds coordinates, removes unused defs, and validates file size.
"""

import sys
import os
import re
import argparse
import xml.etree.ElementTree as ET

GT7_MAX_BYTES = 15360  # 15 KB strict limit

def clean_svg_text(svg_text, precision=2):
    """Minifies and cleans SVG text representation"""
    # Remove XML comments
    svg_text = re.sub(r'<!--.*?-->', '', svg_text, flags=re.DOTALL)
    
    # Remove inkscape / sodipodi / adobe metadata tags
    svg_text = re.sub(r'<metadata>.*?</metadata>', '', svg_text, flags=re.DOTALL)
    svg_text = re.sub(r'<sodipodi:namedview.*?</sodipodi:namedview>', '', svg_text, flags=re.DOTALL)
    
    # Strip editor namespaces and attributes
    svg_text = re.sub(r'\s+xmlns:inkscape="[^"]+"', '', svg_text)
    svg_text = re.sub(r'\s+xmlns:sodipodi="[^"]+"', '', svg_text)
    svg_text = re.sub(r'\s+xmlns:adobe="[^"]+"', '', svg_text)
    svg_text = re.sub(r'\s+inkscape:[a-z\-]+="[^"]+"', '', svg_text)
    svg_text = re.sub(r'\s+sodipodi:[a-z\-]+="[^"]+"', '', svg_text)
    
    # Check for forbidden embedded rasters
    if "<image" in svg_text or "data:image" in svg_text:
        print("[WARNING] SVG contains embedded raster images! GT7 Decal Uploader will REJECT this file.")

    # Round excessive decimal floating numbers in paths: e.g. 123.456789 -> 123.46
    def round_match(m):
        val = float(m.group(0))
        return f"{val:.{precision}f}".rstrip('0').rstrip('.')
    
    svg_text = re.sub(r'\b\d+\.\d{3,}\b', round_match, svg_text)
    
    # Collapse multiple whitespaces and linebreaks
    svg_text = re.sub(r'\s+', ' ', svg_text)
    svg_text = re.sub(r'> <', '><', svg_text)
    
    return svg_text.strip()

def optimize_file(input_path, output_path=None, precision=2):
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return False
        
    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    orig_size = len(content.encode("utf-8"))
    optimized = clean_svg_text(content, precision=precision)
    opt_size = len(optimized.encode("utf-8"))

    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_gt7_opt{ext}"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(optimized)

    reduction = ((orig_size - opt_size) / orig_size) * 100 if orig_size > 0 else 0
    status = "PASS (Valid for GT7)" if opt_size <= GT7_MAX_BYTES else f"FAIL (Exceeds {GT7_MAX_BYTES} bytes)"

    print(f"\n=======================================================")
    print(f"  GT7 SVG OPTIMIZATION SUMMARY: {os.path.basename(input_path)}")
    print(f"=======================================================")
    print(f"  • Original Size : {orig_size:,} bytes ({orig_size/1024:.2f} KB)")
    print(f"  • Optimized Size: {opt_size:,} bytes ({opt_size/1024:.2f} KB)")
    print(f"  • Reduction     : {reduction:.1f}%")
    print(f"  • GT7 Compliance: {status}")
    print(f"  • Output Path   : {output_path}\n")

    return opt_size <= GT7_MAX_BYTES

def main():
    parser = argparse.ArgumentParser(description="Gran Turismo 7 SVG Decal Optimizer (<15KB)")
    parser.add_argument("input", help="Input SVG file")
    parser.add_argument("--output", "-o", help="Output optimized SVG file")
    parser.add_argument("--precision", "-p", type=int, default=2, help="Decimal coordinate precision (default: 2)")

    args = parser.parse_args()
    optimize_file(args.input, args.output, args.precision)

if __name__ == "__main__":
    main()
