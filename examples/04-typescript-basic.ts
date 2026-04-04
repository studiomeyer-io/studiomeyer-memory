/**
 * StudioMeyer Memory \u2014 TypeScript Example
 * Docs: https://memory.studiomeyer.io
 */

const API_URL = process.env.NEX_API_URL ?? "https://memory.studiomeyer.io";
const API_KEY = process.env.NEX_API_KEY ?? "nex_your_key_here";
const headers = { Authorization: `Bearer ${API_KEY}`, "Content-Type": "application/json" };

async function learn(category: string, content: string, tags?: string[]) {
  return (await fetch(`${API_URL}/api/learn`, { method: "POST", headers, body: JSON.stringify({ category, content, tags }) })).json();
}

async function search(query: string, options?: Record<string, unknown>) {
  return (await fetch(`${API_URL}/api/search`, { method: "POST", headers, body: JSON.stringify({ query, ...options }) })).json();
}

async function createEntity(name: string, entityType: string, observations: string[]) {
  return (await fetch(`${API_URL}/api/entity`, { method: "POST", headers, body: JSON.stringify({ name, entityType, observations }) })).json();
}

async function main() {
  await learn("architecture", "API gateway uses token bucket at 5000 req/min", ["api"]);
  await createEntity("Redis", "tool", ["In-memory store", "Used for caching"]);
  const results = await search("rate limiting", { limit: 5 });
  for (const r of results.results || []) console.log(`  [${r.type}] ${(r.content || "").slice(0, 80)}`);
}

main().catch(console.error);
