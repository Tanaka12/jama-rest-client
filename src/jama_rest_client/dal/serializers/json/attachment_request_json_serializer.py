from jama_rest_client.model.attachment import AttachmentRequest

class AttachmentRequestJSONSerializer:

    @staticmethod
    def serialize(attachment_request: AttachmentRequest) -> dict:
        archived_status_request_dict: dict = {}
        archived_status_request_dict['attachment'] = attachment_request.attachment 

        return archived_status_request_dict