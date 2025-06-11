from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.dal.parsers.json import \
(
    AbstractRestResponseJSONParser,
    CreatedResponseJSONParser, 
    TestCycleJSONParser, 
    TestGroupJSONParser, 
    TestPlanJSONParser
)
from jama_rest_client.dal.serializers.json import PatchOperationRequestJSONSerializer, TestCycleRequestJSONSerializer, TestPlanRequestJSONSerializer
from jama_rest_client.model.api_response import AbstractRestResponse, CreatedResponse
from jama_rest_client.model.request import PatchOperationRequest
from jama_rest_client.model.test_cycle import TestCycle, TestCycleRequest
from jama_rest_client.model.test_plan import TestGroup, TestPlan, TestPlanRequest

from .base_api import BaseAPI

class TestPlansAPI(BaseAPI):
    __resourceName: str = '/rest/v1/testplans'

    def __init__(self, http_client: HTTPClient):
        super().__init__(http_client)
        
    def get_test_plans(self, project_id: int) -> List[TestPlan]:
        test_plans: List[TestPlan] = []

        start_index: int = 0
        while True:
            test_plans_batch = self.__parse_test_plans_dict(self._get(f'{self.__resourceName}?project={project_id}&startAt={start_index}&maxResults=50').body['data'])
            
            if len(test_plans_batch) == 0:
                break

            test_plans.extend(test_plans_batch)
            start_index += len(test_plans_batch)

        return test_plans
    
    def create_test_plan(self, test_plan_request: TestPlanRequest) -> CreatedResponse:
        http_response = self._post(self.__resourceName, TestPlanRequestJSONSerializer.serialize(test_plan_request))
        return CreatedResponseJSONParser.parse(http_response.body)

    def get_test_plan(self, test_plan_id: int) -> TestPlan:
        test_plan_dict = self._get(f'{self.__resourceName}/{test_plan_id}').body['data']
        return TestPlanJSONParser.parse(test_plan_dict)
    
    def update_test_plan(self, test_plan_id: int, test_plan_request: TestPlanRequest) -> AbstractRestResponse:
        http_response = self._put(f'{self.__resourceName}/{test_plan_id}', TestPlanRequestJSONSerializer.serialize(test_plan_request))
        return AbstractRestResponseJSONParser.parse(http_response.body)

    def patch_test_plan(self, test_plan_id: int, patch_operation_request: PatchOperationRequest) -> AbstractRestResponse:
        http_response = self._patch(f'{self.__resourceName}/{test_plan_id}', PatchOperationRequestJSONSerializer.serialize(patch_operation_request))
        return AbstractRestResponseJSONParser.parse(http_response.body)

    def delete_test_plan(self, test_plan_id: int) -> AbstractRestResponse:
        http_response = self._delete(f'{self.__resourceName}/{test_plan_id}')
        return AbstractRestResponseJSONParser.parse(http_response.body)

    def get_test_plan_cycles(self, test_plan_id: int) -> List[TestCycle]:
        test_cycles: List[TestCycle] = []

        start_index: int = 0
        while True:
            test_cycles_batch = self.__parse_test_cycles_dict(self._get(f'{self.__resourceName}/{test_plan_id}/testcycles?startAt={start_index}&maxResults=50').body['data'])
            
            if len(test_cycles_batch) == 0:
                break

            test_cycles.extend(test_cycles_batch)
            start_index += len(test_cycles_batch)

        return test_cycles

    def create_test_plan_cycle(self, test_plan_id: int, test_cycle_request: TestCycleRequest) -> CreatedResponse:
        http_response = self._post(f'{self.__resourceName}/{test_plan_id}/testcycles', TestCycleRequestJSONSerializer.serialize(test_cycle_request))
        return CreatedResponseJSONParser.parse(http_response.body)

    def get_test_plan_groups(self, test_plan_id: int) -> List[TestGroup]:
        test_groups: List[TestGroup] = []

        start_index: int = 0
        while True:
            test_groups_batch = self.__parse_test_groups_dict(self._get(f'{self.__resourceName}/{test_plan_id}/testgroups?startAt={start_index}&maxResults=50').body['data'])
            
            if len(test_groups_batch) == 0:
                break

            test_groups.extend(test_groups_batch)
            start_index += len(test_groups_batch)

        return test_groups

    def __parse_test_plans_dict(self, test_plans_list_dict: List[dict]) -> List[TestPlan]:
        return list(map(lambda test_plan_dict: TestPlanJSONParser.parse(test_plan_dict), test_plans_list_dict))

    def __parse_test_cycles_dict(self, test_cycles_list_dict: List[dict]) -> List[TestCycle]:
        return list(map(lambda test_cycle_dict: TestCycleJSONParser.parse(test_cycle_dict), test_cycles_list_dict))
    
    def __parse_test_groups_dict(self, test_groups_list_dict: List[dict]) -> List[TestGroup]:
        return list(map(lambda test_group_dict: TestGroupJSONParser.parse(test_group_dict), test_groups_list_dict))