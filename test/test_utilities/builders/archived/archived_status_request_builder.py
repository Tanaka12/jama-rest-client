from jama_rest_client.model.archived import ArchivedStatusRequest
from typing_extensions import Self

class ArchivedStatusRequestBuilder:
    __archived_status_request: ArchivedStatusRequest

    def __init__(self):
        self.__archived_status_request = ArchivedStatusRequest()

    def set_archived(self, archived: bool) -> Self:
        self.__archived_status_request.archived = archived
        return self

    def get_element(self) -> ArchivedStatusRequest:
        return self.__archived_status_request