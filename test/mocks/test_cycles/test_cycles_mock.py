from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class TestCyclesMocks(str, Enum):
    CASE_NO_ELEMENTS = "NO_ELEMENTS"
    CASE_1_ELEMENT = "1_ELEMENT"
    CASE_30_ELEMENTS = "30 ELEMENTS"
    

TEST_CYCLES_API_MOCKS: dict[TestCyclesMocks, dict] = \
{
    TestCyclesMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'test_cycles_empty.json'))),
    TestCyclesMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_test_cycle.json'))),
    TestCyclesMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_test_cycles.json')))
}