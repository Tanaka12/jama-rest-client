from datetime import datetime
from typing_extensions import Self

class Project:
    id: int
    project_key: str
    parent: int
    is_folder: bool
    created_date: datetime
    modified_date: datetime
    created_by: int
    modified_by: int
    fields: dict

    def __init__(self):
        self.id = 0
        self.project_key = ""
        self.parent = 0
        self.is_folder = False
        self.created_date = datetime.fromtimestamp(0)
        self.modified_date = datetime.fromtimestamp(0)
        self.created_by = 0
        self.modified_by = 0
        self.fields = {}

    def __eq__(self, other: Self):
        return self.id == other.id \
            and self.project_key == other.project_key \
            and self.parent == other.parent \
            and self.is_folder == other.is_folder \
            and self.created_date == other.created_date \
            and self.modified_date == other.modified_date \
            and self.created_by == other.created_by \
            and self.modified_by == other.modified_by \
            and self.fields == other.fields