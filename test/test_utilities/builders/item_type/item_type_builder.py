from typing import List

from jama_rest_client.model.item_type import ItemType, ItemTypeField

class ItemTypeFieldBuilder:
    __item_type_field: ItemTypeField

    def __init__(self):
        self.__item_type_field = ItemTypeField()

    def set_id(self, id: int):
        self.__item_type_field.id = id
        return self
    
    def set_name(self, name: str):
        self.__item_type_field.name = name
        return self
    
    def set_label(self, label: str):
        self.__item_type_field.label = label
        return self
    
    def set_field_type(self, field_type: str):
        self.__item_type_field.field_type = field_type
        return self

    def set_read_only(self, read_only: bool):
        self.__item_type_field.read_only = read_only
        return self
    
    def set_required(self, required: bool):
        self.__item_type_field.required = required
        return self
    
    def set_trigger_suspect(self, trigger_suspect: bool):
        self.__item_type_field.trigger_suspect = trigger_suspect
        return self
    
    def set_synchronize(self, synchronize: bool):
        self.__item_type_field.synchronize = synchronize
        return self
    
    def set_text_type(self, text_type: str):
        self.__item_type_field.text_type = text_type
        return self

    def get_element(self) -> ItemTypeField:
        return self.__item_type_field

class ItemTypeBuilder:
    __item_type: ItemType

    def __init__(self):
        self.__item_type = ItemType()

    def set_id(self, id: int):
        self.__item_type.id = id
        return self
    
    def set_key(self, key: str):
        self.__item_type.key = key
        return self
    
    def set_display(self, display: str):
        self.__item_type.display = display
        return self
    
    def set_display_plural(self, display_plural: str):
        self.__item_type.display_plural = display_plural
        return self
    
    def set_description(self, description: str):
        self.__item_type.description = description
        return self

    def set_category(self, category: str):
        self.__item_type.category = category
        return self
    
    def set_fields(self, fields: List[ItemTypeField]):
        self.__item_type.fields = fields
        return self

    def get_element(self) -> ItemType:
        return self.__item_type