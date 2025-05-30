from jama_rest_client.model.api_response import APICreateResponse, APIDeleteResponse, APIUpdateResponse

class APICreateResponseJSONParser:

    @staticmethod
    def parse(api_create_response_dict: dict) -> APICreateResponse:
        api_create_response: APICreateResponse = APICreateResponse()
        api_create_response.id = api_create_response_dict['id']
        api_create_response.status = api_create_response_dict['status']
        api_create_response.status_reason_phrase = api_create_response_dict['statusReasonPhrase']
        api_create_response.location = api_create_response_dict['location']

        return api_create_response
    
class APIUpdateResponseJSONParser:

    @staticmethod
    def parse(api_update_response_dict: dict) -> APIUpdateResponse:
        api_update_response: APIUpdateResponse = APIUpdateResponse()
        api_update_response.status = api_update_response_dict['status']
        api_update_response.status_reason_phrase = api_update_response_dict['statusReasonPhrase']

        return api_update_response
    
class APIDeleteResponseJSONParser:

    @staticmethod
    def parse(api_delete_response_dict: dict) -> APIDeleteResponse:
        api_delete_response: APIDeleteResponse = APIDeleteResponse()
        api_delete_response.status = api_delete_response_dict['status']
        api_delete_response.status_reason_phrase = api_delete_response_dict['statusReasonPhrase']

        return api_delete_response