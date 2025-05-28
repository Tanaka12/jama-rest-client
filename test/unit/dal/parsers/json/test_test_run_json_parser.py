import pytest

from jama_rest_client.dal.parsers.json import TestRunJSONParser as TypeTestRunJSONParser
from jama_rest_client.model.test_run import TestRun as TypeTestRun

from mocks.test_runs import TestRunsMocks as TypeTestRunsMocks, TEST_RUNS_API_MOCKS
from test_utilities.builders.test_run import TestRunBuilder as TypeTestRunBuilder

class TestTestRunJSONParser():

    @pytest.mark.parametrize(
      "test_run_dict, expected_test_run",
      [
        (
            TEST_RUNS_API_MOCKS[TypeTestRunsMocks.CASE_1_ELEMENT]['data'][0],
            TypeTestRunBuilder().set_id(1)
                                .set_document_key('DummyDocumentKey 1')
                                .set_global_id('DummyGlobalId 1')
                                .set_item_type(2)
                                .set_project(3)
                                .set_created_date('DummyCreatedDate 1')
                                .set_modified_date('DummyModifiedDate 1')
                                .set_last_activity_date('DummyLastActivityDate 1')
                                .set_created_by(4)
                                .set_modified_by(5)                             
                                .set_test_case_version_number(6)                             
                                .set_test_case_current_version_number(7)                             
                                .set_sort_order_from_test_group(8)                             
                                .set_fields(
                                   {
			                           'fieldStr': 'DummyField',
                                       'fieldInt': 0,
                                       'fieldBool': True
                                   }
                                ).get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_test_plan_returns_expected_value(self, test_run_dict: dict, expected_test_run: TypeTestRun) -> None:
        test_run = TypeTestRunJSONParser.parse(test_run_dict)
        assert expected_test_run == test_run