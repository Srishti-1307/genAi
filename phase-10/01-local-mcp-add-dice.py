from fastmcp import FastMCP
import random

# create fastmcp server instacnce
mcp = FastMCP(name="Demo Server")


# creating mcp tool
@mcp.tool()
def add_numbers(a:float, b:float) -> float:
    """Add 2 numbers"""
    print("Srishti's answer is ready!!")
    return a+b


# creating another mcp tool
@mcp.tool()
def roll_dice(n_dice:int = 1) -> list[int]:
    """Roll n_dice (a die n times) & return outcome of each time roll"""
    return [random.randint(1,6) for _ in range(n_dice)]



if __name__ == "__main__":
    mcp.run()



