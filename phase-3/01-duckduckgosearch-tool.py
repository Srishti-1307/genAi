from langchain_community.tools import DuckDuckGoSearchRun

tool = DuckDuckGoSearchRun()

result = tool.invoke('UGC rule in India News')

print(result)