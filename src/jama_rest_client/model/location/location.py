from typing_extensions import Self

class Parent:
    project: int
    item: int
    
    def __init__(self):
        self.project = 0
        self.item = 0

    def __eq__(self, other: Self):
        return self.project == other.project \
            and self.item == other.item
    
class Location:
    global_sort_order: int
    parent: Parent
    sequence: str
    sort_order: int

    def __init__(self):
        self.global_sort_order = 0
        self.parent = Parent()
        self.sequence = ""
        self.sort_order = 0

    def __eq__(self, other: Self):
        return self.global_sort_order == other.global_sort_order \
            and self.parent == other.parent \
            and self.sequence == other.sequence \
            and self.sort_order == other.sort_order