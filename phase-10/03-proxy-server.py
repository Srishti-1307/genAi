from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://remote-expensetracker.fastmcp.app/mcp",
    name="proxy-for-remote")

if __name__ == "__main__":
    mcp.run()
