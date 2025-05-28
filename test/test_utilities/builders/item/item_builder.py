from jama_rest_client.model.item import Item, ItemLocation, ItemLock

class ItemLockBuilder:
    __item_lock: ItemLock

    def __init__(self):
        self.__item_lock = ItemLock()

    def set_locked(self, locked: bool):
        self.__item_lock.locked = locked
        return self
    
    def set_last_locked_date(self, last_locked_date: str):
        self.__item_lock.last_locked_date = last_locked_date
        return self
    
    def get_element(self) -> ItemLock:
        return self.__item_lock

class ItemLocationBuilder:
    __item_location: ItemLocation

    def __init__(self):
        self.__item_location = ItemLocation()

    def set_sort_order(self, sort_order: int):
        self.__item_location.sort_order = sort_order
        return self
    
    def set_global_sort_order(self, global_sort_order: int):
        self.__item_location.global_sort_order = global_sort_order
        return self
    
    def set_sequence(self, sequence: str):
        self.__item_location.sequence = sequence
        return self
    
    def get_element(self) -> ItemLocation:
        return self.__item_location

class ItemBuilder:
    __item: Item

    def __init__(self):
        self.__item = Item()

    def set_id(self, id: int):
        self.__item.id = id
        return self
    
    def set_document_key(self, document_key: str):
        self.__item.document_key = document_key
        return self
    
    def set_global_id(self, global_id: str):
        self.__item.global_id = global_id
        return self

    def set_item_type(self, item_type: int):
        self.__item.item_type = item_type
        return self
    
    def set_project(self, project: int):
        self.__item.project = project
        return self
    
    def set_created_date(self, created_date: str):
        self.__item.created_date = created_date
        return self

    def set_modified_date(self, modified_date: str):
        self.__item.modified_date = modified_date
        return self

    def set_last_activity_date(self, last_activity_date: str):
        self.__item.last_activity_date = last_activity_date
        return self

    def set_created_by(self, created_by: int):
        self.__item.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int):
        self.__item.modified_by = modified_by
        return self

    def set_lock(self, lock: ItemLock):
        self.__item.lock = lock
        return self

    def set_location(self, location: ItemLocation):
        self.__item.location = location
        return self
    
    def set_fields(self, fields: dict):
        self.__item.fields = fields
        return self

    def get_element(self) -> Item:
        return self.__item