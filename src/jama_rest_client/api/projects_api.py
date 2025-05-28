from typing import List

from jama_rest_client.http import HTTPClient
from jama_rest_client.dal.parsers.json import ProjectJSONParser
from jama_rest_client.model.project import Project

from .base_api import BaseAPI

class ProjectsAPI(BaseAPI):
    __resourceName: str = '/rest/v1/projects'

    def __init__(self, http_client: HTTPClient):
        super().__init__(http_client)
        
    def get_projects(self) -> List[Project]:
        projects: List[Project] = []

        start_index: int = 0
        while True:
            projects_batch = self.__parse_projects_dict(self._get(f'{self.__resourceName}?startAt={start_index}&maxResults=50').body['data'])
            
            if len(projects_batch) == 0:
                break

            projects.extend(projects_batch)
            start_index += len(projects_batch)

        return projects
    
    def __parse_projects_dict(self, projects_list_dict: List[dict]) -> List[Project]:
        return list(map(lambda project_dict: ProjectJSONParser.parse(project_dict), projects_list_dict))