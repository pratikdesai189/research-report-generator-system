# Research Report Generator System

Multi-agent AI system with beautiful frontend that researches, analyzes, and writes professional reports.

## 🚀 Live Demo

**Visit:** https://researchreport-generatorsystem-production.up.railway.app/

Just enter your query and watch the AI work!

## Features

✅ Multi-agent research system
✅ Beautiful responsive UI
✅ Web search integration
✅ Automatic analysis & report generation
✅ Conversation memory (per-session)
✅ Production deployment
✅ REST API with Swagger docs

## Architecture

### Agents
- **Researcher Agent**: Searches the web (Tavily) and synthesizes information
- **Analyzer Agent**: Extracts key insights and patterns
- **Writer Agent**: Creates professional reports

### Tech Stack
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: FastAPI, Python
- **AI/ML**: LangChain, LangGraph, OpenAI GPT-5-nano
- **Search**: Tavily API
- **Memory**: InMemorySaver (conversation memory)
- **Deployment**: Railway (Docker)

## How It Works

1. User enters query in frontend
2. Query sent to /research endpoint
3. Researcher Agent searches web
4. Analyzer Agent extracts insights
5. Writer Agent creates report
6. Report returned to frontend
7. User sees beautiful formatted result

## API Endpoints

### GET /
Serves the beautiful frontend UI

### POST /research
Generates research report

**Request:**
```json
{
  "query": "Your research question",
  "session_id": "session_1"
}
```

**Response:**
```json
{
  "status": "success",
  "report": "Full research report...",
  "session_id": "session_1"
}
```

### GET /docs
Swagger UI documentation

## Running Locally

```bash
# Setup
uv init
uv add langchain langchain-openai langchain-tavily fastapi uvicorn

# Run
uv run api.py

# Visit
http://localhost:8000
```

## Deployment

Deployed on Railway with:
- Auto-deployment from GitHub
- Environment variables for API keys
- Public URL for sharing
- Free tier (app sleeps when idle)

## Project Structure

research-report-generator-system/
├── main.py # Initial testing
├── tools.py # AI tools (search, analyze, write)
├── agents.py # Specialist agents
├── workflow.py # Agent orchestration
├── workflow_with_memory.py # With conversation memory
├── api.py # FastAPI server
├── static/
│ └── index.html # Beautiful frontend
├── requirements.txt # Dependencies
├── .env # Secrets (not in repo)
├── .gitignore
└── Procfile # Railway config


## Skills Demonstrated

- Multi-agent system architecture
- LangChain/LangGraph orchestration
- FastAPI REST API development
- Frontend/Backend integration
- Production deployment
- Error handling & debugging
- Conversation memory management
- Web search integration
- Professional UI/UX design

## Try It Now!

Visit: https://researchreport-generatorsystem-production.up.railway.app/

Example queries:
- "What are the latest AI trends in 2024?"
- "Explain quantum computing"
- "Who is Claude and what can it do?"
- "What are neural networks?"

## Author

Built by Pratik Desai (@ich_bin_pratik)
- Portfolio: [Your GitHub]
- Location: Frankfurt, Germany
- Focus: LLM/Agentic AI engineering