from datetime import datetime
from typing_extensions import Self

class Lock:
    locked: bool
    last_locked_date: datetime
    locked_by: int

    def __init__(self):
        self.locked = False
        self.last_locked_date = datetime.fromtimestamp(0)
        self.locked_by = 0

    def __eq__(self, other: Self):
        return self.locked == other.locked \
            and self.last_locked_date == other.last_locked_date \
            and self.locked_by == other.locked_by