from jama_rest_client.model.http import HTTPRequest
from typing_extensions import Self

class HTTPRequestBuilder:
    __request: HTTPRequest

    def __init__(self):
        self.__request = HTTPRequest()

    def set_method(self, method: str) -> Self:
        self.__request.method = method
        return self
    
    def set_resource(self, resource: str) -> Self:
        self.__request.resource = resource
        return self
    
    def set_body(self, body: dict) -> Self:
        self.__request.body = body
        return self
    
    def get_element(self) -> HTTPRequest:
        return self.__request