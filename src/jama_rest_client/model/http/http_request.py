class HTTPRequest:
    method: str
    resource: str
    body: dict

    def __init__(self):
        self.method = ""
        self.body = {}
        self.resource = ""

    def __eq__(self, other):
        if self.method == other.method \
        and self.body == other.body \
        and self.resource == other.resource:
            return True

        return False