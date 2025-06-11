from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ApiResponsesMocks(str, Enum):
    CASE_CREATED_RESPONSE = "CASE_CREATED_RESPONSE"   
    CASE_ABSTRACT_REST_RESPONSE = "CASE_ABSTRACT_REST_RESPONSE"   

API_RESPONSES_API_MOCKS: dict[ApiResponsesMocks, dict] = \
{
    ApiResponsesMocks.CASE_CREATED_RESPONSE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'created_response.json'))),
    ApiResponsesMocks.CASE_ABSTRACT_REST_RESPONSE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'abstract_rest_response.json')))
}