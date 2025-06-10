from jama_rest_client.model.test_plan import TestGroup

class TestGroupJSONParser:

    @staticmethod
    def parse(test_group_dict: dict) -> TestGroup:
        test_group: TestGroup = TestGroup()
        test_group.id = test_group_dict['id']
        test_group.name = test_group_dict['name']
        test_group.assigned_to = test_group_dict['assignedTo']

        return test_group