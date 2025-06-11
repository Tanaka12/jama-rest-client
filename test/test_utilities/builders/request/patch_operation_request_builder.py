from jama_rest_client.model.request import PatchOperationRequest, PatchOperationType
from typing import Optional
from typing_extensions import Self

class PatchOperationRequestBuilder:
    __patch_operation_request: PatchOperationRequest

    def __init__(self):
        self.__patch_operation_request = PatchOperationRequest()

    def set_op(self, op: PatchOperationType) -> Self:
        self.__patch_operation_request.op = op
        return self
    
    def set_path(self, path: str) -> Self:
        self.__patch_operation_request.path = path
        return self
    
    def set_value(self, value: Optional[any]) -> Self:
        self.__patch_operation_request.value = value
        return self

    def get_element(self) -> PatchOperationRequest:
        return self.__patch_operation_request
    