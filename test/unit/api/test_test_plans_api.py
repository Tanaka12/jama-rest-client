from datetime import datetime
from typing import List

import pytest
from unittest.mock import ANY, Mock

from jama_rest_client.api import TestPlansAPI as TypeTestPlansAPI
from jama_rest_client.model.api_response import AbstractRestResponse, CreatedResponse
from jama_rest_client.model.test_cycle import TestCycle as TypeTestCycle, TestCycleRequest as TypeTestCycleRequest
from jama_rest_client.model.test_plan import TestPlan as TypeTestPlan, TestGroup as TypeTestGroup, TestPlanRequest as TypeTestPlanRequest
from jama_rest_client.model.http import HTTPResponse

from mocks.api_responses import ApiResponsesMocks, API_RESPONSES_API_MOCKS
from mocks.test_cycles import TestCyclesMocks as TypeTestCyclesMocks, TEST_CYCLES_API_MOCKS
from mocks.test_plans import TestPlansMocks as TypeTestPlansMocks, TEST_PLANS_API_MOCKS
from test_utilities.builders.api_response import AbstractRestResponseBuilder, CreatedResponseBuilder
from test_utilities.builders.http import HTTPResponseBuilder
from test_utilities.builders.page_info import PageInfoBuilder
from test_utilities.builders.test_cycle import TestCycleBuilder as TypeTestCycleBuilder
from test_utilities.builders.test_plan import \
(
    TestPlanBuilder as TypeTestPlanBuilder,
    TestGroupBuilder as TypeTestGroupBuilder
)

class TestProjectsAPI():
    __service: TypeTestPlansAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = TypeTestPlansAPI(self.__http_client)
    
    # get_test_plans call
    def test_validate_happy_path_get_test_plans_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_project_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_test_plans(dummy_project_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/testplans?project={dummy_project_id}&startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_test_plans",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_1_ELEMENT])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                TypeTestPlanBuilder().set_id(1)
                                     .set_document_key('DummyDocumentKey 1')
                                     .set_global_id('DummyGlobalId 1')
                                     .set_item_type(2)
                                     .set_project(3)
                                     .set_created_date(datetime.fromtimestamp(1582199426))
                                     .set_modified_date(datetime.fromtimestamp(1582199426))
                                     .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                     .set_created_by(4)
                                     .set_modified_by(5)                             
                                     .set_fields(
                                        {
			                                'fieldStr': 'DummyField',
                                            'fieldInt': 0,
                                            'fieldBool': True
                                        }
                                     )   
                                     .set_archived(False)
                                     .get_element()
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_30_ELEMENTS])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                TypeTestPlanBuilder().set_id(index)
                                     .set_document_key(f'DummyDocumentKey {index}')
                                     .set_global_id(f'DummyGlobalId {index}')
                                     .set_item_type(index + 1)
                                     .set_project(index + 2)
                                     .set_created_date(datetime.fromtimestamp(1582199426))
                                     .set_modified_date(datetime.fromtimestamp(1582199426))
                                     .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                     .set_created_by(index + 3)
                                     .set_modified_by(index + 4)                             
                                     .set_fields(
                                        {
			                                'fieldStr': 'DummyField',
                                            'fieldInt': 0,
                                            'fieldBool': True
                                        }
                                     )   
                                     .set_archived(bool(index % 2))
                                     .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_30_ELEMENTS])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_1_ELEMENT])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                TypeTestPlanBuilder().set_id(index)
                                     .set_document_key(f'DummyDocumentKey {index}')
                                     .set_global_id(f'DummyGlobalId {index}')
                                     .set_item_type(index + 1)
                                     .set_project(index + 2)
                                     .set_created_date(datetime.fromtimestamp(1582199426))
                                     .set_modified_date(datetime.fromtimestamp(1582199426))
                                     .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                     .set_created_by(index + 3)
                                     .set_modified_by(index + 4)                             
                                     .set_fields(
                                        {
			                                'fieldStr': 'DummyField',
                                            'fieldInt': 0,
                                            'fieldBool': True
                                        }
                                     )   
                                     .set_archived(bool(index % 2))
                                     .get_element() for index in range(1,30)
            ] +
            [
                TypeTestPlanBuilder().set_id(1)
                                     .set_document_key('DummyDocumentKey 1')
                                     .set_global_id('DummyGlobalId 1')
                                     .set_item_type(2)
                                     .set_project(3)
                                     .set_created_date(datetime.fromtimestamp(1582199426))
                                     .set_modified_date(datetime.fromtimestamp(1582199426))
                                     .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                     .set_created_by(4)
                                     .set_modified_by(5)                             
                                     .set_fields(
                                        {
			                                'fieldStr': 'DummyField',
                                            'fieldInt': 0,
                                            'fieldBool': True
                                        }
                                     )   
                                     .set_archived(False)
                                     .get_element()
            ]
        )
      ]
    )
    def test_validate_happy_path_get_test_plans_returns_expected_value(self, http_responses: List[HTTPResponse], expected_test_plans: List[TypeTestPlan]) -> None:
        dummy_project_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        test_plans: List[TypeTestPlan] = self.__service.get_test_plans(dummy_project_id)  
        assert expected_test_plans == test_plans 


    # create_test_plan call
    def test_validate_happy_path_create_test_plan_calls_http_post_method_with_expected_resource(self) -> None:
        dummy_test_plan_request = TypeTestPlanRequest()
        self.__http_client.post.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                    .set_body(API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_CREATED_RESPONSE]) \
                                                                    .get_element()
        
        self.__service.create_test_plan(dummy_test_plan_request)    
        self.__http_client.post.assert_called_once_with(f'/rest/v1/testplans', ANY)

    @pytest.mark.parametrize(
      "http_responses, expected_created_response",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_CREATED_RESPONSE])
                                     .get_element()
            ],
            CreatedResponseBuilder().set_id(1)
                                    .set_location('/element/elementNew')
                                    .set_page_info(
                                        PageInfoBuilder().set_result_count(1)
                                                            .set_start_index(0)
                                                            .set_total_results(2)
                                                            .get_element()
                                    )
                                    .set_status(0)
                                    .set_status_reason_phrase('DummyStatusReasonPhrase')
                                    .get_element()
        )
      ]
    )
    def test_validate_happy_path_post_test_plan_cycle_returns_expected_value(self, http_responses: List[HTTPResponse], expected_created_response: CreatedResponse) -> None:
        dummy_test_plan_request = TypeTestPlanRequest()
        self.__http_client.post.side_effect = http_responses
        
        created_response = self.__service.create_test_plan_cycle(dummy_test_plan_request)  
        assert expected_created_response == created_response 


    # get_test_plan call
    def test_validate_happy_path_get_test_plan_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_test_plan_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_PLAN_SINGLE])\
                                                                   .get_element()
        
        self.__service.get_test_plan(dummy_test_plan_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/testplans/{dummy_test_plan_id}')

    @pytest.mark.parametrize(
      "http_responses, expected_test_plan",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_PLAN_SINGLE])
                                    .get_element()
            ],
            TypeTestPlanBuilder().set_id(1)
                                 .set_document_key('DummyDocumentKey 1')
                                 .set_global_id('DummyGlobalId 1')
                                 .set_item_type(2)
                                 .set_project(3)
                                 .set_created_date(datetime.fromtimestamp(1582199426))
                                 .set_modified_date(datetime.fromtimestamp(1582199426))
                                 .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                 .set_created_by(4)
                                 .set_modified_by(5)                             
                                 .set_fields(
                                 {
                                     'fieldStr': 'DummyField',
                                     'fieldInt': 0,
                                     'fieldBool': True
                                 }
                                 )   
                                 .set_archived(False)
                                 .get_element()
        )
      ]
    )
    def test_validate_happy_path_get_test_plan_returns_expected_value(self, http_responses: List[HTTPResponse], expected_test_plan: TypeTestPlan) -> None:
        dummy_test_plan_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        test_plan = self.__service.get_test_plan(dummy_test_plan_id)  
        assert expected_test_plan == test_plan 


    # update_test_plan call
    def test_validate_happy_path_update_test_plan_calls_http_put_method_with_expected_resource(self) -> None:
        dummy_test_plan_id: int = 2
        dummy_test_plan_request = TypeTestPlanRequest()
        self.__http_client.put.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_ABSTRACT_REST_RESPONSE])\
                                                                   .get_element()
        
        self.__service.update_test_plan(dummy_test_plan_id, dummy_test_plan_request)    
        self.__http_client.put.assert_called_once_with(f'/rest/v1/testplans/{dummy_test_plan_id}', ANY)

    @pytest.mark.parametrize(
      "http_responses, expected_abstract_rest_response",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_ABSTRACT_REST_RESPONSE])
                                    .get_element()
            ],
            AbstractRestResponseBuilder().set_status(0)
                                         .set_status_reason_phrase('DummyStatusReasonPhrase')
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
    def test_validate_happy_path_update_test_plan_returns_expected_value(self, http_responses: List[HTTPResponse], expected_abstract_rest_response: AbstractRestResponse) -> None:
        dummy_test_plan_id: int = 2
        dummy_test_plan_request = TypeTestPlanRequest()
        self.__http_client.put.side_effect = http_responses
        
        abstract_rest_response = self.__service.update_test_plan(dummy_test_plan_id, dummy_test_plan_request)  
        assert expected_abstract_rest_response == abstract_rest_response 


    # get_test_plan_cycles call
    def test_validate_happy_path_get_test_plan_cycles_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_test_plan_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_test_plan_cycles(dummy_test_plan_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/testplans/{dummy_test_plan_id}/testcycles?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_test_cycles",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_1_ELEMENT])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                TypeTestCycleBuilder().set_id(1)
                                      .set_document_key('DummyDocumentKey 1')
                                      .set_global_id('DummyGlobalId 1')
                                      .set_item_type(2)
                                      .set_project(3)
                                      .set_created_date(datetime.fromtimestamp(1582199426))
                                      .set_modified_date(datetime.fromtimestamp(1582199426))
                                      .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                      .set_created_by(4)
                                      .set_modified_by(5)                             
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
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_30_ELEMENTS])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                TypeTestCycleBuilder().set_id(index)
                                      .set_document_key(f'DummyDocumentKey {index}')
                                      .set_global_id(f'DummyGlobalId {index}')
                                      .set_item_type(index + 1)
                                      .set_project(index + 2)
                                      .set_created_date(datetime.fromtimestamp(1582199426))
                                      .set_modified_date(datetime.fromtimestamp(1582199426))
                                      .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                      .set_created_by(index + 3)
                                      .set_modified_by(index + 4)                             
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
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_30_ELEMENTS])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_1_ELEMENT])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                TypeTestCycleBuilder().set_id(index)
                                      .set_document_key(f'DummyDocumentKey {index}')
                                      .set_global_id(f'DummyGlobalId {index}')
                                      .set_item_type(index + 1)
                                      .set_project(index + 2)
                                      .set_created_date(datetime.fromtimestamp(1582199426))
                                      .set_modified_date(datetime.fromtimestamp(1582199426))
                                      .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                      .set_created_by(index + 3)
                                      .set_modified_by(index + 4)                             
                                      .set_fields(
                                         {
			                                 'fieldStr': 'DummyField',
                                             'fieldInt': 0,
                                             'fieldBool': True
                                         }
                                      ).get_element() for index in range(1,30)
            ] +
            [
                TypeTestCycleBuilder().set_id(1)
                                      .set_document_key('DummyDocumentKey 1')
                                      .set_global_id('DummyGlobalId 1')
                                      .set_item_type(2)
                                      .set_project(3)
                                      .set_created_date(datetime.fromtimestamp(1582199426))
                                      .set_modified_date(datetime.fromtimestamp(1582199426))
                                      .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                      .set_created_by(4)
                                      .set_modified_by(5)                             
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
    def test_validate_happy_path_get_test_plan_cycles_returns_expected_value(self, http_responses: List[HTTPResponse], expected_test_cycles: List[TypeTestCycle]) -> None:
        dummy_test_plan_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        test_cycles: List[TypeTestCycle] = self.__service.get_test_plan_cycles(dummy_test_plan_id)  
        assert expected_test_cycles == test_cycles


    # get_test_plan_groups call
    def test_validate_happy_path_get_test_plan_groups_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_test_plan_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_test_plan_groups(dummy_test_plan_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/testplans/{dummy_test_plan_id}/testgroups?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_test_groups",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                TypeTestGroupBuilder().set_id(0)
                                      .set_name('DummyName 1')
                                      .set_assigned_to(1)
                                      .get_element()
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                TypeTestGroupBuilder().set_id(index)
                                      .set_name(f'DummyName {index}')
                                      .set_assigned_to(index + 1)
                                      .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                TypeTestGroupBuilder().set_id(index)
                                      .set_name(f'DummyName {index}')
                                      .set_assigned_to(index + 1)
                                      .get_element() for index in range(1,30)
            ] +
            [
                TypeTestGroupBuilder().set_id(0)
                                      .set_name(f'DummyName 1')
                                      .set_assigned_to(1)
                                      .get_element()
            ]
        )
      ]
    )
    def test_validate_happy_path_get_test_plan_groups_returns_expected_value(self, http_responses: List[HTTPResponse], expected_test_groups: List[TypeTestGroup]) -> None:
        dummy_test_plan_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        test_groups: List[TypeTestGroup] = self.__service.get_test_plan_groups(dummy_test_plan_id)  
        assert expected_test_groups == test_groups 


    # create_test_plan_cycle call
    def test_validate_happy_path_create_test_plan_cycle_calls_http_post_method_with_expected_resource(self) -> None:
        dummy_test_plan_id: int = 2
        dummy_test_cycle_request = TypeTestCycleRequest()
        self.__http_client.post.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                    .set_body(API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_CREATED_RESPONSE]) \
                                                                    .get_element()
        
        self.__service.create_test_plan_cycle(dummy_test_plan_id, dummy_test_cycle_request)    
        self.__http_client.post.assert_called_once_with(f'/rest/v1/testplans/{dummy_test_plan_id}/testcycles', ANY)

    @pytest.mark.parametrize(
      "http_responses, expected_created_response",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(API_RESPONSES_API_MOCKS[ApiResponsesMocks.CASE_CREATED_RESPONSE])
                                     .get_element()
            ],
            CreatedResponseBuilder().set_id(1)
                                    .set_location('/element/elementNew')
                                    .set_page_info(
                                        PageInfoBuilder().set_result_count(1)
                                                            .set_start_index(0)
                                                            .set_total_results(2)
                                                            .get_element()
                                    )
                                    .set_status(0)
                                    .set_status_reason_phrase('DummyStatusReasonPhrase')
                                    .get_element()
        )
      ]
    )
    def test_validate_happy_path_post_test_plan_cycle_returns_expected_value(self, http_responses: List[HTTPResponse], expected_created_response: CreatedResponse) -> None:
        dummy_test_plan_id: int = 2
        dummy_test_cycle_request = TypeTestCycleRequest()
        self.__http_client.post.side_effect = http_responses
        
        created_response = self.__service.create_test_plan_cycle(dummy_test_plan_id, dummy_test_cycle_request)  
        assert expected_created_response == created_response 