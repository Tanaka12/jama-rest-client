from .api_exceptions import APIElementNotFoundException, APIUnauthorizedException, APIUnknownException

from jama_rest_client.http import HTTPClient
from jama_rest_client.model.http import HTTPResponse

class BaseAPI:
    __http_client: HTTPClient

    def __init__(self, http_client: HTTPClient):
        self.__http_client = http_client

    def _put(self, resource: str, body: dict) -> HTTPResponse:
        http_response: HTTPResponse = self.__http_client.put(resource, body)
        
        self.__process_response(http_response)
        return http_response
    
    def _patch(self, resource: str, body: dict) -> HTTPResponse:
        http_response: HTTPResponse = self.__http_client.patch(resource, body)
        
        self.__process_response(http_response)
        return http_response
    
    def _post(self, resource: str, body: dict) -> HTTPResponse:     
        http_response: HTTPResponse = self.__http_client.post(resource, body)
        
        self.__process_response(http_response)
        return http_response
    
    def _get(self, resource: str) -> HTTPResponse:
        http_response: HTTPResponse = self.__http_client.get(resource)
        
        self.__process_response(http_response)
        return http_response
        
    def _delete(self, resource: str) -> HTTPResponse:
        http_response: HTTPResponse = self.__http_client.delete(resource)
        
        self.__process_response(http_response)
        return http_response
    
    def __process_response(self, http_response: HTTPResponse):
        if http_response.status_code == 401:
            raise APIUnauthorizedException()
        
        if http_response.status_code == 404:
            raise APIElementNotFoundException(http_response.request.resource)
        
        if http_response.status_code > 299 or http_response.status_code < 200:
            raise APIUnknownException()
