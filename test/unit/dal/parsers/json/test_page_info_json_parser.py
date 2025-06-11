import pytest

from jama_rest_client.dal.parsers.json import PageInfoJSONParser
from jama_rest_client.model.page_info import PageInfo

from mocks.page_info import PageInfoMocks, PAGE_INFO_API_MOCKS
from test_utilities.builders.page_info import PageInfoBuilder

class TestPageInfoJSONParser():

    @pytest.mark.parametrize(
      "page_info_dict, expected_page_info",
      [
        (
            PAGE_INFO_API_MOCKS[PageInfoMocks.CASE_PAGE_INFO],
            PageInfoBuilder().set_start_index(0)
                             .set_result_count(1)
                             .set_total_results(2)
                             .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_page_info_returns_expected_value(self, page_info_dict: dict, expected_page_info: PageInfo) -> None:
        page_info = PageInfoJSONParser.parse(page_info_dict)
        assert expected_page_info == page_info