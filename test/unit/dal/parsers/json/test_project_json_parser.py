from typing import List

import pytest

from jama_rest_client.dal.parsers.json import ProjectJSONParser
from jama_rest_client.model.project import Project

from mocks.projects import ProjectsMocks, PROJECTS_API_MOCKS
from test_utilities.builders import ProjectBuilder

class TestProjectJSONParser():

    @pytest.mark.parametrize(
      "project_dict, expected_project",
      [
        (
            PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT]['data'][0],
            ProjectBuilder().set_id(1)
                            .set_project_key('DummyProjectKey 1')
                            .set_is_folder(False)
                            .set_created_date('DummyCreatedDate 1')
                            .set_modified_date('DummyModifiedDate 1')
                            .set_created_by(3)
                            .set_modified_by(4)
                            .set_fields(
                                {
                                  'randomFieldStr': 'randomFieldStr',
                                  'randomFieldBool': False,
                                  'randomFieldInt': 1
                                }
                            ).get_element()
        ),
        (
            PROJECTS_API_MOCKS[ProjectsMocks.CASE_1_ELEMENT_FOLDER]['data'][0],
            ProjectBuilder().set_id(1)
                            .set_project_key('DummyProjectKey 1')
                            .set_is_folder(True)
                            .set_created_date('DummyCreatedDate 1')
                            .set_modified_date('DummyModifiedDate 1')
                            .set_created_by(3)
                            .set_modified_by(4)
                            .set_fields(
                                {
                                  'randomFieldStr': 'randomFieldStr',
                                  'randomFieldBool': False,
                                  'randomFieldInt': 1
                                }
                            ).get_element()
        )
      ]
    )
    def test_validate_happy_path_get_item_type_parser_returns_expected_value(self, project_dict: dict, expected_project: Project) -> None:
        project = ProjectJSONParser.parse(project_dict)
        assert expected_project == project