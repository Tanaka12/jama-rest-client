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

class APIUpdateResponse:
    status: int
    statusResonPhrase: str

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""

class APIDeleteResponse:
    status: int
    status_reason_phrase: str

    def __init__(self):
        self.status = 0
        self.status_reason_phrase = ""
