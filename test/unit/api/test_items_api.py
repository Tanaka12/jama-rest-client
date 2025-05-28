from typing import List

import pytest
from unittest.mock import Mock

from jama_rest_client.api import ItemsAPI
from jama_rest_client.model.item import Item
from jama_rest_client.model.http import HTTPResponse

from mocks.items import ItemMocks, ITEMS_API_MOCKS
from test_utilities.builders.http import HTTPResponseBuilder
from test_utilities.builders.item import ItemBuilder, ItemLocationBuilder, ItemLockBuilder

class TestItemTypesAPI():
    __service: ItemsAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = ItemsAPI(self.__http_client)
    
    # get_item call
    def test_validate_happy_path_get_item_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_ITEM_FOUND])\
                                                                   .get_element()
        
        self.__service.get_item(dummy_item_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/items/{dummy_item_id}')

    @pytest.mark.parametrize(
      "http_response, expected_item",
      [
        (
            HTTPResponseBuilder().set_status_code(200)
                                 .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_ITEM_FOUND])
                                 .get_element(),
            ItemBuilder().set_id(1)
                        .set_document_key('DummyDocumentKey 1')
                        .set_global_id('DummyGlobalId 1')
                        .set_item_type(2)
                        .set_project(3)
                        .set_created_date('DummyCreatedDate 1')
                        .set_modified_date('DummyModifiedDate 1')
                        .set_last_activity_date('DummyLastActivityDate 1')
                        .set_created_by(4)
                        .set_modified_by(5)
                        .set_lock(
                            ItemLockBuilder().set_locked(False)
                                            .set_last_locked_date('DummyLastLockedDate 1')
                                            .get_element()
                        )
                        .set_location(
                            ItemLocationBuilder().set_sort_order(0)
                                                .set_global_sort_order(1)
                                                .set_sequence('DummySequence 1')
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
    def test_validate_happy_path_get_item_returns_expected_value(self, http_response, expected_item) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.return_value = http_response
        
        item: Item = self.__service.get_item(dummy_item_id)

        assert expected_item == item

    
    # get_item_children call
    def test_validate_happy_path_get_item_children_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_item_children(dummy_item_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/items/{dummy_item_id}/children?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_items",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ] +
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ]
        )
      ]
    )
    def test_validate_happy_path_get_item_children_returns_expected_value(self, http_responses: List[HTTPResponse], expected_items: List[Item]) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        items: List[Item] = self.__service.get_item_children(dummy_item_id)  
        assert expected_items == items


    # get_item_upstream_related call
    def test_validate_happy_path_get_item_upstream_related_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_item_upstream_related(dummy_item_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/items/{dummy_item_id}/upstreamrelated?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_items",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ] +
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ]
        )
      ]
    )
    def test_validate_happy_path_get_get_project_children_returns_expected_value(self, http_responses: List[HTTPResponse], expected_items: List[Item]) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        items: List[Item] = self.__service.get_item_upstream_related(dummy_item_id)  
        assert expected_items == items


    # get_item_downstream_related call
    def test_validate_happy_path_get_item_downstream_related_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_item_downstream_related(dummy_item_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/items/{dummy_item_id}/downstreamrelated?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_items",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ] +
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ]
        )
      ]
    )
    def test_validate_happy_path_get_item_downstream_related_returns_expected_value(self, http_responses: List[HTTPResponse], expected_items: List[Item]) -> None:
        dummy_item_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        items: List[Item] = self.__service.get_item_downstream_related(dummy_item_id)  
        assert expected_items == items


    # get_project_children call
    def test_validate_happy_path_get_project_children_calls_http_get_method_with_expected_resource(self) -> None:
        dummy_project_id: int = 2
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_project_children(dummy_project_id)    
        self.__http_client.get.assert_called_once_with(f'/rest/v1/items?project={dummy_project_id}&rootOnly=true&startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_items",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_30_ELEMENTS])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_1_ELEMENT])
                                     .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(ITEMS_API_MOCKS[ItemMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            [
                ItemBuilder().set_id(index)
                         .set_document_key(f'DummyDocumentKey {index}')
                         .set_global_id(f'DummyGlobalId {index}')
                         .set_item_type(index + 1)
                         .set_project(index + 2)
                         .set_created_date(f'DummyCreatedDate {index}')
                         .set_modified_date(f'DummyModifiedDate {index}')
                         .set_last_activity_date(f'DummyLastActivityDate {index}')
                         .set_created_by(index + 3)
                         .set_modified_by(index + 4)
                         .set_lock(
                             ItemLockBuilder().set_locked(bool(index % 2))
                                              .set_last_locked_date(f'DummyLastLockedDate {index}')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(index)
                                                  .set_global_sort_order(index + 1)
                                                  .set_sequence(f'DummySequence {index}')
                                                  .get_element()
                         )
                         .set_fields(
                            {
                              'fieldStr': 'DummyField',
                              'fieldInt': 0,
                              'fieldBool': True
                            }
                         )
                         .get_element() for index in range(1,30)
            ] +
            [
                ItemBuilder().set_id(1)
                         .set_document_key('DummyDocumentKey 1')
                         .set_global_id('DummyGlobalId 1')
                         .set_item_type(2)
                         .set_project(3)
                         .set_created_date('DummyCreatedDate 1')
                         .set_modified_date('DummyModifiedDate 1')
                         .set_last_activity_date('DummyLastActivityDate 1')
                         .set_created_by(4)
                         .set_modified_by(5)
                         .set_lock(
                             ItemLockBuilder().set_locked(False)
                                              .set_last_locked_date('DummyLastLockedDate 1')
                                              .get_element()
                         )
                         .set_location(
                             ItemLocationBuilder().set_sort_order(0)
                                                  .set_global_sort_order(1)
                                                  .set_sequence('DummySequence 1')
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
            ]
        )
      ]
    )
    def test_validate_happy_path_get_get_project_children_returns_expected_value(self, http_responses: List[HTTPResponse], expected_items: List[Item]) -> None:
        dummy_project_id: int = 2
        self.__http_client.get.side_effect = http_responses
        
        items: List[Item] = self.__service.get_project_children(dummy_project_id)  
        assert expected_items == items