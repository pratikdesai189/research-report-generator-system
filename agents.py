# agents.py
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, analyze_content, write_report

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano")

# ============ RESEARCHER AGENT ============
researcher_agent = create_agent(
    model=llm,
    tools=[search_tool],
    system_prompt="You are a research expert. Search for accurate information and provide detailed findings."
)

# ============ ANALYZER AGENT ============
analyzer_agent = create_agent(
    model=llm,
    tools=[analyze_content],
    system_prompt="You are an analyst. Extract key insights and patterns from content."
)

# ============ WRITER AGENT ============
writer_agent = create_agent(
    model=llm,
    tools=[write_report],
    system_prompt="You are a professional writer. Create clear, well-structured reports."
)

# ============ TEST (if running directly) ============
if __name__ == "__main__":
    from langchain_core.messages import HumanMessage
    
    # Test researcher
    print("=== Testing Researcher Agent ===")
    result = researcher_agent.invoke({
        "messages": [HumanMessage(content="Search for Python AI trends 2024")]
    })
    print(f"Researcher result: {result['messages'][-1].content[:200]}...\n")
    
    # Test analyzer
    print("=== Testing Analyzer Agent ===")
    result = analyzer_agent.invoke({
        "messages": [HumanMessage(content="Analyze this: Machine learning is growing rapidly")]
    })
    print(f"Analyzer result: {result['messages'][-1].content[:200]}...\n")
    
    # Test writer
    print("=== Testing Writer Agent ===")
    result = writer_agent.invoke({
        "messages": [HumanMessage(content="Write a report about: AI trends, ML adoption, and future outlook")]
    })
    print(f"Writer result: {result['messages'][-1].content[:200]}...\n")