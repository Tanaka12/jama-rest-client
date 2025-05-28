from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class TestRunsMocks(str, Enum):
    CASE_NO_ELEMENTS = "NO_ELEMENTS"
    CASE_1_ELEMENT = "1_ELEMENT"
    CASE_30_ELEMENTS = "30 ELEMENTS"
    

TEST_RUNS_API_MOCKS: dict[TestRunsMocks, dict] = \
{
    TestRunsMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'test_runs_empty.json'))),
    TestRunsMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_test_run.json'))),
    TestRunsMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_test_runs.json')))
}