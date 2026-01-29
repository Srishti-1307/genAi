# uv add langchain langchain-openai langchain-mcp-adapters python-dotenv streamlit

from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

SERVERS = {
    "Deomo Server" : {
        "transport" : "stdio",
        "command" : "uv",
        "args" : [
            "run",
            "fastmcp",
            "run",
            r"C:\Users\developer\practice_ai\GenAi Module\genAi\phase-10\02-local-mcp-expense-tracker.py"

        ]
    }
}



async def main():
    client = MultiServerMCPClient(SERVERS)
    tools = await client.get_tools()
    # print(tools)
    tools_dict = {}
    for tool in tools:
        tools_dict[tool.name] = tool
    print(tools_dict)




if __name__ == "__main__":
    asyncio.run(main())
