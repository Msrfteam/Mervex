# Models

Every model id looks like `Msrfteam/<name>`. The live catalog (with per-model success rate, latency, context and 14-day history) is public:

```
GET https://api.mervex.cc.cd/v1/models        # OpenAI format
GET https://mervex.cc.cd/models               # human UI with live monitoring
```

## Highlights

| Model | Context | Best for | Credits |
|---|---|---|---|
| `Msrfteam/Mervex-ai-v0.1-lite` | 100K | fast daily chat | x1 |
| `Msrfteam/Mervex-ai-v0.1` | 256K | creative / complex | x1 |
| `Msrfteam/Mervex-ai-v0.2` | 500K | power tasks + vision | x4 |
| `Msrfteam/Mervex-ai-v0.2-pro` | 1M | deep reasoning (VIP) | x8 |
| `Msrfteam/kimi-k3` | 1M | strong reasoning | x8 |
| `Msrfteam/glm-5.3` / `glm-5.3-flash` | 1M | flagship / fast flagship | x8 |
| `Msrfteam/deepseek-v4.1-flash` | 1M | long-context, vision | x8 |
| `Msrfteam/qwen3.5-397b-a17b` | 262K | heavy analysis | x8 |
| `Msrfteam/claude-sonnet-5`, `claude-opus-4-7` | 200K | VIP flagships | x8 |

Plus ~100 community models (Gemma, Llama, Qwen, Mistral, MiniMax, gpt-oss, Nemotron and more).

## Reliability

Models are served through multi-source aggregation with automatic failover and 24/7 health monitoring.
If one source fails, requests route to another automatically — red/green per-model status is public at /models.
