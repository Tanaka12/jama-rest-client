from typing import List

import pytest
from unittest.mock import Mock

from jama_rest_client.api import ItemTypesAPI
from jama_rest_client.model.item_type import ItemType, ItemTypeCategory, ItemTypeFieldTextType, ItemTypeFieldType
from jama_rest_client.model.http import HTTPResponse

from mocks.item_types import ItemTypesMocks, ITEM_TYPES_API_MOCKS
from test_utilities.builders.http import HTTPResponseBuilder
from test_utilities.builders.item_type import ItemTypeBuilder, ItemTypeFieldBuilder

class TestItemTypesAPI():
    __service: ItemTypesAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = ItemTypesAPI(self.__http_client)
    
    def test_validate_happy_path_get_item_types_calls_http_get_method_with_expected_resource(self) -> None:
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_item_types()    
        self.__http_client.get.assert_called_once_with('/rest/v1/itemtypes?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_item_types",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_COMPONENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemTypeBuilder().set_id(1)
                                 .set_type_key('DummyTypeKey 1')
                                 .set_display('DummyDisplay 1')
                                 .set_display_plural('DummyDisplayPlural 1')
                                 .set_description('DummyDescription 1')
                                 .set_image('DummyImage 1')
                                 .set_category(ItemTypeCategory.COMPONENT)
                                 .set_system(True)
                                 .get_element()
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemTypeBuilder().set_id(index)
                                 .set_type_key(f'DummyTypeKey {index}')
                                 .set_display(f'DummyDisplay {index}')
                                 .set_display_plural(f'DummyDisplayPlural {index}')
                                 .set_description(f'DummyDescription {index}')
                                 .set_image(f'DummyImage {index}')
                                 .set_category(ItemTypeCategory.COMPONENT)
                                 .set_fields(
                                    [
                                        ItemTypeFieldBuilder().set_id(1)
                                                              .set_name('DummyName 1')
                                                              .set_label('DummyLabel 1')
                                                              .set_field_type(ItemTypeFieldType.ACTIONS)
                                                              .set_read_only(False)
                                                              .set_read_only_allow_api_overwrite(False)
                                                              .set_required(False)
                                                              .set_trigger_suspect(False)
                                                              .set_synchronize(False)
                                                              .set_pick_list(1)
                                                              .set_text_type(ItemTypeFieldTextType.ATTACHMENT)
                                                              .set_item_type(1)
                                                              .get_element()
                                    ]
                                 )
                                 .set_system(True)
                                 .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_COMPONENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEM_TYPES_API_MOCKS[ItemTypesMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemTypeBuilder().set_id(index)
                                 .set_type_key(f'DummyTypeKey {index}')
                                 .set_display(f'DummyDisplay {index}')
                                 .set_display_plural(f'DummyDisplayPlural {index}')
                                 .set_description(f'DummyDescription {index}')
                                 .set_image(f'DummyImage {index}')
                                 .set_category(ItemTypeCategory.COMPONENT)
                                 .set_fields(
                                    [
                                        ItemTypeFieldBuilder().set_id(1)
                                                              .set_name('DummyName 1')
                                                              .set_label('DummyLabel 1')
                                                              .set_field_type(ItemTypeFieldType.ACTIONS)
                                                              .set_read_only(False)
                                                              .set_read_only_allow_api_overwrite(False)
                                                              .set_required(False)
                                                              .set_trigger_suspect(False)
                                                              .set_synchronize(False)
                                                              .set_pick_list(1)
                                                              .set_text_type(ItemTypeFieldTextType.ATTACHMENT)
                                                              .set_item_type(1)
                                                              .get_element()
                                    ]
                                 )
                                 .set_system(True)
                                 .get_element() for index in range(1,30)
            ] +
            [
                ItemTypeBuilder().set_id(1)
                                 .set_type_key('DummyTypeKey 1')
                                 .set_display('DummyDisplay 1')
                                 .set_display_plural('DummyDisplayPlural 1')
                                 .set_description('DummyDescription 1')
                                 .set_image('DummyImage 1')
                                 .set_category(ItemTypeCategory.COMPONENT)
                                 .set_system(True)
                                 .get_element()
            ]
        )
      ]
    )
    def test_validate_happy_path_get_item_types_returns_expected_value(self, http_responses: List[HTTPResponse], expected_item_types: List[ItemType]) -> None:
        self.__http_client.get.side_effect = http_responses
        
        item_types: List[ItemType] = self.__service.get_item_types()  
        assert expected_item_types == item_types 