# Auto-Decision API

Millisecond probabilistic decisions — built for bots, filters, triage pipelines and automation.
Not a chat model: answers come back as **probabilities**, not text. 7–100ms typical latency. Images accepted.

```
POST https://api.mervex.cc.cd/api/ai/decide
```

## Question types

| Type | What it does | Answer |
|---|---|---|
| `noul` | yes/no detection | `{ "noul": 0.965 }` |
| `choice` | pick one option (per-option criteria required) | `{ "choice": "billing", "probabilities": {...}, "confidence": 0.99 }` |
| `score` | rating with a value legend | `{ "score": 0.94, "legend": {...} }` |

## Example

```json
{
  "userId": "usr-...",
  "state": "customer charged twice and demands a refund",
  "questions": {
    "urgent": { "type": "noul" },
    "team": {
      "type": "choice",
      "options": ["outage", "billing", "feature"],
      "criteria": {
        "billing": "payment, charge or refund issue",
        "outage": "service is down or broken",
        "feature": "asking for new functionality"
      }
    }
  }
}
```

Response:

```json
{
  "success": true,
  "answers": {
    "urgent": { "type": "noul", "noul": 0.24 },
    "team": { "type": "choice", "choice": "billing", "probabilities": { "billing": 0.998, "outage": 0.002, "feature": 0.0002 }, "confidence": 0.987 }
  },
  "remaining": 9999
}
```

## Vision

Add `"image": "https://..."` — vision models classify images (receipts, screenshots, objects) with the same noul/choice format.

## Balance

- **10,000 lifetime requests** per user, free
- **+2,500** for linking Google and **+2,500** for GitHub (via Msr F Team ID)
- Rate limit: 20 decisions/minute
- Check balance: `GET /api/ai/decide/balance?userId=...`

## Use cases

- Email/support triage: urgent? → department?
- Spam / fraud / bot-message filtering
- Lead scoring ("will they buy?" → yes 64%)
- Sentiment 1–10 with confidence
- Image checks: "is this a receipt?", "is there a person?"
