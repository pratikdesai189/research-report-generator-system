# main.py
from tools import search_tool, analyze_content, write_report

# Test search
print("=== SEARCH TEST ===")
results = search_tool.invoke({"query": "Wimbledon 2024"})
print(results)

print("\n=== ANALYSIS TEST ===")
analysis = analyze_content("Tennis is a racquet sport")
print(analysis)

print("\n=== WRITE TEST ===")
report = write_report("Finding: Tennis popularity growing")
print(report)