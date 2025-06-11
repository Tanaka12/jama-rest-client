from datetime import datetime
from jama_rest_client.model.item import Item
from jama_rest_client.model.location import Location
from jama_rest_client.model.lock import Lock
from typing_extensions import Self

class ItemBuilder:
    __item: Item

    def __init__(self):
        self.__item = Item()

    def set_id(self, id: int) -> Self:
        self.__item.id = id
        return self
    
    def set_document_key(self, document_key: str) -> Self:
        self.__item.document_key = document_key
        return self
    
    def set_global_id(self, global_id: str) -> Self:
        self.__item.global_id = global_id
        return self

    def set_item_type(self, item_type: int) -> Self:
        self.__item.item_type = item_type
        return self
    
    def set_project(self, project: int) -> Self:
        self.__item.project = project
        return self
    
    def set_child_item_type(self, child_item_type: int) -> Self:
        self.__item.child_item_type = child_item_type
        return self
    
    def set_created_date(self, created_date: datetime) -> Self:
        self.__item.created_date = created_date
        return self

    def set_modified_date(self, modified_date: datetime) -> Self:
        self.__item.modified_date = modified_date
        return self

    def set_last_activity_date(self, last_activity_date: datetime) -> Self:
        self.__item.last_activity_date = last_activity_date
        return self

    def set_created_by(self, created_by: int) -> Self:
        self.__item.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int) -> Self:
        self.__item.modified_by = modified_by
        return self

    def set_lock(self, lock: Lock) -> Self:
        self.__item.lock = lock
        return self

    def set_location(self, location: Location) -> Self:
        self.__item.location = location
        return self
    
    def set_fields(self, fields: dict) -> Self:
        self.__item.fields = fields
        return self

    def get_element(self) -> Item:
        return self.__item