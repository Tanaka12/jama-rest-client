from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class PageInfoMocks(str, Enum):
    CASE_PAGE_INFO = "CASE_PAGE_INFO"   

PAGE_INFO_API_MOCKS: dict[PageInfoMocks, dict] = \
{
    PageInfoMocks.CASE_PAGE_INFO: json.load(open(os.path.join(API_SCENARIOS_PATH, 'page_info.json')))
}