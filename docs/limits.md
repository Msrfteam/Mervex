# Limits

## Free plan

| | |
|---|---|
| Daily requests | **100** |
| Discord bonus | +50/day (verify via bot in our Discord) |
| Google bonus | +50/day (link on Msr F Team ID) |
| GitHub bonus | +50/day (link on Msr F Team ID) |
| **Max free** | **250 requests/day** |
| Welcome bonus | **+400 requests** — one-time, automatic at sign-up |
| Rate | 5 requests/min |
| Vision | 10 images/month |
| API keys | 2 |

## Credit system

1 credit = 1,000 tokens (input + output). A **group multiplier** applies per model:

- Light models (V0.1 Lite, V0.1, most small community models): **x1** → 100 credits/day ≈ 50–100 messages
- Mid models (V0.2, Gemini Flash, Qwen): **x4**
- Strong models (V0.2 Pro, Kimi K3, GLM 5.3, DeepSeek V4.1, Claude): **x8** → the same daily budget ≈ 6–12 deep replies

## Paid plans

| Plan | Requests/day | Rate | API keys | Vision |
|---|---|---|---|---|
| Plus ($5/mo) | 200 | 10/min | 4 | 20/mo |
| Pro ($15/mo) | 500 | 20/min | 10 | 40/mo |
| Premium ($30/mo) | 1,000 | 40/min | 20 | 60/mo |

All paid plans unlock every model. Upgrade inside the dashboard (wallet, card, crypto).

## Error codes

| HTTP | code | Meaning |
|---|---|---|
| 401 | AUTHENTICATION_REQUIRED | Invalid/missing key |
| 402 | PREMIUM_ACCESS_REQUIRED | VIP model, upgrade needed |
| 403 | KEY_EXPIRED | Key expired |
| 423 | ACCOUNT_LOCKED | Account banned |
| 429 | RATE_LIMIT_EXCEEDED | RPM/RPD exceeded |
| 429 | INSUFFICIENT_QUOTA | Daily credit budget exhausted |
| 429 | DECIDE_EXHAUSTED | Auto-Decision lifetime balance used up |
| 503 | MODEL_DISABLED | Model temporarily disabled |
