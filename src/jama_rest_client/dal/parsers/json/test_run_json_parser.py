from jama_rest_client.model.test_run import TestRun

class TestRunJSONParser:

    @staticmethod
    def parse(test_run_dict: dict) -> TestRun:
        test_run: TestRun = TestRun()
        test_run.id = test_run_dict['id']
        test_run.document_key = test_run_dict['documentKey']
        test_run.global_id = test_run_dict['globalId']
        test_run.project = test_run_dict['project']
        test_run.item_type = test_run_dict['itemType']
        test_run.created_date = test_run_dict['createdDate']
        test_run.modified_date = test_run_dict['modifiedDate']
        test_run.last_activity_date = test_run_dict['lastActivityDate']
        test_run.created_by = test_run_dict['createdBy']
        test_run.modified_by = test_run_dict['modifiedBy']
        test_run.test_case_version_number = test_run_dict['testCaseVersionNumber']
        test_run.test_case_current_version_number = test_run_dict['testCaseCurrentVersionNumber']
        test_run.sort_order_from_test_group = test_run_dict['sortOrderFromTestGroup']
        test_run.fields = test_run_dict['fields']

        return test_run