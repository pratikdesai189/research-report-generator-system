# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from agents import researcher_agent, analyzer_agent, writer_agent

load_dotenv()

app = FastAPI(title="Multi-Agent Research System")

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Add this after creating FastAPI app:
app = FastAPI(title="Multi-Agent Research System")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
def serve_frontend():
    """Serve the frontend"""
    return FileResponse("static/index.html")

# Rest of your code...

# ============ PYDANTIC MODELS ============
class ResearchRequest(BaseModel):
    query: str
    session_id: str = "default_session"

class ResearchResponse(BaseModel):
    status: str
    report: str
    session_id: str

# ============ WORKFLOW (copy from workflow_with_memory.py) ============
class ResearchState(TypedDict):
    messages: list
    research_complete: bool
    analysis_complete: bool
    report_complete: bool

workflow = StateGraph(ResearchState)

def research_node(state):
    result = researcher_agent.invoke(state)
    return {
        "messages": result["messages"],
        "research_complete": True
    }

def analyze_node(state):
    result = analyzer_agent.invoke(state)
    return {
        "messages": result["messages"],
        "analysis_complete": True
    }

def write_node(state):
    result = writer_agent.invoke(state)
    return {
        "messages": result["messages"],
        "report_complete": True
    }

workflow.add_node("researcher", research_node)
workflow.add_node("analyzer", analyze_node)
workflow.add_node("writer", write_node)

workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "analyzer")
workflow.add_edge("analyzer", "writer")
workflow.add_edge("writer", END)

memory = InMemorySaver()
multi_agent_system = workflow.compile(checkpointer=memory)

# ============ API ENDPOINTS ============
@app.get("/")
def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "Multi-Agent Research System",
        "version": "1.0"
    }

@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):
    """
    Research endpoint
    Takes a query, runs through all 3 agents, returns report
    """
    try:
        print(f"📝 Processing query: {request.query}")
        print(f"📌 Session: {request.session_id}")
        
        config = {"configurable": {"thread_id": request.session_id}}
        
        result = multi_agent_system.invoke({
            "messages": [HumanMessage(content=request.query)],
            "research_complete": False,
            "analysis_complete": False,
            "report_complete": False
        }, config=config)
        
        final_report = result["messages"][-1].content
        
        return ResearchResponse(
            status="success",
            report=final_report,
            session_id=request.session_id
        )
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return ResearchResponse(
            status="error",
            report=f"Error: {str(e)}",
            session_id=request.session_id
        )

# ============ RUN SERVER ============
if __name__ == "__main__":
    import uvicorn
    print("\n" + "=" * 60)
    print("🚀 Starting Multi-Agent Research API")
    print("=" * 60)
    print("📍 Local: http://127.0.0.1:8000")
    print("📍 Docs: http://127.0.0.1:8000/docs")
    print("=" * 60 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)