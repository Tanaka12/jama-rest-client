from datetime import datetime
from jama_rest_client.model.attachment import Attachment
from jama_rest_client.model.lock import Lock
from typing_extensions import Self

class AttachmentBuilder:
    __attachment: Attachment

    def __init__(self):
        self.__attachment = Attachment()

    def set_file_name(self, file_name: str) -> Self:
        self.__attachment.file_name = file_name
        return self
    
    def set_mime_type(self, mime_type: str) -> Self:
        self.__attachment.mime_type = mime_type
        return self
    
    def set_file_size(self, file_size: int) -> Self:
        self.__attachment.file_size = file_size
        return self

    def set_id(self, id: int) -> Self:
        self.__attachment.id = id
        return self
    
    def set_document_key(self, document_key: str) -> Self:
        self.__attachment.document_key = document_key
        return self
    
    def set_global_id(self, global_id: str) -> Self:
        self.__attachment.global_id = global_id
        return self

    def set_project(self, project: int) -> Self:
        self.__attachment.project = project
        return self
    
    def set_item_type(self, item_type: int) -> Self:
        self.__attachment.item_type = item_type
        return self
        
    def set_created_date(self, created_date: datetime) -> Self:
        self.__attachment.created_date = created_date
        return self

    def set_modified_date(self, modified_date: datetime) -> Self:
        self.__attachment.modified_date = modified_date
        return self

    def set_last_activity_date(self, last_activity_date: datetime) -> Self:
        self.__attachment.last_activity_date = last_activity_date
        return self

    def set_created_by(self, created_by: int) -> Self:
        self.__attachment.created_by = created_by
        return self
    
    def set_modified_by(self, modified_by: int) -> Self:
        self.__attachment.modified_by = modified_by
        return self

    def set_lock(self, lock: Lock) -> Self:
        self.__attachment.lock = lock
        return self
    
    def set_fields(self, fields: dict) -> Self:
        self.__attachment.fields = fields
        return self

    def get_element(self) -> Attachment:
        return self.__attachment