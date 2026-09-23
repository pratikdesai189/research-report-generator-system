# tools.py
import os
from dotenv import load_dotenv

load_dotenv()

# ============ SEARCH TOOL ============
from langchain_tavily import TavilySearch

search_tool = TavilySearch(
    max_results=5,
    topic="general",
)

# ============ ANALYSIS TOOL ============
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5-nano")

@tool
def analyze_content(text: str) -> str:
    """Analyze content and extract key points."""
    prompt = f"""
    Analyze this content and extract the top 5 key points:
    
    {text}
    
    Return as a numbered list.
    """
    response = llm.invoke(prompt)
    return response.content

# ============ WRITING TOOL ============
@tool
def write_report(findings: str) -> str:
    """Write a professional report from findings."""
    prompt = f"""
    Create a professional report based on these findings:
    
    {findings}
    
    Format as:
    ## Executive Summary
    (2-3 sentences overview)
    
    ## Key Points
    (list of main findings)
    
    ## Conclusion
    (wrap up)
    """
    response = llm.invoke(prompt)
    return response.content

# ============ TEST (if running directly) ============
if __name__ == "__main__":
    # Test search
    print("Testing search tool...")
    results = search_tool.invoke({"query": "AI trends 2024"})
    print(f"Results content: {results}\n")
    
    # Test analysis
    print("Testing analysis tool...")
    analysis = analyze_content.invoke({"text": "Python is popular for AI development"})
    print(f"Analysis: {analysis}\n")
    
    # Test writing
    print("Testing write tool...")
    report = write_report.invoke({"findings": "Finding 1: Python is key. Finding 2: AI is growing"})
    print(f"Report preview: {report[:100]}...\n")