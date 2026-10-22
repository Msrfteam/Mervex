import requests

# Auto-Decision API — millisecond probabilistic decisions
# 10,000 lifetime requests per user (free)
BASE = "https://api.mervex.cc.cd"
USER_ID = "usr-xxxxxxxxxxxx"  # your Mervex user id

r = requests.post(
    f"{BASE}/api/ai/decide",
    json={
        "userId": USER_ID,
        "state": "customer charged twice and demands a refund",
        "questions": {
            "urgent": {"type": "noul"},
            "team": {
                "type": "choice",
                "options": ["outage", "billing", "feature"],
                "criteria": {
                    "billing": "payment, charge or refund issue",
                    "outage": "service is down or broken",
                    "feature": "asking for new functionality",
                },
            },
            "anger": {"type": "score", "criteria": ["1 = calm", "10 = furious"]},
        },
    },
)
data = r.json()
print(data["answers"]["team"])  # {'choice': 'billing', 'probabilities': {...}, 'confidence': 0.99}
print("remaining:", data["remaining"])
