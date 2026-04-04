"""
StudioMeyer Memory \u2014 Official SDK Example

Install: pip install nex-memory
Docs: https://memory.studiomeyer.io
"""

import os
from nex_memory import NexMemoryClient

memory = NexMemoryClient(api_key=os.getenv("NEX_API_KEY", "nex_your_key_here"))

with memory:
    memory.learn(category="architecture", content="API uses token bucket at 5000 req/min", tags=["api"], confidence=0.9)
    memory.entity(name="Redis", entity_type="tool", observations=["In-memory store", "Used for caching"])
    memory.decide(title="Redis for rate limiting", decision="Redis token bucket", reasoning="Sub-ms latency required")

    results = memory.search(query="rate limiting", limit=5)
    for r in results.results:
        print(f"  [{r.type}] {r.content[:80]}")

print("Done!")
