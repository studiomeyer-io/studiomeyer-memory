"""
StudioMeyer Memory + CrewAI Integration Example

Requirements: pip install crewai requests
Docs: https://memory.studiomeyer.io
"""

import os
import requests

API_URL = os.getenv("NEX_API_URL", "https://memory.studiomeyer.io")
API_KEY = os.getenv("NEX_API_KEY", "nex_your_key_here")
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

class NexMemory:
    """Shared memory backend for CrewAI agents."""
    def __init__(self, agent_id: str = None):
        self.agent_id = agent_id

    def store(self, content: str, category: str = "insight") -> dict:
        data = {"category": category, "content": content, "source": "automated"}
        if self.agent_id:
            data["agentId"] = self.agent_id
        return requests.post(f"{API_URL}/api/learn", headers=headers, json=data).json()

    def search(self, query: str, limit: int = 5, cross_agent: bool = True) -> list:
        data = {"query": query, "limit": limit}
        if not cross_agent and self.agent_id:
            data["agentId"] = self.agent_id
        return requests.post(f"{API_URL}/api/search", headers=headers, json=data).json().get("results", [])

    def decide(self, title: str, decision: str, reasoning: str) -> dict:
        data = {"title": title, "decision": decision, "reasoning": reasoning}
        if self.agent_id:
            data["agentId"] = self.agent_id
        return requests.post(f"{API_URL}/api/decide", headers=headers, json=data).json()

if __name__ == "__main__":
    research = NexMemory(agent_id="research-agent")
    coder = NexMemory(agent_id="code-agent")

    research.store("OpenAI deprecated completions API, migrate by June 2026", "research")
    coder.store("Use retry with exponential backoff for external APIs", "pattern")

    print("Cross-agent search:")
    for r in research.search("API", cross_agent=True):
        print(f"  [{r.get('type')}] {r.get('content', '')[:80]}")
