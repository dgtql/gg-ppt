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
  <a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.es.md">Español</a> | <a href="README.de.md">Deutsch</a> | <strong>Français</strong> | <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <img src="assets/comic.png" alt="L'évolution des présentations : des diapositives manuelles, aux diapositives générées par l'IA, aux HTML interactifs générés par l'IA" width="100%"/>
</p>

> On est en 2026. Vous avez une IA qui écrit du code en quelques secondes. Et vous êtes toujours... en train de faire glisser des boîtes de texte autour de diapositives ?

---

## Le problème que personne n'ose mentionner

Tout le monde déteste faire des PowerPoints. Mais on continue à les faire. Pourquoi ?

**"C'est ce que tout le monde utilise."** Votre patron attend un `.pptx`. Votre client attend un `.pptx`. La conférence attend un `.pptx`. Alors vous ouvrez PowerPoint, fixez une diapositive vierge, et vous commencez à faire glisser des boîtes. Encore.

**"Il n'y a pas de meilleure option."** Google Slides ? La même chose, avec un autre logo. Keynote ? La même chose, avec une police plus jolie. Prezi ? Parlons pas de Prezi.

**"L'IA peut faire des diapositives pour moi maintenant."** Et c'est là que ça devient absurde. On a créé la technologie de génération de texte la plus puissante de l'histoire humaine... et on l'utilise pour générer des fichiers `.pptx`. On utilise une Ferrari pour tirer un chariot à chevaux.

Pensez à ce qui se passe quand un LLM "génère un PowerPoint" :
1. L'IA génère du contenu structuré (texte, titres, points clés)
2. Un script le convertit en XML à l'intérieur d'un fichier `.zip` (c'est exactement ce qu'est un `.pptx`)
3. PowerPoint affiche ce XML sous forme de rectangles sur un canevas de taille fixe
4. Vous l'ouvrez, vous plissez les yeux, et vous commencez à corriger manuellement les alignements

**Pourquoi convertir la sortie de l'IA en un format de fichier de 1987, juste pour le rendre avec un logiciel propriétaire ?**

## La réponse évidente

L'IA génère du texte. Les navigateurs affichent le texte magnifiquement. Sautez l'intermédiaire.

<p align="center">
  <img src="assets/system-diagram.png" alt="Diagramme système : Entrée (texte, tableaux, graphiques, logo, URL de site web, .pptx) → IA (Claude, ChatGPT, Codex, Cursor) → HTML (fichier unique, zéro dépendance) → Navigateur (défilement, animation, graphiques, interaction)" width="100%"/>
</p>

C'est tout. Pas de `.pptx`. Pas de XML. Pas de PowerPoint. Pas de frais de licence. Juste une page web.

**gg-ppt** est un kit de prompts + un système de conception que n'importe quelle IA peut utiliser pour générer de magnifiques présentations HTML interactives. Compatible avec **Claude**, **ChatGPT**, **Codex**, **Cursor**, **Copilot**, ou n'importe quel LLM capable d'écrire du code. Une requête en entrée, un fichier `.html` en sortie. Ouvrez-le dans n'importe quel navigateur, sur n'importe quel appareil, en ligne ou hors ligne.

### Qu'est-ce qu'une "présentation HTML" ?

Ce ne sont pas des diapositives. Ce ne sont pas des rectangles sur un canevas. C'est une **page web fluide et interactive** — comme une page de destination de produit bien conçue que vous parcourez en défilant. Chaque section remplit la fenêtre d'affichage, les animations se déclenchent au défilement, les graphiques sont interactifs, et tout semble vivant.

Votre public ne clique pas 47 fois sur "Diapositive suivante". Il défile. Il clique sur les onglets. Il survole les graphiques. Il explore.

## Voir cela en action

Ouvrez [`assets/example.html`](assets/example.html) dans votre navigateur. C'est un examen trimestriel Q3 stylisé pour correspondre à **stripe.com**, généré à partir de :

- [`assets/sample-inputs/agenda.md`](assets/sample-inputs/agenda.md) — un plan textuel
- [`assets/sample-inputs/revenue_quarterly.csv`](assets/sample-inputs/revenue_quarterly.csv) — données de revenus → graphiques en barres auto-générés + tableaux
- [`assets/sample-inputs/customer_segments.csv`](assets/sample-inputs/customer_segments.csv) — données clients → graphique en anneau + cohortes de rétention
- `stripe.com` — URL du site → couleurs de marque, typographie, ombres et ambiance extraites automatiquement

Parcourez-le en défilant. Cliquez sur les onglets. Appuyez sur `N` pour les notes du présentateur. Appuyez sur `Ctrl+P` pour voir la mise en page d'impression PDF.

## Pourquoi PPT existe toujours (et pourquoi ça ne devrait pas)

| Pourquoi les gens utilisent PPT | Pourquoi ce n'est plus justifié |
|---|---|
| "Tout le monde sait l'utiliser" | Tout le monde sait aussi comment ouvrir un navigateur |
| "Mon entreprise a des modèles" | Déposez un logo ou collez l'URL de votre site — l'IA extrait automatiquement les couleurs de marque, les polices et le style |
| "J'ai besoin de graphiques et de tableaux" | HTML a des graphiques SVG intégrés, des tableaux interactifs, des compteurs animés — tout meilleur que SmartArt |
| "J'ai besoin de notes pour le présentateur" | Appuyez sur `N`. Les notes se synchronisent avec votre position de défilement |
| "Je dois le partager en tant que fichier" | C'est un seul fichier `.html`. Envoyez-le par email. Partagez-le sur Slack. Copiez-le sur USB. 142 KB |
| "J'ai besoin d'une version PDF" | `Ctrl+P`. Feuille de style d'impression intégrée avec sauts de page automatiques |
| "Je dois présenter hors ligne" | Zéro dépendance externe. Fonctionne depuis une clé USB sans internet |
| "Mon public s'attend à des diapositives" | Votre public s'attend à ne pas s'ennuyer. Donnez-lui quelque chose d'interactif |

## Ce que vous pouvez alimenter ?

| Entrée | Ce qui se passe |
|-------|-----------|
| **Un sujet ou un plan** | Le structure en sections, choisit des mises en page, rédige le narratif |
| **Notes de réunion ou texte long** | Distille les points clés en une présentation visuelle et défilante |
| **Données CSV / Excel** | Lit les données et génère des graphiques SVG intégrés (barres, lignes, anneaux, légendes de grands nombres) |
| **Images ou graphiques** | Les intègre en base64 pour que le fichier reste autonome |
| **Logo de l'entreprise** | Extrait les couleurs de marque et applique le thème à toute la présentation automatiquement |
| **Un fichier .pptx existant** | Extrait le texte + les images, restructure en page HTML fluide (pas une copie 1:1 des diapositives) |
| **Une URL de site** | "Rendez-le comme stripe.com" — récupère le CSS du site, extrait les couleurs, les polices, border-radius, les ombres et l'ambiance, puis applique le thème de votre présentation |
| **N'importe quelle combinaison** | "Voici le dernier trimestre, les chiffres mis à jour dans ce CSV, et notre nouveau logo — stylisez-le comme linear.app" |

## Démarrage rapide

### Utiliser avec Claude (Skill)

Copiez le dossier `gg-ppt` dans votre répertoire de compétences Claude :

```
~/.claude/skills/gg-ppt/
```

Demandez ensuite simplement à Claude de créer une présentation — la compétence se déclenche automatiquement.

### Utiliser avec ChatGPT / Codex / Copilot / Cursor / N'importe quel LLM

Collez le contenu de [`SKILL.md`](SKILL.md) en tant que contexte (ou en pièce jointe), puis demandez :

> "Lisez le SKILL.md et le guide de conception en pièce jointe. Créez une présentation HTML sur nos résultats Q3. Voici notre logo d'entreprise."

Ou plus simplement — collez simplement [`references/design-guide.md`](references/design-guide.md) comme contexte et dites :

> "Suivez ce système de conception pour créer une présentation HTML à fichier unique sur [votre sujet]. Rendez-la comme une page web défilante, pas des diapositives."

L'idée centrale fonctionne avec **n'importe quel LLM capable de générer du HTML**. Le SKILL.md et le guide de conception sont juste des instructions détaillées — n'importe quelle IA peut les suivre.

### Utiliser en autonome (Sans IA)

Les scripts fonctionnent indépendamment :

**Extraire les couleurs de marque à partir d'un logo :**
```bash
pip install Pillow
python scripts/extract_colors.py your-logo.png --css
```

**Correspondre au style visuel d'un site :**
```bash
pip install requests beautifulsoup4
python scripts/extract_style.py stripe.com --css
```

Les deux génèrent des propriétés CSS personnalisées que vous pouvez coller dans n'importe quel projet HTML.

### Thématisation de marque

Deux façons de thématiser votre présentation — toutes deux automatiques :

**À partir d'un logo** — déposez n'importe quelle image et la compétence extrait une palette de marque à 6 couleurs :

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

**À partir d'un site** — donnez une URL et il extrait le langage visuel complet du site : couleurs, polices, border-radius, ombres et ambiance générale :

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

Les couleurs se propagent dans chaque élément — barres de navigation, titres, couleurs des graphiques, états de survol, dégradés. "Rendez mon présentation comme Stripe" → ça marche d'emblée.

### Itérer

La compétence supporte les allers-retours naturels. Après la première version, parlez simplement :

- *"Rendez la section héros plus dramatique"*
- *"Changez les couleurs pour correspondre à ce nouveau logo"*
- *"Stylisez-le comme linear.app"*
- *"Ajoutez une section chronologique entre les statistiques et la comparaison"*
- *"Les chiffres ne sont pas corrects — utilisez 92%, 4,2x et 0 $"*
- *"Rendez-le plus minimaliste — moins de couleur, plus d'espace blanc"*

Votre IA lit le HTML existant et fait des modifications chirurgicales. Les sections que vous ne mentionnez pas restent intactes. C'est comme parler à un designer qui implémente vos commentaires instantanément.

## Ce que vous obtenez

Un seul fichier `.html` avec :

| Fonctionnalité | Détail |
|---------|--------|
| Animations déclenchées au défilement | Les sections apparaissent progressivement au défilement — fluide, pas criard |
| Thématisation des couleurs de marque | Extraites automatiquement à partir des logos, des URL de sites ou des palettes correspondant au sujet |
| Correspondance du style du site | Donnez une URL — extrait les couleurs, les polices, les ombres, border-radius, l'ambiance |
| Graphiques SVG interactifs | Barres, anneaux, lignes — pas de Chart.js, pas de D3, pas de CDN |
| Compteurs animés | Les grands nombres comptent jusqu'à la valeur quand ils arrivent en vue |
| Contenu par onglets | Cliquez pour basculer entre les vues au sein d'une section |
| Tableaux de données | Tableaux stylisés avec deltas codés par couleur (vert = hausse, rouge = baisse) |
| Notes du présentateur | Appuyez sur `N` pour basculer, synchronisées avec votre position de défilement |
| Imprimer en PDF | Feuille de style `@media print` avec sauts de page propres |
| Réactif | Bureau, tablette, téléphone — CSS Grid gère tout |
| Accessible | `prefers-reduced-motion`, HTML sémantique, contraste WCAG AA |
| Édition itérative | Modifications en langage naturel, pas de régénération complète |
| Zéro dépendance | Tout intégré — fonctionne hors ligne depuis une clé USB |

## PPT vs. gg-ppt

| | PowerPoint | gg-ppt |
|---|---|---|
| **Création** | Faites glisser manuellement des boîtes sur les diapositives | Décrivez en langage naturel, l'IA génère |
| **Sortie** | Format binaire propriétaire | Fichier `.html` unique |
| **Interactivité** | Cliquez sur "diapositive suivante" | Défilement, clics sur onglets, survol des graphiques, exploration |
| **Graphiques** | SmartArt statique | SVG animé avec étiquettes de données réelles |
| **Image de marque** | Appliquez un modèle, corrigez 47 choses | Déposez un logo ou collez une URL — couleurs, polices, ambiance extraites automatiquement |
| **Édition** | Rouvrez, réalignez, ré-exportez | "Assombrissez la section héros" → fait |
| **Partage** | PowerPoint/Viewer doit être installé | N'importe quel navigateur, n'importe quel appareil, n'importe quel OS |
| **Coût** | 159 $/an (Microsoft 365) | 0 $ |
| **Taille du fichier** | 5-50 MB | ~150 KB |
| **Hors ligne** | Oui | Oui |
| **Mobile** | À peine | Entièrement réactif |

## Pourquoi pas Reveal.js / Slidev / etc. ?

Ce sont de bons outils, mais ce sont essentiellement des **frameworks de diapositives** — ils imposent le même modèle mental page par page que PowerPoint. gg-ppt est différent :

- **Pas de framework** — pur HTML/CSS/JS, rien à installer ou configurer
- **Pas de diapositives** — c'est une page web fluide, comme une page de destination de produit
- **Natif pour l'IA** — conçu pour la génération HTML texte-vers-HTML par l'IA, pas la rédaction manuelle
- **Fichier unique** — pas d'étape de construction, pas de `npm install`, pas de fichiers de configuration
- **Pas de courbe d'apprentissage** — vous n'apprenez pas gg-ppt, vous décrivez juste ce que vous voulez

## Structure des fichiers

```
gg-ppt/
├── SKILL.md                          # Instructions pour l'IA (fonctionne avec n'importe quel LLM)
├── README.md                         # Anglais
├── README.zh-CN.md                   # Chinois simplifié
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # Système de conception complet
├── scripts/
│   ├── extract_colors.py             # Logo → palette de marque
│   └── extract_style.py              # URL du site → guide de style
└── assets/
    ├── example.html                   # Démo en direct (stylisé Stripe) — ouvrir dans le navigateur
    ├── comic.png                      # Bande dessinée de bannière pour README
    ├── system-diagram.png             # Diagramme d'architecture pour README
    └── sample-inputs/                 # Les entrées qui ont généré la démo
        ├── agenda.md                  # Plan textuel
        ├── revenue_quarterly.csv      # Données de revenus → graphiques
        └── customer_segments.csv      # Données clients → anneau + cohortes
```

## Le pari

PowerPoint a été inventé en 1987 pour remplacer les transparents de rétroprojecteur. Son modèle d'interaction principal — placer des boîtes sur des diapositives rectangulaires — n'a pas changé en 39 ans.

En 2026, nous avons une IA qui génère du contenu structuré et stylisé en quelques secondes. Le navigateur est le moteur de rendu le plus puissant jamais construit. Chaque appareil sur Terre en possède un.

**gg-ppt** parie que les présentations devraient simplement être des pages web. De magnifiques pages web interactives et personnalisées, que vous décrivez en langage naturel et que n'importe quelle IA construit pour vous.

GG, PowerPoint. Bien joué.

## Contribution

Trouvé un bug ? Vous avez une idée pour un nouveau motif de mise en page ? Les PRs sont bienvenues.

## Licence

MIT
