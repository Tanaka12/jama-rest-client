from jama_rest_client.model.item_type import ItemType, ItemTypeField

class ItemTypeJSONParser:

    @staticmethod
    def parse(item_type_dict: dict) -> ItemType:
        item_type: ItemType = ItemType()
        item_type.id = item_type_dict['id']
        item_type.key = item_type_dict['typeKey']
        item_type.display = item_type_dict['display']
        item_type.display_plural = item_type_dict['displayPlural']
        item_type.description = item_type_dict['description']
        item_type.category = item_type_dict['category']

        for item_type_field in item_type_dict['fields']:
            item_type.fields.append(ItemTypeJSONParser.__parse_item_type_field(item_type_field))

        return item_type
    
    @staticmethod
    def __parse_item_type_field(item_type_field_dict: dict) -> ItemTypeField:
        item_type_field: ItemTypeField = ItemTypeField()

        item_type_field.id = item_type_field_dict['id']
        item_type_field.name = item_type_field_dict['name']
        item_type_field.label = item_type_field_dict['label']
        item_type_field.field_type = item_type_field_dict['fieldType']
        item_type_field.read_only = item_type_field_dict['readOnly']
        item_type_field.required = item_type_field_dict['required']
        item_type_field.trigger_suspect = item_type_field_dict['triggerSuspect']
        item_type_field.synchronize = item_type_field_dict['synchronize']
        item_type_field.text_type = item_type_field_dict['textType']

        return item_type_field
