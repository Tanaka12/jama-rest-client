import pytest

from jama_rest_client.dal.serializers.json import AttachmentRequestJSONSerializer
from jama_rest_client.model.attachment import AttachmentRequest

from mocks.attachments import AttachmentsMocks, ATTACHMENTS_API_MOCKS
from test_utilities.builders.attachment import AttachmentRequestBuilder

class TestAttachmentRequestJSONSerializer():

    @pytest.mark.parametrize(
      "attachment_request, expected_attachment_request_dict",
      [
        (
            AttachmentRequestBuilder().set_attachment(0)
                                      .get_element(),
            ATTACHMENTS_API_MOCKS[AttachmentsMocks.CASE_ATTACHMENT_REQUEST]
        )
      ]
    )
    def test_validate_happy_path_serialize_patch_operation_request_returns_expected_value(self, attachment_request: AttachmentRequest, expected_attachment_request_dict: dict) -> None:
        attachment_request_dict = AttachmentRequestJSONSerializer.serialize(attachment_request)
        assert expected_attachment_request_dict == attachment_request_dict