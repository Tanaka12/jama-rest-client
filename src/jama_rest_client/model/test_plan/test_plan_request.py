from typing_extensions import Self

class TestPlanRequest:
    project: int
    fields: dict

    def __init__(self):
        self.project = 0
        self.fields = {}

    def __eq__(self, other: Self):
        return self.project == other.project \
            and self.fields == other.fields