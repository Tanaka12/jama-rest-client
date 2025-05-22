import jama_rest_client
from jama_rest_client.http import HTTPClient, HTTPFactory

from .item_types_api import ItemTypesAPI
from .items_api import ItemsAPI
from .projects_api import ProjectsAPI

class APIFactory:
    __context: jama_rest_client.Context

    def __init__(self, context: jama_rest_client.Context):
        self.__context = context

    def build_item_types_api(self) -> ItemTypesAPI:
        http_client: HTTPClient = HTTPFactory(self.__context).build_http_client()

        return ItemTypesAPI(http_client)

    def build_items_api(self) -> ItemsAPI:
        http_client: HTTPClient = HTTPFactory(self.__context).build_http_client()

        return ItemsAPI(http_client)

    def build_projects_api(self) -> ProjectsAPI:
        http_client: HTTPClient = HTTPFactory(self.__context).build_http_client()

        return ProjectsAPI(http_client)