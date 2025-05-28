import pytest

from jama_rest_client.dal.parsers.json import ItemTypeJSONParser
from jama_rest_client.model.item_type import ItemType

from mocks.item_types import ItemTypesMocks, ITEM_TYPES_API_MOCKS
from test_utilities.builders.item_type import ItemTypeBuilder, ItemTypeFieldBuilder

class TestItemTypeJSONParser():

    @pytest.mark.parametrize(
      "item_type_dict, expected_item_type",
      [
        (
            ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_1_ELEMENT]['data'][0],
            ItemTypeBuilder().set_id(1)
                             .set_key('DummyTypeKey 1')
                             .set_display('DummyDisplay 1')
                             .set_display_plural('DummyDisplayPlural 1')
                             .set_description('DummyDescription 1')
                             .set_category('DummyCategory 1')
                             .set_fields(
                                 [
                                     ItemTypeFieldBuilder().set_id(1)
                                                           .set_name('DummyName 1')
                                                           .set_label('DummyLabel 1')
                                                           .set_field_type('DummyFieldType 1')
                                                           .set_read_only(True)
                                                           .set_required(False)
                                                           .set_trigger_suspect(False)
                                                           .set_synchronize(False)
                                                           .set_text_type('DummyTextType 1')
                                                           .get_element(),
                                     ItemTypeFieldBuilder().set_id(2)
                                                           .set_name('DummyName 2')
                                                           .set_label('DummyLabel 2')
                                                           .set_field_type('DummyFieldType 2')
                                                           .set_read_only(False)
                                                           .set_required(True)
                                                           .set_trigger_suspect(False)
                                                           .set_synchronize(False)
                                                           .set_text_type('DummyTextType 2')
                                                           .get_element(),
                                     ItemTypeFieldBuilder().set_id(3)
                                                           .set_name('DummyName 3')
                                                           .set_label('DummyLabel 3')
                                                           .set_field_type('DummyFieldType 3')
                                                           .set_read_only(False)
                                                           .set_required(False)
                                                           .set_trigger_suspect(True)
                                                           .set_synchronize(False)
                                                           .set_text_type('DummyTextType 3')
                                                           .get_element(),
                                     ItemTypeFieldBuilder().set_id(4)
                                                           .set_name('DummyName 4')
                                                           .set_label('DummyLabel 4')
                                                           .set_field_type('DummyFieldType 4')
                                                           .set_read_only(False)
                                                           .set_required(False)
                                                           .set_trigger_suspect(False)
                                                           .set_synchronize(True)
                                                           .set_text_type('DummyTextType 4')
                                                           .get_element()
                                 ]
                             ).get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_item_type_returns_expected_value(self, item_type_dict: dict, expected_item_type: ItemType) -> None:
        item_type = ItemTypeJSONParser.parse(item_type_dict)
        assert expected_item_type == item_type