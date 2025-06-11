from jama_rest_client.model.test_plan import TestPlanRequest

class TestPlanRequestJSONSerializer:

    @staticmethod
    def serialize(test_plan_request: TestPlanRequest) -> dict:
        test_plan_request_dict: dict = {}
        test_plan_request_dict['project'] = test_plan_request.project
        test_plan_request_dict['fields'] = test_plan_request.fields

        return test_plan_request_dict