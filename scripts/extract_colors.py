#!/usr/bin/env python3
"""
Extract dominant colors from a company logo and generate a presentation color palette.

Usage:
    python extract_colors.py <logo_path> [--json] [--css]

Outputs a harmonious 6-color palette (primary, secondary, accent, light, dark, neutral)
derived from the logo's dominant colors.
"""

import sys
import json
import argparse
from collections import Counter
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow --break-system-packages")
    sys.exit(1)


def rgb_to_hsl(r, g, b):
    """Convert RGB (0-255) to HSL (0-360, 0-100, 0-100)."""
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2.0

    if mx == mn:
        h = s = 0.0
    else:
        d = mx - mn
        s = d / (2.0 - mx - mn) if l > 0.5 else d / (mx + mn)
        if mx == r:
            h = (g - b) / d + (6.0 if g < b else 0.0)
        elif mx == g:
            h = (b - r) / d + 2.0
        else:
            h = (r - g) / d + 4.0
        h /= 6.0

    return round(h * 360), round(s * 100), round(l * 100)


def hsl_to_rgb(h, s, l):
    """Convert HSL (0-360, 0-100, 0-100) to RGB (0-255)."""
    h, s, l = h / 360.0, s / 100.0, l / 100.0

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    return round(r * 255), round(g * 255), round(b * 255)


def rgb_to_hex(r, g, b):
    """Convert RGB to hex string."""
    return f"#{r:02X}{g:02X}{b:02X}"


def hex_to_rgb(hex_str):
    """Convert hex string to RGB tuple."""
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))


def color_distance(c1, c2):
    """Simple Euclidean distance between two RGB colors."""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


def quantize_colors(image, num_colors=8):
    """Extract dominant colors using PIL's quantize method."""
    # Resize for performance
    img = image.copy()
    img.thumbnail((200, 200))

    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Quantize
    quantized = img.quantize(colors=num_colors, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()
    get_data = getattr(quantized, 'get_flattened_data', quantized.getdata)
    color_counts = Counter(get_data())

    # Build sorted color list (most frequent first)
    colors = []
    for idx, count in color_counts.most_common():
        r, g, b = palette[idx * 3], palette[idx * 3 + 1], palette[idx * 3 + 2]
        colors.append(((r, g, b), count))

    return colors


def filter_colors(colors, min_saturation=10, min_count_ratio=0.02):
    """Filter out near-white, near-black, and very desaturated colors."""
    total = sum(c for _, c in colors)
    filtered = []

    for (r, g, b), count in colors:
        h, s, l = rgb_to_hsl(r, g, b)

        # Skip very light (near white) or very dark (near black)
        if l > 95 or l < 5:
            continue

        # Skip very low saturation grays (unless they're a significant portion)
        if s < min_saturation and count / total < 0.3:
            continue

        # Skip colors that appear very rarely
        if count / total < min_count_ratio:
            continue

        filtered.append(((r, g, b), count))

    return filtered if filtered else colors[:3]  # Fallback to top 3 if everything filtered


def generate_palette(colors):
    """Generate a 6-color palette from extracted colors."""
    if not colors:
        # Fallback: generic tech palette
        return {
            "primary": "#6366F1",
            "secondary": "#818CF8",
            "accent": "#F59E0B",
            "light": "#F8FAFC",
            "dark": "#0F172A",
            "neutral": "#64748B"
        }

    # Pick the most dominant non-gray color as primary
    primary_rgb = colors[0][0]
    primary_h, primary_s, primary_l = rgb_to_hsl(*primary_rgb)

    # If primary is too desaturated, try next color
    for (r, g, b), _ in colors:
        h, s, l = rgb_to_hsl(r, g, b)
        if s > 20:
            primary_rgb = (r, g, b)
            primary_h, primary_s, primary_l = h, s, l
            break

    # Generate secondary: same hue, lighter
    secondary_l = min(primary_l + 15, 70)
    secondary_s = max(primary_s - 10, 30)
    secondary_rgb = hsl_to_rgb(primary_h, secondary_s, secondary_l)

    # Generate accent: complementary or triadic hue
    # Try to find a contrasting color in the extracted palette
    accent_rgb = None
    for (r, g, b), _ in colors[1:]:
        h, s, l = rgb_to_hsl(r, g, b)
        hue_diff = abs(h - primary_h)
        if hue_diff > 180:
            hue_diff = 360 - hue_diff
        # Want a color that's at least 60 degrees away and reasonably saturated
        if hue_diff > 60 and s > 25:
            accent_rgb = (r, g, b)
            break

    if accent_rgb is None:
        # Generate a complementary accent
        accent_h = (primary_h + 150) % 360
        accent_rgb = hsl_to_rgb(accent_h, min(primary_s + 10, 85), 55)

    # Light: very light tint of primary
    light_rgb = hsl_to_rgb(primary_h, max(primary_s - 40, 10), 96)

    # Dark: very dark shade of primary
    dark_rgb = hsl_to_rgb(primary_h, max(primary_s - 20, 15), 12)

    # Neutral: desaturated mid-tone of primary
    neutral_rgb = hsl_to_rgb(primary_h, 15, 50)

    # Hero-safe darkened primary: same hue/saturation but forced to 22% lightness
    # This ensures white text on hero gradients is always readable
    hero_primary_rgb = hsl_to_rgb(primary_h, max(primary_s - 10, 20), 22)

    # Near-black anchored to the brand hue for the gradient start
    hero_dark_rgb = hsl_to_rgb(primary_h, max(primary_s - 30, 10), 6)

    return {
        "primary": rgb_to_hex(*primary_rgb),
        "secondary": rgb_to_hex(*secondary_rgb),
        "accent": rgb_to_hex(*accent_rgb),
        "light": rgb_to_hex(*light_rgb),
        "dark": rgb_to_hex(*dark_rgb),
        "neutral": rgb_to_hex(*neutral_rgb),
        "hero_gradient_start": rgb_to_hex(*hero_dark_rgb),
        "hero_gradient_end": rgb_to_hex(*hero_primary_rgb),
    }


def palette_to_css(palette):
    """Convert palette dict to CSS custom properties."""
    lines = [":root {"]
    for name, color in palette.items():
        lines.append(f"  --color-{name}: {color};")

    # Add derived colors
    pr, pg, pb = hex_to_rgb(palette["primary"])
    lines.append(f"  --color-primary-alpha: rgba({pr}, {pg}, {pb}, 0.1);")
    lines.append(f"  --color-hero-gradient: linear-gradient(135deg, {palette['hero_gradient_start']} 0%, {palette['dark']} 40%, {palette['hero_gradient_end']} 100%);")
    lines.append(f"  --color-section-alt: {palette['light']};")
    lines.append(f"  --color-text: {palette['dark']};")
    lines.append(f"  --color-text-muted: {palette['neutral']};")
    lines.append("}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract brand colors from a logo")
    parser.add_argument("logo_path", help="Path to the logo image file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--css", action="store_true", help="Output as CSS custom properties")
    parser.add_argument("--colors", type=int, default=8, help="Number of colors to extract (default: 8)")
    args = parser.parse_args()

    logo_path = Path(args.logo_path)
    if not logo_path.exists():
        print(f"Error: File not found: {logo_path}")
        sys.exit(1)

    try:
        img = Image.open(logo_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    # Extract and filter colors
    raw_colors = quantize_colors(img, num_colors=args.colors)
    filtered = filter_colors(raw_colors)

    # Generate palette
    palette = generate_palette(filtered)

    # Output
    if args.css:
        print(palette_to_css(palette))
    elif args.json:
        print(json.dumps(palette, indent=2))
    else:
        # Default: print both
        print("Extracted Brand Palette")
        print("=" * 40)
        for name, color in palette.items():
            print(f"  {name:12s}  {color}")
        print()
        print("CSS Variables:")
        print(palette_to_css(palette))
        print()
        print("JSON:")
        print(json.dumps(palette, indent=2))


if __name__ == "__main__":
    main()
