# Fault-Line Radar — streams visualization design prompt

This is a prompt to hand to a Claude design session. It describes what the "streams" page must illustrate and the data that drives the visualization, so the session can recommend the best visualization type.

---

## Context — what we're visualizing

This is the "streams" page for a legal-AI prediction engine called Fault-Line Radar. The engine watches the legal-AI landscape and predicts which legal "duty" a law firm will be pressured to fix next (verification, disclosure, confidentiality, and eight others).

The one thing this page must convey: **four independent streams of information converge into a ranked list of predictions, and the more streams that point at the same prediction, the more confident the engine is in it.** Corroboration is the whole point — a prediction backed by four streams is a stronger call than one backed by one.

## The data we have

Four source streams, each a count of evidence items:

| stream | color | items |
|---|---|---|
| Rules & rulings | rose | 25 |
| Vendors | green | 24 |
| Capability | blue | 17 |
| Market & insurers | amber | 10 |

(76 items total.)

Eleven fault-line predictions, each carrying two numbers:
- **queue** — prediction strength, 0–10 (this is the rank order).
- **corroboration** — how many of the four streams feed it, 1–4.

| prediction | queue | streams |
|---|---|---|
| verification | 8.6 | 4 |
| competence | 7.9 | 3 |
| disclosure | 7.6 | 2 |
| convergence | 7.5 | 3 |
| insurance | 7.3 | 1 |
| confidentiality | 6.9 | 2 |
| benchmark | 6.9 | 3 |
| agentic | 5.8 | 3 |
| vendor liability | 2.3 | 2 |
| judge analytics | 1.9 | 1 |
| fees | 1.7 | 1 |

Plus the wiring: which source feeds which prediction, and how many items. E.g. verification draws 13 rules items + 3 capability + 4 market + 3 vendor = 4 streams. Benchmark draws 15 vendor + 4 capability + 1 market. Fees draws 1 rules item only. Each prediction is fed by a different, overlapping subset of streams.

## What we've tried and where each fell short

1. **Two-column Sankey** (sources → predictions): 25 bands, and they cross constantly because predictions are multi-source. The crossings *are* the corroboration, but they read as spaghetti.
2. **Funnel** (sources → one "scoring" node → predictions): clean, but collapsing through a single middle node erases which-stream-feeds-which-prediction.
3. **Matrix** (prediction rows × source columns, cell = item count): exact, zero crossings, but it flattens the "streams pour in" motion.

There's also a real unit mismatch to respect: sources are counted in *items*, predictions are scored in a *0–10 queue*. They can't be naively chained in one flow without fudging.

## What I need from you

Recommend the best visualization type for this data, and sketch it. The ideal does all of, in priority order:
1. Shows corroboration as the dominant signal (more streams = visibly stronger call) — this is non-negotiable.
2. Preserves which-stream-feeds-which-prediction, at least on hover or in detail.
3. Keeps the left-to-right "streams in → predictions out" motion if possible.
4. Ranks the predictions so verification (top) is unmistakably the headline.

Don't default to a Sankey. Evaluate alternatives honestly: chord diagram, alluvial, upSet/intersection plot, parallel-coordinates, radial/arc, a ranked bar with stream badges, a small-multiples grid. Tell me which single view is best *and* why the others lose. Then give me a concrete direction I can build in plain HTML/SVG.
