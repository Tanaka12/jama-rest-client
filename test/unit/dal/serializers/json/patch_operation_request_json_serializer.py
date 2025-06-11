import pytest

from jama_rest_client.dal.serializers.json import PatchOperationRequestJSONSerializer
from jama_rest_client.model.request import PatchOperationRequest, PatchOperationType

from mocks.requests import RequestsMocks, REQUESTS_API_MOCKS
from test_utilities.builders.request import PatchOperationRequestBuilder

class TestTestPlanJSONParser():

    @pytest.mark.parametrize(
      "patch_operation_request, expected_patch_operation_request_dict",
      [
        (
            PatchOperationRequestBuilder().set_op(PatchOperationType.ADD)
                                          .set_path('/fields/element')
                                          .set_value(1)
                                          .get_element(),
            REQUESTS_API_MOCKS[RequestsMocks.CASE_PATCH_OPERATION_REQUEST_ADD]
        ),
        (
            PatchOperationRequestBuilder().set_op(PatchOperationType.REMOVE)
                                          .set_path('/fields/element')
                                          .set_value(None)
                                          .get_element(),
            REQUESTS_API_MOCKS[RequestsMocks.CASE_PATCH_OPERATION_REQUEST_DELETE]
        ),
        (
            PatchOperationRequestBuilder().set_op(PatchOperationType.REPLACE)
                                          .set_path('/fields/element')
                                          .set_value(1)
                                          .get_element(),
            REQUESTS_API_MOCKS[RequestsMocks.CASE_PATCH_OPERATION_REQUEST_REPLACE]
        )
      ]
    )
    def test_validate_happy_path_serialize_patch_operation_request_returns_expected_value(self, patch_operation_request: PatchOperationRequest, expected_patch_operation_request_dict: dict) -> None:
        patch_operation_request_dict = PatchOperationRequestJSONSerializer.serialize(patch_operation_request)
        assert expected_patch_operation_request_dict == patch_operation_request_dict