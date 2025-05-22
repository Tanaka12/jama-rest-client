class HTTPRequest:
    method: str
    resource: str
    body: str

    def __init__(self):
        self.method = ""
        self.body = ""
        self.resource = ""