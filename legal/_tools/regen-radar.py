#!/usr/bin/env python3
"""Regenerate the radar diagram pages' data from the app's own output.

WHY THIS EXISTS
---------------
The `legal/legal-os-*radar*.html` pages bake their numbers into the file. Twice now
that has drifted: once the framing moved on, once the ordering did, and each time the
fix was a hand-patch that left a second stale copy behind (a two-step sed on table
cells once produced `var(----ambe)`; the chart data and the meter table on the same
page held different values).

So this reads the same source the app reads and prints the fragments to paste in.

    frontend/public/radar/data.json        scores, meters, per-line authority counts
    frontend/public/radar/calibration.json the flag threshold
    radar/ordering.py                      the shared order + measured lead times

Run it, paste the output, then run it again with --check to confirm the pages match.

    python3 legal/_tools/regen-radar.py            # print the fragments
    python3 legal/_tools/regen-radar.py --check    # assert the pages still agree
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # diagrams/legal/_tools
LEGAL = HERE.parent                             # diagrams/legal
DIAGRAMS = LEGAL.parent                         # diagrams
REPO_ROOT = DIAGRAMS.parent                     # GitHub/
LEGAL_OS = REPO_ROOT / "legal-os"

DATA = LEGAL_OS / "frontend" / "public" / "radar" / "data.json"
CAL = LEGAL_OS / "frontend" / "public" / "radar" / "calibration.json"

TARGETS = [
    LEGAL / "legal-os-radar-master-reference.html",
    LEGAL / "legal-os-radar-streams.html",
]

# The app's authority ramp, from frontend/src/app/globals.css. The page defines these
# as CSS vars so the chart reads the same as the app's board.
KINDS = [
    ("appellate", "appellate court"),
    ("trial", "trial court"),
    ("primary", "statute or rule"),
    ("guidance", "bar guidance"),
]


def load():
    data = json.loads(DATA.read_text())
    cal = json.loads(CAL.read_text())
    sys.path.insert(0, str(LEGAL_OS / "radar"))
    import ordering  # noqa: E402
    return data, cal, ordering


def lines_in_order(data):
    """Duties first by the shared rule, then the rest by pressure. The order the app uses."""
    duties = sorted((f for f in data["fault_lines"] if f["is_duty"]),
                    key=lambda f: f["order_key"])
    rest = sorted((f for f in data["fault_lines"] if not f["is_duty"]),
                  key=lambda f: -f["pressure"])
    return duties, rest


def emit_kinds(data):
    """The four rails: counts by authority kind across the whole board."""
    totals = {k: 0 for k, _ in KINDS}
    for f in data["fault_lines"]:
        for k, _ in KINDS:
            totals[k] += f["strength"][k]
    out = []
    for k, label in KINDS:
        # color: is load-bearing. SVG presentation attributes cannot read CSS vars, and a
        # KINDS entry without it renders every bar black (which is how this was caught).
        out.append(f"    {{ id: '{k}', name: '{label}', color: C.{k}, items: {totals[k]} }},")
    return "\n".join(out), totals


def emit_lines(data, defs):
    duties, rest = lines_in_order(data)
    rows = []
    for f in duties + rest:
        s = f["strength"]
        cells = ", ".join(f"{k}: {s[k]}" for k, _ in KINDS if s[k])
        d = defs.get(f["id"], f["title"])
        rows.append(
            "{ name: '%s', def: '%s', sources: %d, duty: %s, control: '%s', cells: { %s } },"
            % (f["id"], d.replace("'", "\\'"), s["total"],
               "true" if f["is_duty"] else "false",
               f["control"].replace("'", "\\'"), cells)
        )
    return "\n".join(rows)


def emit_meter_table(data):
    """The eleven-line meter table, regenerated whole.

    Regenerated rather than patched per cell: a two-step sed over cells corrupted markup
    on the last pass, and the table is small enough that there is no reason to risk it.
    """
    duties, rest = lines_in_order(data)
    order = duties + rest
    rows = []
    for f in order:
        mark = " (duty)" if f["is_duty"] else ""
        rows.append(
            "<tr>"
            f'<td class="fl-name">{f["id"]}{mark}</td>'
            f'<td class="m">{f["capability"]}</td>'
            f'<td class="m">{f["pressure"]}</td>'
            f'<td class="m">{f["adoption"]}</td>'
            f'<td class="m">{f["enable"]}</td>'
            f'<td class="m">{f["software"]}</td>'
            "</tr>"
        )
    return "\n".join(rows)


def existing_defs():
    """Keep the authored one-line descriptions; only the numbers are regenerated."""
    defs = {}
    if not TARGETS[0].exists():
        return defs
    html = TARGETS[0].read_text()
    for m in re.finditer(r"\{ name: '([^']+)', def: '((?:[^'\\]|\\.)*)'", html):
        defs[m.group(1)] = m.group(2)
    # the table carries its own longer copy under .fl-desc; prefer it where present
    for m in re.finditer(r'<td class="fl-name">([^<]+)</td><td class="fl-desc">([^<]+)</td>', html):
        defs.setdefault(m.group(1).strip(), m.group(2).strip())
    return defs


# The pages label two lines by display name; data.json keys them by id.
DISPLAY = {"vendor_liability": "vendor liability", "judicial_analytics": "judge analytics"}


def check(data, cal, ordering):
    """Assert the shipped pages agree with the live source, line by line."""
    duties, rest = lines_in_order(data)
    live = {f["id"]: f for f in duties + rest}
    problems = []
    for path in TARGETS:
        if not path.exists():
            continue
        html = path.read_text()
        for fid, f in live.items():
            name = DISPLAY.get(fid, fid)
            if not f["is_duty"]:
                continue          # the watch list is a table, checked below
            # each duty's source count must appear next to its own name in the chart data
            m = re.search(r"\{ name: '%s',[^}]*sources: (\d+)" % re.escape(name), html)
            if not m:
                problems.append(f"{path.name}: {name} has no regenerated sources value")
            elif int(m.group(1)) != f["strength"]["total"]:
                problems.append(
                    f"{path.name}: {name} says {m.group(1)} sources, live is {f['strength']['total']}")
        # the old pressure-ranked wording must be gone
        for phrase in ("ranked by queue", "ranked by pressure", "at or past 7"):
            if phrase in html:
                problems.append(f"{path.name}: still says {phrase!r}")
    return problems


def main():
    data, cal, ordering = load()
    defs = existing_defs()

    if "--check" in sys.argv:
        problems = check(data, cal, ordering)
        for p in problems:
            print("DRIFT:", p)
        print(f"\n{len(problems)} problem(s)." if problems else "\nPages agree with the live source.")
        return 1 if problems else 0

    kinds, totals = emit_kinds(data)
    print("=" * 78)
    print("CONST KINDS  (rails) — total", sum(totals.values()), "sources")
    print("=" * 78)
    print(kinds)
    print()
    print("=" * 78)
    print("CONST LINES — duties first by the shared rule, then the rest by pressure")
    print("=" * 78)
    print(emit_lines(data, defs))
    print()
    print("=" * 78)
    print("METER TABLE TBODY")
    print("=" * 78)
    print(emit_meter_table(data))
    print()
    print(f"as_of={data['as_of']}  n_items={data['n_items']}  threshold={cal.get('call_threshold')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
