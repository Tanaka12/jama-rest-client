from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class LocksMocks(str, Enum):
    CASE_LOCK_LOCKED = "CASE_LOCK_LOCKED"
    CASE_LOCK_NOT_LOCKED = "CASE_LOCK_NOT_LOCKED"

LOCKS_API_MOCKS: dict[LocksMocks, dict] = \
{
    LocksMocks.CASE_LOCK_LOCKED: json.load(open(os.path.join(API_SCENARIOS_PATH, 'lock_locked.json'))),
    LocksMocks.CASE_LOCK_NOT_LOCKED: json.load(open(os.path.join(API_SCENARIOS_PATH, 'lock_not_locked.json')))
}