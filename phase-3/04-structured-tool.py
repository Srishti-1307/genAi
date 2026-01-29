from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


# arg-schema using pydantic
class MultiplyInput(BaseModel):                   # a pydantic model that inherits from BaseModel
    a : int = Field(required=True, description="First number")
    b : int = Field(required=True, description="Second number")


def multiply(a,b):
    return a*b


tool = StructuredTool.from_function(
    func = multiply,
    name = "multiply",
    description = "multiply 2 numbers",
    args_schema = MultiplyInput
)

result = tool.invoke({'a':13, 'b':5})

print(result)

print(tool.name)
print(tool.description)