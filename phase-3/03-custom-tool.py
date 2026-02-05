from langchain_core.tools import tool

# while creating custom tools.. add doc-string , type-hinting & @tool decorator

@tool
def multiply(a:int, b:int) -> int:
    """Multiplies 2 numbers (a & b)"""
    return a*b

result = multiply.invoke({'a':3, 'b':5})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)