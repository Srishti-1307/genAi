# joule refers this file to know what tools does it have & which tool to call

def get_tools():
    return {
        "tools" : [
            {
                "name": "find_entity_by_name",
                "description" : "Find SAP S/4 entities using a business term",
                "input_schema" : {
                    "type" : "object",
                    "properties" : {"terms" : {"type": "string"}},
                    "required" : ["term"]
                },

            },
            {
                "name": "get_s4_entity_properties",
                "description" : "Get fields and metadata for an SAP entity",
                "input_schema" : {
                    "type" : "object",
                    "properties" : {"entity" : {"type" : "string"}},
                    "required" : ["entity"]
                }
            }
        ]
    }