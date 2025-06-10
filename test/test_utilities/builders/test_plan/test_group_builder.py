from jama_rest_client.model.test_plan import TestGroup
from typing_extensions import Self

class TestGroupBuilder:
    __test_group: TestGroup

    def __init__(self):
        self.__test_group = TestGroup()

    def set_id(self, id: int) -> Self:
        self.__test_group.id = id
        return self
    
    def set_name(self, name: str) -> Self:
        self.__test_group.name = name
        return self
    
    def set_assigned_to(self, assigned_to: int) -> Self:
        self.__test_group.assigned_to = assigned_to
        return self

    def get_element(self) -> TestGroup:
        return self.__test_group