from datetime import datetime
from jama_rest_client.model.activity import Activity, EventType, ObjectType
from typing_extensions import Self

class ActivityBuilder:
    __activity: Activity

    def __init__(self):
        self.__activity = Activity()

    def set_id(self, id: int) -> Self:
        self.__activity.id = id
        return self
    
    def set_date(self, date: datetime) -> Self:
        self.__activity.date = date
        return self
    
    def set_details(self, details: str) -> Self:
        self.__activity.details = details
        return self
    
    def set_action(self, action: str) -> Self:
        self.__activity.action = action
        return self

    def set_user(self, user: int) -> Self:
        self.__activity.user = user
        return self

    def set_user_comment(self, user_comment: str) -> Self:
        self.__activity.user_comment = user_comment
        return self

    def set_item(self, item: int) -> Self:
        self.__activity.item = item
        return self

    def set_item_type(self, item_type: int) -> Self:
        self.__activity.item_type = item_type
        return self
    
    def set_event_type(self, event_type: EventType) -> Self:
        self.__activity.event_type = event_type
        return self
    
    def set_object_type(self, object_type: ObjectType) -> Self:
        self.__activity.object_type = object_type
        return self
    
    def get_element(self) -> Activity:
        return self.__activity
    