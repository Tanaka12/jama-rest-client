import pytest

from jama_rest_client.dal.serializers.json import ArchivedStatusRequestJSONSerializer
from jama_rest_client.model.archived import ArchivedStatusRequest

from mocks.archived import ArchivedMocks, ARCHIVED_API_MOCKS
from test_utilities.builders.archived import ArchivedStatusRequestBuilder

class TestArchivedStatusRequestJSONSerializer():

    @pytest.mark.parametrize(
      "archived_status_request, expected_archived_status_request_dict",
      [
        (
            ArchivedStatusRequestBuilder().set_archived(False)
                                          .get_element(),
            ARCHIVED_API_MOCKS[ArchivedMocks.CASE_NO_ARCHIVED]
        ),
        (
             ArchivedStatusRequestBuilder().set_archived(True)
                                           .get_element(),
            ARCHIVED_API_MOCKS[ArchivedMocks.CASE_ARCHIVED]
        )
      ]
    )
    def test_validate_happy_path_serialize_patch_operation_request_returns_expected_value(self, archived_status_request: ArchivedStatusRequest, expected_archived_status_request_dict: dict) -> None:
        archived_status_request_dict = ArchivedStatusRequestJSONSerializer.serialize(archived_status_request)
        assert expected_archived_status_request_dict == archived_status_request_dict