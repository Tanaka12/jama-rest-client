from .http_request import HTTPRequest 

class HTTPResponse:
    status_code: int
    body: dict
    request: HTTPRequest

    def __init__(self):
        self.status_code = 0
        self.body = {}
        self.request = HTTPRequest()
    
    def __eq__(self, other):
        if self.status_code == other.status_code \
        and self.body == other.body \
        and self.request == other.request:
            return True

        return False