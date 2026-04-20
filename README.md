# gg-ppt

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet?logo=anthropic)](https://claude.ai)
[![No PowerPoint](https://img.shields.io/badge/PowerPoint-Not%20Needed-red)](https://github.com/dgtql/gg-ppt)
[![HTML Only](https://img.shields.io/badge/Output-Single%20.html-blue?logo=html5&logoColor=white)](https://github.com/dgtql/gg-ppt)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)](https://github.com/dgtql/gg-ppt)
[![Works Offline](https://img.shields.io/badge/Offline-Ready-orange)](https://github.com/dgtql/gg-ppt)

**GG, PowerPoint.**

> You're in 2026. You have AI that writes code in seconds. And you're still... dragging text boxes around slides?

---

## The Problem Nobody Talks About

Everyone hates making PowerPoints. But we keep doing it. Why?

**"It's what everyone uses."** Your boss expects a `.pptx`. Your client expects a `.pptx`. The conference expects a `.pptx`. So you open PowerPoint, stare at a blank slide, and start dragging boxes around. Again.

**"There's no better option."** Google Slides? Same thing, different logo. Keynote? Same thing, prettier font. Prezi? Let's not talk about Prezi.

**"AI can make slides for me now."** And here's where it gets absurd. We built the most powerful text generation technology in human history... and we're using it to generate `.pptx` files. We're using a Ferrari to pull a horse cart.

Think about what happens when an LLM "generates a PowerPoint":
1. AI generates structured content (text, headings, bullet points)
2. A script converts that into XML inside a `.zip` file (that's what `.pptx` actually is)
3. PowerPoint renders that XML as rectangles on a fixed-size canvas
4. You open it, squint, and start manually fixing alignments

**Why are we converting AI output into a 1987 file format, only to render it in a proprietary app?**

## The Obvious Answer

AI generates text. Browsers render text beautifully. Skip the middleman.

```
Prompt → AI → HTML → Browser
```

That's it. No `.pptx`. No XML. No PowerPoint. No license fees. Just a webpage.

**gg-ppt** is a [Claude](https://claude.ai) skill that generates beautiful, interactive HTML presentations. One prompt in, one `.html` file out. Open it in any browser, on any device, online or offline.

### What "HTML presentation" actually means

Not slides. Not rectangles on a canvas. A **flowing, interactive webpage** — like a polished product landing page that you scroll through. Each section fills the viewport, animations trigger on scroll, charts are interactive, and the whole thing feels alive.

Your audience doesn't click "Next Slide" 47 times. They scroll. They click tabs. They hover on charts. They explore.

## See It In Action

Open [`assets/example.html`](assets/example.html) in your browser. It's a Q3 business review for a fictional company, generated from:

- [`assets/sample-inputs/agenda.md`](assets/sample-inputs/agenda.md) — a text outline
- [`assets/sample-inputs/revenue_quarterly.csv`](assets/sample-inputs/revenue_quarterly.csv) — revenue data → auto-generated bar charts + tables
- [`assets/sample-inputs/customer_segments.csv`](assets/sample-inputs/customer_segments.csv) — customer data → donut chart + retention cohorts
- A company logo → brand colors extracted automatically

Scroll through it. Click the tabs. Press `N` for speaker notes. Hit `Ctrl+P` to see the print-to-PDF layout.

## Why PPT Still Exists (And Why It Shouldn't)

| Why people use PPT | Why it no longer makes sense |
|---|---|
| "Everyone knows how to use it" | Everyone knows how to open a browser too |
| "My company has templates" | AI extracts your brand colors from a logo and themes everything automatically |
| "I need charts and tables" | HTML has inline SVG charts, interactive tables, animated counters — all better than SmartArt |
| "I need speaker notes" | Press `N`. Notes sync to your scroll position |
| "I need to share it as a file" | It's one `.html` file. Email it. Slack it. USB it. 142KB |
| "I need a PDF version" | `Ctrl+P`. Built-in print stylesheet with automatic page breaks |
| "I need to present offline" | Zero external dependencies. Works from a USB stick with no internet |
| "My audience expects slides" | Your audience expects to not be bored. Give them something interactive |

## What Can You Feed It?

| Input | What Happens |
|-------|-------------|
| **A topic or outline** | Structures it into sections, picks layouts, writes the narrative |
| **Meeting notes or long text** | Distills key points into a visual, scrollable presentation |
| **CSV / Excel data** | Reads the data and generates inline SVG charts (bar, line, donut, big-number callouts) |
| **Images or plots** | Embeds them as base64 so the file stays self-contained |
| **Company logo** | Extracts brand colors and themes the entire presentation automatically |
| **An existing .pptx** | Extracts text + images, restructures into a flowing HTML page (not a 1:1 slide copy) |
| **Any combination** | "Here's last quarter's deck, updated numbers in this CSV, and our new logo" |

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

The skill triggers on keywords like *presentation*, *deck*, *slides*, *pitch*, *demo* — and even *PowerPoint* (it'll suggest HTML instead).

### 3. Brand Theming

Drop in a company logo and the skill extracts a 6-color palette:

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

These colors flow into every element — nav bars, headings, chart colors, hover states, gradients — making each presentation feel custom-designed.

### 4. Iterate

The skill supports natural back-and-forth. After the first version, just talk:

- *"Make the hero section more dramatic"*
- *"Change the colors to match this new logo"*
- *"Add a timeline section between the stats and the comparison"*
- *"The numbers are wrong — use 92%, 4.2x, and $0"*
- *"Make it more minimal — less color, more whitespace"*

Claude reads the existing HTML and makes surgical edits. Sections you don't mention stay untouched. It's like talking to a designer who implements your feedback instantly.

## What You Get

A single `.html` file with:

| Feature | Detail |
|---------|--------|
| Scroll-triggered animations | Sections fade in as you scroll — smooth, not gimmicky |
| Brand color theming | Auto-extracted from logos, or topic-matched palettes |
| Interactive SVG charts | Bar, donut, line charts — no Chart.js, no D3, no CDN |
| Animated counters | Big numbers that count up when they scroll into view |
| Tabbed content | Click to switch views within a section |
| Data tables | Styled tables with color-coded deltas (green = up, red = down) |
| Speaker notes | Press `N` to toggle, synced to your scroll position |
| Print to PDF | `@media print` stylesheet with clean page breaks |
| Responsive | Desktop, tablet, phone — CSS grid handles it |
| Accessible | `prefers-reduced-motion`, semantic HTML, WCAG AA contrast |
| Iterative editing | Plain language edits, no full regeneration |
| Zero dependencies | Everything inline — works offline from a USB stick |

## PPT vs. gg-ppt

| | PowerPoint | gg-ppt |
|---|---|---|
| **Creation** | Manually drag boxes on slides | Describe in plain text, AI generates |
| **Output** | Proprietary binary format | Single `.html` file |
| **Interactivity** | Click "next slide" | Scroll, click tabs, hover charts, explore |
| **Charts** | Static SmartArt | Animated SVG with real data labels |
| **Branding** | Apply template, fix 47 things | Drop logo, colors auto-extracted |
| **Editing** | Re-open, re-align, re-export | "Make the hero darker" → done |
| **Sharing** | Need PowerPoint/Viewer installed | Any browser, any device, any OS |
| **Cost** | $159/year (Microsoft 365) | $0 |
| **File size** | 5-50 MB | ~150 KB |
| **Offline** | Yes | Yes |
| **Mobile** | Barely | Fully responsive |

## Why Not Reveal.js / Slidev / etc.?

Those are solid tools, but they're still **slide frameworks** — they impose the same page-by-page mental model as PowerPoint. gg-ppt is different:

- **No framework** — pure HTML/CSS/JS, nothing to install or configure
- **Not slides** — it's a flowing webpage, like a product landing page
- **AI-native** — designed for AI text-to-HTML generation, not manual authoring
- **Single file** — no build step, no `npm install`, no config files
- **No learning curve** — you don't learn gg-ppt, you just describe what you want

## File Structure

```
gg-ppt/
├── SKILL.md                          # Skill instructions for Claude
├── README.md                         # You are here
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # Full design system
├── scripts/
│   └── extract_colors.py             # Logo → brand palette
└── assets/
    ├── example.html                   # Live demo — open in browser
    └── sample-inputs/                 # The inputs that generated the demo
        ├── agenda.md                  # Text outline
        ├── revenue_quarterly.csv      # Revenue data → charts
        └── customer_segments.csv      # Customer data → donut + cohorts
```

## The Bet

PowerPoint was invented in 1987 to replace overhead projector transparencies. Its core interaction model — place boxes on rectangular slides — hasn't changed in 39 years.

In 2026, we have AI that generates structured, styled content in seconds. The browser is the most powerful rendering engine ever built. Every device on Earth has one.

**gg-ppt** is a bet that presentations should just be web pages. Beautiful, interactive, branded web pages that you describe in plain text and AI builds for you.

GG, PowerPoint. Well played.

## Contributing

Found a bug? Have an idea for a new layout pattern? PRs welcome.

## License

MIT
