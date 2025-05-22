from typing import List

class ItemTypeField:
    id: int
    name: str
    label: str
    fieldType: str
    readOnly: bool
    required: bool
    triggerSuspect: bool
    synchronize: bool
    textType: str

    def __init__(self):
        self.id = 0
        self.name = ""
        self.label = ""
        self.fieldType = ""
        self.readOnly = False
        self.required = False
        self.triggerSuspect = False
        self.synchronize = False
        self.textType = ""

class ItemType:
    id: int
    key: str
    display: str
    displayPlural: str
    description: str
    category: str
    fields: List[ItemTypeField]

    def __init__(self):
        self.id = 0
        self.key = ""
        self.display = ""
        self.displayPlural = ""
        self.description = ""
        self.category = ""
        self.fields = []