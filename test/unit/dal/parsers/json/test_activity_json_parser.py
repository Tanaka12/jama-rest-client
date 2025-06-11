from datetime import datetime
import pytest

from jama_rest_client.dal.parsers.json import ActivityJSONParser
from jama_rest_client.model.activity import Activity, EventType, ObjectType

from mocks.activities import ActivitiesMocks, ACTIVITIES_API_MOCKS
from test_utilities.builders.activity import ActivityBuilder

class TestActivityJSONParser():

    @pytest.mark.parametrize(
      "activity_dict, expected_activity",
      [
        (
            ACTIVITIES_API_MOCKS[ActivitiesMocks.CASE_ACTIVITY_SINGLE]['data'],
            ActivityBuilder().set_id(1)
                             .set_date(datetime.fromtimestamp(1582199426))
                             .set_details('DummyDetails')
                             .set_action('DummyAction')
                             .set_user(2)
                             .set_user_comment('DummyUserComment')
                             .set_item(3)
                             .set_item_type(4)
                             .set_event_type(EventType.BATCH_COPY)
                             .set_object_type(ObjectType.BASELINE)
                             .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_activity_returns_expected_value(self, activity_dict: dict, expected_activity: Activity) -> None:
        activity = ActivityJSONParser.parse(activity_dict)
        assert expected_activity == activity

    @pytest.mark.parametrize(
      "activity_dict, expected_exception",
      [
        (
            ACTIVITIES_API_MOCKS[ActivitiesMocks.CASE_ACTIVITY_SINGLE_WRONG_EVENT_TYPE]['data'],
            ValueError('Activity eventType has an invalid value: DummyEventType')
        ),
        (
            ACTIVITIES_API_MOCKS[ActivitiesMocks.CASE_ACTIVITY_SINGLE_WRONG_OBJECT_TYPE]['data'],
            ValueError('Activity objectType has an invalid value: DummyObjectType')
        )
      ]
    )
    def test_validate_parse_activity_raises_exception_when_wrong_value(self, activity_dict: dict, expected_exception: ValueError) -> None:
        with pytest.raises(ValueError) as value_error_exception:
          ActivityJSONParser.parse(activity_dict)

        assert expected_exception.args == value_error_exception.value.args