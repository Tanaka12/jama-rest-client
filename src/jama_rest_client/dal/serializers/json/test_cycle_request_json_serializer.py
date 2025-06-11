from jama_rest_client.model.test_cycle import TestCycleRequest
from jama_rest_client.model.test_cycle import TestRunGenerationConfig

class TestCycleRequestJSONSerializer:

    @staticmethod
    def serialize(test_cycle_request: TestCycleRequest) -> dict:
        test_cycle_request_dict: dict = {}
        test_cycle_request_dict['testRunGenerationConfig'] = TestCycleRequestJSONSerializer.__serialize_test_run_generation_config(test_cycle_request.test_run_generation_config)
        test_cycle_request_dict['fields'] = test_cycle_request.fields

        return test_cycle_request_dict
    
    @staticmethod
    def __serialize_test_run_generation_config(test_run_generation_config: TestRunGenerationConfig) -> dict:
        test_run_generation_config_dict: dict = {}

        test_run_generation_config_dict['testGroupsToInclude'] = test_run_generation_config.test_groups_to_include
        test_run_generation_config_dict['testRunStatusesToInclude'] = [ run_status.value for run_status in test_run_generation_config.test_run_statuses_to_include ]

        return test_run_generation_config_dict