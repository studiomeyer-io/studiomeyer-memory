# Changelog

## 1.1.0 — June 2026

Server-side release wave on the hosted service (memory.studiomeyer.io). No breaking changes — all 56 tools keep their shapes; `nex_consolidate` gains a `dream` action and a `maxClusters` budget parameter.

- **Dream Cycle** — offline consolidation with a global view: recurring episodic memories are distilled into lasting semantic facts (LLM-distilled with conservative confidence; source episodes are preserved and linked, never replaced), contradictions are flagged for review, confidence decay and lifecycle tiers are rebalanced, and a searchable dream report is written. Runs automatically (daily, gated) or on demand with a dry-run preview.
- **Retrieval reinforcement** — accessing a memory strengthens it: frequently used facts stay present, and archived facts that prove relevant again are reactivated. Spacing damping prevents feedback loops.
- **Timeless facts** — semantic facts now age damped, so a lasting truth is no longer buried by recency while fresh memories stay unaffected.
- **Honest abstention v2** — two independent evidence signals (semantic similarity plus a cross-encoder) decide when the server answers versus honestly reporting "no confident information" — measured at zero false abstains on the internal retrieval harness.

## 1.0.0

Initial public release.
