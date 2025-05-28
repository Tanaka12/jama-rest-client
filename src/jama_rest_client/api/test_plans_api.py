from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.dal.parsers.json import TestCycleJSONParser, TestPlanJSONParser
from jama_rest_client.model.test_cycle import TestCycle
from jama_rest_client.model.test_plan import TestPlan

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
    
    def get_test_plan_cycles(self, test_plan_id: int) -> List[TestCycle]:
        test_cycles: List[TestCycle] = []

        start_index: int = 0
        while True:
            test_cycles_batch = self.__parse_test_cycles_dict(self._get(f'{self.__resourceName}/{test_plan_id}/cycles?startAt={start_index}&maxResults=50').body['data'])
            
            if len(test_cycles_batch) == 0:
                break

            test_cycles.extend(test_cycles_batch)
            start_index += len(test_cycles_batch)

        return test_cycles

    def __parse_test_plans_dict(self, test_plans_list_dict: List[dict]) -> List[TestPlan]:
        return list(map(lambda test_plan_dict: TestPlanJSONParser.parse(test_plan_dict), test_plans_list_dict))

    def __parse_test_cycles_dict(self, test_cycles_list_dict: List[dict]) -> List[TestCycle]:
        return list(map(lambda test_cycle_dict: TestCycleJSONParser.parse(test_cycle_dict), test_cycles_list_dict))