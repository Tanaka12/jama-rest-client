from typing_extensions import Self

class TestGroup:
    id: int
    name: str
    assigned_to: int

    def __init__(self):
        self.id = 0
        self.name = ""
        self.assigned_to = 0

    def __eq__(self, other: Self):
        if self.id == other.id \
        and self.name == other.name \
        and self.assigned_to == other.assigned_to:
            return True

        return False