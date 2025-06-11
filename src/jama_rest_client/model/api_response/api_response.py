from ..page_info import PageInfo
from typing_extensions import Self

class CreatedResponse:
    status: int
    status_reason_phrase: str
    page_info: PageInfo
    location: str
    id: int

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""
        self.page_info = PageInfo()
        self.location = ""
        self.id = 0

    def __eq__(self, other: Self):
        return self.status == other.status \
            and self.status_reason_phrase == other.status_reason_phrase \
            and self.page_info == other.page_info \
            and self.location == other.location \
            and self.id == other.id

class AbstractRestResponse:
    status: int
    status_reason_phrase: str
    page_info: PageInfo

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""
        self.page_info = PageInfo()
    
    def __eq__(self, other: Self):
        return self.status == other.status \
            and self.status_reason_phrase == other.status_reason_phrase \
            and self.page_info == other.page_info