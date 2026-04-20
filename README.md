<h1 align="center">GG-PPT</h1>

<p align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![No PowerPoint](https://img.shields.io/badge/PowerPoint-Not%20Needed-red)](https://github.com/dgtql/gg-ppt)
[![HTML Only](https://img.shields.io/badge/Output-Single%20.html-blue?logo=html5&logoColor=white)](https://github.com/dgtql/gg-ppt)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)](https://github.com/dgtql/gg-ppt)
[![Works Offline](https://img.shields.io/badge/Offline-Ready-orange)](https://github.com/dgtql/gg-ppt)
[![Claude](https://img.shields.io/badge/Claude-Supported-blueviolet?logo=anthropic)](https://claude.ai)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-Supported-74aa9c?logo=openai&logoColor=white)](https://chat.openai.com)
[![Codex](https://img.shields.io/badge/Codex-Supported-74aa9c?logo=openai&logoColor=white)](https://openai.com/codex)
[![Cursor](https://img.shields.io/badge/Cursor-Supported-000?logo=cursor&logoColor=white)](https://cursor.sh)

</p>

<p align="center"><strong>GG, PowerPoint.</strong></p>

<p align="center">
  <img src="assets/comic.png" alt="The Evolution of Presentations: from manual PPT, to AI-generated PPT, to AI-generated interactive HTML" width="100%"/>
</p>

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

<p align="center">
  <img src="assets/system-diagram.png" alt="System diagram: Input (text, tables, plots, logo, website URL, .pptx) → AI (Claude, ChatGPT, Codex, Cursor) → HTML (single file, zero dependencies) → Browser (scroll, animate, charts, interact)" width="100%"/>
</p>

That's it. No `.pptx`. No XML. No PowerPoint. No license fees. Just a webpage.

**gg-ppt** is a prompt kit + design system that any AI can use to generate beautiful, interactive HTML presentations. Works with **Claude**, **ChatGPT**, **Codex**, **Cursor**, **Copilot**, or any LLM that can write code. One prompt in, one `.html` file out. Open it in any browser, on any device, online or offline.

### What "HTML presentation" actually means

Not slides. Not rectangles on a canvas. A **flowing, interactive webpage** — like a polished product landing page that you scroll through. Each section fills the viewport, animations trigger on scroll, charts are interactive, and the whole thing feels alive.

Your audience doesn't click "Next Slide" 47 times. They scroll. They click tabs. They hover on charts. They explore.

## See It In Action

Open [`assets/example.html`](assets/example.html) in your browser. It's a Q3 business review styled to match **stripe.com**, generated from:

- [`assets/sample-inputs/agenda.md`](assets/sample-inputs/agenda.md) — a text outline
- [`assets/sample-inputs/revenue_quarterly.csv`](assets/sample-inputs/revenue_quarterly.csv) — revenue data → auto-generated bar charts + tables
- [`assets/sample-inputs/customer_segments.csv`](assets/sample-inputs/customer_segments.csv) — customer data → donut chart + retention cohorts
- `stripe.com` — website URL → brand colors, typography, shadows, and vibe extracted automatically

Scroll through it. Click the tabs. Press `N` for speaker notes. Hit `Ctrl+P` to see the print-to-PDF layout.

## Why PPT Still Exists (And Why It Shouldn't)

| Why people use PPT | Why it no longer makes sense |
|---|---|
| "Everyone knows how to use it" | Everyone knows how to open a browser too |
| "My company has templates" | Drop a logo or paste your website URL — AI extracts brand colors, fonts, and style automatically |
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
| **A website URL** | "Make it look like stripe.com" — fetches the site's CSS, extracts colors, fonts, border-radius, shadows, and vibes, then themes your presentation to match |
| **Any combination** | "Here's last quarter's deck, updated numbers in this CSV, and our new logo — style it like linear.app" |

## Quick Start

### Use with Claude (Skill)

Copy the `gg-ppt` folder into your Claude skills directory:

```
~/.claude/skills/gg-ppt/
```

Then just ask Claude to make a presentation — the skill triggers automatically.

### Use with ChatGPT / Codex / Copilot / Cursor / Any LLM

Paste the content of [`SKILL.md`](SKILL.md) as context (or attach it), then prompt:

> "Read the attached SKILL.md and the design guide. Create an HTML presentation about our Q3 results. Here's our company logo."

Or simpler — just paste the [`references/design-guide.md`](references/design-guide.md) as context and say:

> "Follow this design system to create a single-file HTML presentation about [your topic]. Make it a scrolling webpage, not slides."

The core idea works with **any LLM that can generate HTML**. The SKILL.md and design guide are just detailed instructions — any AI can follow them.

### Use Standalone (No AI)

The scripts work independently:

**Extract brand colors from a logo:**
```bash
pip install Pillow
python scripts/extract_colors.py your-logo.png --css
```

**Match a website's visual style:**
```bash
pip install requests beautifulsoup4
python scripts/extract_style.py stripe.com --css
```

Both output CSS custom properties you can paste into any HTML project.

### Brand Theming

Two ways to theme your presentation — both automatic:

**From a logo** — drop in any image and the skill extracts a 6-color brand palette:

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

**From a website** — give it a URL and it extracts the site's entire visual language: colors, fonts, border-radius, shadows, and overall vibe:

```bash
python scripts/extract_style.py stripe.com --json
```

```json
{
  "palette": { "primary": "#533afd", "secondary": "#fb76fa", "accent": "#ff6118" },
  "typography": { "heading_font": "sohne-var", "body_font": "SourceCodePro" },
  "shape": { "border_radius": "12px", "shadow_style": "elevated" },
  "vibe": ["colorful"]
}
```

Colors flow into every element — nav bars, headings, chart colors, hover states, gradients. "Make my deck look like Stripe" → it just works.

### Iterate

The skill supports natural back-and-forth. After the first version, just talk:

- *"Make the hero section more dramatic"*
- *"Change the colors to match this new logo"*
- *"Style it like linear.app"*
- *"Add a timeline section between the stats and the comparison"*
- *"The numbers are wrong — use 92%, 4.2x, and $0"*
- *"Make it more minimal — less color, more whitespace"*

Your AI reads the existing HTML and makes surgical edits. Sections you don't mention stay untouched. It's like talking to a designer who implements your feedback instantly.

## What You Get

A single `.html` file with:

| Feature | Detail |
|---------|--------|
| Scroll-triggered animations | Sections fade in as you scroll — smooth, not gimmicky |
| Brand color theming | Auto-extracted from logos, website URLs, or topic-matched palettes |
| Website style matching | Give it a URL — extracts colors, fonts, shadows, border-radius, vibe |
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
| **Branding** | Apply template, fix 47 things | Drop logo or paste a URL — colors, fonts, vibe auto-extracted |
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
├── SKILL.md                          # AI instructions (works with any LLM)
├── README.md                         # You are here
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # Full design system
├── scripts/
│   ├── extract_colors.py             # Logo → brand palette
│   └── extract_style.py              # Website URL → style guide
└── assets/
    ├── example.html                   # Live demo (Stripe-styled) — open in browser
    ├── comic.png                      # Banner comic for README
    ├── system-diagram.png             # Architecture diagram for README
    └── sample-inputs/                 # The inputs that generated the demo
        ├── agenda.md                  # Text outline
        ├── revenue_quarterly.csv      # Revenue data → charts
        └── customer_segments.csv      # Customer data → donut + cohorts
```

## The Bet

PowerPoint was invented in 1987 to replace overhead projector transparencies. Its core interaction model — place boxes on rectangular slides — hasn't changed in 39 years.

In 2026, we have AI that generates structured, styled content in seconds. The browser is the most powerful rendering engine ever built. Every device on Earth has one.

**gg-ppt** is a bet that presentations should just be web pages. Beautiful, interactive, branded web pages that you describe in plain text and any AI builds for you.

GG, PowerPoint. Well played.

## Contributing

Found a bug? Have an idea for a new layout pattern? PRs welcome.

## License

MIT
