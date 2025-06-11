from enum import Enum
import json
import os
import pathlib

API_SCENARIOS_PATH: str = os.path.join(str(pathlib.Path(__file__).parent.resolve()), 'api_scenarios')

class ActivitiesMocks(str, Enum):
    CASE_1_ACTIVITY = "CASE_1_ACTIVITY"   
    CASE_19_ACTIVITIES = "CASE_19_ACTIVITIES"
    CASE_ACTIVITIES_EMPTY = "CASE_ACTIVITIES_EMPTY"
    CASE_ACTIVITY_SINGLE = "CASE_ACTIVITY_SINGLE"
    CASE_ACTIVITY_SINGLE_WRONG_EVENT_TYPE = "CASE_ACTIVITY_SINGLE_WRONG_EVENT_TYPE"
    CASE_ACTIVITY_SINGLE_WRONG_OBJECT_TYPE = "CASE_ACTIVITY_SINGLE_WRONG_OBJECT_TYPE"

ACTIVITIES_API_MOCKS: dict[ActivitiesMocks, dict] = \
{
    ActivitiesMocks.CASE_1_ACTIVITY: json.load(open(os.path.join(API_SCENARIOS_PATH, '1_activity.json'))),
    ActivitiesMocks.CASE_19_ACTIVITIES: json.load(open(os.path.join(API_SCENARIOS_PATH, '19_activities.json'))),
    ActivitiesMocks.CASE_ACTIVITIES_EMPTY: json.load(open(os.path.join(API_SCENARIOS_PATH, 'activities_empty.json'))),
    ActivitiesMocks.CASE_ACTIVITY_SINGLE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'activity_single.json'))),
    ActivitiesMocks.CASE_ACTIVITY_SINGLE_WRONG_EVENT_TYPE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'activity_single_wrong_event_type.json'))),
    ActivitiesMocks.CASE_ACTIVITY_SINGLE_WRONG_OBJECT_TYPE: json.load(open(os.path.join(API_SCENARIOS_PATH, 'activity_single_wrong_object_type.json')))
}