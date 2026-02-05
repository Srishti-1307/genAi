# This file has function definitions of tools

import json


class KgMetaDataProvider:
    """This class represents Knowledge Graph abstraction"""

    def __init__(self):
        with open('kg-data.json', 'r') as f:
            self.entities = json.load(f)  

    
    def get_entity_by_term(self, term): 
        term = term.lower()   
        matches = []
        for entity, meta in self.entities.items():
            if term in meta["business_terms"]:
                matches.append(entity)
        
        return matches 
    


    def get_entity_fields(self, entity):
        if entity not in self.entities:
            raise KeyError(f"Unknown Entity: {entity}")

        result = {}                    # final result to return

        # extract fields
        fields = self.entities[entity]['fields']
        result['fields'] = fields

        # build usage
        usage = {}
        for name, meta in fields.items():
            values = []

            if meta.get('key'):
                values.append("Primary key field")
            if meta.get('filterable'):
                values.append("Usable in OData $filter")
            if meta.get('aggregatable'):
                values.append("Usable in OData $apply aggregation")

            usage[name] = values

        result['usage'] = usage
    
        return result
    

if __name__ == "__main__":
    print(__name__)
