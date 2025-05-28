from jama_rest_client.model.test_cycle import TestCycle

class TestCycleJSONParser:

    @staticmethod
    def parse(test_cycle_dict: dict) -> TestCycle:
        test_cycle: TestCycle = TestCycle()
        test_cycle.id = test_cycle_dict['id']
        test_cycle.document_key = test_cycle_dict['documentKey']
        test_cycle.global_id = test_cycle_dict['globalId']
        test_cycle.item_type = test_cycle_dict['itemType']
        test_cycle.project = test_cycle_dict['project']
        test_cycle.created_date = test_cycle_dict['createdDate']
        test_cycle.modified_date = test_cycle_dict['modifiedDate']
        test_cycle.last_activity_date = test_cycle_dict['lastActivityDate']
        test_cycle.created_by = test_cycle_dict['createdBy']
        test_cycle.modified_by = test_cycle_dict['modifiedBy']
        test_cycle.fields = test_cycle_dict['fields']

        return test_cycle