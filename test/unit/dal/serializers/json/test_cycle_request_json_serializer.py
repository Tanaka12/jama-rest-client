import pytest

from jama_rest_client.dal.serializers.json import TestCycleRequestJSONSerializer as TypeTestCycleRequestJSONSerializer
from jama_rest_client.model.test_cycle import TestCycleRequest as TypeTestCycleRequest, TestRunStatus as TypeTestRunStatus

from mocks.test_cycles import TestCyclesMocks as TypeTestCyclesMocks, TEST_CYCLES_API_MOCKS
from test_utilities.builders.test_cycle import TestCycleRequestBuilder as TypeTestCycleRequestBuilder, TestRunGenerationConfigBuilder as TypeTestRunGenerationConfigBuilder

class TestTestCycleRequestJSONSerializer():

    @pytest.mark.parametrize(
      "test_cycle_request, expected_test_cycle_request_dict",
      [
        (
            TypeTestCycleRequestBuilder().set_fields(
                                          {
                                              "fieldStr": "DummyField",
                                              "fieldInt": 0,
                                              "fieldBool": True
                                          }
                                         )
                                         .set_test_run_generation_config(
                                             TypeTestRunGenerationConfigBuilder().set_test_groups_to_include([ 1, 2, 3 ])
                                                                                 .set_test_run_statuses_to_include(
                                                                                     [
                                                                                        TypeTestRunStatus.PASSED,
                                                                                        TypeTestRunStatus.NOT_RUN,
                                                                                        TypeTestRunStatus.IN_PROGRESS,
                                                                                        TypeTestRunStatus.FAILED,
                                                                                        TypeTestRunStatus.BLOCKED
                                                                                     ]
                                                                                 )
                                                                                 .get_element()
                                         )
                                         .get_element(),
            TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_REQUEST]
        )
      ]
    )
    def test_validate_happy_path_serialize_test_cycle_request_returns_expected_value(self, test_cycle_request: TypeTestCycleRequest, expected_test_cycle_request_dict: dict) -> None:
        test_cycle_request_dict = TypeTestCycleRequestJSONSerializer.serialize(test_cycle_request)
        assert expected_test_cycle_request_dict == test_cycle_request_dict