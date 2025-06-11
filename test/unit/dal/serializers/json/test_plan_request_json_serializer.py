import pytest

from jama_rest_client.dal.serializers.json import TestPlanRequestJSONSerializer as TypeTestPlanRequestJSONSerializer
from jama_rest_client.model.test_plan import TestPlanRequest as TypeTestPlanRequest

from mocks.test_plans import TestPlansMocks as TypeTestPlansMocks, TEST_PLANS_API_MOCKS
from test_utilities.builders.test_plan import TestPlanRequestBuilder as TypeTestPlanRequestBuilder

class TestTestPlanJSONParser():

    @pytest.mark.parametrize(
      "test_plan_request, expected_test_plan_request_dict",
      [
        (
            TypeTestPlanRequestBuilder().set_fields(
                                          {
                                              "fieldStr": "DummyField",
                                              "fieldInt": 0,
                                              "fieldBool": True
                                          }
                                         )
                                         .set_project(0)
                                         .get_element(),
            TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_PLAN_REQUEST]
        )
      ]
    )
    def test_validate_happy_path_serialize_test_cycle_request_returns_expected_value(self, test_plan_request: TypeTestPlanRequest, expected_test_plan_request_dict: dict) -> None:
        test_plan_request_dict = TypeTestPlanRequestJSONSerializer.serialize(test_plan_request)
        assert expected_test_plan_request_dict == test_plan_request_dict