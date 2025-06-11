from datetime import datetime
from typing import List

import pytest
from unittest.mock import Mock

from jama_rest_client.api import TestRunsAPI as TypeTestRunsAPI
from jama_rest_client.model.test_run import TestRun as TypeTestRun
from jama_rest_client.model.http import HTTPResponse

from mocks.test_runs import TestRunsMocks as TypeTestRunsMocks, TEST_RUNS_API_MOCKS
from test_utilities.builders.http import HTTPResponseBuilder
from test_utilities.builders.test_run import TestRunBuilder as TypeTestRunBuilder

class TestRunsAPI():
    __service: TypeTestRunsAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = TypeTestRunsAPI(self.__http_client)
    
    # get_test_runs call
    def test_validate_happy_path_get_test_runs_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_test_cycle_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_test_runs(dummy_test_cycle_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/testruns?testCycle={dummy_test_cycle_id}&startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_test_runs",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                TypeTestRunBuilder().set_id(1)
                                    .set_document_key('DummyDocumentKey 1')
                                    .set_global_id('DummyGlobalId 1')
                                    .set_item_type(2)
                                    .set_project(3)
                                    .set_created_date(datetime.fromtimestamp(1582199426))
                                    .set_modified_date(datetime.fromtimestamp(1582199426))
                                    .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                    .set_created_by(4)
                                    .set_modified_by(5)                             
                                    .set_test_case_version_number(6)                             
                                    .set_test_case_current_version_number(7)                             
                                    .set_sort_order_from_test_group(8)           
                                    .set_test_group([ 1, 2 ])                  
                                    .set_fields(
                                       {
			                               'fieldStr': 'DummyField',
                                           'fieldInt': 0,
                                           'fieldBool': True
                                       }
                                    ).get_element()
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                TypeTestRunBuilder().set_id(index)
                                    .set_document_key(f'DummyDocumentKey {index}')
                                    .set_global_id(f'DummyGlobalId {index}')
                                    .set_item_type(index + 1)
                                    .set_project(index + 2)
                                    .set_created_date(datetime.fromtimestamp(1582199426))
                                    .set_modified_date(datetime.fromtimestamp(1582199426))
                                    .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                    .set_created_by(index + 3)
                                    .set_modified_by(index + 4)                             
                                    .set_test_case_version_number(index + 5)                             
                                    .set_test_case_current_version_number(index + 6)                             
                                    .set_sort_order_from_test_group(index + 7)    
                                    .set_test_group([ 1, 2 ])                         
                                    .set_fields(
                                       {
			                               'fieldStr': 'DummyField',
                                           'fieldInt': 0,
                                           'fieldBool': True
                                       }
                                    ).get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                TypeTestRunBuilder().set_id(index)
                                    .set_document_key(f'DummyDocumentKey {index}')
                                    .set_global_id(f'DummyGlobalId {index}')
                                    .set_item_type(index + 1)
                                    .set_project(index + 2)
                                    .set_created_date(datetime.fromtimestamp(1582199426))
                                    .set_modified_date(datetime.fromtimestamp(1582199426))
                                    .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                    .set_created_by(index + 3)
                                    .set_modified_by(index + 4)                             
                                    .set_test_case_version_number(index + 5)                             
                                    .set_test_case_current_version_number(index + 6)                             
                                    .set_sort_order_from_test_group(index + 7)   
                                    .set_test_group([ 1, 2 ])                          
                                    .set_fields(
                                       {
			                               'fieldStr': 'DummyField',
                                           'fieldInt': 0,
                                           'fieldBool': True
                                       }
                                    ).get_element() for index in range(1,30)
            ] +
            [
                TypeTestRunBuilder().set_id(1)
                                    .set_document_key('DummyDocumentKey 1')
                                    .set_global_id('DummyGlobalId 1')
                                    .set_item_type(2)
                                    .set_project(3)
                                    .set_created_date(datetime.fromtimestamp(1582199426))
                                    .set_modified_date(datetime.fromtimestamp(1582199426))
                                    .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                    .set_created_by(4)
                                    .set_modified_by(5)                             
                                    .set_test_case_version_number(6)                             
                                    .set_test_case_current_version_number(7)                             
                                    .set_sort_order_from_test_group(8)
                                    .set_test_group([ 1, 2 ])                             
                                    .set_fields(
                                       {
			                               'fieldStr': 'DummyField',
                                           'fieldInt': 0,
                                           'fieldBool': True
                                       }
                                    ).get_element()
            ]
        )
      ]
    )
    def test_validate_happy_path_get_test_runs_returns_expected_value(self, http_responses: List[HTTPResponse], expected_test_runs: List[TypeTestRun]) -> None:
        dummy_test_cycle_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        test_runs: List[TypeTestRun] = self.__service.get_test_runs(dummy_test_cycle_id)  
        assert expected_test_runs == test_runs 