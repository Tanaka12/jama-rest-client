from typing import List

class Item:
    id: int
    document_key: str
    name: str
    type_id: int

    def __init__(self):
        self.id = 0
        self.document_key = ""
        self.name = ""
        self.type_id = 0