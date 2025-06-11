from datetime import datetime
from jama_rest_client.model.location import Location
from jama_rest_client.model.lock import Lock
from typing import List
from typing_extensions import Self
   
class Item:
    id: int
    document_key: str
    global_id: str
    item_type: int
    project: int
    child_item_type: int
    created_date: datetime
    modified_date: datetime
    last_activity_date: datetime
    created_by: int
    modified_by: int
    lock: Lock
    location: Location
    fields: List[dict]

    def __init__(self):
        self.id = 0
        self.document_key = ""
        self.global_id = ""
        self.item_type = 0
        self.project = "" 
        self.child_item_type = 0
        self.created_date = datetime.fromtimestamp(0) 
        self.modified_date = datetime.fromtimestamp(0) 
        self.last_activity_date = datetime.fromtimestamp(0) 
        self.created_by = 0
        self.modified_by = 0
        self.lock = Lock()
        self.location = Location()
        self.fields = {}

    def __eq__(self, other: Self):
        return self.id == other.id \
            and self.document_key == other.document_key \
            and self.global_id == other.global_id \
            and self.item_type == other.item_type \
            and self.project == other.project \
            and self.child_item_type == other.child_item_type \
            and self.created_date == other.created_date \
            and self.modified_date == other.modified_date \
            and self.last_activity_date == other.last_activity_date \
            and self.created_by == other.created_by \
            and self.modified_by == other.modified_by \
            and self.lock == other.lock \
            and self.location == other.location \
            and self.fields == other.fields