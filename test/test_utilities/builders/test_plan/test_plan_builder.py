from jama_rest_client.model.test_plan import TestPlan
from typing_extensions import Self

class TestPlanBuilder:
    __test_plan: TestPlan

    def __init__(self):
        self.__test_plan = TestPlan()

    def set_id(self, id: int) -> Self:
        self.__test_plan.id = id
        return self
    
    def set_document_key(self, document_key: str) -> Self:
        self.__test_plan.document_key = document_key
        return self
    
    def set_global_id(self, global_id: str) -> Self:
        self.__test_plan.global_id = global_id
        return self

    def set_project(self, project: int) -> Self:
        self.__test_plan.project = project
        return self

    def set_item_type(self, item_type: int) -> Self:
        self.__test_plan.item_type = item_type
        return self
    
    def set_created_date(self, created_date: str) -> Self:
        self.__test_plan.created_date = created_date
        return self
    
    def set_modified_date(self, modified_date: str) -> Self:
        self.__test_plan.modified_date = modified_date
        return self

    def set_last_activity_date(self, last_activity_date: str) -> Self:
        self.__test_plan.last_activity_date = last_activity_date
        return self

    def set_created_by(self, created_by: int) -> Self:
        self.__test_plan.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int) -> Self:
        self.__test_plan.modified_by = modified_by
        return self
    
    def set_fields(self, fields: dict) -> Self:
        self.__test_plan.fields = fields
        return self

    def set_archived(self, archived: bool) -> Self:
        self.__test_plan.archived = archived
        return self

    def get_element(self) -> TestPlan:
        return self.__test_plan