from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from mcp.tool_registry import get_tools
from mcp.tool_execution import execute_tool

app = FastAPI()

@app.get("/mcp")
def mcp_info():
    return {
        "name": "kg-mcp-server",
        "version": "1.0",
        "description": "SAP Knowledge Graph MCP Server"
    }

@app.get("/mcp/tools")
def list_tools():
    return get_tools()

class FindEntityAndEntityPropertiesRequest(BaseModel):
    term: Optional[str] = Field(None, description='Business term provided by user')
    entity: Optional[str] = Field(None, description='Selected SAP Entity')






@app.post("/mcp/tools/{tool_name}")
def tool_run(tool_name:str, req:FindEntityAndEntityPropertiesRequest):
    try:
        # If term is provided, route to find_entity_by_term
        if req.term:
            
            result = execute_tool(tool_name, {"term": req.term})

        # If entity is provided, route to get_s4_entity_properties
        elif req.entity:
            
            result = execute_tool(tool_name, {"entity": req.entity})
       
        return {"result": result}
        
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))