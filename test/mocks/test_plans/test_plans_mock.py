from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class TestPlansMocks(str, Enum):
    CASE_NO_ELEMENTS = "NO_ELEMENTS"
    CASE_1_ELEMENT = "1_ELEMENT"
    CASE_1_ELEMENT_ARCHIVED = "1_ELEMENT_ARCHIVED"
    CASE_30_ELEMENTS = "30 ELEMENTS"
    CASE_TEST_GROUP_NO_ELEMENTS = "CASE_TEST_GROUP_NO_ELEMENTS"
    CASE_TEST_GROUP_1_ELEMENT = "CASE_TEST_GROUP_1_ELEMENT"
    CASE_TEST_GROUP_30_ELEMENTS = "CASE_TEST_GROUP_30_ELEMENTS"    
    CASE_TEST_PLAN_REQUEST = "CASE_TEST_PLAN_REQUEST"    
    CASE_TEST_PLAN_SINGLE = "CASE_TEST_PLAN_SINGLE"

TEST_PLANS_API_MOCKS: dict[TestPlansMocks, dict] = \
{
    TestPlansMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'test_plans_empty.json'))),
    TestPlansMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_test_plan.json'))),
    TestPlansMocks.CASE_1_ELEMENT_ARCHIVED: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_test_plan_archived.json'))),
    TestPlansMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_test_plans.json'))),
    TestPlansMocks.CASE_TEST_GROUP_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'test_groups_empty.json'))),
    TestPlansMocks.CASE_TEST_GROUP_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_test_group.json'))),
    TestPlansMocks.CASE_TEST_GROUP_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_test_groups.json'))),
    TestPlansMocks.CASE_TEST_PLAN_REQUEST: json.load(open(os.path.join(API_SCENARIOS_PATH, 'test_plan_request.json'))),
    TestPlansMocks.CASE_TEST_PLAN_SINGLE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'test_plan_single.json')))
}