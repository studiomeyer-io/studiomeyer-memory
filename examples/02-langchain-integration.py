"""
StudioMeyer Memory + LangChain Integration Example

Requirements: pip install langchain langchain-anthropic requests
Docs: https://memory.studiomeyer.io
"""

import os
import requests
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic

API_URL = os.getenv("NEX_API_URL", "https://memory.studiomeyer.io")
API_KEY = os.getenv("NEX_API_KEY", "nex_your_key_here")
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

@tool
def remember(content: str, category: str = "insight") -> str:
    """Store a learning in persistent memory."""
    resp = requests.post(f"{API_URL}/api/learn", headers=headers, json={"category": category, "content": content, "source": "automated"})
    data = resp.json()
    return f"Stored: {data.get('action', 'unknown')} \u2014 {data.get('message', '')}"

@tool
def recall(query: str) -> str:
    """Search persistent memory for relevant information."""
    resp = requests.post(f"{API_URL}/api/search", headers=headers, json={"query": query, "limit": 5})
    results = resp.json().get("results", [])
    if not results:
        return "No relevant memories found."
    return "\n".join(f"[{r.get('type')}] {r.get('content', '')[:200]}" for r in results)

@tool
def track_entity(name: str, entity_type: str, facts: list[str]) -> str:
    """Track a person, tool, or concept in the Knowledge Graph."""
    resp = requests.post(f"{API_URL}/api/entity", headers=headers, json={"name": name, "entityType": entity_type, "observations": facts})
    return f"Entity '{name}' updated with {resp.json().get('observationsAdded', 0)} observations"

if __name__ == "__main__":
    llm = ChatAnthropic(model="claude-sonnet-4-5-20241022")
    tools = [remember, recall, track_entity]
    print("LangChain agent with StudioMeyer Memory is ready!")
    print("Tools:", [t.name for t in tools])
