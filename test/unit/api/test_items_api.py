from typing import List

import pytest
from unittest.mock import Mock

from jama_rest_client.api import ItemTypesAPI
from jama_rest_client.model.item_type import ItemType

class TestItemsAPI():
    __service: ItemTypesAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = ItemTypesAPI(self.__http_client)
    
    @pytest.fixture()
    def test_validate_happy_path_get_item_types_returns_expected_value(self) -> None:
        self.__http_client.get.return = 200

        item_types: List[ItemType] = self.__service.get_item_types()