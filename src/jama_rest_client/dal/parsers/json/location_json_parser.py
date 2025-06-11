from datetime import datetime
from jama_rest_client.model.location import Location, Parent

class LocationJSONParser:

    @staticmethod
    def parse(location_dict: dict) -> Location:
        location: Location = Location()
        location.global_sort_order = location_dict['globalSortOrder']
        location.parent = LocationJSONParser.__parse_parent(location_dict['parent'])
        location.sequence = location_dict['sequence']
        location.sort_order = location_dict['sortOrder']

        return location
    
    @staticmethod
    def __parse_parent(parent_dict: dict) -> Parent:
        parent: Parent = Parent()
        parent.project = parent_dict['project']
        parent.item = parent_dict['item']

        return parent
