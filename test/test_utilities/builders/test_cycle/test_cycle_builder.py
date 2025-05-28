from jama_rest_client.model.test_cycle import TestCycle

class TestCycleBuilder:
    __test_cycle: TestCycle

    def __init__(self):
        self.__test_cycle = TestCycle()

    def set_id(self, id: int):
        self.__test_cycle.id = id
        return self
    
    def set_document_key(self, document_key: str):
        self.__test_cycle.document_key = document_key
        return self
    
    def set_global_id(self, global_id: str):
        self.__test_cycle.global_id = global_id
        return self

    def set_project(self, project: int):
        self.__test_cycle.project = project
        return self

    def set_item_type(self, item_type: int):
        self.__test_cycle.item_type = item_type
        return self
    
    def set_created_date(self, created_date: str):
        self.__test_cycle.created_date = created_date
        return self
    
    def set_modified_date(self, modified_date: str):
        self.__test_cycle.modified_date = modified_date
        return self

    def set_last_activity_date(self, last_activity_date: str):
        self.__test_cycle.last_activity_date = last_activity_date
        return self

    def set_created_by(self, created_by: int):
        self.__test_cycle.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int):
        self.__test_cycle.modified_by = modified_by
        return self
    
    def set_fields(self, fields: dict):
        self.__test_cycle.fields = fields
        return self

    def get_element(self) -> TestCycle:
        return self.__test_cycle