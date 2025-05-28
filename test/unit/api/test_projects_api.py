from typing import List

import pytest
from unittest.mock import Mock

from jama_rest_client.api import ProjectsAPI
from jama_rest_client.model.project import Project
from jama_rest_client.model.http import HTTPResponse

from mocks.projects import ProjectsMocks, PROJECTS_API_MOCKS
from test_utilities.builders.http import HTTPResponseBuilder
from test_utilities.builders.project import ProjectBuilder

class TestProjectsAPI():
    __service: ProjectsAPI
    __http_client: Mock

    def setup_method(self):
        self.__http_client = Mock()
        self.__service = ProjectsAPI(self.__http_client)
    
    def test_validate_happy_path_get_projects_calls_http_get_method_with_expected_resource(self) -> None:
        self.__http_client.get.return_value = HTTPResponseBuilder().set_status_code(200) \
                                                                   .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_NO_ELEMENTS])\
                                                                   .get_element()
        
        self.__service.get_projects()    
        self.__http_client.get.assert_called_once_with('/rest/v1/projects?startAt=0&maxResults=50')

    @pytest.mark.parametrize(
      "http_responses, expected_projects",
      [
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                     .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_NO_ELEMENTS])
                                     .get_element()
            ],
            []
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                ProjectBuilder().set_id(1)
                                .set_project_key('DummyProjectKey 1')
                                .set_is_folder(False)
                                .set_created_date('DummyCreatedDate 1')
                                .set_modified_date('DummyModifiedDate 1')
                                .set_created_by(3)
                                .set_modified_by(4)
                                .set_fields(
                                {
                                    "randomFieldStr": "randomFieldStr",
                                    "randomFieldBool": False,
                                    "randomFieldInt": 1
                                }).get_element()
            ] 
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_30_ELEMENTS])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                ProjectBuilder().set_id(index)
                                .set_project_key(f'DummyProjectKey {index}')
                                .set_is_folder(True)
                                .set_created_date(f'DummyCreatedDate {index}')
                                .set_modified_date(f'DummyModifiedDate {index}')
                                .set_created_by(index + 2)
                                .set_modified_by(index + 3)
                                .set_fields(
                                {
                                    "randomFieldStr": "randomFieldStr",
                                    "randomFieldBool": True,
                                    "randomFieldInt": 1
                                }).get_element() for index in range(1,30)
            ]     
        ),
        (
            [
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_30_ELEMENTS])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT])
                                    .get_element(),
                HTTPResponseBuilder().set_status_code(200)
                                    .set_body(PROJECTS_API_MOCKS[ProjectsMocks.CASE_NO_ELEMENTS])
                                    .get_element()
            ],
            [
                ProjectBuilder().set_id(index)
                                .set_project_key(f'DummyProjectKey {index}')
                                .set_is_folder(True)
                                .set_created_date(f'DummyCreatedDate {index}')
                                .set_modified_date(f'DummyModifiedDate {index}')
                                .set_created_by(index + 2)
                                .set_modified_by(index + 3)
                                .set_fields(
                                {
                                    "randomFieldStr": "randomFieldStr",
                                    "randomFieldBool": True,
                                    "randomFieldInt": 1
                                }).get_element() for index in range(1,30)
            ] +
            [
                ProjectBuilder().set_id(1)
                                .set_project_key('DummyProjectKey 1')
                                .set_is_folder(False)
                                .set_created_date('DummyCreatedDate 1')
                                .set_modified_date('DummyModifiedDate 1')
                                .set_created_by(3)
                                .set_modified_by(4)
                                .set_fields(
                                {
                                    "randomFieldStr": "randomFieldStr",
                                    "randomFieldBool": False,
                                    "randomFieldInt": 1
                                }).get_element()
            ]
        )
      ]
    )
    def test_validate_happy_path_get_projects_returns_expected_value(self, http_responses: List[HTTPResponse], expected_projects: List[Project]) -> None:
        self.__http_client.get.side_effect = http_responses
        
        item_types: List[Project] = self.__service.get_projects()  
        assert expected_projects == item_types 