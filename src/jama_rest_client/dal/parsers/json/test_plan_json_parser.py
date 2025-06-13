from datetime import datetime
from jama_rest_client.model.test_plan import TestPlan

class TestPlanJSONParser:

    @staticmethod
    def parse(test_plan_dict: dict) -> TestPlan:
        test_plan: TestPlan = TestPlan()
        test_plan.id = test_plan_dict['id']
        test_plan.document_key = test_plan_dict['documentKey']
        test_plan.global_id = test_plan_dict['globalId']
        test_plan.project = test_plan_dict['project']
        test_plan.item_type = test_plan_dict['itemType']
        test_plan.created_date = datetime.fromisoformat(test_plan_dict['createdDate'])
        test_plan.modified_date = datetime.fromisoformat(test_plan_dict['modifiedDate'])
        test_plan.last_activity_date = datetime.fromisoformat(test_plan_dict['lastActivityDate'])
        test_plan.created_by = test_plan_dict['createdBy']
        test_plan.modified_by = test_plan_dict['modifiedBy']
        test_plan.fields = test_plan_dict['fields']
        test_plan.archived = test_plan_dict['archived']

        return test_plan