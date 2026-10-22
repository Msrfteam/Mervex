# Use Mervex in Cursor

Cursor supports custom OpenAI-compatible endpoints.

1. Open **Cursor → Settings → Models**
2. Under **OpenAI API Key** enable and set:
   - **Key:** your Mervex key (`Mervex-ai-...`) — free at https://mervex.cc.cd/auth
   - **Base URL:** `https://api.mervex.cc.cd/v1` (enable "Override Base URL")
3. Add model ids you want, e.g. `Msrfteam/Mervex-ai-v0.1`, `Msrfteam/kimi-k3`.

Model list: `GET https://api.mervex.cc.cd/v1/models` (public).
