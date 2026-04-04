"""
StudioMeyer Memory \u2014 Import ChatGPT History

Step 1: Export from ChatGPT (Settings \u2192 Data Controls \u2192 Export)
Step 2: python import-chatgpt.py conversations.json --import

Docs: https://memory.studiomeyer.io
"""

import json, os, sys, requests

API_URL = os.getenv("NEX_API_URL", "https://memory.studiomeyer.io")
API_KEY = os.getenv("NEX_API_KEY", "nex_your_key_here")
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def import_chatgpt(file_path: str, dry_run: bool = True):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()

    print("Analyzing...")
    analysis = requests.post(f"{API_URL}/api/import", headers=headers, json={"data": data, "action": "analyze", "platform": "chatgpt"}).json()
    stats = analysis.get("stats", {})
    print(f"  {stats.get('conversations', 0)} conversations, {stats.get('learnings', 0)} learnings, {stats.get('entities', 0)} entities")

    if dry_run:
        print("[DRY RUN] Run with --import to import.")
        return

    result = requests.post(f"{API_URL}/api/import", headers=headers, json={"data": data, "action": "import", "platform": "chatgpt"}).json()
    print(f"  Success: {result.get('success')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import-chatgpt.py conversations.json [--import]")
        sys.exit(1)
    import_chatgpt(sys.argv[1], dry_run="--import" not in sys.argv)
