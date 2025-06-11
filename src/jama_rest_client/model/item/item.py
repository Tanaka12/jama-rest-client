from typing import List
from typing_extensions import Self

class ItemLock:
    locked: bool
    last_locked_date: str

    def __init__(self):
        self.locked = False
        self.last_locked_date = ""

    def __eq__(self, other: Self):
        if self.locked == other.locked \
        and self.last_locked_date == other.last_locked_date:
            return True

        return False

class ItemLocation:
    sort_order: int
    global_sort_order: int
    sequence: str

    def __init__(self):
        self.sort_order = 0
        self.global_sort_order = 0
        self.sequence = ""

    def __eq__(self, other: Self):
        if self.sort_order == other.sort_order \
        and self.global_sort_order == other.global_sort_order \
        and self.sequence == other.sequence:
            return True

        return False

class Item:
    id: int
    document_key: str
    global_id: str
    item_type: int
    project: int
    created_date: str
    modified_date: str
    last_activity_date: str
    created_by: int
    modified_by: int
    lock: ItemLock
    location: ItemLocation
    fields: List[dict]

    def __init__(self):
        self.id = 0
        self.document_key = ""
        self.global_id = ""
        self.item_type = 0
        self.project = "" 
        self.created_date = "" 
        self.modified_date = ""
        self.last_activity_date = ""
        self.created_by = 0
        self.modified_by = 0
        self.lock = ItemLock()
        self.location = ItemLocation()
        self.fields = {}

    def __eq__(self, other: Self):
        if self.id == other.id \
        and self.document_key == other.document_key \
        and self.global_id == other.global_id \
        and self.item_type == other.item_type \
        and self.project == other.project \
        and self.created_date == other.created_date \
        and self.modified_date == other.modified_date \
        and self.last_activity_date == other.last_activity_date \
        and self.created_by == other.created_by \
        and self.modified_by == other.modified_by \
        and self.lock == other.lock \
        and self.location == other.location \
        and self.fields == other.fields:
            return True

        return False