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
2. Confirm the accent: pick the section's existing pair (see Theme below), don't invent a new one.
3. Match the target: technical "how it works" page, executive/overview page, or pure linear flow.
4. Verify content against the actual system it documents — never draw from memory. Read the code/repo first (e.g. AESOP lives in `~/Documents/Vault/GitHub/aesop/`).
5. Add the page to its **category page** (`aesop.html`, `legal/index.html`, …). `index.html` is category-only; content pages are listed on their category landing. Fix the backlink.
6. Open it in a browser and run the verification checklist below.

## Theme — Mulish, light-first

**This repo is Mulish-only. Never generate a Gulf Stream, Fraunces, Ledger, or Survey page here.**

The full spec lives at `~/.claude/skills/visual-explainer/references/mulish-style.md` — **read it before building or restyling any page.**

One family does everything — **Mulish** (`ital,wght@0,300;0,400;0,600;0,700;0,800;1,400`), headings 800 with `letter-spacing:-1px`. Use kebab-case CSS variable names.

**Polarity: `:root` holds the dark tokens, `html.light` overrides, and every page ships `<html class="light">`.** Never `html.dark`, never `@media (prefers-color-scheme)`. There is no theme toggle.

**Accent is a parameter, not a palette.** Each category owns ONE accent pair used on its index page *and* every leaf, so the section reads as a family: legal = rose, csm = blue, aesop = orange, root/non-category = indigo, all against a teal metric. A section may also re-tint the neutral ramp to keep its identity (aesop keeps warm paper) — copy the token block verbatim from an existing page in that section rather than inventing one.

## Required boilerplate (every page)

- **Favicon** in `<head>`: `<link rel="icon" href="../icon.svg">` — depth based on nesting.
- **Breadcrumb `.crumbs`** at the top of the transparent nav → `Index / Section / Page` (content pages point at `aesop.html` etc.; only the category pages themselves point at `index.html`). This is the only back-navigation — no fixed backlink, no theme toggle. 17 older `legal/` pages still carry a fixed backlink; `.crumbs` is the canonical pattern.
- **Title tag**: `[Project] — [Page Name]` (e.g. `AESOP Studio — KB Audit Process`).
- **Meta description**: one sentence, 120–155 chars, present-tense, names the project.
- **No emoji** — Unicode/HTML entities only (`&#9788;` `&rarr;` `&mdash;` `&#9679;`).
- **`@media (prefers-reduced-motion: reduce)`** block when there are animations.

## Mermaid rules (only when Mermaid is the right call — see below)

- Init: `startOnLoad: true`, `theme: 'base'`, `look: 'classic'`. **Never** `layout: 'elk'` or `mermaid.registerLayoutLoaders` — ELK blanks the diagram on GitHub Pages.
- Check the `html.light` class for light colors, not `matchMedia`.
- Quote every label `["..."]`; no `<br/>`, no emoji, escape `&` as `&amp;`.
- `classDef` uses hardcoded rgba/hex (Mermaid can't read CSS vars), then a CSS bridge overrides fills/strokes per theme. Always add the light-mode `.mermaid text`/`.nodeLabel` override block — without it the labels fail contrast.
- Every `.mermaid-wrap` gets zoom controls (+/−/reset), Ctrl/Cmd+scroll zoom, click-drag pan.

## Other layout notes

- **Diagram graphics follow the `visual-explainer` skill**, which delegates them to the `custom-svg-diagram` skill: machine-verified inline SVG (arrows clipped to box edges, no overlaps, no text on a line), generated from `layout()`/`assemble()` and gated with `check.mjs`. This is the default for architecture, data-flow, pipeline, and process diagrams. Don't hand-write a Mermaid chart — an unverified Mermaid is worse than none.
- Linear A→B→C flows: pure-CSS flowchart (no library). Branching/parallel/join process diagrams: custom SVG via `custom-svg-diagram`.
- **Replacing a diagram means redrawing that diagram, node for node.** When a source page contains a rendered process/flow diagram (Mermaid, SVG, or CSS boxes), reproduce the EXACT SAME set of boxes/nodes and their connections, just restyled to the new theme — unless the user explicitly asks for a different structure. Never condense several nodes into one big node, never re-layout the flow arbitrarily, and never flatten the diagram into a list or into `.pmap` ruled rows (those are for arguments, inventories, and reference detail — not a substitute for a drawing). Draw each node that the original drew.
- Mermaid is reserved for where visual-explainer's rendering table calls for it (sequence, ER, state-machine). Keep it out of process/architecture maps.
- Structured data (issue lists, risk tiers, matrices): real `<table>` inside `.table-wrap` — not CSS-grid pretending.
- Page backlinks were standardized one step back to category pages (commit `e866e16`). When a category is renamed the content pages' backlinks follow.

## Verification checklist

Before committing: confirm the light render (all text readable, SVG nodes colored via the palette vars), follow the crumb (right parent), resize to 375px (no overflow, grids stack), confirm the diagram rendered (not blank; custom-SVG diagrams must pass `check.mjs`/`verify.mjs`), no broken links, title matches h1, meta present, no emoji, `html.light` not `@media`, no `themeToggle`, reduced-motion present.

**Diagram-fidelity check:** if the page being restyled originally contained a rendered flow/process diagram (Mermaid, SVG, or CSS box pipeline), the new page must still *draw* one — it needs an `<svg>` process map with 2+ arrow connectors, not just text rows restating the flow. Grep for `mermaid`/`<script>` catching nothing does not clear this; the drawing itself has to be there.

Brand voice: this is AESOP / legal / portfolio work — write like a human, call out the bullshit, short sentences, "you" not "organizations." The full voice spec lives in the `diagrams` skill and Charlie's brand-voice memory.

Backend / source repos referenced by these pages live under `~/Documents/Vault/GitHub/` (e.g. `aesop/`, `legal-os/`). Verify page claims against them before writing.
