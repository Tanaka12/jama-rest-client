from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ItemMocks(str, Enum):
    # For calls that request a single item
    CASE_ITEM_FOUND = "ITEM_FOUND"
    CASE_LOCKED_ITEM_FOUND = "LOCKED_ITEM_FOUND"

    # For calls that request item lists
    CASE_NO_ELEMENTS = "NO_ELEMENTS"
    CASE_1_ELEMENT = "1_ELEMENT"
    CASE_30_ELEMENTS = "30 ELEMENTS"
    

ITEMS_API_MOCKS: dict[ItemMocks, dict] = \
{
    ItemMocks.CASE_ITEM_FOUND: json.load(open(os.path.join(API_SCENARIOS_PATH, 'item_found.json'))),
    ItemMocks.CASE_LOCKED_ITEM_FOUND: json.load(open(os.path.join(API_SCENARIOS_PATH, 'item_locked_found.json'))),
    ItemMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'items_empty.json'))),
    ItemMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item.json'))),
    ItemMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_item.json')))
}