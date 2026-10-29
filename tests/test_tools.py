"""
Automated Unit Tests for Car Livery Creator Suite
Verifies all CLI scripts, SVG generation, GT7 optimizer, palette contrast, and sponsor vault.
"""

import os
import sys
import unittest
import json

# Add scripts directory to path
SCRIPTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.insert(0, SCRIPTS_DIR)

from sponsor_vault import search_sponsors, generate_vertical_stack, SPONSORS
from palette_engine import contrast_ratio, PALETTES
from svg_car_generator import generate_car_svg, CHASSIS_CONFIGS
from gt7_svg_optimizer import clean_svg_text, GT7_MAX_BYTES
from livery_spec import create_default_spec, validate_spec, export_markdown_summary

class TestCarLiveryCreator(unittest.TestCase):

    def test_sponsor_vault_search(self):
        nismo = search_sponsors(query="NISMO")
        self.assertTrue(len(nismo) >= 1)
        self.assertEqual(nismo[0]["name"], "NISMO")

        # Nissan specific stack
        stack = generate_vertical_stack(make="Nissan", count=6)
        self.assertEqual(len(stack), 6)
        self.assertEqual(stack[0]["name"], "NISMO")

    def test_palette_engine_contrast(self):
        # White vs Black should be 21:1
        ratio = contrast_ratio("#FFFFFF", "#000000")
        self.assertAlmostEqual(ratio, 21.0, delta=0.5)

        # Calsonic Blue vs White
        calsonic_ratio = contrast_ratio("#0055A5", "#FFFFFF")
        self.assertTrue(calsonic_ratio >= 4.5)

        # Castrol Tom's Palette verification
        self.assertIn("castrol_toms", PALETTES)
        p = PALETTES["castrol_toms"]
        self.assertTrue(p["boundary_needed"])

    def test_svg_car_generation(self):
        for chassis in CHASSIS_CONFIGS.keys():
            svg = generate_car_svg(chassis_key=chassis, style="wedge_split")
            self.assertTrue(svg.startswith("<svg"))
            self.assertTrue(svg.endswith("</svg>"))
            self.assertIn(CHASSIS_CONFIGS[chassis]["name"].upper(), svg)

    def test_gt7_optimizer(self):
        sample_svg = """<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://inkscape.org">
            <!-- Test Comment -->
            <path d="M 12.34567 45.67891 Z"/>
        </svg>"""
        cleaned = clean_svg_text(sample_svg, precision=2)
        self.assertNotIn("<!-- Test Comment -->", cleaned)
        self.assertNotIn("xmlns:inkscape", cleaned)
        self.assertIn("12.35", cleaned)
        self.assertLessEqual(len(cleaned.encode("utf-8")), GT7_MAX_BYTES)

    def test_livery_spec_lifecycle(self):
        spec = create_default_spec("Test GT-R", "Nissan", "GT-R R34")
        valid, errors = validate_spec(spec)
        self.assertTrue(valid)
        self.assertEqual(len(errors), 0)

        md = export_markdown_summary(spec)
        self.assertIn("Test GT-R", md)
        self.assertIn("60% Dominant Base", md)

if __name__ == "__main__":
    unittest.main()
