from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class RequestsMocks(str, Enum):
    CASE_PATCH_OPERATION_REQUEST_ADD = "CASE_PATCH_OPERATION_REQUEST_ADD"
    CASE_PATCH_OPERATION_REQUEST_DELETE = "CASE_PATCH_OPERATION_REQUEST_DELETE"
    CASE_PATCH_OPERATION_REQUEST_REPLACE = "CASE_PATCH_OPERATION_REQUEST_REPLACE"

REQUESTS_API_MOCKS: dict[RequestsMocks, dict] = \
{
    RequestsMocks.CASE_PATCH_OPERATION_REQUEST_ADD: json.load(open(os.path.join(API_SCENARIOS_PATH, 'patch_operation_request_add.json'))),
    RequestsMocks.CASE_PATCH_OPERATION_REQUEST_DELETE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'patch_operation_request_delete.json'))),
    RequestsMocks.CASE_PATCH_OPERATION_REQUEST_REPLACE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'patch_operation_request_replace.json')))
}