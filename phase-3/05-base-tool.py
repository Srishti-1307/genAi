from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class AddInputargSchema(BaseModel):
    a : int = Field(required=True, description="First number")
    b : int = Field(required=True, description="Second number")


class AddTool(BaseTool):                    # child class multiply-tool of BaseTool class
    name : str = "Add"
    description : str = "Add 2 numbers"
    args_schema : Type[BaseModel] = AddInputargSchema

    def _run(self, a:int, b:int) -> int:
        return a+b
    

tool = AddTool() 
result = tool.invoke({'a':100, "b":200})   
print(result)
print(tool.name)
print(tool.description)