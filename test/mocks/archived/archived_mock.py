from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ArchivedMocks(str, Enum):
    CASE_ARCHIVED = "CASE_ARCHIVED"   
    CASE_NO_ARCHIVED = "CASE_NO_ARCHIVED"   

ARCHIVED_API_MOCKS: dict[ArchivedMocks, dict] = \
{
    ArchivedMocks.CASE_NO_ARCHIVED: json.load(open(os.path.join(API_SCENARIOS_PATH, 'archived_status_request_false.json'))),
    ArchivedMocks.CASE_ARCHIVED: json.load(open(os.path.join(API_SCENARIOS_PATH, 'archived_status_request_true.json')))
}