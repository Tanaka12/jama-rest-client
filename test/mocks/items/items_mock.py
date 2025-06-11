from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ItemMocks(str, Enum):
    CASE_ITEM_FOUND = "CASE_ITEM_FOUND"
    CASE_NO_ELEMENTS = "CASE_NO_ELEMENTS"
    CASE_1_ELEMENT = "CASE_1_ELEMENT"
    CASE_30_ELEMENTS = "30 CASE_30_ELEMENTS"

ITEMS_API_MOCKS: dict[ItemMocks, dict] = \
{
    ItemMocks.CASE_ITEM_FOUND: json.load(open(os.path.join(API_SCENARIOS_PATH, 'item_found.json'))),
    ItemMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'items_empty.json'))),
    ItemMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_item.json'))),
    ItemMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_items.json')))
}