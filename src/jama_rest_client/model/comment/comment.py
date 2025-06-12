from datetime import datetime
from enum import Enum
from typing_extensions import Self

class CommentStatus(str, Enum):
    OPEN = 'OPEN'
    CANCELLED = 'CANCELLED' 
    COMPLETED = 'COMPLETED'

class CommentType(str, Enum):
    GENERAL = 'GENERAL'
    QUESTION = 'QUESTION'
    PROPOSED_CHANGE = 'PROPOSED_CHANGE'
    ACCEPTED_COMMENT = 'ACCEPTED_COMMENT'
    REJECTED_COMMENT = 'REJECTED_COMMENT'
    ISSUE = 'ISSUE'
    DECISION = 'DECISION'
    DECISION_REQUEST = 'DECISION_REQUEST'

class CommentBody:
    text: str

    def __init__(self):
        self.text = ""

    def __eq__(self, other: Self):
        return self.text == other.text

class CommentLocation:
    item: int
    project: int

    def __init__(self):
        self.item = 0
        self.project = 0

    def __eq__(self, other: Self):
        return self.item == other.item \
            and self.project == other.project

class Comment:
    id: int
    in_reply_to: int
    created_date: datetime
    created_by: int
    modified_by: int
    deleted: bool
    status: CommentStatus
    body: CommentBody
    comment_type: CommentType
    location: CommentLocation

    def __init__(self):
        self.id = 0
        self.in_reply_to = 0
        self.created_date = datetime.fromtimestamp(0)
        self.created_by = 0
        self.modified_by = 0
        self.deleted = False
        self.status = CommentStatus.CANCELLED
        self.body = CommentBody()
        self.comment_type = CommentType.ACCEPTED_COMMENT
        self.location = CommentLocation()

    def __eq__(self, other: Self):
        return self.id == other.id \
            and self.in_reply_to == other.in_reply_to \
            and self.created_date == other.created_date \
            and self.created_by == other.created_by \
            and self.modified_by == other.modified_by \
            and self.deleted == other.deleted \
            and self.status == other.status \
            and self.body == other.body \
            and self.comment_type == other.comment_type \
            and self.location == other.location