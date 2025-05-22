class Project:
    id: int
    projectKey: str
    isFolder: bool
    createdDate: str
    modifiedDate: str
    createdBy: int
    modifiedBy: int
    fields: dict

    def __init__(self):
        self.id = 0
        self.projectKey = ""
        self.isFolder = False
        self.createdDate = ""
        self.modifiedDate = ""
        self.createdBy = 0
        self.modifiedBy = 0
        self.fields = {}