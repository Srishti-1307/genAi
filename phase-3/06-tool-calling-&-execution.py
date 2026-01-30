from langchain_core.tools import tool
from langchain_ollama import ChatOllama


@tool
def add(a : int, b : int) -> int:
    """Add 2 numbers"""
    return a+b


@tool
def multiply(a : int, b : int) -> int:
    "Multiply 2 numbers"
    return a*b

llm = ChatOllama(model="llama3", temperature=0.1)
llm_with_tools = llm.bind_tools([multiply, add])              # tool registration with llm

llm_with_tools.invoke("Hi, how are you?")             # No tool calling happens here

result = llm_with_tools.invoke("what is 7 added to 13?")

print(result.tool_calls)

print(result.tool_calls[0])


final_result = result.tool_calls[0]['name'].invoke(result.tool_calls[0]['args'])
# or we can pass the complete result.tool_calls[0]
final_result = result.tool_calls[0]['name'].invoke(result.tool_calls[0])      # this gives ToolMessage




'''
Note : OllamaLLM or ChatOllamaLLM does not support tool calling or even tool binding
Therefore above code will throw lots of errors. 
'''