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
  <a href="README.md">English</a> | <strong>简体中文</strong> | <a href="README.es.md">Español</a> | <a href="README.de.md">Deutsch</a> | <a href="README.fr.md">Français</a> | <a href="README.ru.md">Русский</a>
</p>

<p align="center">
  <img src="assets/comic.png" alt="演示文稿的进化：从手动做PPT，到AI生成PPT，再到AI生成交互式HTML" width="100%"/>
</p>

> 都2026年了，AI几秒钟就能写代码。你居然还在……拖文本框做PPT？

---

## 没人说出口的问题

所有人都讨厌做PPT，但所有人都在做。为什么？

**"大家都用它。"** 老板要 `.pptx`，客户要 `.pptx`，大会要 `.pptx`。于是你打开PowerPoint，盯着空白幻灯片，又开始拖文本框。又来了。

**"没有更好的选择。"** Google Slides？换了个logo的同一个东西。Keynote？换了个字体的同一个东西。Prezi？别提了。

**"AI现在能帮我做PPT了。"** 这才是最荒谬的。我们造出了人类历史上最强大的文本生成技术……然后用它来生成 `.pptx` 文件。这就像开着法拉利去拉马车。

想想LLM"生成PPT"时到底发生了什么：
1. AI生成结构化内容（文字、标题、要点）
2. 脚本把它转换成 `.zip` 文件里的XML（没错，`.pptx` 本质上就是这个）
3. PowerPoint把XML渲染成固定画布上的矩形
4. 你打开它，眯着眼睛，开始手动调对齐

**为什么要把AI的输出塞进一个1987年的文件格式，再用专有软件来渲染？**

## 显而易见的答案

AI生成文本。浏览器渲染文本。跳过中间人。

<p align="center">
  <img src="assets/system-diagram.png" alt="系统架构图：输入（文本、表格、图表、Logo、网站URL、.pptx）→ AI（Claude、ChatGPT、Codex、Cursor）→ HTML（单文件、零依赖）→ 浏览器（滚动、动画、图表、交互）" width="100%"/>
</p>

就这样。不需要 `.pptx`，不需要XML，不需要PowerPoint，不需要授权费。只是一个网页。

**gg-ppt** 是一套提示词工具包 + 设计系统，任何AI都能用它生成精美的交互式HTML演示。支持 **Claude**、**ChatGPT**、**Codex**、**Cursor**、**Copilot**，或任何能写代码的LLM。一句话输入，一个 `.html` 文件输出。在任何浏览器、任何设备上打开，在线离线均可。

### "HTML演示"到底是什么意思

不是幻灯片。不是画布上的矩形。而是一个**流畅的交互式网页** —— 就像精心制作的产品着陆页。每个板块占满视窗，滚动触发动画，图表可交互，整个页面充满生命力。

你的观众不用点47次"下一页"。他们滚动、点击标签页、悬停查看图表、自由探索。

## 看看效果

在浏览器中打开 [`assets/example.html`](assets/example.html)。这是一份模仿 **stripe.com** 风格的Q3季度回顾，由以下输入生成：

- [`assets/sample-inputs/agenda.md`](assets/sample-inputs/agenda.md) —— 文字大纲
- [`assets/sample-inputs/revenue_quarterly.csv`](assets/sample-inputs/revenue_quarterly.csv) —— 营收数据 → 自动生成柱状图 + 表格
- [`assets/sample-inputs/customer_segments.csv`](assets/sample-inputs/customer_segments.csv) —— 客户数据 → 环形图 + 留存分析
- `stripe.com` —— 网站URL → 自动提取品牌色、字体、阴影和设计风格

滚动浏览，点击标签页，按 `N` 查看演讲备注，按 `Ctrl+P` 查看PDF打印布局。

## 为什么PPT还存在（以及为什么不该存在）

| 人们用PPT的理由 | 为什么不再成立 |
|---|---|
| "大家都会用" | 大家也都会打开浏览器 |
| "公司有模板" | 放个Logo或粘贴网站URL —— AI自动提取品牌色、字体和风格 |
| "我需要图表和表格" | HTML有内联SVG图表、交互式表格、动画计数器 —— 全都比SmartArt好 |
| "我需要演讲备注" | 按 `N` 即可，备注与滚动位置同步 |
| "我需要作为文件分享" | 就一个 `.html` 文件。邮件发、Slack发、U盘拷，只有142KB |
| "我需要PDF版本" | `Ctrl+P`，内置打印样式表，自动分页 |
| "我需要离线演示" | 零外部依赖，U盘里没网也能用 |
| "观众期望看到幻灯片" | 观众期望的是不无聊。给他们看点有交互性的 |

## 可以输入什么？

| 输入 | 会发生什么 |
|------|-----------|
| **主题或大纲** | 自动组织成板块，选择布局，撰写叙事 |
| **会议纪要或长文本** | 提炼要点，生成可视化的滚动式演示 |
| **CSV / Excel数据** | 读取数据，生成内联SVG图表（柱状图、折线图、环形图、大数字标注） |
| **图片或图表** | 以base64嵌入，文件保持自包含 |
| **公司Logo** | 提取品牌色，自动为整个演示设定主题 |
| **现有的 .pptx 文件** | 提取文字和图片，重构为流畅的HTML页面（不是逐页复制） |
| **网站URL** | "做成stripe.com的风格" —— 抓取网站CSS，提取颜色、字体、圆角、阴影和设计风格，然后应用到你的演示 |
| **任意组合** | "这是上季度的PPT，这个CSV是更新的数据，这是新Logo —— 风格照linear.app来" |

## 快速开始

### 配合Claude使用（Skill）

将 `gg-ppt` 文件夹复制到Claude的skills目录：

```
~/.claude/skills/gg-ppt/
```

然后直接让Claude做演示 —— skill会自动触发。

### 配合ChatGPT / Codex / Copilot / Cursor / 任何LLM使用

将 [`SKILL.md`](SKILL.md) 的内容作为上下文粘贴（或附件上传），然后输入：

> "阅读附件中的SKILL.md和设计指南，为我们的Q3业绩创建一个HTML演示。这是我们公司的Logo。"

更简单的方式 —— 直接粘贴 [`references/design-guide.md`](references/design-guide.md) 作为上下文，然后说：

> "按照这个设计系统，为[你的主题]创建一个单文件HTML演示。做成滚动式网页，不要幻灯片。"

核心理念适用于**任何能生成HTML的LLM**。SKILL.md和设计指南只是详细说明 —— 任何AI都能遵循。

### 独立使用（不需要AI）

脚本可以独立运行：

**从Logo提取品牌色：**
```bash
pip install Pillow
python scripts/extract_colors.py your-logo.png --css
```

**匹配网站的视觉风格：**
```bash
pip install requests beautifulsoup4
python scripts/extract_style.py stripe.com --css
```

两个脚本都输出CSS自定义属性，可以直接粘贴到任何HTML项目。

### 品牌主题

两种自动化的主题设定方式：

**从Logo** —— 放入任何图片，skill自动提取6色品牌调色板：

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

**从网站** —— 给一个URL，自动提取整个视觉语言：颜色、字体、圆角、阴影和整体风格：

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

颜色会渗透到每一个元素 —— 导航栏、标题、图表配色、悬停状态、渐变。"做成Stripe的风格" → 直接搞定。

### 迭代优化

skill支持自然的对话式迭代。生成第一版后，直接说：

- *"让首屏更有冲击力"*
- *"换成这个新Logo的配色"*
- *"做成linear.app的风格"*
- *"在数据和对比之间加一个时间线"*
- *"数字不对 —— 改成92%、4.2x和$0"*
- *"更简约一点 —— 少点颜色，多点留白"*

AI读取现有HTML，做精准修改。你没提到的部分保持不变。就像跟一个设计师对话，ta会即时实现你的反馈。

## 你会得到什么

一个 `.html` 文件，包含：

| 功能 | 详情 |
|------|------|
| 滚动触发动画 | 板块滚动进入时淡入 —— 流畅而不花哨 |
| 品牌色主题 | 从Logo、网站URL或主题匹配的调色板自动提取 |
| 网站风格匹配 | 给一个URL —— 提取颜色、字体、阴影、圆角、风格 |
| 交互式SVG图表 | 柱状图、环形图、折线图 —— 无需Chart.js、D3或CDN |
| 动画计数器 | 大数字在滚动进入视窗时自动计数 |
| 标签页内容 | 点击切换板块内的不同视图 |
| 数据表格 | 带颜色标识的增减变化（绿色=上升，红色=下降） |
| 演讲备注 | 按 `N` 切换显示，与滚动位置同步 |
| 打印PDF | `@media print` 样式表，自动分页 |
| 响应式 | 桌面、平板、手机 —— CSS Grid搞定 |
| 无障碍 | `prefers-reduced-motion`、语义化HTML、WCAG AA对比度 |
| 迭代编辑 | 用自然语言修改，无需重新生成 |
| 零依赖 | 一切内联 —— U盘离线也能用 |

## PPT vs. gg-ppt

| | PowerPoint | gg-ppt |
|---|---|---|
| **创建** | 手动在幻灯片上拖文本框 | 用自然语言描述，AI生成 |
| **输出** | 专有二进制格式 | 单个 `.html` 文件 |
| **交互** | 点击"下一页" | 滚动、点击标签页、悬停查看图表、自由探索 |
| **图表** | 静态SmartArt | 带真实数据标签的动画SVG |
| **品牌** | 应用模板，然后修47个地方 | 放Logo或粘贴URL —— 颜色、字体、风格自动提取 |
| **编辑** | 重新打开、重新对齐、重新导出 | "把首屏调暗一点" → 搞定 |
| **分享** | 需要安装PowerPoint/Viewer | 任何浏览器、任何设备、任何系统 |
| **费用** | $159/年 (Microsoft 365) | $0 |
| **文件大小** | 5-50 MB | ~150 KB |
| **离线** | 支持 | 支持 |
| **移动端** | 勉强能用 | 完全响应式 |

## 为什么不用Reveal.js / Slidev等？

这些都是不错的工具，但它们本质上还是**幻灯片框架** —— 还是PPT那套逐页翻页的思维模式。gg-ppt不同：

- **无框架** —— 纯HTML/CSS/JS，无需安装或配置
- **不是幻灯片** —— 是流畅的网页，像产品着陆页
- **AI原生** —— 为AI文本到HTML的生成而设计，不是手动编写
- **单文件** —— 无需构建、无需 `npm install`、无需配置文件
- **零学习曲线** —— 你不用学gg-ppt，只需描述你想要什么

## 文件结构

```
gg-ppt/
├── SKILL.md                          # AI指令（适用于任何LLM）
├── README.md                         # 英文说明
├── README.zh-CN.md                   # 简体中文说明（你在这里）
├── LICENSE                           # MIT
├── references/
│   └── design-guide.md               # 完整设计系统
├── scripts/
│   ├── extract_colors.py             # Logo → 品牌调色板
│   └── extract_style.py              # 网站URL → 风格指南
└── assets/
    ├── example.html                   # 在线演示（Stripe风格）—— 在浏览器中打开
    ├── comic.png                      # README横幅漫画
    ├── system-diagram.png             # 架构图
    └── sample-inputs/                 # 生成演示用的示例输入
        ├── agenda.md                  # 文字大纲
        ├── revenue_quarterly.csv      # 营收数据 → 图表
        └── customer_segments.csv      # 客户数据 → 环形图 + 留存分析
```

## 我们的判断

PowerPoint诞生于1987年，用来替代投影胶片。它的核心交互模式 —— 在固定大小的矩形上放置方框 —— 39年来从未改变。

2026年，我们有了能在几秒钟内生成结构化、带样式内容的AI。浏览器是有史以来最强大的渲染引擎。地球上每台设备都有一个。

**gg-ppt** 赌的是：演示文稿应该就是网页。精美的、交互式的、品牌化的网页，你用自然语言描述，AI帮你构建。

GG, PowerPoint.

## 贡献

发现Bug？有新布局模式的想法？欢迎PR。

## 许可证

MIT
