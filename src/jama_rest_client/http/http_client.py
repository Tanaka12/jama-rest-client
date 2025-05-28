import http.client as httplib
import json
import ssl

from jama_rest_client import Context
from jama_rest_client.http.http_exceptions import HTTPConnectionException
from jama_rest_client.model.http import HTTPResponse, HTTPRequest 

class HTTPClient:
    __context: Context
    __headers: dict

    def __init__(self, context: Context):
        self.__context = context
        self.__headers = {
                            'Content-type': 'application/json',
                            'Authorization': context.authorization_secret 
                         }

    def put(self, resource: str, body: dict) -> HTTPResponse:
        http_request: HTTPRequest = HTTPRequest()
        http_request.method = 'PUT'
        http_request.body = body
        http_request.resource = resource

        return self.__request(http_request)
    
    def patch(self, resource: str, body: dict) -> HTTPResponse:
        http_request: HTTPRequest = HTTPRequest()
        http_request.method = 'PATCH'
        http_request.body = body
        http_request.resource = resource

        return self.__request(http_request)

    def post(self, resource: str, body: dict) -> HTTPResponse:
        http_request: HTTPRequest = HTTPRequest()
        http_request.method = 'POST'
        http_request.body = body
        http_request.resource = resource

        return self.__request(http_request)        

    def get(self, resource: str) -> HTTPResponse:
        
        http_request: HTTPRequest = HTTPRequest()
        http_request.method = 'GET'
        http_request.resource = resource

        return self.__request(http_request)
    
    def delete(self, resource: str) -> HTTPResponse:
        
        http_request: HTTPRequest = HTTPRequest()
        http_request.method = 'DELETE'
        http_request.resource = resource

        return self.__request(http_request)
        
    def __request(self, http_request: HTTPRequest) -> HTTPResponse:
        connection = httplib.HTTPSConnection(self.__context.host, self.__context.port, context = ssl._create_unverified_context())
        
        try:
            connection.request(http_request.method, http_request.resource, json.dumps(http_request.body), self.__headers)
            response = connection.getresponse()

            http_response: HTTPResponse = HTTPResponse()
            http_response.status_code = response.status
            http_response.body = json.loads(response.read())
            http_response.request = http_request

            return http_response
        except:
            raise HTTPConnectionException(self.__context.host, self.__context.port)
        
        