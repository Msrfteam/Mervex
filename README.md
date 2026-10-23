<div align="center">

# 🚀 Mervex AI Platform

**100+ AI models. One OpenAI-compatible key. Free.**

[![Website](https://img.shields.io/badge/Website-mervex.cc.cd-00C9FF?style=for-the-badge&logo=googlechrome&logoColor=white)](https://mervex.cc.cd)
[![API Docs](https://img.shields.io/badge/OpenAPI-openapi.json-6BA539?style=for-the-badge&logo=openapiinitiative&logoColor=white)](./openapi.json)
[![CLI](https://img.shields.io/badge/CLI-npm%20mervexai-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://github.com/Msrfteam/Mervexai)
[![Postman](https://img.shields.io/badge/API_Docs-Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)](https://documenter.getpostman.com/view/59154340/2sBYHUSzJ2)
[![Telegram](https://img.shields.io/badge/Telegram-@Msrfteam-229ED9?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Msrfteam)

**Official Product: [Msr F Team](https://msrfteam.com)**

</div>

---

## What is Mervex?

Mervex gives every registered user a **free API key** with access to **100+ AI models** through a single, fully **OpenAI-compatible endpoint** — plus a millisecond **Auto-Decision API** with probabilistic answers and image classification.

- 🔓 **OpenAI-compatible** — drop-in base URL for Open WebUI, LibreChat, Chatbox, Cursor, LangChain, n8n…
- 🤖 **100+ models** — lightweight fast models to 1M-context flagships
- ⚡ **Auto-Decision API** — yes/no, option picking, scoring with probabilities (7–100ms)
- 📊 **Live monitoring** — success %, latency and 14-day history for every model at [/models](https://mervex.cc.cd/models)
- 🔄 **Automatic failover** — if a source goes down, requests route elsewhere (monitored 24/7)
- 🎁 **+400 bonus requests** — one-time gift for every new member, no conditions

## Quick start

**1.** Get a free key → **https://mervex.cc.cd/auth**

**2.** Send your first request:

```bash
curl https://api.mervex.cc.cd/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Msrfteam/Mervex-ai-v0.1-lite",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

**3.** List every model:

```bash
curl https://api.mervex.cc.cd/v1/models
```

More examples in [`examples/`](./examples) — Python, Node.js, Open WebUI, Chatbox, Cursor.

## Free tier

| | |
|---|---|
| Daily requests | **100** (+ Discord +50, Google +50, GitHub +50 → up to **250/day**) |
| Welcome bonus | **+400 requests** — one-time, automatic, no conditions |
| Rate | 5 requests/min |
| Auto-Decision API | **10,000 lifetime requests** (+2,500 per linked Google/GitHub) |
| Vision | 10 images/month |
| API keys | 2 |

*1 credit = 1,000 tokens. Light models cost ×1, strong models ×8 — so the daily budget equals ~50–100 light messages or ~6–12 flagship-model replies. Paid plans (Plus $5, Pro $15, Premium $30) raise limits — see [docs/limits.md](./docs/limits.md).*

## Repository map

| Path | What's inside |
|---|---|
| [`openapi.json`](./openapi.json) | OpenAPI 3.1 spec — chat, models, decision API |
| [`postman_collection.json`](./postman_collection.json) | Ready-to-import Postman collection |
| [`examples/`](./examples) | curl, Python, Node.js + integration guides (Open WebUI, Chatbox, Cursor) |
| [`docs/`](./docs) | Models overview, Auto-Decision API, limits |

## Ecosystem

- 🌐 **Platform** — [mervex.cc.cd](https://mervex.cc.cd) (playground, dashboard, billing)
- ⌨️ **CLI** — [`npm install -g mervexai`](https://github.com/Msrfteam/Mervexai) (Windows / Linux / macOS)
- 📡 **Status** — live model health at [mervex.cc.cd/models](https://mervex.cc.cd/models)

## Community

[Telegram — @Msrfteam](https://t.me/Msrfteam) · [Discord](https://discord.gg/qrTgA4y36N) · [YouTube — @Msrfteam](https://youtube.com/@Msrfteam)

---

<div align="center">

Built by **[Msr F Team](https://msrfteam.com)** — high-precision websites, mobile apps and AI systems.

</div>
