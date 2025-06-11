from jama_rest_client.model.item_type import ItemType, ItemTypeCategory, ItemTypeField, ItemTypeFieldType, ItemTypeFieldTextType

class ItemTypeJSONParser:

    @staticmethod
    def parse(item_type_dict: dict) -> ItemType:
        item_type: ItemType = ItemType()
        item_type.id = item_type_dict['id']
        item_type.type_key = item_type_dict['typeKey']
        item_type.display = item_type_dict['display']
        item_type.display_plural = item_type_dict['displayPlural']
        item_type.description = item_type_dict['description']
        item_type.image = item_type_dict['image']
        item_type.category = ItemTypeJSONParser.__parse_item_type_category(item_type_dict['category'])

        for item_type_field in item_type_dict['fields']:
            item_type.fields.append(ItemTypeJSONParser.__parse_item_type_field(item_type_field))

        item_type.system = item_type_dict['system']

        return item_type
    
    @staticmethod
    def __parse_item_type_category(item_type_category: str) -> ItemTypeCategory:
        if item_type_category == ItemTypeCategory.ATTACHMENT.value:
            return ItemTypeCategory.ATTACHMENT

        if item_type_category == ItemTypeCategory.COMPONENT.value:
            return ItemTypeCategory.COMPONENT
        
        if item_type_category == ItemTypeCategory.CORE.value:
            return ItemTypeCategory.CORE
        
        if item_type_category == ItemTypeCategory.DEFECT.value:
            return ItemTypeCategory.DEFECT
        
        if item_type_category == ItemTypeCategory.SECTION.value:
            return ItemTypeCategory.SECTION
        
        if item_type_category == ItemTypeCategory.SET.value:
            return ItemTypeCategory.SET
        
        if item_type_category == ItemTypeCategory.TEST_CASE.value:
            return ItemTypeCategory.TEST_CASE
        
        if item_type_category == ItemTypeCategory.TEST_CYCLE.value:
            return ItemTypeCategory.TEST_CYCLE
        
        if item_type_category == ItemTypeCategory.TEST_PLAN.value:
            return ItemTypeCategory.TEST_PLAN
        
        if item_type_category == ItemTypeCategory.TEST_RUN.value:
            return ItemTypeCategory.TEST_RUN
        
        if item_type_category == ItemTypeCategory.TEXT.value:
            return ItemTypeCategory.TEXT
        
        raise ValueError(f'ItemType category has an invalid value: {item_type_category}')

    @staticmethod
    def __parse_item_type_field(item_type_field_dict: dict) -> ItemTypeField:
        item_type_field: ItemTypeField = ItemTypeField()

        item_type_field.id = item_type_field_dict['id']
        item_type_field.name = item_type_field_dict['name']
        item_type_field.label = item_type_field_dict['label']
        item_type_field.field_type = ItemTypeJSONParser.__parse_item_type_field_type(item_type_field_dict['fieldType'])
        item_type_field.read_only = item_type_field_dict['readOnly']
        item_type_field.read_only_allow_api_overwrite = item_type_field_dict['readOnlyAllowApiOverwrite']
        item_type_field.required = item_type_field_dict['required']
        item_type_field.trigger_suspect = item_type_field_dict['triggerSuspect']
        item_type_field.synchronize = item_type_field_dict['synchronize']
        item_type_field.pick_list = item_type_field_dict['pickList']
        item_type_field.text_type = ItemTypeJSONParser.__parse_item_type_field_text_type(item_type_field_dict['textType'])
        item_type_field.item_type = item_type_field_dict['itemType']

        return item_type_field
    
    @staticmethod
    def __parse_item_type_field_text_type(item_type_field_text_type: str) -> ItemTypeFieldTextType:
        if item_type_field_text_type == ItemTypeFieldTextType.ATTACHMENT.value:
            return ItemTypeFieldTextType.ATTACHMENT

        if item_type_field_text_type == ItemTypeFieldTextType.KEY.value:
            return ItemTypeFieldTextType.KEY
        
        if item_type_field_text_type == ItemTypeFieldTextType.RICHTEXT.value:
            return ItemTypeFieldTextType.RICHTEXT
        
        if item_type_field_text_type == ItemTypeFieldTextType.TEXTAREA.value:
            return ItemTypeFieldTextType.TEXTAREA
        
        raise ValueError(f'ItemTypeField textType has an invalid value: {item_type_field_text_type}')

    @staticmethod
    def __parse_item_type_field_type(item_type_field_type: str) -> ItemTypeFieldType:
        if item_type_field_type == ItemTypeFieldType.ACTIONS.value:
            return ItemTypeFieldType.ACTIONS

        if item_type_field_type == ItemTypeFieldType.BOOLEAN.value:
            return ItemTypeFieldType.BOOLEAN
        
        if item_type_field_type == ItemTypeFieldType.CALCULATED.value:
            return ItemTypeFieldType.CALCULATED
        
        if item_type_field_type == ItemTypeFieldType.DATE.value:
            return ItemTypeFieldType.DATE
        
        if item_type_field_type == ItemTypeFieldType.DOCUMENT_TYPE.value:
            return ItemTypeFieldType.DOCUMENT_TYPE
        
        if item_type_field_type == ItemTypeFieldType.DOCUMENT_TYPE_CATEGORY_ITEM_LOOKUP.value:
            return ItemTypeFieldType.DOCUMENT_TYPE_CATEGORY_ITEM_LOOKUP
        
        if item_type_field_type == ItemTypeFieldType.DOCUMENT_TYPE_ITEM_LOOKUP.value:
            return ItemTypeFieldType.DOCUMENT_TYPE_ITEM_LOOKUP
        
        if item_type_field_type == ItemTypeFieldType.GROUP.value:
            return ItemTypeFieldType.GROUP
        
        if item_type_field_type == ItemTypeFieldType.INTEGER.value:
            return ItemTypeFieldType.INTEGER
        
        if item_type_field_type == ItemTypeFieldType.LOOKUP.value:
            return ItemTypeFieldType.LOOKUP
        
        if item_type_field_type == ItemTypeFieldType.MULTI_LOOKUP.value:
            return ItemTypeFieldType.MULTI_LOOKUP
        
        if item_type_field_type == ItemTypeFieldType.PROJECT.value:
            return ItemTypeFieldType.PROJECT
        
        if item_type_field_type == ItemTypeFieldType.RELATIONSHIP_STATUS.value:
            return ItemTypeFieldType.RELATIONSHIP_STATUS
        
        if item_type_field_type == ItemTypeFieldType.RELATIVE_DATE_RANGE.value:
            return ItemTypeFieldType.RELATIVE_DATE_RANGE
        
        if item_type_field_type == ItemTypeFieldType.RELEASE.value:
            return ItemTypeFieldType.RELEASE
        
        if item_type_field_type == ItemTypeFieldType.ROLLUP.value:
            return ItemTypeFieldType.ROLLUP
        
        if item_type_field_type == ItemTypeFieldType.STEPS.value:
            return ItemTypeFieldType.STEPS
        
        if item_type_field_type == ItemTypeFieldType.STRING.value:
            return ItemTypeFieldType.STRING

        if item_type_field_type == ItemTypeFieldType.TEST_CASE_STATUS.value:
            return ItemTypeFieldType.TEST_CASE_STATUS
        
        if item_type_field_type == ItemTypeFieldType.TEST_RUN_STATUS.value:
            return ItemTypeFieldType.TEST_RUN_STATUS
        
        if item_type_field_type == ItemTypeFieldType.TEXT.value:
            return ItemTypeFieldType.TEXT
        
        if item_type_field_type == ItemTypeFieldType.TIME.value:
            return ItemTypeFieldType.TIME
        
        if item_type_field_type == ItemTypeFieldType.URL_STRING.value:
            return ItemTypeFieldType.URL_STRING
        
        if item_type_field_type == ItemTypeFieldType.USER.value:
            return ItemTypeFieldType.USER
        
        raise ValueError(f'ItemTypeField fieldType has an invalid value: {item_type_field_type}')
