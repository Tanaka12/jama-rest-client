from datetime import datetime
from jama_rest_client.model.attachment import Attachment
from .lock_json_parser import LockJSONParser

class AttachmentJSONParser:

    @staticmethod
    def parse(attachment_dict: dict) -> Attachment:
        attachment: Attachment = Attachment()
        attachment.lock = LockJSONParser.parse(attachment_dict['lock'])
        attachment.file_name = attachment_dict['fileName']
        attachment.mime_type = attachment_dict['mimeType']
        attachment.file_size = attachment_dict['fileSize']
        attachment.id = attachment_dict['id']
        attachment.document_key = attachment_dict['documentKey']
        attachment.global_id = attachment_dict['globalId']
        attachment.project = attachment_dict['project']
        attachment.item_type = attachment_dict['itemType']
        attachment.created_date = datetime.fromisoformat(attachment_dict['createdDate'])
        attachment.modified_date = datetime.fromisoformat(attachment_dict['modifiedDate'])
        attachment.last_activity_date = datetime.fromisoformat(attachment_dict['lastActivityDate'])
        attachment.created_by = attachment_dict['createdBy']
        attachment.modified_by = attachment_dict['modifiedBy']
        attachment.fields = attachment_dict['fields']

        return attachment