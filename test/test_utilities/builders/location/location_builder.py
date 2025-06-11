from jama_rest_client.model.location import Location, Parent
from typing_extensions import Self

class LocationBuilder:
    __location: Location

    def __init__(self):
        self.__location = Location()

    def set_global_sort_order(self, global_sort_order: int) -> Self:
        self.__location.global_sort_order = global_sort_order
        return self
    
    def set_parent(self, parent: Parent) -> Self:
        self.__location.parent = parent
        return self

    def set_sequence(self, sequence: str) -> Self:
        self.__location.sequence = sequence
        return self
    
    def set_sort_order(self, sort_order: int) -> Self:
        self.__location.sort_order = sort_order
        return self
    
    def get_element(self) -> Location:
        return self.__location
    
class ParentBuilder:
    __parent: Parent

    def __init__(self):
        self.__parent = Parent()

    def set_project(self, project: int) -> Self:
        self.__parent.project = project
        return self
    
    def set_item(self, item: int) -> Self:
        self.__parent.item = item
        return self
    
    def get_element(self) -> Parent:
        return self.__parent