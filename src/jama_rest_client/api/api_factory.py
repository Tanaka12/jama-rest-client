import jama_rest_client
from jama_rest_client.http import HTTPClient, HTTPFactory

from .projects_api import ProjectsAPI

class APIFactory:
    __context: jama_rest_client.Context

    def __init__(self, context: jama_rest_client.Context):
        self.__context = context

    def build_projects_api(self) -> ProjectsAPI:
        http_client: HTTPClient = HTTPFactory(self.__context).build_http_client()

        return ProjectsAPI(http_client)