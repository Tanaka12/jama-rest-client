from typing import List
from typing_extensions import Self

class ItemTypeField:
    id: int
    name: str
    label: str
    field_type: str
    read_only: bool
    required: bool
    trigger_suspect: bool
    synchronize: bool
    text_type: str

    def __init__(self):
        self.id = 0
        self.name = ""
        self.label = ""
        self.field_type = ""
        self.read_only = False
        self.required = False
        self.trigger_suspect = False
        self.synchronize = False
        self.text_type = ""

    def __eq__(self, other: Self):
        if self.id == other.id \
        and self.name == other.name \
        and self.label == other.label \
        and self.field_type == other.field_type \
        and self.read_only == other.read_only \
        and self.required == other.required \
        and self.trigger_suspect == other.trigger_suspect \
        and self.synchronize == other.synchronize \
        and self.text_type == other.text_type:
            return True

        return False

class ItemType:
    id: int
    key: str
    display: str
    display_plural: str
    description: str
    category: str
    fields: List[ItemTypeField]

    def __init__(self):
        self.id = 0
        self.key = ""
        self.display = ""
        self.display_plural = ""
        self.description = ""
        self.category = ""
        self.fields = []

    def __eq__(self, other: Self):
        if self.id == other.id \
        and self.key == other.key \
        and self.display == other.display \
        and self.display_plural == other.display_plural \
        and self.description == other.description \
        and self.category == other.category \
        and self.fields == other.fields:
            return True

        return False