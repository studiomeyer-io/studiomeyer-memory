# StudioMeyer Memory

> Persistent, intelligent memory for AI agents. 53 MCP tools. Knowledge Graph included in every plan.

[![MCP Registry](https://img.shields.io/badge/MCP-Registry-blue)](https://registry.modelcontextprotocol.io/servers/io.studiomeyer/memory)
[![MCPize](https://img.shields.io/badge/MCPize-Marketplace-purple)](https://mcpize.com/mcp/studiomeyer-memory)
[![Glama](https://glama.ai/mcp/servers/studiomeyer-io/studiomeyer-memory/badges/score.svg)](https://glama.ai/mcp/servers/studiomeyer-io/studiomeyer-memory)

## What is this?

StudioMeyer Memory gives AI agents persistent memory across sessions. Instead of starting fresh every conversation, your agents learn, remember, and improve over time.

**53 MCP tools** for learning, search, knowledge graph, session tracking, multi-agent support, contradiction detection, and self-improvement.

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

## Benchmark Results

**LongMemEval v3: 90%** (GPT-4o official scoring)

| System | Score |
|--------|-------|
| Mastra OM | 94.87% |
| Hindsight | 91.4% |
| **StudioMeyer Memory** | **90%** |
| Zep/Graphiti | 71.2% |
| Mem0 | 49% |

## Pricing

| Plan | Price | Calls/Day | Learnings | Knowledge Graph |
|------|-------|-----------|-----------|------------------|
| **Free** | $0 forever | 200 | 1,000 | ✅ |
| **Pro** | $29/mo | 5,000 | 25,000 | ✅ |
| **Team** | $49/mo | Unlimited | Unlimited | ✅ |

All 53 tools available in every plan. Knowledge Graph included from Free.

**Compare:** Mem0 charges $249/mo for Graph Memory. We include it for free.

## Security

- **OAuth 2.1** with PKCE — latest authentication standard
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

## Built By

[StudioMeyer](https://studiomeyer.io) — AI agency based in Spain. Building intelligent systems since 2024.

## License

MIT — see [LICENSE](LICENSE). The memory server is a hosted service — this repository contains documentation and examples.

## Links

- 🌐 [memory.studiomeyer.io](https://memory.studiomeyer.io)
- 🏪 [MCPize Marketplace](https://mcpize.com/mcp/studiomeyer-memory)
- 🏢 [studiomeyer.io](https://studiomeyer.io)
