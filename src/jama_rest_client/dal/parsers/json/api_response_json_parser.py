from jama_rest_client.model.api_response import AbstractRestResponse, CreatedResponse
from .page_info_json_parser import PageInfoJSONParser

class CreatedResponseJSONParser:

    @staticmethod
    def parse(created_response_dict: dict) -> CreatedResponse:
        created_response: CreatedResponse = CreatedResponse()
        created_response.status = created_response_dict['status']
        created_response.status_reason_phrase = created_response_dict['statusReasonPhrase']
        created_response.page_info = PageInfoJSONParser.parse(created_response_dict['pageInfo'])
        created_response.location = created_response_dict['location']
        created_response.id = created_response_dict['id']

        return created_response
    
class AbstractRestResponseJSONParser:

    @staticmethod
    def parse(abstract_rest_response_dict: dict) -> AbstractRestResponse:
        abstract_rest_response: AbstractRestResponse = AbstractRestResponse()
        abstract_rest_response.status = abstract_rest_response_dict['status']
        abstract_rest_response.status_reason_phrase = abstract_rest_response_dict['statusReasonPhrase']
        abstract_rest_response.page_info = PageInfoJSONParser.parse(abstract_rest_response_dict['pageInfo'])

        return abstract_rest_response