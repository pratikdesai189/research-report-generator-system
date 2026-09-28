# Research Report Generator System

Multi-agent AI system that researches, analyzes, and writes professional reports.

## 🚀 Live Demo

**API:** https://researchreport-generatorsystem-production.up.railway.app/docs

**Example Query:**
```bash
curl -X POST "https://researchreport-generatorsystem-production.up.railway.app/research" \
  -H "Content-Type: application/json" \
  -d '{"query": "What are AI trends 2024?", "session_id": "session1"}'
```

## Architecture

- **Researcher Agent**: Web search + synthesis (Tavily)
- **Analyzer Agent**: Key insight extraction
- **Writer Agent**: Professional report generation
- **Memory**: InMemorySaver (per-session conversations)

## Tech Stack

- Python, LangChain, LangGraph
- FastAPI (REST API)
- Railway (Deployment)
- OpenAI GPT-5-nano
- Tavily Search API

## Features

✅ Multi-agent orchestration
✅ Persistent conversation memory
✅ Web search integration
✅ Professional report generation
✅ REST API with Swagger UI
✅ Production deployment

## Try It

1. Open: https://researchreport-generatorsystem-production.up.railway.app/docs
2. Click "/research" endpoint
3. Fill in your query
4. Click Execute
5. See full research report!