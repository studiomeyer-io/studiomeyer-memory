# Changelog

## 1.2.0 — August 2026

Server-side release wave on the hosted service (memory.studiomeyer.io). No breaking changes — all 56 tools keep their shapes; six read tools gain an optional `trackUsage` parameter.

- **Knowledge-graph communities that mean something** — community detection moved from connected components to Louvain modularity clustering. On a dense graph, one bridge edge no longer merges unrelated neighbourhoods: the live graph went from one cluster holding 84% of entities to 21 topically coherent communities. The old reachability semantics remain available as `algorithm: "components"`.
- **Honest tool annotations** — read-path tools that reinforce retrieved memories by default (the memory's testing effect) now say so: annotations reflect actual behaviour, the side effect is documented in each description, and `trackUsage: false` gives a genuinely side-effect-free read for evals and audits.
- **Rerank cost contract** — the neural cross-encoder runs automatically when available (fast, feeds honest abstention); the LLM rerank fallback now requires an explicit `rerank: true`. No search pays a silent LLM call anymore, and results report which engine ran and how long it took.
- **Multi-topic questions** — "what did we learn about deployment and server security" now splits into per-topic search rounds with a question-stem transfer, and a coverage-aware selection guarantees each topic slots in the result instead of letting the hotter topic crowd out the other.
- **Measured, honestly** — a benchmark-mapper bug had under-reported recall since the dataset existed; the corrected truth on the unchanged stack is R@5 0.92 / R@10 0.97. Per-tenant memory-quality metrics (uptake, staleness, zombie contradictions, correction latency, verified fraction) are exposed via `nex_health`, with degraded-marker honesty when a sub-metric falls back.
- **Episodic memory is never superseded** — auto-resolution no longer treats textual similarity between two distinct EVENTS (two runs, two games, two deploys) as evidence one replaced the other; both destructive paths are guarded and resolution is an atomic compare-and-swap.

## 1.1.0 — June 2026

Server-side release wave on the hosted service (memory.studiomeyer.io). No breaking changes — all 56 tools keep their shapes; `nex_consolidate` gains a `dream` action and a `maxClusters` budget parameter.

- **Dream Cycle** — offline consolidation with a global view: recurring episodic memories are distilled into lasting semantic facts (LLM-distilled with conservative confidence; source episodes are preserved and linked, never replaced), contradictions are flagged for review, confidence decay and lifecycle tiers are rebalanced, and a searchable dream report is written. Runs automatically (daily, gated) or on demand with a dry-run preview.
- **Retrieval reinforcement** — accessing a memory strengthens it: frequently used facts stay present, and archived facts that prove relevant again are reactivated. Spacing damping prevents feedback loops.
- **Timeless facts** — semantic facts now age damped, so a lasting truth is no longer buried by recency while fresh memories stay unaffected.
- **Honest abstention v2** — two independent evidence signals (semantic similarity plus a cross-encoder) decide when the server answers versus honestly reporting "no confident information" — measured at zero false abstains on the internal retrieval harness.

## 1.0.0

Initial public release.
