import pytest

from jama_rest_client.dal.parsers.json import AbstractRestResponseJSONParser, CreatedResponseJSONParser
from jama_rest_client.model.api_response import AbstractRestResponse, CreatedResponse

from mocks.api_responses import ApiResponsesMocks, API_RESPONSES_API_MOCKS
from test_utilities.builders.api_response import AbstractRestResponseBuilder, CreatedResponseBuilder
from test_utilities.builders.page_info import PageInfoBuilder

class TestAbstractRestResponseJSONParser():

    @pytest.mark.parametrize(
      "abstract_rest_response_dict, expected_abstract_rest_response",
      [
        (
            API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_ABSTRACT_REST_RESPONSE],
            AbstractRestResponseBuilder().set_status(0)
                                         .set_status_reason_phrase("DummyStatusReasonPhrase")
                                         .set_page_info(
                                             PageInfoBuilder().set_start_index(0)
                                                              .set_result_count(1)
                                                              .set_total_results(2)
                                                              .get_element()
                                         )
                                         .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_abstract_rest_response_returns_expected_value(self, abstract_rest_response_dict: dict, expected_abstract_rest_response: AbstractRestResponse) -> None:
        abstract_rest_response = AbstractRestResponseJSONParser.parse(abstract_rest_response_dict)
        assert expected_abstract_rest_response == abstract_rest_response

class TestCreatedResponseJSONParser():

    @pytest.mark.parametrize(
      "created_response_dict, expected_created_response",
      [
        (
            API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_CREATED_RESPONSE],
            CreatedResponseBuilder().set_status(0)
                                    .set_status_reason_phrase("DummyStatusReasonPhrase")
                                    .set_page_info(
                                        PageInfoBuilder().set_start_index(0)
                                                         .set_result_count(1)
                                                         .set_total_results(2)
                                                         .get_element()
                                    )
                                    .set_location("/element/elementNew")
                                    .set_id(1)
                                    .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_created_response_returns_expected_value(self, created_response_dict: dict, expected_created_response: CreatedResponse) -> None:
        created_response = CreatedResponseJSONParser.parse(created_response_dict)
        assert expected_created_response == created_response