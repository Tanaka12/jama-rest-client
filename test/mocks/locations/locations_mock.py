from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class LocationsMocks(str, Enum):
    CASE_ELEMENT = "CASE_ELEMENT"
    
LOCATIONS_API_MOCKS: dict[LocationsMocks, dict] = \
{
    LocationsMocks.CASE_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, 'location.json')))
}