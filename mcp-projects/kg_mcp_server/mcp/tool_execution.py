# runs the tool joule selected


import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# sys.path is a list in Python that tells it where to look for modules. By default, it includes the directory where the script is located and some standard directories (like site-packages).

# Python couldn’t resolve the path to kg_mcp_server because Python doesn't consider the mcp folder to be part of the kg_mcp_server as You were running the script directly from the mcp folder, not from the root package.

# By modifying sys.path, you’re telling Python to add a new directory to the list of directories it searches for modules.



# from ..kg_provider import KgMetaDataProvider
from kg_mcp_server.kg_provider import KgMetaDataProvider
from fastapi import HTTPException



kg = KgMetaDataProvider()




def execute_tool(tool_name:str, payload:dict):
    
    if tool_name == 'find_entity_by_name':
        return{
            "entities" : kg.get_entity_by_term(payload["term"])
        }
    
    if tool_name == 'get_s4_entity_properties':
        return{
            "result" : kg.get_entity_fields(payload["entity"])
        }
    
    raise HTTPException(status_code=404, detail="Unknown MCP tool")