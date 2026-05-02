<!-- studiomeyer-mcp-stack-banner:start -->
> **Part of the [StudioMeyer MCP Stack](https://studiomeyer.io)** — Built in Mallorca 🌴 · ⭐ if you use it
<!-- studiomeyer-mcp-stack-banner:end -->

# StudioMeyer Memory

[![smithery badge](https://smithery.ai/badge/cod-gb2l/StudioMeyer-Memory)](https://smithery.ai/servers/cod-gb2l/StudioMeyer-Memory)

> Persistent, intelligent memory for AI agents. 56 MCP tools (incl. interactive 3D knowledge graph visualization). Knowledge Graph included in every plan.

[![MCP Registry](https://img.shields.io/badge/MCP-Registry-blue)](https://registry.modelcontextprotocol.io/servers/io.studiomeyer/memory)
[![MCPize](https://img.shields.io/badge/MCPize-Marketplace-purple)](https://mcpize.com/mcp/studiomeyer-memory)
[![Glama](https://glama.ai/mcp/servers/studiomeyer-io/studiomeyer-memory/badges/score.svg)](https://glama.ai/mcp/servers/studiomeyer-io/studiomeyer-memory)

## What is this?

StudioMeyer Memory gives AI agents persistent memory across sessions. Instead of starting fresh every conversation, your agents learn, remember, and improve over time.

**56 MCP tools** for learning, search, knowledge graph, session tracking, multi-agent support, contradiction detection, self-improvement — plus interactive 3D visualization (`nex_graph_view`, `nex_recall_timeline`, `nex_session_replay`) via MCP Apps.

## Connect in 10 Seconds

### Claude Desktop / Cowork
Settings → Connectors → Add URL:
```
https://memory.studiomeyer.io/mcp
```

### Claude Code
```bash
claude mcp add --transport http memory https://memory.studiomeyer.io/mcp
```

### Cursor / VS Code / Windsurf / Zed
```bash
npx mcp-remote https://memory.studiomeyer.io/mcp
```

### MCPize
```bash
npx mcp-remote https://studiomeyer-memory.mcpize.run
```

## REST API

For custom agents, scripts, and integrations:

```bash
# 1. Sign up
curl -X POST https://memory.studiomeyer.io/api/signup \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com"}'

# 2. Store a memory
curl -X POST https://memory.studiomeyer.io/api/learn \
  -H "Authorization: Bearer nex_your_key" \
  -H "Content-Type: application/json" \
  -d '{"category": "insight", "content": "Users prefer dark mode"}'

# 3. Search
curl -X POST https://memory.studiomeyer.io/api/search \
  -H "Authorization: Bearer nex_your_key" \
  -H "Content-Type: application/json" \
  -d '{"query": "user preferences"}'
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/signup` | Create account, get API key |
| `GET` | `/api/account` | Account info, plan, limits |
| `POST` | `/api/learn` | Store a learning |
| `POST` | `/api/search` | Search all knowledge |
| `POST` | `/api/decide` | Log a decision |
| `POST` | `/api/entity` | Create/update entity |
| `POST` | `/api/import` | Import from ChatGPT/Claude/Gemini/Copilot/Perplexity |
| `POST` | `/api/backfill` | Generate embeddings |
| `GET` | `/api/export` | Export all data (Markdown) |
| `POST` | `/api/checkout` | Upgrade plan (Stripe) |

Full API documentation: [openapi.yaml](openapi.yaml)

## SDKs

- **TypeScript:** `npm install @studiomeyer/memory-sdk` ([GitHub](https://github.com/studiomeyer-io/nex-sdk-typescript))
- **Python:** `pip install nex-memory` ([GitHub](https://github.com/studiomeyer-io/nex-sdk-python))
- **OpenAPI Spec:** [openapi.yaml](openapi.yaml) — generate clients for any language

## Features

### Core Memory
- **5-phase parallel search** — semantic vectors, trigram matching, full-text, graph traversal, pattern matching
- **Duplicate detection** — 5-factor admission control prevents noise
- **10 learning categories** — pattern, mistake, insight, research, architecture, and more
- **Decision logging** — track choices with reasoning for traceability

### Knowledge Graph (All Plans)
- **Entities** — people, tools, projects, concepts
- **Observations** — facts attached to entities with temporal validity
- **Relations** — typed, directional connections between entities
- **Graph traversal** — 2-hop BFS search through connections
- **Temporal queries** — "What was true on March 15th?"

### Intelligence
- **Contradiction Detection** — automatically flags conflicting facts
- **FadeMem Adaptive Decay** — important memories fade 6x slower
- **Confidence Scoring** — 0-1 scores with temporal decay
- **Bi-temporal Model** — event time + ingestion time
- **Auto-Consolidation** — merges duplicates, backfills embeddings

### Multi-Agent
- **Agent namespaces** — scope memories to specific agents
- **Cross-agent search** — search across all agents by default
- **Shared Knowledge Graph** — one graph, multiple agents

### Import
- **5 platforms** — ChatGPT, Claude, Gemini, GitHub Copilot, Perplexity
- **LLM extraction** — entities, learnings, decisions, relations
- **Preview mode** — analyze before importing

## Benchmark — LongMemEval

**86% on LongMemEval 50q stratified, GPT-4o judged** (Run S957b, 1 May 2026, Anthropic Sonnet 4.6 as answer generator).

Per-category breakdown:

| Category | Score |
|----------|-------|
| temporal-reasoning | 92% |
| multi-session | 92% |
| single-session-user | 100% |

**Caveat for honesty:** S957b ran against memory-server v3.16.10, before the v3.16.11 cross-project search-leak fix landed (LIVE on production since 2 May 2026). The 86% may be 1-3 percentage points inflated by cross-question help. A clean 50q re-run with the fix in place is the next planned wave once cost-control safeguards in the bench script are wired up. Realistic range after the re-run: **78-86%**.

The full whitepaper with methodology, run history and per-question results lives at [studiomeyer.io/services/memory](https://studiomeyer.io/services/memory) and is updated as new validated runs land.

**Reference scores from other vendors (publicly published):**

| System | Aggregate | Temporal | Source |
|--------|-----------|----------|--------|
| StudioMeyer Memory | 86% | 92% | this README |
| Mem0 (Managed Platform) | 93.4% | 93.2% | mem0.ai/blog April 2026 — Token-Efficient Memory Algorithm |
| Mem0 BEAM 10M tokens | 48.6% | 16.3% | mem0.ai/research — production-scale collapse |
| Mastra Observational Memory | 94.87% (gpt-5-mini) | — | mastra.ai/blog/observational-memory |
| Hindsight | 91.4% | 79.7% | published |
| Zep | 63.8% | — | arXiv 2501.13956 |

**What we are honest about:** in aggregate we sit below Mem0 Managed (93.4%) and Mastra OM with gpt-5-mini (94.87%). Our differentiators are architecture and production behavior — bi-temporal knowledge graph included from the Free tier (Mem0 charges $249/mo for graph features), production-scale stability (Mem0 itself reports 48.6% aggregate / 16.3% temporal at 10M tokens), EU Frankfurt hosting + GDPR, and the live interactive 3D knowledge graph as part of the standard tool surface — verified unique among AI memory SaaS as of April 2026.

## Pricing

| Plan | Price | Calls/Day | Learnings | Entities | Knowledge Graph | Agentic Search + AI Reranker |
|------|-------|-----------|-----------|----------|------------------|------------------------------|
| **Free** | $0 forever | 200 | 1,000 | 100 | ✅ | — (simple hybrid search) |
| **Pro** | $29/mo | 5,000 | 25,000 | 1,000 | ✅ | ✅ |
| **Team** | $49/mo | Unlimited | Unlimited | Unlimited | ✅ | ✅ |
| **Scale** | $99/mo | Unlimited | Unlimited | Unlimited | ✅ | ✅ |

All 56 tools available in every plan — including interactive 3D knowledge graph visualization. Knowledge Graph included from Free.

**What's the difference?** Free uses our hybrid search stack (Trigram + FTS + pgvector + Knowledge-Graph traversal + RRF fusion + temporal decay + per-tenant isolation) — fast, deterministic, no LLM cost. Pro+ adds **agentic retrieval**: an iterative completeness check (Haiku LLM) that detects when a complex query (multi-hop, temporal computation, aggregation, list ordering) needs a refined re-query. On LongMemEval-class benchmarks this lifts recall by 5-10pp on the hardest categories.

**Compare:** Mem0 charges $249/mo for Graph Memory. We include it from Free.

## Security

- **Magic Link Authentication** — email verification on every sign-in. No passwords stored. You receive a single-use link that expires in 10 minutes. Nobody can access your data without proving email ownership.
- **OAuth 2.1** with PKCE S256 — latest authentication standard
- **Supabase Pro** (EU Frankfurt, Germany) — SOC 2 Type II, GDPR-ready
- **Row Level Security** — tenant isolation at database level
- **Secret Scanner** — prevents accidental storage of API keys/passwords
- **Data Export** — `GET /api/export` anytime
- **Encryption** — at rest (AES-256) and in transit (TLS 1.3)

## Examples

See the [examples/](examples/) folder:
- Python basic usage
- LangChain integration
- CrewAI multi-agent
- TypeScript basic
- ChatGPT import
- Official SDK usage

## Resources

- **Documentation:** Built-in — call `nex_guide("quickstart")` via MCP
- **Postman Collection:** [Download](postman/StudioMeyer-Memory-API.postman_collection.json)
- **OpenAPI Spec:** [openapi.yaml](openapi.yaml)
- **MCP Registry:** [io.studiomeyer/memory](https://registry.modelcontextprotocol.io/servers/io.studiomeyer/memory)

## About StudioMeyer

[StudioMeyer](https://studiomeyer.io) is an AI and design studio based in Palma de Mallorca, working with clients worldwide. We build custom websites and AI infrastructure for small and medium businesses. Production stack on Claude Agent SDK, MCP and n8n, with Sentry, Langfuse and LangGraph for observability and an in-house guard layer.

## License

MIT — see [LICENSE](LICENSE). The memory server is a hosted service — this repository contains documentation and examples.

## Links

- 🌐 [memory.studiomeyer.io](https://memory.studiomeyer.io)
- 🏪 [MCPize Marketplace](https://mcpize.com/mcp/studiomeyer-memory)
- 🏢 [studiomeyer.io](https://studiomeyer.io)