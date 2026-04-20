# Design Guide for gg-ppt

This document contains the full design system for generating HTML presentations. Read this when creating a new presentation.

## Table of Contents

1. [Color System](#color-system)
2. [Typography](#typography)
3. [Layout Patterns](#layout-patterns)
4. [Animation System](#animation-system)
5. [Interactive Elements](#interactive-elements)
6. [Responsive Design](#responsive-design)
7. [Print Stylesheet](#print-stylesheet)

---

## Color System

### When a Logo is Provided

Run `scripts/extract_colors.py` to get the brand palette. The script outputs:

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

Apply these colors as CSS custom properties at the `:root` level:

```css
:root {
  --color-primary: #2B5EA7;
  --color-secondary: #5A8FCB;
  --color-accent: #F4A623;
  --color-light: #F0F4F8;
  --color-dark: #1A2332;
  --color-neutral: #6B7B8D;

  /* Derived colors */
  --color-primary-alpha: rgba(43, 94, 167, 0.1);
  /* IMPORTANT: Never use --color-primary directly as gradient endpoint.
     Darken the primary hue to 20-25% lightness so white text stays readable. */
  --color-hero-gradient: linear-gradient(135deg, #070E18 0%, var(--color-dark) 40%, <darkened-primary-at-20pct-lightness> 100%);
  --color-section-alt: var(--color-light);
  --color-text: var(--color-dark);
  --color-text-muted: var(--color-neutral);
}
```

### When No Logo is Provided

Choose from these topic-informed palettes:

| Topic | Primary | Secondary | Accent | Light | Dark |
|-------|---------|-----------|--------|-------|------|
| **Technology / AI** | `#6366F1` indigo | `#818CF8` light indigo | `#F59E0B` amber | `#F8FAFC` | `#0F172A` |
| **Business / Finance** | `#0F766E` teal | `#14B8A6` seafoam | `#F97316` orange | `#F0FDFA` | `#134E4A` |
| **Healthcare / Science** | `#0369A1` blue | `#38BDF8` sky | `#10B981` emerald | `#F0F9FF` | `#0C4A6E` |
| **Education** | `#7C3AED` violet | `#A78BFA` lavender | `#EC4899` pink | `#FAF5FF` | `#2E1065` |
| **Environment / Nature** | `#15803D` green | `#4ADE80` lime | `#EAB308` yellow | `#F0FDF4` | `#14532D` |
| **Creative / Design** | `#DB2777` pink | `#F472B6` rose | `#8B5CF6` purple | `#FDF2F8` | `#831843` |
| **Startup / Pitch** | `#DC2626` red | `#FB923C` orange | `#FBBF24` gold | `#FFF7ED` | `#1C1917` |
| **Minimal / Elegant** | `#18181B` zinc | `#52525B` gray | `#A855F7` purple | `#FAFAFA` | `#09090B` |

### Color Usage Rules

- **Primary** → hero backgrounds, section headings, nav bar, important buttons
- **Secondary** → supporting elements, card borders, hover states, secondary buttons
- **Accent** → call-to-action highlights, key statistics, interactive element active states
- **Light** → alternating section backgrounds, card backgrounds
- **Dark** → text color, hero overlay, footer background
- **Neutral** → body text, captions, muted elements, borders

Always ensure a minimum contrast ratio of 4.5:1 for text (WCAG AA).

**Hero gradient contrast is critical.** The hero section has white text, so the gradient must stay dark enough across the entire viewport — not just the top-left corner. A common mistake is using a gradient that goes from dark to a mid-tone primary color, which washes out the text on the lighter side. Fix this by:
1. Keeping the gradient endpoint dark (use the darkened primary, not the raw primary)
2. Adding `text-shadow: 0 2px 20px rgba(0,0,0,0.4)` to the hero title
3. Adding `text-shadow: 0 1px 10px rgba(0,0,0,0.3)` to hero body text
4. Testing on a bright monitor — if you squint and the text disappears, the gradient is too light

---

## Typography

### Font Stack

Use system fonts for zero-dependency rendering:

```css
:root {
  --font-display: 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-body: 'Segoe UI', system-ui, -apple-system, sans-serif;
  --font-mono: 'Cascadia Code', 'Fira Code', 'Consolas', monospace;
}
```

### Type Scale

| Element | Size | Weight | Line Height | Letter Spacing |
|---------|------|--------|-------------|----------------|
| Hero title | 4rem (64px) | 800 | 1.1 | -0.02em |
| Hero subtitle | 1.5rem (24px) | 400 | 1.4 | 0 |
| Section title | 2.5rem (40px) | 700 | 1.2 | -0.01em |
| Section subtitle | 1.25rem (20px) | 400 | 1.5 | 0 |
| Body text | 1.125rem (18px) | 400 | 1.7 | 0 |
| Card title | 1.25rem (20px) | 600 | 1.3 | 0 |
| Caption / label | 0.875rem (14px) | 500 | 1.4 | 0.02em |
| Big number | 4.5rem (72px) | 800 | 1.0 | -0.03em |
| Nav link | 0.9rem (14.4px) | 500 | 1.0 | 0.01em |

### Typography Rules

- Never go below 14px for any visible text
- Use font-weight contrast (not font-size alone) to create hierarchy within a section
- Headings use `--color-dark` or white (on dark backgrounds); body uses `--color-text`
- Long paragraphs: max-width of 65ch for comfortable reading

---

## Layout Patterns

### Hero Section

```
+--------------------------------------------------+
|                                                  |
|              [Logo]                               |
|                                                  |
|         PRESENTATION TITLE                        |
|         Subtitle or tagline goes here             |
|                                                  |
|              [CTA Button]                         |
|                                                  |
|              ↓ (scroll indicator)                 |
+--------------------------------------------------+
```

- Full viewport height: `height: 100vh`
- Center content both vertically and horizontally
- Gradient background using brand colors
- Animated entrance (title fades up, subtitle follows 200ms later)

### Split Layout (50/50)

```
+-------------------------+-------------------------+
|                         |                         |
|    Section Heading      |    [Chart or Image]     |
|                         |                         |
|    Body text with key   |    Visualizes the       |
|    points explained     |    key data point       |
|    in paragraph form.   |                         |
|                         |                         |
+-------------------------+-------------------------+
```

- Use CSS Grid: `grid-template-columns: 1fr 1fr`
- Gap: 4rem between columns
- On mobile: stack vertically

### Card Grid

```
+--------------------------------------------------+
|            Section Heading                        |
|                                                  |
|  +------------+  +------------+  +------------+  |
|  |  [Icon]    |  |  [Icon]    |  |  [Icon]    |  |
|  |  Title     |  |  Title     |  |  Title     |  |
|  |  Desc...   |  |  Desc...   |  |  Desc...   |  |
|  +------------+  +------------+  +------------+  |
|                                                  |
|  +------------+  +------------+  +------------+  |
|  |  [Icon]    |  |  [Icon]    |  |  [Icon]    |  |
|  |  Title     |  |  Title     |  |  Title     |  |
|  |  Desc...   |  |  Desc...   |  |  Desc...   |  |
|  +------------+  +------------+  +------------+  |
+--------------------------------------------------+
```

- Grid: `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))`
- Cards have subtle shadow, rounded corners (12px), padding (2rem)
- Hover: slight lift (`translateY(-4px)`) and shadow increase
- Staggered entrance animation

### Big Numbers

```
+--------------------------------------------------+
|            Section Heading                        |
|                                                  |
|    98%              $2.4M            150+         |
|    Customer         Revenue          Countries    |
|    satisfaction     growth           served       |
|                                                  |
+--------------------------------------------------+
```

- Numbers at 72px+ bold with accent color
- Labels at 14-16px in neutral color below
- Animate numbers counting up on scroll (use JS)
- Three or four stats in a row, evenly spaced

### Timeline

```
+--------------------------------------------------+
|            Section Heading                        |
|                                                  |
|  2020 ----●---- 2021 ----●---- 2022 ----●----   |
|            |              |              |        |
|         Event A        Event B        Event C     |
|         Details        Details        Details     |
+--------------------------------------------------+
```

- Horizontal line with circular markers
- Content cards below each marker
- Animate markers appearing left-to-right on scroll
- On mobile: switch to vertical timeline

### Comparison Columns

```
+--------------------------------------------------+
|            Section Heading                        |
|                                                  |
|  +---------------------+  +---------------------+|
|  |  Before / Option A  |  |  After / Option B   ||
|  |                     |  |                     ||
|  |  • Point 1          |  |  • Point 1          ||
|  |  • Point 2          |  |  • Point 2          ||
|  |  • Point 3          |  |  • Point 3          ||
|  +---------------------+  +---------------------+|
+--------------------------------------------------+
```

- Two columns with distinct background tints
- Left column uses lighter tint, right uses primary-alpha or accent-alpha
- Can add a "recommended" badge to one column

---

## Animation System

### Scroll Animations

Use Intersection Observer to trigger animations when elements enter the viewport:

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```

### CSS Animation Classes

```css
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Staggered children */
.stagger-children .animate-on-scroll:nth-child(1) { transition-delay: 0ms; }
.stagger-children .animate-on-scroll:nth-child(2) { transition-delay: 100ms; }
.stagger-children .animate-on-scroll:nth-child(3) { transition-delay: 200ms; }
.stagger-children .animate-on-scroll:nth-child(4) { transition-delay: 300ms; }
.stagger-children .animate-on-scroll:nth-child(5) { transition-delay: 400ms; }
.stagger-children .animate-on-scroll:nth-child(6) { transition-delay: 500ms; }
```

### Counter Animation

For big number callouts, animate the count-up:

```javascript
function animateCounter(el) {
  const target = parseInt(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  const prefix = el.dataset.prefix || '';
  const duration = 1500;
  const start = performance.now();

  function update(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
    const current = Math.round(target * eased);
    el.textContent = prefix + current.toLocaleString() + suffix;
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}
```

### Animation Rules

- Maximum transition duration: 0.8s (longer feels sluggish)
- Use `ease` or `ease-out` — never `linear` for UI animations
- Stagger delay between siblings: 80-120ms
- Only animate `opacity` and `transform` for performance
- Disable all animations in print stylesheet and for `prefers-reduced-motion`

---

## Interactive Elements

### Tabbed Content

Clickable tabs that show/hide content panels. Use data attributes to link tabs to panels:

```html
<div class="tabs">
  <button class="tab active" data-tab="overview">Overview</button>
  <button class="tab" data-tab="details">Details</button>
  <button class="tab" data-tab="results">Results</button>
</div>
<div class="tab-panel active" id="overview">...</div>
<div class="tab-panel" id="details">...</div>
<div class="tab-panel" id="results">...</div>
```

### Expandable Cards

Cards that expand on click to show more detail. The expand/collapse is CSS-only using `max-height` transition.

### Hover Tooltips

Use `::after` pseudo-elements with `data-tooltip` attributes. Pure CSS, no JS required.

### Inline SVG Charts

For data visualization, draw charts with inline SVG. This ensures zero dependencies.

**Bar chart pattern:**
```html
<svg viewBox="0 0 400 200" class="chart">
  <rect x="20" y="40" width="60" height="160" fill="var(--color-primary)" rx="4"/>
  <text x="50" y="35" text-anchor="middle" class="chart-label">85%</text>
  <!-- ... more bars -->
</svg>
```

**Donut chart pattern:**
```html
<svg viewBox="0 0 200 200" class="chart">
  <circle cx="100" cy="100" r="80" fill="none"
    stroke="var(--color-primary)" stroke-width="20"
    stroke-dasharray="377 503" stroke-dashoffset="0"
    transform="rotate(-90 100 100)"/>
  <!-- more segments with different dasharray/offset -->
</svg>
```

---

## Responsive Design

### Breakpoints

```css
/* Mobile: default styles (< 768px) */
/* Tablet */
@media (min-width: 768px) { ... }
/* Desktop */
@media (min-width: 1024px) { ... }
/* Large desktop */
@media (min-width: 1280px) { ... }
```

### Responsive Rules

- Hero title: 4rem on desktop, 2.5rem on mobile
- Split layouts: side-by-side on desktop, stacked on mobile
- Card grids: 3 columns on desktop, 2 on tablet, 1 on mobile
- Nav: horizontal on desktop, hamburger menu on mobile
- Big numbers: row on desktop, column on mobile
- Timeline: horizontal on desktop, vertical on mobile
- Padding: 6rem on desktop sections, 3rem on mobile

---

## Print Stylesheet

Always include a print-optimized stylesheet:

```css
@media print {
  * {
    animation: none !important;
    transition: none !important;
  }

  nav, .scroll-indicator, #speaker-notes, .tab:not(.active) {
    display: none !important;
  }

  section {
    page-break-before: always;
    min-height: auto;
    padding: 2rem;
  }

  section:first-of-type {
    page-break-before: avoid;
  }

  .tab-panel {
    display: block !important;
  }

  body {
    color: #000;
    background: #fff;
  }

  a { color: #000; text-decoration: underline; }
}
```

---

## Speaker Notes System

```javascript
document.addEventListener('keydown', (e) => {
  if (e.key === 'n' || e.key === 'N') {
    const notes = document.getElementById('speaker-notes');
    notes.classList.toggle('visible');
    updateNotesContent();
  }
});

function updateNotesContent() {
  const sections = document.querySelectorAll('section[data-notes]');
  const notesContainer = document.getElementById('speaker-notes-content');
  const scrollPos = window.scrollY + window.innerHeight / 2;

  let currentSection = sections[0];
  sections.forEach(section => {
    if (section.offsetTop <= scrollPos) currentSection = section;
  });

  notesContainer.textContent = currentSection.dataset.notes;
}

window.addEventListener('scroll', () => {
  if (document.getElementById('speaker-notes').classList.contains('visible')) {
    updateNotesContent();
  }
});
```

Style the notes panel:

```css
#speaker-notes {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.9);
  color: white;
  padding: 2rem;
  transform: translateY(100%);
  transition: transform 0.3s ease;
  z-index: 1000;
  max-height: 30vh;
  overflow-y: auto;
  font-size: 1rem;
  line-height: 1.6;
}

#speaker-notes.visible {
  transform: translateY(0);
}
```
