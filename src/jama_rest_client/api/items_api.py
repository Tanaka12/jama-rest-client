from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.model.item import Item
from jama_rest_client.dal.parsers.json import ItemJSONParser

from .base_api import BaseAPI

class ItemsAPI(BaseAPI):
    __resourceName: str = '/rest/v1/items'

    def __init__(self, http_client: HTTPClient):
        super().__init__(http_client)

    def get_item(self, item_id: int) -> Item:
        return self.__get_item(item_id)

    def get_project_children(self, project_id: int) -> List[Item]:
       return self.__get_root_items(project_id)

    def get_item_children(self, item_id: int) -> List[Item]:
        return self.__get_item_children(item_id)

    def get_item_upstream_related(self, item_id: int) -> List[Item]:
        return self.__get_item_upstream_related(item_id)

    def get_item_downstream_related(self, item_id: int) -> List[Item]:
        return self.__get_item_downstream_related(item_id)    
    
    def __get_root_items(self, project_id: int) -> List[Item]:
        items: List[Item] = []

        start_index: int = 0
        while True:
            items_batch = self.__parse_items_dict(self._get(f'{self.__resourceName}?project={project_id}&rootOnly=true&startAt={start_index}&maxResults=50').body['data'])
            
            if len(items_batch) == 0:
                break

            items.extend(items_batch)
            start_index += len(items_batch)

        return items

    def __get_item_children(self, item_id: int) -> List[Item]:
        items: List[Item] = []

        start_index: int = 0
        while True:
            items_batch = self.__parse_items_dict(self._get(f'{self.__resourceName}/{item_id}/children?startAt={start_index}&maxResults=50').body['data'])
            
            if len(items_batch) == 0:
                break

            items.extend(items_batch)
            start_index += len(items_batch)

        return items

    def __get_item(self, item_id: int) -> Item:
        item_dict: dict = self._get(f'{self.__resourceName}/{item_id}').body

        return ItemJSONParser.parse(item_dict['data'])
   
    def __get_item_upstream_related(self, item_id: int) -> List[Item]:
        items: List[Item] = []

        start_index: int = 0
        while True:
            items_batch = self.__parse_items_dict(self._get(f'{self.__resourceName}/{item_id}/upstreamrelated?startAt={start_index}&maxResults=50').body['data'])
            
            if len(items_batch) == 0:
                break

            items.extend(items_batch)
            start_index += len(items_batch)

        return items
    
    def __get_item_downstream_related(self, item_id: int) -> List[Item]:
        items: List[Item] = []

        start_index: int = 0
        while True:
            items_batch = self.__parse_items_dict(self._get(f'{self.__resourceName}/{item_id}/downstreamrelated?startAt={start_index}&maxResults=50').body['data'])
            
            if len(items_batch) == 0:
                break

            items.extend(items_batch)
            start_index += len(items_batch)

        return items

    def __parse_items_dict(self, items_list_dict: List[dict]) -> List[Item]:
        return list(map(lambda item_dict: ItemJSONParser.parse(item_dict), items_list_dict))  