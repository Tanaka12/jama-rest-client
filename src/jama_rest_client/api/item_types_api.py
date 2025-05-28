from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.dal.parsers.json import ItemTypeJSONParser
from jama_rest_client.model.item_type import ItemType

from .base_api import BaseAPI

class ItemTypesAPI(BaseAPI):
    __resourceName: str = '/rest/v1/itemtypes'

    def __init__(self, http_client: HTTPClient):
        super().__init__(http_client)
        
    def get_item_types(self) -> List[ItemType]:
        item_types: List[ItemType] = []

        start_index: int = 0
        while True:
            item_types_batch = self.__parse_item_types_dict(self._get(f'{self.__resourceName}?startAt={start_index}&maxResults=50').body['data'])
            
            if len(item_types_batch) == 0:
                break

            item_types.extend(item_types_batch)
            start_index += len(item_types_batch)

        return item_types
    
    def __parse_item_types_dict(self, item_types_list_dict: List[dict]) -> List[ItemType]:
        return list(map(lambda item_type_dict: ItemTypeJSONParser.parse(item_type_dict), item_types_list_dict)) 