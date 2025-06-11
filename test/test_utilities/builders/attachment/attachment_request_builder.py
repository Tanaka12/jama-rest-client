from jama_rest_client.model.attachment import AttachmentRequest
from typing_extensions import Self

class AttachmentRequestBuilder:
    __attachment_request: AttachmentRequest

    def __init__(self):
        self.__attachment_request = AttachmentRequest()

    def set_attachment(self, attachment: int) -> Self:
        self.__attachment_request.attachment = attachment
        return self
    
    def get_element(self) -> AttachmentRequest:
        return self.__attachment_request