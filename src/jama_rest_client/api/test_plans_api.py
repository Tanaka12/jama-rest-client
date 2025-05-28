from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.dal.parsers.json import TestPlanJSONParser
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
    
    def __parse_test_plans_dict(self, test_plans_list_dict: List[dict]) -> List[TestPlan]:
        return list(map(lambda test_plan_dict: TestPlanJSONParser.parse(test_plan_dict), test_plans_list_dict))