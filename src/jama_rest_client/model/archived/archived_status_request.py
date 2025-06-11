from typing_extensions import Self
   
class ArchivedStatusRequest:
    archived: bool

    def __init__(self):
        self.archived = False

    def __eq__(self, other: Self):
        return self.archived == other.archived