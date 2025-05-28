from jama_rest_client.model.http import HTTPRequest, HTTPResponse

class HTTPResponseBuilder:
    __response: HTTPResponse

    def __init__(self):
        self.__response = HTTPResponse()

    def set_status_code(self, status_code: int):
        self.__response.status_code = status_code
        return self
    
    def set_body(self, body: dict):
        self.__response.body = body
        return self
    
    def set_request(self, request: HTTPRequest):
        self.__response.request = request
        return self
    
    def get_element(self) -> HTTPResponse:
        return self.__response