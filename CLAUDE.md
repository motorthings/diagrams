# Diagrams Repo — Charlie Fuller Visual Explainers

GitHub Pages collection at `motorthings.github.io/diagrams`. A folder of self-contained HTML "visual explainer" pages: architecture maps, process diagrams, audits, comparisons. Every page is one `.html` file — no build step, no external CSS/JS beyond Google Fonts and the Mermaid CDN.

## Working convention (read this first)

**Theme comes from this repo. Structure and layout come from the `visual-explainer` skill.**

- The page's visual identity (colors, fonts, typography scale, tone) follows this repo's system.
- How a page is *organized* — section architecture, rendering approach per content type (Mermaid vs pure-CSS flow vs HTML table vs card grids), hierarchy, and component decisions — defers to the `visual-explainer` skill's rules.
- The `diagrams` skill orchestrates the two: it reads the repo constraints, hands content to `visual-explainer` for generation, and enforces the repo-side overrides below.

The point of the split: the repo supplies a consistent, recognizable look; the skill supplies strong structure. Don't let a rigid template flatten the layout, and don't let the skill's aesthetic default override the repo palette.

## Generation workflow

When adding or rebuilding a page:
1. Invoke the `diagrams` skill (repo rules) then the `visual-explainer` skill (layout/structure).
2. Confirm the palette: default **Gulf Stream Racing** (below) unless the user picks custom.
3. Match the target: technical "how it works" page, executive/overview page, or pure linear flow.
4. Verify content against the actual system it documents — never draw from memory. Read the code/repo first (e.g. AESOP lives in `~/Documents/Vault/GitHub/aesop/`).
5. Add the page to its **category page** (`aesop.html`, `legal/index.html`, …). `index.html` is category-only; content pages are listed on their category landing. Fix the backlink.
6. Open it in a browser and run the verification checklist below.

## Theme — Gulf Stream Racing (repo default)

Fraunces (display/body) + Source Code Pro (mono/labels).

```
Light:  bg=#eef4f9  surface=#ffffff  text=#0a1628  primary=#e8621a  secondary=#4a90c4  metric=#0f766e
Dark:   bg=#0a1628  surface=#132240  text=#e8edf5  primary=#f37021  secondary=#6cace4  metric=#2dd4bf
```

Full set: `--primary` (orange), `--secondary` (blue), `--metric` (teal), `--amber`, `--violet`, `--rose`, `--slate`, each with a `--*-dim` variant (~8% light, ~12% dark). Use kebab-case CSS variable names on new pages.

Dark mode is a manual toggle via the `html.dark` class and `localStorage` key `diagram-theme`. **Never** `@media (prefers-color-scheme)`. Each page carries the sticky blur nav with a brand link + toggle.

## Required boilerplate (every page)

- **Favicon** in `<head>`: `<link rel="icon" href="../icon.svg">` — depth based on nesting.
- **Fixed backlink** top-left → its category page (content pages point at `aesop.html` etc., i.e. `../<category>.html`; only the category pages themselves point at `index.html`). The nav brand link points to the same parent.
- **Title tag**: `[Project] — [Page Name]` (e.g. `AESOP Studio — KB Audit Process`).
- **Meta description**: one sentence, 120–155 chars, present-tense, names the project.
- **No emoji** — Unicode/HTML entities only (`&#9788;` `&rarr;` `&mdash;` `&#9679;`).
- **`@media (prefers-reduced-motion: reduce)`** block when there are animations.

## Mermaid rules (only when Mermaid is the right call — see below)

- Init: `startOnLoad: true`, `theme: 'base'`, `look: 'classic'`. **Never** `layout: 'elk'` or `mermaid.registerLayoutLoaders` — ELK blanks the diagram on GitHub Pages.
- Check `html.dark` class for dark colors, not `matchMedia`.
- Quote every label `["..."]`; no `<br/>`, no emoji, escape `&` as `&amp;`.
- `classDef` uses hardcoded rgba/hex (Mermaid can't read CSS vars), then a CSS bridge overrides fills/strokes per theme. Always add the dark-mode `.mermaid text`/`.nodeLabel` override block.
- Every `.mermaid-wrap` gets zoom controls (+/−/reset), Ctrl/Cmd+scroll zoom, click-drag pan.

## Other layout notes

- **Diagram graphics follow the `visual-explainer` skill**, which delegates them to the `custom-svg-diagram` skill: machine-verified inline SVG (arrows clipped to box edges, no overlaps, no text on a line), generated from `layout()`/`assemble()` and gated with `check.mjs`. This is the default for architecture, data-flow, pipeline, and process diagrams. Don't hand-write a Mermaid chart — an unverified Mermaid is worse than none.
- Linear A→B→C flows: pure-CSS flowchart (no library). Branching/parallel/join process diagrams: custom SVG via `custom-svg-diagram`.
- Mermaid is reserved for where visual-explainer's rendering table calls for it (sequence, ER, state-machine). Keep it out of process/architecture maps.
- Structured data (issue lists, risk tiers, matrices): real `<table>` inside `.table-wrap` — not CSS-grid pretending.
- Page backlinks were standardized one step back to category pages (commit `e866e16`). When a category is renamed the content pages' backlinks follow.

## Verification checklist

Before committing: toggle dark/light (all text readable, SVG nodes re-colored via the palette vars), follow the backlink (right parent), resize to 375px (no overflow, grids stack), confirm the diagram rendered (not blank; custom-SVG diagrams must pass `check.mjs`/`verify.mjs`), no broken links, title matches h1, meta present, no emoji, `html.dark` not `@media`, reduced-motion present.

Brand voice: this is AESOP / legal / portfolio work — write like a human, call out the bullshit, short sentences, "you" not "organizations." The full voice spec lives in the `diagrams` skill and Charlie's brand-voice memory.

Backend / source repos referenced by these pages live under `~/Documents/Vault/GitHub/` (e.g. `aesop/`, `legal-os/`). Verify page claims against them before writing.
