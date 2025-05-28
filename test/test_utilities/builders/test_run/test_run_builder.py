from jama_rest_client.model.test_run import TestRun

class TestRunBuilder:
    __test_run: TestRun

    def __init__(self):
        self.__test_run = TestRun()

    def set_id(self, id: int):
        self.__test_run.id = id
        return self
    
    def set_document_key(self, document_key: str):
        self.__test_run.document_key = document_key
        return self
    
    def set_global_id(self, global_id: str):
        self.__test_run.global_id = global_id
        return self

    def set_project(self, project: int):
        self.__test_run.project = project
        return self

    def set_item_type(self, item_type: int):
        self.__test_run.item_type = item_type
        return self
    
    def set_created_date(self, created_date: str):
        self.__test_run.created_date = created_date
        return self
    
    def set_modified_date(self, modified_date: str):
        self.__test_run.modified_date = modified_date
        return self

    def set_last_activity_date(self, last_activity_date: str):
        self.__test_run.last_activity_date = last_activity_date
        return self

    def set_created_by(self, created_by: int):
        self.__test_run.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int):
        self.__test_run.modified_by = modified_by
        return self
    
    def set_test_case_version_number(self, test_case_version_number: int):
        self.__test_run.test_case_version_number = test_case_version_number
        return self
    
    def set_test_case_current_version_number(self, test_case_current_version_number: int):
        self.__test_run.test_case_current_version_number = test_case_current_version_number
        return self
    
    def set_sort_order_from_test_group(self, sort_order_from_test_group: int):
        self.__test_run.sort_order_from_test_group = sort_order_from_test_group
        return self
    
    def set_fields(self, fields: dict):
        self.__test_run.fields = fields
        return self

    def get_element(self) -> TestRun:
        return self.__test_run