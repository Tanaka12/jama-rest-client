from .http_request import HTTPRequest 

class HTTPResponse:
    status_code: int
    body: dict
    request: HTTPRequest

    def __init__(self):
        self.status_code = 0
        self.body = {}
        self.request = HTTPRequest()