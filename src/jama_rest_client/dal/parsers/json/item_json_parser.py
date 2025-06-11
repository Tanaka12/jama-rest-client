from datetime import datetime
from jama_rest_client.model.item import Item
from .location_json_parser import LocationJSONParser
from .lock_json_parser import LockJSONParser

class ItemJSONParser:

    @staticmethod
    def parse(item_dict: dict) -> Item:
        item: Item = Item()
        item.id = item_dict['id']
        item.document_key = item_dict['documentKey']
        item.global_id = item_dict['globalId']
        item.item_type = item_dict['itemType']
        item.project = item_dict['project']
        item.child_item_type = item_dict['childItemType']
        item.created_date = ItemJSONParser.__parse_date_time(item_dict['createdDate'])
        item.modified_date = ItemJSONParser.__parse_date_time(item_dict['modifiedDate'])
        item.last_activity_date = ItemJSONParser.__parse_date_time(item_dict['lastActivityDate'])
        item.created_by = item_dict['createdBy']
        item.modified_by = item_dict['modifiedBy']
        item.lock = LockJSONParser.parse(item_dict['lock'])
        item.location = LocationJSONParser.parse(item_dict['location'])
        item.fields = item_dict['fields']

        return item
    
    @staticmethod
    def __parse_date_time(date_time: str) -> datetime:
        return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.000+0000')