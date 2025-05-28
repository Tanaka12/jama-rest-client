class Project:
    id: int
    project_key: str
    is_folder: bool
    created_date: str
    modified_date: str
    created_by: int
    modified_by: int
    fields: dict

    def __init__(self):
        self.id = 0
        self.project_key = ""
        self.is_folder = False
        self.created_date = ""
        self.modified_date = ""
        self.created_by = 0
        self.modified_by = 0
        self.fields = {}

    def __eq__(self, other):
        if self.id == other.id \
        and self.project_key == other.project_key \
        and self.is_folder == other.is_folder \
        and self.created_date == other.created_date \
        and self.modified_date == other.modified_date \
        and self.created_by == other.created_by \
        and self.modified_by == other.modified_by \
        and self.fields == other.fields:
            return True

        return False