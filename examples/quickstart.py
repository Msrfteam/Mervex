import requests

BASE = "https://api.mervex.cc.cd"
API_KEY = "Mervex-ai-YOUR_KEY"  # https://mervex.cc.cd/auth

# List all models (public)
models = requests.get(f"{BASE}/v1/models").json()
print(f"{len(models['data'])} models available")

# Chat completion (OpenAI-compatible)
r = requests.post(
    f"{BASE}/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "Msrfteam/Mervex-ai-v0.1-lite",
        "messages": [{"role": "user", "content": "Hello! Who are you?"}],
    },
)
print(r.json()["choices"][0]["message"]["content"])
