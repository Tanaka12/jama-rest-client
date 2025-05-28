import json
import pytest
from unittest.mock import ANY, patch

from jama_rest_client import Context
from jama_rest_client.http import HTTPClient, HTTPConnectionException

from mocks.projects import ProjectsMocks, PROJECTS_API_MOCKS
from test_utilities.builders import HTTPRequestBuilder, HTTPResponseBuilder

class TestHTTPClient():
    __service: HTTPClient
    __context: Context

    def setup_method(self):
        self.__context = Context('127.0.0.1', 123, 'DummyUser', 'DummyPassword')
        self.__service = HTTPClient(self.__context)
    
    @pytest.fixture(scope='function')
    def https_connection_mock(self):
        with patch('jama_rest_client.http.http_client.httplib.HTTPSConnection') as mock_class:
            mock_class.return_value.getresponse.return_value.status = 200
            mock_class.return_value.getresponse.return_value.read.return_value = '{}'
            yield mock_class
    
    # PUT tests
    def test_validate_happy_path_http_client_put_connects_to_given_host_port(self, https_connection_mock) -> None:
        self.__service.put('DummyResource', {})

        https_connection_mock.assert_called_with(self.__context.host, self.__context.port, context=ANY)


    def test_validate_happy_path_http_client_put_calls_request_with_expected_parameters(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body: dict = {}
        
        self.__service.put(resource, body)

        expected_headers: dict = {
                                    'Content-type': 'application/json',
                                    'Authorization': self.__context.authorization_secret 
                                 }
        https_connection_mock.return_value.request.assert_called_with('PUT', resource, '{}', expected_headers)

    def test_validate_happy_path_http_client_put_returns_expected_value(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body_request: dict = {}
        body_response: dict = PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT]
        body_response_serialized: str = json.dumps(body_response) 

        https_connection_mock.return_value.getresponse.return_value.read.return_value = body_response_serialized

        http_response = self.__service.put(resource, body_request)

        expected_http_response = HTTPResponseBuilder().set_status_code(200) \
                                                      .set_body(body_response) \
                                                      .set_request( \
                                                        HTTPRequestBuilder().set_method('PUT') \
                                                                            .set_resource(resource) \
                                                                            .set_body(body_request) \
                                                                            .get_element()
                                                      ).get_element()
                                                    
        assert expected_http_response == http_response

    def test_validate_http_client_put_raises_connection_exception_when_request_fails(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body: dict = {}

        https_connection_mock.return_value.getresponse.side_effect = Exception()

        with pytest.raises(HTTPConnectionException):
            self.__service.put(resource, body)


    #PATCH tests
    def test_validate_happy_path_http_client_patch_connects_to_given_host_port(self, https_connection_mock) -> None:
        self.__service.patch('DummyResource', {})

        https_connection_mock.assert_called_with(self.__context.host, self.__context.port, context=ANY)


    def test_validate_happy_path_http_client_patch_calls_request_with_expected_parameters(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body: dict = {}
        
        self.__service.patch(resource, body)

        expected_headers: dict = {
                                    'Content-type': 'application/json',
                                    'Authorization': self.__context.authorization_secret 
                                 }
        https_connection_mock.return_value.request.assert_called_with('PATCH', resource, '{}', expected_headers)

    def test_validate_happy_path_http_client_patch_returns_expected_value(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body_request: dict = {}
        body_response: dict = PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT]
        body_response_serialized: str = json.dumps(body_response) 

        https_connection_mock.return_value.getresponse.return_value.read.return_value = body_response_serialized

        http_response = self.__service.patch(resource, body_request)

        expected_http_response = HTTPResponseBuilder().set_status_code(200) \
                                                      .set_body(body_response) \
                                                      .set_request( \
                                                        HTTPRequestBuilder().set_method('PATCH') \
                                                                            .set_resource(resource) \
                                                                            .set_body(body_request) \
                                                                            .get_element()
                                                      ).get_element()
                                                    
        assert expected_http_response == http_response

    def test_validate_http_client_patch_raises_connection_exception_when_request_fails(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body: dict = {}

        https_connection_mock.return_value.getresponse.side_effect = Exception()

        with pytest.raises(HTTPConnectionException):
            self.__service.patch(resource, body)


    #POST tests
    def test_validate_happy_path_http_client_post_connects_to_given_host_port(self, https_connection_mock) -> None:
        self.__service.post('DummyResource', {})

        https_connection_mock.assert_called_with(self.__context.host, self.__context.port, context=ANY)


    def test_validate_happy_path_http_client_post_calls_request_with_expected_parameters(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body: dict = {}
        
        self.__service.post(resource, body)

        expected_headers: dict = {
                                    'Content-type': 'application/json',
                                    'Authorization': self.__context.authorization_secret 
                                 }
        https_connection_mock.return_value.request.assert_called_with('POST', resource, '{}', expected_headers)

    def test_validate_happy_path_http_client_post_returns_expected_value(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body_request: dict = {}
        body_response: dict = PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT]
        body_response_serialized: str = json.dumps(body_response) 

        https_connection_mock.return_value.getresponse.return_value.read.return_value = body_response_serialized

        http_response = self.__service.post(resource, body_request)

        expected_http_response = HTTPResponseBuilder().set_status_code(200) \
                                                      .set_body(body_response) \
                                                      .set_request( \
                                                        HTTPRequestBuilder().set_method('POST') \
                                                                            .set_resource(resource) \
                                                                            .set_body(body_request) \
                                                                            .get_element()
                                                      ).get_element()
                                                    
        assert expected_http_response == http_response

    def test_validate_http_client_post_raises_connection_exception_when_request_fails(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body: dict = {}

        https_connection_mock.return_value.getresponse.side_effect = Exception()

        with pytest.raises(HTTPConnectionException):
            self.__service.post(resource, body)

    #GET tests
    def test_validate_happy_path_http_client_get_connects_to_given_host_port(self, https_connection_mock) -> None:
        self.__service.get('DummyResource')

        https_connection_mock.assert_called_with(self.__context.host, self.__context.port, context=ANY)


    def test_validate_happy_path_http_client_get_calls_request_with_expected_parameters(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        
        self.__service.get(resource)

        expected_headers: dict = {
                                    'Content-type': 'application/json',
                                    'Authorization': self.__context.authorization_secret 
                                 }
        https_connection_mock.return_value.request.assert_called_with('GET', resource, '{}', expected_headers)

    def test_validate_happy_path_http_client_get_returns_expected_value(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body_response: dict = PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT]
        body_response_serialized: str = json.dumps(body_response) 

        https_connection_mock.return_value.getresponse.return_value.read.return_value = body_response_serialized

        http_response = self.__service.get(resource)

        expected_http_response = HTTPResponseBuilder().set_status_code(200) \
                                                      .set_body(body_response) \
                                                      .set_request( \
                                                        HTTPRequestBuilder().set_method('GET') \
                                                                            .set_resource(resource) \
                                                                            .get_element()
                                                      ).get_element()
                                                    
        assert expected_http_response == http_response

    def test_validate_http_client_get_raises_connection_exception_when_request_fails(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'

        https_connection_mock.return_value.getresponse.side_effect = Exception()

        with pytest.raises(HTTPConnectionException):
            self.__service.get(resource)

    #DELETE tests
    def test_validate_happy_path_http_client_delete_connects_to_given_host_port(self, https_connection_mock) -> None:
        self.__service.delete('DummyResource')

        https_connection_mock.assert_called_with(self.__context.host, self.__context.port, context=ANY)


    def test_validate_happy_path_http_client_delete_calls_request_with_expected_parameters(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        
        self.__service.delete(resource)

        expected_headers: dict = {
                                    'Content-type': 'application/json',
                                    'Authorization': self.__context.authorization_secret 
                                 }
        https_connection_mock.return_value.request.assert_called_with('DELETE', resource, '{}', expected_headers)

    def test_validate_happy_path_http_client_delete_returns_expected_value(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'
        body_response: dict = PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT]
        body_response_serialized: str = json.dumps(body_response) 

        https_connection_mock.return_value.getresponse.return_value.read.return_value = body_response_serialized

        http_response = self.__service.delete(resource)

        expected_http_response = HTTPResponseBuilder().set_status_code(200) \
                                                      .set_body(body_response) \
                                                      .set_request( \
                                                        HTTPRequestBuilder().set_method('DELETE') \
                                                                            .set_resource(resource) \
                                                                            .get_element()
                                                      ).get_element()
                                                    
        assert expected_http_response == http_response

    def test_validate_http_client_delete_raises_connection_exception_when_request_fails(self, https_connection_mock) -> None:
        resource: str = 'DummyResource'

        https_connection_mock.return_value.getresponse.side_effect = Exception()

        with pytest.raises(HTTPConnectionException):
            self.__service.delete(resource)