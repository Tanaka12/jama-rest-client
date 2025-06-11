from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class AttachmentsMocks(str, Enum):
    CASE_NO_ELEMENTS = "CASE_NO_ELEMENTS"
    CASE_1_ELEMENT = "CASE_1_ELEMENT"
    CASE_30_ELEMENTS = "30 CASE_30_ELEMENTS"

ATTACHMENTS_API_MOCKS: dict[AttachmentsMocks, dict] = \
{
    AttachmentsMocks.CASE_NO_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, 'attachments_empty.json'))),
    AttachmentsMocks.CASE_1_ELEMENT: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_attachment.json'))),
    AttachmentsMocks.CASE_30_ELEMENTS: json.load(open(os.path.join(API_SCENARIOS_PATH, '30_attachments.json')))
}