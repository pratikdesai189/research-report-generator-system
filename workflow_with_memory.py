# workflow_with_memory.py
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from typing_extensions import TypedDict
from agents import researcher_agent, analyzer_agent, writer_agent

load_dotenv()

class ResearchState(TypedDict):
    messages: list
    research_complete: bool
    analysis_complete: bool
    report_complete: bool

workflow = StateGraph(ResearchState)

def research_node(state):
    print("\n📊 RESEARCHER WORKING...")
    result = researcher_agent.invoke(state)
    return {
        "messages": result["messages"],
        "research_complete": True
    }

def analyze_node(state):
    print("\n🔍 ANALYZER WORKING...")
    result = analyzer_agent.invoke(state)
    return {
        "messages": result["messages"],
        "analysis_complete": True
    }

def write_node(state):
    print("\n✍️ WRITER WORKING...")
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

# ============ ADD MEMORY ============
memory = InMemorySaver()
multi_agent_system = workflow.compile(checkpointer=memory)

# ============ TEST WITH MEMORY ============
if __name__ == "__main__":
    print("=" * 60)
    print("🤖 MULTI-AGENT SYSTEM WITH MEMORY")
    print("=" * 60)
    
    # Use thread_id for memory
    config = {"configurable": {"thread_id": "research_session_1"}}
    
    # Query 1
    print("\n📝 Query 1: What are AI trends 2024?")
    result1 = multi_agent_system.invoke({
        "messages": [HumanMessage(content="What are AI trends 2024?")],
        "research_complete": False,
        "analysis_complete": False,
        "report_complete": False
    }, config=config)
    
    print("\n📄 Report 1 Preview:")
    print(result1["messages"][-1].content[:150] + "...\n")
    
    # Query 2 (with memory!)
    print("\n" + "=" * 60)
    print("📝 Query 2: Tell me more about LLMs")
    result2 = multi_agent_system.invoke({
        "messages": [HumanMessage(content="Tell me more about LLMs specifically")],
        "research_complete": False,
        "analysis_complete": False,
        "report_complete": False
    }, config=config)
    
    print("\n📄 Report 2 (with memory):")
    print(result2["messages"][-1].content[:150] + "...\n")
    
    print("=" * 60)
    print("✅ System remembered previous query!")
    print("=" * 60)