from enum import Enum
from typing import Optional
from typing_extensions import Self

class PatchOperationType(str, Enum):
    ADD = 'add'
    REMOVE = 'remove' 
    REPLACE = 'replace'

class PatchOperationRequest:
    op: PatchOperationType
    path: str
    value: Optional[any]

    def __init__(self):
        self.op = PatchOperationType.ADD
        self.path = ""
        self.value = None

    def __eq__(self, other: Self):
        return self.op == other.op \
            and self.path == other.path \
            and self.value == other.value
