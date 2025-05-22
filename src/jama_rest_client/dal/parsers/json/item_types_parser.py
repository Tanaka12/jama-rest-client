
from jama_rest_client.model.item_type import ItemType, ItemTypeField

class ItemTypeParser:

    @staticmethod
    def parse(item_type_dict: dict) -> ItemType:
        item_type: ItemType = ItemType()
        item_type.id = item_type_dict['id']
        item_type.key = item_type_dict['typeKey']
        item_type.display = item_type_dict['display']
        item_type.displayPlural = item_type_dict['displayPlural']
        item_type.description = item_type_dict['description']
        item_type.category = item_type_dict['category']

        for item_type_field in item_type_dict['fields']:
            item_type.fields.append(ItemTypeParser.__parse_item_type_field(item_type_field))

        return item_type
    
    @staticmethod
    def __parse_item_type_field(item_type_field_dict: dict) -> ItemTypeField:
        item_type_field: ItemTypeField = ItemTypeField()

        item_type_field.id = item_type_field_dict['id']
        item_type_field.name = item_type_field_dict['id']
        item_type_field.label = item_type_field_dict['id']
        item_type_field.fieldType = item_type_field_dict['id']
        item_type_field.readOnly = item_type_field_dict['id']
        item_type_field.required = item_type_field_dict['id']
        item_type_field.triggerSuspect = item_type_field_dict['id']
        item_type_field.synchronize = item_type_field_dict['id']
        item_type_field.textType = item_type_field_dict['id']

        return item_type_field
