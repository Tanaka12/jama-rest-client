class TestPlan:
    id: int
    document_key: str
    global_id: str
    project: int
    item_type: int
    created_date: str
    modified_date: str
    last_activity_date: str
    created_by: int
    modified_by: int
    fields: dict
    archived: bool

    def __init__(self):
        self.id = 0
        self.document_key = ""
        self.global_id = ""
        self.project = 0
        self.item_type = 0
        self.created_date = ""
        self.modified_date = ""
        self.last_activity_date = ""
        self.created_by = 0
        self.modified_by = 0
        self.fields = {}
        self.archived = False

    def __eq__(self, other):
        if self.id == other.id \
        and self.document_key == other.document_key \
        and self.global_id == other.global_id \
        and self.project == other.project \
        and self.item_type == other.item_type \
        and self.created_date == other.created_date \
        and self.modified_date == other.modified_date \
        and self.last_activity_date == other.last_activity_date \
        and self.created_by == other.created_by \
        and self.modified_by == other.modified_by \
        and self.fields == other.fields \
        and self.archived == other.archived:
            return True

        return False