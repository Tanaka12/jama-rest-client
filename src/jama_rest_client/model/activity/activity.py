from enum import Enum
from datetime import datetime
from typing_extensions import Self

class EventType(str, Enum):
    BATCH_COPY = 'BATCH_COPY'
    BATCH_CREATE = 'BATCH_CREATE'
    BATCH_DELETE = 'BATCH_DELETE'
    BATCH_SUMMARY = 'BATCH_SUMMARY'
    BATCH_UPDATE = 'BATCH_UPDATE'
    COPY = 'COPY'
    CREATE = 'CREATE'
    DELETE = 'DELETE'
    MOVE = 'MOVE'
    PUBLIC = 'PUBLIC'
    UPDATE = 'UPDATE'

class ObjectType(str, Enum):
    BASELINE = 'BASELINE'
    CHANGE_REQUEST = 'CHANGE_REQUEST'
    COMMENT = 'COMMENT'
    INTEGRATION = 'INTEGRATION'
    ITEM_ATTACHMENT = 'ITEM_ATTACHMENT'
    ITEM_TAG = 'ITEM_TAG'
    MISCELLANEOUS = 'MISCELLANEOUS'
    PROJECT = 'PROJECT'
    RELATIONSHIP = 'RELATIONSHIP'
    REVIEW = 'REVIEW'
    REVISION = 'REVISION'
    REVISION_ITEM = 'REVISION_ITEM'
    TAG = 'TAG'
    TEST_CYCLE = 'TEST_CYCLE'
    TEST_PLAN = 'TEST_PLAN'
    TEST_RESULT = 'TEST_RESULT'
    TEST_RUN = 'TEST_RUN'
    URL = 'URL'
    USER = 'USER'

class Activity:
    id: int
    date: datetime
    details: str
    action: str
    user: int
    user_comment: str
    item: int
    item_type: int
    event_type: EventType
    object_type: ObjectType

    def __init__(self):
        self.id = 0
        self.date = datetime.fromtimestamp(0)
        self.details = ""
        self.action = ""
        self.user = 0
        self.user_comment = "" 
        self.item = 0
        self.item_type = 0
        self.event_type = EventType.BATCH_COPY
        self.object_type = ObjectType.BASELINE

    def __eq__(self, other: Self):
        return self.id == other.id \
            and self.date == other.date \
            and self.details == other.details \
            and self.action == other.action \
            and self.user == other.user \
            and self.user_comment == other.user_comment \
            and self.item == other.item \
            and self.item_type == other.item_type \
            and self.event_type == other.event_type \
            and self.object_type == other.object_type