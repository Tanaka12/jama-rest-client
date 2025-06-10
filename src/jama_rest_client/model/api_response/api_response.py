from typing_extensions import Self

class APICreateResponse:
    status: int
    status_reason_phrase: str
    location: str
    id: int

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""
        self.location = ""
        self.id = 0

    def __eq__(self, other: Self):
        if self.status == other.status \
        and self.status_reason_phrase == other.status_reason_phrase \
        and self.location == other.location \
        and self.id == other.id:
            return True

        return False

class APIUpdateResponse:
    status: int
    statusResonPhrase: str

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""
    
    def __eq__(self, other: Self):
        if self.status == other.status \
        and self.status_reason_phrase == other.status_reason_phrase:
            return True

        return False

class APIDeleteResponse:
    status: int
    status_reason_phrase: str

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""

    def __eq__(self, other: Self):
        if self.status == other.status \
        and self.status_reason_phrase == other.status_reason_phrase:
            return True

        return False
