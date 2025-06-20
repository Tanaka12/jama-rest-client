from datetime import datetime
import pytest

from jama_rest_client.dal.parsers.json import ItemJSONParser
from jama_rest_client.model.item import Item

from mocks.items import ItemMocks, ITEMS_API_MOCKS
from test_utilities.builders.item import ItemBuilder
from test_utilities.builders.location import LocationBuilder, ParentBuilder
from test_utilities.builders.lock import LockBuilder

class TestItemJSONParser():

    @pytest.mark.parametrize(
      "item_dict, expected_item",
      [
        (
            ITEMS_API_MOCKS[ItemMocks.CASE_ITEM_FOUND]['data'],
            ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_child_item_type(6)
                         .set_created_date(datetime.fromtimestamp(1582199426))
                         .set_modified_date(datetime.fromtimestamp(1582199426))
                         .set_last_activity_date(datetime.fromtimestamp(1582199426))
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             LockBuilder().set_locked(False)
                                          .set_last_locked_date(datetime.fromtimestamp(1582199426))
                                          .set_locked_by(0)
                                          .get_element()
                         )
                         .set_location(
                             LocationBuilder().set_sort_order(0)
                                              .set_global_sort_order(1)
                                              .set_sequence('DummySequence 1')
                                              .set_parent(
                                                  ParentBuilder().set_project(2)
                                                                 .set_item(3)
                                                                 .get_element()
                                              )
                                              .get_element()
                         )
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
    def test_validate_happy_path_parse_item_returns_expected_value(self, item_dict: dict, expected_item: Item) -> None:
        item = ItemJSONParser.parse(item_dict)
        assert expected_item == item