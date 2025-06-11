from jama_rest_client.model.test_plan import TestPlanRequest
from typing_extensions import Self

class TestPlanRequestBuilder:
    __test_plan_request: TestPlanRequest

    def __init__(self):
        self.__test_plan_request = TestPlanRequest()

    def set_project(self, project: int) -> Self:
        self.__test_plan_request.project = project
        return self
    
    def set_fields(self, fields: dict) -> Self:
        self.__test_plan_request.fields = fields
        return self
    
    def get_element(self) -> TestPlanRequest:
        return self.__test_plan_request