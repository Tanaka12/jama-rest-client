import pytest

from jama_rest_client.dal.parsers.json import TestGroupJSONParser as TypeTestGroupJSONParser
from jama_rest_client.model.test_plan import TestGroup as TypeTestGroup

from mocks.test_plans import TestPlansMocks as TypeTestPlansMocks, TEST_PLANS_API_MOCKS
from test_utilities.builders.test_plan import TestGroupBuilder as TypeTestGroupBuilder

class TestTestRunJSONParser():

    @pytest.mark.parametrize(
      "test_group_dict, expected_test_group",
      [
        (
            TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_TEST_GROUP_1_ELEMENT]['data'][0],
            TypeTestGroupBuilder().set_id(0)
                                  .set_name('DummyName 1')
                                  .set_assigned_to(1)
                                  .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_test_plan_returns_expected_value(self, test_group_dict: dict, expected_test_group: TypeTestGroup) -> None:
        test_run = TypeTestGroupJSONParser.parse(test_group_dict)
        assert expected_test_group == test_run