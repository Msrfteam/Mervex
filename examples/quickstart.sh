#!/usr/bin/env bash
# Mervex quickstart — get a free key at https://mervex.cc.cd/auth

API_KEY="Mervex-ai-YOUR_KEY"
BASE="https://api.mervex.cc.cd"

# List all models (public)
curl "$BASE/v1/models"

# Chat completion (OpenAI-compatible)
curl -X POST "$BASE/v1/chat/completions" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Msrfteam/Mervex-ai-v0.1-lite",
    "messages": [{"role": "user", "content": "Hello! Who are you?"}]
  }'
