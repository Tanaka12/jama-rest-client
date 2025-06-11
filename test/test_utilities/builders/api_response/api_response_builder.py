from jama_rest_client.model.api_response import AbstractRestResponse, CreatedResponse
from jama_rest_client.model.page_info import PageInfo
from typing_extensions import Self

class AbstractRestResponseBuilder:
    __abstract_rest_response: AbstractRestResponse

    def __init__(self):
        self.__abstract_rest_response = AbstractRestResponse()

    def set_status(self, status: int) -> Self:
        self.__abstract_rest_response.status = status
        return self
    
    def set_status_reason_phrase(self, status_reason_phrase: str) -> Self:
        self.__abstract_rest_response.status_reason_phrase = status_reason_phrase
        return self
    
    def set_page_info(self, page_info: PageInfo) -> Self:
        self.__abstract_rest_response.page_info = page_info
        return self

    def get_element(self) -> AbstractRestResponse:
        return self.__abstract_rest_response
    
class CreatedResponseBuilder:
    __created_response: CreatedResponse

    def __init__(self):
        self.__created_response = CreatedResponse()

    def set_status(self, status: int) -> Self:
        self.__created_response.status = status
        return self
    
    def set_status_reason_phrase(self, status_reason_phrase: str) -> Self:
        self.__created_response.status_reason_phrase = status_reason_phrase
        return self
    
    def set_page_info(self, page_info: PageInfo) -> Self:
        self.__created_response.page_info = page_info
        return self
    
    def set_location(self, location: str) -> Self:
        self.__created_response.location = location
        return self
    
    def set_id(self, id: int) -> Self:
        self.__created_response.id = id
        return self

    def get_element(self) -> CreatedResponse:
        return self.__created_response