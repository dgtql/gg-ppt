---
name: gg-ppt
description: "Use this skill to create beautiful, interactive HTML presentations that replace traditional PowerPoint slides. Instead of rigid slide-by-slide decks, this generates flowing, webpage-style presentations with smooth scrolling, animations, and interactivity. Accepts any input: text outlines, meeting notes, CSV/Excel data (auto-generates charts), images/plots, company logos (auto-extracts brand colors), or existing .pptx files (converts to HTML). Trigger whenever the user mentions 'presentation', 'deck', 'slides', 'pitch', 'demo', 'keynote', or wants to present information visually — even if they say 'PowerPoint' or 'PPT', suggest HTML instead. Also triggers when converting a .pptx to a better format, when the user has data they want to visualize in a presentation, or when they want interactive charts, animations, or click-to-reveal elements."
---

# gg-ppt

**HTML presentations for the AI era.** Instead of generating rigid slide decks, this skill creates beautiful, flowing HTML pages that look like polished landing pages — scrollable, interactive, and responsive.

## Why HTML over PPT

PowerPoint was designed for an era when humans manually placed boxes on slides. In the AI era, text-to-HTML is the natural path: AI generates structured content, HTML renders it beautifully, and the result is more interactive, more shareable, and more impressive than any slide deck.

HTML presentations can include live charts, smooth animations, click-to-reveal sections, embedded videos, responsive layouts — things that are painful or impossible in PPT.

## Quick Reference

| Task | How |
|------|-----|
| Create a presentation | Follow the [Creation Workflow](#creation-workflow) below |
| Extract brand colors from a logo | `python scripts/extract_colors.py logo.png` |
| Design reference | Read [references/design-guide.md](references/design-guide.md) |

---

## Creation Workflow

### Step 1: Gather Inputs

Ask the user what they have. People come with very different starting materials — the skill should handle all of them gracefully.

#### Supported Input Types

**Text & Outlines:**
- A topic and rough agenda ("5 slides about our Q3 results")
- Bullet-point outline or meeting notes
- Long-form text, a blog post, or a document to distill into a presentation
- Markdown files

When the input is text, your job is to structure it into sections, pick appropriate layout patterns for each (cards, stats, timeline, split, etc.), and write the narrative.

**Data Tables (CSV, Excel, JSON):**
- Spreadsheets with numbers the user wants to visualize
- Financial data, survey results, metrics

When the user provides tabular data:
1. Read the file (use `python -m markitdown <file>` for Excel, or read CSV directly)
2. Identify which columns/rows are most important to visualize
3. Pick the right chart type: bar chart for comparisons, line for trends, donut for proportions, big-number callouts for key stats
4. Generate inline SVG charts with the actual data — label axes and include data values
5. If there's too much data for a single chart, summarize or let the user pick what to highlight

**Images & Plots:**
- Company logos (used for brand color extraction + display)
- Charts or plots the user has already created (e.g., matplotlib exports, screenshots)
- Photos or illustrations to embed in specific sections

When the user provides images:
1. For logos → run `extract_colors.py` and embed the logo in the nav/hero
2. For charts/plots → embed as `<img>` with base64-encoded `src` so the file stays self-contained. Read the image file and convert: `base64 -w0 chart.png` → use as `src="data:image/png;base64,..."`. If the image is very large (>500KB), suggest the user provide a smaller version
3. For photos → embed as base64 `<img>` in the relevant section, with appropriate sizing and rounded corners

**Existing .pptx Files (Convert to HTML):**
- The user has a PowerPoint they want to turn into an HTML presentation

When converting from .pptx:
1. Extract text content: `python -m markitdown presentation.pptx`
2. This gives you the full text of every slide — titles, body text, speaker notes
3. Restructure the content for a flowing webpage format — don't just reproduce the slides as-is. Merge thin slides, pick better layout patterns, and add interactivity where it makes sense
4. If the .pptx has images, extract them: unzip the .pptx (`unzip presentation.pptx -d unpacked/`) and look in `unpacked/ppt/media/` for image files. Embed relevant ones as base64
5. Carry over speaker notes as `data-notes` attributes on the corresponding sections
6. Apply brand theming: if the .pptx has a consistent color scheme, try to match it. If the user provides a logo, use that instead

**Mixed Inputs:**
Users often provide a combination — "here's our deck from last quarter, plus this new Excel with updated numbers, and our new logo." Handle each input type as described above and weave them together into a coherent presentation.

#### What to Ask For

After understanding the inputs, collect any missing context:
1. **Audience** — who will view it (investors, team, customers, conference)
2. **Tone** — formal, casual, energetic, minimal
3. **Key message** — what's the one thing the audience should remember?
4. **Company logo** (optional) — for brand color extraction

Don't over-ask. If the user gives you a detailed outline and a logo, you have enough — just build it. Only ask about audience/tone if it's genuinely unclear from context.

### Step 2: Extract Brand Colors (if logo provided)

Run the color extraction script on the user's logo:

```bash
pip install Pillow --break-system-packages -q
python <skill-path>/scripts/extract_colors.py <logo-path>
```

This outputs a JSON palette with primary, secondary, accent, and neutral colors extracted from the logo. Use these colors throughout the presentation for a cohesive brand feel.

If no logo is provided, choose a palette from the design guide that matches the topic's mood.

**Important — hero gradient from palette:** When building `--color-hero-gradient`, never use `--color-primary` as the gradient endpoint. Primary colors are often mid-tone (40-50% lightness) which makes white hero text unreadable. Instead, darken the primary hue to 20-25% lightness for the gradient endpoint. The formula: take the primary's HSL hue and saturation, but set lightness to 20-25%. This keeps the brand feel while ensuring white text pops.

### Step 3: Build the HTML

Read [references/design-guide.md](references/design-guide.md) for the full design system, then generate a single self-contained `.html` file.

**Architecture: single file, zero dependencies.** Everything — CSS, JS, SVG icons, chart rendering — goes into one `.html` file. No CDN links, no external fonts that require network. The file should work when opened locally from the filesystem, offline, anywhere.

**The presentation is NOT slides.** It's a beautiful scrolling webpage with distinct sections. Think of it like a polished landing page or a long-form interactive article. Each "section" of the presentation is a full-viewport (or near full-viewport) block that the viewer scrolls through.

#### Required HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Presentation Title]</title>
  <style>
    /* All CSS inline — design system, animations, responsive */
  </style>
</head>
<body>
  <!-- Navigation bar (fixed) -->
  <nav>...</nav>

  <!-- Hero section (full viewport) -->
  <section class="hero">...</section>

  <!-- Content sections -->
  <section class="content-section">...</section>

  <!-- Footer / CTA -->
  <footer>...</footer>

  <!-- Speaker notes panel (hidden by default, toggle with 'N' key) -->
  <div id="speaker-notes">...</div>

  <script>
    /* All JS inline — animations, interactivity, charts, speaker notes */
  </script>
</body>
</html>
```

#### Section Design Patterns

**Hero Section:**
- Full viewport height (`100vh`)
- Large title with animated entrance (fade-up or scale)
- Subtitle or tagline
- Optional company logo
- **Dark** gradient background — the hero has white text, so the background must be dark enough for clear readability across the entire viewport. Build the hero gradient from the `--color-dark` value, not from `--color-primary`. A good pattern: `linear-gradient(135deg, <near-black> 0%, <dark> 40%, <darkened-primary> 100%)` where the darkened primary is the primary hue at 20-25% lightness, not the raw primary. Never let any part of the gradient go above ~35% lightness when the text is white.
- Always add `text-shadow: 0 2px 20px rgba(0,0,0,0.4)` on the hero title and `text-shadow: 0 1px 10px rgba(0,0,0,0.3)` on hero body text as a safety net for varying screens and brightness settings
- Scroll indicator at bottom (animated chevron)

**Content Sections:**
- Near full viewport height (`min-height: 90vh`) with padding
- Each section has a clear heading and visual content
- Use a mix of these layouts — never repeat the same layout twice in a row:
  - **Split layout**: text on one side, visual (chart/image/illustration) on the other
  - **Card grid**: 2x2 or 3x3 cards with icons, each revealing detail on hover
  - **Timeline**: horizontal or vertical timeline with milestone markers
  - **Big number callouts**: large statistics (72px+) with supporting context
  - **Comparison columns**: side-by-side comparison with visual differentiation
  - **Quote/highlight block**: centered large text with accent border
  - **Interactive tabs**: clickable tabs that switch visible content without page reload

**Charts & Data (inline, no dependencies):**
- Use inline SVG or canvas for charts — no Chart.js or D3 CDN
- For bar charts, line charts, pie charts: draw with SVG `<rect>`, `<line>`, `<circle>`, `<path>`
- Animate chart elements on scroll into view using Intersection Observer
- Always include data labels directly on the chart

**Animations:**
- Use CSS animations + Intersection Observer for scroll-triggered reveals
- Fade-up, fade-in, scale-up — keep it smooth and professional
- Stagger animations within a section (e.g., cards appear one by one with 100ms delay)
- Never use animations that feel gimmicky — no bouncing, no spinning, no 3D flips

**Speaker Notes:**
- Hidden panel toggled with the 'N' key
- Slides in from the bottom or side
- Each section's notes are keyed to data attributes on the sections
- Styled with semi-transparent dark background

**PDF Export:**
- Include a `@media print` stylesheet that:
  - Removes animations, fixed navs, and interactive elements
  - Adds page breaks between sections (`page-break-before: always`)
  - Ensures all content is visible (no hidden/collapsed elements)
  - Sets a clean white background for print
- User can print to PDF from the browser (Ctrl/Cmd + P)

### Step 4: Polish

- **Test responsive**: the layout should work on desktop (1200px+) and look reasonable on tablet (768px)
- **Check color contrast**: all text must be readable against its background (WCAG AA minimum)
- **Verify interactivity**: all clickable elements should have hover states and work correctly
- **Smooth scroll**: use `scroll-behavior: smooth` on the html element
- **Keyboard navigation**: arrow keys or scroll should feel natural

### Step 5: Deliver

Save the `.html` file and present it to the user. Mention:
- Open it in any browser to view
- Press 'N' to toggle speaker notes
- Ctrl/Cmd+P to export as PDF
- It works offline — no internet needed
- **They can ask for changes** — invite the user to refine it iteratively

---

## Editing & Refinement Workflow

After delivering the first version, the user will often want to iterate. This is a core strength of HTML over PPT — edits are fast, precise, and don't break layouts. Support these kinds of follow-up requests:

### Types of Edit Requests

| Request | How to Handle |
|---------|---------------|
| "Change the colors" | Re-run color extraction with new logo, or swap the `:root` CSS variables |
| "Add a section about X" | Insert a new `<section>` block using an appropriate layout pattern |
| "Remove the section about Y" | Delete the section and its nav link |
| "Make the hero more dramatic" | Adjust gradient, font size, add background pattern or animation |
| "The stats are wrong, use these numbers" | Update `data-target` attributes and labels |
| "Make it shorter / longer" | Merge or split sections, adjust content density |
| "Change the tone" | Rewrite copy — formal, casual, energetic, minimal |
| "Add a chart showing X" | Generate inline SVG chart with the provided data |
| "Reorder sections" | Move `<section>` blocks and update nav links |
| "Add my logo" | Insert logo in nav and/or hero, re-extract brand colors |

### How to Edit

1. **Read the existing HTML file** — always read the current state before making edits
2. **Make surgical changes** — use the Edit tool to modify specific sections rather than regenerating the entire file (unless the user wants a complete overhaul)
3. **Preserve what works** — don't change sections the user hasn't mentioned; their silence means approval
4. **Maintain consistency** — if you change colors, update them everywhere (`:root` variables make this easy). If you change a layout pattern, make sure it still flows well with adjacent sections
5. **Re-deliver** — after edits, save the updated file and briefly note what changed

### Inviting Feedback

After delivering the first version (and after each edit), prompt the user naturally:

- "How does that look? I can adjust the colors, add/remove sections, change the layout of any part, or tweak the copy."
- "Want me to make any section more visual? I can add charts, timelines, or interactive elements."
- "If you'd like a different vibe — more minimal, more energetic, darker theme — just say the word."

The goal is a collaborative, conversational loop. The user describes what they want in plain language, you edit the HTML, they react, repeat until they're happy. This should feel as natural as talking to a designer — not like filing JIRA tickets.

### Multi-round Editing Tips

- **Keep a mental model of the structure**: track which sections exist, their order, and their layout types so you can reference them naturally ("the stats section", "the comparison at the end")
- **Batch related changes**: if the user says "make it more minimal and use darker colors", do both in one pass rather than asking if they want to do one at a time
- **Suggest improvements proactively**: if you notice something that could be better while making an edit (e.g., a section that would benefit from a chart), mention it — but don't force it
- **Don't over-ask**: if the intent is clear, just make the change. Reserve questions for genuinely ambiguous cases (e.g., "make it better" — better how?)

---

## Design Principles

The full design system is in [references/design-guide.md](references/design-guide.md). Key principles:

1. **Brand-first**: every presentation should feel like it belongs to the company whose logo was provided
2. **Content density over slide count**: one scrolling page replaces 20 thin slides
3. **Show, don't list**: replace bullet points with visuals, charts, timelines, and cards
4. **Motion with purpose**: animations should guide the eye, not distract
5. **Typography is the design**: use font size, weight, and spacing to create hierarchy — not decorative elements

---

## Common Mistakes to Avoid

- **Don't make it look like slides**: no bordered rectangles, no "slide numbers", no fixed-height boxes
- **Don't use external CDNs**: everything must be self-contained and work offline
- **Don't over-animate**: subtle fade-ups are elegant; spinning logos are not
- **Don't forget print styles**: many people will want a PDF version
- **Don't use tiny text**: minimum 16px for body text, 14px for captions
- **Don't ignore mobile**: use CSS grid/flexbox that gracefully reflows
- **Don't make monochrome presentations**: use the full brand palette with intentional contrast
- **Don't use light gradients behind white text**: the hero gradient must stay dark (max ~35% lightness) across the entire viewport. This is the single most common visual bug — a gradient that looks fine on the left but washes out on the right, making the title invisible. Always darken the primary color for hero gradients and add text-shadow as a safety net
