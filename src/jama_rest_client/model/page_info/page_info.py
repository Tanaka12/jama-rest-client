from typing_extensions import Self

class PageInfo:
    start_index: int
    result_count: int
    total_results: int

    def __init__(self):
        self.start_index = 0
        self.result_count = 0
        self.total_results = 0

    def __eq__(self, other: Self):
        return self.start_index == other.start_index \
            and self.result_count == other.result_count \
            and self.total_results == other.total_results