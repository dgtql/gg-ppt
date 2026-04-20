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
  <a href="../README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <strong>Español</strong> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <img src="../assets/comic.png" alt="La evolución de las presentaciones: de crear diapositivas manualmente, a presentaciones generadas por IA, a HTML interactivo generado por IA" width="100%"/>
</p>

> Estamos en 2026. Tienes una IA que escribe código en segundos. ¿Y todavía estás... arrastrando cuadros de texto por las diapositivas?

---

## El Problema que Nadie Menciona

Todos odiamos hacer PowerPoints. Pero seguimos haciéndolo. ¿Por qué?

**"Es lo que todos usan."** Tu jefe quiere un `.pptx`. Tu cliente quiere un `.pptx`. La conferencia quiere un `.pptx`. Así que abres PowerPoint, miras una diapositiva en blanco y empiezas a arrastrar cuadros. Otra vez.

**"No hay opciones mejores."** ¿Google Slides? Lo mismo con otro logo. ¿Keynote? Lo mismo con una fuente más bonita. ¿Prezi? Mejor no hablamos de Prezi.

**"Ahora la IA puede hacer diapositivas por mí."** Y aquí es donde se vuelve absurdo. Construimos la tecnología de generación de texto más poderosa de la historia humana... y la estamos usando para generar archivos `.pptx`. Es como usar un Ferrari para tirar de un carro de caballos.

Piensa en lo que sucede cuando un LLM "genera un PowerPoint":
1. La IA genera contenido estructurado (texto, títulos, puntos clave)
2. Un script lo convierte en XML dentro de un archivo `.zip` (eso es lo que `.pptx` realmente es)
3. PowerPoint renderiza ese XML como rectángulos en un lienzo de tamaño fijo
4. Lo abres, entrecerras los ojos y empiezas a arreglar alineaciones manualmente

**¿Por qué convertimos la salida de la IA en un formato de archivo de 1987, solo para renderizarlo en una aplicación propietaria?**

## La Respuesta Obvia

La IA genera texto. Los navegadores renderizan texto hermosamente. Salta al intermediario.

<p align="center">
  <img src="../assets/system-diagram.png" alt="Diagrama del sistema: Entrada (texto, tablas, gráficos, logo, URL de sitio web, .pptx) → IA (Claude, ChatGPT, Codex, Cursor) → HTML (archivo único, cero dependencias) → Navegador (desplazamiento, animaciones, gráficos, interacción)" width="100%"/>
</p>

Eso es. Sin `.pptx`. Sin XML. Sin PowerPoint. Sin cuotas de licencia. Solo una página web.

**gg-ppt** es un kit de prompts + un sistema de diseño que cualquier IA puede usar para generar presentaciones HTML hermosas e interactivas. Funciona con **Claude**, **ChatGPT**, **Codex**, **Cursor**, **Copilot**, o cualquier LLM que pueda escribir código. Una solicitud de entrada, un archivo `.html` de salida. Ábrelo en cualquier navegador, en cualquier dispositivo, en línea u sin conexión.

### Qué significa realmente "presentación HTML"

No son diapositivas. No son rectángulos en un lienzo. Es una **página web fluida e interactiva** — como una página de destino de producto pulida por la que se desplaza. Cada sección llena la ventana gráfica, las animaciones se activan al desplazarse, los gráficos son interactivos y todo se siente vivo.

Tu audiencia no hace clic en "Siguiente" 47 veces. Se desplaza. Hace clic en pestañas. Pasa el ratón sobre gráficos. Explora.

## Véalo en Acción

Abre [`assets/example.html`](../assets/example.html) en tu navegador. Es una revisión de negocios del Q3 diseñada para que coincida con **stripe.com**, generada a partir de:

- [`assets/sample-inputs/agenda.md`](../assets/sample-inputs/agenda.md) — un esquema de texto
- [`assets/sample-inputs/revenue_quarterly.csv`](../assets/sample-inputs/revenue_quarterly.csv) — datos de ingresos → gráficos de barras generados automáticamente + tablas
- [`assets/sample-inputs/customer_segments.csv`](../assets/sample-inputs/customer_segments.csv) — datos de clientes → gráfico de donuts + cohortes de retención
- `stripe.com` — URL de sitio web → colores de marca, tipografía, sombras y vibra extraídos automáticamente

Desplázate por él. Haz clic en las pestañas. Presiona `N` para notas del orador. Presiona `Ctrl+P` para ver el diseño de impresión en PDF.

## Por Qué PowerPoint Aún Existe (Y Por Qué No Debería)

| Por qué la gente usa PPT | Por qué ya no tiene sentido |
|---|---|
| "Todos saben cómo usarlo" | Todos también saben cómo abrir un navegador |
| "Mi empresa tiene plantillas" | Coloca un logo o pega tu URL de sitio web — la IA extrae colores de marca, fuentes y estilo automáticamente |
| "Necesito gráficos y tablas" | HTML tiene gráficos SVG en línea, tablas interactivas, contadores animados — todo mejor que SmartArt |
| "Necesito notas del orador" | Presiona `N`. Las notas se sincronizan con tu posición de desplazamiento |
| "Necesito compartirlo como archivo" | Es un archivo `.html`. Envíalo por correo. Slack. USB. 142KB |
| "Necesito una versión en PDF" | `Ctrl+P`. Hoja de estilos de impresión integrada con saltos de página automáticos |
| "Necesito presentar sin conexión" | Cero dependencias externas. Funciona desde una memoria USB sin internet |
| "Mi audiencia espera diapositivas" | Tu audiencia espera no aburrirse. Dale algo interactivo |

## ¿Qué Puedes Alimentarle?

| Entrada | Qué Sucede |
|-------|-----------|
| **Un tema o esquema** | Lo estructura en secciones, elige diseños, escribe la narrativa |
| **Notas de reunión o texto largo** | Destila puntos clave en una presentación visual y desplazable |
| **Datos CSV / Excel** | Lee los datos y genera gráficos SVG en línea (barras, líneas, donuts, callouts de números grandes) |
| **Imágenes o gráficos** | Los incrusta como base64 para que el archivo se mantenga autónomo |
| **Logo de la empresa** | Extrae colores de marca y tema de toda la presentación automáticamente |
| **Un archivo .pptx existente** | Extrae texto + imágenes, reestructura en una página HTML fluida (no una copia 1:1 de diapositivas) |
| **Una URL de sitio web** | "Hazlo parecer a stripe.com" — obtiene el CSS del sitio, extrae colores, fuentes, border-radius, sombras y vibra, luego tema tu presentación para que coincida |
| **Cualquier combinación** | "Aquí está la presentación del trimestre pasado, números actualizados en este CSV, y nuestro nuevo logo — estilízalo como linear.app" |

## Inicio Rápido

### Usar con Claude (Skill)

Copia la carpeta `gg-ppt` en tu directorio de skills de Claude:

```
~/.claude/skills/gg-ppt/
```

Luego simplemente pídele a Claude que haga una presentación — el skill se activa automáticamente.

### Usar con ChatGPT / Codex / Copilot / Cursor / Cualquier LLM

Pega el contenido de [`SKILL.md`](../SKILL.md) como contexto (o adjúntalo), luego solicita:

> "Lee el SKILL.md adjunto y la guía de diseño. Crea una presentación HTML sobre nuestros resultados del Q3. Aquí está nuestro logo de la empresa."

O más simple — solo pega [`references/design-guide.md`](../references/design-guide.md) como contexto y di:

> "Sigue este sistema de diseño para crear una presentación HTML de archivo único sobre [tu tema]. Hazla una página web desplazable, no diapositivas."

La idea central funciona con **cualquier LLM que pueda generar HTML**. El SKILL.md y la guía de diseño son solo instrucciones detalladas — cualquier IA puede seguirlas.

### Usar Independientemente (Sin IA)

Los scripts funcionan de forma independiente:

**Extrae colores de marca de un logo:**
```bash
pip install Pillow
python scripts/extract_colors.py your-logo.png --css
```

**Coincide con el estilo visual de un sitio web:**
```bash
pip install requests beautifulsoup4
python scripts/extract_style.py stripe.com --css
```

Ambos generan propiedades CSS personalizadas que puedes pegar en cualquier proyecto HTML.

### Tema de Marca

Dos formas de tema tu presentación — ambas automáticas:

**De un logo** — coloca cualquier imagen y el skill extrae una paleta de marca de 6 colores:

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

**De un sitio web** — dale una URL y extrae todo el lenguaje visual del sitio: colores, fuentes, border-radius, sombras y vibra general:

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

Los colores fluyen hacia cada elemento — barras de navegación, títulos, colores de gráficos, estados de desplazamiento, gradientes. "Haz que mi presentación parezca Stripe" → simplemente funciona.

### Iterar

El skill admite conversación natural y de ida y vuelta. Después de la primera versión, solo habla:

- *"Haz la sección de héroe más dramática"*
- *"Cambia los colores para que coincidan con este nuevo logo"*
- *"Estilízalo como linear.app"*
- *"Agrega una sección de línea de tiempo entre las estadísticas y la comparación"*
- *"Los números son incorrectos — usa 92%, 4.2x y $0"*
- *"Hazlo más minimalista — menos color, más espacio en blanco"*

Tu IA lee el HTML existente y hace ediciones quirúrgicas. Las secciones que no menciones permanecen intactas. Es como hablar con un diseñador que implementa tu retroalimentación instantáneamente.

## Lo Que Obtienes

Un archivo `.html` único con:

| Característica | Detalle |
|--------|--------|
| Animaciones desencadenadas por desplazamiento | Las secciones se desvanecen cuando se desplazan — suave, no cursi |
| Tema de color de marca | Auto-extraído de logos, URLs de sitios web o paletas coincidentes por tema |
| Coincidencia de estilo de sitio web | Dale una URL — extrae colores, fuentes, sombras, border-radius, vibra |
| Gráficos SVG interactivos | Barras, donuts, líneas — sin Chart.js, sin D3, sin CDN |
| Contadores animados | Números grandes que cuentan hacia arriba cuando se desplazan a la vista |
| Contenido con pestañas | Haz clic para cambiar vistas dentro de una sección |
| Tablas de datos | Tablas con estilo con deltas codificados por color (verde = arriba, rojo = abajo) |
| Notas del orador | Presiona `N` para alternar, sincronizado con tu posición de desplazamiento |
| Imprimir en PDF | Hoja de estilos `@media print` con saltos de página limpios |
| Responsivo | Escritorio, tableta, teléfono — CSS Grid lo maneja |
| Accesible | `prefers-reduced-motion`, HTML semántico, contraste WCAG AA |
| Edición iterativa | Ediciones en lenguaje simple, sin regeneración completa |
| Cero dependencias | Todo en línea — funciona sin conexión desde una memoria USB |

## PPT vs. gg-ppt

| | PowerPoint | gg-ppt |
|---|---|---|
| **Creación** | Arrastra manualmente cuadros en diapositivas | Describe en texto simple, la IA genera |
| **Salida** | Formato binario propietario | Archivo `.html` único |
| **Interactividad** | Haz clic en "siguiente diapositiva" | Desplázate, haz clic en pestañas, pasa el ratón sobre gráficos, explora |
| **Gráficos** | SmartArt estático | SVG animado con etiquetas de datos reales |
| **Marca** | Aplica plantilla, arregla 47 cosas | Coloca logo o pega una URL — colores, fuentes, vibra auto-extraídos |
| **Edición** | Reabre, realinea, reexporta | "Haz el héroe más oscuro" → listo |
| **Compartición** | Se necesita PowerPoint/Viewer instalado | Cualquier navegador, cualquier dispositivo, cualquier SO |
| **Costo** | $159/año (Microsoft 365) | $0 |
| **Tamaño de archivo** | 5-50 MB | ~150 KB |
| **Sin conexión** | Sí | Sí |
| **Móvil** | Apenas | Completamente responsivo |

## ¿Por Qué No Reveal.js / Slidev / etc.?

Esas son herramientas sólidas, pero son esencialmente **marcos de diapositivas** — imponen el mismo modelo mental página por página que PowerPoint. gg-ppt es diferente:

- **Sin marco** — HTML/CSS/JS puro, nada que instalar o configurar
- **No son diapositivas** — es una página web fluida, como una página de destino de producto
- **Nativa de IA** — diseñada para generación de texto a HTML por IA, no autoría manual
- **Archivo único** — sin paso de compilación, sin `npm install`, sin archivos de configuración
- **Sin curva de aprendizaje** — no aprendes gg-ppt, solo describes lo que quieres

## Estructura de Archivos

```
gg-ppt/
├── SKILL.md                          # Instrucciones de IA (funciona con cualquier LLM)
├── README.md                         # Inglés
├── README.zh-CN.md                   # Chino simplificado
├── README.es.md                      # Español (estás aquí)
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # Sistema de diseño completo
├── scripts/
│   ├── extract_colors.py             # Logo → paleta de marca
│   └── extract_style.py              # URL de sitio web → guía de estilo
└── assets/
    ├── example.html                   # Demostración en vivo (con estilo Stripe) — abre en navegador
    ├── comic.png                      # Cómic de banner para README
    ├── system-diagram.png             # Diagrama de arquitectura para README
    └── sample-inputs/                 # Las entradas que generaron la demostración
        ├── agenda.md                  # Esquema de texto
        ├── revenue_quarterly.csv      # Datos de ingresos → gráficos
        └── customer_segments.csv      # Datos de clientes → donuts + cohortes
```

## La Apuesta

PowerPoint fue inventado en 1987 para reemplazar las transparencias de proyectores. Su modelo de interacción central — coloca cuadros en diapositivas rectangulares — no ha cambiado en 39 años.

En 2026, tenemos IA que genera contenido estructurado y con estilo en segundos. El navegador es el motor de renderización más poderoso jamás construido. Todos los dispositivos del planeta tienen uno.

**gg-ppt** es una apuesta de que las presentaciones deberían ser simplemente páginas web. Hermosas, interactivas, páginas web de marca que describes en texto simple y cualquier IA construye para ti.

GG, PowerPoint. Bien jugado.

## Contribuyendo

¿Encontraste un error? ¿Tienes una idea para un nuevo patrón de diseño? Los PRs son bienvenidos.

## Licencia

MIT
