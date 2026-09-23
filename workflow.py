# workflow.py
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from agents import researcher_agent, analyzer_agent, writer_agent

load_dotenv()

# ============ DEFINE WORKFLOW STATE ============
class ResearchState(TypedDict):
    messages: list
    research_complete: bool
    analysis_complete: bool
    report_complete: bool

# ============ CREATE WORKFLOW ============
workflow = StateGraph(ResearchState)

# ============ ADD NODES (Agent Steps) ============
def research_node(state):
    """Step 1: Researcher searches for info"""
    print("\n📊 RESEARCHER WORKING...")
    result = researcher_agent.invoke(state)
    return {
        "messages": result["messages"],
        "research_complete": True
    }

def analyze_node(state):
    """Step 2: Analyzer extracts key points"""
    print("\n🔍 ANALYZER WORKING...")
    result = analyzer_agent.invoke(state)
    return {
        "messages": result["messages"],
        "analysis_complete": True
    }

def write_node(state):
    """Step 3: Writer creates final report"""
    print("\n✍️ WRITER WORKING...")
    result = writer_agent.invoke(state)
    return {
        "messages": result["messages"],
        "report_complete": True
    }

# ============ BUILD WORKFLOW ============
workflow.add_node("researcher", research_node)
workflow.add_node("analyzer", analyze_node)
workflow.add_node("writer", write_node)

# ============ CONNECT NODES ============
workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "analyzer")
workflow.add_edge("analyzer", "writer")
workflow.add_edge("writer", END)

# ============ COMPILE ============
multi_agent_system = workflow.compile()

# ============ TEST ============
if __name__ == "__main__":
    print("=" * 60)
    print("🤖 MULTI-AGENT RESEARCH SYSTEM")
    print("=" * 60)
    
    user_query = "What are the latest AI trends in 2024?"
    print(f"\n📝 User Query: {user_query}\n")
    
    result = multi_agent_system.invoke({
        "messages": [HumanMessage(content=user_query)],
        "research_complete": False,
        "analysis_complete": False,
        "report_complete": False
    })
    
    print("\n" + "=" * 60)
    print("📄 FINAL REPORT")
    print("=" * 60)
    final_message = result["messages"][-1]
    print(f"\n{final_message.content}\n")
    print("=" * 60)