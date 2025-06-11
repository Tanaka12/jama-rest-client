from jama_rest_client.model.page_info import PageInfo
from typing_extensions import Self

class PageInfoBuilder:
    __page_info: PageInfo

    def __init__(self):
        self.__page_info = PageInfo()

    def set_start_index(self, start_index: int) -> Self:
        self.__page_info.start_index = start_index
        return self
    
    def set_result_count(self, result_count: int) -> Self:
        self.__page_info.result_count = result_count
        return self
    
    def set_total_results(self, total_results: int) -> Self:
        self.__page_info.total_results = total_results
        return self

    def get_element(self) -> PageInfo:
        return self.__page_info
    