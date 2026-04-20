#!/usr/bin/env python3
"""
Extract visual style from a website URL and generate a presentation style guide.

Fetches the page HTML+CSS, then extracts:
  - Color palette (background, text, accent, border colors)
  - Typography (font families, sizes, weights)
  - Layout characteristics (spacing, border-radius, shadow style)
  - Overall vibe (minimal, bold, corporate, playful, etc.)

Usage:
    python extract_style.py <url> [--json] [--css]

Requires: pip install requests beautifulsoup4 cssutils
"""

import sys
import json
import re
import argparse
from collections import Counter
from urllib.parse import urljoin

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests --break-system-packages")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 is required. Install with: pip install beautifulsoup4 --break-system-packages")
    sys.exit(1)


def hex_normalize(color_str):
    """Normalize a color string to 6-digit hex if possible."""
    color_str = color_str.strip().lower()

    # Already hex
    if re.match(r'^#[0-9a-f]{6}$', color_str):
        return color_str
    if re.match(r'^#[0-9a-f]{3}$', color_str):
        return '#' + ''.join(c * 2 for c in color_str[1:])

    # rgb() / rgba()
    m = re.match(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)', color_str)
    if m:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return f'#{r:02x}{g:02x}{b:02x}'

    # Named colors (common ones)
    named = {
        'white': '#ffffff', 'black': '#000000', 'red': '#ff0000',
        'blue': '#0000ff', 'green': '#008000', 'gray': '#808080',
        'grey': '#808080', 'orange': '#ffa500', 'purple': '#800080',
        'navy': '#000080', 'teal': '#008080', 'transparent': None,
        'inherit': None, 'initial': None, 'currentcolor': None,
    }
    return named.get(color_str)


def hex_to_hsl(hex_color):
    """Convert hex to HSL."""
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16) / 255, int(hex_color[2:4], 16) / 255, int(hex_color[4:6], 16) / 255
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        h = s = 0
    else:
        d = mx - mn
        s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
        if mx == r: h = (g - b) / d + (6 if g < b else 0)
        elif mx == g: h = (b - r) / d + 2
        else: h = (r - g) / d + 4
        h /= 6
    return round(h * 360), round(s * 100), round(l * 100)


def classify_color(hex_color):
    """Classify a color by its role (dark, light, mid, accent)."""
    h, s, l = hex_to_hsl(hex_color)
    if l > 92: return 'near-white'
    if l < 8: return 'near-black'
    if l > 80: return 'light'
    if l < 20: return 'dark'
    if s > 50: return 'accent'
    if s < 15: return 'neutral'
    return 'mid'


def extract_colors_from_css(css_text):
    """Pull all color values from CSS text."""
    colors = []

    # Match hex colors
    for m in re.finditer(r'#[0-9a-fA-F]{3,6}\b', css_text):
        c = hex_normalize(m.group())
        if c: colors.append(c)

    # Match rgb/rgba
    for m in re.finditer(r'rgba?\([^)]+\)', css_text):
        c = hex_normalize(m.group())
        if c: colors.append(c)

    return colors


def extract_fonts_from_css(css_text):
    """Pull font-family declarations from CSS."""
    fonts = []
    for m in re.finditer(r'font-family\s*:\s*([^;}{]+)', css_text, re.IGNORECASE):
        family = m.group(1).strip().strip('"').strip("'")
        # Take the first font in the stack
        first = family.split(',')[0].strip().strip('"').strip("'")
        if first and first.lower() not in ('inherit', 'initial', 'sans-serif', 'serif', 'monospace', 'system-ui'):
            fonts.append(first)
    return fonts


def extract_border_radius(css_text):
    """Find common border-radius values."""
    radii = []
    for m in re.finditer(r'border-radius\s*:\s*([^;}{]+)', css_text, re.IGNORECASE):
        val = m.group(1).strip()
        # Only keep concrete values (px, rem, em, %) — skip CSS variables
        if not val.startswith('var('):
            radii.append(val)
    return radii


def extract_shadows(css_text):
    """Check if the site uses box shadows."""
    shadow_count = len(re.findall(r'box-shadow\s*:', css_text, re.IGNORECASE))
    return shadow_count


def classify_vibe(colors_by_role, fonts, has_shadows, radii):
    """Attempt to classify the overall design vibe."""
    vibes = []

    # Color-based
    dark_count = sum(1 for c in colors_by_role if colors_by_role[c] in ('dark', 'near-black'))
    light_count = sum(1 for c in colors_by_role if colors_by_role[c] in ('light', 'near-white'))
    accent_count = sum(1 for c in colors_by_role if colors_by_role[c] == 'accent')

    if dark_count > light_count:
        vibes.append('dark-mode')
    if accent_count >= 3:
        vibes.append('colorful')
    elif accent_count <= 1:
        vibes.append('minimal')

    # Radius-based
    large_radii = sum(1 for r in radii if any(v in r for v in ('20', '24', '32', '50%', '999', '9999')))
    if large_radii > 2:
        vibes.append('rounded')
    no_radii = sum(1 for r in radii if r in ('0', '0px'))
    if no_radii > len(radii) * 0.5 and len(radii) > 3:
        vibes.append('sharp')

    # Shadow-based
    if has_shadows > 5:
        vibes.append('elevated')
    elif has_shadows == 0:
        vibes.append('flat')

    # Font-based
    serif_fonts = [f for f in fonts if any(s in f.lower() for s in ('georgia', 'times', 'serif', 'garamond', 'palatino', 'merriweather', 'playfair'))]
    if serif_fonts:
        vibes.append('editorial')

    if not vibes:
        vibes.append('modern')

    return vibes


def fetch_page(url):
    """Fetch page HTML and inline + linked CSS."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; gg-ppt style extractor)'
    }
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')

    # Collect all CSS
    all_css = []

    # Inline styles from <style> tags
    for style_tag in soup.find_all('style'):
        if style_tag.string:
            all_css.append(style_tag.string)

    # Inline styles from style= attributes
    for tag in soup.find_all(style=True):
        all_css.append(tag['style'])

    # Linked stylesheets (fetch first 3 to avoid being too slow)
    link_count = 0
    for link in soup.find_all('link', rel='stylesheet'):
        if link_count >= 3:
            break
        href = link.get('href')
        if href:
            css_url = urljoin(url, href)
            try:
                css_resp = requests.get(css_url, headers=headers, timeout=10)
                if css_resp.status_code == 200:
                    all_css.append(css_resp.text)
                    link_count += 1
            except Exception:
                pass

    return soup, '\n'.join(all_css)


def build_palette(color_counts, colors_by_role):
    """Build a 6-color palette from extracted colors."""
    # Group by role
    darks = [(c, n) for c, n in color_counts if colors_by_role.get(c) == 'dark']
    lights = [(c, n) for c, n in color_counts if colors_by_role.get(c) == 'light']
    accents = [(c, n) for c, n in color_counts if colors_by_role.get(c) == 'accent']
    mids = [(c, n) for c, n in color_counts if colors_by_role.get(c) == 'mid']
    neutrals = [(c, n) for c, n in color_counts if colors_by_role.get(c) == 'neutral']

    # Pick most common from each group
    primary = (accents[0][0] if accents else (mids[0][0] if mids else '#3B82F6'))
    secondary = (accents[1][0] if len(accents) > 1 else (mids[0][0] if mids else '#64748B'))
    accent = (accents[2][0] if len(accents) > 2 else (accents[0][0] if accents else '#F59E0B'))
    # Avoid primary == secondary == accent
    if secondary == primary and mids:
        secondary = mids[0][0]
    if accent == primary:
        accent = '#F59E0B' if primary != '#F59E0B' else '#EF4444'

    light = lights[0][0] if lights else '#F8FAFC'
    dark = darks[0][0] if darks else '#0F172A'
    neutral = neutrals[0][0] if neutrals else '#64748B'

    return {
        'primary': primary,
        'secondary': secondary,
        'accent': accent,
        'light': light,
        'dark': dark,
        'neutral': neutral,
    }


def _hsl_to_hex(h, s, l):
    """HSL (0-360, 0-100, 0-100) to hex."""
    h, s, l = h / 360, s / 100, l / 100
    if s == 0:
        r = g = b = l
    else:
        def f(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p
        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r, g, b = f(p, q, h + 1/3), f(p, q, h), f(p, q, h - 1/3)
    return f'#{round(r*255):02x}{round(g*255):02x}{round(b*255):02x}'


def extract_style(url):
    """Main extraction: fetch URL and extract full style profile."""
    soup, css_text = fetch_page(url)

    # Colors
    raw_colors = extract_colors_from_css(css_text)
    color_counts = Counter(raw_colors).most_common(50)

    # Classify each unique color
    colors_by_role = {}
    for c, _ in color_counts:
        colors_by_role[c] = classify_color(c)

    # Filter out near-white and near-black for palette building (but keep them for light/dark)
    palette = build_palette(color_counts, colors_by_role)

    # Fonts
    fonts = extract_fonts_from_css(css_text)
    font_counts = Counter(fonts).most_common(5)
    top_fonts = [f for f, _ in font_counts]

    # Border radius
    radii = extract_border_radius(css_text)
    radius_counts = Counter(radii).most_common(3)
    common_radius = radius_counts[0][0] if radius_counts else '8px'

    # Shadows
    shadow_count = extract_shadows(css_text)

    # Vibe
    vibes = classify_vibe(colors_by_role, top_fonts, shadow_count, radii)

    # Build hero gradient from palette (safe for white text)
    h, s, l = hex_to_hsl(palette['primary'])
    hero_start = _hsl_to_hex(h, max(s - 30, 10), 6)
    hero_end = _hsl_to_hex(h, max(s - 10, 20), 22)

    return {
        'source_url': url,
        'palette': palette,
        'hero_gradient': {
            'start': hero_start,
            'end': hero_end,
        },
        'typography': {
            'fonts': top_fonts if top_fonts else ['system-ui', 'sans-serif'],
            'heading_font': top_fonts[0] if top_fonts else 'system-ui',
            'body_font': top_fonts[1] if len(top_fonts) > 1 else (top_fonts[0] if top_fonts else 'system-ui'),
        },
        'shape': {
            'border_radius': common_radius,
            'has_shadows': shadow_count > 3,
            'shadow_style': 'elevated' if shadow_count > 3 else 'flat',
        },
        'vibe': vibes,
        'top_colors': [{'color': c, 'count': n, 'role': colors_by_role[c]} for c, n in color_counts[:15]],
    }


def palette_to_css(result):
    """Convert extracted style to CSS custom properties."""
    p = result['palette']
    t = result['typography']
    s = result['shape']
    hg = result['hero_gradient']

    lines = [
        f"/* Style extracted from: {result['source_url']} */",
        f"/* Vibe: {', '.join(result['vibe'])} */",
        "",
        ":root {",
        f"  /* Colors */",
        f"  --color-primary: {p['primary']};",
        f"  --color-secondary: {p['secondary']};",
        f"  --color-accent: {p['accent']};",
        f"  --color-light: {p['light']};",
        f"  --color-dark: {p['dark']};",
        f"  --color-neutral: {p['neutral']};",
        f"",
        f"  /* Hero (safe for white text) */",
        f"  --color-hero-gradient: linear-gradient(135deg, {hg['start']} 0%, {p['dark']} 40%, {hg['end']} 100%);",
        f"",
        f"  /* Typography */",
        f"  --font-display: '{t['heading_font']}', system-ui, sans-serif;",
        f"  --font-body: '{t['body_font']}', system-ui, sans-serif;",
        f"",
        f"  /* Shape */",
        f"  --radius: {s['border_radius']};",
        f"  --shadow: {'0 4px 20px rgba(0,0,0,0.08)' if s['has_shadows'] else 'none'};",
        "}",
    ]
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description="Extract visual style from a website")
    parser.add_argument("url", help="URL to extract style from")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--css", action="store_true", help="Output as CSS custom properties")
    args = parser.parse_args()

    url = args.url
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    print(f"Fetching {url}...", file=sys.stderr)

    try:
        result = extract_style(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)

    if args.css:
        print(palette_to_css(result))
    elif args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"\nStyle extracted from: {url}")
        print("=" * 50)
        print(f"\nVibe: {', '.join(result['vibe'])}")
        print(f"\nPalette:")
        for name, color in result['palette'].items():
            print(f"  {name:12s}  {color}")
        print(f"\nHero gradient (white-text safe):")
        print(f"  start:  {result['hero_gradient']['start']}")
        print(f"  end:    {result['hero_gradient']['end']}")
        print(f"\nTypography:")
        for f in result['typography']['fonts']:
            print(f"  {f}")
        print(f"\nShape:")
        print(f"  border-radius: {result['shape']['border_radius']}")
        print(f"  shadows: {'yes' if result['shape']['has_shadows'] else 'no'}")
        print(f"\nCSS Variables:")
        print(palette_to_css(result))


if __name__ == "__main__":
    main()
