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
  <a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.es.md">Español</a> | <strong>Deutsch</strong> | <a href="README.fr.md">Français</a> | <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <img src="assets/comic.png" alt="Die Evolution von Präsentationen: von manueller PowerPoint über KI-generierte PowerPoint bis zu KI-generiertem interaktivem HTML" width="100%"/>
</p>

> Wir schreiben 2026. Die KI schreibt Code in Sekunden. Und du ziehst immer noch... Textfelder über Folien herum?

---

## Das Problem, das niemand ausspricht

Alle hassen es, PowerPoints zu machen. Aber wir machen sie trotzdem. Warum?

**"Das benutzt jeder."** Dein Chef erwartet eine `.pptx`. Dein Kunde erwartet eine `.pptx`. Die Konferenz erwartet eine `.pptx`. Also öffnest du PowerPoint, starrst auf eine leere Folie und fängst an, Boxen herumzuschieben. Schon wieder.

**"Es gibt keine bessere Alternative."** Google Slides? Das Gleiche in Anderem Logo. Keynote? Das Gleiche mit schönerem Font. Prezi? Lass uns nicht über Prezi sprechen.

**"KI kann mir jetzt Folien machen."** Und hier wird es absurd. Wir haben die mächtigste Text-Generierungstechnologie der Menschheitsgeschichte gebaut... und wir nutzen sie, um `.pptx`-Dateien zu generieren. Wir fahren einen Ferrari, um einen Pferdewagen zu ziehen.

Denk darüber nach, was passiert, wenn ein LLM "eine PowerPoint generiert":
1. KI generiert strukturierte Inhalte (Text, Überschriften, Bullet Points)
2. Ein Script konvertiert das zu XML innerhalb einer `.zip`-Datei (das ist wirklich das, was `.pptx` ist)
3. PowerPoint rendert dieses XML als Rechtecke auf einer festen Leinwand
4. Du öffnest es, kniffelst und fängst an, Ausrichtungen manuell zu beheben

**Warum konvertieren wir KI-Output in ein Format von 1987, nur um es in einer proprietären App zu rendern?**

## Die offensichtliche Antwort

KI generiert Text. Browser rendern Text wunderbar. Lass den Zwischenhändler weg.

<p align="center">
  <img src="assets/system-diagram.png" alt="Systemdiagramm: Input (Text, Tabellen, Diagramme, Logo, Website-URL, .pptx) → KI (Claude, ChatGPT, Codex, Cursor) → HTML (Einzeldatei, keine Abhängigkeiten) → Browser (Scrollen, Animationen, Diagramme, Interaktionen)" width="100%"/>
</p>

Das war's. Keine `.pptx`. Kein XML. Kein PowerPoint. Keine Lizenzgebühren. Nur eine Webseite.

**gg-ppt** ist ein Prompt-Kit + Design-System, das jede KI nutzen kann, um schöne, interaktive HTML-Präsentationen zu generieren. Funktioniert mit **Claude**, **ChatGPT**, **Codex**, **Cursor**, **Copilot** oder jedem LLM, das Code schreiben kann. Ein Prompt rein, eine `.html`-Datei raus. Öffne sie in jedem Browser, auf jedem Gerät, online oder offline.

### Was "HTML-Präsentation" wirklich bedeutet

Nicht Folien. Nicht Rechtecke auf einer Leinwand. Eine **fließende, interaktive Webseite** — wie eine polierte Product-Landing-Page zum Durchscrollen. Jeder Abschnitt füllt den Viewport, Animationen werden beim Scrollen ausgelöst, Diagramme sind interaktiv und das Ganze fühlt sich lebendig an.

Dein Publikum klickt nicht 47 Mal auf "Nächste Folie". Sie scrollen. Sie klicken auf Tabs. Sie hovern über Diagrammen. Sie erkunden.

## Sieh es in Aktion

Öffne [`assets/example.html`](assets/example.html) in deinem Browser. Es ist eine Q3-Geschäftsübersicht im Stripe-Stil, generiert aus:

- [`assets/sample-inputs/agenda.md`](assets/sample-inputs/agenda.md) — eine Text-Gliederung
- [`assets/sample-inputs/revenue_quarterly.csv`](assets/sample-inputs/revenue_quarterly.csv) — Umsatzdaten → automatisch generierte Balkendiagramme + Tabellen
- [`assets/sample-inputs/customer_segments.csv`](assets/sample-inputs/customer_segments.csv) — Kundendaten → Donut-Diagramm + Retention-Kohorten
- `stripe.com` — Website-URL → Markenfarben, Typographie, Schatten und Flair automatisch extrahiert

Scroll durch. Klick auf die Tabs. Drücke `N` für Sprechnotizen. Drücke `Ctrl+P`, um das Druck-zu-PDF-Layout zu sehen.

## Warum PowerPoint immer noch existiert (und warum es nicht sollte)

| Warum Leute PowerPoint nutzen | Warum das keinen Sinn mehr macht |
|---|---|
| "Jeder kann es benutzen" | Jeder kann auch einen Browser öffnen |
| "Mein Unternehmen hat Templates" | Lade dein Logo hoch oder füge deine Website-URL ein — KI extrahiert Markenfarben, Fonts und Stil automatisch |
| "Ich brauche Diagramme und Tabellen" | HTML hat inline SVG-Diagramme, interaktive Tabellen, animierte Zähler — alle besser als SmartArt |
| "Ich brauche Sprechnotizen" | Drücke `N`. Notizen sind mit deiner Scroll-Position synchronisiert |
| "Ich muss es als Datei teilen" | Es ist eine `.html`-Datei. Email, Slack, USB. 142KB |
| "Ich brauche eine PDF-Version" | `Ctrl+P`. Eingebautes Print-Stylesheet mit automatischen Seitenumbrüchen |
| "Ich muss offline präsentieren" | Keine externen Abhängigkeiten. Funktioniert von USB-Stick ohne Internet |
| "Mein Publikum erwartet Folien" | Dein Publikum erwartet, nicht gelangweilt zu sein. Gib ihnen etwas Interaktives |

## Was kannst du füttern?

| Input | Was passiert |
|-------|-------------|
| **Ein Thema oder eine Gliederung** | Strukturiert es in Abschnitte, wählt Layouts, schreibt die Erzählung |
| **Meeting-Notizen oder langer Text** | Destilliert Schlüsselpunkte in eine visuelle, scrollbare Präsentation |
| **CSV / Excel-Daten** | Liest die Daten und generiert inline SVG-Diagramme (Balken, Linie, Donut, große Zahlen) |
| **Bilder oder Diagramme** | Bettet sie als base64 ein, damit die Datei selbstenthalten bleibt |
| **Firmenlogo** | Extrahiert Markenfarben und thematisiert die gesamte Präsentation automatisch |
| **Eine vorhandene .pptx** | Extrahiert Text + Bilder, strukturiert in eine fließende HTML-Seite (keine 1:1-Folienkopie) |
| **Eine Website-URL** | "Mach es wie stripe.com" — holt die CSS der Website, extrahiert Farben, Fonts, Border-Radius, Schatten und Flair, dann thematisiert deine Präsentation dementsprechend |
| **Beliebige Kombination** | "Hier ist das letzte Quartal, aktualisierte Zahlen in dieser CSV und unser neues Logo — mach es wie linear.app" |

## Schnelleinstieg

### Verwendung mit Claude (Skill)

Kopiere den `gg-ppt`-Ordner in dein Claude-Skills-Verzeichnis:

```
~/.claude/skills/gg-ppt/
```

Dann bitte Claude einfach, eine Präsentation zu machen — der Skill wird automatisch ausgelöst.

### Verwendung mit ChatGPT / Codex / Copilot / Cursor / Jedem LLM

Füge den Inhalt von [`SKILL.md`](SKILL.md) als Kontext ein (oder hänge es an), dann eingeben:

> "Lese die angehängte SKILL.md und das Design-Guide. Erstelle eine HTML-Präsentation über unsere Q3-Ergebnisse. Hier ist unser Firmenlogo."

Oder einfacher — füge [`references/design-guide.md`](references/design-guide.md) als Kontext ein und sag:

> "Folge diesem Design-System, um eine Single-File HTML-Präsentation über [dein Thema] zu erstellen. Mach es zu einer scrollbaren Webseite, nicht zu Folien."

Die Kernidee funktioniert mit **jedem LLM, das HTML generieren kann**. Die SKILL.md und das Design-Guide sind nur detaillierte Anweisungen — jede KI kann sie befolgen.

### Eigenständige Verwendung (Keine KI)

Die Scripts funktionieren unabhängig:

**Markenfarben aus einem Logo extrahieren:**
```bash
pip install Pillow
python scripts/extract_colors.py your-logo.png --css
```

**Den visuellen Stil einer Website nachahmen:**
```bash
pip install requests beautifulsoup4
python scripts/extract_style.py stripe.com --css
```

Beide geben CSS-Custom-Properties aus, die du in jedes HTML-Projekt einfügen kannst.

### Marken-Theming

Zwei Wege, um deine Präsentation zu thematisieren — beide automatisch:

**Von einem Logo** — drop ein Bild ein und der Skill extrahiert eine 6-Farben-Brandpalette:

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

**Von einer Website** — gib eine URL ein und es extrahiert die gesamte visuelle Sprache der Website: Farben, Fonts, Border-Radius, Schatten und Gesamtvibe:

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

Farben fließen in jedes Element — Navigationsleisten, Überschriften, Diagrammfarben, Hover-Zustände, Gradienten. "Mach mein Deck wie Stripe" → es funktioniert einfach.

### Iteration

Der Skill unterstützt natürliches Hin-und-Her. Nach der ersten Version, sprich einfach:

- *"Mach die Hero-Section dramatischer"*
- *"Ändere die Farben für dieses neue Logo"*
- *"Stil wie linear.app"*
- *"Füge eine Timeline zwischen Stats und Vergleich hinzu"*
- *"Die Zahlen sind falsch — nutze 92%, 4,2x und $0"*
- *"Mach es minimaler — weniger Farbe, mehr Whitespace"*

Deine KI liest das bestehende HTML und macht chirurgische Edits. Abschnitte, die du nicht erwähnst, bleiben unverändert. Es ist wie mit einem Designer zu sprechen, der dein Feedback sofort umsetzt.

## Was du bekommst

Eine Single `.html`-Datei mit:

| Feature | Details |
|---------|---------|
| Scroll-ausgelöste Animationen | Abschnitte verblassen beim Scrollen rein — glatt, nicht übertrieben |
| Markenfarben-Theming | Automatisch extrahiert aus Logos, Website-URLs oder thema-abgestimmten Paletten |
| Website-Stil-Matching | Gib eine URL ein — extrahiert Farben, Fonts, Schatten, Border-Radius, Vibe |
| Interaktive SVG-Diagramme | Balken, Donut, Linie — kein Chart.js, kein D3, kein CDN |
| Animierte Zähler | Große Zahlen zählen hoch, wenn sie ins Sichtfenster scrollen |
| Tab-Inhalt | Klick zum Wechsel zwischen Ansichten in einem Abschnitt |
| Datentabellen | Stilisierte Tabellen mit farbkodierten Deltas (grün = auf, rot = ab) |
| Sprechnotizen | Drücke `N` zum Umschalten, synchronisiert mit deiner Scroll-Position |
| Druck zu PDF | `@media print`-Stylesheet mit sauberen Seitenumbrüchen |
| Responsiv | Desktop, Tablet, Handy — CSS Grid kümmert sich darum |
| Barrierefreiheit | `prefers-reduced-motion`, semantisches HTML, WCAG AA Kontrast |
| Iterative Bearbeitung | Edits in natürlicher Sprache, keine vollständige Neugenerierung |
| Keine Abhängigkeiten | Alles inline — funktioniert offline von einem USB-Stick |

## PowerPoint vs. gg-ppt

| | PowerPoint | gg-ppt |
|---|---|---|
| **Erstellung** | Manuell Boxen auf Folien ziehen | In Klartext beschreiben, KI generiert |
| **Output** | Proprietäres Binärformat | Single `.html`-Datei |
| **Interaktivität** | Klick "nächste Folie" | Scrollen, Tabs klicken, Diagramme hovern, erkunden |
| **Diagramme** | Statisches SmartArt | Animierte SVG mit echten Datenlabeln |
| **Branding** | Template anwenden, 47 Dinge beheben | Logo fallen lassen oder URL einfügen — Farben, Fonts, Vibe automatisch extrahiert |
| **Bearbeitung** | Neu öffnen, neu ausrichten, neu exportieren | "Mach das Hero dunkler" → erledigt |
| **Sharing** | Braucht PowerPoint/Viewer installiert | Jeder Browser, jedes Gerät, jedes OS |
| **Kosten** | $159/Jahr (Microsoft 365) | $0 |
| **Dateigröße** | 5-50 MB | ~150 KB |
| **Offline** | Ja | Ja |
| **Mobil** | Kaum | Vollständig responsiv |

## Warum nicht Reveal.js / Slidev / etc.?

Das sind solide Tools, aber sie sind immer noch **Folien-Frameworks** — sie setzen das gleiche Seite-für-Seite-Gedankenmodell wie PowerPoint durch. gg-ppt ist anders:

- **Kein Framework** — reines HTML/CSS/JS, nichts zum Installieren oder Konfigurieren
- **Keine Folien** — es ist eine fließende Webseite, wie eine Product-Landing-Page
- **KI-nativ** — designt für KI-Text-zu-HTML-Generierung, nicht für manuelle Erstellung
- **Single File** — kein Build-Schritt, kein `npm install`, keine Config-Dateien
- **Keine Lernkurve** — du lernst nicht gg-ppt, du beschreibst einfach, was du willst

## Dateien-Struktur

```
gg-ppt/
├── SKILL.md                          # KI-Anweisungen (funktioniert mit jedem LLM)
├── README.md                         # Englisch
├── README.zh-CN.md                   # Vereinfachtes Chinesisch
├── README.de.md                      # Du bist hier
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # Vollständiges Design-System
├── scripts/
│   ├── extract_colors.py             # Logo → Brand-Palette
│   └── extract_style.py              # Website-URL → Style-Guide
└── assets/
    ├── example.html                   # Live-Demo (Stripe-Stil) — im Browser öffnen
    ├── comic.png                      # Banner-Comic für README
    ├── system-diagram.png             # Architektur-Diagramm für README
    └── sample-inputs/                 # Die Inputs, die die Demo generiert haben
        ├── agenda.md                  # Text-Gliederung
        ├── revenue_quarterly.csv      # Umsatzdaten → Diagramme
        └── customer_segments.csv      # Kundendaten → Donut + Kohorten
```

## Die Wette

PowerPoint wurde 1987 erfunden, um Overhead-Projektor-Folien zu ersetzen. Sein Kerninteraktionsmodell — Boxen auf rechteckigen Folien platzieren — hat sich in 39 Jahren nicht verändert.

2026 haben wir KI, die strukturierte, gestylte Inhalte in Sekunden generiert. Der Browser ist die mächtigste Rendering-Engine, die je gebaut wurde. Jedes Gerät auf der Erde hat einen.

**gg-ppt** ist eine Wette, dass Präsentationen einfach Webseiten sein sollten. Schöne, interaktive, brandisierte Webseiten, die du in Klartext beschreibst und die jede KI für dich aufbaut.

GG, PowerPoint. Gut gemacht.

## Mitwirkung

Einen Bug gefunden? Hast du eine Idee für ein neues Layout-Pattern? PRs willkommen.

## Lizenz

MIT
