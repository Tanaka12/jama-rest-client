from datetime import datetime
import pytest

from jama_rest_client.dal.parsers.json import LocationJSONParser
from jama_rest_client.model.location import Location

from mocks.locations import LocationsMocks, LOCATIONS_API_MOCKS
from test_utilities.builders.location import LocationBuilder, ParentBuilder

class TestLocationJSONParser():

    @pytest.mark.parametrize(
      "location_dict, expected_location",
      [
        (
            LOCATIONS_API_MOCKS[LocationsMocks.CASE_ELEMENT],
            LocationBuilder().set_global_sort_order(1)
                             .set_parent(
                                 ParentBuilder().set_project(2)
                                                .set_item(3)
                                                .get_element()
                             )
                             .set_sequence('DummySequence 1')
                             .set_sort_order(4)
                             .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_item_returns_expected_value(self, location_dict: dict, expected_location: Location) -> None:
        location = LocationJSONParser.parse(location_dict)
        assert expected_location == location