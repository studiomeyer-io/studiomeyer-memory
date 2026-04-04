"""
StudioMeyer Memory — Basic Usage Example (Python)

Docs: https://memory.studiomeyer.io
"""

import os
import requests

API_URL = os.getenv("NEX_API_URL", "https://memory.studiomeyer.io")
API_KEY = os.getenv("NEX_API_KEY", "nex_your_key_here")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def store_learning(category: str, content: str, **kwargs) -> dict:
    data = {"category": category, "content": content, **kwargs}
    return requests.post(f"{API_URL}/api/learn", headers=headers, json=data).json()

def search(query: str, **kwargs) -> dict:
    data = {"query": query, **kwargs}
    return requests.post(f"{API_URL}/api/search", headers=headers, json=data).json()

def create_entity(name: str, entity_type: str, observations: list[str]) -> dict:
    data = {"name": name, "entityType": entity_type, "observations": observations}
    return requests.post(f"{API_URL}/api/entity", headers=headers, json=data).json()

def log_decision(title: str, decision: str, reasoning: str) -> dict:
    data = {"title": title, "decision": decision, "reasoning": reasoning}
    return requests.post(f"{API_URL}/api/decide", headers=headers, json=data).json()

if __name__ == "__main__":
    print("Storing memories...")
    store_learning("architecture", "API uses token bucket rate limiting, 5000 req/min", tags=["api"])
    store_learning("mistake", "Never deploy on Friday without a rollback plan")

    print("Creating entity...")
    create_entity("Redis", "tool", ["In-memory key-value store", "Used for caching"])

    print("Logging decision...")
    log_decision("Redis for rate limiting", "Redis token bucket", "Sub-ms latency required")

    print("\nSearching...")
    results = search("rate limiting", limit=5)
    for r in results.get("results", []):
        print(f"  [{r.get('type')}] {r.get('content', '')[:80]}...")
