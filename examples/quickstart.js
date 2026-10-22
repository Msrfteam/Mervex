const BASE = "https://api.mervex.cc.cd";
const API_KEY = "Mervex-ai-YOUR_KEY"; // https://mervex.cc.cd/auth

// List all models (public)
const models = await fetch(BASE + "/v1/models").then((r) => r.json());
console.log(models.data.length + " models available");

// Chat completion (OpenAI-compatible)
const res = await fetch(BASE + "/v1/chat/completions", {
  method: "POST",
  headers: { Authorization: "Bearer " + API_KEY, "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "Msrfteam/Mervex-ai-v0.1-lite",
    messages: [{ role: "user", content: "Hello! Who are you?" }],
  }),
});
const data = await res.json();
console.log(data.choices[0].message.content);
