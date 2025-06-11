from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ItemTypesMocks(str, Enum):
    CASE_NO_ELEMENTS = "CASE_NO_ELEMENTS"
    CASE_1_ELEMENT = "CASE_1_ELEMENT"
    CASE_1_ELEMENT_CATEGORY_COMPONENT = "CASE_1_ELEMENT_CATEGORY_COMPONENT"
    CASE_1_ELEMENT_CATEGORY_CORE = "CASE_1_ELEMENT_CATEGORY_CORE"
    CASE_1_ELEMENT_CATEGORY_DEFECT = "CASE_1_ELEMENT_CATEGORY_DEFECT"
    CASE_1_ELEMENT_CATEGORY_SECTION = "CASE_1_ELEMENT_CATEGORY_SECTION"
    CASE_1_ELEMENT_CATEGORY_SET = "CASE_1_ELEMENT_CATEGORY_SET"
    CASE_1_ELEMENT_CATEGORY_TEST_CASE = "CASE_1_ELEMENT_CATEGORY_TEST_CASE"
    CASE_1_ELEMENT_CATEGORY_TEST_CYCLE = "CASE_1_ELEMENT_CATEGORY_TEST_CYCLE"
    CASE_1_ELEMENT_CATEGORY_TEST_PLAN = "CASE_1_ELEMENT_CATEGORY_TEST_PLAN"
    CASE_1_ELEMENT_CATEGORY_TEST_RUN = "CASE_1_ELEMENT_CATEGORY_TEST_RUN"
    CASE_1_ELEMENT_CATEGORY_TEXT = "CASE_1_ELEMENT_CATEGORY_TEXT"
    CASE_1_ELEMENT_WRONG_FIELD_TYPE = "CASE_1_ELEMENT_WRONG_FIELD_TYPE"
    CASE_1_ELEMENT_WRONG_TEXT_TYPE = "CASE_1_ELEMENT_WRONG_TEXT_TYPE"
    CASE_1_ELEMENT_WRONG_CATEGORY = "CASE_1_ELEMENT_WRONG_CATEGORY"
    CASE_30_ELEMENTS = "CASE_30_ELEMENTS"
    

ITEM_TYPES_API_MOCKS: dict[ItemTypesMocks, dict] = \
{
    ItemTypesMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'item_types_empty.json'))),
    ItemTypesMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_COMPONENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_component.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_CORE: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_core.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_DEFECT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_defect.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_SECTION: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_section.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_SET: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_set.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_TEST_CASE: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_test_case.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_TEST_CYCLE: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_test_cycle.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_TEST_PLAN: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_test_plan.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_TEST_RUN: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_test_run.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_CATEGORY_TEXT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_category_text.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_WRONG_FIELD_TYPE: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_item_field_wrong_field_type.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_WRONG_TEXT_TYPE: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_item_field_wrong_text_type.json'))),
    ItemTypesMocks.CASE_1_ELEMENT_WRONG_CATEGORY: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item_type_wrong_category.json'))),
    ItemTypesMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_item_type.json')))
}