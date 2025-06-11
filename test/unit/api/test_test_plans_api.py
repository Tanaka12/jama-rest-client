from datetime import datetime
from typing import List

import pytest
from unittest.mock import Mock

from jama_rest_client.api import TestPlansAPI as TypeTestPlansAPI
from jama_rest_client.model.test_cycle import TestCycle as TypeTestCycle
from jama_rest_client.model.test_plan import TestPlan as TypeTestPlan
from jama_rest_client.model.http import HTTPResponse

from mocks.test_cycles import TestCyclesMocks as TypeTestCyclesMocks, TEST_CYCLES_API_MOCKS
from mocks.test_plans import TestPlansMocks as TypeTestPlansMocks, TEST_PLANS_API_MOCKS
from test_utilities.builders.http import HTTPResponseBuilder
from test_utilities.builders.test_cycle import TestCycleBuilder as TypeTestCycleBuilder
from test_utilities.builders.test_plan import TestPlanBuilder as TypeTestPlanBuilder

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