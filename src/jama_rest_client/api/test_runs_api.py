from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.dal.parsers.json import TestRunJSONParser
from jama_rest_client.model.test_run import TestRun

from .base_api import BaseAPI

class TestRunsAPI(BaseAPI):
    __resourceName: str = '/rest/v1/testruns'

    def __init__(self, http_client: HTTPClient):
        super().__init__(http_client)
        
    def get_test_runs(self, test_cycle_id: int) -> List[TestRun]:
        test_runs: List[TestRun] = []

        start_index: int = 0
        while True:
            test_runs_batch = self.__parse_test_runs_dict(self._get(f'{self.__resourceName}?testCycle={test_cycle_id}&startAt={start_index}&maxResults=50').body['data'])
            
            if len(test_runs_batch) == 0:
                break

            test_runs.extend(test_runs_batch)
            start_index += len(test_runs_batch)

        return test_runs
    
    def __parse_test_runs_dict(self, test_runs_list_dict: List[dict]) -> List[TestRun]:
        return list(map(lambda test_run_dict: TestRunJSONParser.parse(test_run_dict), test_runs_list_dict))