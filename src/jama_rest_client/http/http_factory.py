from jama_rest_client import Context

from .http_client import HTTPClient

class HTTPFactory:
    __context: Context

    def __init__(self, context: Context):
        self.__context = context

    def build_http_client(self) -> HTTPClient:
        return HTTPClient(self.__context)