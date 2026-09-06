# Breadcrumb Nav Rollout — Reusable Prompt

Paste this into a fresh Claude Code session (or hand it to an agent) to roll the
`Index / Category / Page` breadcrumb nav out across the whole diagrams repo.

Reference implementation: `legal/legal-os-fault-line-radar.html` — copy its
`.crumbs` markup and CSS exactly.

---

```
Roll out a breadcrumb nav across the entire diagrams repo
(/Users/motorthings/Documents/Vault/GitHub/diagrams), replacing the current
double-backlink pattern. Use legal/legal-os-fault-line-radar.html as the
reference implementation — copy its .crumbs markup and CSS exactly.

THE CONVENTION
Every content page gets ONE breadcrumb in the sticky nav bar, left side,
theme-toggle stays on the right. Format:

    Index / <Category> / <Page>

- "Index" links to the ROOT index.html (the master collection).
- "<Category>" links to that page's category page (see mapping below).
- "<Page>" is the current page: plain text, not a link, aria-current="page".

Remove BOTH of the old elements on each page:
1. the fixed top-left <a class="backlink">…</a> element, and
2. the <a class="nav-brand">…</a> link inside .nav-inner.
Replace the nav-brand with the <nav class="crumbs"> block. Leave the
.backlink CSS rule in place if harmless, or delete it — your call, but the
ELEMENT must go.

CATEGORY-TARGET MAPPING (the repo has two patterns — detect per folder)
- Folders WITH their own index.html (e.g. legal/, csm/, portfolio/):
  the category link is index.html (same folder). Root Index is ../index.html.
- Folders WITHOUT an index.html: their pages are listed on a root-level
  category file named <folder>.html (e.g. aesop/*.html -> ../aesop.html,
  enablement/ -> ../enablement.html, monday/ -> ../monday.html). Category
  link is ../<folder>.html. Root Index is ../index.html.
- If a subfolder has neither its own index NOR a matching root-level
  <folder>.html, fall back to just: Index / <Page> (no category crumb).
- Root-level content pages (html files directly in the repo root, e.g.
  overview.html, the-harness.html, ip-portfolio.html): breadcrumb is
  Index / <Page>, where Index -> index.html (same dir). Do NOT convert
  index.html itself, and do NOT convert the root-level category pages'
  breadcrumb to point at themselves — a category page like aesop.html gets
  Index / <Category(current, plain)>.
- Category index pages (legal/index.html etc.): Index / <Category(current,
  plain)>, Index -> ../index.html.

CATEGORY LABELS
Humanize the folder name (aesop -> AESOP, ai-platform -> AI Platform,
legal -> Legal, csm -> CSM, tbg -> TBG). If the category page has a clear
<h1> or <title>, prefer a short version of that. Build the full
folder -> {category_href, label} map FIRST, print it, and sanity-check it
before editing anything.

THEME SAFETY (critical)
Do not touch any page's color variables, fonts, or layout. The crumb link
color must match whatever accent that page already used for its nav-brand
(varies by page: --primary, --accent, --indigo, etc.). Reuse the existing
var. .crumbs .sep uses --text-faint, .crumbs .current uses --text-dim.
Relative path depth must be correct per page location (subfolder pages use
../index.html for root; root pages use index.html).

EXECUTION
~200 files — write a script (Python) to do the transform, but:
- Make it idempotent: skip pages that already have <nav class="crumbs">.
- Handle pages that lack a .backlink or .nav-brand gracefully (some may
  differ) — log any page the script can't confidently transform and leave
  it untouched for manual review rather than corrupting it.
- Print a summary: converted / skipped / needs-manual, with counts.

VERIFY before committing
- Spot-check 5 pages across different folders (a legal/ page, an aesop/
  page, a root-level page, a category index, a portfolio/ page): open each,
  confirm the breadcrumb renders, every ancestor link resolves to a real
  file, the current page is plain text, and toggling dark/light keeps the
  crumbs readable.
- grep the repo: zero remaining class="backlink" ELEMENTS, zero
  class="nav-brand" links, breadcrumb count ≈ page count minus root index.
- Confirm no color/font vars were changed (git diff should only touch the
  nav region + one CSS block per file).

Then commit with a clear message and push. Report the converted/skipped/
needs-manual list so I can eyeball the exceptions.
```

---

## Notes before running

- **Theme-safety is the highest-risk clause.** Pages use different accent
  variable names, so a blind `var(--primary)` would break pages that call it
  `--accent` or `--indigo`. The prompt tells the agent to reuse each page's
  existing nav-brand color.
- **Run it on a branch**, or at least eyeball the `needs-manual` list before
  pushing. Across ~200 hand-built files there will be a few oddballs that don't
  match the standard nav structure.

## Reference: the `.crumbs` block

Markup (inside `.nav-inner`, replacing the nav-brand link):

```html
<nav class="crumbs" aria-label="Breadcrumb">
  <a href="../index.html">Index</a>
  <span class="sep">/</span>
  <a href="index.html">Legal</a>
  <span class="sep">/</span>
  <span class="current" aria-current="page">Fault-Line Radar</span>
</nav>
```

CSS:

```css
.crumbs { font-family: var(--font-mono); font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; min-width: 0; }
.crumbs a { color: var(--primary); text-decoration: none; }
.crumbs a:hover, .crumbs a:focus-visible { text-decoration: underline; outline: none; }
.crumbs .sep { color: var(--text-faint); }
.crumbs .current { color: var(--text-dim); font-weight: 400; }
```
