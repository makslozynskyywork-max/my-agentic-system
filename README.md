# Unified Agent System 🤖

A production-ready, Dockerized environment that unifies three powerful AI frameworks:
* **Paperclip** - Organizational orchestration and multi-agent management.
* **OpenClaw** - Deep execution engine and local-first AI workers.
* **MemPalace** - Global, persistent MCP-based memory palace (Wings/Rooms architecture).

## 🚀 Features

- **Deploy Anywhere:** Fully containerized using `docker-compose`. Works out-of-the-box on any VPS (Hostinger, DigitalOcean) or local machine.
- **Ephemeral Workers:** Dynamically spawns `OpenClaw` docker containers to handle individual tasks from Paperclip. Workers are destroyed after the task is complete, keeping server overhead at absolute zero.
- **Secure by Default:** Services run on an isolated Docker network. Only the main UI is exposed. Postgres and MemPalace are kept safe from external access.
- **VPS Optimized:** Built-in log rotation (preventing SSD bloat) and automatic container restart policies.

## 📦 Installation & Deployment

1. **Clone this repository** (or download it to your VPS).
2. **Rename the `.env.example`** file to `.env`:
   ```bash
   cp .env.example .env
   ```
3. **Add your API Keys** inside the `.env` file (e.g., Anthropic API Key).
4. **Run Docker Compose:**
   ```bash
   docker-compose build
   docker-compose up -d
   ```

## 🛠️ Architecture

1. **Paperclip (`:80`):** Your main interface. When you create an employee or delegate a task, Paperclip sends a webhook.
2. **Webhook Proxy (`Internal: 8080`):** Intercepts Paperclip webhooks and spawns ephemeral `openclaw` containers tied to specific MemPalace wings.
3. **MemPalace (`Internal: 5000`):** Acts as the centralized MCP Server, structuring long-term context into manageable Wings.

## 🤝 Customization

- To change how OpenClaw executes tasks, modify `webhook-proxy/main.py`.
- To update MemPalace versions, modify the `git clone` URL in `mempalace-docker/Dockerfile`.
