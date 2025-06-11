from datetime import datetime
import pytest

from jama_rest_client.dal.parsers.json import TestCycleJSONParser as TypeTestCycleJSONParser
from jama_rest_client.model.test_cycle import TestCycle as TypeTestCycle

from mocks.test_cycles import TestCyclesMocks as TypeTestCyclesMocks, TEST_CYCLES_API_MOCKS
from test_utilities.builders.test_cycle import TestCycleBuilder as TypeTestCycleBuilder

class TestTestCycleJSONParser():

    @pytest.mark.parametrize(
      "test_cycle_dict, expected_test_cycle",
      [
        (
            TEST_CYCLES_API_MOCKS[TypeTestCyclesMocks.CASE_1_ELEMENT]['data'][0],
            TypeTestCycleBuilder().set_id(1)
                                 .set_document_key('DummyDocumentKey 1')
                                 .set_global_id('DummyGlobalId 1')
                                 .set_item_type(2)
                                 .set_project(3)
                                 .set_created_date(datetime.fromtimestamp(1582199426))
                                 .set_modified_date(datetime.fromtimestamp(1582199426))
                                 .set_last_activity_date(datetime.fromtimestamp(1582199426))
                                 .set_created_by(4)
                                 .set_modified_by(5)                             
                                 .set_fields(
                                    {
			                            'fieldStr': 'DummyField',
                                        'fieldInt': 0,
                                        'fieldBool': True
                                    }
                                 )   
                                 .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_test_cycle_returns_expected_value(self, test_cycle_dict: dict, expected_test_cycle: TypeTestCycle) -> None:
        test_cycle = TypeTestCycleJSONParser.parse(test_cycle_dict)
        assert expected_test_cycle == test_cycle