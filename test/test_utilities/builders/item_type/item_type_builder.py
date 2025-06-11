from jama_rest_client.model.item_type import ItemType, ItemTypeCategory, ItemTypeField, ItemTypeFieldTextType, ItemTypeFieldType
from typing import List
from typing_extensions import Self

class ItemTypeFieldBuilder:
    __item_type_field: ItemTypeField

    def __init__(self):
        self.__item_type_field = ItemTypeField()

    def set_id(self, id: int) -> Self:
        self.__item_type_field.id = id
        return self
    
    def set_name(self, name: str) -> Self:
        self.__item_type_field.name = name
        return self
    
    def set_label(self, label: str) -> Self:
        self.__item_type_field.label = label
        return self
    
    def set_field_type(self, field_type: ItemTypeFieldType) -> Self:
        self.__item_type_field.field_type = field_type
        return self

    def set_read_only(self, read_only: bool) -> Self:
        self.__item_type_field.read_only = read_only
        return self

    def set_read_only_allow_api_overwrite(self, read_only_allow_api_overwrite: bool) -> Self:
        self.__item_type_field.read_only_allow_api_overwrite = read_only_allow_api_overwrite
        return self
    
    def set_required(self, required: bool) -> Self:
        self.__item_type_field.required = required
        return self
    
    def set_trigger_suspect(self, trigger_suspect: bool) -> Self:
        self.__item_type_field.trigger_suspect = trigger_suspect
        return self
    
    def set_synchronize(self, synchronize: bool) -> Self:
        self.__item_type_field.synchronize = synchronize
        return self
    
    def set_pick_list(self, pick_list: int) -> Self:
        self.__item_type_field.pick_list = pick_list
        return self

    def set_text_type(self, text_type: ItemTypeFieldTextType) -> Self:
        self.__item_type_field.text_type = text_type
        return self
    
    def set_item_type(self, item_type: int) -> Self:
        self.__item_type_field.item_type = item_type
        return self

    def get_element(self) -> ItemTypeField:
        return self.__item_type_field

class ItemTypeBuilder:
    __item_type: ItemType

    def __init__(self):
        self.__item_type = ItemType()

    def set_id(self, id: int) -> Self:
        self.__item_type.id = id
        return self
    
    def set_type_key(self, type_key: str) -> Self:
        self.__item_type.type_key = type_key
        return self
    
    def set_display(self, display: str) -> Self:
        self.__item_type.display = display
        return self
    
    def set_display_plural(self, display_plural: str) -> Self:
        self.__item_type.display_plural = display_plural
        return self
    
    def set_description(self, description: str) -> Self:
        self.__item_type.description = description
        return self
    
    def set_image(self, image: str) -> Self:
        self.__item_type.image = image
        return self

    def set_category(self, category: ItemTypeCategory) -> Self:
        self.__item_type.category = category
        return self
    
    def set_fields(self, fields: List[ItemTypeField]) -> Self:
        self.__item_type.fields = fields
        return self

    def set_system(self, system: bool) -> Self:
        self.__item_type.system = system
        return self

    def get_element(self) -> ItemType:
        return self.__item_type