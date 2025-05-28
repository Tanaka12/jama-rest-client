from jama_rest_client.model.item import Item, ItemLock, ItemLocation

class ItemJSONParser:

    @staticmethod
    def parse(item_dict: dict) -> Item:
        item: Item = Item()
        item.id = item_dict['id']
        item.document_key = item_dict['documentKey']
        item.global_id = item_dict['globalId']
        item.item_type = item_dict['itemType']
        item.project = item_dict['project']
        item.created_date = item_dict['createdDate']
        item.modified_date = item_dict['modifiedDate']
        item.last_activity_date = item_dict['lastActivityDate']
        item.created_by = item_dict['createdBy']
        item.modified_by = item_dict['modifiedBy']
        item.lock = ItemJSONParser.__parse_item_lock(item_dict['lock'])
        item.location = ItemJSONParser.__parse_item_location(item_dict['location'])
        item.fields = item_dict['fields']

        return item
    
    @staticmethod
    def __parse_item_lock(item_lock_dict: dict) -> ItemLock:
        item_lock: ItemLock = ItemLock()
        item_lock.locked = item_lock_dict['locked']
        item_lock.last_locked_date = item_lock_dict['lastLockedDate']

        return item_lock
    
    @staticmethod
    def __parse_item_location(item_location_dict: dict) -> ItemLocation:
        item_location: ItemLocation = ItemLocation()
        item_location.sort_order = item_location_dict['sortOrder']
        item_location.global_sort_order = item_location_dict['globalSortOrder']
        item_location.sequence = item_location_dict['sequence']

        return item_location
