from jama_rest_client.model.project import Project
from typing_extensions import Self

class ProjectBuilder:
    __project: Project

    def __init__(self):
        self.__project = Project()

    def set_id(self, id: int) -> Self:
        self.__project.id = id
        return self
    
    def set_project_key(self, project_key: str) -> Self:
        self.__project.project_key = project_key
        return self
    
    def set_is_folder(self, is_folder: bool) -> Self:
        self.__project.is_folder = is_folder
        return self
    
    def set_created_date(self, created_date: str) -> Self:
        self.__project.created_date = created_date
        return self
    
    def set_modified_date(self, modified_date: str) -> Self:
        self.__project.modified_date = modified_date
        return self

    def set_created_by(self, created_by: int) -> Self:
        self.__project.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int) -> Self:
        self.__project.modified_by = modified_by
        return self
    
    def set_fields(self, fields: dict) -> Self:
        self.__project.fields = fields
        return self

    def get_element(self) -> Project:
        return self.__project