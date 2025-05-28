import pytest
from unittest.mock import Mock

from jama_rest_client.api.base_api import BaseAPI
from jama_rest_client.api.base_api import (
    APIElementNotFoundException, 
    APIUnauthorizedException, 
    APIUnknownException
)

from test_utilities.builders.http import HTTPResponseBuilder

class TestProjectsAPI():
    __service: BaseAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = BaseAPI(self.__http_client)

    def test_validate_happy_path_put_calls_http_client_with_expected_values(self) -> None:
        dummy_resource: str = 'dummyResource'
        dummy_body: dict = { 'element1': 'value', 'element2': 2}
        self.__http_client.put.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .get_element()
        
        self.__service._put(dummy_resource, dummy_body)
        self.__http_client.put.assert_called_once_with(dummy_resource, dummy_body)

    @pytest.mark.parametrize(
      "status_code, exception_type",
      [
          (404, APIElementNotFoundException),
          (401, APIUnauthorizedException),
          (500, APIUnknownException)
      ]
    )
    def test_validate_put_returns_exception_when_status_code(self, status_code: int, exception_type: Exception) -> None:
        dummy_resource: str = 'dummyResource'
        dummy_body: dict = { 'element1': 'value', 'element2': 2}
        self.__http_client.put.return_value = HTTPResponseBuilder().set_status_code(status_code) \
                                                                   .get_element()

        with pytest.raises(exception_type):
          self.__service._put(dummy_resource, dummy_body)

        
    def test_validate_happy_path_patch_calls_http_client_with_expected_values(self) -> None:
        dummy_resource: str = 'dummyResource'
        dummy_body: dict = { 'element1': 'value', 'element2': 2}
        self.__http_client.patch.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                     .get_element()
        
        self.__service._patch(dummy_resource, dummy_body)
        self.__http_client.patch.assert_called_once_with(dummy_resource, dummy_body)

    @pytest.mark.parametrize(
      "status_code, exception_type",
      [
          (404, APIElementNotFoundException),
          (401, APIUnauthorizedException),
          (500, APIUnknownException)
      ]
    )
    def test_validate_patch_returns_exception_when_status_code(self, status_code: int, exception_type: Exception) -> None:
        dummy_resource: str = 'dummyResource'
        dummy_body: dict = { 'element1': 'value', 'element2': 2}
        self.__http_client.patch.return_value = HTTPResponseBuilder().set_status_code(status_code) \
                                                                     .get_element()

        with pytest.raises(exception_type):
          self.__service._patch(dummy_resource, dummy_body)


    def test_validate_happy_path_post_calls_http_client_with_expected_values(self) -> None:
        dummy_resource: str = 'dummyResource'
        dummy_body: dict = { 'element1': 'value', 'element2': 2}
        self.__http_client.post.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                    .get_element()
        
        self.__service._post(dummy_resource, dummy_body)
        self.__http_client.post.assert_called_once_with(dummy_resource, dummy_body)

    @pytest.mark.parametrize(
      "status_code, exception_type",
      [
          (404, APIElementNotFoundException),
          (401, APIUnauthorizedException),
          (500, APIUnknownException)
      ]
    )
    def test_validate_post_returns_exception_when_status_code(self, status_code: int, exception_type: Exception) -> None:
        dummy_resource: str = 'dummyResource'
        dummy_body: dict = { 'element1': 'value', 'element2': 2}
        self.__http_client.post.return_value = HTTPResponseBuilder().set_status_code(status_code) \
                                                                    .get_element()

        with pytest.raises(exception_type):
          self.__service._post(dummy_resource, dummy_body)


    def test_validate_happy_path_get_calls_http_client_with_expected_values(self) -> None:
        dummy_resource: str = 'dummyResource'
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .get_element()
        
        self.__service._get(dummy_resource)
        self.__http_client.get.assert_called_once_with(dummy_resource)

    @pytest.mark.parametrize(
      "status_code, exception_type",
      [
          (404, APIElementNotFoundException),
          (401, APIUnauthorizedException),
          (500, APIUnknownException)
      ]
    )
    def test_validate_get_returns_exception_when_status_code(self, status_code: int, exception_type: Exception) -> None:
        dummy_resource: str = 'dummyResource'
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(status_code) \
                                                                   .get_element()

        with pytest.raises(exception_type):
          self.__service._get(dummy_resource)


    def test_validate_happy_path_delete_calls_http_client_with_expected_values(self) -> None:
        dummy_resource: str = 'dummyResource'
        self.__http_client.delete.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                      .get_element()
        
        self.__service._delete(dummy_resource)
        self.__http_client.delete.assert_called_once_with(dummy_resource)

    @pytest.mark.parametrize(
      "status_code, exception_type",
      [
          (404, APIElementNotFoundException),
          (401, APIUnauthorizedException),
          (500, APIUnknownException)
      ]
    )
    def test_validate_delete_returns_exception_when_status_code(self, status_code: int, exception_type: Exception) -> None:
        dummy_resource: str = 'dummyResource'
        self.__http_client.delete.return_value = HTTPResponseBuilder().set_status_code(status_code) \
                                                                      .get_element()

        with pytest.raises(exception_type):
          self.__service._delete(dummy_resource)