import pytest

from jama_rest_client.dal.parsers.json import TestPlanJSONParser as TypeTestPlanJSONParser
from jama_rest_client.model.test_plan import TestPlan as TypeTestPlan

from mocks.test_plans import TestPlansMocks as TypeTestPlansMocks, TEST_PLANS_API_MOCKS
from test_utilities.builders.test_plan import TestPlanBuilder as TypeTestPlanBuilder

class TestTestPlanJSONParser():

    @pytest.mark.parametrize(
      "test_plan_dict, expected_test_plan",
      [
        (
            TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_1_ELEMENT]['data'][0],
            TypeTestPlanBuilder().set_id(1)
                                 .set_document_key('DummyDocumentKey 1')
                                 .set_global_id('DummyGlobalId 1')
                                 .set_item_type(2)
                                 .set_project(3)
                                 .set_created_date('DummyCreatedDate 1')
                                 .set_modified_date('DummyModifiedDate 1')
                                 .set_last_activity_date('DummyLastActivityDate 1')
                                 .set_created_by(4)
                                 .set_modified_by(5)                             
                                 .set_fields(
                                    {
			                            'fieldStr': 'DummyField',
                                        'fieldInt': 0,
                                        'fieldBool': True
                                    }
                                 )   
                                 .set_archived(False)
                                 .get_element()
        ),
        (
            TEST_PLANS_API_MOCKS[TypeTestPlansMocks.CASE_1_ELEMENT_ARCHIVED]['data'][0],
            TypeTestPlanBuilder().set_id(1)
                             .set_document_key('DummyDocumentKey 1')
                             .set_global_id('DummyGlobalId 1')
                             .set_item_type(2)
                             .set_project(3)
                             .set_created_date('DummyCreatedDate 1')
                             .set_modified_date('DummyModifiedDate 1')
                             .set_last_activity_date('DummyLastActivityDate 1')
                             .set_created_by(4)
                             .set_modified_by(5)                             
                             .set_fields(
                                {
			                        'fieldStr': 'DummyField',
                                    'fieldInt': 0,
                                    'fieldBool': True
                                }
                             )
                             .set_archived(True)
                             .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_test_plan_returns_expected_value(self, test_plan_dict: dict, expected_test_plan: TypeTestPlan) -> None:
        test_plan = TypeTestPlanJSONParser.parse(test_plan_dict)
        assert expected_test_plan == test_plan