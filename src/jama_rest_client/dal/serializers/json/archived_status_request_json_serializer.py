from jama_rest_client.model.archived import ArchivedStatusRequest

class ArchivedStatusRequestJSONSerializer:

    @staticmethod
    def serialize(archived_status_request: ArchivedStatusRequest) -> dict:
        archived_status_request_dict: dict = {}
        archived_status_request_dict['archived'] = archived_status_request.archived 

        return archived_status_request_dict