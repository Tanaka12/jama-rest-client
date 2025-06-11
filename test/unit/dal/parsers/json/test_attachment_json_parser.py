from datetime import datetime
import pytest

from jama_rest_client.dal.parsers.json import AttachmentJSONParser
from jama_rest_client.model.attachment import Attachment

from mocks.attachments import AttachmentsMocks, ATTACHMENTS_API_MOCKS
from test_utilities.builders.attachment import AttachmentBuilder
from test_utilities.builders.lock import LockBuilder

class TestAttachmentJSONParser():

    @pytest.mark.parametrize(
      "attachment_dict, expected_attachment",
      [
        (
            ATTACHMENTS_API_MOCKS[AttachmentsMocks.CASE_1_ELEMENT]['data'][0],
            AttachmentBuilder().set_file_name('DummyFileName 1')
                               .set_mime_type('DummyMimeType 1')
                               .set_file_size(0)
                               .set_id(1)
                               .set_document_key('DummyDocumentKey 1')
                               .set_global_id('DummyGlobalId 1')
                               .set_project(2)
                               .set_item_type(3)
                               .set_created_date(datetime.fromtimestamp(1582199426))
                               .set_modified_date(datetime.fromtimestamp(1582199426))
                               .set_last_activity_date(datetime.fromtimestamp(1582199426))
                               .set_created_by(4)
                               .set_modified_by(5)
                               .set_lock(
                                   LockBuilder().set_locked(False)
                                                .set_last_locked_date(datetime.fromtimestamp(1582199426))
                                                .set_locked_by(0)
                                                .get_element()
                               )
                               .set_fields(
                                  {
                                    'fieldStr': 'DummyField',
                                    'fieldInt': 0,
                                    'fieldBool': True
                                  }
                               )
                               .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_item_returns_expected_value(self, attachment_dict: dict, expected_attachment: Attachment) -> None:
        attachment = AttachmentJSONParser.parse(attachment_dict)
        assert expected_attachment == attachment