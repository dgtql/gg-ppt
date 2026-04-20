# gg-ppt

**GG, PowerPoint. Well played, but it's over.**

In the AI era, there's no reason to manually drag boxes around slides. This is a [Claude](https://claude.ai) skill that generates beautiful, interactive HTML presentations from plain text — complete with brand-aware color theming, scroll animations, interactive charts, and speaker notes.

One prompt in, one `.html` file out. No PowerPoint. No Keynote. No Google Slides. Just a webpage that makes your audience go *wow*.

---

## What It Does

You describe your presentation in plain text. The skill generates a single, self-contained HTML file that:

- **Flows like a modern webpage** — not rigid slides, but smooth scrolling sections with purposeful animations
- **Matches your brand** — drop in a company logo and it extracts your brand colors to theme the entire presentation automatically
- **Includes real interactivity** — tabbed content, expandable cards, hover effects, animated counters, inline SVG charts
- **Has speaker notes** — press `N` to toggle a notes panel synced to the current section
- **Supports iterative editing** — say "make the hero darker" or "add a chart to section 3" and it surgically updates the HTML, no regeneration needed
- **Prints to PDF** — `Ctrl+P` gives you a clean printable version with automatic page breaks
- **Works offline** — zero external dependencies, no CDNs, no fonts to download, opens in any browser

## See It In Action

Open [`assets/example.html`](assets/example.html) in your browser to see a live demo — a Q3 business review for a fictional company, generated from:

- **Text outline** → [`assets/sample-inputs/agenda.md`](assets/sample-inputs/agenda.md) — the meeting agenda and key messages
- **Revenue CSV** → [`assets/sample-inputs/revenue_quarterly.csv`](assets/sample-inputs/revenue_quarterly.csv) — quarterly revenue data, turned into bar charts and tables
- **Customer data** → [`assets/sample-inputs/customer_segments.csv`](assets/sample-inputs/customer_segments.csv) — segment breakdown, turned into donut chart and retention cohort tables
- **Company logo** → brand colors extracted automatically (blue + orange palette)

The example shows bar charts, donut charts, animated counters, data tables, card grids, timelines, tabbed content, and speaker notes — all generated from those simple inputs.

## What Can You Feed It?

| Input | What Happens |
|-------|-------------|
| **A topic or outline** | Structures it into sections, picks layouts, writes the narrative |
| **Meeting notes or long text** | Distills key points into a visual, scrollable presentation |
| **CSV / Excel data** | Reads the data and generates inline SVG charts (bar, line, donut, big-number callouts) |
| **Images or plots** | Embeds them as base64 so the file stays self-contained, no external refs |
| **Company logo** | Extracts brand colors and themes the entire presentation automatically |
| **An existing .pptx** | Extracts text + images, restructures into a flowing HTML page (not a 1:1 slide copy) |
| **Any combination** | Handles mixed inputs — e.g., "here's last quarter's deck, new numbers in this spreadsheet, and our updated logo" |

## Quick Start

### 1. Install the Skill

Copy the `gg-ppt` folder into your Claude skills directory:

```
~/.claude/skills/gg-ppt/
```

Or for project-level installation:

```
your-project/.claude/skills/gg-ppt/
```

### 2. Use It

Tell Claude to make a presentation:

> "Create an HTML presentation about our Q3 results. Here's our company logo. Audience is the board of directors, tone should be confident but not aggressive."

Or more casually:

> "I need to present our new product roadmap to the team tomorrow. Can you make something that looks way better than a PowerPoint?"

The skill triggers on keywords like *presentation*, *deck*, *slides*, *pitch*, *demo*, and even *PowerPoint* (it'll suggest HTML instead).

### 3. Brand Theming (Optional)

If you provide a company logo, the skill runs `scripts/extract_colors.py` to pull out dominant colors and build a harmonious 6-color palette:

```bash
python scripts/extract_colors.py your-logo.png --json
```

```json
{
  "primary": "#2B5EA7",
  "secondary": "#5A8FCB",
  "accent": "#F4A623",
  "light": "#F0F4F8",
  "dark": "#1A2332",
  "neutral": "#6B7B8D"
}
```

These colors flow into every element — nav bars, headings, chart colors, hover states, gradients — making the presentation feel custom-designed for the brand.

## What You Get

A single `.html` file with:

| Feature | How |
|---------|-----|
| Smooth scroll sections | Each topic gets a full-viewport section with entrance animations |
| Brand color theming | Automatic palette extraction from logos, or curated topic palettes |
| Interactive charts | Inline SVG bar charts, donut charts, animated counters — no libraries |
| Tabbed content | Click to switch views within a section |
| Speaker notes | Press `N` to toggle notes synced to your scroll position |
| Print to PDF | Built-in `@media print` stylesheet with clean page breaks |
| Responsive design | Looks great on desktop, tablet, and phone |
| Accessibility | Respects `prefers-reduced-motion`, semantic HTML, good contrast ratios |
| Iterative editing | Ask for changes in plain language — surgical edits, no full regeneration |
| Zero dependencies | Everything is inline — works offline from a USB stick |

## File Structure

```
gg-ppt/
├── SKILL.md                          # Main skill instructions
├── README.md                         # This file
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # Full design system (colors, typography, layouts, animations)
├── scripts/
│   └── extract_colors.py             # Logo color extraction tool
└── assets/
    ├── example.html                   # Live demo — open in browser
    └── sample-inputs/                 # The inputs that generated the example
        ├── agenda.md                  # Text outline / meeting agenda
        ├── revenue_quarterly.csv      # Revenue data → bar charts + tables
        └── customer_segments.csv      # Customer data → donut chart + cohorts
```

## Iterative Editing

The skill supports natural back-and-forth. After the first version is generated, just tell Claude what to change:

- *"Make the hero section more dramatic"*
- *"Change the colors to match this new logo"*
- *"Add a timeline section between the stats and the comparison"*
- *"The numbers in the stats section are wrong — use 92%, 4.2x, and $0"*
- *"Make it more minimal — less color, more whitespace"*
- *"Remove the comparison section, it's not needed"*

Claude reads the existing HTML and makes surgical edits rather than regenerating everything. Sections you don't mention stay untouched. It's like having a conversation with a designer who instantly implements your feedback.

## Why Not Reveal.js / Slidev / etc.?

Those are great tools, but they're still slide frameworks — they impose a slide-by-slide mental model. gg-ppt breaks free from that entirely:

- **No framework dependency** — pure HTML/CSS/JS, nothing to install or configure
- **Not slides** — it's a flowing webpage, like a polished landing page or interactive article
- **AI-native** — designed specifically for AI text-to-HTML generation, not manual authoring
- **Single file** — no build step, no `npm install`, no config files

## Philosophy

PowerPoint was invented in 1987. It was revolutionary for its time — it replaced overhead projector transparencies. But the core interaction model hasn't changed: you place boxes on rectangular slides, one after another.

In 2026, we have AI that can generate structured, styled HTML in seconds. The browser is the most powerful rendering engine ever built. Every device has one. Why are we still making PowerPoint?

**gg-ppt** is a bet that the future of presentations is just... web pages. Beautiful, interactive, branded web pages that you describe in plain text and AI builds for you.

## Contributing

Found a bug? Have an idea for a new layout pattern? PRs welcome.

## License

MIT
