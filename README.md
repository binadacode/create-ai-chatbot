# create-ai-chatbot

[![PyPI version](https://img.shields.io/pypi/v/create-ai-chatbot.svg)](https://pypi.org/project/create-ai-chatbot/)
[![npm version](https://img.shields.io/npm/v/create-ai-chatbot.svg)](https://www.npmjs.com/package/create-ai-chatbot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

Scaffold a full-stack AI chatbot project in seconds. Stop rebuilding the same chatbot architecture — start customizing.

```bash
# Via PyPI
pip install create-ai-chatbot
create-ai-chatbot my-chatbot

# Via npm
npx create-ai-chatbot my-chatbot
```

![Chatbot Demo](assets/demo.png)

## What you get

A production-ready chatbot with:

- **Backend:** FastAPI with streaming SSE endpoint (`/chat`)
- **Frontend:** Vite + React with a floating chat widget
- **LLM:** OpenRouter (supports 100+ models, free tier available)
- **Deploy:** Ready for Render (backend) + Vercel (frontend)

## Interactive setup

```
$ create-ai-chatbot
==================================================
  create-ai-chatbot
  Full-stack AI chatbot scaffolding tool
==================================================

project_name [my-ai-chatbot]:
project_slug [my-ai-chatbot]:
description [AI Chatbot powered by OpenRouter]:
backend [fastapi]:
frontend [vite-react]:
llm_provider [openrouter]:
theme [dark-minimal]:
```

## Quick start after scaffolding

```bash
cd my-chatbot

# Terminal 1 — Backend
cd backend
cp .env.example .env
# Edit .env: add your OPENROUTER_API_KEY (free at https://openrouter.ai/keys)
pip install -r requirements.txt
python -m uvicorn main:app --reload

# Terminal 2 — Frontend
cd frontend
npm install
npm run dev
```

Open http://localhost:3000 — click the chat button in the bottom-right.

## Deploy

### Backend → Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/YOUR_USERNAME/create-ai-chatbot)

1. Push to GitHub
2. Create new Web Service on Render
3. Build: `cd backend && pip install -r requirements.txt`
4. Start: `cd backend && python -m uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add env var: `OPENROUTER_API_KEY`

### Frontend → Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/create-ai-chatbot)

1. Import repo on Vercel
2. Set root directory to `frontend`
3. Add env var: `VITE_API_URL` = your Render backend URL

## Customization

### Change the system prompt

Edit `backend/data/system_prompt.py`:

```python
SYSTEM_PROMPT = """You are a real estate assistant for Acme Properties.
Help users find apartments, schedule viewings, and answer questions."""
```

### Change the model

Edit `backend/.env`:

```
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
```

Or any model from https://openrouter.ai/models.

### Add tools

Edit `backend/main.py` to add function-calling tools. The streaming SSE format supports tool calls via OpenRouter's OpenAI-compatible API.

### Change the theme

Edit `frontend/tailwind.config.js` to customize colors, fonts, and styling.

## Project structure

```
my-chatbot/
├── backend/
│   ├── main.py              # FastAPI app with /chat and /health
│   ├── config.py            # Settings via pydantic-settings
│   ├── schemas.py           # Pydantic request/response models
│   ├── services/
│   │   └── llm.py           # LLM service with streaming
│   ├── data/
│   │   └── system_prompt.py # Your system prompt
│   ├── requirements.txt
│   ├── .env.example
│   └── render.yaml          # Render deployment config
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── index.css
│   │   └── components/
│   │       └── Chat.tsx     # Floating chat widget
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── tsconfig.node.json
├── .gitignore
└── README.md
```

## Supported configurations

| Option | Choices |
|--------|---------|
| Backend | `fastapi` |
| Frontend | `vite-react` |
| LLM Provider | `openrouter` (default), `openai` |
| Theme | `dark-minimal` (default) |

## Why this exists

I built the same chatbot architecture three times — for a real estate company, a hackathon, and a client project. Every time: FastAPI backend, React frontend, OpenRouter for LLM, streaming SSE, floating chat widget. The only thing that changed was the system prompt and the tools.

So I packaged it. Now you can go from zero to a deployed AI chatbot in under 5 minutes.

## Contributing

PRs welcome! Areas we'd love help with:

- Next.js App Router template option
- Anthropic Claude direct integration
- Pre-built tool templates (RAG, web search, database)
- Additional themes

## License

MIT
