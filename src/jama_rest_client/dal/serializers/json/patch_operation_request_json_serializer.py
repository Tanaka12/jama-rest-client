from jama_rest_client.model.request import PatchOperationRequest

class PatchOperationRequestJSONSerializer:

    @staticmethod
    def serialize(patch_operation_request: PatchOperationRequest) -> dict:
        patch_operation_request_dict: dict = {}
        patch_operation_request_dict['op'] = patch_operation_request.op.value
        patch_operation_request_dict['path'] = patch_operation_request.path

        if patch_operation_request.value is not None:
            patch_operation_request_dict['value'] = patch_operation_request.value

        return patch_operation_request