from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ProjectsMocks(str, Enum):
    CASE_NO_ELEMENTS = "NO_ELEMENTS"
    CASE_1_ELEMENT = "1_ELEMENT"
    CASE_1_ELEMENT_FOLDER = "1_ELEMENT_FOLDER"
    CASE_30_ELEMENTS = "30 ELEMENTS"
    

PROJECTS_API_MOCKS: dict[ProjectsMocks, dict] = \
{
    ProjectsMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'projects_empty.json'))),
    ProjectsMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_project.json'))),
    ProjectsMocks.CASE_1_ELEMENT_FOLDER: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_project_folder.json'))),
    ProjectsMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_projects.json')))
}