from jama_rest_client.model.test_cycle import TestCycleRequest, TestRunGenerationConfig, TestRunStatus
from typing import List
from typing_extensions import Self

class TestRunGenerationConfigBuilder:
    __test_run_generation_config: TestRunGenerationConfig

    def __init__(self):
        self.__test_run_generation_config = TestRunGenerationConfig()

    def set_test_groups_to_include(self, test_groups_to_include: List[int]) -> Self:
        self.__test_run_generation_config.test_groups_to_include = test_groups_to_include
        return self
    
    def set_test_run_statuses_to_include(self, test_run_statuses_to_include: List[TestRunStatus]) -> Self:
        self.__test_run_generation_config.test_run_statuses_to_include = test_run_statuses_to_include
        return self
    
    def get_element(self) -> TestRunGenerationConfig:
        return self.__test_run_generation_config

class TestCycleRequestBuilder:
    __test_cycle_request: TestCycleRequest

    def __init__(self):
        self.__test_cycle_request = TestCycleRequest()

    def set_test_run_generation_config(self, test_run_generation_config: TestRunGenerationConfig) -> Self:
        self.__test_cycle_request.test_run_generation_config = test_run_generation_config
        return self
    
    def set_fields(self, fields: dict) -> Self:
        self.__test_cycle_request.fields = fields
        return self
    
    def get_element(self) -> TestCycleRequest:
        return self.__test_cycle_request